#28/03/2023
#All this exercise are from PYnative
#Exercise 1: Calculate the multiplication and sum of two numbers
def sum(a,b):
    sum = a + b
    return sum

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
# sum(a,b)
summation = sum(a,b)

def multiply(a,b):
    multiply = a * b
    return multiply
mul = multiply(a,b)

if mul <= 1000:
    print(mul)
else:
    print(summation)

#Exercise 2: Print the sum of the current number and the previous number
num = int(input("Enter a number: "))
previous_num = 0
for i in range (num):
    print(f"current number {i} previous number {previous_num} sum: {i+ previous_num}")
    previous_num = i
    
#Exercise 3: Print characters from a string that are present at an even index number
strig = input("Enter a string: ")
lst = []
for i in strig:
    lst.append(i)
print(lst)
index = 0
for i in lst:
    if index % 2 == 0:
        print(i)
    index = index + 1
#or
word = input("Enter a word: ")
length = len(word)
for i in range(0,length-1,2):
    print(f"The even word at index {i} is {word[i]}")


#Exercise 4: Remove first n characters from a string
def remove_chars(word,number):
    print("Original string is:", word)
    x = word[number:]
    return x
    

word = input("Enter a word: ")
number = int(input("Enter a number: "))

removed = remove_chars(word,number)
print(removed)

#Exercise 5: Check if the first and last number of a list is the same
def check(x):
    if x[0] == x[-1]:
        return True
    else:
        return False
x = [10,20,30,40,30]
print(f"The result is {check(x)}")
      
#Exercise 6: Display numbers divisible by 5 from a list
def div(user):
    out_lst = []
    lst = []
    for i in range(0, len(user), 2):
        num = int(user[i]) * 10 + int(user[i+1])
        lst.append(num)
    
    
    for i in lst:
        if i % 5 == 0:
            out_lst.append(i)
    return out_lst

user = input("Enter a list: ")
print(f"Dividible by 5: {div(user)}")

#Exercise 7: Return the count of a given substring from a string
def count(strg, sub):
    count = 0
    for i in range(0,len(strg) + 1):#0,19
        if strg[i: len(sub) + i] == sub:#(0:7)
            count = count + 1
    return count

strg = input("Enter a string: ")
sub = input("Enter a sub string: ")
print(f"{sub} appeared {count(strg,sub)} times")

#Exercise 8: Print the following pattern
for x in range(1,6):
    for y in range(x):
        print(x,end = " ")
    print("\n")


#Exercise 9: Check Palindrome Number
number = input("Enter a number: ")
for i in number:
    if number[0] == number[-1]:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")
    break


#Exercise 10: Create a new list from a two list using the following condition
#Create a new list from a two list using the following condition
#Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
n = int(input("Enter the number of elements you want to add: "))
lst_one = []
for i in range(0,n):
    number = int(input("Enter the element: "))
    lst_one.append(number)
print(lst_one)

nn = int(input("Enter the number of elements you want to add: "))
lst_two = []
for i in range(0,nn):
    numberr = int(input("Enter the element: "))
    lst_two.append(numberr)
print(lst_two)

if nn > n:
    r_n = nn
else:
    r_n = n

new_lst = []
for i in range(0, r_n):
    if lst_one[i] % 2 != 0:
        new_lst.append(lst_one[i])

for i in range(0,r_n):
    if lst_two[i] % 2 == 0:
        new_lst.append(lst_two[i])
        
print(new_lst)


#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
n = input("Enter a number: ")
for i in range(1,len(n) + 1):
    print(n[-i], end=" ")

#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
n = 1234
while n > 0:
    dig = n % 10
    n = n // 10
    print(dig, end = " ")

#
n = int(input("Enter a number: "))
tw_two = n * 0.2222
tw_twoo = n * 0.2222
fi_si = n * 0.5556
print(tw_two*0 + tw_twoo * 0.1 + fi_si * 0.20)

# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:

# For example, suppose the taxable income is 45000 the income tax payable is

# 10000*0% + 10000*10%  + 25000*20% = $6000.
n = int(input("Enter the amount: "))
tax_payable = 0
if n <= 10000:
    tax_payable = 0
elif n <= 20000:
    x = n - 10000
    tax_payable = x * 10/100
else:
    tax_payable = 0

    tax_payable = 10000 * 10/100

    tax_payable = tax_payable + (n - 20000) * 20/100

print(f"The total tax is {tax_payable} ")

#Exercise 13: Print multiplication table form 1 to 10
for i in range(1,10):
    for j in range(1,11):
        print(i*j,end=" ")
    print("\t\t")

#Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\t\t")


#xercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    answer = base**exp
    return answer



base = int(input("Enter a number:"))
exp = int(input("Enter a number:"))
exponent(base,exp)
print(f"{base} raises to the power of {exp}: {base**exp}")


##Python loop and control statements
#Exercise 1: Print First 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i = i + 1

#Exercise 2: Print the following pattern
#Write a program to print the following number pattern using a loop.
n = 5
for i in range(0,n):
    for j in range(1,i+2,1):
        print(j, end=" ")
    print()

#Exercise 3: Calculate the sum of all numbers from 1 to a given number
n = int(input("Enter a number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
    i = i + 1
print(f"Sum is {sum}")

#Exercise 4: Write a program to print multiplication table of a given number
num = int(input("Enter a number = "))
for i in range(1,11):
    print(f"{num * i}")

#Exercise 5: Display numbers from a list using loop
lst = []
number = int(input("Enter nu. of elements: "))
for i in range(number):
    num = int(input("Enter element for list: "))
    lst.append(num)
print(lst)

for i in range(len(lst)):
    if lst[i] > 500:
        break
    elif lst[i] > 150:
        continue
    elif lst[i] % 5 == 0:
        print(lst[i])

#xercise 6: Count the total number of digits in a number
number = int(input("Enter the number: "))#75689
count = 0
while number > 0:
    # digit = number % 10#9
    number = number // 10#7568
    count = count + 1
print(count)

#Exercise 7: Print the following pattern
for i in range(5):
    for j in range(5-i, 0,-1):
        print(j,end=" ")
    print()

#Exercise 8: Print list in reverse order using a loop
lst = []
number = int(input("Enter the number of elements: "))
for i in range(number):
    num = int(input("Enter the elements: "))
    lst.append(num)
print(lst)
for i in range(number-1,-1,-1):
    print(lst[i])

#Exercise 9: Display numbers from -10 to -1 using for loop
for i in range(-10,0,1):
    print(i)

#Exercise 10: Use else block to display a message “Done” after successful execution of for loop
for i in range(5):
    print(i)
else:
    print("Done!")

#Exercise 11: Write a program to display all prime numbers within a range
start = 25
end = 50
for num in range(start,end+1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)

#29/03/2023
#Exercise 12: Display Fibonacci series up to 10 terms
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
#Sum will go in b and previous will go in a
a = 0
b = 1
for i in range(10):
    print(a,end=" ")
    sum = a + b#1
    a = b
    b = sum

#Exercise 13: Find the factorial of a given number
n = 5
fact = 1
for i in range(n,0,-1):
    fact = fact * i

print(f"{n}! = ",end=" ")
for i in range(n,0,-1):
    print(i,end="")
    if i != 1:
        print(" x ",end="")
    else:
        print(f" = {fact}")

#Exercise 14: Reverse a given integer number
n = 76542
rev_num = 0
while n != 0:
    num = n % 10 #2 4
    rev_num = rev_num*10 + num #24
    n = n // 10#7654 765
print(rev_num)

#Exercise 15: Use a loop to display elements from a given list present at odd index positions
number = int(input("Enter number of elements: "))
lst = []
for i in range(number):
    num = int(input("Enter element: "))
    lst.append(num)

for i in range(0,number):
    if i % 2 != 0:
        print(lst[i],end=" ")

#Exercise 16: Calculate the cube of all numbers from 1 to a given number
num = int(input("Enter number: "))
for i in range(1,num+1):
    print(f"Current Number is : {i} and the cube is {i*i*i}")

#Exercise 17: Find the sum of the series upto n terms
start = 2
sum  = 0
n = int(input("Enter a number: "))
for i in range(n):
    #print(start,end=" + ")
    sum = sum + start
    start = start * 10 + 2
print(sum)

#Exercise 18: Print the following pattern
for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print()
    
for i in range(5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

#The following pattern questions are from quescol.com
#1
for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

#2
for i in range(5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

#3
for i in range(5):

    for j in range(i):
        print(" ",end="")
    
    for k in range(5-i):
        print("*",end="")
    print()

#4
for i in range(1,6):
    for j in range(1,i+1):#2
        print(j,end=" ")
    print()

#5
for i in range(5):
    for j in range(5,i,-1):
        print(" ",end="")
    

    for k in range(i):
        print("*",end="")
    
    for l in range(i+1):
        print("*",end="")
    print()

#6
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


#7
for i in range(5):
    for j in range(i+1):
        print(" ",end="")

    for k in range(5,i,-1):
        print("*",end=" ")   
    print()

#8 Again see this
n = 4  # number of rows
num = 0 # starting number

for i in range(1, n+1):        # loop for each row
    for j in range(n-i):      # print spaces
        print(" ", end="")
        
    for j in range(1, 2*i):   # print numbers
        if j <= i:           # increasing sequence
            num += 1
            print(num, end="")
        else:                # decreasing sequence
            num -= 1
            print(num, end="")
    
    num += 1                  # update starting number for next row
    print()                   # print newline after each row

# Explanation:

# The variable n holds the number of rows in the pattern.
# The variable num holds the starting number for each row, which is updated after each row is printed.
# The outer loop iterates over each row, from 1 to n.
# The first inner loop prints the spaces before each row, which depends on the current row number and the total number of rows.
# The second inner loop prints the sequence of numbers in each row, which consists of an increasing sequence followed by a decreasing sequence.
# The if statement inside the loop checks whether we are in the increasing or decreasing sequence, based on the current value of j.
# If j is less than or equal to i, we are in the increasing sequence, so we increment num and print its value.
# Otherwise, we are in the decreasing sequence, so we decrement num and print its value.
# After each row is printed, the num variable is updated to the starting number for the next row by adding 1 to the current value of num.
# The print() function with no arguments is used to print a newline after each row.

#9
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()

     
#10
for i in range(5):
    for j in range(5,i,-1):
        print(" ",end="")
    
    
    for j in range(i+1):
        print("*",end="")
    print()

for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    
    for j in range(5,i,-1):
        print("*",end="")
    print()

#11
for i in range(5):
    for j in range(5,i+1,-1):
        print("*",end="")
    print()


#Interview questiom
#input = [0,0,1,1,1,2,2,3,3,4]
#output = [0,1,2,3,4,_,_,_,_,_]
num = [0,0,1,1,1,2,2,3,3,4]
for i in range(len(num)+1):
    for j in range(len(num)+1):
        if num[i] == num[j]:
            num.remove(num[i])
print(num)


#Date - 10/05/2023
#Source -CHATGPT (Pattern Question)
#q1
n = 5
for i in range(1, n+1):
    print("*"*5)

#q2
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()

#q3
#In the following question if I start the loop from 1 then it will 
#give me issue because character start from 0
n = 5
for i in range(n,0,-1):#5 4
    for j in range(1,i+1):#5,0,-1 
        print(chr(65+j),end=" ")
    print()

n = 5
for i in range(n,0,-1):#5 4
    for j in range(0,i):#5,0,-1 
        print(chr(65+j),end=" ")
    print()

#q4
n = 3
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end=" ")
    
    for k in range(i):
        print("*",end=" ")

    for l in range(1,i):
        print("*",end=" ")
    
    print()

for i in range(1,n+1):
    for j in range(i):
        print(" ",end=" ")
    
    for k in range(n,i,-1):
        print("*",end=" ")
    
    for k in range(n,i-1,-1):
        print("*",end=" ")

    print()


#pattern with number practice
#Increasing pattern with number
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()

#
n = 5
p = 1
for i in range(1,n+1):
    for j in range(i):
        print(p,end=" ")
    p = p + 1
    print()

#
n = 5
p = 5
for i in range(1,n+1):
    for j in range(i):
        print(p,end=" ")
    p = p - 1
    print()

#
n = 5
p = 0
for i in range(1,n+1):
    for j in range(i):
        print(p,end=" ")
    p = p + 2
    print()

#
n = 5
for i in range(n):
    for j in range(i+1):
        if i % 2 == 0:
            print("1",end=" ")
        else:
            print("2",end=" ")
    print()

#
n = 5
for i in range(n):
    for j in range(n,i,-1):
        print(" ",end=" ")
    
    for j in range(i+1):
        if i % 2 == 0:
            print("#",end=" ")
        else:
            print("$",end=" ")
    
    for k in range(i):
        if i % 2 == 0:
            print("#",end=" ")
        else:
            print("$",end=" ")
    
    print()

#
n = 5
p = 1
for i in range(1,n+1):
    for j in range(i,n+1):
        print(" ",end=" ")
    
    for k in range(i):
        print(p,end=" ")

    for l in range(1,i):
        print(p,end=" ")
    
    p = p + 1
    print()

for i in range(1,n+1):
    for j in range(i):
        print(" ",end=" ")
    
    for k in range(n,i,-1):
        print(p,end=" ")
    
    for k in range(n,i-1,-1):
        print(p,end=" ")
    
    p = p + 1
    print()

#
n =  5
p = 1
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(" ",end=" ")
    
    for k in range(i-1):
        print(p,end=" ")
    
    for l in range(i):
        print(p,end=" ")
    p = p + 1
    print()

for i in range(1,n+1):
    for j in range(i):
        print(" ",end=" ")
    
    for k in range(n,i-1,-1):
        print(p,end=" ")
    
    for k in range(n,i,-1):
        print(p,end=" ")
    
    p = p - 1
    print()

#
n = 5
for i in range(1,n+1):
    p = 1
    for j in range(i):
        print(p,end=" ")
        p = p + 1
    print()

#
n = 5
for i in range(1,n+1):
    for j in range(i):
        print(" ",end=" ")
    
    p = 1
    for j in range(n,i-1,-1):
        print(p,end=" ")
        p = p + 1
    print()

#Q5
n = 5

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    
    for j in range(i, 2 * i):
        print(j, end="")

    for j in range(2 * i - 2, i - 1, -1):
        print(j, end="")
    
    print()

#q6
n = 5
p =  0
q = 9 
for i in range(1,n+1):
    for j in range(i):
        print(" ",end=" ")
    
    for k in range(1):
        
        print(chr(65+p),end=" ")
        p = p + 1

    for k in range(n,i,-1):
        print(" ",end=" ")
        
    for k in range(n,i,-1):
        print(" ",end=" ")
   
    for k in range(1):
        
        print(chr(65+q),end=" ")
        q = q - 1
    print()

#q7
n = 5
for i in range(1,n+1):
    if i % 2 == 0:
        for j in range(1,n+1):
            if j % 2 == 0:
                print("X",end=" ")
            else:
                print("O",end=" ")
        print()
    else:
        for j in range(1,n+1):
            if j % 2 == 0:
                print("O",end=" ")
            else:
                print("X",end=" ")
        print()

#More Chat GPt Question that include all the concept
#Question 1:
# Write a function calculate_sum that takes a list of numbers as input and returns the sum of all the numbers in the list.
# Input: [1, 2, 3, 4, 5]
# Output: 15
n = int(input("Enter the number of elements: "))
def calculate_sum(n):
    user_list = []
    for i in range(n):
        inp = int(input("Enter a number: "))
        user_list.append(inp)
    sum = 0
    for i in range(len(user_list)):
        sum = sum + user_list[i]
        
    return sum

print("The sum of the given list is: ",calculate_sum(n))


n = int(input("Enter the number of elements: "))
lst = []
sum = 0
for i in range(0,n):
    inp = int(input("Enter the number: "))
    lst.append(inp)
for i in lst:
    if i % 2 != 0:
        sum = sum + i
    else:
        continue
print(sum)






# Question 2:
# Write a function count_vowels that takes a string as input and returns the count of vowels (a, e, i, o, u) in the string.
# Input: "Hello, World!"
# Output: 3
def count_vowels(usr_input):
    count = 0
    usr_input_lst = []
    for i in range(len(usr_input)):
        usr_input_lst.append(usr_input[i])
    
    for i in range(len(usr_input_lst)):
        if  usr_input_lst[i] == 'a' or  usr_input_lst[i] == 'e' or  usr_input_lst[i] == 'i' or  usr_input_lst[i] == 'o' or  usr_input_lst[i] == 'u':
            count = count + 1

    if count == 0:
            return "no vowel found"
    
    return count
usr_input = input("Enter word: ")    
print(count_vowels(usr_input))

# Question 3:
# Write a function is_prime that takes an integer as input and returns True if the number is prime, and False otherwise.
# Question 3:
# Input: 7
# Output: True
inpt = int(input("Enter a number: "))
if inpt < 2:
    print("It is not a prime number")
elif inpt == 2:
    print("2 is the smallest prime nunber")
else:
    for i in range(2,inpt):
        if inpt % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")

# Question 4:
# Write a function reverse_list that takes a list as input and returns a new list with the elements in reverse order.
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
n = int(input("Enter number of elements: "))
usr_input = []
new_lst = []
for i in range(1,n+1):
    n = int(input("Enter the number: "))
    usr_input.append(n)
for i in range(n-1,-1,-1):
    new_lst.append(usr_input[i])
print(new_lst)


# n = input("Enter a number: ")
# for i in range(len(n),0,-1):
#     print(i,end=" ")

# Question 5:
# Write a function remove_duplicates that takes a list as input and returns a new list with duplicate elements removed.
# Question 5:
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]
n = int(input("Enter the number of elements: "))
lst = []
for i in range(0,n):
    inp = int(input("Enter the number: "))
    lst.append(inp)
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)

#To count unique elements in the list
n = int(input("Enter the number of elements: "))
lst = []
count = 0
for i in range(0,n):
    inp = int(input("Enter the number: "))
    lst.append(inp)
new_lst = []
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
        count = count + 1
    
print(new_lst)
print(count)


# Question 6:
# Write a function find_max_min that takes a list of numbers as input and returns a tuple containing the maximum and minimum values in the list.
# Input: [5, 2, 9, 1, 7]
# Output: (9, 1)
n = int(input("Enter the number of elements: "))
lst = []
for i in range(0,n):
    inp = int(input("Enter the number: "))
    lst.append(inp)

max_val = lst[0]
for i in range(1, len(lst)):
    if lst[i] > max_val:
        max_val = lst[i]


min_val = lst[0]
for i in range(1, len(lst)):
    if lst[i] < min_val:
        min_val = lst[i]

print(max_val,min_val)


# Question 7:
# Write a function capitalize_names that takes a list of names as input and returns a new list with the names capitalized.
# Input: ["alice", "bob", "charlie"]
# Output: ["Alice", "Bob", "Charlie"]
n = int(input("Enter number of name you want: "))
name_lst = []
for i in range(n):
    name = input("Enter name: ")
    name_lst.append(name)
cap_name = [name.capitalize() for name in name_lst]
print(cap_name)   

# Question 8:
# Write a function is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise.
# Input: "radar"
# Output: True
name = input("Enter name: ")
lst_name = []
for i in name:
    lst_name.append(i)
if lst_name[0] == lst_name[-1]:
    print(True)
else:
    print(False)

# Question 9:
# Write a function calculate_factorial that takes an integer as input and returns the factorial of that number.
# Input: 5
# Output: 120
n = int(input("Enter the number: "))
fact = 1
for i in range(n,0,-1):
    fact = fact * i
print(fact)

# Question 10:
# Write a function find_common_elements that takes two lists as input and returns a new list containing the common elements between the two lists.
# Input: [1, 2, 3, 4, 5], [3, 4, 5, 6, 7]
# Output: [3, 4, 5]
lst_one = []
n1 = int(input("Enter the number of element: "))
for i in range(n1):
    ele = int(input("Enter the number: "))
    lst_one.append(ele)

lst_two = []
n2 = int(input("Enter the number of element: "))
for i in range(n2):
    ele = int(input("Enter the number: "))
    lst_two.append(ele)


unq_lst = []
for num in lst_one:
    if num in lst_two:
        unq_lst.append(num)
print(unq_lst)


#Flipkart Python Interview Question
# Check if a number is Armstrong number in Python. An armstrong number is a number that equals the sum of cube of all the digits of the number. Ex. 153 = 1^3+5^3+3^3
number = input("Enter a number: ")
sum = 0
num_count = 0
lst = []

for i in range(len(number)):
    num_count = num_count + 1
print(num_count)

n = int(number)
for i in range(num_count):
    a = n % 10
    b = n // 10
    n = b
    c = a
    lst.append(c)

for i in lst:
    sum = sum + i**num_count
print(sum)

if str(sum) == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")


#Write a program to get the Prime number in a list of numbers with starting and end point
# Input 1:
# Start point: 10
# End point: 20

# Output 1:
# Prime numbers between 10 and 20 are: [11, 13, 17, 19]

start = int(input("Enter a starting range greater than 1: "))
end = int(input("Enter a end range : "))
print("Prime Number between the range", start, "to", end, "is")
lst = []
for i in range(start,end+1):
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        lst.append(i)
print(lst)        


# Largest element of an array
# Sample Input:
# arr = [12, 45, 89, 27, 53, 19]

# Sample Output:
# The largest element in the array is: 89
n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    inp = int(input("Enter the number: "))
    lst.append(inp)
maximum = lst[0]
for i in lst:
    if i > maximum:
        maximum = i
    else:
        continue
print(maximum)


#Rotate an array
n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    inp = int(input("Enter the number: "))
    lst.append(inp)
out_lst = []
for i in range(len(lst), 0, -1):
    out_lst.append(i)
print(out_lst)


#Little practice on list

# a,b
# a --> t
# b --> a 
# t --> a

# question: Write a function to find the second smallest element in a list.
# Sample Input: [5, 2, 8, 1, 3]
# Sample Output: 2
n = int(input("Enter the number of elements: "))
lst = []
for i in range(n):
    inp = int(input("Enter the number: "))
    lst.append(inp)

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
            
print("The sorted list is:", lst)
print("The second smallest element in the list is: ",lst[1])


#Pynative list practice
# Exercise 2: Concatenate two lists index-wise
#Input
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# Expected output:
# ['My', 'name', 'is', 'Kelly']
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []
for i in range(0,len(list1)):
    lst = list1[i] + list2[i]
    list3.append(lst)
print(list3)

#Nested list
a = ['car', ['BMW', 'KIA', 'Ford'], 'Truck', ['Pick Up', 'Monster Truck', ['Ford', 'GMC']], 
     'Motorcycle', ['Honda']]


# Question 1:
# Write a program that takes a nested list as input and flattens it, i.e., converts it into a single-dimensional list.

# Sample Input: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Sample Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = int(input("Enter the number of the elments: "))
lst1_mainlist = []
for i in range(0,n):
    lst2_sublist = []
    size = int(input("The number of element in the sublist is: "))
    for j in range(0,size):
        inpt = int(input("Enter the elments: "))
        lst2_sublist.append(inpt)
    lst1_mainlist.append(lst2_sublist)
lst = []
for i in lst1_mainlist:
    lst  = lst + i
print(lst)

#Modified version I can use the extend() which will modify the original list and not create a new list
n = int(input("Enter the number of the elments: "))
lst1_mainlist = []
for i in range(0,n):
    lst2_sublist = []
    size = int(input("The number of element in the sublist is: "))
    for j in range(0,size):
        inpt = int(input("Enter the elments: "))
        lst2_sublist.append(inpt)
    lst1_mainlist.append(lst2_sublist)
lst = []
for i in lst1_mainlist:
    lst.extend(i)
print(lst)


# Question 2:
# Write a program that takes a nested list of integers as input and returns the sum of all the elements in the list.

# Sample Input: [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Sample Output: 45
    
n = int(input("Enter the number of elements you want: "))
lst_main = []
for i in range(0,n):
    lst_sub = []
    size = int(input("Enter the number of element for the sublist: "))
    for j in range(size):
        inpt = int(input("Enter the element for the sublist: "))
        lst_sub.append(inpt)
    lst_main.append(lst_sub)

sum = 0
lst = []
for i in lst_main:
    lst.extend(i)

for i in lst:
    sum = sum + i
print(sum)    

# Question 3:
# Write a program that finds the largest element in a nested list of integers.

# Sample Input: [[3, 2, 8], [5, 1], [4, 7, 6, 9]]
# Sample Output: 9

n = int(input("Enter the number of elements you want: "))
lst_main = []
for i in range(0,n):
    lst_sub = []
    size = int(input("Enter the number of element for the sublist: "))
    for j in range(size):
        inpt = int(input("Enter the element for the sublist: "))
        lst_sub.append(inpt)
    lst_main.append(lst_sub)

lst = []
for i in lst_main:
    lst.extend(i)

max = lst[0]
for i in lst:
    if max < i:
        max = i
    else:
        continue
print(max)

# Question 4:
# Write a program that counts the total number of occurrences of a specific element in a nested list.

# Sample Input: [[1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5]]
# Element to Count: 2
# Sample Output: 2

n = int(input("Enter the number of elements you want: "))
lst_main = []
for i in range(0,n):
    lst_sub = []
    size = int(input("Enter the number of element for the sublist: "))
    for j in range(size):
        inpt = int(input("Enter the element for the sublist: "))
        lst_sub.append(inpt)
    lst_main.append(lst_sub)
print(lst_main)

lst = []
for i in lst_main:
    lst.extend(i)

count = 0
number = int(input("Enter the number that you want to check: "))
for i in lst:
    if i == number:
        print(True)
print(count)


# Question 5:
# Write a program that checks if a given element exists in a nested list.

# Sample Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Element to Check: 6
# Sample Output: True

n = int(input("Enter the number of elements you want: "))
lst_main = []
for i in range(0,n):
    lst_sub = []
    size = int(input("Enter the number of element for the sublist: "))
    for j in range(size):
        inpt = int(input("Enter the element for the sublist: "))
        lst_sub.append(inpt)
    lst_main.append(lst_sub)
print(lst_main)

lst = []
for i in lst_main:
    lst.extend(i)


number = int(input("Enter the number that you want to check: "))
for i in lst:
    if i == number:
        print("True")
        break

#List are mutable and tuples are immutable that means the element cant be changed once it is created



#TUPLES
tup = (1,2,3)
tup_2 = tup + (2,)
print(tup_2)

user_input = input("Enter elements separated by a comma: ")
input_list = user_input.split(',')  # Split the input by space to create a list
input_tuple = tuple(input_list)  # Convert the list into a tuple

print(input_tuple)

#Pynative excercise
#Q1
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])


#Q2
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

#Q3
#If you want to print single element without comma use indexing
tuple1 = (50,)
print(tuple1[0])

#Q4
#This is known as unpacking
tuple1 = (10, 20, 30, 40)
a,b,c,d = tuple1
print(a)
print(b)
print(c)
print(d)


#Q5
#Swap loic
# a,b
# t = a
# a = b
# b = t
# a = 4

tuple1 = (11, 22)
tuple2 = (99, 88)
t = ()
t = tuple1
tuple1 = tuple2
tuple2 = t
print(tuple1)
print(tuple2)

#Q6
tuple1 = (11, 22, 33, 44, 55, 66)
print(tuple1[3:-1])

#Q7
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#Q8 visit the question again and do it with bubble sort copied the solution
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

#Q9
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#10
tuple1 = (45, 45, 45, 45, 42)
count = 0
for i in tuple1:
    if i == tuple1[0]:
        count = count + 1
if count == len(tuple1):
    print(True)
else:
    print(False)


tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
lst1 = list(tuple1)
for i in range(0,len(lst1)):
    for j in range(i, len(lst1)):
        if lst1[i][1] > lst1[j][1]:
            lst1[i][1] , lst1[j][1] = lst1[j][1] , lst1[i][1]
print(lst1)

#Bubble sort
lst1 = [6,2,4,5,7,9,10,3,1]
for i in range(0,len(lst1)):
    for j in range(i, len(lst1)):
        if lst1[i] > lst1[j]:
            lst1[i] , lst1[j] = lst1[j] , lst1[i]
print(lst1)


#Chat GPT Tuple Question

# Question: Write a program that takes a list of tuples as input. Each tuple represents a student's name and their corresponding score in a test. The program should calculate and print the average score for each student.

# Sample Input: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
# Sample Output:
# Average score for Alice: 85
# Average score for Bob: 92
# Average score for Charlie: 78

n = int(input("Enter the number of element in the list: "))
lst_main = []
for i in range(0,n):
    sub_lst = []
    size = int(input("Enter the number of element for the sublist: "))
    for i in range(0,size):
        inpt = eval(input("Enter the element: "))
        sub_lst.append(inpt)
    lst_main.append(sub_lst)

lst = []
for i in lst_main:
    lst.append(tuple(i))
print(lst)

for i in range(0, len(lst)):
    print(f"Average score for {lst[i][0]}:", lst[i][1])

#Revise the code it tells how to take tuple in list
n = int(input("Enter the number of students: "))
student_scores = []
for i in range(n):
    name = input("Enter the student's name: ")
    score = int(input("Enter the student's score: "))
    student_scores.append((name, score))
print(student_scores)

print("Student Scores:")
for student in student_scores:
    name = student[0]
    score = student[1]
    print(f"Average score for {name}: {score}")


#SET
s1 = {1,2,4,4}
print(s1)
print(type(s1))

#How to create a single element of set
a = {2}  # Using set literal
print(set(a))

b = set([2])  # Using a list
print(b)

c = set((2,))  # Using a tuple
print(c)

d = set("2")  # Using a string
print(d)


#If you want to create an empty set we have to use the keyword set() 
#otherwise it will create an empty dictionary
s1 ={}
s3 = set()
s4 = ()
print(type(s1))
print(type(s3))
print(type(s4))

s1 = {1,2,3,4}
s1.add(5)
print(s1)

#If we use remove and element is not present and throws error
s2 = {2,3,4,5}
s2.remove(5)
#If we use discard and element is not present and do nothing
s2.discard(5)

#We can update as well
s3 = {1,2}
s3.update([3,4,5], [4,5,6])
print(s3)

#Different set operations
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

#intersection
#This will return the common elements between sets 
#So the following will return common between s1 and s2
#We can also give multiple arguments
s4 = s1.intersection(s2,s3)
print(s4)

#Difference
#This show the element that are present in set 1 but not in set 2
#So given below we are seeing the elements that are present in s1
# but not in s2
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s4 = s1.difference(s2, s3)
print(s4)

#If we want what all difference are there in 2 sets OR
#Return a set of elements present in Set A or B, but not both
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}
s4 = s1.symmetric_difference(s2)
print(s4)

#Remove duplicates using set
le = [1,2,23,3,4,5,4,5,1,4]
l2 = list(set(le))
print(l2)

#other methods of set
employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

#The following will tell us that the gym members that are developers
result = set(gym_members).intersection(developers)
#print(list(result))

#Now to find the employees that are neither gym members nor developers
result = set(employees).difference(gym_members, developers)
print(list(result))


#Sets practice from pynative
#Q1
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)

#Exercise 2: Return a new set of identical items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.intersection(set2)
print(result)

#Exercise 3: Get Only unique items from two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1.union(set2))

#Exercise 4: Update the first set with items that don’t exist in the second set
set1 = {10, 20, 30}
set2 = {20, 40, 50}

result = set1.difference(set2)
print(result)

#Exercise 5: Remove items from the set at once
set1 = {10, 20, 30, 40, 50}
result = set1.difference({10,20,30})
print(result)

#Exercise 6: Return a set of elements present in Set A or B, but not both
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
result = set1.symmetric_difference(set2)
print(result)

#Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
result = set1.intersection(set2)
print("Two set have items in common",
      result)


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))


#dictionaries
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}

print(student["name"])
print(student["Age"])
print(student["cources"])

#If we try to access the key that does not exist we get the keyerror
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
print(student["phone"])

#But instead of error we can print none using get method
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
print(student.get("height"))

#We can also use our own default value
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
print(student.get("phone", "Not Found"))

#If we want to add new key-value pair
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
student["phone"] = 9769764450
print(student)

#We can also update the value in the key value pair
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
student["name"] = "poo"
print(student)

#To add we can use the update method which can be helpful to add more values
#It takes dictionaries as input
#If there are multiple inputs as dictionarie do it one by one
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
student.update({"name" : "gaurav", "Age" : 22, "phone number" : 48484815484})
print(student)

#If we want to see the len of our dictionarie
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
print(len(student))

#If we want to print all the keys of our dictionrie
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
print(student.keys())

#If we want to print all the values of our dictionarie
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
print(student.values())

#If we want to print all the key value pair in our dictionrie
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
print(student.items())

#If we want to loop through then we can use the following
student = {"name" : "Gaurav", "Age" : 21, "cources" : ["Math", "Science"]}
for key, value in student.items():
    print(key,value)


#Pynative dictionarie excercise

#Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

#using zip
output = dict(zip(keys, values))
print(output)

#using loop
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionarie = {}
for i in range(0 , len(keys)):
    dictionarie[keys[i]] = values[i]

print(dictionarie)


#using update method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionarie = {}
for i in range(0, len(keys)):
    dictionarie.update({keys[i] : values[i]})
print(dictionarie)


#Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict1.update(dict2)
print(dict1)

#Exercise 3: Print the value of key ‘history’ from the below
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

for i in sampleDict.items():
    print(i)

print(sampleDict["class"]["student"]["marks"]["history"])

#Exercise 4: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

#using fromkeys
dictionarie = {}
print(dictionarie.fromkeys(employees, defaults))

#using loop
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dictionarie = {}

for i in employees:
    dictionarie[i] = defaults.copy()
print(dictionarie)


#Exercise 5: Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

output = {}

for i in keys:
    output.update({i : sample_dict[i]})

print(output)

#Exercise 6: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for i in keys:
    sample_dict.pop(i)
print(sample_dict)

#Exercise 7: Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}

for i in sample_dict.values():
    if i == 200:
        print("200 present in a dict")
    else:
        continue

#Exercise 8: Rename key of a dictionary

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict.pop("city")
print(sample_dict)

sample_dict.update({"Location" : "New York"})
print(sample_dict)

#Another approach
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

new_key = "Location"
if "city" in sample_dict:
    sample_dict[new_key] = sample_dict.pop("city")

print(sample_dict)


#Exercise 9: Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print(min(sample_dict, key=sample_dict.get))

#Exercise 10: Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}


sample_dict["emp3"]["salary"] = 8500
print(sample_dict) 

#Caht GPT Problems

# Exercise 11: Count the frequency of elements in a list and store them in a dictionary.
# Sample Input: [1, 2, 3, 2, 1, 3, 4, 5]
# Sample Output: {1: 2, 2: 2, 3: 2, 4: 1, 5: 1}

sample_input = [1, 2, 3, 2, 1, 3, 4, 5]
keys = []
for i in sample_input:
    if i in keys:
        continue
    else:
        keys.append(i)

lst = []
values = []
for i in sample_input:
    if i in lst:
        continue
    else:
        values.append(sample_input.count(i))
        lst.append(i)

output = dict(zip(keys, values))
print(output)

#Other approach
sample_input = [1, 2, 3, 2, 1, 3, 4, 5]
dictionarie = {}
for i in sample_input:
    if i in dictionarie:
        dictionarie[i] = dictionarie[i] + 1
    else:
        dictionarie[i] = 1
print(dictionarie)


# Exercise 12: Find the common keys in two dictionaries and create a new dictionary with their values as a list.
# Sample Input:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}
# Sample Output: {'b': [2, 4], 'c': [3, 5]}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}

new_dict = {}
for i in dict1:
    if i in dict2:
        new_dict.update({i : [dict1[i], dict2[i]]})
print(new_dict)


# Exercise 13: Sort a dictionary by its values in ascending order.
#visit the following concept again
# Sample Input: {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}
# Sample Output: {'banana': 2, 'date': 3, 'apple': 5, 'cherry': 8}
        
sample_input = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 3}

print(sorted(sample_input.items(), key= lambda x:x[1]))

# Exercise 14: Remove the key-value pairs from a dictionary if the values are below a certain threshold.
# Sample Input: {'a': 10, 'b': 5, 'c': 15, 'd': 3}, threshold = 8
# Sample Output: {'a': 10, 'c': 15}

sample_input = {'a': 10, 'b': 5, 'c': 15, 'd': 3}
threshold = 8

output = {}
for i in sample_input:
    if sample_input[i] > threshold:
        output.update({i : sample_input[i]})
print(output)


# Exercise 15: Reverse the keys and values of a dictionary.
# Sample Input: {'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}
# Sample Output: {'fruit': 'banana', 'vegetable': 'carrot'}

sample_input = {'apple': 'fruit', 'banana': 'fruit', 'carrot': 'vegetable'}

output = {}
for x, y in sample_input.items():
    output.update({y:x})
print(output)

# Exercise 16: Find the key with the maximum value in a dictionary.
# Sample Input: {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 8}
# Sample Output: 'cherry'

sample_input = {'apple': 10, 'banana': 5, 'cherry': 15, 'date': 8}

print(max(sample_input.values()))

# Exercise 17: Merge multiple dictionaries into one dictionary.
# Sample Input:
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict3 = {'e': 5, 'f': 6}
# Sample Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

dict4 = {}
dict4.update(dict1)
dict4.update(dict2)
dict4.update(dict3)
print(dict4)


# Exercise 18: Find the intersection of values in multiple dictionaries.
# Sample Input:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'c': 3, 'd': 4}
# dict3 = {'c': 3, 'd': 4, 'e': 5}
# Sample Output: {'c': 3}

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'd': 4}
dict3 = {'c': 3, 'd': 4, 'e': 5}

for i in dict1.items():
    if i in dict2.items() and i in dict3.items():
        print(i)

# Exercise 19: Check if two dictionaries are equal.
# Sample Input:
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 2, 'c': 3, 'a': 1}
# Sample Output: True

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 3, 'a': 1}
for i in dict1.items():
    if i in dict2.items():
        print("True")
        break
    else:
        print("False")


#List/Tuple/Dictionarie comprehension

#List comprehension
#Syntax : new_list = [expression for item in iterable if condition]


nums = [1,2,3,4,5,6,7,8,9,10]
    
# I want 'n' for each 'n' in nums
my_list = []
for i in nums:
  my_list.append(i)
print(my_list)

#Same above thing using list comprehension
nums = [1,2,3,4,5,6,7,8,9,10]
my_list = [i for i in nums]
print(my_list)


#New example
nums = [1,2,3,4,5,6,7,8,9,10]
new_lst = []
for i in nums:
    count = i * i
    if count > 5:
        new_lst.append(count)
print(new_lst)

#Above using list comprehension
nums = [1,2,3,4,5,6,7,8,9,10]
new_lst = [i * i for i in nums if i*i > 5]
print(new_lst)

#other example
nums = [1,2,3,4,5,6,7,8,9,10]
new_lst = []
for i in nums:
    if i % 2 == 0:
        new_lst.append(i)
print(new_lst)

#Same above using list comprehension
nums = [1,2,3,4,5,6,7,8,9,10]
new_lst = [i for i in nums if i % 2 == 0]
print(new_lst)


#If we want to print the following
# [('a', '0'), ('b', '1'), ('c', '2'), ('d', '3')] 
letter = 'abcd'
number = '0123'
new_lst = []
for i in range(0, len(letter)):
    new_lst.append((letter[i], number[i]))
print(new_lst)

#Another example

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
letter = 'abcd'
number = '0123'
new_lst = []
for i in letter:
    for j in number:
        new_lst.append((i,j))
print(new_lst)

#Using list comprehension
letter = 'abcd'
number = '0123'
new_lst = [(i,j) for i in letter for j in number]
print(new_lst)


# Dictionarie Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#print(dict(zip(names,heros)))

dictionarie = {}
for name, hero in zip(names,heros):
    dictionarie[name] = hero
print(dictionarie)

#Using dictionrie comprehension for above
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

new_dict = { names:heros for names, heros in zip(names,heros) }
print(new_dict)


#Set Comprehension
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set(nums)
for i in nums:
    my_set.add(i)
print(my_set)
print()
#Using set comprehension for above
my_Set = {i for i in nums}
print(my_set)


#Comprehension practice CHATGPT

# Question 1: Create a new list that contains the square of each number from the given list.
# Sample Input: [1, 2, 3, 4, 5]
# Sample Output: [1, 4, 9, 16, 25]

sample_input = [1, 2, 3, 4, 5]
lst = [i*i for i in sample_input]
print(lst)

# Question 2: Create a new list that contains only the even numbers from the given list.
# Sample Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Sample Output: [2, 4, 6, 8, 10]

sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst = [i for i in sample_input if i % 2 == 0]
print(lst)

# Question 3: Create a new set that contains the square of each number from the given set.
# Sample Input: {1, 2, 3, 4, 5}
# Sample Output: {1, 4, 9, 16, 25}

sample_input = {1, 2, 3, 4, 5}
new_st = {i*i for i in sample_input}
print(new_st)

# Question 4: Create a new set that contains only the odd numbers from the given set.
# Sample Input: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Sample Output: {1, 3, 5, 7, 9}

sample_input = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
new_st = { i for i in sample_input if i % 2 != 0}
print(new_st)

# Question 5: Create a new dictionary that contains the square of each number from the given list as keys and their respective cubes as values.
# Sample Input: [1, 2, 3, 4, 5]
# Sample Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

sample_input = [1, 2, 3, 4, 5]
new_dict = {keys:values**3 for keys, values in zip(sample_input,sample_input)}
print(new_dict)


# Question 6: Create a new dictionary that contains the elements from the given list as keys and their lengths as values.
# Sample Input: ['apple', 'banana', 'cherry']
# Sample Output: {'apple': 5, 'banana': 6, 'cherry': 6}

sample_input = ['apple', 'banana', 'cherry']
length_input = []
for i in sample_input:
    length_input.append(len(i))

new_dict = {keys:values for keys, values in zip(sample_input, length_input)}
print(new_dict)

#Or we can use enumerate function(visit chatgpt answer)

input = "ABCDCDC"
sub_str = "CDC"
count = 0
for i in input:
    if sub_str in input:
        count = count + 1
print(count)



    

    
    
    
    
    































































