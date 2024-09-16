def reverse(s):
    if len(s) == 0:
        return ""
    else:
        return reverse(s[1:]) + s[0]
    
print(reverse('yonara'))