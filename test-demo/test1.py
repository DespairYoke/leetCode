# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


def twoSum(nums,target):
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = i
    for i in range(len(nums)):
        d = target - nums[i]
        if d in dic.keys() and i != dic[d]:
            return [i,dic[d]]
if __name__ == '__main__':
    print(twoSum(nums=[3, 2, 4], target=6))
