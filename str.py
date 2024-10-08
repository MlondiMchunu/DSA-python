class Solution:

    def compress(s):
        res = ""
        count = 1

        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count+=1
            else:
                res = res + s[i-1] #for appending characters to string
                if count > 1:
                    res = res + str(count) #for appending character count to string
                count = 1

        res = res + s[-1]
        if count > 1:
            res = res + str(count)
        return res


if __name__ == "__main__":

    sc = Solution

    print(sc.compress("ooplllzdbbn"))