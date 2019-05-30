print('hello world')

# 写方法 def:关键字, int_demo:名字, ():内容
def zhou_demo():
    # 声明一个变量(变量名)=aint/zhou  =(变量值) int/zhou类型的5
    zhou = 5
    # type(zhou): 获取zhou的数据(变量),Print:打印类型
    print(type(zhou))
def str_join():
    a = 2323
    b = '宝宝'
    c = '乖啊'
    print(b+c)
    print(str(a)+b)
    print('%s,%s'%(a,b))
    print(b + c)
def add(num1,num2):
    print(num1)
    print(num2)
    print(num1+num2)
    return num1+num2
def zhuanhuan():
    a = 50
    print(type(a))
    print(type(str(a)))

def zhou():
    a = 3.1415
    print(type(a))
def zhuanhuan1():
    a = '50'
    print(type(a))
    print(type(int(a)))

def test1():
    print('test1')
def test2():
    print('test2')
def test3():
    print('test3')
# main方法可以直接执行,不可再使用其他方法,否则会报错
if __name__ == '__main__':
# print:打印
    print('hello world')
    zhou_demo()
    test3()
    test1()
    test2()
    zhuanhuan()
    zhou()
    zhuanhuan()
    str_join()

    a = str_join()
    b = add(2,8)
    print('----')
    print(a)
    print(type(a))
    print(b)


