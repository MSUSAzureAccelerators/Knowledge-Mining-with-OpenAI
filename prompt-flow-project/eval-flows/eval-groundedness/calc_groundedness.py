from promptflow import tool
import re


@tool
def parse_score(gpt_score: str):
    score = extract_float(gpt_score)
    if score is not None:
        return float(score)
    else:
        return 0.0


def extract_float(s):
    match = re.search(r"[-+]?\d*\.\d+|\d+", s)
    if match:
        return float(match.group())
    else:
        return None
