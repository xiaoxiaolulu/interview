# 判断 101-200 之间有多少个素数，并输出所有素数
# 提示：质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数。

count = 0
t = []
for i in range(101, 201):

    for j in range(2, i):  # 2-i的范围保证了除数不是1以及本身

        if i % j == 0:
            break
    else:
        count += 1
        t.append(i)
else:
    print(count)
    print(t)
