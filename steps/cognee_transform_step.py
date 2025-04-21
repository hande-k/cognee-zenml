import cognee
import asyncio
from zenml.steps import step

@step
def run_cognify(text: str) -> None:
    """Step 2: adds data and runs the cognify process on input text."""
    print("Running cognify to create knowledge graph...\n")

    async def _add_and_cognify(text: str):
        await cognee.add(text)
        await cognee.cognify()
    
    asyncio.run(_add_and_cognify(text))
    print("Cognify process complete.\n")
