n = int(input())

lst = [input() for x in range(n)]

def fun():
    for p in lst: 
        if len(p) <= 10:
            print(p)
        else:
            print(p[0] + str(len(p)-2) + p[len(p)-1])








