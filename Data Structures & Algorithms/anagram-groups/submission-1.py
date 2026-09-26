class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        
        for word in strs:
            count = [0]*26
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(word)


        output = []
        for k in my_dict:
            output.append(my_dict[k])
        return output
        


