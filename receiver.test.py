
import unittest
import receiver

class RcevierTest(unittest.TestCase):
  
    def test_getindex(self):
        self.assertTrue(receiver.getindex("SOC") == 0)
        self.assertTrue(receiver.getindex("temperature") == 1)
    
    def test_extractEachParameterReadings(self):
        self.assertTrue(receiver.extractEachParameterReadings([[25,13],[6,15]], "SOC") == [25,6])
        self.assertTrue(receiver.extractEachParameterReadings([[6,12],[6,35]], "temperature") == [12,35])      
        
    def test_calculateMinMaxParameter(self):
        self.assertTrue(receiver.calculateMinMaxReading([7,15,5,3,10]) == {'min': 3, 'max': 15})
        self.assertTrue(receiver.calculateMinMaxReading([7,18,5,12,10]) == {'min': 5, 'max': 18})
        self.assertTrue(receiver.calculateMinMaxReading([27,15,6,13,12]) == {'min': 6, 'max': 27})
        self.assertTrue(receiver.calculateMinMaxReading([7,15,5,3,10]) == {'min': 3, 'max': 15})
    
    def test_calculateMovingAverage(self):
        self.assertTrue(receiver.calculateMovingAverage([8,12,4,5,11,19,16,14], 5) == [8.0,10.2,11,13])
    
    def test_createRangeWindow(self):
        self.assertTrue(receiver.createRangeWindow([8,12,4,5,11,19,16,14], 5) == [[8,12,4,5,11], [12,4,5,11,19], [4,5,11,19,16], [5,11,19,16,14]])

    def test_processInput(self):
        self.assertTrue(receiver.processInput(['5,10\n','6,15\n']) == [[5,10],[6,15]])

if __name__ == '__main__': # pragma: no cover
  unittest.main()
