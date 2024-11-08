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
        self.timer.start(1000)
        
    def stop_record(self):
        ws=obsws("localhost", webport, password)
        ws.connect()
        ws.call(requests.StopRecord())
        ws.disconnect()
        self.timer.stop()
        self.label.setText("录制已停止")
    
    def toggle_record(self):
        ws=obsws("localhost", webport, password)
        ws.connect()
        ws.call(requests.ToggleRecordPause())
        ws.disconnect() 
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("obs控制")
        control_rec_Widget = QWidget(self)
        control_rec_Widget_v = QWidget(self)
        
        button_start_rec = QPushButton("开始录制", control_rec_Widget)
        button_start_rec.clicked.connect(self.start_record)
        
        button_stop_rec = QPushButton("停止录制", control_rec_Widget)
        button_stop_rec.clicked.connect(self.stop_record)
        
        button_toggle_rec = QPushButton("暂停", control_rec_Widget)
        button_toggle_rec.clicked.connect(self.toggle_record)
        
        control_rec_Widget_v.setLayout(QVBoxLayout())
        
        control_rec_Widget.setLayout(QHBoxLayout())
        control_rec_Widget.layout().addWidget(button_start_rec)
        control_rec_Widget.layout().addWidget(button_stop_rec)
        control_rec_Widget.layout().addWidget(button_toggle_rec)
        
        control_rec_Widget_v.layout().addWidget(control_rec_Widget)
         # 创建一个标签并添加到布局中
        self.label = QLabel("请开始录制", control_rec_Widget_v)
        control_rec_Widget_v.layout().addWidget(self.label)
        
         # 设置计时器，每秒更新一次标签内容
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_label)
          # 每秒更新一次
        
        
        self.setWidget(control_rec_Widget_v)


    def canvasChanged(self, canvas):
        pass
    
    def update_label(self):
        ws=obsws("localhost", webport, password)
        ws.connect()
        status=ws.call(requests.GetRecordStatus()).datain
        if status["outputPaused"] == True:
            self.label.setText("obs状态: 录制已暂停")
        else:
            self.label.setText("obs状态: " + status ["outputTimecode"])
        if status["outputActive"] == False:
            self.label.setText("录制已停止")
        #self.label.setText("obs状态: " + status ["outputTimecode"])
        ws.disconnect()

Krita.instance().addDockWidgetFactory(DockWidgetFactory("obs_control_Docker", DockWidgetFactoryBase.DockRight, obs_control_Docker))