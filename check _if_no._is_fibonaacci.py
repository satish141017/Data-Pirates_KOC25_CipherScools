def is_fibonacci(n):
    temp = n
    start = 0
    nstart = 1
    if (n == 0 or n == 1):
        return True
    while n > 0:
        next = start + nstart
        if next == temp:
            return True
        start = nstart
        nstart = next
        n = n - 1
    return False


n = input("Enter number/ numbers : ")
l1 = list(n.split(" "))
for i in range(len(l1)):
    if is_fibonacci(int(l1[i])):
        print("---> ", l1[i], "--> ", "Fibonacci number")
    else:
        print("---> ", l1[i], "--> ", "Not a Fibonacci number")