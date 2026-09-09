class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        n = len(password)
        if n < 8:
            return False
        special_char = "!@#$%^&*()-+"
        has_digit = False
        has_upper = False
        has_lower = False
        has_special = False
        for i in range(len(password)):
            c = password[i]
            if c.isdigit():
                has_digit= True
            if c.isupper():
                has_upper= True
            if c.islower():
                has_lower= True
            if c in special_char:
                has_special= True

            if i > 0 and password[i] == password[i-1]:
                return False
        return has_digit and has_upper and has_lower and has_special 