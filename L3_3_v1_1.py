import re
flag = int(0)
reg = r'1([01]+)'
#for line in file:
#str = line
strok = 's101tg100100hfdg'
str2 = strok
while ((re.search(reg, strok)!= None) and not flag):
    m = re.search(reg, strok)
    de = strok[int(m.start()): int(m.end())]
    for i in range (2, len(de)+1):
        a = int(de[:i], 2)
        if (a%3 ==0):
            flag = True
            print(a)
            #break;
    strok = strok[:m.start()]+strok[m.end():]
    if flag: print(str2)#
    flag = False
