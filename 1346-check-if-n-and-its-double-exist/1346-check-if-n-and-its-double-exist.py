class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            temp = arr[i] * 2
            for j in range(len(arr)):
                if i != j and arr[j] == temp:
                    return True

        return False