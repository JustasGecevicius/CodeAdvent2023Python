import re
import cProfile

def part1():
  task = open('input4.txt')
  lines = task.readlines()
  sum = 0
  for line in lines:
    [winningNumbers, givenNumbers] = line[10:].split('|')
    individualWinningNumbers = re.findall('\d+', winningNumbers)
    individualGivenNumbers = re.findall('\d+', givenNumbers)
    countPerLine = 0
    for winningNumber in individualWinningNumbers:
      if (winningNumber in individualGivenNumbers):
        countPerLine += 1
    if (countPerLine == 0):
      continue
    if(countPerLine == 1):
      sum += 1
      continue
    if(countPerLine > 1):
      exponent = countPerLine - 1
      sum += 2**exponent
  print(sum)
part1()
