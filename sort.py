# John Loeber | contact@johnloeber.com | Python 2.7.9 | September 2, 2015

with open('words.txt','r') as f:
    lines = f.readlines()
    print lines
print lines
separate = lines.index(' \n')
words = lines[:separate].sort()
with open('words.txt','w') as g:
    for word in words:
        g.write(word)
    for line in lines[separate]:
        g.write(line)
