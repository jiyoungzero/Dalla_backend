from __future__ import division
from django.shortcuts import render

import time

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
import requests
import json

import re
import sys

from google.cloud import speech
import pyaudio
# import six 
import queue
# from six.moves import queue
from threading import Thread
import time

# Audio recording parameters
RATE = 16000
CHUNK = int(RATE / 10)  # 100ms

class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True
        self.isPause = False

    def __enter__(self):
        self._audio_interface = pyaudio.PyAudio()
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            channels=1, rate=self._rate,
            input=True, frames_per_buffer=self._chunk,
            stream_callback=self._fill_buffer,
        )

        self.closed = False

        return self

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()


        self.closed = True
        self._buff.put(None)
        self._audio_interface.terminate()

    def pause(self):
        if self.isPause == False:
            self.isPause = True


    def resume(self):
        if self.isPause == True:
            self.isPause = False


    def status(self):
        return self.isPause

    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        if self.isPause == False:
            self._buff.put(in_data)
        #else
        return None, pyaudio.paContinue

    def generator(self):
        while not self.closed:
            chunk = self._buff.get()
            if chunk is None:
                return

            data = [chunk]

            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data)


# [END audio_stream]



class Gspeech(Thread):
    def __init__(self):
        Thread.__init__(self)

        self.language_code = 'ko-KR'  # a BCP-47 language tag

        self._buff = queue.Queue()

        self.client = speech.SpeechClient()
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=RATE,
            language_code=self.language_code)
        self.streaming_config = speech.StreamingRecognitionConfig(
            config=self.config,
            single_utterance=True, # 한 단어 인식 후 종료되도록 추가한 옵션
            interim_results=True)

        self.mic = None
        self.status = True

        self.daemon = True
        self.start()

    def __eixt__(self):
        self._buff.put(None)

    def run(self):
        with MicrophoneStream(RATE, CHUNK) as stream:
            self.mic = stream
            audio_generator = stream.generator()
            requests = (speech.StreamingRecognizeRequest(audio_content=content)
                        for content in audio_generator)

            responses = self.client.streaming_recognize(self.streaming_config, requests)

            # Now, put the transcription responses to use.
            self.listen_print_loop(responses, stream)
        self._buff.put(None)
        self.status = False

    def pauseMic(self):
        if self.mic is not None:
            self.mic.pause()

    def resumeMic(self):
        if self.mic is not None:
            self.mic.resume()

    # 인식된 Text 가져가기
    def getText(self, block = True):
        return self._buff.get(block=block)

    # 음성인식 처리 루틴
    def listen_print_loop(self, responses, mic):
        num_chars_printed = 0
        try:
            for response in responses:
                if not response.results:
                    continue

                result = response.results[0]
                if not result.alternatives:
                    continue

                transcript = result.alternatives[0].transcript
                overwrite_chars = ' ' * (num_chars_printed - len(transcript))
                if not result.is_final:
                    sys.stdout.write(transcript + overwrite_chars + '\r')
                    sys.stdout.flush()
                    #### 추가 ### 화면에 인식 되는 동안 표시되는 부분.
                    num_chars_printed = len(transcript)
                else:
                    # 큐에 넣는다.
                    self._buff.put(transcript+overwrite_chars)
                    num_chars_printed = 0
        except:
            return

###
###
###

def apic(request):
    gsp = Gspeech()
    while True:
        stt = gsp.getText()
        if stt is None:
            break
        print(stt)
        time.sleep(0.01)
        break
    return render(request, 'button.html', {'result':stt})
    # return HttpResponse(str(stt))


# # 인증키 : dc17f42ec0927fb4b40b8ae0c0066050
# import wave
# import asyncio
# import datetime
# import asyncio
# import json
# from os.path import exists
# # OpenSources, need install
# # https://pypi.org/project/websockets/
# import websockets
# # https://pypi.org/project/aiofile/
# from aiofile import AIOFile, Reader

# class WebSocketClient():
#     # Custom class for handling websocket client
#     def __init__(self, url, onStartMessage, bits_per_seconds):
#         self.url=url
#         # chunk size is depend on sendfile duration, which is now 0.02s(20ms)
#         # set chunk size as byte unit
#         self.chunksize=bits_per_seconds*0.02/8
#         self.onStartMessage = onStartMessage
#         pass

#     async def connect(self):
#         self.connection = await websockets.connect(self.url)
#         if self.connection.open:
#             await self.connection.send(json.dumps(self.onStartMessage))
#             return self.connection

#     async def receiveMessage(self, connection):
#         while True:
#             try:
#                 message = await connection.recv()
#                 print(message)
#             except websockets.exceptions.ConnectionClosed as e:
#                 print('Connection with server closed')
#                 break
#             except Exception as e:
#                 print(e)

#     async def sendfile(self, connection, filepath):
#         try:
#             async with AIOFile(filepath, 'rb') as afp:
#                 reader = Reader(afp, chunk_size=self.chunksize)
#                 async for chunk in reader:
#                     await connection.send(chunk)
#                     await asyncio.sleep(0.02)
#         except Exception as e:
#             print(e)

# def argsChecks(args):
#     # Check given arguments are valid
#     # Plase check guide for more details
#     if not exists(args["filepath"]):
#         raise "Please give exist filepath in filepath args"
    
#     filepath = args["filepath"]
#     onStartMessage = {
#         "type": "recogStart",
#         "service": "DICTATION",
#         "requestId": "GNTWSC-{}".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S')),
#         "showFinalOnly": args["showFinalOnly"],
#         "showExtraInfo": args["showExtraInfo"],
#     }
#     if filepath.endswith(".wav"):
            
#         with wave.open(filepath, 'rb') as wf:
#             bit_depth = wf.getsampwidth() * 8
#             samplerate = wf.getframerate()
#             channels = wf.getnchannels()
#             onStartMessage["audioFormat"] = "RAWPCM/{bitDepth}/{sampleRate}/{channel}/_/_".format(bitDepth=bit_depth, sampleRate=samplerate, channel=channels)
#             bits_per_seconds = bit_depth * samplerate * channels
#     else:
#             # If file is PCM data
#             onStartMessage["audioFormat"] = "RAWPCM/16/16000/1/_/_"
#             bits_per_seconds = 256000
#     return args["url"], filepath, onStartMessage, bits_per_seconds

# if __name__ == '__main__':
#     args = {
#         "url": "wss://6471d23f-5937-4bcd-ba58-ca4de6dcda15.api.kr-central-1.kakaoi.io/ai/speech-to-text/ws/long?signature=9793206ecc9144aea3d42a7ab93f1108&x-api-key=dc17f42ec0927fb4b40b8ae0c0066050",
#         "filepath": "{FILE PATH}",
#         "showFinalOnly": False,
#         "showExtraInfo": False,
#     }
    
#     url, filepath, onStartMessage, bits_per_seconds = argsChecks(args)

#     # Creating client object
#     client = WebSocketClient(url, onStartMessage, bits_per_seconds)
#     loop = asyncio.get_event_loop()
#     # Start connecting
#     connection = loop.run_until_complete(client.connect())
#     # Define async jobs
#     tasks = [
#         asyncio.ensure_future(client.sendfile(connection, filepath)),
#         asyncio.ensure_future(client.receiveMessage(connection)),
#     ]
#     # Run async jobs
#     loop.run_until_complete(asyncio.wait(tasks))





