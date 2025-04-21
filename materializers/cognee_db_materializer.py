# materializers/cognee_db_materializer.py

import os
import shutil
from pathlib import Path
from typing import Type, Any
from zenml.materializers.base_materializer import BaseMaterializer
from zenml.enums import ArtifactType

class CogneeDBMaterializer(BaseMaterializer):
    """Materializer that saves/loads a directory of Cognee DB files."""

    # We plan to return a `Path` object from our step
    ASSOCIATED_TYPES = (Path,)
    # Mark it as a DATA artifact
    ASSOCIATED_ARTIFACT_TYPE = ArtifactType.DATA

    def load(self, data_type: Type[Any]) -> Path:
        """Load the directory from the artifact store into a local path."""
        # self.artifact_store_path is a local directory where ZenML has the artifact
        return Path(self.artifact_store_path)

    def save(self, db_dir: Path) -> None:
        """Save the entire directory to the artifact store."""
        # We'll copy `db_dir` into self.artifact_store_path:
        shutil.copytree(db_dir, self.artifact_store_path, dirs_exist_ok=True)
