def main():
    total = 0

    num = 1
    prev = 0

    while num < 4000000:
        a = num
        num += prev
        prev = a

        if num % 2 == 0:
            total += num
        print(num)
    print(total)


if __name__ == "__main__":
    main()