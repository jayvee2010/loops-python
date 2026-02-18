#experiment no.7
#name:jayvee shah
#prn:25070123058
#entc a3

#program to demonstrate loops in python
#numbers from 1 to 5 using for loop
for i in range(1, 6):
    print(i)

n=int(input("Enter a number to print upto "))
for i in range(1,n+1):
    print(i,end= " ")

#take input of a number and print its factorial
fact=1
x=int(input("\n enter a number to print its factorial "))
for i in range(1,x+1):
    fact=fact*i
print(fact)

#fibonacci series
n=int(input("Enter the number of terms in the Fibonacci series "))
a=0
b=1
c=a+b
for i in range(n):
    print(a,end=" ")
    c=a+b
    a,b=b,c

#reverse a number
num=int(input("\n enter a number to reverse "))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

#check palindorm string
str=input("enter a string to check palindrome ")
i=0
j=len(str)-1
while str[i]==str[j] and i<j:
    i+=1
    j-=1
if i>=j:
    print("palindrome")
else: 
    print("not palindrome")

#check palindrome string
str=input("enter a string to check palindrome ")
if str==str[::-1]:
    print("palindrome")
else:
    print("not palindrome") 

#count digits in a number
num=int(input("enter a number to count digits "))
count=0
while num>0:
    num=num//10
    count+=1
print(count)
 

 #break statement

 #exit loop when i is 3
for i in range(1,6):
    if i==3:
        break
    print(i)

#search an element in a list adn print the position of the element
lst=[10,20,30,40,50]
x=int(input("enter a number to search in the list "))
for i in lst:
    if i==x:
        print("found, position is ",lst.index(i))
        break
else:
    print("not found")

#print numbers from 1 to 10
i=1
while i<=10:
    if i==5:
        i+=1
        continue
    print(i)
    i+=1  

#print only odd numbers from 1 to 10
i=1
while i<=10:
    if i%2==0:
        i+=1
        continue
    print(i)
    i+=1

#for loop
for a in range(1,6):
    print(a)

#print even using for
for x in range(0,11,2):
    print(x,end=" ")

for i in range(1,4):
    for j in range(1,4):
        print(i,j)  

#a=[[1,2,3],[4,5,6],[7,8,9]]
#for i in range(4):
    #for j in range(4):
        #print(a[i][j],end=" ")
    #print() 


a=[[1,2,3],[4,5,6],[7,8,9]]
b=[[9,8,7],[6,5,4],[3,2,1]]
result=[[0,0,0],[0,0,0],[0,0,0]] 
for i in range(3):
    for j in range(3):
        for k in range(3):
            result[i][j]+=a[i][k]*b[k][j]
print("product of matrices:")
for i in range(3):
    for j in range(3):
        print(result[i][j],end=" ")
    print()



#python program to accept three digits and print all possible combinations from the digits
digits=input("enter three digits ")
for i in range(len(digits)):
    for j in range(len(digits)):
        for k in range(len(digits)):
            if i!=j and j!=k and i!=k:
              print(digits[i],digits[j],digits[k])

#armstrong number
num=int(input("enter a number to check armstrong "))
sum=0
len1=len(str(num))
for i in str(num):
    sum+=int(i)**len1
print(sum)

#prime number
num=int(input("enter a number to check if its prime"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("it is not prime")
            break
    else:
        print("it is prime")

n=5
for i in range (n):
    print(i*' '+" *"*(n-i)) 

#hourglass 
n=6
for i in range (n):
    print(i*' '+" *"*(n-i)) 
for i in range (1,n):
    print((n-i-1)*' '+" *"*(i+1))

#floyds triange
n=4
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()



