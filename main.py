import os

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
    os.system(
        f"cmd /c ffmpeg -i assets/{mkv} -codec copy result/{output_name}")
