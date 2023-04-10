from paddlespeech.cli.tts.infer import TTSExecutor
tts = TTSExecutor()
tts(text="今天天气十分不错。今天天气十分不错。", output="output.wav")
# tts(text="How are you. What's your name", output="output_en.wav") 
