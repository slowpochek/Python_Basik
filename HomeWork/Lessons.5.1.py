# Ім'я змінної
import string
import keyword

test_value = ["_","__","___","x","get_value","get value","get!value",
             "some_super_puper_value","Get_value","get_Value",
             "3m","m3","assert","assert_exception"]

simbols = string.punctuation.replace("_","")

for variable_name in test_value:

    if variable_name in keyword.kwlist or variable_name[0].isdigit():
        print("False", end=" ")

    elif "__" in variable_name:
        print("False", end=" ")

    else:
        for _ in variable_name:
            if _ in simbols or _.isupper() or _ == " ":
                print("False", end=" ")
                break
        else:
            print("True", end=" ")
