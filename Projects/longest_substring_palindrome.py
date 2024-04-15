# Longest substring palindrome
# https://leetcode.com/problems/longest-palindromic-substring/
import math

def isPalindrome(s):
    l = math.floor(len(s)/2)
    return s[l:][::-1] == s[:l] or s[l+1:][::-1] == s[:l]

    
# def getSubs(arr, s, e, subs=[]):
#     if e == len(arr):
#         return subs
#     elif s > e:
#         return getSubs(arr, 0, e + 1, subs)

#     test = arr[s:e+1]
#     if isPalindrome(test):
#         subs.append(test)

#     return getSubs(arr, s + 1, e, subs)

def getSubs(arr, s, e):
    sub = arr[0]

    c = True
    while c:
        if e == len(arr):
            c = False

        e += 1
        test = arr[s:e]

        if isPalindrome(test):
            sub = test if len(test) > len(sub) else sub

    return sub


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         return max(getSubs(s, 0, 1), key=len)

def longestPalindrome(s: str) -> str:
    N = len(s)
    if N == 0:
        return
    N = 2*N+1    # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition
    R = 2     # centerRightPosition
    i = 0    # currentRightPosition
    iMirror = 0     # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1
  
    for i in range(1,N):
        # get currentLeftPosition iMirror for currentRightPosition i
        iMirror = 2*C-i
        L[i] = 0
        diff = R - i
        # If currentRightPosition i is within centerRightPosition R
        if diff > 0:
            L[i] = min(L[iMirror], diff)
  
        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE
        # If even position, we just increment LPS by ONE without
        # any character comparison
        try:
            while ((i + L[i]) < N and (i - L[i]) > 0) and \
                    (((i + L[i] + 1) % 2 == 0) or \
                    (s[(i + L[i] + 1) // 2] == s[(i - L[i] - 1) // 2])):
                L[i]+=1
        except Exception as e:
            pass
  
        if L[i] > maxLPSLength:        # Track maxLPSLength
            maxLPSLength = L[i]
            maxLPSCenterPosition = i
  
        # If palindrome centered at currentRightPosition i
        # expand beyond centerRightPosition R,
        # adjust centerPosition C based on expanded palindrome.
        if i + L[i] > R:
            C = i
            R = i + L[i]
  
    # Uncomment it to print LPS Length array
    # printf("%d ", L[i]);
    start = (maxLPSCenterPosition - maxLPSLength) // 2
    end = start + maxLPSLength - 1
    # print ("LPS of string is " + s + " : ", s[start:end+1])
    return s[start:end+1]

print(longestPalindrome('lcnvoknqgejxbfhijmxglisfzjwbtvhodwummdqeggzfczmetrdnoetmcydwddmtubcqmdjwnpzdqcdhplxtezctvgnpobnnscrmeqkwgiedhzsvskrxwfyklynkplbgefjbyhlgmkkfpwngdkvwmbdskvagkcfsidrdgwgmnqjtdbtltzwxaokrvbxqqqhljszmefsyewwggylpugmdmemvcnlugipqdjnriythsanfdxpvbatsnatmlusspqizgknabhnqayeuzflkuysqyhfxojhfponsndytvjpbzlbfzjhmwoxcbwvhnvnzwmkhjxvuszgtqhctbqsxnasnhrusodeqmzrlcsrafghbqjpyklaaqximcjmpsxpzbyxqvpexytrhwhmrkuybtvqhwxdqhsnbecpfiudaqpzsvfaywvkhargputojdxonvlprzwvrjlmvqmrlftzbytqdusgeupuofhgonqoyffhmartpcbgybshllnjaapaixdbbljvjomdrrgfeqhwffcknmcqbhvulwiwmsxntropqzefwboozphjectnudtvzzlcmeruszqxvjgikcpfclnrayokxsqxpicfkvaerljmxchwcmxhtbwitsexfqowsflgzzeynuzhtzdaixhjtnielbablmckqzcccalpuyahwowqpcskjencokprybrpmpdnswslpunohafvminfolekdleusuaeiatdqsoatputmymqvxjqpikumgmxaxidlrlfmrhpkzmnxjtvdnopcgsiedvtfkltvplfcfflmwyqffktsmpezbxlnjegdlrcubwqvhxdammpkwkycrqtegepyxtohspeasrdtinjhbesilsvffnzznltsspjwuogdyzvanalohmzrywdwqqcukjceothydlgtocukc'))
print(longestPalindrome('a'))


class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':
        if len(s) <= 1:
            return s
        start = end = 0
        length = len(s)
        for i in range(length):
            max_len_1 = self.get_max_len(s, i, i + 1)
            max_len_2 = self.get_max_len(s, i, i)
            max_len = max(max_len_1, max_len_2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start: end+1]
        
    def get_max_len(self, s: 'list', left: 'int', right: 'int') -> 'int':
        length = len(s)
        i = 1
        max_len = 0
        while left >= 0 and right < length and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
