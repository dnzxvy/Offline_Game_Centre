def is_prime(n):

    if n <= 1:
        return False

    for i in range(2,(n//2)+1):
        if n % i == 0:
            return True
    else:
        return False

def largest_prime(prime_list):
    primes = [num for num in prime_list if is_prime(num)]
    return max(primes) if primes else None

def sum_of_primes(limit):
    return sum(n for n in range(2, limit) if is_prime(n))




limit_num = int (input("Enter a number: "))
result = sum_of_primes(limit_num)

print(f"the sum of all the prime numbers less than {limit_num} is {result}")

prime_list = [10,4,6,28,99,81,87]
largest = largest_prime(prime_list)
if largest:
    print(f"the largest prime number is {largest}")


#print(is_prime(199))






numbers = [1,2,3,4,5,]

print(max(numbers))


