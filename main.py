##!/usr/bin/env python3

from gradio_client import Client

import os
import subprocess


API_URL = "https://sanchit-gandhi-whisper-jax.hf.space/"

# set up the Gradio client
client = Client(API_URL)


def transcribe_audio(audio_path, task="transcribe", return_timestamps=True):
	"""Function to transcribe an audio file using the Whisper JAX endpoint."""
	if task not in ["transcribe", "translate"]:
		raise ValueError("task should be one of 'transcribe' or 'translate'.")

	text, runtime = client.predict(
		audio_path,
		task,
		return_timestamps,
		api_name="/predict_1",
	)
	return text


# Get the current directory
current_path = os.getcwd()

# Loop through all files in the current directory
for filename in os.listdir(current_path):
	filepath = os.path.join(current_path, filename)

	# Check if the file is a video file
	if os.path.isfile(filepath) and filename.lower().endswith(('.mp4', '.avi', '.mkv', '.mov')):
		print(f"Processing video file: {filename}")

		# Extract audio using ffmpeg
		audio_filename = f"{os.path.splitext(filename)[0]}_audio.mkv"
		ffmpeg_command = f"ffmpeg -i \"{filepath}\" -y -vn -acodec copy \"{audio_filename}\""

		ffmpeg_process = subprocess.Popen(ffmpeg_command, shell=True)

		# Wait for the process to finish
		ffmpeg_process.wait()

		print(f"Audio extracted and saved as: {audio_filename}")

		transcribe_input = f"{current_path}/{audio_filename}"

		# transcribe and return timestamps
		output_with_timestamps = transcribe_audio(transcribe_input, return_timestamps=True)

		print(output_with_timestamps)


		def convert_to_srt(transcript):
			lines = transcript.split('\n')
			srt_content = ''
			counter = 1

			for line in lines:
				if '->' in line:
					times, text = line.split('] ', 1)
					start_time, end_time = times.strip('[ ').split(' -> ')

					srt_content += f"{counter}\n{start_time.replace('.', ',')} --> {end_time.replace('.', ',')}\n{text}\n\n"
					counter += 1

			return srt_content.strip()

		transcript = output_with_timestamps

		srt_content = convert_to_srt(transcript)

		# Save to a file
		with open(f"{current_path}/{filename}.srt", 'w', encoding='utf-8') as file:
			file.write(srt_content)

		print(f"Conversion complete. SRT file created: {filename}.srt")

		print(f"Deleting audio file.")

		os.remove(transcribe_input)

