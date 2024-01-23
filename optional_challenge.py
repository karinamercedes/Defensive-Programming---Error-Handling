# Write a program with two compilation errors, a runtime error and a logical error.

print "What's the meaning of life? Hint, it's a number."    #Syntax Error; missing opening and closing brackets 
meaning_guess = int(input("\nEnter your answer: "))
meaning_of_life = int(42)

#Logical Error; control structure 'while' missing ---> while meaning_guess != meaning_of_life:
while meaning_guess != meaning_of_life  #Syntax Error; expected ':' at the end of the line (before statements)
    if meaning_guess < meaning_of_life:
        meaning_guess = int(input("Too small! Life has a bigger meaning. Try again: "))
    else:  meaning_guess = int(input("Too big! Life meaning is smaller than that. Try again: "))

print("__________________________________________________________")
print("\nExactly. " + meaning_of_life + " is the meaning of life!") #Runtime Error; 'meaning_of_life' need to be cast to a str()
print("__________________________________________________________")

# End-of-file (EOF)
