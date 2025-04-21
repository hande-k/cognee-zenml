import cognee
import asyncio
from zenml.steps import step

@step
def reset_cognee_data() -> None:
    """
    Step 1: Reset cognee data and system state.
    """
    print("Resetting cognee...")

    async def _reset():
        await cognee.prune.prune_data()
        await cognee.prune.prune_system(metadata=True)
    
    asyncio.run(_reset())
    print("Cognee data reset complete.\n")
