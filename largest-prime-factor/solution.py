from math import sqrt

def main():
    number = 600851475143

    max_prime = -1

    while number % 2 == 0:
        max_prime = 2
        number /= 2
    
    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            max_prime = i
            number /= i
    
    if number > 2:
        max_prime = number

    print(max_prime)

if __name__ == "__main__":
    main()