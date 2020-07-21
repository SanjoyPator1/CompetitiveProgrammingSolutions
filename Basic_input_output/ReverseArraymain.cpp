/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;



int
main ()
{
  int n;
  int arr[n];

  cin >> n;

  if (n >= 1 && n <= 1000)
    {				//contraint 1 satisfied ---> total number of elements

      int i = 0;

      //input
      while (i < n)
	{

	  int num;
	  cin >> num;

	  if (num >= 1 && num <= 10000)
	    {			//constraint 2 satisfied ---> input number range
	      arr[i] = num;
	      i++;

	    }			//closing brace for if - 2nd
	}

      while (n--)
	cout << arr[n] << " ";	//without this format - segmentation fault


    }				//closing brace for if - 1st



  return 0;
}
