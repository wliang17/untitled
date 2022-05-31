
#序列的通用操作，索引
a=(1,2,3,'abc')
print(a[1])

#序列的切片lst[start:end:step] start是包括当前值的,默认0，end是不包括的，默认为序列长度,step默认为1
lst5 = ['red','green','blue','black','gold','orange']
print(lst5[1:5:1])
print(lst5[0::2]) #省略end的位置
print(lst5[::])    #全省略
print(lst5[:3:])    #省略start和step

################################
print('=========='*6)
lst6=[]
for i in range(1,11):
    lst6.append(i)

print(lst6)

string='hello'
string1='world'
print(string+string1)


lst7 = ['red','green','blue','black','gold','orange']

# 题 ：将后面的字符串转化为12345“[1,2,3,4,5]” ==> 12345
lst1=[1,2,3,4,5]
lst2=str(lst1)
print(lst2)

