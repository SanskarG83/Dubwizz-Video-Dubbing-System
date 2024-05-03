from flask import Flask, jsonify, send_file, request
from flask_cors import CORS
from extract_audio import extract_video_and_audio
import threading

app = Flask(__name__)
CORS(app)
# hindi, bengali, tamil, telugu, gujarati
# FrontEnd to Cloudinary
@app.route("/upload/<language>", methods=["POST"])
def upload_video(language):
    try:
        video = "vid1.mp4"
        lang = language
        thread = threading.Thread(target=extract_video_and_audio, args=(video, lang))
        thread.start()

        return jsonify({"message": "Video received successfully. Processing has started"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/subtitle", methods=["GET"])
def get_subtitle():
    try:
        subtitle_path = "Output\\eng_sub.txt"

        return send_file(subtitle_path)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/trans_sub", methods=["GET"])
def get_trans_sub():
    try:
        eng_subtitle = "Output\\trans_sub.txt"

        return send_file(eng_subtitle)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/audio", methods=["GET"])
def get_audio():
    try:
        audioFile = "extracted\\audio_only.mp3"

        return send_file(audioFile)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/trans_audio", methods=["GET"])
def get_trans_audio():
    try:
        transAudioFile = "Output\\translated_audio.mp3"

        return send_file(transAudioFile)

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/dub", methods=["GET"])
def get_dubbed_video():
    try:
        dubbed_video = "Final\\dubbed_video.mp4"

        return send_file(dubbed_video)

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
