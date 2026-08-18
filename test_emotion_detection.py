#test_emotion_detection.py
import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    def test_joy_dominant(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy", 
                         "Expected 'joy' as dominant emotion for: 'I am glad this happened'")

    def test_anger_dominant(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger", 
                         "Expected 'anger' as dominant emotion for: 'I am really mad about this'")

    def test_disgust_dominant(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust", 
                         "Expected 'disgust' as dominant emotion for: 'I feel disgusted just hearing about this'")

    def test_sadness_dominant(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness", 
                         "Expected 'sadness' as dominant emotion for: 'I am so sad about this'")

    def test_fear_dominant(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear", 
                         "Expected 'fear' as dominant emotion for: 'I am really afraid that this will happen'")

    def test_result_structure(self):
        """Verify the function returns the exact dictionary structure required by the lab."""
        result = emotion_detector("Test sentence.")
        expected_keys = {"anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"}
        self.assertEqual(set(result.keys()), expected_keys, 
                         "Result dictionary missing or has extra keys")
        self.assertIsInstance(result["dominant_emotion"], str, 
                              "dominant_emotion must be a string")

if __name__ == '__main__':
    unittest.main()