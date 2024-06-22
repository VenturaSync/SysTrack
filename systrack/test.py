from pyfiglet import Figlet
from rich.console import Console

# Create instances of Figlet and Console
f = Figlet(font='slant')
console = Console()

# Generate ASCII art text
ascii_art = f.renderText('Systrack')

# Print the ASCII art text with color using Rich
console.print(ascii_art, style="bold blue")
