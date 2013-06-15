from wx.richtext import RichTextCtrl
import wx,threading,socket,string

class ServerRTC(RichTextCtrl):
    '''
    self.sck,domain, name, connected, channels
    '''

    def __init__(self,parent,domain,port,*args,**kwargs):
        super(ServerRTC,self).__init__(parent,*args,**kwargs)
        self.Hide()
        self.GetCaret().Hide()         
        self.SetSize((1050,954))
        self.SetEditable(False)        
        self.parent=parent
        self.domain=domain
        self.name=self.domain.split('.')[1]
        self.topic_name=''
        self.port=port
        self.connected=False
        self.SetValue(self.domain)

    def makeConnection(self):
        f=open("UserInfo.txt","r")
        username=f.readline().rstrip()
        nickname=f.readline().rstrip()
        realname=f.readline().rstrip()
        f.close()
        #print username,realname,nickname
        self.sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sck.connect((self.domain,self.port))
        self.sck.send('NICK %s\r\n' %(nickname))
        self.sck.send('USER %s STirc STirc %s\r\n' %(username,realname))

        while True:
            data=self.sck.recv(1024)
            #print data
            if data.find('PING') != -1:
                self.sck.send('PONG ' + data.split() [1] + '\r\n')
                if not self.connected:
	    		    self.connected=1
            elif data.find('PRIVMSG')!=-1 :
                msg=string.split(data,':')
                sender=msg[1][0:msg[1].find("!")]
                content=msg[2]
                channel=msg[1].split()[-1].rstrip()
                print sender
                print channel
                print content
                print '------------------'
                #self.channels[channel].WriteText(sender,content)
            else:
                self.WriteText(data)
                self.ShowPosition(self.GetLastPosition())
        
    def joinChannel(self):
        while not self.connected:
            pass
        channelName='#vjtians'
        self.sck.send('JOIN %s\r\n' %(channelName))       
#       self.channels[channelName]=Channel(self,channelname)