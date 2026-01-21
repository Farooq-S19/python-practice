dict = {1:'idli',2:'puri',3:'dosa',4:'vada'}
# print(dict)

def menu(item):
    match item:
        case 1:
            return f"one plate {dict.get(item)}"
        case 2:
            return f"one plate {dict.get(item)}"  
        case 3:
            return f"one plate {dict.get(item)}"
        case 4:
            return f"one plate {dict.get(item)}"
        case _:
            return "No item "
user_option=int(input(f"Enter what you want :"))
print(menu(user_option))