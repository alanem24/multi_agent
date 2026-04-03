
from agents.llm import llm

from pydantic import BaseModel, Field

class GetWeather(BaseModel):
    '''Get the current weather in a given location'''

    location: str = Field(
        ..., description="The city and state, e.g. San Francisco, CA"
    )

class GetPopulation(BaseModel):
    '''Get the current population in a given location'''

    location: str = Field(
        ..., description="The city and state, e.g. San Francisco, CA"
    )

model_with_tools = llm.bind_tools(
    [GetWeather, GetPopulation]
    # strict = True  # Enforce tool args schema is respected
)
ai_msg = model_with_tools.invoke(
    "Which city is hotter today and which is bigger: LA or NY?"
)
print(ai_msg)