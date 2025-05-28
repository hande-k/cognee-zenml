from zenml import pipeline

from steps.add_tasks import ingest_data_step, resolve_data_directories_step


@pipeline(enable_cache=False)
def cognee_add_pipeline():
    """
    Adds data to cognee.
    """
    paths = resolve_data_directories_step()
    data_docs = ingest_data_step(resolved_paths=paths)
    # The pipeline ends by returning data_docs as an artifact
