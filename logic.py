import os
import google.generativeai as genai
import PIL.Image
import numpy as np
import streamlit as st
from google.cloud import texttospeech
from google.oauth2 import service_account

# Create credentials
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

# Initialize gemini
genai.configure(api_key=st.secrets['GEMINI_API_KEY'])

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
    prompt = f'Check to see the correctness of {response} to {observation}, and grade the accuracy on scale of 10. keep it very short and sweet'
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
    prompt = 'extract texts only from audio'
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
    NOTE: IF YOU FACE A SITUATION WHERE NO QUESTIONS CAN BE GENERATED, SAY SO.
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

def text_to_wav(voice_name: str, text: str, output_filename: str = None) -> str:
    """
    Convert text to speech using Google Cloud Text-to-Speech API and save as WAV file.
    
    Args:
        voice_name (str): The voice name (e.g., 'en-GB-Standard-A')
        text (str): The text to convert to speech
        output_filename (str, optional): Custom output filename. If None, uses voice name
    
    Returns:
        str: Path to the generated audio file
    
    Raises:
        Exception: If credentials are not properly set up
    """
    # Initialize client
    client = texttospeech.TextToSpeechClient(credentials=credentials)
    
    # Extract language code from voice name (e.g., 'en-GB' from 'en-GB-Standard-A')
    language_code = "-".join(voice_name.split("-")[:2])
    
    # Create the synthesis input
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    # Configure voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code=language_code,
        name=voice_name
    )
    
    # Configure audio output
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    
    # Generate the speech
    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )
    
    # Generate output filename if not provided
    if output_filename is None:
        output_filename = f"{voice_name}.wav"
    elif not output_filename.endswith('.wav'):
        output_filename += '.wav'
    
    # Save the audio content
    with open(output_filename, "wb") as out:
        out.write(response.audio_content)
        print(f'Generated speech saved to "{output_filename}"')
    
    return output_filename


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