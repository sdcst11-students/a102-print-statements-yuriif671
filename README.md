## SDSS Computing Studies Python Assignment
### Assignment #1 Basic Output (Total Marks 10)

Objectives:
* Clone a repository and edit the files inside it
* Make use of the print() function to generate output
* Make use of escaped characters: \n \" \' to print line breaks or quotation marks

This assignment will test the basic structure of a python program.  
You will need to have proper structure and the recommended basic output.
You can refer to the example1.py file for different ways that the print statement can be used.

### 3 Tasks

##### Task 1
(2 points) Modify the existing assignment file called "assignment.py".  It should display the message "Hello World!" Note that the output is case sensitive. Make sure that it is an exact match


##### Task 2
(2 points) **Create** a new assignment file called "assignment2.py".  It should display the following:

Sample Output Task #2
This is my second program.
It uses "two commands" to display the output.

Note that you can't use the command print("It uses "two commands" to display the output.") because the Python3 interpreter sees the second double quotation is ending the first one.  In this case, we have two choices:
  - Use a single quotation mark as the beginning and end of the output string.
  - "Escape" the internal double quotation mark.  Using \" instead of " will tell the compiler that the double quote is for display, and is not functional

##### Task 3
(2 points) Modify the assignment file called "assignment3.py".  We are going to make
this program print on 2 lines even though it uses only 1 print statement. We will use
the escape character \n to introduce a line break.

Expected output:
This is the first sentence.
This is the second sentence.

#### Task 4
(2 points) Modify the assignment called "assignment4.py".  We want it to only display the print statement.  The rest of the lines in the source code need to be commented out so that they do not affect the program running:

Expected output:
Hello!

#### Task 5
(2 points)
Create a file called "assignment5.py" in your project.  We are going to have your program display the clasic poem, "Ozymandias" by Percy Bysshe Shelly.
Your program should display a title on one line, the author's name on the line below it and then a couple spaces before you display the poem.
https://www.poetryfoundation.org/poems/46565/ozymandias

