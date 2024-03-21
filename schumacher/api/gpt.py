from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from functools import partial
from openai import OpenAI
import typing as tp
from enum import Enum
import os
from getpass import getpass

class AssistantSettings(str,Enum):
    OpenAI_env = 'OPENAI_TOKEN'
    OpenAI_url ='https://openrouter.ai/api/v1'


class OpenAITranslator:
    def __init__(self, api_key: tp.Optional[str] = None):
        if api_key is None:
            if AssistantSettings.OpenAI_env in os.environ:
                api_key = os.environ[AssistantSettings.OpenAI_env]
            else:
                api_key = getpass('Enter OpenAI token')

        self.client = OpenAI(
            base_url=AssistantSettings.OpenAI_url,
            api_key=api_key,
        )

    def call_openai_api(self,entry,pbar):
        answer = self.client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": f"Translate markdown from English to Russian. Preserve equations form :\n {entry}"
                },
            ],
        )