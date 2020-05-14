import wx
import wx.xrc
import MySQLdb
import sys
import locale

config = {  # dict타입
    'host': '127.0.0.1',
    'user': 'root',
    'password': '123',
    'database': 'test',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}


class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        #         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"작성자 : 최한솔", wx.DefaultPosition, wx.DefaultSize,
                                           0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        bSizer1.Add(self.m_panel1, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText2 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"상품명 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        bSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.SangName = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.SangName, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"수량 :", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer3.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.SangSu = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(50, -1), 0)
        bSizer3.Add(self.SangSu, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"단가:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer3.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.SangDan = wx.TextCtrl(self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(80, -1), 0)
        bSizer3.Add(self.SangDan, 0, wx.ALL, 5)

        self.SangInsert = wx.Button(self.m_panel2, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.SangInsert, 0, wx.ALL, 5)

        self.m_panel2.SetSizer(bSizer3)
        self.m_panel2.Layout()
        bSizer3.Fit(self.m_panel2)
        bSizer1.Add(self.m_panel2, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel3 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.lstSangpum = wx.ListCtrl(self.m_panel3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer4.Add(self.lstSangpum, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel3.SetSizer(bSizer4)
        self.m_panel3.Layout()
        bSizer4.Fit(self.m_panel3)
        bSizer1.Add(self.m_panel3, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.SangCount = wx.StaticText(self.m_panel4, wx.ID_ANY, u"건수 : 0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.SangCount.Wrap(-1)
        bSizer5.Add(self.SangCount, 0, wx.ALL, 5)

        self.m_panel4.SetSizer(bSizer5)
        self.m_panel4.Layout()
        bSizer5.Fit(self.m_panel4)
        bSizer1.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # lstSangpum 객체에 제목
        self.lstSangpum.InsertColumn(0, '코드', width=100)
        self.lstSangpum.InsertColumn(1, '상품명', width=150)
        self.lstSangpum.InsertColumn(2, '수량', width=100)
        self.lstSangpum.InsertColumn(3, '단가', width=200)
        self.lstSangpum.InsertColumn(4, '금액', width=200)

        # Connect Events
        self.SangInsert.Bind(wx.EVT_BUTTON, self.Onclick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Onclick(self, event):
        if self.SangName.GetValue() == '':
            wx.MessageBox('상품명을  입력하시오', '알림', wx.OK)
            self.SangName.SetFocus()
            return

        if self.SangSu.GetValue() == '':
            wx.MessageBox('수량을  입력하시오', '알림', wx.OK)
            self.SangSu.SetFocus()
            return

        if self.SangDan.GetValue() == '':
            wx.MessageBox('단가를  입력하시오', '알림', wx.OK)
            self.SangDan.SetFocus()
            return

        self.SangpumCheck()

    def SangpumCheck(self):
        try:
            conn = MySQLdb.connect(**config)  # dict타입의 자료는 **를 사용해서 받는다.
            # print(conn) # 연결 확인
            cursor = conn.cursor()  # SQL문 수행을 위한 객체 생성

            # 현재 상품의 최대 코드 가져오기
            sql = 'select max(code) from sangdata'
            cursor.execute(sql)
            code = cursor.fetchone()[0]

            code += 1
            sang = self.SangName.GetValue()
            su = self.SangSu.GetValue()
            dan = self.SangDan.GetValue()

            # 상품 추가
            sql = '''
                insert into sangdata(code, sang, su, dan)
                values({0}, '{1}', '{2}', '{3}')
            '''.format(code, sang, su, dan)
            count = cursor.execute(sql)

            # 상품 추가 확인
            if count <= 0:
                wx.MessageBox('상품 추가 실패', '알림', wx.OK)
                return
            else:
                conn.commit()
                self.DisplayData()

        except Exception as e:
            print('SangpumCheck err : ', e)
        finally:
            cursor.close()
            conn.close()

    def DisplayData(self):  # 출력
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()

            # 상품 목록 출력
            sql = '''
                select code, sang, su, dan
                from sangdata
            '''

            cursor.execute(sql)
            datas = cursor.fetchall()

            self.lstSangpum.DeleteAllItems()  # 초기화 작업

            for d in datas:
                i = self.lstSangpum.InsertItem(1000, 0)
                self.lstSangpum.SetItem(i, 0, str(d[0]))
                self.lstSangpum.SetItem(i, 1, d[1])
                self.lstSangpum.SetItem(i, 2, str(d[2]))
                self.lstSangpum.SetItem(i, 3, str(d[3]))
                price = d[2] * d[3]
                self.lstSangpum.SetItem(i, 4, locale.format_string('%d', price, grouping=True))

            self.SangCount.SetLabelText('건수 : ' + str(len(datas)))

        except Exception as e:
            print('DisplayData err : ', e)
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':  # main 모듈이면 설정
    # 앱 생성자 콜
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()
