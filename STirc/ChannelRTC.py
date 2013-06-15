#!usr/bin/python
 
import wx
import wx.richtext
import re
from time import strftime, localtime
 
 
class ChannelRTC (wx.richtext.RichTextCtrl):
    def __init__ (self,parent ,cname, tname, nick, *args, **kwargs):
        super(ChannelRTC,self).__init__(parent,*args,**kwargs)
        self.SetSize(wx.GetDisplaySize())
        self.RedColor = wx.Color("red")
        self.SelfColor = wx.Color("grey")
        self.ServerColor = wx.Color("green")
        self.BlueColor = wx.Color("blue")
        self.parent = parent
        self.name = cname
        self.topic_name=tname
        self.logging = True
        self.nick = nick
        self.smileys = [":)", ":(", ":D", ":P", ":p", ":@", ":|", ":\\", ":/", ":*", "xD", "-_-", ":'(", ":o", ":O", "(y)"]
        self.images = ["happy.png", "sad.png", "laugh.png", "p.png", "p.png", "angry.png", "straight.png", "slash.png","slash.png" ,"kiss.png", "xD.png", "-_-.png", "cry.png", "o.png", "o.png", "thumbsup.png"]
       
    def ParseSmiley (self, string):
        positions = []
        strlen = len(string)
        smlen = len(self.smileys)
        for i in range(0, smlen):
            start = 0
            while True:
                a = string.find(self.smileys[i],start, strlen)
                if a != -1:
                    if (len(self.smileys[i]) == strlen):
                        positions.append([i, a])
                        return positions
                    if (a >= 0 and string[a+len(self.smileys[i])-1] == " ") and (a <= strlen - len(self.smileys[i]) and string[a-1] == " "):
                        positions.append([i, a])
                    start = a + len(self.smileys[i])
                else:
                    break
        positions.sort(key=lambda x: x[1])
        return positions
   
    def ParseURL (self, s):
        strlen = len(s)
        urls = re.findall(r'(https?://\S+)', s)
        if (len(urls) == 0):
            self.WriteText(s)
            return
        start = 0
        for i in range(0, len(urls)):
            index = s.find(urls[i], start, strlen)
            self.WriteText(s[start:index])
            self.BeginURL(urls[i])
            self.BeginUnderline()
            self.BeginItalic()
            self.WriteText(urls[i])
            self.EndItalic()
            self.EndUnderline()
            self.EndURL()
            start = index + len(urls[i])
        self.WriteText(s[start:len(s)])
   
    def ContainsNick(self, string, source):
        return source != self.nick and self.nick in string
   
    def AttachTime(self, string):
        curtime = localtime()
        if self.logging:
            with open(self.name+".txt", "a") as myfile:
                myfile.write(strftime("%Y-%m-%d %H:%M:%S", curtime)+string)
        return "["+strftime("%H:%M:%S", curtime)+"] "
   
    def AddLine(self, string):
        string = string.replace("\\", "\\\\")
        pos = self.ParseSmiley(string)
        if len(pos) == 0:
            self.ParseURL(string)
        else:
            start = 0
            for i in range(0, len(pos)):
                smno = pos[i][0]
                smpos = pos[i][1]
                self.ParseURL(string[start:smpos])
                i = wx.Image("smilies/"+self.images[smno])
                self.WriteImage(i)
                start = smpos+len(self.smileys[smno])
            self.ParseURL(str[start:len(string)])
                   
   
    def AddChatMsg (self, string, nick):
        msg = string
        hasnick = self.ContainsNick(string, nick)
        timestamp = self.AttachTime(string)
        self.WriteText(timestamp)
        if hasnick:
            self.BeginBold()
            self.BeginTextColor(self.RedColor)
        elif nick != self.nick:
            self.BeginTextColor(self.BlueColor)
        self.WriteText(" <"+nick+"> ")
        if hasnick:
            self.EndBold()
        elif nick != self.nick:
            self.EndTextColour()
        if nick == self.nick:
            self.BeginTextColour(self.selfColor)
        self.AddLine(msg)
        if hasnick or nick == self.nick:
            self.EndTextColour()
       
    def AddServerMsg(self, string):
        msg = string
        string = "*"+string
        timestamp = self.AttachTime(string)
        self.BeginColor(self.ServerColor)
        self.WriteText(timestamp+ " * ")
        self.AddLine(msg)
        self.EndTextColour()
       
    def AddNoticeMsg(self, string, nick):
        msg = string
        string = " >>"+nick+"<< "+string
        timestamp = self.AttachTime(string)
        self.WriteText(timestamp)
        self.WriteText
        self.AddLine(msg)