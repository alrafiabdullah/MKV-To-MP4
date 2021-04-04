import os
import subprocess

if not os.path.exists("assets"):
    raise Exception("Please create and put all your vidoes in assets folder!")

mkv_list = os.listdir("assets")

if not os.path.exists("result"):
    os.mkdir("result")


for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)
    if ext != ".mkv":
        raise Exception("Please add MKV files only!")

    output_name = name + ".mp4"
    try:
        subprocess.run(
            ["ffmpeg", "-i", f"assets/{mkv}", "-codec", "copy", f"result/{output_name}"], check=True)
    except:
        raise Exception(
            "Please DOWNLOAD, INSTALL & ADD the path to Environment Variables!")


print(f"{len(mkv_list)} video(s) converted to MP4!")
os.startfile("result")
