import sys

l =[]

while True:
    try:
        n = int(input())
        l.append(n)

    except:
        break

def postorder(first, end):
    if first > end:
        return

    root = end+1

    for i in range(first+1, end+1):
        if l[first] < l[i]:
            root = i
            break

    postorder(first+1, root-1)
    postorder(root, end)
    print(l[first])

postorder(0, len(l)-1)

