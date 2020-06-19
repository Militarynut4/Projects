import os, time, sys
from PIL import Image

print("#####")
for filename in os.listdir('./photos'):
    print(filename)
print("#####")

while True:
    print("\nPlease choose a file! Ex. {cat.png}")
    file_name = input("Filename: ")

    if not os.path.isfile(f"./photos/{file_name}"):
        print("\nError, This photo does not exist!")
    else:
      break  

print("\nWhat extension do you want?")
ext = input("Extension: ")

print("\nWhat name for the file?")
name = input(":")

photo = Image.open(f'./photos/{file_name}')

if str(file_name).endswith("png"):
    photo = photo.convert("RGB")

try:
    photo.save(f"./output/{name + '.' + ext.lower()}")
except:
    print("OOPS, We run into some problems!")

print("Successfully converted the image!")
input("Press enter to close")