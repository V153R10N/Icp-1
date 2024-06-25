    x = input("Enter the string : ")
    chars = list(x)
    del chars[0]
    chars.pop()
    chars.reverse()
    y = "".join(chars)
    print(y)
