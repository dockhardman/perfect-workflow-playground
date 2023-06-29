from textwrap import dedent
from typing import Dict
import json

from prefect import task
from prefect.artifacts import create_markdown_artifact
from rich import print
import platform


@task(name="Get PC Info", tags=["os"], version="0.2.0", persist_result=True)
def get_pc_info(*args, **kwargs) -> Dict:
    pc_info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
    }
    create_markdown_artifact(
        markdown=dedent(
            """
            ## PC Information
            | Key | Value |
            | --- | --- |
            | System | {System} |
            | Node Name | {Node Name} |
            | Release | {Release} |
            | Version | {Version} |
            | Machine | {Machine} |
            | Processor | {Processor} |
            """
        ).format(**pc_info),
    )
    pc_info = json.loads(json.dumps(pc_info))
    print("PC Information:", pc_info)
    return pc_info
