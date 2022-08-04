"""Basic profiling functionality. Bit scatty but seems to work."""
import time
from collections import OrderedDict


def profiler():
    start_time = time.time()
    events = OrderedDict()

    def add_event(name: str):
        events[name] = time.time()

    def get_report() -> str:
        report = ""

        for i in range(len(events)):
            ev, t = list(events.items())[i]

            if i == 0:
                report += f"{ev} - {t - start_time}\n"
            else:
                report += f"{ev} - {t - list(events.items())[i - 1][1]}\n"

        report += f"\nTotal time was {next(reversed(list(events.items())))[1] - start_time} seconds."

        return report

    return add_event, get_report