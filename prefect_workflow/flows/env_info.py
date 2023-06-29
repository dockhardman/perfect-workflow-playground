from typing import Dict, TYPE_CHECKING

from prefect import flow
from rich import print

from prefect_workflow.shared.pc_info import get_pc_info

if TYPE_CHECKING:
    from prefect.futures import PrefectFuture


@flow(name="Get Enviriment Information", version="0.1.1", persist_result=True)
def get_env_info(*args, **kwargs) -> Dict:
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

    env_info = {}
    pf_future: "PrefectFuture" = get_pc_info.submit(*args, **kwargs)

    pc_info = pf_future.result(timeout=20.0)
    env_info.update(**pc_info)
    return env_info
