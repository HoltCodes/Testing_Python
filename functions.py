from re import X


def add(a,b):   #function name: 'add', parameters: a and b
  x = a + b     # process
  return x      #return value: x

new_val = add(3, 5)  
print(new_val)



def say_hi(name):
  print("Hi, " + name + "!")

say_hi("Rogan")
say_hi("Rachel")
say_hi("Ramp")
say_hi("Nala")

def say_hi(name):
  return "Hi " + name
greeting = say_hi("Josh")
print(greeting)  

def add(a, b):
  x = a + b
  return x
sum1 = add(4,6)  # =10
sum2 = add(1,4)  # =5
sum3 = sum1 + sum2 #sum3 = 15
