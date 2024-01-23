# This example program is meant to demonstrate errors.

# There are some errors in this program.
# Run the program, look at the error messages, and find and fix the errors.

'''
print "Welcome to the error program"
    print "\n"

    # Variables declaring the user's age, casting the str to an int, and printing the result
    age_Str == "24 years old" 
    age = int(age_Str) 
    print("I'm" + age + "years old.")

    # Variables declaring additional years and printing the total years of age
    years_from_now = "3"
    total_years = age + years_from_now

print "The total number of years:" + "answer_years"

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total * 12
print "In 3 years and 6 months, I'll be " + total_months + " months old"

#HINT, 330 months is the correct answer

'''

print("Welcome to the error program")  #Syntax Error; missing opening and closing brackets
print ("")  #Syntax Error; missing opening and closing brackets  #Logical error; there's no need to type \n, empty quotation marks are going to leave a blank line and if we add \n there are going to be two blank lines therefore the space will be too wide  # + Unexpected indentation


# Variables declaring the user's age, casting the str to an int, and printing the result

age_str = "24"  #Syntax Error; "str" in variable's name doesn't need capital letter    #Runtime Error; the correct symbol to define variable is =, not ==     #Runtime Error; str() need to be cast to a int() so I can only type numbers therefore 24 without "years old" (as they're letters)    # + Unexpected indentation
age = int(age_str)  #Syntax Error; "str" in variable's name doesn't need capital letter    # + Unexpected indentation
print("I'm " + str(age) + " years old.")    #Runtime Error; 'age' need to be cast to a str() to have a correct output  # + Unexpected indentation


# Variables declaring additional years and printing the total years of age

years_from_now = 3  #Runtime Error; 3 is an integer, not a string  # + Unexpected indentation
total_years = age + years_from_now  # + Unexpected indentation

print("The total number of years: " + str(total_years)) #Syntax Error; missing opening and closing brackets    #Syntax Error; the correct variable name is total_years, not answer_years  #Logical Error; total_years need to be cast to a str() to have the correct output

# Variable to calculate the total amount of months from the total amount of years and printing the result

total_months = total_years * 12
#Syntax Error; the correct variable name is total_years, not total although it could be consider a Logical Error too as its output would have been "total" repeated twelve times

print ("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old.")
#Syntax Error; missing opening and closing brackets    #Runtime Error; need to convert total_months into a string to have a correct output    #Logical Error; need to add 6 (months) to total_months to have the correct output as the program wants to calcute your age in 3 years and 6 months

# End-of-file (EOF)
