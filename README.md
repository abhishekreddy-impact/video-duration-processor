# Instagram Video Duration Extractor

This project helps you:
- Read a CSV file (`urls.csv`) containing a column `unique_post_url`
- Download each Instagram video using `yt-dlp`
- Extract its duration using `ffmpeg`
- Save results to `output.csv`
- Delete the video file afterward

## How to Use (with Render.com)
1. Deploy this repo using Render
2. Upload your `urls.csv` file via the Render shell
3. Run the script: `python extract_durations.py`
4. Download the result from `output.csv`

Built for Abhishek to process 850k video URLs from Instagram 🚀
