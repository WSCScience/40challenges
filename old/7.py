d = int(input("Please enter the distance (in metres): "))
t = int(input("Please enter the time (in seconds): "))

def v(d,t):
    return d/t

print("Average speed is", v(d, t), "metres per second")