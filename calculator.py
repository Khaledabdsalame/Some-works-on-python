import termcolor
termcolor.cprint("welcome to calculator python","red")
while True:
    num1 = input("choose a number 1: ")
    try:
      num1 = int(num1)
    except ValueError:
        print("choose a number please")
        continue
    num2 = input("choose number 2: ")
    try:
      num2 = int(num2)
    except:
        print("choose a number please","red")
        continue
    print("choose a number pleas")
    print("*......1")
    print("+.......2")
    print("/........3")
    print("-..........4")
    methode=input("choose a methode")
    if methode=="1":
      print(num1*num2)
      continue

    if methode=="2":
       print(num1+num2)
       continue

    if methode=="3":
       print(num1/num2)
       continue

    if methode=="4":
       print(num1-num2)
       continue

    else:
      print("choose a methode by select a number for them")


