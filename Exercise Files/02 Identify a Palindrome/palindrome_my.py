
from curses.ascii import isalnum


def is_palindrome(in_str):
    in_str = in_str.upper()
    in_str = list(filter(lambda x : isalnum(x) , in_str))
    if in_str[:len(in_str)//2] == in_str[:len(in_str)//2:-1]:
        return True
    return False    


print(is_palindrome("aA' caa"))