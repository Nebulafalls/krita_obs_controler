import obswebsocket as obsw
webport=4455
password="XoVO1rxSMY67xfbV"
ws=obsw.obsws("localhost", webport, password)
ws.connect()
ws.call(obsw.requests.StartRecord())
##开始录制
##StopRecord 停止录制
ws.disconnect()