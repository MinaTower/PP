import re
flag = int(0)
reg = r'1([01]+)'
with open('inp_file.txt', 'r') as file:
    for line in file:
        strok = line
        while ((re.search(reg, strok) != None) and not flag):
            m = re.search(reg, strok)
            de = strok[int(m.start()): int(m.end())]
            for i in range (2, len(de)+1):
                a = int(de[:i], 2)
                if (a%3 == 0):
                    flag = True
                    break;
                strok = strok[:m.start()]+strok[m.end():]
        if flag:
            if line[-1] == '\n': line = line[:-1]
            print(line)#
        flag = False
