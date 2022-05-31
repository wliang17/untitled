def add(x,y):
    try:
        z=x/y
        print(z)
        return z

    except Exception as e:
        print(e)

    finally:
        print('您没有正确执行函数')


if __name__ == '__main__':

    add(4,5)
    add(4,0)
    add(1,8)

