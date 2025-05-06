import asyncio
from typing import Optional, Union, List
from zenml import step, ArtifactConfig
from cognee.tasks.ingestion.resolve_data_directories import resolve_data_directories
from cognee.tasks.ingestion.ingest_data import ingest_data
from cognee.modules.data.models import Data

from typing_extensions import Annotated


@step
def resolve_data_directories_step(
    data_input: Union[str, List[str]],
    include_subdirectories: bool = True
) -> List[str]:
    """
    Calls cognee's async `resolve_data_directories()`.
    """
    return asyncio.run(
        resolve_data_directories(
            data=data_input,
            include_subdirectories=include_subdirectories
        )
    )

@step
def ingest_data_step(
    resolved_paths: List[str],
    dataset_name: str = "main_dataset",
    node_set: Optional[List[str]] = None
) -> Annotated[
    List[Data],
    ArtifactConfig(name="cognee_data_docs")  # custom name
]:
    """
    Calls cognee's async `ingest_data()` to create or update Data objects.
    """
    data_docs: List[Data] = asyncio.run(
        ingest_data(
            data=resolved_paths,
            dataset_name=dataset_name,
            user=None,
            node_set=node_set,
        )
    )
    print(f"[ingest_data_step] Ingested {len(data_docs)} cognee Data items.")
    return data_docs
