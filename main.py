from PySide6.QtWidgets import QApplication,QButtonGroup,QInputDialog,QLineEdit
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
import subprocess

app=QApplication()
loader=QUiLoader()
file=QFile('fangui2.ui')

window=loader.load(file)
file.close

text,ok = QInputDialog.getText(None,"You need root privileges","Password:",QLineEdit.Password)
if ok:
    password=text



fixed_speed=window.spinBox.value()


def setmode():
    keyaccess=password
    if keyaccess:
        if window.silent_mode.isChecked():
            mode=0
        elif window.normal_mode.isChecked():
            mode=1
        elif window.gaming_mode.isChecked():
            mode=2
        elif window.custom_mode.isChecked():
            mode=3
        elif window.auto_mode.isChecked():
            mode=4
        elif window.fixed_mode.isChecked():
            mode=5
            setspeed()

        com = subprocess.run(f"echo {keyaccess}|sudo -S sh -c 'echo '{mode}' > /sys/devices/platform/aorus_laptop/fan_mode'",capture_output=True,shell=True)
        print(com.returncode)

        

def setspeed():
    keyaccess=password
    fixed_speed=window.spinBox.value()
    subprocess.run(f"echo {keyaccess}|sudo -S sh -c 'echo '{fixed_speed}' > /sys/devices/platform/aorus_laptop/fan_custom_speed'",capture_output=True,shell=True)
    
def chargelimit():
    keyaccess=password
    charge_limit=window.charging_limit.value()
    if password:
        subprocess.run(f"echo {keyaccess}|sudo -S sh -c 'echo '{charge_limit}' > /sys/devices/platform/aorus_laptop/charge_limit'",capture_output=True,shell=True)

window.applymode_btn.clicked.connect(setmode)
window.applylimit_btn.clicked.connect(chargelimit)

window.show()

app.exec()
