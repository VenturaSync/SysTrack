import psutil as psu
from psutil._common import bytes2human
from utils import bytes_to_gb

# Get memory usage statistics
def get_memory_usage():
    memory = psu.virtual_memory()
    return {
        'total': bytes_to_gb(memory.total),
        'available': bytes_to_gb(memory.available),
        'percent used': memory.percent,
        'used': bytes_to_gb(memory.used),
        'free': bytes_to_gb(memory.free),
        'active': bytes_to_gb(memory.active),
        'inactive': bytes_to_gb(memory.inactive),
        'wired': bytes_to_gb(memory.wired)
    }

# Get the CPU usage statistics
def get_cpu_usage():
    cpu = psu.cpu_percent(interval=1, percpu=True)
    return {
        'cpu count': len(cpu),
        'cpu usage': cpu[0]
    }

# Get the disk usage statistics
def get_disk_usage():
    disk = psu.disk_usage('/')
    return {
        'total': bytes_to_gb(disk.total),
        'used': bytes_to_gb(disk.used),
        'free': bytes_to_gb(disk.free),
        'percent used': disk.percent
    }
