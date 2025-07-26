from pydantic_ai import Agent
from agent.output.output_response import Questions
from agent.prompt.prompt import prompt
from dotenv import load_dotenv
load_dotenv()

agente_entrevista = Agent("deepseek:deepseek-chat",system_prompt=prompt,output_type=Questions)

