#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import logging
import pyttsx3

q = queue.Queue()
synthesizer = pyttsx3.init()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def choose_random_question():
    return "Hallo wie gehts dir?"


def ask_question():
    synthesizer.say(choose_random_question())
    logging.debug("question: " + choose_random_question())
    synthesizer.say(choose_random_question())
    synthesizer.runAndWait()
    synthesizer.stop()
    return 0


def start_loop():
    input_device = "hw:1,0"
    try:
        device_info = sd.query_devices(input_device, 'input')
        samplerate = int(device_info['default_samplerate'])
        model = vosk.Model("model")

        with sd.RawInputStream(samplerate=samplerate, blocksize=8000, device=input_device, dtype='int16',
                               channels=1, callback=callback):
            rec = vosk.KaldiRecognizer(model, samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    result = rec.Result()
                    logging.debug(result)
                    if "frage" in result:
                        ask_question()

    except KeyboardInterrupt:
        logging.info('\nDone')
        sys.exit(0)
    except Exception as e:
        logging.error(type(e).__name__ + ': ' + str(e))
        sys.exit(0)


if __name__ == '__main__':
    engine = pyttsx3.init("espeak")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[11].id)  # English


    def speak(text):
        engine.say(text)
        engine.runAndWait()


    speak("Hello World and this is a test.")
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
    # start_loop()
