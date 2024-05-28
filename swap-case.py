


def swap_case(s):
    result = ""
    for c in s:
        if c == c.upper():
            result += c.lower()
        else: 
            result += c.upper()
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
