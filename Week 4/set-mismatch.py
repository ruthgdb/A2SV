cmp = list(range(1, len(nums)+1))
        c = Counter(nums)
        for i in range(len(nums)):
            if(c[nums[i]] == 2):
                res.append(nums[i])
                nums[i] = len(nums)+1
                break
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] != cmp[i]):
                res.append(cmp[i])
                break
        return res