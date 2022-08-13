from gtts import gTTS
import os 

myText = "Hello Abdul ! One hour completed"
language = "hi"
output = gTTS(text=myText,lang=language,slow=True)

output.save("output.mp3")

os.system("mplayer output.mp3")
