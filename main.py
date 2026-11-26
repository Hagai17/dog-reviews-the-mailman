"""The Dog Reviews the Mailman — entry program (program/v1).

Writes the review line to /output/entry.txt and prints it.
"""

import os

LINE = (
    "Two stars. He feeds the door instead of me. "
    "The door does not even eat. "
    "I have watched it not eat for three years."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
