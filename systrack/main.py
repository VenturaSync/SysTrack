import typer
from system_monitor import get_memory_usage, get_cpu_usage, get_disk_usage, get_network_stats, get_sensor_temps

app = typer.Typer()

@app.command()
def memory():
    """Displays memory usage statistics."""
    typer.echo(get_memory_usage())

@app.command()
def cpu():
    """Displays CPU usage statistics."""
    typer.echo(get_cpu_usage())

if __name__ == "__main__":
    app()