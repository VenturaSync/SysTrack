import psutil as psu
from psutil._common import bytes2human

# Get memory usage statistics
def get_memory_usage():
    memory = psu.virtual_memory()
    return {
        'total': bytes2human(memory.total),
        'available': bytes2human(memory.available),
        'percent used': memory.percent,
        'used': bytes2human(memory.used),
        'free': bytes2human(memory.free),
        'active': bytes2human(memory.active),
        'inactive': bytes2human(memory.inactive),
        'wired': bytes2human(memory.wired)
    }
