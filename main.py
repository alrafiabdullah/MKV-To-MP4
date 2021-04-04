import os

mkv_list = os.listdir("assets")

if not os.path.exists("result"):
    os.mkdir("result")


for mkv in mkv_list:
    name, ext = os.path.splitext(mkv)
    if ext != ".mkv":
        print("Please add MKV files only!")
        break
    output_name = name + ".mp4"
    os.system(
        f"cmd /c ffmpeg -i assets/{mkv} -codec copy result/{output_name}")
