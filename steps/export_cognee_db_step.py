import os
import shutil
from zenml import step

@step
def export_cognee_db_step(
    cognee_db_folder: str = "/Users/handekafkas/Documents/local-code/integrations/zenml/zenml-env/lib/python3.12/site-packages/cognee/.cognee_system/databases",
    output_archive: str = "cognee_db.zip"
) -> str:
    """
    Zips the cognee data store and returns the path to the zip as a ZenML artifact.
    """
    if not os.path.exists(cognee_db_folder):
        raise ValueError(f"DB folder not found: {cognee_db_folder}")

    # Create a zip or tar of the entire DB folder
    shutil.make_archive(
        base_name=output_archive.replace(".zip", ""),  # 'cognee_db'
        format="zip",
        root_dir=cognee_db_folder
    )

    # Return the path to the new archive
    archive_path = os.path.abspath(output_archive)
    return archive_path
