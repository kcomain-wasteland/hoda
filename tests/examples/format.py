#!/usr/bin/env python3
# Script to format json stuffs
import time
import json
import os
import sys


def main():
    things = os.listdir()

    for item in things:
        if not item.endswith(".json"):
            continue
        try:
            with open(item) as f:
                data = json.load(f)
                print(f"loaded {item}")
                it = time.perf_counter_ns()

            with open(item, "w") as f:
                json.dump(data, f, indent=4)
                print(f"formatted {item} in {time.perf_counter_ns() - it} nanoseconds")
        except json.JSONDecodeError:
            print(f"Error while trying to format {item}: JSON Decode Error. Skipped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
