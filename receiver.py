import sys

ValuessizeinMovingAverage = 5
parameters = ["SOC", "temperature"]

def readFromConsole():
    lines = sys.stdin.readlines()
    return lines
    
def  processInput(stream):
    mergedReadings = []
    for csvReading in stream:
        csvReading = csvReading.strip('\n')
        reading = list(map(float,csvReading.split(',')))
        mergedReadings.append(reading)
    return mergedReadings

def extractEachParameterReadings(mergedReadings, parameter):
    index = getindex(parameter)
    return [readings[index] for readings in mergedReadings]

def getindex(parameter):
    for index, parameterName in enumerate(parameters):
        if parameterName == parameter:
            return index

def calculateMovingAverage(readings, ValuessizeinMovingAverage):
    Rangewindows = createRangeWindow(readings, ValuessizeinMovingAverage)
    movingAverages = [round((sum(range) / len(range)), 2) for range in Rangewindows]
    return movingAverages
                            
def processInputReadings(ValuessizeinMovingAverage, readFromConsole,  processInput, extractEachParameterReadings, calculateMovingAverage, calculateMinMaxReading, convertCSVFormat):
    stream = readFromConsole()
    mergedreadings =  processInput(stream)
    statisticsReading = []
    for parameter in parameters:
        readings = extractEachParameterReadings(mergedreadings, parameter)
        movingAverage = calculateMovingAverage(readings, ValuessizeinMovingAverage)
        minMaxReading = calculateMinMaxReading(readings)
        formattedString = convertCSVFormat(parameter,minMaxReading,movingAverage)
        statisticsReading.append(formattedString)
        print(formattedString)
    return statisticsReading

def createRangeWindow(readings, ValuessizeinMovingAverage):
    Rangewindows = [readings[index : index + ValuessizeinMovingAverage] for index, value in enumerate(readings) if index < len(readings) - ValuessizeinMovingAverage + 1]
    return Rangewindows

def calculateMinMaxReading(readings):
    minReading = min(readings)
    maxReading = max(readings)
    return {'min': minReading, 'max': maxReading}

def convertCSVFormat(parameter,minMaxReading,movingAverage):
  return f'{parameter}:{minMaxReading},{movingAverage}'

if __name__ == '__main__':  # pragma: no cover
  processInputReadings(ValuessizeinMovingAverage, readFromConsole,  processInput, extractEachParameterReadings, calculateMovingAverage, calculateMinMaxReading,convertCSVFormat)
