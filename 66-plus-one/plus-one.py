class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last_digit = digits[-1]
        new_last_digit = last_digit + 1
        new_list = digits[:]
        new_list[-1] = new_list[-1]+1
        for i in range(len(new_list) - 1, -1, -1):
            if new_list[i] == 10:
                new_list[i] = 0
                if i == 0:
                    new_list.insert(0, 1)
                else:
                    new_list[i - 1] += 1

        return new_list