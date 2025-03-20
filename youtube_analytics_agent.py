# from agno.agent import Agent
# from agno.embedder.google import GeminiEmbedder
# from agno.knowledge.youtube import YouTubeKnowledgeBase
# from agno.models.google import Gemini
# from agno.vectordb.pgvector import PgVector, SearchType
# from dotenv import load_dotenv

# load_dotenv()

# db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"
# # Create a knowledge base of PDFs from URLs
# knowledge_base = YouTubeKnowledgeBase(
#     urls=["https://www.youtube.com/watch?v=pTB0EiLXUC8"],
#     # Use PgVector as the vector database and store embeddings in the `ai.recipes` table
#     vector_db=PgVector(
#         table_name="youtubevideos",
#         db_url=db_url,
#         search_type=SearchType.hybrid,
#         embedder=GeminiEmbedder(dimensions=768),
#     ),
# )
# # Load the knowledge base: Comment after first run as the knowledge base is already loaded
# knowledge_base.load(upsert=True)

# agent = Agent(
#     model=Gemini(id="gemini-2.0-flash-exp"),
#     knowledge=knowledge_base,
#     # Enable RAG by adding context from the `knowledge` to the user prompt
#     add_references=True,
#     # Set as False because Agents default to `search_knowledge=True`
#     search_knowledge=False,
#     markdown=True,
# )
# agent.print_response(
#     "Tell Detailed summary with timestamps for the video.", stream=True
# )









# import os
# import googleapiclient.discovery
# from dotenv import load_dotenv
# from agno.agent import Agent
# from agno.embedder.google import GeminiEmbedder
# from agno.knowledge.text import TextKnowledgeBase
# from agno.models.google import Gemini
# from agno.vectordb.pgvector import PgVector, SearchType

# # Load environment variables (YouTube API Key & DB URL)
# load_dotenv()

# YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
# DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://ai:ai@localhost:5532/ai")

# # Initialize YouTube API Client
# youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

# def get_video_transcript(video_id):
#     """Fetches YouTube video transcript (timestamps + text)."""
#     try:
#         from youtube_transcript_api import YouTubeTranscriptApi
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         return "\n".join([f"{t['start']}s: {t['text']}" for t in transcript])
#     except Exception as e:
#         return f"Transcript not available: {str(e)}"

# def get_video_metadata(video_id):
#     """Fetches YouTube video metadata (title, description, views, etc.)."""
#     request = youtube.videos().list(
#         part="snippet,statistics",
#         id=video_id,
#     )
#     response = request.execute()
    
#     if "items" in response and len(response["items"]) > 0:
#         video = response["items"][0]
#         title = video["snippet"]["title"]
#         description = video["snippet"]["description"]
#         views = video["statistics"].get("viewCount", "N/A")
#         return f"Title: {title}\nViews: {views}\nDescription: {description}"
#     return "Video metadata not found."

# # Replace with the actual YouTube video ID
# video_id = "pTB0EiLXUC8"

# # Fetch metadata & transcript
# video_metadata = get_video_metadata(video_id)
# video_transcript = get_video_transcript(video_id)
# video_data = f"{video_metadata}\n\nTranscript:\n{video_transcript}"

# # Store YouTube data in a knowledge base
# knowledge_base = TextKnowledgeBase(
#     texts=[video_data],
#     vector_db=PgVector(
#         table_name="youtube_videos",
#         db_url=DB_URL,
#         search_type=SearchType.hybrid,
#         embedder=GeminiEmbedder(dimensions=768),
#     ),
# )

# # **Load the knowledge base (Run once, then comment out)**
# knowledge_base.load(upsert=True)

# # Create an AI-powered YouTube analytics agent
# agent = Agent(
#     model=Gemini(id="gemini-2.0-flash-exp"),
#     knowledge=knowledge_base,
#     add_references=True,
#     search_knowledge=False,
#     markdown=True,
# )

# # Query the agent for a detailed video summary
# agent.print_response(
#     "Provide a detailed summary with timestamps for the video.", stream=True
# )



import os
import googleapiclient.discovery
from dotenv import load_dotenv
from agno.agent import Agent
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.text import TextKnowledgeBase
from agno.models.google import Gemini
from agno.vectordb.pgvector import PgVector, SearchType
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables (YouTube API Key & DB URL)
load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://ai:ai@localhost:5532/ai")

# Initialize YouTube API Client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

def get_video_transcript(video_id):
    """Fetches YouTube video transcript (timestamps + text)."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return "\n".join([f"{t['start']}s: {t['text']}" for t in transcript])
    except Exception as e:
        return f"Transcript not available: {str(e)}"

def get_video_metadata(video_id):
    """Fetches YouTube video metadata (title, description, views, etc.)."""
    request = youtube.videos().list(
        part="snippet,statistics",
        id=video_id,
    )
    response = request.execute()
    
    if "items" in response and len(response["items"]) > 0:
        video = response["items"][0]
        title = video["snippet"]["title"]
        description = video["snippet"]["description"]
        views = video["statistics"].get("viewCount", "N/A")
        return f"Title: {title}\nViews: {views}\nDescription: {description}"
    return "Video metadata not found."

# Replace with the actual YouTube video ID
# video_id = "pTB0EiLXUC8"
video_id = "WJ-UaAaumNA&t=2s"

# Fetch metadata & transcript
video_metadata = get_video_metadata(video_id)
video_transcript = get_video_transcript(video_id)

# Ensure they are strings
video_metadata = str(video_metadata)
video_transcript = str(video_transcript)

# Format the video data properly as a string
video_data = f"{video_metadata}\n\nTranscript:\n{video_transcript}"

# Ensure `video_data` is a string and print it to verify
print(f"Type of video_data: {type(video_data)}")
print(f"Content of video_data: {video_data}")

# Store YouTube data in a knowledge base
knowledge_base = TextKnowledgeBase(
    texts=[video_data],
    vector_db=PgVector(
        table_name="youtube_videos",
        db_url=DB_URL,
        search_type=SearchType.hybrid,
        embedder=GeminiEmbedder(dimensions=768),
    ),
)

# **Load the knowledge base (Run once, then comment out)**
knowledge_base.load(upsert=True)

# Create an AI-powered YouTube analytics agent
agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    knowledge=knowledge_base,
    add_references=True,
    search_knowledge=False,
    markdown=True,
)

# Query the agent for a detailed video summary
agent.print_response(
    "Provide a detailed summary with timestamps for the video.", stream=True
)
