import logfire

from pydantic_ai import Agent, RunContext
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from pydantic_ai.common_tools.duckduckgo import duckduckgo_search_tool

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("api_key")

logfire.configure()
logfire.instrument_pydantic_ai()
provider = GoogleProvider(api_key=api_key)
model = GoogleModel("gemini-2.5-pro", provider=provider)

agent = Agent(
                model=model,
                tools=[duckduckgo_search_tool()],
                system_prompt='Search DuckDuckGo for the given query and return the results. Use duckduckgo_search tool whenever you need to look up information.',
            )

result = agent.run_sync(
    'Can you list the top five highest-grossing animated films of 2025?'
)
print(result.output)