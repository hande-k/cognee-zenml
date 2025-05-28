from zenml.client import Client
from pipelines.add_pipeline import cognee_add_pipeline
from pipelines.cognify_pipeline import cognee_cognify_pipeline
from pipelines.reset_pipeline import cognee_reset_pipeline
from pathlib import Path
import os

if __name__ == "__main__":
    current_directory = Path(__file__).resolve().parent
    data_file_path = os.path.join(current_directory, "data", "sample_text.txt")
    
    # === OPTIONAL: Reset Cognee Data ===
    # Comment the next line if you want to keep all existing cognee data and system state instead of starting fresh
    cognee_reset_pipeline()
    
    print("=== Running Cognee Add Pipeline ===")
    add_pipe = cognee_add_pipeline.with_options(
        steps={
            "resolve_data_directories_step": {"parameters": {"data_input": data_file_path}},
            "ingest_data_step": {
                "parameters": {
                    "dataset_name": "nlp_dataset",
                    "node_set": ["demo_node_set"],
                }
            },
        }
    )

    add_run = add_pipe()

    # After it finishes, retrieve the artifact from the `ingest_data_step`.
    add_pipeline_run = Client().get_pipeline_run(add_run.name)
    data_docs_artifact = add_pipeline_run.steps["ingest_data_step"].outputs[
        "cognee_data_docs"
    ][0]
    data_docs = data_docs_artifact.load()  # This is a list[Data]
    print("Number of Data docs loaded:", len(data_docs))
    print("Sample doc:", data_docs[0] if data_docs else None)
    print("Type of data_docs:", type(data_docs))
    if data_docs:
        print("Type of first doc:", type(data_docs[0]))

    print("=== Running Cognee Cognify Pipeline ===")
    cognify_pipe = cognee_cognify_pipeline.with_options(
        steps={"extract_chunks_step": {"parameters": {"max_chunk_size": 512}}}
    )
    cognify_run = cognify_pipe()

    # check each step's outputs
    cognify_pipeline_run = Client().get_pipeline_run(cognify_run.name)
    final_output_artifact = cognify_pipeline_run.steps["add_data_points_step"].outputs[
        "output"
    ][0]
    final_data = final_output_artifact.load()
    print(f"Final data points: {final_data}")
    
    # Show where the visualization is saved
    home_dir = os.path.expanduser("~")
    visualization_path = os.path.join(home_dir, "cognee_graph_visualization.html")
    print(f"Graph visualization can be found at: {visualization_path}")
    
    print("Pipelines Complete!")

    visual_step_info = cognify_pipeline_run.steps["visualize_graph_step"]
    # print(f"Visualization step info: {visual_step_info}")
    artifact = visual_step_info.outputs["output"][0]
    html_str = artifact.load()

    db_step_info = cognify_pipeline_run.steps["export_cognee_db_step"]
    db_artifact = db_step_info.outputs["output"][0]
    zip_path = db_artifact.load()  # returns the local path to the 'cognee_db.zip'
    print("Cognee DB archive is at:", zip_path)
    db_artifact_id = db_artifact.id
    print("DB artifact ID is:", db_artifact_id)
