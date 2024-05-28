

def count_substring(string, sub_string):
    str_len = len(string)
    substr_len = len(sub_string)
    
    if substr_len > str_len:
        return 0
    else:
        ngrams = []
        for i in range(0, str_len - substr_len + 1):
            ngrams.append(string[i:i+substr_len])
        return len([ x for x in ngrams if x == sub_string ])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
