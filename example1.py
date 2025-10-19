import logfire

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("api_key")

logfire.configure()
logfire.instrument_pydantic_ai()

provider = GoogleProvider(api_key=api_key)
model = GoogleModel("gemini-2.5-flash-lite", provider=provider)

agent = Agent(model)

@agent.tool
async def roulette_wheel(ctx: RunContext[int], square: int) -> str:  
    """check if the square is a winner"""
    return 'winner' if square == ctx.deps else 'loser'


success_number = 18  
result = agent.run_sync('Put my money on square eighteen', deps=success_number)
print(result.output)  
#> True

result = agent.run_sync('I bet five is the winner', deps=success_number)
print(result.output)