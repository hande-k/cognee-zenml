# cognee-zenml simple demo

- Clone https://github.com/zenml-io/zenml/pull/3529 locally and run this project in the same venv
- set cognee env variables
- run run_pipelines.py to add a sample text to cognee store and generate a knowledge graph -> copy the artifact_id
- run python run_search.py <artifact_id> "<query_text>"

### Low level pipelines
1. add_pipeline
2. cognify_pipeline
3. search_pipeline 

