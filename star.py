
# 打印菱形
str1='*'
alst1=[x for x in range(1,8,2)]
alst1.extend([y for y in range(5,0,-2)])
print(alst1)
for i in alst1:
    print((str1*i).center(7))


