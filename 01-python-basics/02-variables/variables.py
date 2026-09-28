# Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 12
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

# Concatenation of variables in a print

print(my_string_variable, my_int_to_str_variable, my_bool_variable)
print("This is the value of:", my_bool_variable)

# Some system functions

print(len(my_string_variable))

# Variables on a single line ¡You shouldn't use so much this syntax¡

name, surname, alias, age = "Aiden", "Pearce", 'The Vigilante', 37
print("His name is:", name, surname, ". He is:", age, "and his alias is", alias)

# Input function

first_name = input("What's your name? " )
age = input("How old are you? ")

print(first_name)
print(age)