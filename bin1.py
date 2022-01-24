def decimal(num):
    if num >= 1:
        decimal(num // 2)
    print(num % 2,end="")

num=17
t=decimal(num)

