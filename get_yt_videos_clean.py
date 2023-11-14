# import required modules
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from youtube_transcript_api import YouTubeTranscriptApi

import os
import pickle
import pandas as pd
import sys

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Function to authorize API access using OAuth2
import json
from googleapiclient.discovery import build

def youtube_authenticate():
    with open('credentials.json', 'r') as file:
        credentials = json.load(file)
    api_key = credentials['youtube']['api_key']
    return build("youtube", "v3", developerKey=api_key)


# Function to search for videos based on a keyword
def search_videos(service, threshold_api_units, **kwargs):
    all_results = []
    next_page_token = ''

    total_api_units_used = 0
    print("Total units used: %d" % total_api_units_used)

    while total_api_units_used < threshold_api_units and next_page_token is not None:
        # Calculate the number of API units needed for the upcoming request (e.g., 100 units for search)
        api_units_needed = 100

        # Check if making the next request would exceed the threshold
        if total_api_units_used + api_units_needed <= threshold_api_units:
    
            search_results = service.search().list(**kwargs).execute()
            all_results.extend(search_results.get('items', []))

            total_api_units_used += api_units_needed
            print("Total units used: %d" % total_api_units_used)
        
            if total_api_units_used + api_units_needed <= threshold_api_units:
            # Check for more pages of results
                next_page_token = search_results.get('nextPageToken')
                total_api_units_used += api_units_needed
                print("Total units used: %d" % total_api_units_used)
                if not next_page_token:
                    break
                kwargs['pageToken'] = next_page_token
            else:
                print("Reached API unit threshold. Stopping requests.")
                break
        else:
            print("Reached API unit threshold. Stopping requests.")
            break
                
    return all_results

# Function to retrieve video details
def get_video_details(service, video_id):
    video_details = service.videos().list(part='snippet,statistics', id=video_id).execute()
    return video_details.get('items', [])[0] if video_details.get('items', []) else None


if __name__ == '__main__':

    KEYWORD = "vegan"
    START_DATE = "2022-12-01T00:00:00Z"
    END_DATE = "2023-03-01T00:00:00Z"

    youtube = youtube_authenticate()

    # Step 1: Search for videos based on the keyword
    search_results = search_videos(youtube, threshold_api_units = 8000, q=KEYWORD, publishedAfter=START_DATE, publishedBefore=END_DATE, relevanceLanguage="en", type="video", part='id', maxResults=50, order="date")
    
    video_data = []
    
    for video in search_results:
        video_id = video['id']['videoId']
        
        # Step 2: Retrieve video details
        video_details = get_video_details(youtube, video_id)
        
        if video_details:
            video_title = video_details['snippet']['title']
            video_description = video_details['snippet']['description']
            video_timestamp = video_details['snippet']['publishedAt']
            video_likes = video_details['statistics']['likeCount']
            
            video_data.append({
                'Video ID': video_id,
                'Video Title': video_title,
                'Video Timestamp': video_timestamp,
                'Video Description': video_description,
                'Video Likes': video_likes
            })

    # Create a DataFrame-like structure using pandas
    df = pd.DataFrame(video_data)

    print(df.head())
    print(df["Video Timestamp"].min())
    print(df.shape)

    # get transcripts if automatic caption is available
    video_ids = list(df["Video ID"].values)

    transcript_list, unretrievable_videos = YouTubeTranscriptApi.get_transcripts(video_ids, continue_after_error=True)

    list_transcripts = []

    for video_id in video_ids:

        if video_id in transcript_list.keys():

            srt = transcript_list.get(video_id)

            text_list = []
            for i in srt:
                text_list.append(i['text'])

            text = '.'.join(text_list)
            list_transcripts.append(text)
            
        else:
            list_transcripts.append(None)

    df["Video Transcript"] = list_transcripts

    retrieved_videos = df

    with open("./data/retrieved_video_2022_key_"+str(KEYWORD)+".pickle", "wb") as token:    
        pickle.dump(retrieved_videos, token)    