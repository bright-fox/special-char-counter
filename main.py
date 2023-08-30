from collections import defaultdict
import glob
import os
import re
from utils.arg_parser import parse_args
from utils.counter import count_bigrams, count_single_chars
from utils.exclude_rules import load_exclusion_rules
from utils.output import display_plot, write_to_file


def main():
    args = parse_args()

    if not os.path.exists(args.path):
        raise Exception("Please provide a valid path..")

    path = os.path.abspath(args.path)
    counter = defaultdict(lambda: 0)
    exclusion_rules = load_exclusion_rules(args.exclude_path)

    # read all files in a project
    for file_path in glob.iglob(f"{path}/**/*.{args.ext}", recursive=True):
        with open(file_path, "r") as f:
            for line in f:
                # exclude lines that match regex in exclude file
                if any(re.match(rule, line) for rule in exclusion_rules):
                    continue

                # count characters, either single or bigrams
                last_char = None
                for char in line:
                    if args.pattern == "single":
                        count_single_chars(char, counter)
                    elif args.pattern == "bigram":
                        last_char = count_bigrams(char, last_char, counter)

    # sort and transform the results
    sorted_counter = sorted(counter.items(), key=lambda i: -i[1])
    if args.min_count:
        sorted_counter = [c for c in sorted_counter if c[1] >= args.min_count]
    if args.max_entries:
        sorted_counter = sorted_counter[: args.max_entries]

    # output results
    if args.out == "visual":
        display_plot(sorted_counter)
    elif args.out == "txt":
        write_to_file(dict(sorted_counter))
    else:
        print(dict(sorted_counter))


if __name__ == "__main__":
    main()
