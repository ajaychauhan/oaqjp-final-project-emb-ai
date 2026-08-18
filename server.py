"""Flask application for Emotion Detection API."""

from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Render the index.html page."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_endpoint():
    """Handle emotion detection requests from the frontend."""
    # 1. Extract & sanitize user input
    text_to_analyze = request.args.get('textToAnalyze', '').strip()

    # 2. Handle blank/empty user input (Client-side 400)
    if not text_to_analyze:
        return jsonify({
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }), 400

    try:
        # 3. Call updated emotion_detector (handles Watson API 400s internally)
        result = emotion_detector(text_to_analyze)
        return jsonify(result)

    except Exception as e:  # pylint: disable=broad-exception-caught
        # 4. Catch unexpected errors (network, parsing, etc.)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    