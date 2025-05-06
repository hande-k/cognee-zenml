from zenml import pipeline

from steps.add_tasks import ingest_data_step, resolve_data_directories_step
from steps.reset_cognee_step import reset_cognee_data

@pipeline(enable_cache=False)
def cognee_add_pipeline():
    """
    Equivalent to cognee.add() but including the prune step.
    """
    reset_cognee_data()
    paths = resolve_data_directories_step()
    data_docs = ingest_data_step(resolved_paths=paths)
    # The pipeline ends by returning data_docs as an artifact
