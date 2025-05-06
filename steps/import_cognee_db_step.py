import os
import shutil
from zenml import step

from cognee.base_config import get_base_config
bc = get_base_config()
bc.data_root_directory = "/tmp/restored_cognee_db"

@step
def import_cognee_db_step(archive_path: str, target_folder: str = "/tmp/restored_cognee_db") -> str:
    """
    Extracts the previously archived cognee DB folder into `target_folder`.
    Returns the path to the restored DB folder.
    """
    if os.path.exists(target_folder):
        shutil.rmtree(target_folder)
    os.makedirs(target_folder, exist_ok=True)

    # Unzip the file
    shutil.unpack_archive(archive_path, target_folder, "zip")

    return os.path.abspath(target_folder)
