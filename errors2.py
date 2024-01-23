# This example program is meant to demonstrate errors.
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

'''
animal = Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

print full_spec
'''

animal = "Lion"  #Syntax Error; missing opening and closing quotation marks
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  #Syntax Error; missing initial f for this f-string     #Logical Error; varibles in 'full_spec' were in the wrong logical order

print(full_spec)  #Syntax Error - missing opening and closing brackets

# End-of-file (EOF)
