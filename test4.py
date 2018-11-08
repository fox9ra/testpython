import re; 
print(re.sub(r'(.)(\1)+|(.)', lambda m: m.group(0)[0] + str(len(m.group(0))), input()))