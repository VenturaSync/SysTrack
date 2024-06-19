import typer
from system_monitor import get_memory_usage, get_cpu_usage, get_disk_usage, get_network_stats, get_sensor_temps
from rich.console import Console
from rich.table import Table

app = typer.Typer()
console = Console()

@app.command()
def memory():
    """Displays memory usage statistics."""
    typer.echo(get_memory_usage())

@app.command()
def cpu():
    """Displays CPU usage statistics."""
    typer.echo(get_cpu_usage())

@app.command()
def disk():
    """Displays disk usage statistics."""
    typer.echo(get_disk_usage())

@app.command()
def network():
    """Displays network statistics."""
    typer.echo(get_network_stats())

@app.command()
def sensors():
    """Displays sensor temperature statistics, if available."""
    typer.echo(get_sensor_temps())

# @app.command()
# def show_data():
#     table = Table(title="System Stats")

#     table.add_column("Metric", style="dim", width=12)
#     table.add_column("Value", style="bold")

#     table.add_row("CPU", "50%")
#     table.add_row("Memory", "8 GB")
    
#     console.print(table)

if __name__ == "__main__":
    app()