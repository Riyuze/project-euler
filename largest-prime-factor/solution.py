from math import sqrt

def main():
    number = 600851475143

    maxPrime = -1

    while number % 2 == 0:
        maxPrime = 2
        number /= 2
    
    for i in range(3, int(sqrt(number)) + 1, 2):
        while number % i == 0:
            maxPrime = i
            number /= i
    
    if number > 2:
        maxPrime = number

    print(maxPrime)

if __name__ == "__main__":
    main()