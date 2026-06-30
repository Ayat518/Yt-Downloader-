from flask import Flask, request, render_template, redirect
import yt_dlp

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/download")
def download_video():
    video_url = request.args.get("url")
    if not video_url:
        return "URL is missing", 400
    try:
        ydl_opts = {
            "format": "best",
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "nocheckcertificate": True,
            "headers": {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return redirect(info.get("url"))
    except Exception as e:
        return f"YouTube Block Error: {str(e)}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
    
