""" I'm learning python
This is my first project from a video tutorial  """

# intro = "Welcome to my first Python code!"

# name = input("What is your name?")
# age = input("What is your age? ")
# print ("Hello " + name + ", ")
# print(intro)
# print("You are " + age + " " + "years old. " + "Soon you will be " + str(next_age) + "!") 

#If age not a number: 

# age = 0

# while age == 0:
#     age_str = input("What is your age? ")
#     try:
#         age = int(age_str)
#     except:
#         print("Error: Age must be a number.")
        
# print ("Hello " + name + ", ")
# print(intro)
# print("You are " + age + " " + "years old. " + "Soon you will be " + str(next_age) + "!") 

#seperate code for converting age into a number:

# try:
#     next_age = int(age) + 1
# except:
#     print("Eror: please enter a number for your age.")
# else:
#     print ("Hello " + name + ", ")
#     print(intro)
#     print("You are " + age + " " + "years old. " + "Soon you will be " + str(next_age) + "!") 
   
#while looping:

# n = 0
# while n <= 5:
#      print("Value = " + str(n))
#      n = n + 1
# print("Value increment excedes protocol. Closing Loop.")

#password check:

# pw = ""

# while not pw == "1234":
#     pw = input("What is your password? ")
    
# print("Password is correct. Welcome!")    
    
#note: when debugging, red circle = break point

#exercise: if no user input, ask user for input. use while loop:

# name = ""

# while name == "":
#     name = input("What is your name?" )

#Functions:

#ask for age function with local variable:
# def ask_age():
#     age_int = 0 
#     while age_int == 0:
#         age_str = input("What is your age? ")
#         try:
#             age_int = int(age_str)
#         except:
#             print("Error: Age must be a number.")
#     return age_int

#ask for age function with global variable:
# age_int = 0
# def ask_age():
#     global age_int
#     while age_int == 0:
#         age_str = input("What is your age? ")
#         try:
#             age_int = int(age_str)
#         except:
#             print("Error: Age must be a number.")
#     return age_int

#local is better because it reduces dependency

#ask for name function:
# def ask_name():
#     name_answer = ""
#     while name_answer == "":
#         name_answer = input("What is your name? ")
#     return name_answer
# #call for the name
# name = ask_name()
# #call for the age:
# age = ask_age()


#display results:
# print("Your name is " + name + ". " + "You are " + str(age) + " years old.")
# print("Soon you will be "+ str(age + 1) + "!")

#using function parameters:
# def ask_name():
#     name_answer = ""
#     while name_answer == "":
#         name_answer = input("What is your name? ")
#     return name_answer


# def ask_age(person_name):
#     age_int = 0 
#     while age_int == 0:
#         age_str = input(person_name +" what is your age? ")
#         try:
#             age_int = int(age_str)
#         except:
#             print("Error: Age must be a number.")
#     return age_int

# name1 = ask_name()
# name2 = ask_name()
# age1 = ask_age(name1)
# age2 = ask_age(name2)

# print("Your name is " + name1 + ". " + "You are " + str(age1) + " years old.")
# print("Soon you will be "+ str(age1 + 1) + "!")
# print()
# print("Your name is " + name2 + ". " + "You are " + str(age2) + " years old.")
# print("Soon you will be "+ str(age2 + 1) + "!")

#exercise: remove duplicate code (print messages) by creating function with multiple parameters:

# def person_info(name, age, height = 0):
#     print()
#     print("Your name is " + name + ". " + "You are " + str(age) + " years old.")
#     print("Soon you will be "+ str(age + 1) + "!")
# #formatted strings to use different syntax for concatenations 
#print(Your name is {name}, you are {age} years old.)
#or
#print("Your name is %s, you are %s years old." % (name, age))

# #under <18, display:
#     print("You are a minor.")
 
#  #over >=18, display: 
#     print("You are an adult.")
#add elif statements
# if age == 17 "You are almost an adult"
#if age == 18 "You are now an adult. Congrats!"
#print only 1 of the 4 available sentences
#exercise: if age > 60 print "You are a senior."
#           if age < 10 print "You are a kid."
#and or conditions simplified: if age <=10 and <18 simp to 10<= age <18

#     if age == 17:
#         print("You are almost an adult.")
#     elif 13 <= age < 18:
#         print("You are a Teenager.")
#     elif age == 1 or age == 2:
#         print("You are a baby.")
#     elif age == 18:
#         print("You are an adult. Congrats!")
#     elif age < 10:
#         print("You are a kid.")
# #because > 60 conflicts with >= 18, must come before.
#     elif age > 60:
#         print("You are a senior.")
#     elif age >= 18:
#         print("You are an adult.")
#     else:
#         print("You are a minor.")
# #add variable (height) while not breaking results that only give 2 variables (name1,age1). use if not to not display height variable if = 0.
#     if not height == 0:
#         print("Your height is " + str(height) + "m.")
    
# person_info(name1,age1)
# person_info(name2,age2)



    # while age == 0:
    #     age_str = input(name + " what is your age? ")
    #     try:
    #         age = int(age_str)
    #     except:
    #         print("Error: age must be a number.")
    # return age
    
    #for loops
# for i in range(0, 4):
#     #i = index (a variable), the range tells to loop 4 times, it exits at 4 and 4 is excluded from the values
#     print(i)

# NB_PERSON = 5 #creates a convention (?) to use as a variable in for loops. instead of (0,4) use 0, convention
# for i in range(0, NB_PERSON):
#     name = "Josh" + str(i+1)
#     age = ask_age(name)
#     person_info(name, age, 0)
    
 #print multiple lines using one print syntax
# print("""I 
#        can
#             print
#                 like
#             this""")