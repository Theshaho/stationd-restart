
import requests,subprocess,platform,time,tg

command = "sudo systemctl restart stationd"

vpsname = platform.node()

def monitor_stationd():
    try:
      output = subprocess.check_output(command, shell=True, text=True)
      output = "Done"
    except:
      output = "failed"
      
    message = f"On {vpsname} Stationd restart log is:{output}"

    url = f"https://api.telegram.org/bot{tg.TOKEN}/sendMessage?chat_id={tg.chat_id}&text={message}"

    print(requests.get(url).json()) 


while True:
    try:
        monitor_stationd()
    except Exception as e:
        print("An error occurred:", e)

    time.sleep(3600)
