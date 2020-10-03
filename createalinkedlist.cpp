#include<bits/stdc++.h>
using namespace std;
struct node{
	int data;
	node *next;
}*head,*first,*temp;
void create()
{
  int n;
  cout<<"length of linked list should be of"<<endl;	
  cin>>n;
 for(int i =0;i<n;i++)
 {
 	node*temp = new node();
 	cout<<"enter"<<i+1<<"data in linked list"<<endl;
 	cin>>temp->data;
 	 temp->next = 0;
 	 if(i==0)
 	 temp = head=first;
 	 else
 	 {
 	 	first->next= temp;
 	 	first = temp;
	  }
 }
 for(int i =0;i<n;i++)
 {cout<<head->data;
    head = head->next;
 }
}
void deletee()
{ cout<<"enter the data that you want to delete?";
int n;
cin>>n;
	temp=first=head;
	temp=temp->next;
	while(temp->next!=0)
	{   
		temp=temp->next;
		first=first->next;
		if(temp->data==n)
		  {
		  	temp=temp->next;
		  	first->next=temp;
		  }
	}
	
}
int main()
{
	int n;
	cout<<"enter total operations that you want to perform"<<endl;
	cin>>n;
	while(n--)
	{
		int t;
		cout<<"which operation you want to perfrom"<<endl;
		cin>>t;
		if(t==1)
		{
			create();
		}
		if(t==2)
		{
		    deletee();
		}
	}
	
	
}
