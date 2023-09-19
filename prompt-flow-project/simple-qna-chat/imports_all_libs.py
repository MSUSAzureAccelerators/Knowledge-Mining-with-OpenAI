from typing import List
from promptflow import tool
from embeddingstore.core.contracts import SearchResultEntity
from embeddingstore.tool.vector_index_lookup import VectorIndexLookup

@tool
def search_question_from_indexed_docs(path: str, query: list[float], top_k: int) -> str:
    vectorIndexLookup = VectorIndexLookup(path)
    return vectorIndexLookup.search(query, top_k)
