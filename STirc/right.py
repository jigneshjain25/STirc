import wx

class Right(wx.Panel):
	def __init__(self,parent,id):
		wx.Panel.__init__(self,parent,id)
		self.parent = parent
		self.il = wx.ImageList(10,10)
		self.op_count = 0
		self.ord_count = 0

		self.il.Add(wx.Bitmap('images/289.png'))		

		vbox = wx.BoxSizer(wx.VERTICAL)

		self.user_list = wx.ListCtrl(self,-1,style=wx.BORDER_SUNKEN)		
		self.user_list.SetImageList(self.il, wx.IMAGE_LIST_SMALL)
		vbox.Add(self.user_list,1,flag=wx.EXPAND|wx.ALL,border=0)
		vbox.Add((-1,3))

		self.AddOperator('tan')
		self.AddUser('gaurav')
		self.AddUser('jignesh')		
		self.AddOperator('annarajini')		

		vbox.Add(wx.StaticLine(self),flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=10)
		
		self.user_count = wx.StaticText(self,-1,'Total',style=wx.ALIGN_CENTER)
		vbox.Add(self.user_count, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, border=0)
		vbox.Add((-1,5))			

		self.SetUserCount('2 ops, 4 total')

		self.SetSizerAndFit(vbox)

	def SetUserCount(self,text):
		self.user_count.SetLabel(text)

	def AddOperator(self,text):				
		self.user_list.InsertStringItem(self.op_count,text)
		self.user_list.SetItemImage(self.op_count,0)		
		self.op_count+=1

	def  AddUser(self,text):
		self.user_list.InsertStringItem(self.op_count+self.ord_count,text)
		self.ord_count+=1