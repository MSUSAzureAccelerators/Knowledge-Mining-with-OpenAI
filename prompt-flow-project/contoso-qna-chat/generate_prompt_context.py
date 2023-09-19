from typing import List
from promptflow import tool
import json

@tool
def generate_prompt_context(search_result: List[dict]) -> str:
    def format_doc(doc: dict):
        return f"Content: {doc['Content']}\nSource: {doc['Source']}"

    SOURCE_KEY = "source"

    retrieved_docs = []
    for item in (search_result or []):
        content = "" if 'text' not in item else item['text']

        # if 'metadata' in item:
        #     metadata = item['metadata']

        #     if type(metadata) is str:
        #         metadata = json.loads(metadata)

        #     source = ""
        #     if SOURCE_KEY in metadata:
        #         source = metadata[SOURCE_KEY]
        # else:
        #     source = ""
        source = ""

        retrieved_docs.append({
            "Content": content,
            "Source": source
        })
    doc_string = "\n\n".join([format_doc(doc) for doc in retrieved_docs])

    print(doc_string)
    return doc_string
