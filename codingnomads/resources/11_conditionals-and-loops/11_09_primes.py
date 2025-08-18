# Print out every prime number between 1 and 1000.

# define as is_prime function
    #this is True if it's prime
def is_prime(n):
    #negative numbers aren't prime
    if n <= 1:
        return False
    #1,2,3 are prime
    if n <= 3:
        return True

    #numbers which are divisible by 2 and 3 aren't prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    #we are iterating through all of the numbers it could be divisible, up to it
    #we forget 4, because this is divisible by 2
    i = 5
    #we are trying numbers which are a lot bigger than it, in case they are divisible by this number
    while i * i <= n:
        #it's not prime if it's divisible by that number or that number +2
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


#iterating through the 1000 different numbers
# Print all primes from 1 to 1000
for num in range(1, 1001):
    if is_prime(num):
        #if the number is prime, then it is printed
        print(num)



