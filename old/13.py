time = input("Please say if you are full-time or part-time: ").lower()

if time == 'part-time' or time == 'part time':
    h = int(input("How many hours a week do you work?"))
    print(h/5 * 28)

else:
    print("28")
