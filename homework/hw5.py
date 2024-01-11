#老師的程式碼，透過chatgpt加上註解並試圖理解

import random

def hillClimbing(f, p, h=0.01):
    failCount = 0
    while (failCount < 10000):
        fnow = f(*p)  # 計算目前高度
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:
            fnow = f1
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0
        else:
            failCount = failCount + 1
    return (p, fnow)

def neighbor(f, p, h):
    # 在鄰近點中找到更高的點
    n = len(p)
    index = random.randint(0, n - 1)
    delta = [-h if i == index else 0 for i in range(n)]
    p1 = [a + b for a, b in zip(p, delta)]
    f1 = f(*p1)
    return p1, f1

def f(x, y, z):
    return -1*(x**2 + y**2 + z**2)

# 初始解
initial_point = [2, 1, 3]

# 執行爬山演算法
result_point, result_value = hillClimbing(f, initial_point)

# 輸出結果
print("最終解：", result_point)
print("最終值：", result_value)
