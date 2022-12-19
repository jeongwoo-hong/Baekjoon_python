import sys

N = int(input())
l = []

for i in range(N):
    n = int(sys.stdin.readline())

    for j in range(n):
        num = sys.stdin.readline().split()
        print(num)

def order(size):
    root = l[0]
    bigNum = 0
    smallNum = 0

    if l[1] > root:
        big = l[1]
        
        for i in range(2,size+1):
            if l[i] > root:
                continue
            elif l[i] < root:
                small = l[i]

    elif l[1] < root:
        small = [1]

        for i in range(2,size+1):
            if l[i] < root:
                continue
            elif l[i] > root:
                big = l[i]

    for i in range(2,size+1):
        if l[i] > root:
            bigNum += 1

        elif l[i] < root:
            smallNum += 1



    

