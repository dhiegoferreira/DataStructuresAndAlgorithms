'''Suppose you have a sorted list of 128 names, and you´re seraching through 
using binary serach. Whatś the maximium number of steps it would take?'''

'''
Answer:

Try to find the worst scenario for this.


Theory: The best scnearios tend to be in the center 
Thesis: [1,2,3,4,5,6,7,8,9,10]

-- T1: 0 steps in binary search approach
item = 5
low = 1
high = 10
guess = 5

-- T2: 1 steps in binary search approach
step 1
item = 4
low = 1
high = 5
guess = list[3] = 4 

-- T2: 1 steps in binary search approach
- step 1
item = 3
low = 1
high = 5
mid = (1 + 5)/2 = 6 /2 = 3
guess = list[3] = 4 
result: guess is more or equal to item -> so high = mid - 1 = 4 -1 = 3 so high = 3

- step 2
item = 3
low = 1
high = 3
mid = 2
guess = list[2] = 3 
result: guess  equal to item -> return mid -> finished.


So when we take distance of middle of list we incrase the steps number. Then on base
the explanation above we can concluse that if we take the first number or each extremity 
we will get the worst scneario as we can.

At the end, for one list with 120 elements the maximiun steps will be the scenario that
we take the first and the last element (1º and 119º)


for item = 1

120 / 2 = 60
60 / 2 = 30
30 / 2 = 15
15 / 2 = 8
8 / 2 = 4 
4 / 2 = 2 
2 / 2 = 1

for item = 119
is the same

7 steps to get result








low 
high (lengh of list)


while low <= high:
    mid = (low + high)
    guess = list[mid]
    
    if guess == item:
        return middle
    if guess > item:
        high = mid - 1
    else
        low = mid + 1

    return None

my_List = [1, 2, 3, ... , 120]






'''
