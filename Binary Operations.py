# Purpose: Binary Operations.
# Description: Program to apply some operations at binary numbders.
# Author: Esraa Emary Abd Elsalam.
#version: 4.
#******************************************************
#first complement

def first_complement(binary_num):
    binary_num = str(binary_num)
    complement = ""
    for bit in binary_num:
        if bit == '0':
            complement += '1'
        elif bit == '1':
            complement += '0'
    return complement

#******************************************************
#second complement

def second_complement(binary_num):
    binary_num = binary_num[::-1]
    complement = ""
    i = 0
    # Find the first '1' in the binary number, and include it and everything before it
    for i in range(0, len(binary_num)):
        if binary_num[i] == "0":
            complement += '0'
        elif binary_num[i] == "1":
            complement += "1"
            break
    # Calculate the one's complement for the remaining bits after the first '1'
    j = i+1
    for j in range(j, len(binary_num)):
        if binary_num[j] == '0':
            complement += '1'
        elif binary_num[j] == '1':
            complement += '0'
    complement = complement[::-1]
    return complement

#**************************************************
#addition

def addition_operation(num1, num2):
    carry = 0
    result = "0"
    final_result = []
    # Adding 0 for if there an overflow
    num1 = "0"+num1
    num2 = "0"+num2
    if len(num1) < len(num2):
        num1 = num1.zfill(len(num2))
    elif len(num2) < len(num1):
        num2 = num2.zfill(len(num1))
    num1 = num1[::-1]
    num2 = num2[::-1]
    # Loop through each binary digit and add  bits along with the carry
    for i in range(len(num1)):
        temp_sum = int(num1[i]) + int(num2[i]) + carry
    # Determine the result and carry based on the current sum
        if temp_sum == 3:
            carry = 1
            result = "1"
        elif temp_sum == 2:
            carry = 1
            result = "0"
        elif temp_sum == 1:
            carry = 0
            result = "1"
        else:
            carry = 0
            result = "0"
        final_result.append(result)
    final_result = ''.join(final_result)[::-1]
    if final_result[0] == "0":
        final_result = final_result[:0] + final_result[0+1:]
    return final_result

#**********************************************************
#subtraction

def subtraction(bin1, bin2):
    # Ensure both binary numbers have the same length by padding the shorter one with leading zeros
    bins = [bin1, bin2]
    length = max(len(bins[0]), len(bins[1]))
    diff = length - min(len(bins[0]), len(bins[1]))
    if len(bins[0]) == length:
        short = 1
    else:
        short = 0
    bins[short] = "0" * diff + bins[short]

    # Determine which binary number is larger and which one is smaller
    if bins[0] >= bins[1]:
        big = 0
        small = 1
    else:
        big = 1
        small = 0

    result = ""
    # Initialize an array to keep track of borrow values for each bit
    borrow = [0] * length

    # Iterate through each bit of the binary numbers from right to left
    for i in range(length):
        j = length - i - 1
        bit1 = int(bins[big][j])
        bit2 = int(bins[small][j])

        # Compare bits and determine the result of subtraction
        if bit1 + borrow[j] > bit2:
            result += '1'
        elif bit1 + borrow[j] == bit2:
            result += '0'
        elif bit1 + borrow[j] < bit2:
            result += '1'
            k = j-1
            # Update borrow values based on the subtraction result
            while bins[big][k] == '0':
                borrow[k] += 1
                k -= 1
            borrow[k] = -1

    # Reverse the result string to get the final output
    result = result[::-1]
    return result

#***********************************************************
#validity of binary numbers

def validity(binary_number):
    i = 0
    while i < len(binary_number):
        if int(binary_number[i]) > 1:
            input("please insert a valid binary number")
        i += 1
#***********************************************************
#main program

while True:
    import sys
    #manu1
    print("**binary calculator**")
    print("A)Insert new numbers")
    print("B)Exit")
    condition1 = input("Enter a choice: ")

    #check if the input from user in options1
    options1 = {"A", "B"}
    while condition1 not in options1:
        condition1 = input("Please select a valid choice: ")

    #finish the program is the user input "B"
    if condition1 == "B":
        sys.exit()

    #if the user input "A" apply a binary calculator
    elif condition1 == "A":

    # take the first binary number from the user and check the validity of it
        first_binary_number = input("Enter the binary number: ")
        validity(first_binary_number)

    #manu2
        print("**please select the operation**")
        print("A)compute one's complement")
        print("B)compute two's complement")
        print("C)addition")
        print("D)subtraction")
        operation = input("Enter a choice: ")

    # check if the input from user in options2
        options2 = {"A", "B", "C", "D"}
        while operation not in options2:
            operation = input("Please select a valid choice: ")

        #apply first complement
        if operation == "A":
            print("The first complement for the number is: ", first_complement(first_binary_number))

        # apply second complement
        elif operation == "B":
            print("The second complement for the number is: ", second_complement(first_binary_number))

        # apply addition
        elif operation == "C":
        # take the second binary number from the user and check the validity of it
            second_binary_number = input("Enter the second binary number: ")
            validity(second_binary_number)
            print("The addition for the two numbers is: ", addition_operation(first_binary_number, second_binary_number))

        # apply subtraction
        elif operation == "D":
        # take the second binary number from the user and check the validity of it
            second_binary_number = input("Enter the second binary number: ")
            validity(second_binary_number)
            print("The subtraction for the two numbers is: ", subtraction(first_binary_number, second_binary_number))
