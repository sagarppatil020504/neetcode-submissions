class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        repeater={}
        result=[]
        for i in nums:

            if i in repeater:        
                repeater[i] +=1
            else:
                repeater[i]=1

        
        for num, frequency in repeater.items():
            result.append((frequency, num))

        result.sort(reverse=True)

        return [num for frequency, num in result[:k]]
