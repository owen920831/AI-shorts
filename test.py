from gradio_client import Client

with open("test.txt", "rb") as file:
    prompt = file.read().decode("utf-8")

client = Client("https://k2-fsa-text-to-speech.hf.space/--replicas/fdmt0/")
result = client.predict(
		"Chinese (Mandarin, 普通话)",	# Literal['English', 'Chinese (Mandarin, 普通话)', 'Cantonese (粤语)', 'Min-nan (闽南话)', 'Arabic', 'Afrikaans', 'Bengali', 'Bulgarian', 'Catalan', 'Croatian', 'Czech', 'Danish', 'Dutch', 'Estonian', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hungarian', 'Icelandic', 'Irish', 'Italian', 'Kazakh', 'Korean', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Maltese', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Thai', 'Tswana', 'Turkish', 'Ukrainian', 'Vietnamese']  in 'Language' Radio component
		"csukuangfj/vits-piper-zh_CN-huayan-medium",	
		prompt,	# str  in 'Input text' Textbox component
		"0",	# str  in 'Speaker ID' Textbox component
		0.9,	# float (numeric value between 0.1 and 10) in 'Speed (larger->faster; smaller->slower)' Slider component
		api_name="/process"
)
with open(result[0], "rb") as file:
    audio = file.read()
with open("test.mp3", "wb") as file:
    file.write(audio)
