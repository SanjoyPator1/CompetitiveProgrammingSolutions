#include <bits/stdc++.h>
using namespace std;

class Node
{

public:
    int data;
    Node *next;

    // constructor
    Node(int data)
    {
        this->data = data;
        this->next = NULL;
    }

    // destructor
    ~Node()
    {
        int value = this->data;
        // memory free
        if (this->next != NULL)
        {
            delete next;
            this->next = NULL;
        }

        cout << "Memory is free for node with data " << value << endl;
    }
};

void insertAtHead(Node *&head, int d)
{

    // new node create
    Node *temp = new Node(d);
    temp->next = head;
    head = temp;
}

void insertAtTail(Node *&tail, int d)
{

    // new node create
    Node *temp = new Node(d);
    tail->next = temp;
    tail = temp;
}

void insertAtPosition(Node *&tail, Node *&head, int d, int position)
{
    // edge case- position = 1
    if (position == 1)
    {
        cout << "insert at pos 1 edge case" << endl;
        insertAtHead(head, d);
        return;
    }

    // traverse to the postion
    Node *temp = head;
    int count = 1;

    while (count < (position - 1))
    {
        temp = temp->next;
        count++;
    }

    // edge case check if temp is the last position and we have to add node after that
    if (temp->next == NULL)
    {
        cout << "insert at pos last edge case" << endl;
        insertAtTail(tail, d);
        return;
    }

    // passed all test case now insert in position
    Node *nodeToInsert = new Node(d);
    nodeToInsert->next = temp->next;
    temp->next = nodeToInsert;
}

void deleteNode(Node *&tail, Node *&head, int position)
{

    // deleting first or start node - EDGE case
    if (position == 1)
    {
        Node *temp = head;
        head = head->next;
        // memory free start node
        temp->next = NULL;
        delete temp;
    }
    else
    {
        // deleting any middle node or last node
        Node *current = head;
        Node *previous = NULL;

        int count = 1;
        // just for traversing
        while (count < position)
        {
            previous = current;
            current = current->next;
            count++;
        }
        // pointer movement
        previous->next = current->next;
        current->next = NULL;
        delete current;

        // move tail pointer if deletion was last node
        if (previous->next == NULL)
        {
            tail = previous;
        }
    }
}

void print(Node *&head)
{
    Node *temp = head;

    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl;
}

int main()
{
    cout << "Singly Linked List" << endl;

    // create d a new node
    Node *node1 = new Node(10); // [10]
    // cout << node1->data << endl;
    // cout << node1->next << endl;

    // head pointed to node1
    Node *head = node1;
    Node *tail = node1;
    print(head);

    insertAtHead(head, 5); //[5] [10]
    print(head);

    insertAtTail(tail, 15); // [5] [10] [15]
    print(head);

    insertAtPosition(tail, head, 2, 1);  // insert at beginning -edge case  // [2] [5] [10] [15]
    insertAtPosition(tail, head, 20, 5); // insert at end -edge case     // [2] [5] [10] [15] [20]
    insertAtPosition(tail, head, 15, 3); // insert at middle position   // [2] [5] [15] [10] [15] [20]

    print(head);

    // deletion
    deleteNode(tail, head, 1); // After deletion 1st position   //  [5] [15] [10] [15] [20]
    deleteNode(tail, head, 3); // After deletion 3rd position   //  [5] [15] [15] [20]
    deleteNode(tail, head, 4); // After deletion 4th i.e last position   //  [5] [15] [15]

    print(head);

    // check head and tail
    cout << "Head : " << head->data << endl;
    cout << "Tail : " << tail->data << endl;

    return 0;
}
