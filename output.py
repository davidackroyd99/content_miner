"""For outputting results to the console or saving them to a file."""
from collections import Counter

from analysis import AnalysedContent


def print_output(analysed_content: AnalysedContent, scan_mode: bool, freq: bool) -> str:
    """Print the output of content analysis to the console"""
    print(_produce_output(analysed_content, scan_mode, freq))


def save_output(analysed_content: AnalysedContent, destination: str, scan_mode: bool, freq: bool):
    with open(destination, mode="w", encoding="utf-8") as destination_file:
        destination_file.write(_produce_output(analysed_content, scan_mode, freq))


def _produce_output(analysed_content: AnalysedContent, scan_mode: bool, freq: bool) -> str:
    output = [f"Percentage of tokens known: {(analysed_content.token_count - analysed_content.target_count) / analysed_content.token_count}", ""]

    for t, count in Counter(analysed_content.all_targets).most_common():
        if freq:
            output.append(f"{t} {count}")
        else:
            output.append(t)

        if scan_mode:
            continue

        for sent in analysed_content.sentences:
            if sent.target_count > 0 and sent.targets[0] == t:
                try:
                    output.append(sent.text)
                except:
                    output.append("WARNING: unprintable sentence!")

    return "\n".join(output)