from typing import Dict

from prefect import flow, task
from rich import print
import platform


@task(retries=3)
def get_pc_info(*args, **kwargs) -> Dict:
    pc_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    print(pc_info)
    return pc_info


@flow(name="PC Info")
def flow_pc_info(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
    return get_pc_info()


flow_pc_info()
