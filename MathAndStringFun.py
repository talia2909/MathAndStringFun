# Q1-function that count the number of letters that different from low case
def f1(x):
    count = 0
    c1 = 0
    for i in range(0, len(x)):
        if x[i].isalpha() == True:
            c1 = c1 + 1
            if x[i] == 'a' or x[i] == 'e' or x[i] == 'i' or x[i] == 'o' or x[i] == 'u' or x[i] == 'y':
                count = count + 1
    return c1 - count


def f2(x, n):
    sum = 0
    if x <= -1:
        return False
    for i in range(1, n + 1):
        if i % 2 == 0:
            sum = sum - (x ** i) / i
        else:
            sum = sum + (x ** i) / i
    return sum


def f3(x):
    list1 = []
    list2 = []
    plist = x.split()

    list2 = plist[0::2]
    list1 = plist[1::2]
    list1 = [x.lower() for x in list1]
    list2 = [x.upper() for x in list2]
    list1.sort(reverse=True)
    list2.sort()
    list3 = list2 + list1
    ans = ' '.join([str(elem) for elem in list3])
    return (ans)


def f4(x):
    counter = 0
    ispolind = ispolindrom(x)
    while counter < 500:
        if ispolind == -1:
            return counter
        else:
            counter = counter + 1
            ispolind = ispolindrom(ispolind)
    return True


def ispolindrom(y):
    num = y
    revy = 0
    while y > 0:
        revy = y % 10 + revy * 10
        y = y // 10
    if num == revy:
        return -1
    else:
        return revy + num


inq = 0
ques = int(input())
if ques == 1:
    inq = 1
    mah = input()
    print(f1(mah))
if ques == 2:
    inq = 1
    p = float(input())
    order = float(input())

    if (p <= 0.7) and (p >= -0.7) and (order > 0) and int(order) == order:
        order = int(order)
        print(f2(p, order))
    elif (p <= 0.7) and (p >= -0.7) and (order == 0):
        print('0')
    else:
        print("error")
    exit()
if ques == 3:
    inq = 1
    stri1 = input()
    print(f3(stri1))
    exit()
if ques == 4:
    inq = 1
    numb = int(input())
    print(f4(numb))
    exit()
if inq == 0:
    print('error')
    exit()