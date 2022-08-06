"""For outputting results to the console or saving them to a file."""
from collections import Counter

from .analysis import AnalysedContent


def print_output(analysed_content: AnalysedContent, scan_mode: bool, freq: bool, target_count=1) -> str:
    """Print the output of content analysis to the console"""
    print(_produce_output(analysed_content, scan_mode, freq, target_count))


def save_output(analysed_content: AnalysedContent, destination: str, scan_mode: bool, freq: bool, target_count=1):
    with open(destination, mode="w", encoding="utf-8") as destination_file:
        destination_file.write(_produce_output(analysed_content, scan_mode, freq, target_count))


def _produce_output(analysed_content: AnalysedContent, scan_mode: bool, freq: bool, target_count: int) -> str:
    output = [f"Percentage of tokens known: {(analysed_content.token_count - analysed_content.target_count) / analysed_content.token_count}", ""]

    for t, count in Counter(analysed_content.all_targets).most_common():
        if freq:
            output.append(f"{t} {count}")
        else:
            output.append(t)

        if scan_mode:
            continue

        for sent in analysed_content.sentences:
            if 0 < sent.target_count <= target_count and t in sent.targets:
                try:
                    output.append(sent.text)
                except: # TODO: resolve what to do about printing weird characters, obvs this code is pointless
                    output.append("WARNING: unprintable sentence!")

    return "\n".join(output)