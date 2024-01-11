#chatgpt撰寫+看過老師範例，稍微有些看不懂，沒有更改
def permute(nums):
    result = []
    generate_permutation(nums, 0, result)
    return result

def generate_permutation(nums, index, result):
    if index == len(nums):
        result.append(nums.copy())  # 將當前排列加入結果
        return

    for i in range(index, len(nums)):
        # 交換元素，進行遞迴
        nums[index], nums[i] = nums[i], nums[index]
        generate_permutation(nums, index + 1, result)
        # 回溯，撤銷交換
        nums[index], nums[i] = nums[i], nums[index]

# 測試
nums = [1, 2, 3]
result = permute(nums)
print(result)

