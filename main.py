import openai
import requests
import tkinter
from tkinter import *
from PIL import Image, ImageTk
theprompt=str(input("Enter the full prompt: "))
openai.api_key = open("API_KEY.txt","r").readline()
response = openai.Image.create(
prompt=theprompt,
n=1,
size="1024x1024"
)
image_url = response['data'][0]['url']  
response1 = requests.get(image_url)
with open("image.jpg", "wb") as f:
    f.write(response1.content)
root = Tk()
root.geometry("1024x1024")
image1 = Image.open("image.jpg")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)
root.mainloop()
