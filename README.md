# Cognee + ZenML Integration Demo

*Repeatable, scalable AI memory system to ensure your AI applications have reliable context and knowledge to draw from, even as they grow more complex*

- Cognee is a modular system for building and managing structured knowledge from structured and unstructured. It uses tasks (e.g., ingestion, knowledge graph extraction, search) to transform raw text into an organized knowledge graph. The goal is to give LLMs apps or AI agents a persistent, structured memory that improves their reasoning and reduces hallucinations. 

- ZenML is a production-grade pipeline orchestration framework with composable steps, artifact tracking, and reproducibility. By wrapping Cognee tasks inside ZenML steps, we can chain these tasks into robust pipelines for knowledge processing. ZenML handles the execution flow, tracks all intermediate artifacts, and ensures the entire pipeline is reproducible and easy to scale. 

- This repository contains an initial subset of cognee tasks implemented as ZenML steps and pipelines. It’s a friendly starting point that shows how to integrate cognee’s knowledge-building tasks with ZenML’s orchestration. Users can easily extend this demo by plugging in additional cognee tasks or adding their own custom steps to the pipeline. 

## how to run the example 
- Update bcrypt = { version = ">=4.0.1,<5" } dependency of zenml locally and run this project in the same venv
- set cognee env variables (Use your OpenAI API key for LLM_API_KEY)
- run run_pipelines.py to add a sample text to cognee store and generate a knowledge graph -> copy the artifact_id
- run python run_search.py <artifact_id> "<query_text>"


