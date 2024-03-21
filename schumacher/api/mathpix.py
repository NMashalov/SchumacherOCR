import asyncio
import json
import httpx
import typing as tp
from asynciolimiter import LeakyBucketLimiter
from enum import Enum
from pathlib import Path
import os
from getpass import getpass


class MathPixSettings(str,Enum):
    url='https://api.mathpix.com/v3/text'
    matpix_token = "MATHPIX_TOKEN"

class MathPix:
    def __init__(self,rate_limit:int, app_id:str, token: str):
        self.app_id = app_id

        if token is None:
            if  MathPixSettings.matpix_token.value in os.environ:
                self.token = os.environ[MathPixSettings.matpix_token.value]
            else:
                self.token = getpass('Enter Mathpix token:')

        self.limiter = LeakyBucketLimiter(rate=50/60)
        
    def read_folder(self):
        pass

    def process_doc(self,folder:Path):
        if folder.exists():
            folder.mkdir(exist_ok=True)

    async def scan_img(self,img: bytes):
        '''
            Sends image in base64
        '''
        await self.limiter()
        async with httpx.AsyncClient() as client:
            response = await client.post(
                MathPixSettings.url,
                data=json.dumps(
                    {
                    "src": f"data:image/jpeg;base64, {img}",
                    }
                ),
                headers={
                    "app_id": self.app_id,
                    "app_key":  self.token,
                    "Content-Type": "application/json"
                }
            )
            print(response)

