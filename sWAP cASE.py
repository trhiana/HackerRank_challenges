import string 

def swap_case(s):
    word = ''
    for i in s:
        if i in string.ascii_lowercase:
            word += i.upper()
        elif i in string.ascii_uppercase:
            word += i.lower()
        else:
            word += i
    
    return word
