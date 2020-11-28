import sys

def getGPA(grade):
  if (grade > 89):
    return 4
  elif (grade > 84):
    return 3.9
  elif (grade > 79):
    return 3.7
  elif (grade > 76):
    return 3.3
  elif (grade > 72):
    return 3
  elif (grade > 69):
    return 2.7
  elif (grade > 66):
    return 2.3
  elif (grade > 62):
    return 2
  elif (grade > 59):
    return 1.7
  elif (grade > 56):
    return 1.3
  elif (grade > 52):
    return 1
  elif (grade > 49):
    return 0.7
  return 0

def readGrades(fname, defaultWeight=0.5):
  # open file
  gradeFile = open(fname, 'r')
  sum = 0
  denom = 0

  # read the lines
  for line in gradeFile.readlines():
    seg = line.split(',')
    if (len(seg) > 1):
      sum += getGPA(int(seg[0])) * float(seg[1])
      denom += float(seg[1])
    else:
      sum += getGPA(int(line)) * defaultWeight
      denom += 0.5
  return(sum / denom)

# read argument
fname = sys.argv[1]
myGPA = readGrades(fname)

print("Your GPA:", myGPA)
