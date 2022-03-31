course = 'Python for Beginners'
print('Python' in course)
first = 'john'
last = 'smith'
print(f'{first} [{last}] is a coder')
print(10**3)
x=10
x+=3
print(x)
a=[1,2,3],[3,4,5]
a[0][1]=10
print(a)
import math
x = 10
print(math.ceil(x))
print(math.pow(x,3))
print(round(x))
temp=50
if temp>20:
    print("Hotty")
elif temp>30:
    print("fine")
i=1
while i<=5:
    print(i*'*')
    i+=1
names=["Mosh","Joyi","Ham","Sam"]
print(names[0:2])
numbers = [1,2,3,4,5]
for item in numbers:
        print(item)
for num in range(5):
    print(num)
number=(1,2,3,4)
number[0]=2
# Function


def greet(name,country):
    print(f'Hi {name}')
    print(f'Welcome {country}')


print("Start")
greet('mosh','us')

print("End")


def square(num):
    return num*num


result=square(10)
print(result)
# Exception

try:
    age = int(input("Age:"))
    income=2000
    risk=income/age
    print(age)s
except ValueError:
    print("invalid")
except ZeroDivisionError:
    print("Age can't be 0.")
names=['john','moly','harsh','spider','batman','wonder']
print(names[0:3])
for number in range(5):
    print(number)