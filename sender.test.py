import unittest
import sender

class SenderTest(unittest.TestCase):
    def test_printOnConsole(self):
        self.assertTrue(sender.printOnConsole('All is fine!') == True)

    def test_formatOutputStringAsCSV(self):
        self.assertTrue(sender.formatOutputStringAsCSV({'soc':25,'temp':30}) == "25,30")
        self.assertTrue(sender.formatOutputStringAsCSV({'soc':35,'temp':50}) == "35,50")

    
    def test_readFromCSV(self):
        self.assertTrue(sender.readFromCSV("./sensorOutputValues/ReadingsTest.csv") == [{'soc': '25', 'temp': '35'}, {'soc': '22', 'temp': '32'}])

    def test_sendSensorData(self):
        self.assertTrue(sender.sendSensorData("./sensorOutputValues/ReadingsTest.csv", sender.readFromCSV, sender.formatOutputStringAsCSV, sender.printOnConsole) == True)
        

if __name__ == '__main__': # pragma: no cover
  unittest.main()