__author__ = "8568922, Wolff"

import turtle
import time

'''
This function accepts an input, checks if it is a float and falls within the range of 0 to 1. 
If not, it repeatedly prompts the user until a valid input is provided. 
The result is displayed both in the console and the turtle.py window. 
The two imported modules facilitate the pop-up window functionality.
'''

def get_float():
    while True:
        # Input.
        u_input = input("Please input your decimal number:\n")
        try:
            # Processing.
            n = float(u_input)
            if not (0 < n < 1):
                print("Please make sure the input between 0 and 1 (exclusive).")
                continue
            return n
        except ValueError:
            print("Please make sure the input is a correct data type.")

n = get_float() #calls the function

# Discards of the number that comes before the comma.
right_of_commma = n % 1

'''
This function converts the user input into its correlating base two.
'''

def binary_convert(decimal):
    result = "" # Empty result variable.
    for i in range (1, 33): # Range for the 32-bit approxiamtion.
        t = 2 ** - i # Formula for the conversion.
        ben = decimal >= t
        if ben: 
            decimal -= t
        result += str(int(ben)) # If the number fits into t, it is added into the result var.
    return result
# Output in the console.
print(f"{n} in binary: {binary_convert(right_of_commma)}")

# Graphic Output in hacker style.
turtle.getscreen()
turtle.hideturtle()

text = str(n) + " in binary: \n" + binary_convert(right_of_commma) + " !!!"

screen_text = ""
turtle.color("green")
turtle.bgcolor("black")
for character in text: # The loop adds each character to the screen after the time.sleep delay.
    screen_text += character
    turtle.clear()
    turtle.write(screen_text, align="center", font=("Monaco", 24, "bold"))
    time.sleep(0.1)


turtle.mainloop()

# Test cases.
def test_cases():
    print("Assertion error output, when something goes wrong")

    # Positive test.
    assert (binary_convert(0.5) == '0.5 in binary: 10000000000000000000000000000000')
    
    # Negative tests.
    assert (binary_convert(-100) == 'Please make sure the input between 0 and 1 (exclusive).')
    assert (binary_convert("Ben") == 'Please make sure the input is a correct data type.')
    assert (binary_convert(1) == 'Please make sure the input between 0 and 1 (exclusive).')

if __name__ == '__main__':
    test_cases