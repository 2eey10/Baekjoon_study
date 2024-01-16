def check_id(id):
    if id.isalpha():
        if id.islower():
            if len(id) <= 50:
                return True
            else:
                False
        else:
            return False
    else:
        return False
id = input()

result = check_id(id)

if result == True:
    print(id + "??!")    




