import typer
from system_monitor import get_memory_usage, get_cpu_usage, get_disk_usage, get_network_stats, get_sensor_temps
from rich.console import Console
from rich.table import Table
from rich import box

app = typer.Typer()
console = Console()

@app.command()
def memory():
    """Displays memory usage statistics."""
    typer.echo(get_memory_usage())

@app.command()
def cpu():
    """Displays CPU usage statistics."""
    CPU_Usage = get_cpu_usage()

    cpu_count = str(CPU_Usage["cpu count"])
    cpu_usage = str(CPU_Usage["cpu usage"]) + "%"

    table = Table(title="CPU Stats", 
                  box=box.DOUBLE, 
                  show_lines=True, 
                  style="bold")

    table.add_column("Metric", justify="right", style="bold red", width=12, overflow="fold")
    table.add_column("Value", justify="right", style="bold magenta", overflow="fold")
    
    table.add_row("CPU Cores", cpu_count)
    table.add_row("CPU Usage", cpu_usage)
    
    console.print(table)

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

if __name__ == "__main__":
    app()
