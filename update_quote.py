import random
import re
from quotes_list import quotes

new_quote = random.choice(quotes)

filename = "README.md"

# Read the README file
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

new_content = re.sub(
    r"<!--QUOTE_START-->.*<!--QUOTE_END-->",
    f"<!--QUOTE_START-->\n\"{new_quote}\"\n<!--QUOTE_END-->",
    content,
    flags=re.DOTALL
)

with open(filename, "w", encoding="utf-8") as file:
    file.write(new_content)
