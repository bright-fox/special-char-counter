# Symbol Counter

This project provides a Python script that counts special characters in a codebase or text project. It can be particularly useful when designing a symbol layer for a programmable keyboard, helping you decide where to place each symbol for optimal efficiency.

The script supports counting either:

- Single characters (e.g., `@`, `#`, `{`)
- Bigrams (pairs of characters, e.g., `!=`, `->`)
<img src="assets/imgs/example_plot.png" alt="example plot output" width="75%"/>

## How to run the script

1. Clone the project
```bash
git clone https://github.com/bright-fox/symbol-counter.git
cd symbol-counter
```
3. Create a virtual environment
```bash
python3 -m venv symbol_counter_env
```
3. Activate the virtual environment
```bash
source symbol_counter_env/bin/activate
```
4. Install the required packages
```bash
pip install -r requirements.txt
```

5. _(Optional)_ Configure exclusions
> Add a `.exclude` file with the help of `.exclude.example` file to define regex rules for ignoring lines in files

8. Run the script
```bash
python main.py ./path/to/your/project
```

### Arguments

| Argument        | Type     | Choices                  | Default | Help                                                                                       |
|-----------------|----------|--------------------------|---------|--------------------------------------------------------------------------------------------|
| `--pattern`     | `str`    | `["single", "bigram"]`   | `single`| Count either single characters or bigrams (pairs of characters). |
| `--ext`         | `str`    |                          | `ts`    | Filter files by extension (e.g., py, js, ts). |
| `--out`         | `str`    | `["visual", "cmd", "txt"]`| `visual`| Choose output format: chart (visual), terminal (cmd), or text file (txt). |
| `--min_count`   | `int`    |                          |         | Show only symbols that appear at least min_count times. |
| `--max_entries` | `int`    |                          |         | Limit output to the top max_entries results. |
| `--exclude_path`| `str`    |                          | `./.exclude`| Path to a regex file for ignored lines. Each line in the file is one rule. |

### Examples

```bash
# Count single characters in all .ts files
python main.py ./my_project --pattern single --ext ts

# Count bigrams in Python files and save results to txt
python main.py ./my_project --pattern bigram --ext py --out txt

# Show only symbols that appear at least 10 times
python main.py ./my_project --min_count 10

# Limit output to the top 20 results and print in terminal
python main.py ./my_project --max_entries 20 --out cmd
```


