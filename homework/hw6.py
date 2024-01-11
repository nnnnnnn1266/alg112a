#chatgpt+老師範例+參考同學程式碼

import numpy as np

def gradient_descent_optimization_with_gradient(objective_function, gradient_function, initial_solution, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
    current_solution = initial_solution.copy()

    for iteration in range(max_iterations):
        current_value = objective_function(current_solution)
        gradient = gradient_function(objective_function, current_solution)

        if np.linalg.norm(gradient) < tolerance:
            break  # 梯度足夠小，視為已收斂

        current_solution = current_solution - learning_rate * gradient

    return current_solution, objective_function(current_solution)

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    step = 0.001
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return np.array(gp)

# 以一個簡單的函數作為示例
def sample_objective_function(x):
    return x[0]**2 + x[1]**2 + x[2]**2  # 要找最小值，不需要負號

# 初始解
initial_solution = np.array([2.0, 1.0, 3.0])

# 執行梯度下降法
final_solution, final_value = gradient_descent_optimization_with_gradient(sample_objective_function, grad, initial_solution)

# 輸出結果
print("最終解：", final_solution)
print("最終值：", final_value)
