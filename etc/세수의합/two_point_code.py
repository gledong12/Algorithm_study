def threeSum(nums):
    results = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = 0, len(nums)-1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum > 0:
                left += 1
            elif sum <0:
                right -=1
            else:
                # 정답인 경우
                results.append((nums[i], nums[left], nums[right]))

                # 정답인 경우 skip 처리하기
                while left < right and nums[left] == nums[right +1]:
                    left +=1 
                while left < right and nums[right] == nums[right -1]:
                    right -=1
                left +=1
                right -=1
    return results
