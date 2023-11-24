def main():
    number = int(input("Enter a positive decimal number: "))
    number_of_bits = int(input("Enter number of bits: "))
    number = convert_to_binary(number, number_of_bits)
    modified_number = replace_digits_and_add_1(number, number_of_bits)
    print(modified_number)

def convert_to_binary(number, number_of_bits):
    binary_number = bin(number)[2:].zfill(number_of_bits)
    return binary_number

def replace_digits_and_add_1(number, number_of_bits):
    modified_number = ""
    for digit in number:
        if digit == '0':
            modified_number += "1"
        else:
            modified_number += "0"
    num1 = int(modified_number, 2)
    num2 = int('0001', 2)
    sum = num1 + num2
    return bin(sum)[2:].zfill(number_of_bits)

if __name__ == '__main__':
    main()
