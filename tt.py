import os
from google.cloud import texttospeech

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
    # Ensure credentials are set
    if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
        raise Exception("Please set GOOGLE_APPLICATION_CREDENTIALS environment variable")

    # Initialize client
    client = texttospeech.TextToSpeechClient()
    
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

# Example usage
if __name__ == "__main__":
    # Set your Google Cloud credentials
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'demo_service_account.json'
    
    # Example text
    sample_text = 'Keras is a deep learning API written in Python that runs on top of TensorFlow. It is quite popular among deep learning users because of its ease of use'
    
    # Convert text to speech
    try:
        output_file = text_to_wav(
            voice_name='en-GB-Standard-A',
            text=sample_text
        )
        print(f"Successfully generated audio file: {output_file}")
    except Exception as e:
        print(f"Error generating speech: {e}")