"""For outputting results to the console or saving them to a file."""
from collections import Counter

from analysis import AnalysedContent


def print_output(analysed_content: AnalysedContent, scan_mode: bool) -> str:
    """Print the output of content analysis to the console"""
    print(_produce_output(analysed_content, scan_mode))


def _produce_output(analysed_content: AnalysedContent, scan_mode: bool) -> str:
    output = [f"Percentage of tokens known: {(analysed_content.token_count - analysed_content.target_count) / analysed_content.token_count}", ""]

    for t, count in Counter(analysed_content.all_targets).most_common():
        if scan_mode:
            output.append(t)
            continue
        output.append(f"{t} {count}")

        for sent in analysed_content.sentences:
            if sent.target_count > 0 and sent.targets[0] == t:
                try:
                    output.append(sent.text)
                except:
                    output.append("WARNING: unprintable sentence!")

    return "\n".join(output)