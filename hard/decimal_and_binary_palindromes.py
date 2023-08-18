def palindrome_type(n):
    s_num = str(n)
    binary_num = bin(n)[2:]
    if s_num[::-1] == s_num and binary_num[::-1] == binary_num:
        return "Decimal and binary."
    elif s_num[::-1] == s_num and binary_num[::-1] != binary_num:
        return "Decimal only."
    elif binary_num[::-1] == binary_num:
        return "Binary only."
    else:
        return "Neither!"


print(palindrome_type(1306031))
print(palindrome_type(427787))
print(palindrome_type(313))
print(palindrome_type(934))
