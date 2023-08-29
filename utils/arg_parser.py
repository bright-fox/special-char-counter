import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="path to the source code of the project")
    parser.add_argument(
        "--pattern",
        type=str,
        choices=["single", "bigram"],
        default="single",
        help="Either count single characters or bigrams",
    )
    parser.add_argument(
        "--ext",
        type=str,
        default="ts",
        help="file extension of the files you want the counter to work on",
    )
    parser.add_argument(
        "--out",
        type=str,
        choices=["visual", "cmd", "txt"],
        default="visual",
        help="how to output the results.\nThe options are visual: Visual Plot, cmd: object on command line, txt: object in a txt file.",
    )
    parser.add_argument(
        "--min_count",
        type=int,
        help="minimum count of the occurence of a character to be shown in the results",
    )
    parser.add_argument(
        "--max_entries",
        type=int,
        help="maximum number of entries that should be shown in results",
    )
    parser.add_argument(
        "--exclude_path",
        type=str,
        default="./.exclude",
        help="path to file for defining regex rules to exclude lines in files",
    )
    return parser.parse_args()
