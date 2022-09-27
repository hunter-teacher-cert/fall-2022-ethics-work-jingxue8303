import re


def find_name(line):
    pattern = r"(Mr|Ms|Mrs\.?\s[A-Z]\w*)"
    result = re.findall(pattern,line)

    pattern=r'([A-Z]\w*\s[A-Z]\w*\s[A-Z]\w*)'
    result = result + re.findall(pattern,line)
    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)