#Q1
'''
L = [11, 12, 13, 14]

# (i) add 50 and 60
L.append(50)
L.append(60)
print(L)

# (ii) remove 11 and 13
L.remove(11)
L.remove(13)
print(L)

# (iii) sort ascending
L.sort()
print(L)

# (iv) sort descending
L.sort(reverse=True)
print(L)

# (v) search for 13
if 13 in L:
    print("13 found")
else:
    print("13 not found")

# (vi) count elements
print(len(L))

# (vii) sum all elements
s = 0
for x in L:
    s += x
print(s)

# (viii) sum all ODD numbers
odd_sum = 0
for x in L:
    if x % 2 != 0:
        odd_sum += x
print(odd_sum)

# (ix) sum all EVEN numbers
even_sum = 0
for x in L:
    if x % 2 == 0:
        even_sum += x
print(even_sum)

# (x) sum all PRIME numbers
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_sum = 0
for x in L:
    if is_prime(x):
        prime_sum += x
print(prime_sum)

# (xi) clear all elements
L.clear()
print(L)

# (xii) delete L
del L
'''

#Q2
'''
nums = [2, 5, 7, 3]
total = 0
for n in nums:
    total += n
print(total)
'''


#Q3
'''
num = [2, 5, 7, 3]
p = 1
for n in num:
    p *= n
print(p)
'''

#Q4
'''
L1= [[["*" for i in range(6)] for i in range(4)] for i in range(3)]
print(L1)
'''


#Q5
'''
D = {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}

# (i) add key=8, value=8.8
D[8] = 8.8
print(D)

# (ii) remove key=2
D.pop(2)

# (iii) check whether key=6 is present
print(6 in D)


# (iv) count number of elements
print(len(D))

# (v) add all values
total = 0.0
for v in D.values():
    total += v
print(total)

# (vi) update value of key 3 to 7.1
D[3] = 7.1
print(D)

# (vii) clear dictionary
D.clear()
'''


#Q6
'''
S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) add 55 and 66 to S1
S1.add(55)
S1.add(66)

# (ii) remove 10 and 30 from S1
S1.discard(10)
S1.discard(30)

# (iii) check whether 40 is present in S1
print(40 in S1)

# (iv) union
print(S1 | S2)

# (v) intersection
print(S1 & S2)

# (vi) S1 - S2
print(S1 - S2)
'''


#Q7
'''
# (i) 100 random strings (length 6–8, letters only)
import random, string
for _ in range(100):
    k = random.randint(6, 8)
    s = ""
    for _ in range(k):
        s += random.choice(string.ascii_letters)
    print(s)

# (ii) all primes between 600 and 800
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for n in range(600, 801):
    if is_prime(n):
        print(n)

# (iii) numbers between 100 and 1000 divisible by 7 and 9
for n in range(100, 1001):
    if n % 7 == 0 and n % 9 == 0:   # i.e., divisible by 63
        print(n)
'''


#Q8
'''
exam_st_date = (11, 12, 2025)

# Just join the 3 numbers with "/" in between
print("The examination will start from:", exam_st_date[0], "/", exam_st_date[1], "/", exam_st_date[2])
'''


#Q9
'''
nums = [10, 12, 15, 22, 25, 40, 41]  
for n in nums:
    if n % 5 == 0:
        print(n,end=",")
'''


#Q10
'''
n = 37  
even = (n % 2 == 0)
if even:
    print("Even")
else:
    print("Odd")
'''


#Q11
'''
t = "Emma is good. Emma likes Python. Emma!"
l=t.split()
count=0
for i in l:
    if i=="Emma":
        count=count+1
print("no. of times Emma appears is ",count)
'''


#Q12
'''
l1 = [10, 21, 4, 45, 66, 93]
l2 = [13, 22, 57, 24, 40, 5]

l3 = []
for x in l1:
    if x % 2 == 1:
        l3.append(x)
for y in l2:
    if y % 2 == 0:
        l3.append(y)
print(l3)
'''


#Q13
'''
p = [(2,3), (4,5), (6,7), (7,8)]
evenp = []
for (x, y) in p:
    if x % 2 == 0:
        evenp.append((x, y))
print(evenp)
'''


#Q14
'''
sd = {1: 2.3, 2: 4.5, 3: 1.8, 4: 3.6}
ids = []
for k, v in sd.items():
    if v > 3.0:
        ids.append(k)
print(ids)
'''


#Q15

'''
commands_received = {"MOVE", "TURN_LEFT", "TURN_RIGHT", "STOP"}
commands_executed = {"MOVE", "TURN_LEFT", "STOP"}

ne= commands_received - commands_executed
print("commands which were not executed",ne)
'''



