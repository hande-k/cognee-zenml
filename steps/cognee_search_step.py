import cognee
import asyncio
from cognee.api.v1.search import SearchType
from typing import List
from zenml.steps import step

@step
def cognee_search(query: str) -> List[str]:
    """Step 3: Perform a search for the given query and return the search results as a list of strings (or objects)."""
    print(f"Searching cognee for with query: '{query}'")
    
    async def _search():
        return await cognee.search(query_type=SearchType.GRAPH_COMPLETION, query_text=query)
    
    search_results = asyncio.run(_search())

    print("Search results:")
    for result_text in search_results:
        print(result_text)

    return search_results
