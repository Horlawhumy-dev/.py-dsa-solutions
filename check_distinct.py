def solution(s):
    count = 0
    if len(s) == 1:
        return 0
    for i in range(len(s)-2):
        for j in range(i+2, i-1, -1):
            if s[j] == s[j-1] or s[j-1] == s[j-2] or s[j] == s[j-2]:
                count -= 1
            break
        count += 1
    return count
