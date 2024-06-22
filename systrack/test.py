from pyfiglet import Figlet
from rich.console import Console

f = Figlet(font='slant')
console = Console()

ascii_art = f.renderText('Systrack')

console.print(ascii_art, style="bold blue")
