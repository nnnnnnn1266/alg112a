#chatgpt撰寫
#牛頓法
def polynomial(coeffs, x):
    # 計算多項式的值
    result = 0
    for i, coeff in enumerate(coeffs):
        result += coeff * (x ** i)
    return result

def derivative(coeffs):
    # 計算多項式的導數
    return [i * coeff for i, coeff in enumerate(coeffs)][1:]

def newton_method(coeffs, initial_guess, tolerance=1e-6, max_iterations=100):
    x = initial_guess
    for _ in range(max_iterations):
        fx = polynomial(coeffs, x)
        f_prime_x = polynomial(derivative(coeffs), x)

        if abs(f_prime_x) < tolerance:
            break

        x -= fx / f_prime_x

        if abs(fx) < tolerance:
            break

    return x

# 範例使用
# 多項式 p(x) = x^3 - 6x^2 + 11x - 6
coefficients = [1, -6, 11, -6]
initial_guess = 2.0
root = newton_method(coefficients, initial_guess)

print(f"The root of the polynomial is approximately: {root}")
