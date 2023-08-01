n = [13,67,98,34,113,567]
while True:
    a = input('guess the number or press x to quit:\n')
    if a == "x":
        break
    try:
        a = int(a)
    except ValueError:
        print('please type a number or x to quit')
    if a in n:
        print('you guessed')
    else:
        print('try again')