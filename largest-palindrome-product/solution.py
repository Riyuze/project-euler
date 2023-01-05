def main():
    palindrome = 0

    for i in range(100, 999):
        for j in range(100, 999):
            number = i * j

            if check(number) and number >= palindrome:
                palindrome = number

    print(palindrome)

def check(number):
    check = number
    reversed_num = 0

    while check != 0:
        digit = check % 10
        reversed_num = reversed_num * 10 + digit
        check //= 10

    if reversed_num == number:
        return True
    else:
        return False


if __name__ == "__main__":
    main()