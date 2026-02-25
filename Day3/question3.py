#Use a loop to find all prime numbers between 1 and 500 and print them in rows of 10.

count = 0  # counts how many primes printed in current row

for num in range(2, 501):  # check numbers from 2 to 500
    is_prime = True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num:4}", end=" ")
        count += 1
        
        if count % 10 == 0:
            print()  # move to next line