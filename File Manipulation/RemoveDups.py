import sys

lines_seen = set() # holds lines already seen
outfile = open("out.txt", "a+")
for line in open(sys.argv[1], "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
