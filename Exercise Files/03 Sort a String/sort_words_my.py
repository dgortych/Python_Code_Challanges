
def sort_words(in_str):
    sp = in_str.split()
    sp.sort(key=lambda x : x.casefold())
    return " ".join(sp)

print(sort_words("Ban ban BAN bAN"))    

