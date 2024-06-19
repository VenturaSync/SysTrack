import cpuinfo
import platform
import GPUtil
import psutil
import netifaces
import pySMART


def get_cpu_info():
    return cpuinfo.get_cpu_info()

print(get_cpu_info())