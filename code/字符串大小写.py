# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。
inputOut = input("请输入：")
if inputOut:
    with open("test", 'w', encoding="utf-8") as stream:
        stream.write(inputOut.upper())
