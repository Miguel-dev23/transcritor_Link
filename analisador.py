from youtube_transcript_api import YouTubeTranscriptApi

video_id = "COLE_AQUI_O_ID_DO_VIDEO"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

for line in transcript:
    print(line)