class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = x
        num_list = list(str(x))
        reverse_num_list = num_list[::-1]
        if num_list == reverse_num_list:
            return(True)
        else:
            return False