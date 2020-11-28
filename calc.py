import sys

# read argument
fname = sys.argv[1]

# open file
gradeFile = open(fname, 'r')

# read the lines
for line in gradeFile.readlines():
  print(int(line))
