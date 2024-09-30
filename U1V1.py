# Problem #1, Print List
def print_list(lst):
    for list in lst:
        print(list)

lst = ["squirtle", "gengar", "charizard", "pikachu"]

print(print_list(lst))

#Problem #2: Print Doubled List
def doubled(lst):
    for list in lst:
        print(list *2)

lst = [1,2,3]
print(doubled(lst))

#Problem #3, Return Doubled List
def doubled(lst):
    i=[]
    for list in lst:
        i.append(list*2)
    return i

lst = [1,2,3]
new_lst= doubled(lst)
print(new_lst)

#Problem #4, Flip Signs
def flip_sign(lst):
    i =[]
    for list in lst:
        i.append(list*-1)
    return i

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
 
 #Problem #5, Max Difference
def max_difference(lst):
    maxi = max(lst)
    mini = min(lst)
    return maxi - mini
#Drea, remember to RETURN THE RESULT.
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)

#Problem #6, Below Threshold
def count_less_than(numbers, threshold):
    i = []
    for item in numbers:
        if item < threshold:
            i.append(item)
    return len(i)
#Andrea, don't return INSIDE THE LOOP
numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter)

#Problem #7, Evens List
def get_evens(lst):
    i = []
    for item in lst:
        if (item%2 == 0):
            i.append(item)
    return i 
lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst)

#Problem #8, Multiples of Five
def multiples_of_five():
    for list in range(5,105,5):
        print(list)

print(multiples_of_five())
#Problem #9, find Divisors
def find_divisors(n):
    i = []
    for d in range(1,n+1):
        if n % d == 0:
            i.append(d)
    return i

lst = find_divisors(6)
print(lst)

#Problem #10, FizzBuzz
def fizzbuzz(n):
    i = []
    for n in range(1, n + 1):
        if n % 3 == 0:
            print ("Fizz")
        elif n % 5 == 0:
            print ("Buzz")
        else:
            print(n)

fizzbuzz(13)

#Problem #11, Print the Index
def print_indices(lst):
    pass

#Problem #12, Linear Search
def linear_search(lst, target):
    pass
