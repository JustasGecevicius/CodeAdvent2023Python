
def part1():
  task = open('input2.txt')
  gamesTotal = 0
  allBalls = { 'red': 12, 'green': 13, 'blue': 14 }
  for index, line in enumerate(task.readlines()):
    correctedIndex = index + 1
    data = line.strip().split(':')[1].split(';')
    goodGame = True
    for set in data:
      individualBalls = set.split(', ')
      currentSet = { 'red': 0, 'blue': 0, 'green': 0 }
      for ball in individualBalls:
        numberBallPair = ball.strip().split(' ')
        currentSet[numberBallPair[1]] += int(numberBallPair[0])
      for item in currentSet.items():
        if (allBalls[item[0]] < item[1]):
          goodGame = False
    if (goodGame):
      gamesTotal += correctedIndex
  print(gamesTotal)
  task.close()

def part2():
  task = open('input2.txt')
  power = 0
  keys = ('red', 'blue', 'green')
  for line in task.readlines():
    powerCount = 1
    data = line.strip().split(':')[1].split(';')
    minimumGameData = { 'red': None, 'blue': None, 'green': None }
    for set in data:
      placeholderGameData = { 'red': 0, 'blue': 0, 'green': 0 }
      individualBalls = set.split(', ')
      for ball in individualBalls:
        numberBallPair = ball.strip().split(' ')
        placeholderGameData[numberBallPair[1]] += int(numberBallPair[0])
        print(ball, placeholderGameData)
      for key in keys:
        if(minimumGameData[key] == None or minimumGameData[key] < placeholderGameData[key]):
          # print(minimumGameData, placeholderGameData)
          minimumGameData[key] = placeholderGameData[key]
    for key in keys:
      powerCount *= minimumGameData[key]
    # print(powerCount, 'POWER')
    power += powerCount
  print(power)
  task.close()

part1()
part2()

