import sounddevice as sd
import soundfile as sf
import speechregonition as sr
import text_to_speech as ts
import os
import boto3
import time
import json

def record_audio(duration, output_file):
    # Set the audio parameters
    sample_rate = 44100  # Sample rate in Hz
    channels = 2        # Stereo

    # Record audio
    ts.say("Recording started. ")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)

    # Wait for recording to complete
    sd.wait()

    # Save the recording to a file
    sf.write(output_file, recording, sample_rate)

    ts.say(f"Recording saved to {output_file}")

# Example usage: record audio for 5 seconds and save to "output.wav" file
def convert_audio_text():
    record_audio(10,"output.wav")
    x = "output.wav"
    os.system(f"curl -X PUT  https://vfodi1nfs1.execute-api.ap-south-1.amazonaws.com/mytriggerfors3/myupload/{x} --upload-file {x}")
    s3 = boto3.client('s3')
    time.sleep(5)
    response = s3.get_object(Bucket='mytranscribebucket12345',Key='output.txt')
    text = response['Body'].read().decode('utf-8')
    output = json.loads(text)
    result = output['results']['transcripts'][0]['transcript']
    def write_to_file(file_path, text):
        with open(file_path, 'w') as file:
            file.write(text)


# Example usage: write "Hello, World!" into a file named "output.txt"
    write_to_file("output.txt", result)
    ts.say("Output Converted to text and Suceesfully saved as output.txt")