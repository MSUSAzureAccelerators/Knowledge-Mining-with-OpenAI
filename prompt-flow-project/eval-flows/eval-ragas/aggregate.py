from typing import List
from promptflow import tool
import json
# Log metric for each variant
from promptflow import log_metric


@tool
def aggregate(ragas_scores: List[str]):
    """
    This tool aggregates the processed result of all lines to the variant level and log metric for each variant.

    :param processed_results: List of the output of line_process node.
    :param variant_ids: List of variant ids that can be used to group the results by variant.
    :param line_numbers: List of line numbers of the variants. If provided, this can be used to
                        group the results by line number.
    """

    aggregated_results = {}

    # Calculate average groundedness score for each variant
    for _, ragas_score in enumerate(ragas_scores):
        json_string = ragas_score
        json_object = json.loads(json_string)

        # go through all properies of json_object
        for key in json_object:
            # check if key is already in aggregated_results
            if key not in aggregated_results:
                aggregated_results[key] = 0
            
            aggregated_results[key] += json_object[key]
    
    for key in aggregated_results:
        # check if key is already in aggregated_results
        aggregated_results[key] /= len(ragas_scores)
        log_metric(key=key, value=aggregated_results[key])

    return aggregated_results
