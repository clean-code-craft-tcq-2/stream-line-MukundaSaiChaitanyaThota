import json
import csv

def formatOutputStringAsCSV(streamReading):
    return f'{streamReading["soc"]},{streamReading["temp"]}'

def readFromCSV(fileName):
    rows = []
    file = open(fileName)
    csvreader = csv.DictReader(file)
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows

def sendSensorData(fileName, readFromCSV, formatOutputString, printOnConsole):
    readings = readFromCSV(fileName)
    for reading in readings:
        formattedstring = formatOutputString(reading)
        printOnConsole(formattedstring)
    return True

def printOnConsole(string):
    print(string)
    return True

if __name__ == '__main__': # pragma: no cover
  sendSensorData("./sensorOutputValues/Readings.csv", readFromCSV, formatOutputStringAsCSV, printOnConsole)