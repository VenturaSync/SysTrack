from pyfiglet import Figlet
from rich.console import Console

console = Console()
figlet = Figlet(font='slant')
title = figlet.renderText('SysTrack')
console.print(title, style="bold blue")