In this script:
1. We import the `YouTube` class from the pytube library. Make sure you have `pytube` installed (`pip install pytube`).
2. We define the `download_youtube_video` function that takes the YouTube video URL as a parameter.
3. Inside the function, we create a `YouTube` object by passing the video URL to it. This object represents the YouTube video.
4. We retrieve the video streams using `video.streams.filter(progressive=True, file_extension='mp4')`. This filters the streams to get only the progressive streams (streams that contain both audio and video) with the MP4 file extension.
5. We select the highest resolution stream from the filtered streams using `streams.order_by('resolution').desc().first()`. This orders the streams by resolution in descending order and selects the first stream, which will be the highest resolution stream.
6. We start downloading the video using `highest_resolution_stream.download()`. This will download the video to the current directory.
7. We print a success message if the video is downloaded successfully.
8. If any exception occurs during the process, we catch it and print an error message.
9. Finally, we provide an example usage of the `download_youtube_video` function by specifying a YouTube video URL.

When you run this script with a valid YouTube video URL, it will download the video in the highest available resolution to the current directory.

Note: The `pytube` library is subject to changes in the YouTube API, so make sure you have the latest version installed. If you encounter any issues, you can refer to the `pytube` documentation for troubleshooting and updates.

Also, keep in mind that downloading YouTube videos may be subject to copyright restrictions and the terms of service of YouTube. Make sure you have the necessary permissions and comply with the applicable legal requirements when using this script.
