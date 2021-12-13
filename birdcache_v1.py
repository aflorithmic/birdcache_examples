from pprint import pprint
import json
import asyncio
import aiohttp


API_KEY = "YOUR_API_KEY_HERE"
VOICE_NAME = "alessia"
ENDPOINT_URL = "https://v1.api.audio/sync_speech/synthesize"

f = open("sentences.txt", "r")
sentences = f.readlines()
f.close()


def async_tts_creation():
    async def dispense():
        calls = {}
        async with aiohttp.ClientSession() as session:
            for line in sentences:
                line = line.strip()
                print(f"Producing TTS for the sentence: {line}")
                async with session.post(
                    url=ENDPOINT_URL,
                    headers={"x-api-key": API_KEY},
                    data=json.dumps(
                        {
                            "voice": VOICE_NAME,
                            "metadata": "full",
                            "text": line,
                        }
                    ),
                ) as response:
                    result = await response.json()
                    calls[line] = result["audio_url"]

        return calls

    return asyncio.run(dispense())


pprint(async_tts_creation())
