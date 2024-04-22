from pytube import YouTube

def download_youtube_video(url):
    try:
        # Create a YouTube object
        video = YouTube(url)
        
        # Get the video streams
        streams = video.streams.filter(progressive=True, file_extension='mp4')
        
        # Select the highest resolution stream
        highest_resolution_stream = streams.order_by('resolution').desc().first()
        
        # Download the video
        print(f"Downloading: {video.title}")
        highest_resolution_stream.download()
        
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
video_url = "https://www.youtube.com/watch?v=mv6QKnLC1NY"
download_youtube_video(video_url)