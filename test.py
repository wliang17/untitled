
# print("hello world")
# True
# print(type('你好'),type(121))
# a= 5
# b = 16
# c = 12.3
# d = 'hello world'
#
# print(b // a)
# print(b % a)
# print(a ** b)
# print(a > b)
# print(a <= b)
# print(a == b)
# print(a != b)
# print(a is b)
# print(a is not b)
# a -= b
#
# print(a)
# a1=2
# a2=9
# a2 *= a1
# print(a2)
#
# aa1 = 2
# aa2 = 9
# aa2%=aa1
# print(aa2)
#
# aaa1 = 2
# aaa2 = 9
# aaa2**=aaa1
# print(aaa2)
# print(aaa2 and aaa1)
# print(aaa2 or aaa1)
# print(a,b,c,d)

# e= a + c
# f= 1==c
# g,h=a+e,'牌神'
# print(e)
# print(g,h)


# a=10
# b=18
# if a>b:
#     print('这个数大于18')
# else:
#     print('这个数小于18')

# score = 76
# if score > 90:
#     print('优秀')
# elif score > 80:
#     print('良好')
# elif score > 60:
#     print('及格')
# else:
#     print('不及格')
#
# if 0.001:
#     print('kong')
# elif 'qwe':
#     print('hahaha')
# else:
#     print('meiyou')
# modle='abcdefg'
# for i in modle:
#     print(i)

# 练习：计算1~100内所有数的和
# a=0
# b=0
# while a<100:
#     a=a+1
#     b=b+a
# print(b)

# rangefangfa
# a=0
# for i in range(1,101):
#     a+=i
# print(a)

# sum方法
# print (sum(range(1,101)))

# for i in range(1,11):
#     print(i)
#     if i == 7:
#         break

# alst = []
blst = [11,22.2,True,None]
# print(alst)
# print(blst)
#
# for i in blst:
#     print('列表中的元素有','.',i)


clst = ['red','blue','black']
clst.append('green')
print('在列表末尾添加新元素的结果：',clst)

print(clst.count('green')) #计数

clst.extend(blst) #扩展列表
print('扩展列表后的结果：',clst)

print(clst.index(11)) #clst.index()查询列表中某个元素的位置

clst.insert(1,'white')
print('在列表第2个位置插入一个元素的结果：',clst)

# 翻转列表中的内容
clst.reverse()
print(clst)


#删除列表某个位置的值
clst.pop(0)
print('删除clst中第一位元素后的结果：',clst)

# 删除列表中特点元素
clst.remove('white')
print('删除列表中特点元素后的结果：',clst)

