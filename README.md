# Special Character Counter

This python script counts the occurences for each special character inside a TypeScript project.

This is helpful when you want to create a symbol layer on your programmable keyboard.

## How to run the script

1. Clone the project
2. Create a virtual environment
```bash
python3 -m venv char_env
```
3. Activate the virtual environment
```bash
source char_env/bin/activate
```
4. Install the packages
```bash
pip install -r requirements.txt
```
5. Run the script
    - The script receives as an argument the path to the project's folder.
    ```bash
    python single_char.py ./path-to-project
    ```

    - The other script lets you count the occurences for special character bigrams. It also receives as an argument the path to the project's folder.
    ```bash
    python bigram.py ./path-to-project
    ```
