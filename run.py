from pipelines.cognee_pipeline import cognee_pipeline

if __name__ == "__main__":
    # Example text and query from the simplified Cognee snippet
    text = """
    Natural language processing (NLP) is an interdisciplinary
    subfield of computer science and information retrieval.
    """
    query = "Tell me about NLP"

    cognee_pipeline(input_text=text, search_query=query) 
