#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
num = 5;
print("Factorial of",num,"is",
factorial(num))


# In[2]:


num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           print(i,"times",num//i,"is",num)  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  


# In[5]:


def ispalindrome(s):
    return s == s[::-1]
 
 

s = input('enter the string : ')
ans = ispalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")


# In[6]:


def pythagoras(opposite_side,adjacent_side,hypotenuse):
        if opposite_side == str("x"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent_side**2))**0.5))
        elif adjacent_side == str("x"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite_side**2))**0.5))
        elif hypotenuse == str("x"):
            return ("Hypotenuse = " + str(((opposite_side**2) + (adjacent_side**2))**0.5))
        else:
            return "You know the answer!"
    
print(pythagoras(3,4,'x'))
print(pythagoras(3,'x',5))
print(pythagoras('x',4,5))
print(pythagoras(3,4,5))


# In[7]:


x=input('enter the string')
freq = {}
  
for i in x:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print ("Count of all characters is :\n "+  str(freq))


# In[ ]:




