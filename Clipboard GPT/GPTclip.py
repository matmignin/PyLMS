import re
import json
import pyperclip
import os
from datetime import datetime
import subprocess

# Regex pattern to match
# pattern = re.compile(r'\d{3}-\d{2}-\d{4}')
patterns = {
        'product': r'(?<=\w{3})?(?P<product>[abdefghijklABDEFGHIJKL]\d{3})(?=\w{4})?',
        'batch': r'[^(ct\#?)](?P<batch>\d{3}-\d{4}\b)',
        'lot': r'(?P<lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)'
}
# pattern_product = re.compile(r'(?<=\w{3})?(?P<product>[abdefghijkl]\d{3})(?=\w{4})?',re.IGNORECASE|re.DOTALL)
# pattern_batch = re.compile(r'[^(ct\#?)](?P<batch>\d{3}-\d{4}\b)',re.IGNORECASE|re.DOTALL)
# pattern_lot = re.compile(r'(?P<lot>\b\d{4}\w\d\w?|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d)',re.IGNORECASE|re.DOTALL)
# pattern_coated = re.compile(r'(?:\d{4}\w\d\w?.|\bBulk\b|G\d{7}\w?\b|VC\d{6}[ABCDEFGH]?|V[A-Z]\d{5}[A-Z]\d?|\d{5}\[A-Z]{3}\d\s|coated:?\s?|ct\#?\s?)(?P<coated>\d{3}-\d{4})',re.IGNORECASE|re.DOTALL)

# Define the JSON file to save the clipboard history
json_file = 'clipboard_history.json'

# Read the existing history from the JSON file if it exists
if os.path.exists(json_file):
    with open(json_file, 'r') as f:
        history = json.load(f)
else:
    history = {}

while True:
    # Get the current clipboard text
    clipboard_text = subprocess.run(
        ['pbpaste'], capture_output=True, text=True).stdout

    # Check for matches against each regular expression
    for pattern_name, pattern in patterns.items():
        matches = re.finditer(pattern, clipboard_text)

        # Add the matches to the history
        for match in matches:
            match_text = match.group(0)
            named_group = match.lastgroup
            if named_group not in history:
                history[named_group] = []
            if match_text not in history[named_group]:
                history[named_group].append(match_text)

    # Write the updated history to the JSON file
    with open(json_file, 'w') as f:
        json.dump(history, f)



# # History of unique matches
# history = []

# while True:
#     # Get current clipboard data
#     clipboard_data = pyperclip.paste()

#     # Search for matches in clipboard data
#     matches = pattern_product.findall(clipboard_data)
#     # matches = pattern_batch.findall(clipboard_data)
#     # matches = pattern_lot.findall(clipboard_data)
#     # matches = pattern_coated.findall(clipboard_data)
#     for pattern in patterns:
#         # matches.extend(re.findall(pattern, clipboard_data))
#         matches.extend(re.finditer(pattern, clipboard_data))
#     # Iterate through matches
#     for match in matches:
#         # Check if match is not already in history
#         if match not in history:
#             # Add match to history
#             history.append(match[1])
#         # time.sleep(1)

#     # Write history to JSON file
#     with open('clipboard_history.json', 'w') as f:
#         json.dump(history, f)