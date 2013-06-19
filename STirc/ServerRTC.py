from wx.richtext import RichTextCtrl
import wx,threading,socket,string,time
from STircFactory import STircFactory
from twisted.internet import reactor

class ServerRTC(RichTextCtrl):

    def __init__(self,parent,MainScreen,domain,port,name,fc=[],*args,**kwargs):
        super(ServerRTC,self).__init__(parent,*args,**kwargs)
        print "Inside ServerRTC"
        self.MainScreen = MainScreen
        self.TreeItemId = None
        self.Hide()
        self.GetCaret().Hide()         
        self.SetSize(wx.GetDisplaySize())
        self.SetEditable(False)        
        self.domain=domain
        self.name=name
        self.topic_name=''
        self.port=port
        self.fc=fc
        self.connected=False        

    def makeConnection(self):
        f=open("UserInfo.txt","r")
        username=f.readline().rstrip()
        nickname=f.readline().rstrip()
        realname=f.readline().rstrip()
        f.close()

        self.factory = STircFactory(self,nickname)
        self.factory.setFavChannels(self.fc)
        reactor.connectTCP(self.domain,self.port,self.factory)
        reactor.run(installSignalHandlers=0)   #required to solve signal only works in main thread error

    def joinChannel(self):
        channelName='#vjtians'
        self.sck.send('JOIN %s\r\n' %(channelName))       

'''
if __name__ == '__main__':
    app = wx.App()
    frame = wx.Frame(None)
    frame.Maximize()
    s = ServerRTC(frame,'irc.dejatoons.net',6667,'Dejatoons',['#vjtians'])
    t = threading.Thread(target = s.makeConnection)
    t.start()
    frame.Show()
    app.MainLoop()

'''
