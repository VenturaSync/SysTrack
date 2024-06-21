import typer
from systrack.system_monitor import get_memory_usage, get_cpu_usage, get_disk_usage, get_network_stats, get_sensor_temps
from systrack.hardware_info import get_cpu_info
from systrack.dashboard import create_dashboard
from rich.console import Console
from rich.table import Table
from rich import box
from rich.markdown import Markdown
from typer import Context

app = typer.Typer()
console = Console()

def custom_help(ctx: Context):
    """
    Display custom help message using rich.
    """
    console = Console()
    help_text = """
    # SysTrack Help
    
    **Usage**: `systrack [OPTIONS] COMMAND [ARGS]...`
    
    **Options**:
    - `--help`: Show this message and exit.
    
    **Commands**:
    - `memory`: Displays memory usage statistics.
    - `cpu`: Displays CPU usage statistics.
    - `disk`: Displays disk usage statistics.
    """
    console.print(Markdown(help_text))

# Set the callback for --help to use the custom_help function
app.callback(invoke_without_command=True)(custom_help)

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

# Disk Command
@app.command()
def disk():
    """Displays disk usage statistics."""
    # typer.echo(get_disk_usage())
    Disk_Usage = get_disk_usage()
    total_disk = str(Disk_Usage["total"]) + " GB"
    used_disk = str(Disk_Usage["used"]) + " GB"
    free_disk = str(Disk_Usage["free"]) + " GB"
    percent_disk_used = str(Disk_Usage["percent used"]) + "%"

    table = Table(title="Disk Stats", box=box.HEAVY)

    table.add_column("Total", justify="center", style="bold yellow", overflow="ellipsis")
    table.add_column("Used", style="bold yellow", overflow="ellipsis")
    table.add_column("Free", style="bold yellow", overflow="ellipsis")
    table.add_column("Used %", style="bold yellow", overflow="ellipsis")

    table.add_row(
        total_disk, used_disk, free_disk, percent_disk_used
    )

    console.print(table)

# Network Command
@app.command()
def network():
    """Displays network statistics."""
    # typer.echo(get_network_stats())
    Network_Stats = get_network_stats()
    bytes_sent = str(Network_Stats["bytes sent"]) + " B"
    bytes_recv = str(Network_Stats["bytes received"]) + " B"
    packets_sent = str(Network_Stats["packets sent"])
    packets_recv = str(Network_Stats["packets received"])

    table = Table(title="Network Stats", box=box.MINIMAL)

    table.add_column("Bytes Sent", justify="center", style="bold blue", overflow="ellipsis")
    table.add_column("Bytes Received", style="bold blue", overflow="ellipsis")
    table.add_column("Packets Sent", style="bold blue", overflow="ellipsis")
    table.add_column("Packets Received", style="bold blue", overflow="ellipsis")

    table.add_row(
        bytes_sent, bytes_recv, packets_sent, packets_recv
    )

    console.print(table)

# Sensors Command
@app.command()
def temperature():
    """Displays sensor temperature statistics, if available."""
    message = get_sensor_temps()
    console.print(message, style="bold green",justify="center")

# Hardware Command
@app.command()
def hardware():
    cpu_info = get_cpu_info()
    brand_raw = cpu_info["brand_raw"]
    cores = str(cpu_info["count"])
    bits = str(cpu_info["bits"])
    arch_string_raw = cpu_info["arch"]

    table = Table(title="Hardware Info", box=box.MINIMAL)

    table.add_column("CPU Brand", justify="center", style="bold cyan2", overflow="ellipsis")
    table.add_column("Cores", style="bold cyan2", overflow="ellipsis")
    table.add_column("Bits", style="bold cyan2", overflow="ellipsis")
    table.add_column("Architecture", style="bold cyan2", overflow="ellipsis")

    table.add_row(
        brand_raw, cores, bits, arch_string_raw
    )

    console.print(table)

# Dashboard Command
@app.command()
def dashboard():
    """Displays a live dashboard of system statistics that changes dynamically."""
    create_dashboard()

if __name__ == "__main__":
    app()
