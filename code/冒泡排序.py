# 使用你熟悉的语言写一个冒泡排序，数组A排序，int[]={11，2，5，82，7，0，4，89，72，42}
def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    print(bubble_sort([11, 2, 5, 82, 7, 0, 4, 89, 72, 42]))
