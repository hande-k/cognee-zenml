# Cognee + ZenML Integration Demo

*Repeatable, scalable AI memory system to ensure your AI applications have reliable context and knowledge to draw from, even as they grow more complex*

- Cognee is a modular system for building and managing structured knowledge from structured and unstructured. It uses tasks (e.g., ingestion, knowledge graph extraction, search) to transform raw text into an organized knowledge graph. The goal is to give LLMs apps or AI agents a persistent, structured memory that improves their reasoning and reduces hallucinations. 

- ZenML is a production-grade pipeline orchestration framework with composable steps, artifact tracking, and reproducibility. By wrapping Cognee tasks inside ZenML steps, we can chain these tasks into robust pipelines for knowledge processing. ZenML handles the execution flow, tracks all intermediate artifacts, and ensures the entire pipeline is reproducible and easy to scale. 

- This repository contains an initial subset of cognee tasks implemented as ZenML steps and pipelines. It’s a friendly starting point that shows how to integrate cognee’s knowledge-building tasks with ZenML’s orchestration. Users can easily extend this demo by plugging in additional cognee tasks or adding their own custom steps to the pipeline. 

## How to run this example?

### Setting up ZenML editable version
- create a python venv in your preferred directory `python3.11 -m venv venv`
- clone zenml to the same directory `gh repo clone zenml-io/zenml`
- activate your venv and navigate to zenml `cd zenml`
- in pyproject.toml, update bcrypt = { version = ">=4.0.1,<5" } 
- run `pip install --upgrade pip && pip install -e .`

*now you have the updated version of local zenml in your venv.*

### Setting up cognee & other dependencies & env variables

- clone cognee-zenml to your preferred directory `gh repo clone hande-k/cognee-zenml`
- copy/paste the `.env.template` file and rename it to `.env`
- set your **OpenAI API** key for `LLM_API_KEY`
- navigate to cognee-zenml directory within the venv you created earlier (which you have your local zenml)
- run `pip install -r requirements.txt` to install cognee and other dependencies. 

*now you have your environment ready.*

### Run an example

- run `python run_pipelines.py` to clean-up all existing data from cognee, add the sample text(`data/sample_text.txt`) to cognee store and generate a knowledge graph
- the location of the graph visualization and the zenml artifact_id will be printed.
- copy that artifact_id to use it in the below step to query cognee.
- run `python run_search.py <artifact_id> "<query_text>"` 


