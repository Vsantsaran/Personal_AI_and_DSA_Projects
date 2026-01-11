# Automorphic number
def is_automorphic(num):
    l = []
    sqr = num ** 2
    while sqr%10:
        r = sqr % 10
        l.append(r)
        sqr //= 10
    if len(l) >= 2:
        f = l[1]
        s = l[0]
    else:
        return False
    l.clear()
    temp = num
    while temp % 10:
        r = temp % 10
        l.append(r)
        temp //= 10
    f1 = l[1]
    s1 = l[0]
    if f is f1 and s is s1:
        return True
    return False

if __name__ == '__main__':
    num = int(input('Enter number: '))
    if not num%10 or num//10 == 0:
        print('no')
        exit(0)
    if is_automorphic(num):
        print('yes')
    else:
        print('no')