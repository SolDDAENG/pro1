import wx
import wx.xrc
import MySQLdb
import ast

config = {

    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True

}

rec_r =0
datas =[]
datas1 =[]

class MyFrame1 ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 869,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        #self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_3DLIGHT ) )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"고객자료", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )
        
        
        self.m_panel1.SetSizer( bSizer2 )
        self.m_panel1.Layout()
        bSizer2.Fit( self.m_panel1 )
        bSizer1.Add( self.m_panel1, 0, wx.ALL|wx.EXPAND, 5 )
        
        self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText2 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"번호", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
        
        self.txtno = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtno, 0, wx.ALL, 5 )
        
        self.m_staticText3 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"고객명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer3.Add( self.m_staticText3, 0, wx.ALL, 5 )
        
        self.txtname = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtname, 0, wx.ALL, 5 )
        
        self.m_staticText4 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"성별", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        bSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
        
        self.txtjen = wx.TextCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer3.Add( self.txtjen, 0, wx.ALL, 5 )
        
        
        self.m_panel2.SetSizer( bSizer3 )
        self.m_panel2.Layout()
        bSizer3.Fit( self.m_panel2 )
        bSizer1.Add( self.m_panel2, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.btn1 = wx.Button( self.m_panel3, wx.ID_ANY, u"처음", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn1, 0, wx.ALL, 5 )
        
        self.btn2 = wx.Button( self.m_panel3, wx.ID_ANY, u"이전", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn2, 0, wx.ALL, 5 )
        
        self.btn3 = wx.Button( self.m_panel3, wx.ID_ANY, u"다음", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn3, 0, wx.ALL, 5 )
        
        self.btn4 = wx.Button( self.m_panel3, wx.ID_ANY, u"마지막", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.btn4, 0, wx.ALL, 5 )
        
        
        self.m_panel3.SetSizer( bSizer4 )
        self.m_panel3.Layout()
        bSizer4.Fit( self.m_panel3 )
        bSizer1.Add( self.m_panel3, 0, wx.EXPAND |wx.ALL, 5 )
        
        self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText5 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"직원명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        bSizer5.Add( self.m_staticText5, 0, wx.ALL, 5 )
        
        self.jik_name = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.jik_name, 0, wx.ALL, 5 )
        
        self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"브서명", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer5.Add( self.m_staticText6, 0, wx.ALL, 5 )
        
        self.jik_buser = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.jik_buser, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"전화", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer5.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.jik_tel = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.jik_tel, 0, wx.ALL, 5 )
        
        self.m_staticText8 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"직급", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer5.Add( self.m_staticText8, 0, wx.ALL, 5 )
        
        self.jik_jik = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.jik_jik, 0, wx.ALL, 5 )
        
        
        self.m_panel4.SetSizer( bSizer5 )
        self.m_panel4.Layout()
        bSizer5.Fit( self.m_panel4 )
        bSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn1.Bind( wx.EVT_BUTTON, self.onclick )
        self.btn2.Bind( wx.EVT_BUTTON, self.onclick )
        self.btn3.Bind( wx.EVT_BUTTON, self.onclick )
        self.btn4.Bind( wx.EVT_BUTTON, self.onclick )
        
        self.btn1.id=1
        self.btn2.id=2
        self.btn3.id=3
        self.btn4.id=4
        
        self.DbLoad()
        self.DbLoad2()
        
    
    
    # Virtual event handlers, overide them in your derived class
    def onclick( self, event ):
        id = event.GetEventObject().id
        #print(id)
        global rec_r
        
        if id == 1:     #  처음
            rec_r =0
            
        elif id ==2:      #  이전
            rec_r = rec_r -1
            if rec_r <0: rec_r =0
            
        elif id ==3:    #  다음
            rec_r = rec_r +1
            if rec_r >(len(datas)-1): rec_r =(len(datas)-1)
        
        elif id ==4:    #  마지막    
           rec_r = len(datas)-1
           
        self.ShowData(rec_r)
        self.ShowData2(rec_r)

    def DbLoad(self):
        try:
            conn=MySQLdb.connect(**config)
            cursor = conn.cursor()
            #sql = "select gogek_no,gogek_name,gogek_jumin from gogek where gogek_jumin like '_______1'as'남자' or '_______2' as'여자' "
            sql = "SELECT gogek_no,gogek_name,(case when gogek_jumin LIKE '_______1%' then '남' else '여' end ) AS 'gogek_gen' from gogek;"
            cursor.execute(sql)
            
            global datas
            datas = cursor.fetchall()
            
            #print(datas[0][0])
            self.ShowData(rec_r)
            
        except Exception as e:
            print('DbLoad err : '+str(e))
            
        finally:
            cursor.close()
            conn.close()
            
    def DbLoad2(self):
        try:
            conn=MySQLdb.connect(**config)
            cursor = conn.cursor()
            #sql = "select gogek_no,gogek_name,gogek_jumin from gogek where gogek_jumin like '_______1'as'남자' or '_______2' as'여자' "
            sql = "select jikwon_name,buser_name,buser_tel,jikwon_jik from gogek inner join jikwon on gogek_damsano = jikwon_no inner JOIN buser on buser_num = buser_no order by gogek_no asc"
            cursor.execute(sql)
            
            global datas1
            datas1 = cursor.fetchall()
            
            #print(datas[0][0])
            self.ShowData2(rec_r)
            
        except Exception as e:
            print('DbLoad err : '+str(e))
            
        finally:
            cursor.close()
            conn.close()
    
    def ShowData(self,r):
        self.txtno.SetLabelText(str(datas[r][0]))
        self.txtname.SetLabelText(datas[r][1])
        self.txtjen.SetLabelText(str(datas[r][2]))
    
    def ShowData2(self,r):
        self.jik_name.SetLabelText(str(datas1[r][0]))
        self.jik_buser.SetLabelText(datas1[r][1])
        self.jik_tel.SetLabelText(str(datas1[r][2]))
        self.jik_jik.SetLabelText(str(datas1[r][3]))
    
    

if __name__=='__main__':
    app=wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
