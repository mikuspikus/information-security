def generate_OTPs(initial_number, period = 100, p = 5923 , m = 12619):
    def _make_pwd(old_pwd, p, m):
        return ((old_pwd % m) ** p) % m

    pwds = [initial_number]
    for i in range(0, period + 1):
        pwds.append(_make_pwd(pwds[-1], p, m)) # <- appendr
    
    return pwds[::-1] #<- reverse list with slice