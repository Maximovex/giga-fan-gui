from PySide6.QtWidgets import QApplication,QButtonGroup
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import subprocess

app=QApplication()
loader=QUiLoader()
file=QFile('fangui.ui')

window=loader.load(file)
file.close

password=window.password_input.text()
#password='Kf8gCe25!@'

fixed_speed=window.spinBox.value()

def setmode():
    password=window.password_input.text()
    if password:
        if window.silent_mode.isChecked():
            subprocess.run(f"echo {password}|sudo -S sh -c 'echo '0' > /sys/devices/platform/aorus_laptop/fan_mode'",capture_output=True,shell=True)
        if window.normal_mode.isChecked():
            subprocess.run(f"echo {password}|sudo -S sh -c 'echo '1' > /sys/devices/platform/aorus_laptop/fan_mode'",capture_output=True,shell=True)
        elif window.gaming_mode.isChecked():
            subprocess.run(f"echo {password}|sudo -S sh -c 'echo '2' > /sys/devices/platform/aorus_laptop/fan_mode'",capture_output=True,shell=True)
        elif window.custom_mode.isChecked():
            subprocess.run(f"echo {password}|sudo -S sh -c 'echo '3' > /sys/devices/platform/aorus_laptop/fan_mode'",capture_output=True,shell=True)
        elif window.auto_mode.isChecked():
            subprocess.run(f"echo {password}|sudo -S sh -c 'echo '4' > /sys/devices/platform/aorus_laptop/fan_mode'",capture_output=True,shell=True)
        elif window.fixed_mode.isChecked():
            subprocess.run(f"echo {password}|sudo -S sh -c 'echo '5' > /sys/devices/platform/aorus_laptop/fan_mode'",capture_output=True,shell=True)
            setspeed()

def setspeed():
    password=window.password_input.text()
    fixed_speed=window.spinBox.value()
    subprocess.run(f"echo {password}|sudo -S sh -c 'echo '{fixed_speed}' > /sys/devices/platform/aorus_laptop/fan_custom_speed'",capture_output=True,shell=True)
    
def chargelimit():
    password=window.password_input.text()
    charge_limit=window.charging_limit.value()
    if password:
        subprocess.run(f"echo {password}|sudo -S sh -c 'echo '{charge_limit}' > /sys/devices/platform/aorus_laptop/charge_limit'",capture_output=True,shell=True)

window.applymode_btn.clicked.connect(setmode)
window.applylimit_btn.clicked.connect(chargelimit)

window.show()

app.exec()
