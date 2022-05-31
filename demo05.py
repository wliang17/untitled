#列表推导式： [表达式2 循环体 表达式1]  先执行循环体，再执行表达式1，最后执行表达式2

# 需求1:创造一个列表包含1-10
alst=[x for x in range(1,11) ]
print(alst)

# 需求2:创造一个列表包含1-10，打印奇数
blst=[x for x in range(1,11) if x%2!=0]
print(blst)

# 需求3:创造一个列表包含1-10，打印奇数后再加10
clst=[x+10 for x in range(1,11) if x%2!=0]
print(clst)
print('='*100)
# 题 ：将后面的字符串转化为12345“[1,2,3,4,5]” ==> 12345
lst1=[1,2,3,4,5]
lst2=str(lst1)
print(lst2[1::3])
