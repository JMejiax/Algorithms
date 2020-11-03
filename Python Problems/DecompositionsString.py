
def is_palindrome(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return is_palindrome(s, l+1, r-1)

def deco(arr, s, pos, curr_deco):
    if pos == len(s):
        arr.append(curr_deco)
        return
    for i in range(pos, len(s)):
        if is_palindrome(s, pos, i):
            if pos == 0:
                deco(arr, s, i+1, s[pos:i-pos+1])
            else:
                new_curr = curr_deco + '|' + s[pos:i+1]
                deco(arr, s, i+1, new_curr)


s = input()
arr = []
deco(arr, s, 0, '')
print(*arr, sep='\n')
print(is_palindrome(s, 0, len(s)-1))

