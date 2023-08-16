#None is object that represent absence of value
# to use input funtion
name = input("What is your name: ")
print("Hey There " + name)


#Type Conversion
#There are different type of function for type conversion: int(), float(), bool()
#input() function always takes string
#we can multiply int and float
birth_year = int(input("Enter your birth year: "))
age = 2023 - birth_year
print(age)
print(type(age))
print(type(birth_year))


#string
# if we want to add ' in any string use double quotes
# if we want to add " in any string use single quotes
#So below you can see that in order to print multiple line we have to add triple quotes
output = """
Hey Gaurav
hope Your doing good
"""
print(output)

#in order to use indexing we use '[]'
out = "Gaurav Bohra"
print(out[-1])
#if we write [0:3] then it is actuall [0:2]
print(out[0:3])
#there are multiple options we can try
print(out[0:])#will print everything 
print(out[:])#will print everything
print(out[:5])#will print till 4 character


#Formatted string
#our aim is to print 'john [smith] is a coder
#"This aproach is not optimal message = first + ' [' + last + '] ' + "is a coder"
first = 'john'
last = 'smith'
message = f'{first} [{last}] is a coder'
print(message)
#So over here 'f' is used for formatted string and {} are the place holders
#We can use different types of string function like len
#We can also use different tyeps of methods like .upper(),lower()
#We can also find character in the string using find method
print(message.find('j'))
#If we find any character that is not present in the string then it will return -1
#In order to see is there is a specific character in string or not we can use 'in'
print('john' in message)
#So the major difference between find and 'in' is that one gives index and other one gives boolean result


#Aritmatic operator in python
print(2+4)
print(4-2)
print(2*4)
print(10/3)#normal division
print(10//3)#given interger value 
print(10%3)#gives remainder
print(10**3)#power
#Augmented assignment operator that is +=, -=, *=
x = 10
x = 10 + 2
print(x)

y = 10
y += 2
print(y)

#IF statemnts
is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
 
#Logical Operator
#And : Both condition should be true
#OR : Any one condition should be true
#NOT : If we give ture boolean it converts to false

has_high_income = False
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


#Logical Operator: <,>,!=,==,<=,>=
temperature = 30

if temperature < 30:
    print("It is cold")
else:
    print("It is lovely day")


#While Loops
i = 1
while i<=5:
    print(i)
    i = i + 1

#pattern
i = 1 
while i<=5:
    print("*" * i)
    i = i + 1

#Guessing program
number = int(input("Guess: "))
actual_number = 9
option = 0
if number==actual_number:
    print("You Win!")
elif number != actual_number:
    while option < 3:
        number = int(input("Guess: "))
        if number == actual_number:
            print("You win!")
            break
    else:
        option = option + 1
    print("Sorry You failed!")

#Different appproach
#In normal we canwrite if and else in while also we can write if and then in the same level of while we can write else
number = 9
count = 0
guess = 3
while count < 3:
    user = int(input("Guess: "))
    count = count + 1
    if user == number:
        print("You won!")
        break
else:
    print("Sorry You failed")

#Game
#Here there is a new concept while True: this means the loop will continue until break coondition is reached
while True:
    command = input(">").lower()
    if command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    elif command == "start":
        print("car started ready to go")
    elif command == "stop":
        print("car stopped")
    elif command == "quit":
        break
    else:
        print("I don't understand that")


#Change the program and tell the user if the car is already start or stop
started  = False
while True:
    command = input(">").lower()
    if command == "start":
        if started:
            print("CAR IS ALREADY STARTED")
        else:
            started = True
            print("Car started.. read to go")
    elif command == "stop":
        if not started:
            print("CAR IS ALREADY STOPPED")
        else:
            started = False
            print("car stopped")
    elif command == "quit":
        break
    elif command == "help":
        print("""
start - to start the car
stop -  to stop the car
quit - to exit""")
    else:
        print("I don't understand that")
    

#For Loop
for item in 'Python':
    print(item)

for item in ['gaurav','dinesh','emil']:
    print(item)

for item in [1,2,3,4]:
    print(item)

for item in range(10): #It will start from 0 and end at 9
    print(item)

for item in range(5,10,2): #It will start from 5 end at 9 with 2 gap
    print(item)

#Nested Loops
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")


#List to find largets number
#List also have unpacking feature
#number = [1,2,2]
#a,b,c = number
number = [5,10,20,15]
max = 0
for i in number:
    if i > max:
        max = i
print(max)


#2d List
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])#So here we are seeing row 1 value and in that coloumn 2

#To iterate in 2d list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)

#To count number in list
numbers = [1,2,3,4,5,6,7,8,9,2,3,4,5,5,65,6,7,5,6,7]
count = 0
for i in numbers:
    count = count + 1
print(count)

#Functions of list
numbers = [1,2,4,5,6]
#To insert anywhere
numbers.insert(0,10)
#To insert at the end
numbers.append(10)
#To remove
numbers.remove(2)
#To remove all
numbers.clear()
#To remove end element
numbers.pop
#To know index of a element
numbers.index(2)
#To count specific number
numbers.count(2)
#To sort a list in ascending
#When we print this this will return none 
#So the below method is right and after the line just again call the list
numbers.sort()
#To sort the list in descending 
numbers.reverse()
#To copy the list
numbers.copy()


#Tuples are like list but are immutable this means 
#we can't add, remove or update tuples like list
numbers = (1,2,3)
print(numbers[0])

#Unpacking
#In order to use elements of tuple
coordinates = (1,2,3)
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]

x,y,z = coordinates
print(x,y,z)
#The above are the two methods which we can use
#And second method is known as unpacking

#Dictionaries
#Key value pairs, each key should be unique
customer = {
    "name": "john",
    "age": 30,
    "is_verified": True
}
print(customer)
#We can get the pair by typing the key
print(customer["age"])

# create a dictionary with some key-value pairs
my_dict = {"apple": 3, "banana": 2, "orange": 5}

# get the value associated with the "apple" key using the get() method
apple_count = my_dict.get("apple")

# print the result
print("The number of apples is:", apple_count)

# get the value associated with a key that doesn't exist using the get() method
nonexistent_count = my_dict.get("grapefruit")

# print the result (will return None since the key doesn't exist)
print("The number of grapefruits is:", nonexistent_count)

# get a default value if the key doesn't exist using the get() method
default_count = my_dict.get("grapefruit", 0)

# print the result (will return 0 since the key doesn't exist and we provided a default value of 0)
print("The number of grapefruits is:", default_count)

#creating emoji convertor
user_input = input(">")
words = user_input.split(" ")
emojis = {
    ":)" : "😊",
    ":(" : "😣"
}
output = " "
for word in words:
    output = output + emojis.get(word, word) + " "
print(output)


#function
def greet_user():
    print("Hey there")
    print("Welcome Aboard!")


print("Start")
greet_user()
print("stop")

#Paramter are the placeholders that we define in a function for recieving information
#Argument are the actual pieces of information that we supply to the function
#Position argument because there position matters

#Function Parameter
def greet_user(name):#2 Parameter
    print(f"Hey there {name}")#3
    print(f"Welcome Aboard {name}")

greet_user("Gaurav")#1 Argument
greet_user("Pooja")

#Function Parameter
name = input("Enter name")
def greet_user(name):#2 Parameter
    print(f"Hey there {name}")#3
    print(f"Welcome Aboard {name}")

greet_user(name)#1 Argument
# greet_user(name)

#Multiple parameter
def greet_user(first_name, last_name):
    print(f"Hey there {first_name} {last_name}")

greet_user("Gaurav","Bohra")

#Key word argument
#In this we dont have to worry about the position
#position argument should be first and then keyword argument
def greet_user(first_name, last_name):
    print(f"Hey there {first_name} {last_name}")
greet_user(last_name="Bohra",first_name="Gaurav")


#Return in function
def square(number):
    return number * number
print(square(3))
#So here if dont use none then will get the output but will also get "None"

#rusable function
def emoji_convertor(user_input):
    words = user_input.split(" ")
    emojis = {
        ":)" : "😊",
        ":(" : "😣"
    }
    output = " "
    for word in words:
        output = output + emojis.get(word, word) + " "
    return output
message = input(">")
print(emoji_convertor(message))


