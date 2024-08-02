'''
Unit Tests for the 'emotion_detection' function.
'''
import unittest

from EmotionDetection.emotion_detection import emotion_detector


class TestSentimentAnalyzer(unittest.TestCase):
    '''
    Define a test case class for testing
    the 'sentiment_analyzer' function.
    '''
    def test_sentiment_analyzer(self):
        '''
        Define a test method for the 'sentiment_analyzer' function.
        '''
        # Check that calling 'emotion_detector('I am glad this happened')' returns "joy".
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        # Check that calling 'emotion_detector('I am really mad about this')'
        # returns "anger".
        result_2 = emotion_detector('I am really mad about this')
        self.assertEqual(result_2['dominant_emotion'], 'anger')
        # Check that calling 'emotion_detector('I feel disgusted just hearing about this')'
        # returns "disgust".
        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_3['dominant_emotion'], 'disgust')
        # Check that calling 'emotion_detector('I am so sad about this')' returns "sadness".
        result_4 = emotion_detector('I am so sad about this')
        self.assertEqual(result_4['dominant_emotion'], 'sadness')
        # Check that calling 'emotion_detector('I am really afraid
        # that this will happen')' returns "fear".
        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_5['dominant_emotion'], 'fear')

unittest.main()
