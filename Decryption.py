# Dela Cruz, Lailanie E. _ BSCPE 1-4
# Assignment 2
# Problem 2 - Decryption

# Ask the user to input an encrypted text
input_str = input("Enter a string to decrypt: ")
output_str = ""
# Check every character
for i in range (len(input_str)):
# if *, change to a
    if input_str[i] == "*":
        output_str += "a"
# if &, change to e
# if #, change to i
# if +, change to o
# if !, change to u
# print the output