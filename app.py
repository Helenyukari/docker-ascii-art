import pyfiglet
from datetime import datetime

text = pyfiglet.figlet_format("HELEN DEV")
timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

output = text + "\nGerado em: " + timestamp

with open("output.txt", "w") as f:
    f.write(output)

print(output)