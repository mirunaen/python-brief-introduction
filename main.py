"""
def main():
  print("hello world")

if __name__=="__main__":
  main()
"""

#Declare a variable and initialize it
f=0
print(f)
f="abc"
print(f)
print("this is a string "+ str(123))

def someFunction():
  global f
  f="def"
  print(f)

someFunction()
print(f)

"""del f #to delete f 
print(f)
"""
#FUCTIONS
def func1(): #scope definer and indentation(tab)
  print("I am a function")

func1()
print(func1()) #function called fuction doesnt returns a value
print(func1)#func is not executes fuctions are objects

def func2(arg1, arg2):
  print(arg1," ",arg2)

def cube(x):
  return x*x*x

func2(10,20)
print(func2(10,20))#no return value from func2
print(cube(3))#has a return

def power(num, x=1):
  result= 1
  for i in range(x):
    result = result * num 
  return result

print(power(2))#num
print(power(2,3))#num and power
print(power(x=3,num=2))#python allows to do this

#the arguments are a varialbe argument list (*)
def multi_add(*args):
  result = 0
  for x in args:
    result = result + x
  return result
#I can pass in a variable number of arguments
#the fuction tehn loops over each argument and adds them all to a running total,which is then returned.
print(multi_add(10,4,5,6,7))

#Conditionals
def main():
  x, y = 10,100
  if(x<y):
    st = "x is less than y"
  elif(x==y):
      st="x is equal to y"
  else:
    st = "x is greater than y"
  
  print(st)

  st="x is less than y" if(x<y) else "x is greater or the same than y "
  print(st)

if __name__=="__main__":
  main()

#LOOPS

x=0
while(x<5):
  print(x)
  x=x+1

for x in range(5,10):
  print(x)

days=["Monday","Tuesday","Wednesday","Fri","Sat","Sund"]
for d in days:
  print (d)

#BREAK AND CONTINUE STATEMENTS

for x in range(5,10):
  if (x==7):break
  print(x)

for x in range(5,10):
  if (x % 2 == 0):continue # if the rest is 0 then continue skip the rest dont do the statement in the loop
  print(x)

days=["Monday","Tuesday","Wednesday","Fri","Sat","Sund"]
for i,d in enumerate(days):
  print (d,i)

#Classes

class myClass():
  def method1(self):
    print("myClass method1")
  
  def method2(self,someString):
    print("myClass method2 " + someString)

c = myClass()
c.method1()
c.method2("This si a string")


class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("anotherClass method1")
  
  def method2(self,someString):
    print("anotherClass method2")

c2=anotherClass()
c2.method1()
c2.method2("This is a string")

class Person:
  def __initialize__(self, name, age, sex):
    self.name = name
    self.age = age
    self.sex = sex 

def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)


def SetAnnual():
  global annual
  annual=10000
def PrintMonthly():
  print("Your monthly payment is "+str(annual/12)+" USD.")
SetAnnual()
PrintMonthly()

number=int(input("Enter a num: "))
if (number>=1000):
  print(4)
elif (number>=100):
  print(3)
elif (number>=10):
  print(2)
else:
  print(1)

"""max=x if (x>y) else y 
is equivalen to:
max=y
if (x>y):
    max=x"""

def Sum10th(data):
  sum=0
  for i,d in enumerate(data):
    if (i % 10 == 0): sum=sum+d
  return sum

print(Sum10th([1,2,3,4,5,6,7,9,8,10,10]))

"""
if __name__ == "__main__":
  main()
It executes the main() function only if this file is executed as the main program.
"""


from datetime import date
from datetime import time
from datetime import datetime

#im going to import date time and datetime Classes

today = date.today()

#Get today´s date from the simple today() method from the date class
print("Today´s date is ",today)

#Print out the date´s individual components 

print("Date comoponents: ",today.day,today.month,today.year)

#retrieve today´s weekday (0=Monday, 6=Sunday)

print("Today´s weekday # is:",today.weekday())
days=["Mon","tue","wed","thuer","fri","sat","sund"]
print("Which is a : ", days[today.weekday()])

##DATETIME OBJECTS  
#Get today´s date from the datetime class

today = datetime.now()
print("The current date is", today)
t= datetime.time(datetime.now())
print("The hour is ",t)

#FORMATTING TIME OUTPUT

#Example file for formatting time and date output

#Times and dates can be formatted using a set of predefined string control codes
now=datetime.now()
### Date formatting ###
# %y/%Y - Year,%a/$A -weekday, %b/%B - month, %d- day of the month
print(now.strftime("The current year is: %Y"))
print(now.strftime("%a,%d,%B,%y"))


# %c -locate´s date and time,%x - locate´s date,%X - locale´s time

print(now.strftime("Locate date and time: %c"))
print(now.strftime("Locate date: %x"))
print(now.strftime("Locate time: %X"))

### Time Formatting  ###
#%I/%H -12/24hour, %M -minute, %S - second, %p - locale´s AM/PM

print(now.strftime("Current time: %I:%M:%S %p"))
print(now.strftime("24 hour time: %H:%M "))