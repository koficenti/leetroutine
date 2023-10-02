# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
# Runtime: 90ms ( Beat 99.73% )

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = dict()
        perms = 0

        for char in set(s):
	        freq[s.count] = char
	        count = s.count(char)
	        while freq.get(count, None) != char and count in freq:
		        count -= 1
		        perms += 1
	        if count != 0:
		        freq[count] = char

        return perms
