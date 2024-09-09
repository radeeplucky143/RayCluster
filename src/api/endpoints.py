from fastapi import APIRouter, HTTPException
from src.utils.yaml_util import Yaml
from src.utils.subprocess_utils import SubProcess
from src.utils.logger_util import Logger
import asyncio

router = APIRouter()

@router.post("/create_node")
async def create_node(node_name: str):
    """
    Creates a new Tailscale node with the given name.
    - **node_name** (str): The desired name for the new Tailscale node.

    Raises:
    - HTTPException: If the node creation fails.
    """

    try:
        logger = Logger(__name__).create_log_file()
        commands = Yaml().load_yaml()

        SubProcess().execute(commands['node_creation'], success_code=201, message='Tailscale Node creation failed')
        logger.info('Tailscale node created successfully.')
        return {"message": "Tailscale Node created and authenticated successfully", "status_code": 201}

    except Exception as e:
        logger.error(f'Exception: {e}')
        return {"status_code":500, "message":f"{e}"}


@router.post("/start_ray_cluster")
async def start_ray_cluster():
    """
    Starts a Ray cluster using Docker containers.
    This endpoint attempts to build and run Docker images for the Ray head node and worker nodes.

    Raises:
    - HTTPException: If any of the Docker commands fail.
    """

    try:
        logger = Logger(__name__).create_log_file()
        commands = Yaml().load_yaml()

        SubProcess().execute(commands['build_ray_head'], success_code=201, message='Building Ray head image failed')
        logger.info('Building Ray head image successfully.')
        SubProcess().execute(commands['running_ray_head'], success_code=201, message='Running Ray head container failed')
        logger.info('Running Ray head container successfully.')
        SubProcess().execute(commands['build_ray_worker'], success_code=201, message='Building Ray worker image failed')
        logger.info('Building Ray worker image successfully')
        SubProcess().execute(commands['run_ray_worker'], success_code=201, message='Running Ray worker container failed')
        logger.info('Running Ray worker container successfully')
        return {"status_code": 200, "message": "Ray cluster started successfully"}


    except Exception as e:
        logger.error(f'Exception: {e}')
        return {"status_code":500, "message":f"{e}"}
