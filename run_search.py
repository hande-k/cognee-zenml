from zenml.client import Client
from pipelines.search_pipeline import cognee_search_pipeline
import sys
def run_search_pipeline(archive_artifact_id: str, query_text: str):
    
    artifact = Client().get_artifact_version(archive_artifact_id)

    sp = cognee_search_pipeline.with_options(
        steps={
            "import_cognee_db_step": {
                "parameters": {
                    "archive_path": artifact.load()
                }
            },
            "cognee_search": {
                "parameters": {
                    "query": query_text
                }
            }
        }
    )
    search_run = sp()
    return search_run


if __name__ == "__main__":
    # Quick dirty CLI for search
    if len(sys.argv) < 3:
        print("Usage: python run_search.py <artifact_id> <query_text>")
        sys.exit(1)

    artifact_id = sys.argv[1]
    query = " ".join(sys.argv[2:]) 

    print(f"Running search with artifact_id={artifact_id} and query='{query}'...")
    search_run = run_search_pipeline(archive_artifact_id=artifact_id, query_text=query)
    
    search_results_artifact = search_run.steps["cognee_search"].outputs["output"][0]
    search_results = search_results_artifact.load()
    print("Search results:", search_results)