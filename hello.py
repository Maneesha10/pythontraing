

for num in range(2,1001):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


#break,continue,pass
for h in range(10):
    print(h)
    break
print("hello")