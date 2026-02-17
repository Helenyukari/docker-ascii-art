import pyfiglet
import sys
from datetime import datetime

if len(sys.argv) > 1:
    text_input = sys.argv[1]
else:
    text_input = "DOCKER LAB"

# fonts = pyfiglet.getFonts()
font = "slant"

ascii_art = pyfiglet.figlet_format(text_input, font=font)
timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

output = ascii_art + f"\nGenerated at: {timestamp}"

print(output)

with open("output.txt", "w") as f:
    f.write(output)