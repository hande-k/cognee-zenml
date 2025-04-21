# to save cognee db to zenml artifact

from pathlib import Path
from zenml.steps import step

from materializers.cognee_db_materializer import CogneeDBMaterializer

@step(output_materializers={"output": CogneeDBMaterializer})
def export_cognee_db() -> Path:
    """Return the path where Cognee DB files are located."""
    db_path = Path("/Users/handekafkas/Documents/local-code/integrations/zenml/zenml-env/lib/python3.12/site-packages/cognee/.cognee_system/databases")
    return db_path.resolve()
