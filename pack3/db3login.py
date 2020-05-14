# GUI
import wx
import wx.xrc
import MySQLdb
import sys

config = {  # dict타입
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"직원 관리 고객", pos=wx.DefaultPosition, size=wx.Size(500, 339),
                          style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        #         self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel10 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"사번", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer4.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.txtNo = wx.TextCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.txtNo, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"직원명", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer4.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.txtName = wx.TextCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.txtName, 0, wx.ALL, 5)

        self.btnLogin = wx.Button(self.m_panel10, wx.ID_ANY, u"로그인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.btnLogin, 0, wx.ALL, 5)

        self.m_panel10.SetSizer(bSizer4)
        self.m_panel10.Layout()
        bSizer4.Fit(self.m_panel10)
        bSizer3.Add(self.m_panel10, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel11 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.staMsg = wx.StaticText(self.m_panel11, wx.ID_ANY, u"정보", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staMsg.Wrap(-1)
        bSizer5.Add(self.staMsg, 0, wx.ALL, 5)

        self.m_panel11.SetSizer(bSizer5)
        self.m_panel11.Layout()
        bSizer5.Fit(self.m_panel11)
        bSizer3.Add(self.m_panel11, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel12 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.lstGogek = wx.ListCtrl(self.m_panel12, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer6.Add(self.lstGogek, 1, wx.ALL, 5)

        self.m_panel12.SetSizer(bSizer6)
        self.m_panel12.Layout()
        bSizer6.Fit(self.m_panel12)
        bSizer3.Add(self.m_panel12, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel13 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.staCount = wx.StaticText(self.m_panel13, wx.ID_ANY, u"인원수 : 0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staCount.Wrap(-1)
        bSizer7.Add(self.staCount, 0, wx.ALL, 5)

        self.m_panel13.SetSizer(bSizer7)
        self.m_panel13.Layout()
        bSizer7.Fit(self.m_panel13)
        bSizer3.Add(self.m_panel13, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

        self.Centre(wx.BOTH)

        # lstGogek 객체에 제목
        self.lstGogek.InsertColumn(0, '고객번호', width=100)
        self.lstGogek.InsertColumn(1, '고객명', width=150)
        self.lstGogek.InsertColumn(2, '고객전화', width=200)

        # Connect Events
        self.btnLogin.Bind(wx.EVT_BUTTON, self.OnLogin)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnLogin(self, event):
        if self.txtNo.GetValue() == '':
            wx.MessageBox('사번을  입력하시오', '알림', wx.OK)
            self.txtNo.SetFocus()
            return

        if self.txtName.GetValue() == '':
            wx.MessageBox('직원명을  입력하시오', '알림', wx.OK)
            self.txtNo.SetFocus()
            return

        self.LoginCheck()

    def LoginCheck(self):
        try:
            conn = MySQLdb.connect(**config)  # dict타입의 자료는 **를 사용해서 받는다.
            # print(conn) # 연결 확인
            cursor = conn.cursor()  # SQL문 수행을 위한 객체 생성
            no = self.txtNo.GetValue()
            name = self.txtName.GetValue()

            sql = '''
                select count(jikwon_no)
                from jikwon
                where jikwon_no='{0}' and jikwon_name='{1}'
            '''.format(no, name)

            cursor.execute(sql)
            count = cursor.fetchone()[0]  # fetchone : 하나만 넘어옴
            # print(count)

            if count <= 0:
                wx.MessageBox('로그인 실패', '알림', wx.OK)
                return
            else:
                self.staMsg.SetLabelText(no + ' 번 직원의 관리고객 목록')
                self.DisplayData(no)

        except Exception as e:
            print('LoginCheck err : ', e)
        finally:
            cursor.close()
            conn.close()

    def DisplayData(self, no):  # ListCtrl로 출력
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()

            sql = '''
                select gogek_no, gogek_name, gogek_tel
                from gogek
                where gogek_damsano={}
            '''.format(no)
            # print(sql)

            cursor.execute(sql)
            datas = cursor.fetchall()

            self.lstGogek.DeleteAllItems()  # ListCtrl 초기화

            for d in datas:
                # i = self.lstGogek.InsertItem(sys.maxsize, 0)
                i = self.lstGogek.InsertItem(1000, 0)  # 최대 행 수를 적어줌.
                self.lstGogek.SetItem(i, 0, str(d[0]))  # 고객번호
                self.lstGogek.SetItem(i, 1, d[1])  # 고객명
                self.lstGogek.SetItem(i, 2, d[2])  # 고객전화

            self.staCount.SetLabelText('인원수  : ', str(len(datas)))

        except Exception as e:
            print('LoginCheck err : ', e)
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':  # main 모듈이면 설정
    # 앱 생성자 콜
    app = wx.App()
    MyFrame1(None).Show()
    app.MainLoop()
