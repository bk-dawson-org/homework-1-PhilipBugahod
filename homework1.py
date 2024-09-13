radius = float(input("Enter radius: "))

def calculatevolume(radius) :
    volume = (4/3)*3.14*radius**3
    return volume

sphere1 = calculatevolume(radius)
print(round(sphere1,2))