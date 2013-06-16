from twisted.words.protocols import irc
from twisted.internet import protocol
from twisted.internet import reactor

class STirc(irc.IRCClient):
    def _get_nickname(self):
        return self.factory.nickname
    nickname = property(_get_nickname)

    def signedOn(self):
        #self.join(self.factory.channel)
        print "Signed on as %s." % (self.nickname,)        

    def joined(self, channel):
        print "Joined %s." % (channel,)

    def privmsg(self, user, channel, msg):
        print msg
        print type(self.factory.parent)
        self.factory.parent.AppendText(msg)

    def irc_NOTICE(self, prefix, params):        
        print prefix        
        print type(self.factory.parent)
        for param in params:
            print param             
            self.factory.parent.AppendText(param+'\n')

    #def dataReceived(self, line):
        #pass

class STircFactory(protocol.ClientFactory):
    protocol = STirc

    def __init__(self,parent ,nickname='twistedTrial'):        
        self.nickname = nickname
        self.parent = parent

    def buildProtocol(self, address):
        proto = protocol.ClientFactory.buildProtocol(self, address)
        self.connectedProtocol = proto
        return proto        

    def clientConnectionLost(self, connector, reason):
        print "Lost connection (%s), reconnecting." % (reason,)        
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "Could not connect: %s" % (reason,)    

if __name__=="__main__":
    chan = 'vjtians'    
    factory = STircFactory()
    connector = reactor.connectTCP('irc.dejatoons.net',6667,factory)
    reactor.run()  
    print factory.connectedProtocol._get_nickname()  