def is_palindrome(num):
    if num == int(str(num)[::-1]):
        return True
    else:
        return False

def palindrome(num,s):
    if not (type(num) == type(s) == int) or num < 0 or s < 0:
        return "Not Valid"
    
    ans, num = [], max(num, 11)
    
    while len(ans) != s:
        if is_palindrome(num):
          ans.append(num)
        num += 1

    return ans