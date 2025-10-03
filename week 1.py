#program to add , delete and display grocery items using dictionary
grocery={}
while True:
    choice=int(input("""Enter Operation to be performed:
    1.add
    2.delete
    3.display"""))
    if choice== 1:
        item=input("Enter item to be added ")
        value=int(input("Enter weight in kgs"))
        grocery[item]=value
        print(f"{item} kg added.")
    elif choice == 2:
        item=input("Enter item to be deleted")
        if item in grocery:
            grocery.pop(item)
            print(f"{item} {value} deleted.")
        else :
            print(f"{item} not in list")
    elif choice==3:
        for item,weight in grocery.items():
            print(f"{item}: {weight} kg")
    else :
        print("Invalid choice")
        break
    
    
#program to add,delete and display items in a grocery list
grocery=[]
while True:
    choice=int(input("""Enter Operation to be performed:
    1.add
    2.delete
    3.display"""))
    if choice== 1:
        item=input("Enter item to be added")
        grocery.append(item)
        print(f"{item} added.")
    elif choice == 2:
        item=input("Enter item to be deleted")
        if item in grocery:
            grocery.remove(item)
        else :
            print(f"{item} not in list")
    elif choice==3:
        for list in grocery:
            print(list," ")
    else :
        print("Invalid choice")
        break
    
# WAP to find an element in the array
def find_element(arr,l,key):
    for i in range(l):
        if arr[i]==key:
            return i
    return -1

arr = [1,5,13,66,85,33]
key = 88
l=len(arr)
    
index = find_element(arr,l,key)
if index != -1:
    print(" index at which element 88 :",str(index+1)) 
else :
    print("element not in the array")
    
#WAP to inseet an element in the array
def insert_at_end(arr,key):
    arr.append(key)
arr= [5,1,4,2,6]
key=3

print("array before insertion of new element:",arr)
insert_at_end(arr,key)
print("array after insertion of new element:",arr)  

# Python program for inserting an element in an unsorted array

def insertEnd(arr, element):
    arr.append(element)

arr = [12, 16, 20, 40, 50, 70]
key = 26

print("Before Inserting: ")
print(arr)

insertEnd(arr, key)
print("After Inserting: ")
print(arr)

def flargest(arra):
    lar = arra[0]
    for i in arra:
        if i > lar:
            lar = i
    return lar

arra = [1,5,4,3]
largest = flargest(arra)
print("largest number is:", largest)


#Write a function def count_vowels(s): that counts how many vowels are in a given string s.

def count(s):
    num=0
    vowels=['a','e','i','o','u']
    s=s.lower()
    for i in s:
        num+=1 if i in vowels else 0
    print(num)
count("hello world")

#program to guess random number
import random
comp=random.randint(1,10)
num=1
while num>=1 and num<=10:
    n=int(input("Enter a number: "))
    if n== comp:
        print("You guessed it right!!")
    else :
        print("Try again!!")
        continue

#program to check whether the number is prime or not
def prime_num(num):
    for i in range(2,int((num/2)+1)):
        if num % i==0:
            return False
    return True

n=int(input("Enter number: "))
if prime_num(n):
    print(f"{n} is prime.")
else :
    print(f"{n} is not prime.")
    
# WAP to print  pattern
k=int(input("Enter a number: "))
for i in range(k):
    for j in range(k):
        if i==0 or i==k-1 or j==0 or j==k-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

# WAP to print  pattern
k=int(input("Enter a number: "))
for i in range(k):
    for j in range(k):
        if i==0 or i==k-1 or j==0 or j==k-1:
            print("*",end=" ")
        elif i==j or i+j==k-1:
            print("$",end=" ")
        else:
            print(" ",end=" ")
    print()

#WAP to print right angled pattern with stars
k=int(input("Enter a number: "))
for i in range(k+1):
    print("*" * i)
    
#WAP to print a reverse right angled traingle with numbers
k=int(input("Enter a number: "))
for i in range(k):
    for j in range(k):
        if i>j:
            print(" ",end=" ")
        else:
            print(j+1,end=" ")
    print()