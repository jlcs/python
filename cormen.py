def longestpalindrome(s):
    # Find longest palindromic substring in the string s

    length_s = len(s)
    sub_lp = {} #sub_lp{(i,l)} contains the longest palidromic substring of s[i:i+l]

    for i in range(length_s):
        sub_lp[(i,1)] = s[i] 

    for l in range(2, length_s+1):
        for i in range(length_s - l+1):            
            c = s[i+l-1]
            previous = sub_lp[(i,l-1)]
            try:
                prefix = s[i:i+l-1]
                first_c_in_prefix = prefix.index(c)
                length_after_first_c_in_prefix = (len(prefix)-1) - (first_c_in_prefix+1) + 1
                candidate = c+c if length_after_first_c_in_prefix == 0 else c + sub_lp[(i+first_c_in_prefix+1, length_after_first_c_in_prefix)] + c
            except ValueError:
                sub_lp[(i,l)] = previous
                continue
            sub_lp[(i,l)] = candidate if len(candidate) >= len(previous) else previous

    return sub_lp[(0,length_s)]
                
