import math
import random
from gmssl import sm3, func

def getRandomList(n):
    """集合方式实现生成n个随机数"""
    numbers = []
    m = n**(2)
    while len(numbers) < n:
        i = random.randint(0, m-1)
        if i not in numbers:
            numbers.append(i)
    return numbers

def brithAttack(n):
    samevalue_x = []
    sameindex_x = []
    while(len(samevalue_x) == 0):
        sqrt_n = int(math.sqrt(2**n))
    #建立两个列表，其中一个存储不同的hash值，另一个存储碰撞的hash值
        list_x_value = []
        list_x_index = []
        list_x = getRandomList(sqrt_n)#随机选取在[0，2^n)中2^(n/2)个随机数
        for i in range(sqrt_n):
            str_x = list_x[i].to_bytes(64 ,"big")
            result = sm3.sm3_hash(func.bytes_to_list(str_x))[:int(n/4)]
            if i not in list_x_value:
                list_x_value.append(result)
                list_x_index.append(list_x[i])
                print("失败")
            else:
                samevalue_x.append(result)
                sameindex_x.append(list_x[i])
                print("成功")

    return True


if __name__ == '__main__':
    n=16
    while True:
        if brithAttack(int(n)):
            break

