import asyncio
from typing import Optional
from zenml import step

# Import the async function
from cognee.api.v1.visualize.visualize import visualize_graph

@step
def visualize_graph_step(destination_file_path: Optional[str] = None) -> str:
    """
    Calls cognee's async `visualize_graph()` function to generate an HTML graph visualization.
    """
    graph_html = asyncio.run(visualize_graph(destination_file_path))

    return graph_html
