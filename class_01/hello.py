# %%
print("Hello, engineers!", "testing")
# %%
# List all prime numbers from 1 to 100
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = [num for num in range(1, 101) if is_prime(num)]
print("Prime numbers from 1 to 100:", primes)
# %%
print ("one", "two", "three") 
print("four\n five")
print("five")
# %%
# Class exercise
name_list = ["Alice", "Bob", "Charlie", "David"]
print("All names: ", name_list)

name_list = name_list[:3]
print("First three names: ", name_list)

name_list.pop(1)
print("names list without the second persons: ", name_list)

name_list.extend(["Eve"])
print("names list after adding a new person at the end: ", name_list)
# %%
