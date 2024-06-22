<p align="center">
  <img src="images/main.png" alt="alt text">
</p>

<h1 align="center">SysTrack</h1>

<p align='center'>SysTrack is a powerful CLI tool for monitoring and tracking system resources in real-time.</p>

## Features

- Memory usage statistics
- CPU usage tracking
- Disk usage information
- Network statistics
- Hardware information
- Temperature sensors (Linux and FreeBSD)
- Live system dashboard

## Installation

```bash
pip install systracker
```

# SysTrack CLI Commands

This section provides an overview of all available commands in the SysTrack CLI tool.

## systrack help

![systrack help command output](images/systrack_help.png)

The `systrack help` command provides an overview of all available commands in the SysTrack CLI tool. It displays a stylized ASCII art logo of "SysTrack" followed by usage instructions, available options, and a list of all commands with brief descriptions. This command is essential for users to quickly understand the tool's capabilities and how to use each feature. The help output includes information on CPU, dashboard, disk, hardware, memory, network, and temperature commands, giving users a comprehensive guide to monitoring various aspects of their system.

## systrack cpu

![systrack cpu command output](images/systrack_cpu.png)

The `systrack cpu` command provides a quick and visually appealing snapshot of the system's CPU statistics. It displays information in a neatly formatted table with two key metrics:

1. **CPU Cores**: Shows the total number of CPU cores available on the system. In this example, the system has 8 cores.

2. **CPU Usage**: Displays the current CPU utilization as a percentage. The screenshot shows a 24.0% usage, indicating the current load on the CPU.

This command is particularly useful for quickly assessing the CPU's capacity and its current workload. The clear, color-coded output makes it easy to read and interpret at a glance, making it an excellent tool for system administrators and users who need to monitor CPU performance regularly.

## systrack dashboard

![systrack dashboard command output](path_to_systrack_dashboard_screenshot.png)

The `systrack dashboard` command provides a comprehensive real-time overview of key system metrics. This dynamic dashboard displays:

- Total and Available Memory: Shows the system's total RAM (8.0 GB) and currently available memory.
- Used Memory: Indicates the amount of RAM currently in use.
- CPU Usage: Displays current CPU utilization as a percentage (31.3% in this example).
- Disk Free: Shows the amount of free storage space on the system.
- Network Statistics: Provides data on network usage, including sent and received data.

This command is invaluable for system administrators and users who need a quick, all-in-one view of their system's current state and performance.

## systrack disk

![systrack disk command output](path_to_systrack_disk_screenshot.png)

The `systrack disk` command offers a detailed snapshot of the system's disk usage. It presents information in a clear, tabular format:

- Total: Displays the total disk capacity (228.27 GB in this case).
- Used: Shows the amount of disk space currently in use (19.23 GB).
- Free: Indicates the available disk space (28.50 GB).
- Used %: Provides the percentage of disk space utilized (40.3%).

This command is essential for monitoring storage utilization, helping users manage their disk space effectively and plan for future storage needs.

## systrack hardware

![systrack hardware command output](path_to_systrack_hardware_screenshot.png)

The `systrack hardware` command delivers key information about the system's CPU hardware:

- CPU Brand: Identifies the processor (Apple M1 in this instance).
- Cores: Shows the number of CPU cores (8 cores).
- Bits: Indicates the processor architecture bit-depth (64-bit).
- Architecture: Specifies the CPU architecture (ARM_8).

This command is particularly useful for quickly identifying the system's hardware capabilities, which is valuable for software compatibility checks, performance expectations, and system requirements assessments.

## systrack memory

![systrack memory command output](path_to_systrack_memory_screenshot.png)

[Add functionality description for the memory command here]

## systrack network

![systrack network command output](path_to_systrack_network_screenshot.png)

[Add functionality description for the network command here]
