from zenml import pipeline
import os
from steps.cognify_tasks import (
    add_data_points_step,
    check_permissions_step,
    classify_documents_step,
    combine_chunks_and_summaries_step,
    extract_chunks_step,
    extract_graph_step,
    summarize_text_step,
    load_data_docs_step,
)
from steps.export_cognee_db_step import export_cognee_db_step
from steps.graph_visualization import visualize_graph_step


@pipeline(enable_cache=False)
def cognee_cognify_pipeline():
    """
    Equivalent to cognee.cognify() but taking the docs from the previous pipeline and including the visualization step:
    """
    docs = load_data_docs_step()
    classified = classify_documents_step(docs=docs)
    permitted = check_permissions_step(classified)
    chunks = extract_chunks_step(permitted)
    chunk_graphs = extract_graph_step(chunks)
    summaries = summarize_text_step(chunks)
    combined = combine_chunks_and_summaries_step(chunk_graphs, summaries)

    final = add_data_points_step(combined)

    # Define location where to store html visualization of graph
    home_dir = os.path.expanduser("~")
    destination_file_path = os.path.join(home_dir, "cognee_graph_visualization.html")

    visualization = visualize_graph_step(
        after=final, destination_file_path=destination_file_path
    )

    db_archive = export_cognee_db_step(after=visualization)
