#####################
## 0- HELLO WORLD 
#####################

print("hello world")

#########################
## 1- VARIABLES + TYPES 
#########################

message = "hello world"
text = "je suis un texte" 
num = 15
pi = 3.14
cond = True 
tableau = []

# Check type of a variable

print(type(pi))
print(type(num))
print(type(text))
print(type(cond))
print(type(tableau))
isinstance(num, str) #boolean

##############################
## 2- NATIVE METHODS PYTHON 
##############################

hello2 = message.capitalize()
split = message.split()
# print(hello2)
# print(split[0])

# INPUT method
name = input("what's your name? ")
age = input("how old are you? ")

print(type(age))
print("Vous vous appelez " + name + " et vous avez " + age + " ans") # concaténation = super lourd car il faut gérer les espaces/whitespace
print(f"Vous vous appelez {name} et vous avez {age} ans") # f-string = formatted string literal = template literals in javascript 👌🏾

#################
## 3- FUNCTIONS
#################

def test():
  print("je suis une fonction")
# test()
# print(type(fonction))

def demander_age_nom():
  name = input("what's your name? ")
  age = input("how old are you? ")
  print(f"Vous vous appelez {name} et vous avez {age} ans") 

# demander_age_nom()


# def ask_age():
#   age = int(input("age?"))
#   print(type(age))
#   print("ceci n'est pas un nombre")

# TRY / EXCEPT / FINALLY
def ask_age():
  try:
    age = int(input("age?"))
    print(type(age))
  except ValueError:
   print("ceci n'est pas un nombre")
  finally:
    print("la fonction est finie")

# ask_age()

######################################
## 4- ITERATIONS / BOUCLE FOR / WHILE
######################################

# FOR IN

for num in range(0, 10):
  if num == 5:
    num += 3
  print(num)

words = ["il", "était", "une", "fois"] 
tblConte = []

def createIntro():
  strConte = ""
  for word in words:
    tblConte.append(word) 
    strConte = strConte + " " + word
  print(tblConte)
  print(strConte)

# createIntro()

# WHILE 

q = input("age? ")
age = int(q)
while age < 20:
  input("age please? ")
  if age >= 20:
    break
print("age ok. thank you")

###########################
## 5- CONDITIONS IF / ELSE
###########################

# name = input("whats your name? ")
# age = input("how old are you? ")

def verifier():
  # if not age and not name:
  #   print("vous n'avez pas répondu aux questions") 
  # elif not age or not name:
  #   print("vous n'avez pas répondu à l'une des 2 questions")
  # else: print("merci")

  try:
    name = input("whats your name? ")
    age = int(input("how old are you? "))
    # if type(age) is int: 
    if isinstance(age, int):
      print("merci")
  except:
      print("ceci n'est pas un nombre") 
      

verifier()



