import subprocess
import json
from pathlib import Path
import platform
def speed_test():
    # get ssid
    # get os (mac, linux, windows)
    os = platform.system()
    print(os)
    if os.lower() in ['darwin']:
        process = subprocess.Popen(['networksetup', '-listallhardwareports'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        process.wait()
        # read lines to list
        lines = out.decode('utf-8').split('\n')
        for idx, line in enumerate(lines):
            print(line)
            if 'Wi-Fi' in line:
                print(line)
                device = lines[idx + 1].split(' ')[1]
                print(device)
                process = subprocess.Popen(['networksetup', '-getairportnetwork', device], stdout=subprocess.PIPE)
                out, err = process.communicate()
                process.wait()
                ssid = out.decode('utf-8').split('Current Wi-Fi Network: ')[1].split('\n')[0]
                print(ssid)
    elif os.lower() in ['linux']:
        process = subprocess.Popen(['iwgetid', '-r'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        process.wait()
        ssid = out.decode('utf-8').split('SSID: ')[1].split('\n')[0]
        print(ssid)
    elif os in ['Windows']:
        process = subprocess.Popen(['netsh', 'wlan', 'show', 'interfaces'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        process.wait()
        ssid = out.decode('utf-8').split('SSID  ')[1].split('\n')[0]
        print(ssid)
    else:
        ssid = "unknown"
    speedtest_path = Path("./speedtests.json")
    if not speedtest_path.exists():
        speedtest_json = [{'date': ' ', 'time': ' ', 'download': ' ', 'upload': ' ', 'ping': ' '}]
        with open(speedtest_path, "w") as f:
            json.dump(speedtest_json, f)

    with open(speedtest_path, "r") as f:
        speedtest_json = json.load(f)
    
    result = subprocess.run(["speedtest-cli", "--secure", "--json"], capture_output=True, text=True)
    print(result.stdout)
    data = json.loads(result.stdout)
    data['ssid'] = ssid
    speedtest_json.append(data)
    with open(speedtest_path, "w") as f:
        json.dump(speedtest_json, f)
    

speed_test()


