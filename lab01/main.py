name = input("Enter your name: ")
print(f"Hello, {name}!")

var_int = 100
var_float = 3.14
var_short_str = "This is a short string"
var_long_str = ("""This is a long string
Second line
Third line
Fourth line""")

print(type(var_int), type(var_float))
print(len(var_long_str))
print(var_short_str.upper())
print(var_short_str[0:4])


elem1 = "este"
elem2 = "formatat"
print("Acesta {} un string {}.".format(elem1, elem2))