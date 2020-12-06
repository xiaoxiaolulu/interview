# 从长度为1万的有序且有重复数字的列表找出第一个0前面的一位数字和最后一个0后面的一个数字，例如[...,-1,0,0,0,6,...]打印-1和6
arr = [-3, -2, -12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 61, 6, 7]
for i in range(len(arr)):
    if arr[i] == 0:
        if arr[i - 1] != 0:
            print(arr[i - 1])
        elif arr[i + 1] != 0:
            print(arr[i + 1])
            break

#  有两个磁盘文件 A 和 B,各存放一行字母,要求把这两个文件中的信息合并 (按字母顺序排列), 输出到一个新文件 C 中

with open("xx/A") as a:
    content_a = a.readlines()
with open("xx/B") as b:
    content_b = b.readlines()
content_c = sorted(content_a + content_b)
c = open("xx/C", 'w')
result = c.write(content_c)
a.close()
b.close()
c.close()

# 现在有一个未知大小的日志文件 (可能 100G)，要求如果日志文件有包含字符串'error'的行，输出前后 3 行 (包括字符串所在行) 到新的文件中，
# 问怎么实现，用 Python 实现，需要手写到纸上

# 实现就行不用考虑性能；O(∩_∩)O哈哈~
pattern_set = []

with open('test', 'r', encoding='utf-8') as stream:
    content = stream.readlines()

    for index, value in enumerate(content):
        if 'error' in value:
            err_before_index = index - 3
            err_after_index = index + 3
            pattern_set.extend(content[err_before_index: index])
            pattern_set.append(content[index])
            pattern_set.extend(content[index + 1: err_after_index + 1])

for content_value in pattern_set:
    print(content_value.strip())


# 统计字符串里的字母个数怎么测试？
# 可以通过字符在ASCII码表里有序号一一对应来判断，就不用写太多if判断了
# a~z小写英文字母的取值范围为97~122
# A~Z大写英文字母的取值范围为65~90
def numbercharacters(sstr):
    characters = []
    others = []
    for i in range(len(sstr)):
        if ord(sstr[i]) in range(65, 91) or ord(sstr[i]) in range(97, 123):
            characters.append(sstr[i])
        else:
            others.append(sstr[i])
    return len(characters)

print("The number of characters is " + str(numbercharacters("abc12,/'io")))
