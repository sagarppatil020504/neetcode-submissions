class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binSearchR(l,r,t):
            while (l!=r):
                mid = (l+r)//2
                if numbers[mid+1] > t:
                    r=mid
                else:
                    l=mid+1
            return l, numbers[r] == t
        
        def binSearchL(l,r,t):
            while (l!=r):
                mid = (l+r)//2
                if numbers[mid] >= t:
                    r=mid
                else:
                    l=mid+1
            return l, numbers[l] == t
        
        n = len(numbers)
        left = 0
        right = n-1
        bsl = numbers[left] + numbers[right] < target
        while True:
            if bsl:
                left, found = binSearchL(left, right-1, target - numbers[right])
            else:
                right, found = binSearchR(left+1, right, target - numbers[left])

            if found:
                return [left+1, right+1]
            bsl = not bsl
            

                
        