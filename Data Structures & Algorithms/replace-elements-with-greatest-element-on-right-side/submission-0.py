class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        tmp_max = -1
        for i in range(len(arr) -1, -1, -1):
            tmp = arr[i]
            arr[i] = tmp_max
            tmp_max = max(tmp, tmp_max)


            

        return arr
                