def count_substring(string, sub_string):
    sublen = len(sub_string)
    count = 0
    for i in string:
        if(string.startswith(sub_string, i, i + sublen)):
            count+= 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)