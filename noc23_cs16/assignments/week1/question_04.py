#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 10:28:55 2023

@author: ram

Question:
How many times is the comparison i <= n performed in the following program?

int i = 60, n = 300;
main(){
  while (i <= n){
    i = i+2;
    n = n-3; 
  }
}    

"""
i=60
n=300
count=0
while(i <= n):
    i += 2
    n -= 3
    count+= 1

print('Count: '+str(count))    

# The output is 49 but it would have taken an extra check to come out of the loop
# Hence it is 50
