from PIL import Image
from openai import OpenAI
import pytesseract as pyt
import os

pyt.pytesseract.tesseract_cmd = r"C:\Users\kumar\Downloads\tesseract-ocr-w64-setup-5.5.0.20241111.exe"

api_key="" # Your API key

while True:
    path = input("Enter the path to your image: ")
    path = fr"{path}"
    path = path.replace('"', "")

    if os.path.exists(path) and not os.path.isdir(path):
        break

    print("The path either does not exist or the path is of a directory")

image = Image.open(path)
text = pyt.image_to_string(image)

client = OpenAI(
  api_key=api_key
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "grade this paragraph on a scale of 1-10 and if it is not 10, tell me how to make it better: " + text},
  ]
)

print(completion.choices[0].message.content)