
import subprocess
from datetime import datetime


def run_command(command):
    """
    Execute a Linux command and return its output.
    """
    try:
        result = subprocess.check_output(
            command,
            shell=True,
            text=True,
            stderr=subprocess.STDOUT
        )
        return result.strip()
    except subprocess.CalledProcessError:
        return "Unable to retrieve information."


def print_section(title):
    print(f"\n{title}")
    print("-" * 50)


def get_hostname():
    print_section("Hostname")
    print(run_command("hostname"))


def get_datetime():
    print_section("Current Date & Time")
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def get_cpu_info():
    print_section("CPU Information")
    print(run_command("lscpu"))


def get_memory_info():
    print_section("Memory Usage")
    print(run_command("free -h"))


def get_disk_info():
    print_section("Disk Usage")
    print(run_command("df -h"))


def get_logged_users():
    print_section("Logged-in Users")
    print(run_command("who"))


def get_top_processes():
    print_section("Top 5 Running Processes (by CPU Usage)")
    print(run_command("ps -eo pid,user,%cpu,comm --sort=-%cpu | head -6"))


def main():
    print("=" * 50)
    print("Linux System Information")
    print("=" * 50)

    get_hostname()
    get_datetime()
    get_cpu_info()
    get_memory_info()
    get_disk_info()
    get_logged_users()
    get_top_processes()


if __name__ == "__main__":
    main()