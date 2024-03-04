import google.generativeai as genai
from gradio_client import Client
import moviepy.editor as mpe
import os
import cv2
import random
# 設定語錄主題
topic = "成功"

# 使用 AI 模型生成語錄
def generate_quote():
	with open("assests/gem.txt", "r") as f:
		API_KEY = f.read()

	prompt = "生成一個關於{topic}的語錄, 大約 300 字"
	genai.configure(api_key=API_KEY)
	model = genai.GenerativeModel(model_name="gemini-pro")
	chat = model.start_chat(history=[])
	response = chat.send_message(prompt)
	# for chunk in response:
	# 	print(chunk.text)
	# write to test.txt encoding="utf-8"
	with open("test.txt", "w", encoding="utf-8") as f:
		f.write(response.text)
  
	return response.text

# 使用 AI 模型生成語音
def generate_voice(text):
	client = Client("https://k2-fsa-text-to-speech.hf.space/--replicas/fdmt0/")
	result = client.predict(
			"Chinese (Mandarin, 普通话)",	# Literal['English', 'Chinese (Mandarin, 普通话)', 'Cantonese (粤语)', 'Min-nan (闽南话)', 'Arabic', 'Afrikaans', 'Bengali', 'Bulgarian', 'Catalan', 'Croatian', 'Czech', 'Danish', 'Dutch', 'Estonian', 'Finnish', 'French', 'Georgian', 'German', 'Greek', 'Gujarati', 'Hungarian', 'Icelandic', 'Irish', 'Italian', 'Kazakh', 'Korean', 'Latvian', 'Lithuanian', 'Luxembourgish', 'Maltese', 'Nepali', 'Norwegian', 'Persian', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Serbian', 'Slovak', 'Slovenian', 'Spanish', 'Swahili', 'Swedish', 'Thai', 'Tswana', 'Turkish', 'Ukrainian', 'Vietnamese']  in 'Language' Radio component
			"csukuangfj/vits-piper-zh_CN-huayan-medium",	
			text,	# str  in 'Input text' Textbox component
			"0",	# str  in 'Speaker ID' Textbox component
			0.9,	# float (numeric value between 0.1 and 10) in 'Speed (larger->faster; smaller->slower)' Slider component
			api_name="/process"
	)
	with open(result[0], "rb") as file:
		audio = file.read()
	with open("test.mp3", "wb") as file:
		file.write(audio)


# 生成影片
def generate_video():
	quote = generate_quote()
	generate_voice(quote)

	# 設定圖片路徑
	image_dir = "success_man_picture/"

	# 設定文字路徑
	text_path = "test.txt"

	# 設定語音路徑
	audio_path = "test.mp3"

	# 讀取圖片
	images = [os.path.join(image_dir, f) for f in os.listdir(image_dir)]

	# Choose a target size (e.g., 640x480)
	target_width = 896
	target_height = 1344

	# dont use the img if is not target size
	for filename in os.listdir(image_dir):
		img = cv2.imread(os.path.join(image_dir, filename))
		if img.shape[0] != target_height or img.shape[1] != target_width:
			os.remove(os.path.join(image_dir, filename))
   
   # random shuffle the images
	random.shuffle(images)
   

	# 讀取文字
	with open(text_path, "r", encoding="utf-8") as f:  # Replace "utf-8" with the identified encoding
		text = f.read()


	# 讀取語音
	audio = mpe.AudioFileClip(audio_path)

	# 建立影片
	video = mpe.ImageSequenceClip(images, fps=0.5)

	# 將文字加入影片
	video = video.set_audio(audio)
	video = video.set_duration(audio.duration)
	video.write_videofile("output.mp4", fps=0.5)

	
# 執行
generate_video()
