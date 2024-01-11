#使用chatgpt，沒有修改程式碼
暴力法:
‵‵‵
def brute_force_solve_quadratic(a, b, c):
    solutions = []
    for x in range(-1000, 1001):  # 在範圍內列舉可能的 x 值
        if a * x**2 + b * x + c == 0:  # 檢查是否滿足方程
            solutions.append(x)
    return solutions

# 對於方程 x^2 - 3x + 1 = 0
a = 1
b = -3
c = 1

solutions_brute_force = brute_force_solve_quadratic(a, b, c)
print("暴力解法的解：", solutions_brute_force)
‵‵‵
迭代法:
‵‵‵
def newton_solve_quadratic(a, b, c, initial_guess, tolerance=1e-6, max_iterations=1000):
    x = initial_guess
    for _ in range(max_iterations):
        fx = a * x**2 + b * x + c
        f_prime_x = 2 * a * x + b

        if abs(fx) < tolerance:
            return x  # 解足夠接近，返回解

        x = x - fx / f_prime_x  # 更新 x

    return None  # 未找到足夠接近的解

# 對於方程 x^2 - 3x + 1 = 0
a = 1
b = -3
c = 1

initial_guess = 0  # 初始猜測
solution_newton = newton_solve_quadratic(a, b, c, initial_guess)
print("迭代法的解：", solution_newton)
‵‵‵
