from typing import Dict
import json

from prefect import task
from rich import print
import platform


@task(name="Get PC Info", tags=["os"], version="0.1.1", persist_result=True)
def get_pc_info(*args, **kwargs) -> Dict:
    pc_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    pc_info = json.loads(json.dumps(pc_info))
    print("PC Information:", pc_info)
    return pc_info
