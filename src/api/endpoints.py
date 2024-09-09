from fastapi import APIRouter, HTTPException

from src.utils.yaml_util import Yaml
from src.utils.subprocess_utils import SubProcess
import asyncio

router = APIRouter()

@router.post("/create-node")
async def create_node(node_name: str):
    """
    Creates a new Tailscale node with the given name.
    - **node_name** (str): The desired name for the new Tailscale node.

    Raises:
    - HTTPException: If the node creation fails.
    """

    try:
        commands = Yaml().load_yaml()
        SubProcess.execute(commands['node_creation'], success_code=201, message='Node creation failed')
        return {"status": "Node created and authenticated successfully"}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")


@router.post("/start-ray-cluster")
async def start_ray_cluster():
    """
    Starts a Ray cluster using Docker containers.
    This endpoint attempts to build and run Docker images for the Ray head node and worker nodes.

    Raises:
    - HTTPException: If any of the Docker commands fail.
    """

    try:
        commands = Yaml().load_yaml()

        SubProcess.execute(commands['build_ray_head'], success_code=201, message='Building Ray head image failed')
        SubProcess.execute(commands['running_ray_head'], success_code=201, message='Running Ray head container failed')
        SubProcess.execute(commands['build_ray_worker'], success_code=201, message='Building Ray worker image failed')
        SubProcess.execute(commands['run_ray_worker'], success_code=201, message='Running Ray worker container failed')
        return {"status": "Ray cluster started successfully"}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
