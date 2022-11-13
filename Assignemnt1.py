## Assignment Part-1
##Q1. Why do we call Python as a general purpose and high-level programming language?
# Python programing allow user to wirte program in high level language.
# High level language reduce complexity of program bcz it easily user can understand.
# Python is an one of the easy language for beginer and have supprot lot's of library to perform various tasks.


## Q2. Why is Python called a dynamically typed language?
# In python we don't need to specify datatype of variable during declaration as (like other programing
#  language) dynamically based on assigned value dynamicaly type assigne to the variable that's 
#  why python called as dynamically typed lang.


## Q3. List some pros and cons of Python programming language?
# Pros
# 1. Less code.
# 2. Easy to understand.
# 3. Extensive library available.
# 4. It's Object oriented
# 5. Reduce complexity.
# Cons
# 1. Compile & run at runtime so increase runtime.
# 2. Dynamic Typed increase the possiblity of error in runtime.
# 3. Poor memory efficiency.


## Q4. In what all domains can we use Python?
# 1. Machine Learning/AI
# 2. Data Science
# 3. Data Analysis/Data Visualizaton
# 4. Big Data
# 5. Game Davelopment


## Q5. What are variable and how can we declare them?
# Variable is an name given to the memory location that can be access by using variable name.
# variable we can declare using alfabet and number
# variable name not allow any special character.
# variable name must start with _ or any alfabet not with number.


## Q6. How can we take an input from the user in Python?
# Using input() method we take input from the user this method allow user to enter input.


## Q7. What is the default datatype of the value that has been taken as an input using input() function?
# String is a default datatype for input() function in python.


## Q8. What is type casting?
# Typicasting is an change the data type of data. eg. float to integer


## Q9. Can we take more than one input from the user using single input() function? If yes, how? 
# If no, why?

# Yes we can, using the split() method we able to take multiple input from user in split we pass 
# specific saperater this can sepereate multiple input in we not give seperater then bydefault it
# consider as space.
# eg. firstName, lastName = input("Enter First and Last Name: ").split();


## Q10. What are keywords?
# Keyword is an special predefined word that have specific meaning.
# Keyword name we cannot use as variable or method name


## Q11. Can we use keywords as a variable? Support your answer with reason.
# No we can't use keyword as variable because of keyword as predefined meaning.


## Q12. What is indentation? What's the use of indentaion in Python?
# Indentaion meaning in spaces in begining in python is work like block of code 
# (like parenthesis in other lang.) 


## Q13. How can we throw some output in Python?
# Using print() we can print the output, in bracket whichever we added this w'll be print.


## Q14. What are operators in Python?
# Operator are used to perform operation on variables and values
# below operateros used in python
# 1) Arithemetic Operator(+, -, *, /, %, **, //)
# 2) Assignment Operator(=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=)
# 3) Comparison Operator(==, !=, >, <, >=, <=)
# 4) Logical Operator(and, or, not)
# 5) Identity Operator(is, is not)
# 6) Membership Operator(in ,not in)
# 7) Bitwise Operator(&, |, ^, ~, <<, >>)

## Q15. What is difference between / and // operators?
# Both are used for dividation / return the float value and // returns the integer value. 

# Q16. Write a code that gives following as an output.
# iNeuroniNeuroniNeuroniNeuron
print("iNeuron"*4);


# Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
number = int(input("Enter the number"))
if (number % 2) == 0:
    print("The given number is even")
else:
    print("The given number is odd")

# Q18. What are boolean operator?
# Boolean operators is in the form of True and False(1 and 0) value.
# if the condition satisfy then return True otherwise return False


#Q19. What will the output of the following?
#1 or 0
#0 and 0
#True and False and True
#1 or 0 or 0

print(1 or 0);
print(0 and 0);
print(True and False and True)
print(0 or 0 or 0)


# Q20. What are conditional statements in Python?
# The conditional statumest is an if else.
# if the condition true then execute if block otherwise else block will be executed.

# Q21. What is use of 'if', 'elif' and 'else' keywords? 
# 'if' if the condition is true the execute if block.
# 'elif' if the elsif condition is true then execute elif block of code.
# 'else' used to write block of code will be execute when is condition is false.


# Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
age = int(input("Enter the Age: "))
if age>= 18:
  print("I can vote")
else:
  print("I can't vote");

#Q23. Write a code that displays the sum of all the even numbers from the given list.
numbers = [12, 75, 150, 180, 145, 525, 50]
sum = 0;
for i in numbers:
  if i%2 == 0:
    sum += i
print("The sum of all even numbers ",sum)



# Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
x,y,z = input("Enter the three number : ").split()
if x>y and x>z:
  print("The greatest number is : ", x)
elif y>x and y>z: 
  print("The greatest number is : ", y)
else:
  print("The greatest number is : ", z);



# Q25. Write a program to display only those numbers from a list that satisfy the following conditions
# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop
# numbers = [12, 75, 150, 180, 145, 525, 50]
numbers = [12, 75, 150, 180, 145, 525, 50]
for j in numbers:
  if j> 500:
    break;
  if j%5 == 0 and j<=150:
    print(j," ")
