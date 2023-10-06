def check_uppercase(mystring):
    for character in mystring:
        if character.isupper():
            return True
    return False

def check_lowercase(mystring):
    for character in mystring:
        if character.islower():
            return True
    return False


def check_symbol(mystring):
    import re
    pattern = "[~!@#$%^&*()]"
    for character in mystring:
        if re.match(pattern, character):
            print('Match: ', character)
            return True
    return False

def test_password(mystring):
    # code below this line
    if check_uppercase(mystring) and check_lowercase(mystring) and check_symbol(mystring):
        print('Valid password')
    # code above this line

pwd = "aq12r_bc"
test_password("aW12R@_bc")
check_symbol(pwd)