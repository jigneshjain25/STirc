from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.internet import reactor
from ChannelRTC import ChannelRTC
import wx

class STirc(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)

    def signedOn(self):
        for cha in self.factory.favchan:
            self.join(cha)
        print "Signed on as %s." % (self.nickname,)        

    def joined(self, channel):        
        print "Joined %s." % (channel,)
        MainScreen = self.factory.parent.MainScreen
        srtc = self.factory.parent        
        MainScreen.middle.chat_panel = wx.Panel(MainScreen.middle,size=(-1,-1),id=-1)
        crtc = ChannelRTC(MainScreen.middle.chat_panel,channel,'newTopic','gaurav')            
        MainScreen.AddChannelNode(srtc.TreeItemId,crtc)
        MainScreen.middle.SetChatWindow(crtc)

    def topicUpdated(self,user,channel,newTopic):
        print "%s set topic '%s'" % (user,newTopic,)
        print "%s %s %s" % (channel,newTopic,self.nickname)        
    
    def privmsg(self, user, channel, msg):
        print msg
        print type(self.factory.parent)
        self.factory.parent.AppendText(msg)

    def irc_NOTICE(self, prefix, params):        
        print prefix                
        for param in params:
            print param             
            self.factory.parent.AppendText(param+'\n')    

class STircFactory(protocol.ClientFactory):
    protocol = STirc

    def __init__(self,parent,nickname='twistedTrial'):        
        self.nickname = nickname
        self.parent = parent
        self.favchan = []

    def buildProtocol(self, address):
        proto = protocol.ClientFactory.buildProtocol(self, address)
        self.connectedProtocol = proto
        return proto        

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)        
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)    

    def setFavChannels(self,list):
        self.favchan = list

'''
if __name__=="__main__":
    factory = STircFactory(None,"TomRiddle")
    mylist = ['#vjtians','#tp','nonsense']
    factory.setFavChannels(mylist)
    connector = reactor.connectTCP('irc.dejatoons.net',6667,factory)
    reactor.run()  
    print factory.connectedProtocol._get_nickname()  
'''
