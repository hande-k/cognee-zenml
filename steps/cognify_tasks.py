import asyncio
from typing import List, Union
from zenml import step
from zenml.client import Client
from cognee.tasks.documents.classify_documents import classify_documents
from cognee.tasks.documents.check_permissions_on_documents import check_permissions_on_documents
from cognee.tasks.documents.extract_chunks_from_documents import extract_chunks_from_documents
from cognee.tasks.graph.extract_graph_from_data import extract_graph_from_data
from cognee.tasks.summarization.summarize_text import summarize_text
from cognee.tasks.storage.add_data_points import add_data_points
from cognee.tasks.summarization.models import TextSummary
from cognee.modules.data.models import Data
from cognee.modules.chunking.models.DocumentChunk import DocumentChunk
from cognee.shared.data_models import KnowledgeGraph


@step
def load_data_docs_step() -> List[Data]:
    # retrieve "cognee_data_docs" artifact
    client = Client()
    data_artifact = client.get_artifact_version(name_id_or_prefix="cognee_data_docs")
    data_docs = data_artifact.load()  # This is a List[Data]
    return data_docs

@step
def classify_documents_step(docs: List[Data]) -> List:
    """Wraps the async `classify_documents` cognee task."""
    classified = asyncio.run(classify_documents(docs))
    for doc in classified:
        if doc.belongs_to_set:
            for node in doc.belongs_to_set:
                node.metadata.setdefault("type", "NodeSet") 
    print(f"[classify_documents_step] Classified {len(classified)} documents.")
    return classified

@step
def check_permissions_step(docs: List, user=None, permissions=["write"]) -> List:
    """Wraps the async `check_permissions_on_documents` cognee task."""
    allowed = asyncio.run(check_permissions_on_documents(docs, user, permissions))
    print(f"[check_permissions_step] Permission check done. {len(allowed)} docs remain.")
    return allowed

@step
def extract_chunks_step(docs: List, max_chunk_size: int = 1024) -> List[DocumentChunk]:
    """
    Wraps the async `extract_chunks_from_documents` cognee task.
    """
    chunk_list = []
    async def gather_chunks():
        async for chunk_batch in extract_chunks_from_documents(docs, max_chunk_size=max_chunk_size):
            chunk_list.append(chunk_batch)
    asyncio.run(gather_chunks())
    print(f"[extract_chunks_step] Extracted {len(chunk_list)} total chunks.")
    return chunk_list

@step
def extract_graph_step(chunks: List[DocumentChunk]) -> List[KnowledgeGraph]:
    """Wraps the async `extract_graph_from_data` cognee task."""
    chunk_graphs = asyncio.run(extract_graph_from_data(chunks, graph_model=KnowledgeGraph))
    print(f"[extract_graph_step] Graph extraction complete. Same {len(chunk_graphs)} chunk(s).")
    return chunk_graphs

@step
def summarize_text_step(chunks: List[DocumentChunk]) -> List:
    """Wraps the async `summarize_text` cognee task, returning summary objects."""
    summaries = asyncio.run(summarize_text(chunks))
    print(f"[summarize_text_step] Summaries generated: {len(summaries)}")
    return summaries

@step
def add_data_points_step(chunks_and_summaries: List) -> List:
    """
    Wraps the async `add_data_points` cognee task.
    """
    stored = asyncio.run(add_data_points(chunks_and_summaries))
    print(f"[add_data_points_step] Data points stored: {len(stored)}")
    return stored

@step
def combine_chunks_and_summaries_step(
    chunk_graphs: List[DocumentChunk],
    summaries: List[TextSummary],
) -> List[Union[DocumentChunk, TextSummary]]:
    """Concatenates the DocumentChunk objects with the summaries into one list."""
    combined = chunk_graphs + summaries
    return combined

