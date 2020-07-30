#include <iostream>
#include <cstddef>
using namespace std;
class Node
{
public:
    int data;
    Node *next;
    Node(int d){
        data=d;
        next=NULL;
    }
};
class Solution{
public:

    Node *last = NULL;
    Node* insert(Node *head,int data)
    {
        //Complete this method
        Node* t = new Node(data);
        Node* h = head;
        t->next = NULL;

        if(h == NULL){
            h = last = t;
        }else{
            last-> next = t;
            last = t;
        }
        return h;
    }

    void display(Node *head)
    {
        Node *start=head;
        while(start)
        {
            cout<<start->data<<" ";
            start=start->next;
        }
    }
};
int main()
{
    Node* head=NULL;
    Solution mylist;
    int T,data;
    cin>>T;
    while(T-->0){
        cin>>data;
        head=mylist.insert(head,data);
    }
    mylist.display(head);

}
