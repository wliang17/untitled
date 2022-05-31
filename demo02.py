# 字符串格式化
str='请输入你的名字：%s' % ('张三')
print(str)

#整数格式化
str1='你的年龄是：%d' % (22)
print(str1)

#浮点数格式化
str2='你的余额为：%f' % (23.33)
print(str2)

# #显示辅助指令m.n:   其中m是宽带，n是保留小数位数
str3='苹果的价格是：%4.3f元' % (4.98)
print(str3)

#显示左对齐：
str4='苹果的价格是：%-12.3f元' % (4.98)
print(str4)

#正数面前显示+号：+
str5='苹果的价格是：%-+12.3f元' % (4.98)
print(str5)

#正数面前显示空格：
str6='苹果的价格是：%     4.3f元' % (4.98)
print(str6)

#前面使用0代替空格
str7='苹果的价格是：%012.3f元' % (4.98)
print(str7)

#其他格式化方法：{}.format（）
str8='苹果的价格是：{}元'.format(4.98)
print(str8)

#其他格式化方法：{}{}.format（参数1，参数2）
str9='今天星期{}，苹果的价格是：{}元'.format(1,4.98)
print(str9)

#format格式化里面的位置参数：{0}{1}.format（第一个数，第二个数）
str10='今天星期{1}，苹果的价格是：{0}元'.format(1,4)
print(str10)


#format格式化里面的变量参数：{x}{y}.format（x=''，y=''）
str11='今天星期{x}，苹果的价格是{y}元'.format(x='一',y='4.98')
print(str11)

#format和input一起用
x=input('请输入今天周几：')
y=input('请输入今天苹果的价格：')
str12='今天星期{x}，苹果的价格是{y}元'.format(x,y)
print(str12)