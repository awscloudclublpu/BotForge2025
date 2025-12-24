from discord.ext import commands
from fastapi import FastAPI, APIRouter
import uvicorn
import asyncio
#Asyncio is needed to run the FastAPI server in the background alongside the Discord bot

my_api = FastAPI()
class ApiCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.router = APIRouter()
        self.register_routes()
        my_api.include_router(self.router)
    def register_routes(self):
        self.router.add_api_route("/health", self.GET_health_check, methods=["GET"])
        self.router.add_api_route("/ping", self.GET_ping, methods=["GET"])
    async def GET_health_check(self):
        return {"status": "ok"}
    async def GET_ping(self):
        return {"message": "pong"}
class ServerAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.uvicorn = uvicorn.Server
        self.task = None
    async def start_api(self):
        config = uvicorn.Config(
            app=my_api,
            host="0.0.0.0",
            port=8000,
        )
        server = uvicorn.Server(config)
        print("Starting API server on http://127.0.0.1:8000")
        await server.serve()
    async def cog_load(self):
        self.task = asyncio.create_task(self.start_api())
async def setup(bot):
    await bot.add_cog(ApiCog(bot))
    await bot.add_cog(ServerAPI(bot))