tamout = int(input("Please input the amount of money you have. In pounds: ")) * 100

accept = [100, 50, 20, 10, 5, 2, 1]

exhange = int(input("Please enter in 100p, 50p, 20p, 10p, 5p, 2p, 1p: "))
correct = 0
if exhange in accept:
    correct = True
else:
    correct = False
while correct == False:
    exhange = int(input("Please enter in 100p, 50p, 20p, 10p, 5p, 2p, 1p: "))

print(tamout / exhange)