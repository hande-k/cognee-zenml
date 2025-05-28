from zenml import pipeline

from steps.reset_cognee_step import reset_cognee_data


@pipeline(enable_cache=False)
def cognee_reset_pipeline():
    """
    Resets cognee data and system state.
    Use this pipeline before add_pipeline if you want to start fresh.
    """
    reset_cognee_data() 