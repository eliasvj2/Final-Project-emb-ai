import unittest
from EmotionDetection.emotion_detection import emotion_predictor

class TestSentimentAnalyzer(unittest.TestCase):
    def test_emotion_predictor(self):
        result_1 = emotion_predictor('I am glad this happened')
        self.assertEqual(result_1['dominant emotion'], 'joy')

        result_2 = emotion_predictor('I am really mad about this')
        self.assertEqual(result_2['dominant emotion'], 'anger')

        result_3 = emotion_predictor('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant emotion'], 'disgust')

        result_4 = emotion_predictor('I am so sad about this')
        self.assertEqual(result_4['dominant emotion'], 'sadness')

        result_5 = emotion_predictor('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant emotion'], 'fear')

unittest.main()