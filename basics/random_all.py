#to genrate random numbers for bank balance 
import random
a=random.random()
#it will genrate floating number between 0 and 1
print(f"you have current balance of {a}")
#to genrate random integers for lucky number
b=random.randint(1,10)
print((f"Your lucky number is {b}"))
#random.rondom() will genrate floating number between 0 and 1
#to get randonm floating numbers beyond 0 and 1 we can use random.uniform(a,b)
c=random.uniform(0,100)
print(f"Your random number is {c}")
#now i whant to genrate a random numbers from a sequence like even, odd, from 4th table etc
#then we need to use random.randrange(start, stop[, step])
d=random.randrange(0, 40, 4)
print(f"Your random number from 4th table is {d}")
#oddnumbers
e=random.randrange(1,100,2)
print(f"Your random odd number is {e}")
#suppose i have a list of items and i want to select one item randomly
#then we need to use random.choice(sequence)
items=['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
f=random.choice(items)
print(f"My favorite fruit is {f}")
#if i whant to select more than one item randomly from the list
#then we need to use random.sample(population, k)
g=random.sample(items, 3)
print(f"my favorite fruits are {g}")
#to print items without brackets and quotes
print(", "   .join(g))
#to shuffle the items in the list
#then we need to use random.shuffle(x)
random.shuffle(items)
print(f"Shuffled items are {items}")
random.seed(1)
print(f"Random number with seed 10 is {random.random()}")
print(f"Random number with seed 10 is {random.random()}")
