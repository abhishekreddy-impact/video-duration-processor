import pandas as pd
import subprocess
import os
from yt_dlp import YoutubeDL

# Load the CSV
df = pd.read_csv("urls.csv")
urls = df['unique_post_url'].dropna().tolist()

# Output list
results = []

# Download options
ydl_opts = {
    'outtmpl': 'video.%(ext)s',
    'quiet': True,
    'no_warnings': True,
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
}

def get_duration(filename):
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries',
             'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', filename],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        return float(result.stdout.decode().strip())
    except Exception:
        return None

for url in urls:
    try:
        # Remove any existing files
        if os.path.exists("video.mp4"):
            os.remove("video.mp4")

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        duration = get_duration("video.mp4")
        results.append((url, duration if duration else "failed"))

        os.remove("video.mp4")

    except Exception:
        results.append((url, "failed"))

# Save results
pd.DataFrame(results, columns=["unique_post_url", "duration"]).to_csv("output.csv", index=False)
print("✅ Done. Results saved to output.csv")
