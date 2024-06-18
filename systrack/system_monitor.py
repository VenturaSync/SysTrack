import psutil as psu
from psutil._common import bytes2human

mem_usage = psu.virtual_memory()
print(mem_usage)

THRESHOLD = 100 * 1024 * 1024  # 100MB
if mem_usage.available <= THRESHOLD:
    print("warning")