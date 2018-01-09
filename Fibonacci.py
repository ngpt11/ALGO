# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 22:20:19 2018

@author: naman
"""
# using simple technique for creating Fibonacci. Has exponential time complexity.
def fib(n):
    if(n==0 or n ==1):
        return n;
    else:
        return fib(n-1) + fib(n-2);

print(fib(6)); 

# using array to store intermediate  results 
farray= []; 
def fibarray(n):
    farray= [0,1];
    for i in range(1,n+1):    
        if (i==0 or i==1):
            continue;
        else:
            c= farray[i-1] + farray[i-2];
            farray.append(c);      
    return farray[n];       # return of function is required else function return none.

print(fibarray(6));
