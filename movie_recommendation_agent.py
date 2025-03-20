import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.google import Gemini
from agno.vectordb.pgvector import PgVector, SearchType

# Load environment variables
load_dotenv()

# PostgreSQL connection
DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://ai:ai@localhost:5532/ai")

try:
    # Create a knowledge base from a movie-related PDF
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://example.com/movies.pdf"],  # Replace with actual movie dataset PDF
        vector_db=PgVector(
            table_name="movies",
            db_url=DB_URL,
            search_type=SearchType.hybrid,
            embedder=GeminiEmbedder(dimensions=768),
        ),
    )

    # **Load the knowledge base (Run once, then comment out)**
    # knowledge_base.load(upsert=True)

    # Create an AI-powered movie recommendation agent
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        knowledge=knowledge_base,
        add_references=True,  # Enables RAG (Retrieval-Augmented Generation)
        search_knowledge=False,
        markdown=True,
    )

    # Query the agent for movie recommendations
    agent.print_response(
        "Can you recommend a bollywood sci-fi movie with a deep storyline?", stream=True
    )

except Exception as e:
    print(f"⚠️ Error: {e}")
