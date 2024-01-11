#程式碼由chatgpt+上課內容-->小小修改

# 方法 1
def power2n(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_rec_a(n):
    if n == 0:
        return 1
    return power2n_rec_a(n - 1) + power2n_rec_a(n - 1)

# 方法 2b：用遞迴
def power2n_rec_b(n):
    if n == 0:
        return 1
    return 2 * power2n_rec_b(n - 1)

# 方法 3：用遞迴+查表
def power2n_rec_memo(n, memo={}):
    if n == 0:
        return 1
    if n not in memo:
        memo[n] = power2n_rec_memo(n - 1, memo) + power2n_rec_memo(n - 1, memo)
    return memo[n]

# test
n = 5
print(power2n(n))
print(power2n_rec_a(n))
print(power2n_rec_b(n))
print(power2n_rec_memo(n))
