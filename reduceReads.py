import sys, random

if sys.argv[4][-1] == 'z':
    infile = gzip.open(sys.argv[1])
    outfile = gzip.open(sys.argv[2], 'wb')
else:
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')
if sys.argv[4][:2] == 'fa':
    z = 2
else:
    z = 4
getrate = float(sys.argv[3])



count = 0
for line in infile:
    count += 1
    if count % z == 1:
        if random.random() <= getrate:
            getit = True
            outfile.write(line)
        else:
            getit = False
    elif count % z == 2:
        if getit:
            outfile.write(line)
    elif count % z == 3:
        if getit:
            outfile.write(line)
    elif count % z == 0:
        if getit:
            outfile.write(line)
