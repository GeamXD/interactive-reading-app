import os
import google.generativeai as genai
import torch
from TTS.api import TTS
import PIL.Image
import numpy as np

# Initialize gemini
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# Create gemini model
MODEL = 'gemini-1.5-flash'
MODEL_2 = 'gemini-1.5-pro'
gemini_client = genai.GenerativeModel(MODEL)

def text_from_image(image_path: str) -> str:
    """
    Extracts text from images

    Args:
        image_path: string containing path to image
    Returns:
        A string of text
    """
    image = PIL.Image.open(image_path)
    prompt = 'extract texts only from this image'
    response = gemini_client.generate_content([prompt, image])
    return response.text

def image_recognition(image_path: str) -> str:
    """
    Identify Image being showed
    Args:
        image_path: string containing path to image
    Returns:
        A string of text
    """
    image = PIL.Image.open(image_path)
    prompt = 'what does this image show'
    response = gemini_client.generate_content([prompt, image])
    return response.text

def evaluate_image_recognition(response: str, observation: str) -> str:
    """
    Evaluates users ability in recognizing the image

    Args:
        response: feed back from user
        observation: Observation of image recognition
    Returns:
        A string of text
    """
    prompt = f'Check to see the correctness of {response} to {observation}, and grade the accuracy'
    result = gemini_client.generate_content(prompt)
    return result.text

def text_from_audio(audio_path: str) -> str:
    """
    Extracts text from audio
    Args:
        audio_path: string containing path to image
    Returns:
        A string of text
    """
    audio = genai.upload_file(audio_path)
    prompt = 'extract texts only from this audio'
    response = gemini_client.generate_content([prompt, audio])
    return response.text

def set_questions(text: str) -> str:
    """
    Sets simple question from Uploaded images

    Args:
        text: String of texts
    Returns:
        A string of texts
    """
    prompt = f"""
    Using {text} as basis, set simple questions and answers. 
    """
    report = """
    return simple markdown with questions and answers in good format where users can find the answer at the bottom in this format

    Questions
    Options
    Answer
    explanation 
    """
    result = gemini_client.generate_content([prompt, report])
    return result.text

def text_to_speech(text: str) -> np.array:
    """
    Converts text to speech

    Args:
        text: simple text input
    Returns:
        A numpy array of audio
    """
    pass

def evaluate_passage_reading(passage: str, word: str) -> str:
    """
    Evaluates users reading ability and provides a summary report


   Args:
        passage: Image/Upload converted to text
        word: Speech from user converted to text
    Return:
            A string of texts
"""
    prompt = f"""
    You are a speech expert training youths on how to read properly.
    Highlight mistakes when comparing {passage} with {word},
    point out mistakes in pronunciation, offer solutions which are helpful. keep it short and sweet. Give a rating on a scale of 10, with 1 being lowest and 10 being highest
    return a summary report that is very concise. TAKE NOTE THAT {word} is transcribed audio.
    Treat transcribed text as normal audio response and refer to the speaker.
    Be friendly and Make it interactive. Act like a speech trainer for people with difficult in reading
    return a well structured report.
    NOTE: THIS IS NOT A WRITING EXERCISE BUT FOR PROPER SPEECH AND PRONUNCIATION

    use a well structured format. Keep report very conscise
    """
    response = gemini_client.generate_content(prompt)
    return response.text















# # # Get device
# # device = "cuda" if torch.cuda.is_available() else "cpu"

# # # List available 🐸TTS models
# # print(TTS().list_models())

# # # TTS with fairseq models
# # api = TTS("tts_models/deu/fairseq/vits")
# # api.tts_to_file?


# import torch
# from TTS.api import TTS

# # Get device
# device = "cuda" if torch.cuda.is_available() else "cpu"

# # Init TTS with the target model name
# tts = TTS(model_name="tts_models/en/ek1/tacotron2", progress_bar=False)
# # Run TTS
# text_a = """
# Keras is a deep learning API written in Python that runs on top of TensorFlow. 
# It is quite popular among deep learning users because of its ease of use.
# """
# tts.tts_to_file(text=text_a, file_path='output.wav')

# # api = TTS(model_name="tts_models/eng/fairseq/vits").to(device)
# # api.tts_to_file("This is a test.", file_path="output.wav")
