def groupAnagrams(strs):
     anagrams = []

     anagram_dict = {}

     for item in strs:
         listed = list(item)
         listed.sort()

         if str(listed) in anagram_dict:
             anagram_dict[str(listed)].append(item)
         else:
             anagram_dict[str(listed)] = [item]

     for key, val in anagram_dict.items():
         anagrams.append(val)

     return anagrams

cadena = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(cadena))