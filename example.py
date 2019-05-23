a = input()
b = a.split(".")
if (len(b) < 4):
    print("No")
else:
    key = False
    for s in b:
        if len(s) < 1 or type(eval(s)) != int or int(s) < 0 or int(s) > 255:
            print("No")
            key = True
            break
    if key is False:
        print("Yes")
