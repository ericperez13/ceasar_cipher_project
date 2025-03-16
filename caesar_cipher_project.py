#initializing alphabet globally so that each 'if' statement has access to it
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#user chooses e, q, or d with if statement in case user chooses something other
#than e, d, or q
choice = input("Would you like to encode(e), decode(d), or quit(q)? ")
if choice != 'e' and choice != 'd' and choice != 'q':
    print("Oops! That's not an option. Did your cat walk across your keyboard?"
          " Try again!") 

#encoding message  
if choice == 'e':
    encoded_message = input("What would you like to encode? ")
    rotation_number = int(input("How many times would you like to rotate?(1-25) "))
    if rotation_number < 1 or rotation_number > 25:
        print("Nice try, but the rotation must be between 1 and 25. No time"
        " travel allowed! Try again!")
        exit()
    else:
        encoded_result = ''
        for char in encoded_message:
            if char in alphabet:
                index = alphabet.index(char)
                new_char = alphabet[(index + rotation_number) % 26]
                encoded_result += new_char
            elif char in alphabet.upper(): #helps keep uppercase letters same
                encoded_result += char
            else: #helps keep puncuation the same
                encoded_result += char
        print(encoded_result)

#just undid or reversed the encoding process
if choice == 'd':
    decoded_message = input("What would you like to decode? ")
    for number_of_shifts in range(1,26):
        decoded_result= ''
        for char in decoded_message:
            if char.islower():
                index = alphabet.index(char)
                new_char = alphabet[(index - number_of_shifts) % 26]
                decoded_result += new_char
            elif char.isupper():
                decoded_result += char
            else:
                decoded_result += char
        print(decoded_result)

#user choose q for qutting or exiting the program
if choice == 'q':
    print("Quitting? Fine, I'll just shift my gears elsewhere. Farewell")

#code works, just prints out every solution their is instead of just the right 
# one
# type: ignore