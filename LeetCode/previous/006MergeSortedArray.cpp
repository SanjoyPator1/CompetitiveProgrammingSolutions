#include<bits/stdc++.h>
using namespace std;

 
void
rev (vector < int >&a, int m) 
{
  
for (int i = 0; i < m / 2; i++)
    
swap (a[i], a[m - i - 1]);

} 
void

merge (vector < int >&a, int m, vector < int >&b, int n) 
{
  
 
int i, j = 0, pos = 0;
  
rev (a, m);
  
reverse (a.begin (), a.end ());
  
i = n;
  
while (i < m + n && j < n)
    
    {
      
if (a[i] > b[j])
	
	{
	  
a[pos] = b[j];
	  
j++;
	
}
      
      else
	
	{
	  
a[pos] = a[i];
	  
i++;
	
}
      
pos++;
    
}
  
while (i < m + n)
    
    {
      
a[pos] = a[i];
      
pos++;
      
i++;
    
}
  
while (j < n)
    
    {
      
a[pos] = b[j];
      
j++;
      
pos++;
    
}

}


 
 
int
main () 
{
  
 
 
int in, out;
  
    // cin >> in;
    
    // out = in * 2;
    
    // cout << "The output is " << out << endl;
  
vector < int >a = { 1, 2, 3, 0,0,0 };
  
vector < int >b = { 2,5,6 };
  
 
merge (a, a.size ()-b.size(), b, b.size ());
  
 
for (int i = 0; i < a.size (); i++)
    {
      
cout << "The ans is " << a[i] << endl;

} 
 
 
 
}

