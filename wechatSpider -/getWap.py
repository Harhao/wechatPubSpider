import re
f=open('C:\\Users\\Administrator\\Desktop\\2.txt', 'r',encoding='utf-8',errors='ignore')
content=f.readlines()
key=re.sub("^Set-Cookie:",'',content[6].strip())
key=re.sub("^ wap_sid2=",'',key)
key=key.split(';')[0]
print(key)
