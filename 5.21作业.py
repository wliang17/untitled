# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
a=int(input('请输入一个整数：'))
b=int(input('请输入一个整数：'))
c=int(input('请输入一个整数：'))
d=int(input('请输入一个整数：'))
print('a+b-c*d=',a+b-c*d)
print('===========================')
# 2. 打印1~100内被3整除的所有数的和 。
aa=0
sum=0
for aa in range(1,101):

    if aa % 3 == 0:
        sum+=aa
print('1-100以内被3整除的数的和为：',sum)
print('===========================')

# 3. 使用range()输出1~10内的所有奇数 。
for a2 in range(1,11,2):
    print('输出1-10内的所有奇数：',a2)
print('===========================')
# 4. 打印1~100所有偶数的和 减去 所有奇数的和 的值
a3=0
sum1=0
while a3 <=100:
    if a3%2 == 0:
        sum1+=a3
    a3+=1
print('打印1~100所有偶数的和:',sum1)

a4=0
sum2=0
for a4 in range(1,101):
    if a4 % 3 == 0:
        sum2+=a4
print('打印1~100所有偶数的和 减去 所有奇数的和 的值:',sum1-sum2)
print('===========================')

# 5. 求1+2+3+...+100的和
a5=0
sum3=0
for a5 in range(1,101):
    sum3+=a5
print('1-100的求和:',sum3)

# 6. 判断一个数n能同时被3和5整除
N = int(input('请输入一个整数：'))

if N%3==0 and N%5==0:
    print('这个数能被3和5整除')
else:
    print('这个数不能被3和5整除')

exit()

# 7. 定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
A = int(input('请输入一个整数：'))
if A in range(1,101):
    print('这个数在1-100内，且是：',A)
else:
    print('这个数不在1-100内')
exit()


# 8. 输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
X = int(input('请输入一个整数'))
Y = int(input('请输入一个整数'))
Z = int(input('请输入一个整数'))
A=[X,Y,Z]
A.sort()
print(A)
exit()


# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，
# 60分以下的用C表示。备注：需要使用input()方法


score = int(input('请输入您的成绩：'))
if score>=90:
    print(score,'-----A')
elif score>=60 and score<=89:
    print(score,'-----B')
else:
    print('成绩不合格')
exit()



# 10. 将一个列表的数据复制到另一个列表中。
alst = [1,2,3,4]
blst = ['a','b','c']
alst.extend(blst)
print(blst)
print(alst)


# 11. 输出 9*9 乘法口诀表。
for x in range(1,10):
    for y in range(1,x+1):
        print(y,' * ',x,'=',x*y,end='  ')
    print()



# 12. 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
alpha=0
number=0
space=0
other=0
str = input('请输入一行字符：')
for i in str:
    if i.isalpha():
        alpha+=1
    elif i.isdigit():
        number+=1
    elif i.isspace():
        space+=1
    else:
        other+=1
print('字母出现的个数为：',alpha)
print('数字出现的个数为：',number)
print('空格出现的个数：',space)
print('其他字符出现的个数：',other)



# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个
# 数相加)，几个数相加由键盘控制。

a = input('请输入要相加的数字:')
b = int(input('请输入要相加的个数:'))

res=[]
for i in range(1,b+1):
    res.append(int(a*i))

print(res)
sum(res)
print(sum(res))




# 14. 题目：打印出如下图案（菱形）:
str1='*'
alst1=[x for x in range(1,8,2)]
alst1.extend([y for y in range(5,0,-2)])
print(alst1)
for i in alst1:
    print((str1*i).center(7))