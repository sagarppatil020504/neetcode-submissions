class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        base= {}

        for i in strs:
         
            word = "".join(sorted(i))

            if word in base:
                base[word].append(i)
            else: 
                base[word] = [i]

        return list(base.values())