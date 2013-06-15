#!usr/bin/python

import wx
import wx.richtext
import re
from time import strftime, localtime


class ChannelRTC (wx.richtext.RichTextCtrl):
    
    def __init__ (self, cname, nick):
        self.name = cname
        self.logging = True
        self.nick = nick
        self.HLColor = wx.Color(255,0,0)
        self.selfColor = wx.Color(96, 96, 96)
        #self.SetEditable(False)
        self.smileys = [":)", ":(", ":D", ":P", ":p", ":@", ":|", ":\\", ":/", ":*", "xD", "-_-", ":'(", ":o", ":O", "(y)"]
        self.images = ["happy.png", "sad.png", "laugh.png", "p.png", "p.png", "angry.png", "straight.png", "slash.png","slash.png" ,"kiss.png", "xD.png", "-_-.png", "cry.png", "o.png", "o.png", "thumbsup.png"]   
        
    def ParseString (self, string):
        positions = []
        strlen = len(string)
        smlen = len(self.smileys)
        
        for i in range(0, smlen):
            start = 0
            while True:
                a = string.find(self.smileys[i],start, strlen)
                if a != -1:
                    positions.append([i, a])
                    start = a + len(self.smileys[i])
                else:
                    break
        positions.sort(key=lambda x: x[1])
        return positions

    def ContainsNick(self, string, source):
        return source != self.nick and self.nick in string
    
    def AttachTime(self, string):
        curtime = localtime()
        if self.logging:
            with open(self.name+".txt", "a") as myfile:
                myfile.write(strftime("%Y-%m-%d %H:%M:%S", curtime)+string)
        return "["+strftime("%H:%M:%S", curtime)+"] "+string
    
    def AddLine (self, string, nick):
        self.SetEditable(False)
        
        #nick specifies whether msg came from server or textbox
        string.replace("\\", "\\\\")
        boolean = self.ContainsNick(string, nick)
        if boolean:
            self.BeginTextColour(self.RedColor)
        elif nick == self.nick:
            self.BeginTextColour(self.selfColor)
        string = "<"+nick+"> "+string
        string = self.AttachTime(string)
        pos = self.ParseStrings(string)
        if len(pos) == 0:
            a.AppendText(string)
        else:
            start = 0
            for i in range(0, len(pos)):
                smno = pos[i][0]
                smpos = pos[i][1]
                a.WriteText(string[start:smpos])
                i = wx.Image("smilies/"+self.images[smno])
                a.WriteImage(i)
                start = smpos+len(self.smileys[smno])
            a.AppendText(str[start:len(string)])
        if boolean:
            self.EndTextColour()
        
        
# a = ChannelRTC("hi", "lol")
# print a.AttachTime("hiiii")