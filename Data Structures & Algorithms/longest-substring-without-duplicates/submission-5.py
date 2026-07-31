class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # xzxyzxyz
        # curr = xz

        # x already in there
        # previous x index + 1 and include this x
        # curr = zx
        # curr = zxy
        # now we get z again, z is in window,
        # curr = xyz

        # left is 0, right keeps incrementing by one
        # right - left + 1 = current window_size

        # add nums[left] to set
        # add nums[right] to set
        # when checking nums[right], we ask if nums[right] in set
        # if yes, contract the window, left = 
        # if no keep adding
        # increasing window size


        mp = {}
        left,curr_window = 0, 0
        max_window = 0
        # mp[s[left]] = 0
             # "pwwkew"
            #  s="abaac"
        
        for right in range(len(s)):
            if s[right] in mp and mp[s[right]] >= left:
                    index = mp[s[right]]
                    left = index + 1
            
            mp[s[right]] = right
            curr_window = right - left + 1
            max_window = max(curr_window, max_window)

        return max_window



        # "pwwkew"
        # pw
        # w problem right here, how
        # wk
        # wke
        # kew
        # using a hash map to keep storing the chars
        # and their index

        # go through the string, if char in dict
        # dict[char] will give index





        