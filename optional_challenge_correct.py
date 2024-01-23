# Write a program with two compilation errors, a runtime error and a logical error.

print ("What's the meaning of life? Hint, it's a number.")
meaning_guess = int(input("\nEnter your answer: "))
meaning_of_life = int(42)

while meaning_guess != meaning_of_life:
    if meaning_guess < meaning_of_life:
        meaning_guess = int(input("Too small! Life has a bigger meaning. Try again: "))
    else:  meaning_guess = int(input("Too big! Life meaning is smaller than that. Try again: "))
  
print("__________________________________________________________")
print(f"\nExactly. {meaning_of_life} is the meaning of life!")
print("__________________________________________________________")