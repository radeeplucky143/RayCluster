from src.utils.logger_util import Logger
from fastapi import HTTPException
import asyncio


class SubProcess:

    def __init__(self):
        self.process = None
        self.stdout = None
        self.stderr = None
        self.status_code = None
        self.message = None
        self.logger = Logger(__name__).create_log_file()

    async def execute(self, command, success_code, message):
        self.logger.info(f"command: {' '.join(command)} executing.")
        self.process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        self.stdout, self.stderr = await self.process.communicate()

        if self.process.returncode != 0:
            self.logger.error(f'Error: {self.stderr}')
            self.logger.error(f'status_code: {success_code}')
            raise HTTPException(status_code=500, detail=f"{message}: {stderr.decode()}")

        self.logger.info(f'Output: {self.stdout}')
        self.logger.info(f'status_code: {status_code}')
        self.status_code = success_code
        self.message = message
