class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        count =0
        for i in range(len(arr)):
            count += 1

            if arr[i] == 0:
                count += 1
            if count >= len(arr):
                break

        j = len(arr) -1
        while j>0:
            # print(arr)
            if arr[i] != 0:
                arr[j] = arr[i]
            elif arr[i] == 0 and count > len(arr) and j == len(arr) -1:
                arr[j] = arr[i]
            else:
                arr[j] = arr[i]
                arr[j-1] =arr[i]
                j = j-1
            i -= 1
            j -= 1

        print(arr)

# Solution().duplicateZeros([1,0,2,3,0,4,5,0])
Solution().duplicateZeros([8,4,5,0,0,0,0,7])
# Solution().duplicateZeros([1,5,2,0,6,8,0,6,0])
Solution().duplicateZeros([9,9,9,4,8,0,0,3,7,2,0,0,0,0,9,1,0,0,1,1,0,5,6,3,1,6,0,0,2,3,4,7,0,3,9,3,6,5,8,9,1,1,3,2,0,0,7,3,3,0,5,7,0,8,1,9,6,3,0,8,8,8,8,0,0,5,0,0,0,3,7,7,7,7,5,1,0,0,8,0,0])