class Solution:
    def smallestNumber(self, num: int) -> int:
        neg = 1 if num >= 0 else -1

        if neg < 0:
            num = -num

        s_num = sorted([int(x) for x in str(num)])

        if len(s_num) == 1:
            return neg * s_num[0]
        
        if neg > 0:
            i = j = 0
            while s_num[i] == 0:
                i += 1
            s_num[i], s_num[j] = s_num[j], s_num[i]
        else:
            s_num = s_num[::-1]

        return neg * int(''.join([str(x) for x in s_num]))



