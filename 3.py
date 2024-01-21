import re
import cProfile

symbolsArray = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '/', '?']

def getLineToSearchIndexes(currIndex, length):
  linesToSearch = [0, 1]
  if (currIndex > 0 and currIndex < length):
    linesToSearch = [currIndex - 1, currIndex, currIndex + 1]
  elif (currIndex == length): linesToSearch = [currIndex - 1, currIndex]
  return linesToSearch


def part1():
  task = open('input3.txt')
  lines = task.readlines()
  sum = 0
  for index, line in enumerate(lines):
    serialNumbers = []
    def searchFunction(string, currIndex, lines, goodParts):
      lineIndexesToSearch = getLineToSearchIndexes(currIndex, len(lines) - 1)
      breakLoop = False
      find = re.search('\d+', string)
      if(find):
        span = find.span()
        text = find.group()
      else: return goodParts
      for lineIndex in lineIndexesToSearch:
        lineToSearch = lines[lineIndex]
        for index in range(span[0] - 1, span[1] + 1):
          if(index == -1): continue
          if(lineToSearch[index] in symbolsArray):
            goodParts.append(text)
            breakLoop = True
            break
        if(breakLoop):
          break
      replacement = ''.join(['.' for i in range(len(text))])
      correctedString = re.sub(text, replacement, string, 1)
      searchFunction(correctedString, currIndex, lines, goodParts)
    searchFunction(line, index, lines, serialNumbers)
    for number in serialNumbers:
      sum += int(number)

def getWidthToSearch(starIndex, length):
  if (starIndex == 0):
    return (0, 1)
  elif (starIndex == length - 1):
    return (starIndex - 1, starIndex)
  return (starIndex - 1, starIndex + 1)
          
def checkNumber(number, snippet, previousNum, starLocation):
  correctedSnippet = snippet
  if (previousNum):
    replacement = ''.join(['.' for i in range(len(previousNum))])
    correctedSnippet = re.sub(previousNum, replacement, snippet, 1)
  searchResult = re.search(number, correctedSnippet)
  numberSpan = searchResult.span()
  if(starLocation - 1 <= numberSpan[0] <= starLocation + 1
     or starLocation - 1 <= numberSpan[1] - 1 <= starLocation + 1):
    return number

def getSnippets(line, width):
  correctedWidth = [width[0] - 2, width[1] + 3]
  if(width[0] <= 3):
    correctedWidth[0] = 0
  if(width[1] >= len(line) - 1):
    correctedWidth[1] = len(line) - 1
  return line[correctedWidth[0]: correctedWidth[1]]

      
def getStarIndex(starSnippet):
  if(len(starSnippet) == 7):
    return 3
  star = re.search('\*', starSnippet)
  return star.span()[0]

def getStarSnippetIndex(currIndex):
  if(currIndex == 0):
    return 0
  return 1

def searchFunction(string, currIndex, lines, totals = 0):
  goodParts = []
  total = totals
  lineIndexesToSearch = getLineToSearchIndexes(currIndex, len(lines) - 1)
  start = re.search('\*', string)
  if(not start):
    return total
  starLocation = start.span()[0]
  width = getWidthToSearch(starLocation, len(string))
  stringSnippets = [
    getSnippets(lines[index], width) for index in lineIndexesToSearch
  ]
  starIndexInSnippet = getStarIndex(
    stringSnippets[getStarSnippetIndex(currIndex)]
  )
  for snippet in stringSnippets:
    numbers = re.findall('\d+', snippet)
    if(not numbers): continue
    goodNumber = ''
    for number in numbers:
      goodNumber = checkNumber(number, snippet, goodNumber, starIndexInSnippet)
      if(goodNumber):
        goodParts.append(goodNumber)
  if (len(goodParts) == 2):
    total += int(goodParts[0]) * int(goodParts[1])
  newString = re.sub("\*", '.', string, 1)
  return searchFunction(newString, currIndex, lines, total)

def part2():
  task = open('input3.txt')
  lines = task.readlines()
  sum = 0
  for index, line in enumerate(lines):
    sum += searchFunction(line, index, lines)
  print(sum)
cProfile.run('part2()')
part2()
# 84399773
