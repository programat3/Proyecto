import logfire

from pydantic_ai import Agent, Tool
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider

from tools_for_example3 import test_python_org_search

from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("api_key")

logfire.configure()
logfire.instrument_pydantic_ai()
provider = GoogleProvider(api_key=api_key)
model = GoogleModel("gemini-2.5-pro", provider=provider)

agent_py = Agent(
                model=model,
                deps_type=str,
                tools=[Tool(test_python_org_search)],
                system_prompt='Use the tool to search for the given country on python.org and return the URL of the PyCon page.',
            )

result = agent_py.run_sync(
    'Find me the PyCon Italy page on python.org', deps='Italy')
print(result.output)