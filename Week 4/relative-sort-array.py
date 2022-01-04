class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        relArray = []
        temp = []
        for i in arr2:
            if i in count:
                relArray.extend([i]*count[i])
                count.pop(i)
                
        for key in count:
            temp.extend([key]*count[key])
            
        relArray.extend(sorted(temp))

        return relArray
© 2022 GitHub, Inc.
Terms
Privacy
Security
