from typing import List

from promptflow import log_metric, tool

import numpy as np

@tool
def calculate_accuracy(grades: List[float]):
    mean = np.mean(grades)
    standard = np.std(grades)

    # calculate confidence interval
    confidence_interval = 1.96 * standard / np.sqrt(len(grades))

    # calculate accuracy for each variant
    log_metric("accuracy", f'{mean:.3f} ± {confidence_interval:.3f}')

    return confidence_interval
