##归并排序：分而治之
##  将包含N个元素的列表拆分成两个含N/2个元素的子列表
##  对两个子列表递归调用归并排序（最后可以将整个列表分解为N个子列表）
##  合并两个已排好序的子列表

def merge(left, right):
    merged = []         #合并两个列表
    i, j = 0, 0         #i和j分别作为left和right的下标
    left_len, right_len = len(left), len(right)  #分别获取左右子列表的长度
    while i < left_len and j < right_len:        #循环归并左右子列表元素
        if left[i] <= right[j]:
            merged.append(left[i])   #归并左子列表元素
            i += 1
        else:
            merged.append(right[j])  #归并右子列表元素
            j += 1
    merged.extend(left[i:])   #归并左子列表剩余元素
    merged.extend(right[j:])  #归并右子列表剩余元素
    print(left,right,merged)  #跟踪调试
    return merged             #返回归并好的列表


def mergeSort(a):      #归并排序
    if len(a) <= 1:
        return a       #空或者只有1个元素，直接返回列表
    mid = len(a) // 2  #列表中间位置
    left = mergeSort(a[:mid])  #归并排序左子列表
    right = mergeSort(a[mid:]) #归并排序右子列表
    return merge(left, right)  #合并排好序的左右两个子列表


a = [98,23,45,14,6,67,33,42]
a1 = mergeSort(a)
print(a1)



##归并排序算法的分析
##  归并排序需要将列表一步步拆分成子列表，共log2N步
##  每一步都相当于需要合并N个元素的有序列表，最大比较次数是N次
##  归并排序需要至多Nlog2N次比较


"""
Python语言系统提供的排序算法：底层采用了一种归并排序算法实现


Python的列表类型提供sort()方法：

a = [98,23,45,14,6,67,33,42]
a.sort()	#默认升序排序
print(a)	#输出[6, 14, 23, 33, 42, 45, 67, 98]

a = [98,23,45,14,6,67,33,42]
a.sort(reverse=True)  #降序排序
print(a)              #输出[98, 67, 45, 42, 33, 23, 14, 6]


Python的内置函数sorted

a = [98,23,45,14,6,67,33,42]
b = sorted(a)	#降序采用sorted(a,reverse=True)
print(a)	#输出[98, 23, 45, 14, 6, 67, 33, 42]不变
print(b)	#输出[6, 14, 23, 33, 42, 45, 67, 98]

"""
