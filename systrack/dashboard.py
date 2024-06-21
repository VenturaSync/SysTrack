from rich.console import Console
from rich.live import Live
from rich.table import Table
from systrack.system_monitor import get_memory_usage, get_cpu_usage, get_disk_usage, get_network_stats
import time

def generate_table():
    memory_stats = get_memory_usage()
    cpu_stats = get_cpu_usage()
    disk_stats = get_disk_usage()
    network_stats = get_network_stats()
    
    table = Table(title="System Monitor Dashboard", show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="dim bold", justify="right")
    table.add_column("Value", justify="left")

    table.add_row("Total Memory", f"{memory_stats['total']} GB")
    table.add_row("Available Memory", f"{memory_stats['available']} GB")
    table.add_row("Used Memory", f"{memory_stats['used']} GB")
    table.add_row("CPU Usage (%)", f"{cpu_stats['cpu usage']}")
    table.add_row("Disk Free", f"{disk_stats['free']} GB")
    table.add_row("Network Sent", f"{network_stats['bytes sent']} GB")
    table.add_row("Network Received", f"{network_stats['bytes received']} GB")

    return table

def create_dashboard():
    console = Console()
    duration = 10
    update_interval = 0.5
    iterations = int(duration / update_interval)

    with Live(generate_table(), console=console, refresh_per_second=1, transient=True) as live:
        for _ in range(iterations):
            live.update(generate_table())
            time.sleep(update_interval)

if __name__ == "__main__":
    create_dashboard()
