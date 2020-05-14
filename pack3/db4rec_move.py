import wx
import wx.xrc
import ast
import MySQLdb

rec_r = 0
datas = []

with open('../../../Downloads/pack3/mariadb.txt', mode ='r') as ff: # ( , encoding='UTF8' )
    aa = ff.read()
    config = ast.literal_eval(aa)
    
class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 395,278 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
#         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer6 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText6 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"코드 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.txtCode = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtCode, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"품명 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer7.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.txtSang = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.txtSang, 0, wx.ALL, 5 )
        
        
        self.m_panel5.SetSizer( bSizer7 )
        self.m_panel5.Layout()
        bSizer7.Fit( self.m_panel5 )
        bSizer6.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText8 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"수량 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer8.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.txtSu = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtSu, 0, wx.ALL, 5 )
        
        self.m_staticText9 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"단가 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        bSizer8.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        self.txtDan = wx.TextCtrl( self.m_panel6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.txtDan, 0, wx.ALL, 5 )
        
        
        self.m_panel6.SetSizer( bSizer8 )
        self.m_panel6.Layout()
        bSizer8.Fit( self.m_panel6 )
        bSizer6.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel7 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"금액 : ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer9.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        self.staKum = wx.StaticText( self.m_panel7, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.staKum.Wrap( -1 )
        bSizer9.Add( self.staKum, 0, wx.ALL, 5 )
        
        
        self.m_panel7.SetSizer( bSizer9 )
        self.m_panel7.Layout()
        bSizer9.Fit( self.m_panel7 )
        bSizer6.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel8, wx.ID_ANY, u"||<<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel8, wx.ID_ANY, u"<", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel8, wx.ID_ANY, u">", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel8, wx.ID_ANY, u">>||", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel8.SetSizer( bSizer10 )
        self.m_panel8.Layout()
        bSizer10.Fit( self.m_panel8 )
        bSizer6.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer6 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btn2.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btn3.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btn4.Bind( wx.EVT_BUTTON, self.OnClick )
        self.btn1.id = 1
        self.btn2.id = 2
        self.btn3.id = 3
        self.btn4.id = 4
       
        self.DbLoad()   # DB를 콘솔창에 출력
    
    
    # Virtual event handlers, overide them in your derived class
    def OnClick( self, event ):
        id = event.GetEventObject().id
        # print(id)   # 버튼(btn) 작동 확인
        
        global rec_r    # rec_r을 전역변수로 함
        
        # 버튼을 누르면 db를 불러옴 
        if id == 1:     # 처음
            rec_r = 0   # 여기에 쓰는 rec_r이 global
        elif id == 2:   # 이전
            rec_r = rec_r - 1
            if rec_r < 0: rec_r = 0
        elif id == 3:   # 다음
            rec_r = rec_r + 1
            if rec_r > (len(datas) - 1): rec_r = (len(datas) - 1)
        elif id == 4:   # 마지막
            rec_r = len(datas) - 1
        
        self.ShowData(rec_r)    # 이걸 마지막에 작성함....
        
    def DbLoad(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from sangdata"
            cursor.execute(sql)
            
            global datas    # datas를 전역변수로 바꿈.
            datas = cursor.fetchall()
            # print(datas[0][0])
            self.ShowData(rec_r)
            
        except Exception as e:
            print('Dbload err : ' + str(e))
        finally:
            cursor.close()
            conn.close()
            
    def ShowData(self, r): # 출력 메소드
        self.txtCode.SetLabelText(str(datas[r][0]))
        self.txtSang.SetLabelText(datas[r][1])
        self.txtSu.SetLabelText(str(datas[r][2]))
        self.txtDan.SetLabelText(str(datas[r][3]))
        self.staKum.SetLabelText(str(datas[r][2] * datas[r][3]))
        
if __name__ == '__main__':  # main 모듈이면 설정
    # 앱 생성자 콜
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
    
    
    
    

