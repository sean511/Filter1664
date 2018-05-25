#Sean Kessinger @ MGSU
#Python 3.6.4
import binascii
import base64
x, i, d, o, p, q, r, s, t, u, v, w, y, z, flag = '', 0, [], [], [], [], [], [], [], [], [], [], [], [], []
b16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f','A', 'B', 'C', 'D', 'E', 'F']
b64 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '+', '/', '=']
yes = ['y', 'yes', 'Y', 'YES']
no = ['n', 'no', 'N', 'NO']
file = input('\n\n\tThis program filters possible Base16(Hexadecimal) and Base64 strings then can sort them and search for user set flags.\n\n\t\tMake sure the file you want to filter is in the currently set directory.\n\n\tName any file with any extension you want to filter (E.g. file.pcap): ')
if file == '':
    print ('\n\n\tTry entering a file name next time.')
    input('\n\n\tPress ENTER to exit. . . ')
    exit()
else:
    try:
        f = open(file, 'r', encoding='latin-1').read()
    except:
        print ('\n\n\tERROR: "Make sure the file you want to filter is in the currently set directory."\n\n\t\tIn Windows use "cd [full path of the file you want to filter]" without brackets or quotes.')
        input('\n\n\tPress ENTER to exit. . . ')
        exit()
a = input ('\n\tExclude duplicate results and sort? (y/n): ')
if a == '':
    print ('\n\t\tNothing to say? I\'ll take that as a "no".')
elif a in yes:
    a = True
    print ('\n\t\tOK. I will get rid of duplicate results and sort by ascending length then alphabetically.')
elif a in no:
    print ('\n\t\tOK. I won\'t get rid of duplicate results and I\'ll leave the order alone.')
else:
    print ('\n\t\tWhat? I\'ll take that as a "no".')
b = input ('\n\tLooking for a flag? (y/n): ')
if b in yes:
    b = True
    c = input ('\n\n\tWhat to look for in a flag? (E.g. mgactf): ')
    if c != '':
        flag_filter = list(c)
        print ('\n\t\tOK. I\'ll filter for strings that contain "', c, '".')
    else:
        print ('\n\t\tYou didn\'t tell me what to look for, so I won\'t filter for possible flags.')
        b = False
elif b in no:
    print ('\n\t\tOK. I won\'t filter for possible flags')
    b = False
elif b == '':
    print ('\n\t\tNothing to say? I\'ll take that as a "no".')
    b = False
else:
    print ('\n\t\tWhat? I\'ll take that as a "no".')
    b = False
print('\n\t%s' %(file), 'found!\n\n\tI\'m thinking. . . ')
f = list(f)
f.insert (0,'')
f.append('')
try: 
    for i in f:
        if i in flag_filter:
            x = x + i
        else:
            d.append(x)
            x = ''
except:
    flag_filter = []
if a == True:
    d = list(set(d))
    d = sorted(d)
    d = sorted(d, key = len)
for i in f:
    if i in b16:
        x = x + i
    else:
        p.append(x)
        x = ''
p = list(filter(None, p))
for i in p:
    if len(i) % 2 == 0:
        q.append(i)
if a == True:
    q = list(set(q))
    q = sorted(q)
    q = sorted(q, key = len)
for i in q:
    i = binascii.unhexlify(i)
    z.append(i)
for i in z:
    try:
        i = str(i,'ascii')
        o.append(i)
    except:
        pass
for i in f:
    if i in b64:
        x = x + i
    else:
        r.append(x)
        x = ''
for i in r:
    if len(i) % 4 == 0:
        s.append(i)
for i in s:
    if '===' in i:
        s.remove(i)
s = list(filter(None, s))
if a == True:
    s = list(set(s))
    s = sorted(s)
    s = sorted(s, key = len)
for i in s:
    if i.endswith('=='):
        t.append(i)
try:
    for i in s:
        u.append(base64.b64decode(i))
except:
    pass
for i in u:
    i = i.decode('latin-1')
    v.append(i)
try:
    for i in t:
        w.append(base64.b64decode(i))
except:
    pass
for i in w:
    i = i.decode('latin-1')
    y.append(i)
if b == True:
    for i in d:
        if c in i:
            flag.append(i)
    for i in o:
        if c in i:
            flag.append(i)
    for i in v:
        if c in i:
            flag.append(i)
flag = list(set(flag))
flag = sorted(flag)
flag.sort(key=len, reverse=True)
if len(q) == 0:
    print ('\n\n\tPossibly Base16(Hexadecimal): Move along, nothing to see here.')
else:
    print ('\n\n\tPossibly Base16(Hexadecimal):', q)
if len(s) == 0:
    print ('\n\tBase64: Move along, nothing to see here.')
else:
    print ('\n\tPossibly Base64:', s)
if len(t) == 0:
    print ('\n\n\tBase64 ending in ==: Move along, nothing to see here.')
else:
    print ('\n\tPossibly Base64 ending in ==:', t)
if len(o) == 0:
    print ('\n\n\tPossibly Base16(Hexadecimal) to ASCII: Move along, nothing to see here.')
else:
    print ('\n\n\tPossibly Base16(Hexadecimal) to ASCII:', o)
if len(v) == 0:
    print ('\n\tPossibly Base64 to ASCII: Move along, nothing to see here.')
else:
    print ('\n\tPossibly Base64 to ASCII:', v)
if len(y) == 0:
    print ('\n\tBase64 ending in == to ASCII: Move along, nothing to see here.')
else:
    print ('\n\tPossibly Base64 ending in == to ASCII:', y)
if b == True and len(flag) == 0:
    print ('\n\tFlags: Move along, nothing to see here.')
elif b == False:
    print ('\n\tI wrote this sentance with the time I saved not filtering for a flag.')
else:
    print('\n\n\tPossibly Flags:', flag)
print ('\n\n\tDone!\n\n\t\tYou may need to scroll up to see the full results.\n\n\t\tDon\'t forget to check the origional file for context.')
input('\n\n\tPress ENTER to exit. . . ')