# 示例： a + b = a * b
def mul(x, y):
    s = x
    for i in range(abs(y) - 1):
        s += x
    return s

