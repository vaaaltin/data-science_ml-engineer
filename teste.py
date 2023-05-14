def rotate(nums, k:int):
    result = None

    if isinstance(k, list):
        k = sum(k)
    
    n = len(nums)
    k = k % n
    
    return nums[-k:] + nums[:-k]


if __name__=='__main__':
    line = input()
    components = line.strip().split()

    nums = [int(component) for component in components]

    k = int(input())

    nums = rotate(nums, k)

    print(nums)