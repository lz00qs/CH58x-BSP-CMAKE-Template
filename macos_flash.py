import os
import subprocess
import re


# 获取当前 project 的路径
project_path = os.getcwd()

# 获取当前 project 名称
project_name = os.path.basename(project_path)

device_location_id = ""
try:
    cmd = "ioreg -p IOUSB -l -w 0 | grep -B 5 -i '21984'"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, shell=True).stdout
    match = re.search(r"IOUSBHostDevice@(\w+)", result)
    if match:
        device_location_id = match.group(1)
except Exception as e:
    print("No device found")
    exit(1)

if device_location_id == "":
    print("No device found")
    exit(1)

# 检查 hex 文件是否存在
hex_path = project_path + "/build/" + project_name + ".hex"
if os.path.exists(hex_path):
    try:
        os.chdir(project_path + "/macos")
        os.system(
            f"./WCHISPTool_CMD -p 0x{device_location_id} -c ch582_flash.config -o program -f {hex_path}"
        )
    except Exception as e:
        print(e)
        print("Flash failed")
        exit(1)
else:
    print("Hex file not found, please build project first")
    exit(1)
