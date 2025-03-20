import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.google import Gemini
from agno.vectordb.pgvector import PgVector, SearchType

# Load environment variables (store credentials in .env file)
load_dotenv()

# PostgreSQL database connection string
DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://ai:ai@localhost:5532/ai")

# Ensure the pgvector extension is enabled in PostgreSQL before running
try:
    # Create a knowledge base of PDFs from URLs
    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://agno-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
        vector_db=PgVector(
            table_name="recipes",
            db_url=DB_URL,
            search_type=SearchType.hybrid,
            embedder=GeminiEmbedder(dimensions=768),
        ),
    )

    # **Load the knowledge base (Run once, then comment out)**
    # knowledge_base.load(upsert=True)

    # Create an AI agent with Gemini model and RAG capabilities
    agent = Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        knowledge=knowledge_base,
        add_references=True,  # Enables retrieval-augmented generation (RAG)
        search_knowledge=False,
        markdown=True,
    )

    # Query the agent
    agent.print_response(
        "How do I make Chapati?", stream=True
    )

except Exception as e:
    print(f"⚠️ Error: {e}")
