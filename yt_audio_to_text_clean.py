# import required modules
import whisper
from langdetect import detect
from pytube import YouTube
import pickle
import sys
import os

KEYWORD = "vegan"
YEAR = 2022

with open("./data/retrieved_video_"+YEAR+"_key_"+str(KEYWORD)+".pickle", "rb") as token:    
    retrieved_videos = pickle.load(token)

print("Year: "+str(YEAR))
print("Total size: "+str(len(retrieved_videos)))

# language filter on the description of the videos in retrieved_videos with detect from langdetect
list_to_drop = []
for i in range(len(retrieved_videos)):
    try:
        language = detect(retrieved_videos["Video Description"].values[i])
        if language != "en":
            list_to_drop.append(i)
    except:
        try:
            language = detect(retrieved_videos["Video Title"].values[i])
            if language != "en":
                list_to_drop.append(i)
        except:
            print(retrieved_videos["Video Description"].values[i])
            print("Error in language detection")

retrieved_videos = retrieved_videos.drop(list_to_drop)

print("English size: "+str(len(retrieved_videos)))

# check which values in the Video Transcript column are None and save the video ids in a list  
video_ids = []
for i in range(len(retrieved_videos)):
    if retrieved_videos["Video Transcript"].values[i] == None:
        video_ids.append(retrieved_videos["Video ID"].values[i])

# print number of rows with Video Transcript not None
auto_caption_size = len(retrieved_videos) - len(video_ids)
print("Auto-caption size: ", auto_caption_size)

# download audio and transcribe
for id in video_ids:
    url = "https://www.youtube.com/watch?v=" + id

    print(id)

    # Create a YouTube object from the URL
    yt = YouTube(url)

    # Get the audio stream
    try:
        audio_stream = yt.streams.filter(only_audio=True).first()

        # Download the audio stream
        output_path = "YoutubeAudios"
        # if the folder does not exist, create it
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        filename = "audio_"+id+".mp3"
        audio_stream.download(output_path=output_path, filename=filename)

        # Load the base model and transcribe the audio
        model = whisper.load_model("base")
        result = model.transcribe("./YoutubeAudios/audio_"+id+".mp3")

        transcribed_text = result["text"]
        # assign transcribed text as value to the Video Transcript column for the given video id in retrieved_videos dataframe
        retrieved_videos.loc[retrieved_videos["Video ID"] == id, "Video Transcript"] = transcribed_text
    except:
        print("Error in audio download or transcription")
        #delete row corresponding to video ID from retrieved_videos
        retrieved_videos = retrieved_videos[retrieved_videos["Video ID"] != id]

# reset index of retrieved_videos
retrieved_videos = retrieved_videos.reset_index(drop=True)

print("Whisper caption size: ", len(retrieved_videos)-auto_caption_size)

with open("./data/retrieved_videos_transcript_"+str(YEAR)+"_key_"+KEYWORD+".pickle", "wb") as token:    
    pickle.dump(retrieved_videos, token)