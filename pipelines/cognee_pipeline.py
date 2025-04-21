from typing import List
from zenml import pipeline
from steps.reset_cognee_step import reset_cognee_data
from steps.cognee_transform_step import run_cognify
from steps.cognee_search_step import cognee_search

@pipeline(enable_cache=False)
def cognee_pipeline(input_text: str, search_query: str) -> List[str]:
    
    reset_cognee_data()

    run_cognify(text=input_text, after="reset_cognee_data")

    cognee_search(query=search_query, after="run_cognify")
