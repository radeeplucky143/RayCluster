import asyncio


class SubProcess:

    def __init__(self):
        self.process = None
        self.stdout = None
        self.stderr = None
        self.status_code = None
        self.message = None

    async def execute(self, command, success_code, message):
        self.process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        self.stdout, self.stderr = await self.process.communicate()

        if self.process.returncode != 0:
            raise HTTPException(status_code=500, detail=f"{message}: {stderr.decode()}")

        self.status_code = success_code
        self.message = message
