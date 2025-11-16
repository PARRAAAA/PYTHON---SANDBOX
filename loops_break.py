secret_number = 7

for number in range(1,11):
    if number != secret_number:
        print(f"{number} Is not your secret number")
    else:
        print(f"{secret_number} is your secret number :)")
        break 
