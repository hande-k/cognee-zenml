from zenml import pipeline
from steps.cognee_search_step import cognee_search
from steps.import_cognee_db_step import import_cognee_db_step

@pipeline(enable_cache=False)
def cognee_search_pipeline():
    db_folder = import_cognee_db_step()
    # Then run search once the DB is restored
    results = cognee_search(after=db_folder)
