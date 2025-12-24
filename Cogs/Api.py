from discord.ext import commands
from fastapi import FastAPI, APIRouter
import uvicorn
import asyncio
from pydantic import BaseModel

class BanRequest(BaseModel):
    mod_id: int
    user_id: int
    guild_id: int

class SendMessageRequest(BaseModel):
    channel_id: int
    message: str

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
        self.router.add_api_route("/ban_user", self.POST_ban_user, methods=["POST"])
        self.router.add_api_route("/send_message", self.POST_send_message, methods=["POST"])
    async def GET_health_check(self):
        return {"status": "ok"}
    async def GET_ping(self):
        return {"message": "pong"}
    
    async def POST_ban_user(self, data: BanRequest):
        guild = self.bot.get_guild(data.guild_id)
        if guild is None:
            return {"error": "Guild not found"}, 404
        mod = self.bot.get_user(data.mod_id)
        if not mod or not mod.guild_permissions.ban_members or not mod.guild_permissions.administrator:
            return {"error": "Moderator does not have ban permissions"}, 403
        user = guild.get_member(data.user_id)
        if user is None:
            return {"error": "User not found in guild"}, 404
        await guild.ban(user, reason="Banned via API")
        return {"status": f"User {data.user_id} has been banned by moderator {data.mod_id}"} 
    
    # class SendMessageRequest(BaseModel):
    #     channel_id: int
    #     message: str
    
    async def POST_send_message(self, data: SendMessageRequest):
        channel = self.bot.get_channel(data.channel_id)
        if channel is None:
            return {"error": "Channel not found"}, 404
        await channel.send(data.message)
        return {"status": f"Message sent to channel {data.channel_id}"}
    
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