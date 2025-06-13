def groupAnagrams_v1(strs):
        groups = {}
        
        for s in strs:
            freq = {}
            for char in s:
                freq[char] = freq.get(char, 0) + 1
            
            print(freq.items())
            key = tuple(sorted(freq.items()))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)
            # print(key)
            # print(groups[key])

        # print(list(groups.values()))
        
        return list(groups.values())

strs =["eat","tea","tan","ate","nat","bat"]

groupAnagrams_v1(strs)
