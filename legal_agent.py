import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.embedder.google import GeminiEmbedder
from agno.knowledge.pdf_url import PDFUrlKnowledgeBase
from agno.models.google import Gemini
from agno.vectordb.pgvector import PgVector, SearchType

load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql+psycopg2://ai:ai@localhost:5532/ai")

try:

    knowledge_base = PDFUrlKnowledgeBase(
        urls=["https://www.archives.gov/files/about/laws/basic-laws-book-2016.pdf"],  
        vector_db=PgVector(
            table_name="laws",
            db_url=DB_URL,
            search_type=SearchType.hybrid,
            embedder=GeminiEmbedder(dimensions=768),
        ),
    )

    agent = Agent(
        model=Gemini(id="gemini-2.0-flash-exp"),
        knowledge=knowledge_base,
        add_references=True,  
        search_knowledge=False,
        markdown=True,
    )

    agent.print_response(
        "What are the key provisions of the U.s. Constitution?", stream=True
    )

except Exception as e:
    print(f"⚠️ Error: {e}")
