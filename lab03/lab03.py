#2-----------------
list = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15)]
sorted_list = sorted(list, key= lambda x: x[1])
print(sorted_list)

#3-----------------
sqr = lambda x: x*x
print(sqr(5))

#4a----------------
def print_hello():
    print("Hello!")

def add(a, b):
    return a + b

def greet_person(nume="John"):
    print(f"Hello, {nume}!")

#4b----------------
def multiply(a, b):
    return a * b

def show_message():
    print("This function does't return anything")

#5-----------------
print_hello()

rezultat_adunare = add(3, 4)
print(rezultat_adunare)

greet_person("Ion")
greet_person()

rezultat_inmultire = multiply(5, 6)
print(rezultat_inmultire)

show_message()