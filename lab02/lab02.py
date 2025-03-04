#b-----------------------
value_list = ["elem1", 2, 4.3, "other", True]

print(value_list[0], value_list[2])
value_list[0] = "elem1_modified"
a = value_list[2:]
a[0]=8
print()

value_list.append(123)
len(value_list)
# max(value_list)

print(123 in value_list)
value_list[1] = value_list[1] * 2
print(value_list[-1] - len(value_list[0]))


#c----------------------------

my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple))
print(my_tuple[0], my_tuple[-1])
print(my_tuple[1:3])

len(my_tuple)
min(my_tuple)
max(my_tuple)

#d------------------------

my_set = {5, 3, 5, 3 ,58, 12345}
print(my_set)
len(my_set)
my_set.add(23)

#e---------------------

num_key_dic = {200: "Success", 400: "Error"}
text_key_dic = {"name": "Ion", "age": 21}

print(num_key_dic[200])
print(text_key_dic["age"])

len(num_key_dic)
sorted(text_key_dic)

keys = list(num_key_dic.keys())
num_key_dic["jkl"] = 90 
print(keys)
print(text_key_dic.values())

#f-------------------------

print(type(tuple(value_list)))

#2a-----------------------

preturi = [10, 20, 30]
produse = ["Lapte", "Pâine", "Mere"]

for i in range(3):
    print("Produs: {} - Preț: {} lei".format(produse[i], preturi[i]))

#b-----------------------

varsta = int(input("Introduceți vârsta: "))
varsta_viitoare = varsta + 5
print("În 5 ani veți avea " + str(varsta_viitoare) + " ani.")

#c-----------------------
caractere = "abcdefg"
print('a' in caractere)
print('z' not in caractere)