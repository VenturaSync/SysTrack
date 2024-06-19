import typer
from system_monitor import get_memory_usage, get_cpu_usage, get_disk_usage, get_network_stats, get_sensor_temps
from rich.console import Console
from rich.table import Table
from rich import box

app = typer.Typer()
console = Console()

# Memory Command
@app.command()
def memory():
    """Displays memory usage statistics."""
    Memory_Usage = get_memory_usage()
    total_memory = str(Memory_Usage["total"]) + " GB"
    available_memory = str(Memory_Usage["available"]) + " GB"
    percent_memory_used = str(Memory_Usage["percent used"]) + "%"
    memory_used = str(Memory_Usage["used"]) + " GB"
    memory_free = str(Memory_Usage["free"]) + " GB"
    memory_active = str(Memory_Usage["active"]) + " GB"
    memory_inactive = str(Memory_Usage["inactive"]) + " GB"
    memory_wired = str(Memory_Usage["wired"]) + " GB"

    table = Table(title="Memory Stats", box=box.ROUNDED)

    table.add_column("Total", justify="center", style="bold green", overflow="ellipsis")
    table.add_column("Available", style="bold green", overflow="ellipsis")
    table.add_column("Used %", style="bold green", overflow="ellipsis")
    table.add_column("Used", style="bold green", overflow="ellipsis")
    table.add_column("Free", style="bold green",overflow="ellipsis")
    table.add_column("Active", style="bold green", overflow="ellipsis")
    table.add_column("Inactive", style="bold green", overflow="ellipsis")
    table.add_column("Wired", style="bold", overflow="ellipsis")

    table.add_row(
        total_memory, available_memory, percent_memory_used, 
        memory_used, memory_free, memory_active, 
        memory_inactive, memory_wired
    )

    console.print(table)

# CPU Command
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
