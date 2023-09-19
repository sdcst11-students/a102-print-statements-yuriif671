#!python3

# This is a comment because the line begins with a #
# This code is not executed

# Basic print statement
print("Hello world!")

# Multiple items can be printed by separating with a ,
# but a space is inserted between each item:
print("Hello","world!","There ","is a double space here")

# An expression can be included in a print statement
print("3 + 5 =", 8 )
print("4 * 2 =", 4*2)

# Mixtures of variables and string literals can be included using formatted strings
# Old style of formatted string
# each {} is replaced by the expression included in the .format()
name = "Bob"
print("Hello, {}. 3 + 5 = {}".format(name,8))

# New style of formatted string where .format() is not needed
# Note the inclusion of f before the ""
name = "Bob"
print(f"Hello, {name}.  3 + 5 = {3+5}")

# We have to make sure there are no extra " symbols that might close a string literal
# if we need to use a " in the string, consider '' or \"
print('This is how we can include a " in the string literal')
print("This is how we can escape a \" symbol in a string literal")

# A multiline string literal uses """  or '''
print("""This is
multiple lines""")

content = '''This is a multi line string.
It is predefined as a variable and then the variable is printed later.
'''
print(content)


# Optional parameters can be included at the end of the print statement:
print("This is a string literal",end="-+-")
# end= is a commonly used print option that change the print statement from adding a line break to whatever you specify instead.