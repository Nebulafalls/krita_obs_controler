from PyQt5.QtWidgets import *
from krita import *
from .obswebsocket import *

webport=4455
password="XoVO1rxSMY67xfbV"

class obs_control_Docker(DockWidget):

    
    def start_record(self):
        ws=obsws("localhost", webport, password)
        ws.connect()
        ws.call(requests.StartRecord())
        ws.disconnect()
        
    def __init__(self):
        super().__init__()
        self.setWindowTitle("obs控制")
        start_stop_rec_Widget = QWidget(self)
        self.setWidget(start_stop_rec_Widget)
        button_start_stop_rec = QPushButton("开始录制", start_stop_rec_Widget)
        button_start_stop_rec.clicked.connect(self.start_record)
    def canvasChanged(self, canvas):
        pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("obs_control_Docker", DockWidgetFactoryBase.DockRight, obs_control_Docker))