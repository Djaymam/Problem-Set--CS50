

stair = int(input("stair: "))

while stair < 1 or stair > 8 :
    stair = int(input("stair: "))

for i in range(1, stair+1):
    print(" " * (stair-i) + "#" * (i), end=" ")
    print("#" * i)


