first_number = float(input("Insert first number: "))
second_number = float(input("Insert second number: "))
opperand = input('''Choose an opperand to perform the calculation
Choose from:
1. +
2. -
3. *
4. /
Insert here: ''')
if '+' in opperand:
    sum = first_number + second_number
    print("The answer is: " + str(sum))
elif '-' in opperand:
    if first_number > second_number:
        minus = first_number - second_number
    else:
        minus = second_number - first_number
    print("The answer is:" + str(minus))
elif '*' in opperand:
    mul = first_number * second_number
    print("The answer is: " + str(mul))
elif '/' in opperand:
    divi = first_number / second_number
    print("The answer is: " + str(divi))