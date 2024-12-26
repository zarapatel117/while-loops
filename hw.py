user_input = input("Enter a word ")
reversed_string = ""
q = len(user_input) - 1
while q >= 0:
    reversed_string += user_input[q] 
    q -= 1  
print("Reversed string is", reversed_string)
