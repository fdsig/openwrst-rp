import subprocess
import json
def speed_test():
    result = subprocess.run(["speedtest-cli", "--secure", "--json"], capture_output=True, text=True)
    print(result.stdout)
    data = json.loads(result.stdout)
    print(data)

speed_test()

