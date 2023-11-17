partnum = input("Please enter the 4 digit part number: ")
oldmodel = 0
newmodel = 0
total = 0

while (partnum != "9999"):

    while (len((partnum)) != 4):
        print("Please try again.")
        partnum = int(input("Please enter the 4 digit part number: "))

    if(partnum[3] == "6" or partnum[3] == "7" or partnum[3] == "8"):
        oldmodel = oldmodel + 1
    else:
        newmodel = newmodel + 1
    total = total + 1

    partnum = input("Please enter the 4 digit part number: ")

print(f"Total parts entered: {total}\n{newmodel} of these were new, {oldmodel} of these were old")
    
    