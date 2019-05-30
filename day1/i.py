


#字符连接模板
from day1 import base_type

if __name__ == '__main__':

    value = base_type.add(20,80)
#索引
    a = '撒拉黑呀'
    print(a[-1])
    print(a[3:])
    print(a[0])
    print(a[1])
#切片字从零开始数 取值选后一位 :号是开始取到尾
    print(a[0:4])
    print(a[2:])
    print(a[0:])
#反转 ::-1 双冒号属于反转硬规定
    print(a[::-1])