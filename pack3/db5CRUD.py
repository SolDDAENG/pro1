import wx
import wx.xrc
import MySQLdb
import ast

with open('mariadb.txt', mode='r') as ff:  # ( , encoding='UTF8' )
    aa = ff.read()
    config = ast.literal_eval(aa)


class MyFrame2(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(485, 458), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        #         self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )

        bSizer17 = wx.BoxSizer(wx.VERTICAL)

        self.m_panel14 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer18 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText27 = wx.StaticText(self.m_panel14, wx.ID_ANY, u"번호 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText27.Wrap(-1)
        bSizer18.Add(self.m_staticText27, 0, wx.ALL, 5)

        self.txtNo = wx.TextCtrl(self.m_panel14, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.txtNo, 0, wx.ALL, 5)

        self.btnInsert = wx.Button(self.m_panel14, wx.ID_ANY, u"등록", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer18.Add(self.btnInsert, 0, wx.ALL, 5)

        self.m_panel14.SetSizer(bSizer18)
        self.m_panel14.Layout()
        bSizer18.Fit(self.m_panel14)
        bSizer17.Add(self.m_panel14, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel15 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer19 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText28 = wx.StaticText(self.m_panel15, wx.ID_ANY, u"이름 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText28.Wrap(-1)
        bSizer19.Add(self.m_staticText28, 0, wx.ALL, 5)

        self.txtName = wx.TextCtrl(self.m_panel15, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19.Add(self.txtName, 0, wx.ALL, 5)

        self.btnUpdate = wx.Button(self.m_panel15, wx.ID_ANY, u"수정", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19.Add(self.btnUpdate, 0, wx.ALL, 5)

        self.btnConfirm = wx.Button(self.m_panel15, wx.ID_ANY, u"확인", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer19.Add(self.btnConfirm, 0, wx.ALL, 5)

        self.m_panel15.SetSizer(bSizer19)
        self.m_panel15.Layout()
        bSizer19.Fit(self.m_panel15)
        bSizer17.Add(self.m_panel15, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel16 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer20 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText30 = wx.StaticText(self.m_panel16, wx.ID_ANY, u"전화", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText30.Wrap(-1)
        bSizer20.Add(self.m_staticText30, 0, wx.ALL, 5)

        self.txtTel = wx.TextCtrl(self.m_panel16, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.txtTel, 0, wx.ALL, 5)

        self.btnDel = wx.Button(self.m_panel16, wx.ID_ANY, u"삭제", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer20.Add(self.btnDel, 0, wx.ALL, 5)

        self.m_panel16.SetSizer(bSizer20)
        self.m_panel16.Layout()
        bSizer20.Fit(self.m_panel16)
        bSizer17.Add(self.m_panel16, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel17 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer21 = wx.BoxSizer(wx.VERTICAL)

        self.lstMem = wx.ListCtrl(self.m_panel17, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT)
        bSizer21.Add(self.lstMem, 1, wx.ALL | wx.EXPAND, 5)

        self.m_panel17.SetSizer(bSizer21)
        self.m_panel17.Layout()
        bSizer21.Fit(self.m_panel17)
        bSizer17.Add(self.m_panel17, 1, wx.EXPAND | wx.ALL, 5)

        self.m_panel18 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText31 = wx.StaticText(self.m_panel18, wx.ID_ANY, u"인원수 : ", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText31.Wrap(-1)
        bSizer22.Add(self.m_staticText31, 0, wx.ALL, 5)

        self.staCount = wx.StaticText(self.m_panel18, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0)
        self.staCount.Wrap(-1)
        bSizer22.Add(self.staCount, 0, wx.ALL, 5)

        self.m_panel18.SetSizer(bSizer22)
        self.m_panel18.Layout()
        bSizer22.Fit(self.m_panel18)
        bSizer17.Add(self.m_panel18, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer17)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.btnInsert.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnUpdate.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnConfirm.Bind(wx.EVT_BUTTON, self.OnBtnClick)
        self.btnDel.Bind(wx.EVT_BUTTON, self.OnBtnClick)

        self.btnInsert.id = 1
        self.btnUpdate.id = 2
        self.btnConfirm.id = 3
        self.btnDel.id = 4

        self.lstMem.InsertColumn(0, '번호', width=50)
        self.lstMem.InsertColumn(1, '이름', width=50)
        self.lstMem.InsertColumn(2, '전화', width=50)

        self.btnConfirm.Enable(enable=False)  # 수정이 가능 할 때만 확인 선택할 수 있다

        self.ViewListData()

    def __del__(self):
        pass

    def ViewListData(self):
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()

            sql = "select * from pymem"
            cursor.execute(sql)

            self.lstMem.DeleteAllItems()  # 초기화
            count = 0
            for data in cursor:
                i = self.lstMem.InsertItem(65535, 0)  # 65535개의 최대값을 가진다. // 실제로 리스트에 이만큼 데이터를 주는 경우는 없대요
                self.lstMem.SetItem(i, 0, str(data[0]))
                self.lstMem.SetItem(i, 1, data[1])
                self.lstMem.SetItem(i, 2, data[2])
                count += 1
            self.staCount.SetLabelText(str(count))

        except Exception as e:
            wx.MessageBox('ViewListData err : ' + str(e))
        finally:
            cursor.close()
            conn.close()

    # Virtual event handlers, overide them in your derived class
    def OnBtnClick(self, event):
        id = event.GetEventObject().id
        # print(id)
        if id == 1:
            self.MemInsert()  # 등록
        elif id == 2:
            self.MemUpdate()  # 수정준비
        elif id == 3:
            self.MemUpdateOk()  # 수정 처리
        elif id == 4:
            self.MemDelete()  # 삭제 처리
        elif id == 5:
            self.MemUpdateCancel()  # 수정 취소

    def MemInsert(self):
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()

        if no == '' or name == '' or tel == '':
            wx.MessageBox('자료를 입력하시오', '입력', wx.OK)
            return  # 자료가 입력되지 않을 경우 뒤를 실행하지 않고 MemInsert문을 무조건 탈출한다.

        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()

            data = self.SelectData(no)  # 추가용 번호의 등록 가능 여부 판단
            if data != None:  # 데이터가 있다면
                wx.MessageBox('이미 사용 중인 번호입니다', '알림', wx.OK)
                self.txtNo.SetFocus()
                return

            # 추가 계속
            sql = "insert into pymem values(%s, %s, %s)"
            result = cursor.execute(sql,
                                    (no, name, tel))  # 밑에 if에 cursor.execute(sql, (no, name, tel))를 치기 귀찮아서 result로....

            if result == 1:
                conn.commit()
            else:
                conn.rollback()
                # .... 그 외의 다양한 내용이 있겠쥬
                return

            conn.commit()

            self.ViewListData()  # 추가 후 자료(목록) 보기
            self.txtNo.SetValue('')  # 입력 자료 초기화(내용을 추가하면 텍스트박스가 지워짐)
            self.txtName.SetValue('')
            self.txtTel.SetValue('')

        except Exception as e:
            wx.MessageBox('MemInsert err : ' + str(e))
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def MemUpdate(self):  # 수정 준비
        dlg = wx.TextEntryDialog(None, '수정할 번호 입력', '수정')  # 다이얼로그 박스
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue == '':  # 수정할 번호가 입력되지 않았을 경우
                return

            upno = dlg.GetValue()
            # print(upno)
            data = self.SelectData(upno)
            if data == None:  # 수정할땐 번호가 있어야된다
                wx.MessageBox(upno + '번은 등록된 번호가 아닙니다', '알림', wx.OK)
                return

            # 수정 준비 계속
            self.txtNo.SetValue(str(data[0]))  # 수정할 자료를 화면에 표시
            self.txtName.SetValue(data[1])
            self.txtTel.SetValue(data[2])

            self.txtNo.SetEditable(False)  # 번호는 수정에서 제외 // 번호는 수정 못하게 함
            self.btnConfirm.Enable(True)
            self.btnUpdate.SetLabel('취소')
            self.btnUpdate.id = 5  # line 168

        else:
            return

        dlg.Destroy()  # 끝나면 번호 입력하는 창(모달창)을 끝냄

    def MemUpdateOk(self):  # 수정 확인
        no = self.txtNo.GetValue()
        name = self.txtName.GetValue()
        tel = self.txtTel.GetValue()

        if name == '' or tel == '':
            wx.MessageBox('자료를 입력하시오', '입력', wx.OK)
            return  # 자료가 입력되지 않을 경우 뒤를 실행하지 않고 MemInsert문을 무조건 탈출한다.

        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()

            sql = "update pymem set irum=%s, junhwa=%s where bun=%s"
            cursor.execute(sql, (name, tel, no))  # (name, tel, no) : tuple type
            conn.commit()

            self.ViewListData()  # 수정 후 자료 보기
            self.txtNo.SetValue('')  # 입력 자료 초기화(내용을 추가하면 텍스트박스가 지워짐)
            self.txtName.SetValue('')
            self.txtTel.SetValue('')
            self.txtNo.SetEditable(True)
            self.btnUpdate.SetLabel('수정')
            self.btnUpdate.id = 2
            self.btnConfirm.Enable(False)

        except Exception as e:
            wx.MessageBox('MemUpdateOk err : ' + str(e))
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

    def MemDelete(self):  # 자료 삭제
        dlg = wx.TextEntryDialog(None, '삭제할 번호 입력', '수정')  # 다이얼로그 박스
        if dlg.ShowModal() == wx.ID_OK:
            if dlg.GetValue == '':  # 수정할 번호가 입력되지 않았을 경우
                return

            delno = dlg.GetValue()
            data = self.SelectData(delno)
            if data == None:  # 수정할땐 번호가 있어야된다
                wx.MessageBox(delno + '번은 등록된 번호가 아닙니다', '알림', wx.OK)
                return

            # 삭제 준비 계속
            try:
                conn = MySQLdb.connect(**config)
                cursor = conn.cursor()
                sql = "delete from pymem where bun={}".format(delno)
                cursor.execute(sql)
                conn.commit()

                self.ViewListData()  # 삭제 후 자료보기

            except Exception as e:
                wx.MessageBox('MemDelete err : ' + str(e))
                conn.rollback()
            finally:
                cursor.close()
                conn.close()

    def MemUpdateCancel(self):
        self.ViewListData()  # 수정 후 자료 보기
        self.txtNo.SetValue('')  # 입력 자료 초기화(내용을 추가하면 텍스트박스가 지워짐)
        self.txtName.SetValue('')
        self.txtTel.SetValue('')
        self.txtNo.SetEditable(True)
        self.btnUpdate.SetLabel('수정')
        self.btnUpdate.id = 2
        self.btnConfirm.Enable(False)

    def SelectData(self, no):  # 해당 번호의 자료 읽기 (번호 중복 확인)
        try:
            conn = MySQLdb.connect(**config)
            cursor = conn.cursor()
            sql = "select * from pymem where bun={0}".format(no)
            cursor.execute(sql)
            data = cursor.fetchone()
            return data

        except Exception as e:
            wx.MessageBox('SelectData err : ' + str(e))
        finally:
            cursor.close()
            conn.close()


if __name__ == '__main__':
    app = wx.App()
    MyFrame2(None).Show()
    app.MainLoop()

