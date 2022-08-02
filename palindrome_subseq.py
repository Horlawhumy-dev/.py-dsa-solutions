
def palindrome_subsequence(s):
    """"
        @params - s is string 
        @returns - count of subsequences of length 5 from string s
    """
    count = 0
    subseq_list = get_subseq_list(s)

    for el in subseq_list:
        if is_palidrome(el):
            count += 1
    return count


def get_subseq_list(s):
    subseq_list = []

    i = 0
    j = i 
    last_index = len(s) -1

    while i < last_index:
        k = 0
        res = ''
        if len(s[i:]) < 5:
            break
        while k <= 4 and j <= last_index:
            res += s[j]
            j += 1 
            k += 1
        subseq_list.append(res)
        i += 1
        j = i
    return subseq_list


def is_palidrome(sub):
    temp_sub = sub
    rev_sub = "".join(reversed(sub))
    if temp_sub == rev_sub:
        return True 
    return False

print(palindrome_subsequence("01010101"))

# "01010"
# "10101"
# "01010"
# "10101"
