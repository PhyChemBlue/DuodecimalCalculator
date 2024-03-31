# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 23:57:46 2024

@author: PhyChemBlue
"""

import sys
from Base12UI import Ui_MainWindow
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from fractions import Fraction as frc
import math


DtoT = {'O':0, 'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'K':10, 'L':11}
TtoD = "OABCDEFGHIKL"

def DoztoDec(ns):
    minsgn = False
    if '-' in ns:
        ns = ns[1:]
        minsgn = True
    #Q
    if '.' in ns:
        sn, sq = ns.split('.')
    else:
        sn = ns
        sq = ''
    #N Converter
    nt = 0
    for i in range(len(sn)):
        nt += DtoT[sn[i]] * 12 ** (len(sn) - 1 - i)
    #Q Converter
    for i in range(len(sq)):
        nt += frc(DtoT[sq[i]] , 12 ** (1 + i))
    #Result
    if minsgn:
        nt = -nt
    return nt

def DectoDoz(ni):
    #0
    if ni == 0:
        return "O"
    #Negative
    if ni < 0: 
        prestr = '-'
        ni = abs(ni)
    else:
        prestr = ''
    #Q
    if ni - int(ni) != 0:
        nq = ni - int(ni)
        ni = int(ni)
    else:
        nq = 0
        ni = int(ni)
    #Q Converter
    if nq == 0:
        poststr = ''
    else:
        poststr = '.'
        cnt = 0
        while nq > 0 and cnt < 12:
            nq *= 12
            poststr += TtoD[int(nq)]
            nq -= int(nq)
            cnt += 1
        #Round L
        if TtoD[int(nq * 12)] in "FGHIKL":
            while poststr[-1] == 'L':
                poststr = poststr[:-1]
            if poststr != '.':
                poststr = poststr[:-1] + TtoD[DtoT[poststr[-1]] + 1]
            else:
                poststr += 'O'
                ni += 1
        #Round O
        elif TtoD[int(nq * 12)] in "OABCDE":
            while poststr[-1] == 'O':
                poststr = poststr[:-1]
            if poststr == '.':
                poststr += 'O'
    #N Converter
    res = ''
    while ni > 0:
        res = TtoD[ni % 12] + res
        ni //= 12
    if res == '':
        res = 'O'
    #Result
    return prestr + res + poststr

class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setupUi(self)
        self.connector()
        self.setFixedSize(360, 420)
        self.setWindowTitle("Dozenal Calculator")
        self.stackedWidget.setCurrentIndex(0)
        self.radioButton_Doz.setChecked(True)
        self.RBDoz()
        self.show()
        self.CNA = 0
        self.CNB = 0
        self.Cop = 0
        self.SNA = 0
        self.SNB = 0
        self.Sop = 0
        self.SAns = 0
        self.SM = 0
        self.SRad = 1
    
    #Menu
    def BCDoz(self):
        self.stackedWidget.setCurrentIndex(0)
    def SCDoz(self):
        self.stackedWidget.setCurrentIndex(1)
    def ConvDozDec(self):
        self.stackedWidget.setCurrentIndex(2)
    
    #Basic Calculator
    def BC0(self):
        self.lineEdit_BC1.insert('O')
    def BC1(self):
        self.lineEdit_BC1.insert('A')
    def BC2(self):
        self.lineEdit_BC1.insert('B')
    def BC3(self):
        self.lineEdit_BC1.insert('C')
    def BC4(self):
        self.lineEdit_BC1.insert('D')
    def BC5(self):
        self.lineEdit_BC1.insert('E')
    def BC6(self):
        self.lineEdit_BC1.insert('F')
    def BC7(self):
        self.lineEdit_BC1.insert('G')
    def BC8(self):
        self.lineEdit_BC1.insert('H')
    def BC9(self):
        self.lineEdit_BC1.insert('I')
    def BC10(self):
        self.lineEdit_BC1.insert('K')
    def BC11(self):
        self.lineEdit_BC1.insert('L')
    
    def BCPrsOprtBtn(self):
        self.CNA = DoztoDec(self.lineEdit_BC1.text())
        self.lineEdit_BC2.setText(self.lineEdit_BC1.text())
        if self.lineEdit_BC1.text() == '' or self.lineEdit_BC1.text() == '.':
            self.lineEdit_BC2.setText('O')
        self.lineEdit_BC1.clear()
        self.pushButton_BCdot.setEnabled(True)
        self.pushButton_BCadd.setEnabled(False)
        self.pushButton_BCsub.setEnabled(False)
        self.pushButton_BCmul.setEnabled(False)
        self.pushButton_BCdiv.setEnabled(False)
    
    def BCadd(self):
        self.BCPrsOprtBtn()
        self.Cop = 1
        self.lineEdit_BC2.insert('+')
    def BCsub(self):
        self.BCPrsOprtBtn()
        self.Cop = 2
        self.lineEdit_BC2.insert('-')
    def BCmul(self):
        self.BCPrsOprtBtn()
        self.Cop = 3
        self.lineEdit_BC2.insert('×')
    def BCdiv(self):
        self.BCPrsOprtBtn()
        self.Cop = 4
        self.lineEdit_BC2.insert('÷')
    
    def BCdot(self):
        self.lineEdit_BC1.insert('.')
        self.pushButton_BCdot.setEnabled(False)
    
    def BCBack(self):
        if self.lineEdit_BC1.text() != '':
            if self.lineEdit_BC1.text()[-1] == '.':
                self.pushButton_BCdot.setEnabled(True)
            self.lineEdit_BC1.setText(self.lineEdit_BC1.text()[:-1])
    
    def BCAC(self):
        self.lineEdit_BC1.clear()
        self.lineEdit_BC2.clear()
        self.CNA = 0
        self.CNB = 0
        self.Cop = 0
        self.pushButton_BCdot.setEnabled(True)
        self.pushButton_BCadd.setEnabled(True)
        self.pushButton_BCsub.setEnabled(True)
        self.pushButton_BCmul.setEnabled(True)
        self.pushButton_BCdiv.setEnabled(True)

    def BCeql(self):
        self.CNB = DoztoDec(self.lineEdit_BC1.text())
        try:
            if self.Cop == 1:
                frres = self.CNA + self.CNB
            elif self.Cop == 2:
                frres = self.CNA - self.CNB
            elif self.Cop == 3:
                frres = self.CNA * self.CNB
            elif self.Cop == 4:
                frres = self.CNA / self.CNB
            else:
                frres = self.CNB
            dozres = DectoDoz(frres)
            histxt = self.lineEdit_BC2.text().split(' ')[-1]
            self.lineEdit_BC2.setText(histxt)
            self.lineEdit_BC2.insert(self.lineEdit_BC1.text())
            if self.lineEdit_BC1.text() == '' or self.lineEdit_BC1.text() == '.':
                self.lineEdit_BC2.insert('O')
            self.lineEdit_BC2.insert('=')
            self.lineEdit_BC2.insert(dozres)
            self.lineEdit_BC2.insert(' ')
        except:
            self.lineEdit_BC2.setText("ERROR ")
        self.CNA = 0
        self.CNB = 0
        self.Cop = 0
        self.lineEdit_BC1.clear()
        self.pushButton_BCdot.setEnabled(True)
        self.pushButton_BCadd.setEnabled(True)
        self.pushButton_BCsub.setEnabled(True)
        self.pushButton_BCmul.setEnabled(True)
        self.pushButton_BCdiv.setEnabled(True)
    
    #Scientific Calculator
    def SC0(self):
        self.lineEdit_SC1.insert('O')
    def SC1(self):
        self.lineEdit_SC1.insert('A')
    def SC2(self):
        self.lineEdit_SC1.insert('B')
    def SC3(self):
        self.lineEdit_SC1.insert('C')
    def SC4(self):
        self.lineEdit_SC1.insert('D')
    def SC5(self):
        self.lineEdit_SC1.insert('E')
    def SC6(self):
        self.lineEdit_SC1.insert('F')
    def SC7(self):
        self.lineEdit_SC1.insert('G')
    def SC8(self):
        self.lineEdit_SC1.insert('H')
    def SC9(self):
        self.lineEdit_SC1.insert('I')
    def SC10(self):
        self.lineEdit_SC1.insert('K')
    def SC11(self):
        self.lineEdit_SC1.insert('L')
    
    def SCe(self):
        self.lineEdit_SC1.setText(DectoDoz(math.e))
        self.pushButton_SCdot.setEnabled(False)
    def SCpi(self):
        self.lineEdit_SC1.setText(DectoDoz(math.pi))
        self.pushButton_SCdot.setEnabled(False)
    def SCAns(self):
        self.lineEdit_SC1.setText(DectoDoz(self.SAns))
        if '.' in self.lineEdit_SC1.text():
            self.pushButton_SCdot.setEnabled(False)
    def SCM(self):
        self.lineEdit_SC1.setText(DectoDoz(self.SM))
        if '.' in self.lineEdit_SC1.text():
            self.pushButton_SCdot.setEnabled(False)
    def SCtoM(self):
        DozM = self.lineEdit_SC1.text()
        if DozM == '':
            DozM = 'O'
        self.SM = DoztoDec(DozM)
        self.SCAC()
        self.lineEdit_SC2.setText(DozM + '→M ')
    
    def SCPrsOprtBtn(self):
        self.SNA = DoztoDec(self.lineEdit_SC1.text())
        self.lineEdit_SC2.setText(self.lineEdit_SC1.text())
        if self.lineEdit_SC1.text() == '' or self.lineEdit_SC1.text() == '.':
            self.lineEdit_SC2.setText('O')
        self.lineEdit_SC1.clear()
        self.pushButton_SCdot.setEnabled(True)
        self.pushButton_SCadd.setEnabled(False)
        self.pushButton_SCsub.setEnabled(False)
        self.pushButton_SCmul.setEnabled(False)
        self.pushButton_SCdiv.setEnabled(False)
        self.pushButton_SCpow.setEnabled(False)
        self.pushButton_SCrt.setEnabled(False)
        self.pushButton_SClog.setEnabled(False)
        self.pushButton_SCP12.setEnabled(False)
    
    def SCadd(self):
        self.SCPrsOprtBtn()
        self.Sop = 1
        self.lineEdit_SC2.insert('+')
    def SCsub(self):
        self.SCPrsOprtBtn()
        self.Sop = 2
        self.lineEdit_SC2.insert('-')
    def SCmul(self):
        self.SCPrsOprtBtn()
        self.Sop = 3
        self.lineEdit_SC2.insert('×')
    def SCdiv(self):
        self.SCPrsOprtBtn()
        self.Sop = 4
        self.lineEdit_SC2.insert('÷')
    def SCpow(self):
        self.SCPrsOprtBtn()
        self.Sop = 5
        self.lineEdit_SC2.insert('^')
    def SCrt(self):
        self.SCPrsOprtBtn()
        self.Sop = 6
        self.lineEdit_SC2.setText('√(' + self.lineEdit_SC2.text() + ',')
    def SClog(self):
        self.SCPrsOprtBtn()
        self.Sop = 7
        self.lineEdit_SC2.setText('log(' + self.lineEdit_SC2.text() + ')')
    def SCP12(self):
        self.SCPrsOprtBtn()
        self.Sop = 8
        self.lineEdit_SC2.insert('×AO^')
    
    def SCPrsFunBtn(self):
        DozNum = self.lineEdit_SC1.text()
        if DozNum == '' or DozNum == '.':
            DozNum = 'O'
        self.SCAC()
        return DozNum
    
    def SCmin(self):
        dozx = self.SCPrsFunBtn()
        if '-' in dozx:
            res = dozx[1:]
        elif dozx == 'O':
            res = dozx
        else:
            res = '-' + dozx
        self.lineEdit_SC2.setText('-(' + dozx + ')=' + res)
        self.lineEdit_SC2.insert(' ')
        self.SAns = DoztoDec(res)
    def SCinv(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = 1 / decx
            self.lineEdit_SC2.setText('A/' + dozx + '=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCfct(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.factorial(decx)
            self.lineEdit_SC2.setText(dozx + '!=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCexp(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.exp(decx)
            self.lineEdit_SC2.setText('exp(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCsin(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.sin(decx * self.SRad)
            self.lineEdit_SC2.setText('sin(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCcos(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.cos(decx * self.SRad)
            self.lineEdit_SC2.setText('cos(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCtan(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.tan(decx * self.SRad)
            self.lineEdit_SC2.setText('tan(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCsq(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = decx ** 2
            self.lineEdit_SC2.setText(dozx + '^B=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCcb(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = decx ** 3
            self.lineEdit_SC2.setText(dozx + '^C=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCln(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.log(decx)
            self.lineEdit_SC2.setText('ln(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCasin(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.asin(decx) / self.SRad
            self.lineEdit_SC2.setText('arcsin(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCacos(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.acos(decx) / self.SRad
            self.lineEdit_SC2.setText('arccos(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCatan(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.atan(decx) / self.SRad
            self.lineEdit_SC2.setText('arctan(' + dozx + ')=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCsqrt(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = decx ** (1/2)
            self.lineEdit_SC2.setText('√' + dozx + '=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SCcbrt(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = decx ** (1/3)
            self.lineEdit_SC2.setText('ᶜ√' + dozx + '=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")
    def SClg(self):
        dozx = self.SCPrsFunBtn()
        try:
            decx = DoztoDec(dozx)
            res = math.log(decx, 12)
            self.lineEdit_SC2.setText('log(AO)' + dozx + '=' + DectoDoz(res))
            self.lineEdit_SC2.insert(' ')
            self.SAns = res
        except:
            self.lineEdit_SC2.setText("ERROR ")

    def SCdot(self):
        self.lineEdit_SC1.insert('.')
        self.pushButton_SCdot.setEnabled(False)
    
    def SCBack(self):
        if self.lineEdit_SC1.text() != '':
            if self.lineEdit_SC1.text()[-1] == '.':
                self.pushButton_SCdot.setEnabled(True)
            self.lineEdit_SC1.setText(self.lineEdit_SC1.text()[:-1])
    
    def SCAC(self):
        self.lineEdit_SC1.clear()
        self.lineEdit_SC2.clear()
        self.SNA = 0
        self.SNB = 0
        self.Sop = 0
        self.pushButton_SCdot.setEnabled(True)
        self.pushButton_SCadd.setEnabled(True)
        self.pushButton_SCsub.setEnabled(True)
        self.pushButton_SCmul.setEnabled(True)
        self.pushButton_SCdiv.setEnabled(True)
        self.pushButton_SCpow.setEnabled(True)
        self.pushButton_SCrt.setEnabled(True)
        self.pushButton_SClog.setEnabled(True)
        self.pushButton_SCP12.setEnabled(True)

    def SCeql(self):
        self.SNB = DoztoDec(self.lineEdit_SC1.text())
        try:
            if self.Sop == 1:
                frres = self.SNA + self.SNB
            elif self.Sop == 2:
                frres = self.SNA - self.SNB
            elif self.Sop == 3:
                frres = self.SNA * self.SNB
            elif self.Sop == 4:
                frres = self.SNA / self.SNB
            elif self.Sop == 5:
                frres = self.SNA ** self.SNB
            elif self.Sop == 6:
                frres = self.SNA ** (1 / self.SNB)
            elif self.Sop == 7:
                frres = math.log(self.SNB , self.SNA)
            elif self.Sop == 8:
                frres = self.SNA * 12 ** self.SNB
            else:
                frres = self.SNB
            dozres = DectoDoz(frres)
            histxt = self.lineEdit_SC2.text().split(' ')[-1]
            self.lineEdit_SC2.setText(histxt)
            self.lineEdit_SC2.insert(self.lineEdit_SC1.text())
            if self.lineEdit_SC1.text() == '' or self.lineEdit_SC1.text() == '.':
                self.lineEdit_SC2.insert('O')
            if '(' in self.lineEdit_SC2.text() and ')' not in self.lineEdit_SC2.text():
                self.lineEdit_SC2.insert(')')
            self.lineEdit_SC2.insert('=')
            self.lineEdit_SC2.insert(dozres)
            self.lineEdit_SC2.insert(' ')
            self.SAns = frres
        except:
            self.lineEdit_SC2.setText("ERROR ")
        self.SNA = 0
        self.SNB = 0
        self.Sop = 0
        self.lineEdit_SC1.clear()
        self.pushButton_SCdot.setEnabled(True)
        self.pushButton_SCadd.setEnabled(True)
        self.pushButton_SCsub.setEnabled(True)
        self.pushButton_SCmul.setEnabled(True)
        self.pushButton_SCdiv.setEnabled(True)
        self.pushButton_SCpow.setEnabled(True)
        self.pushButton_SCrt.setEnabled(True)
        self.pushButton_SClog.setEnabled(True)
        self.pushButton_SCP12.setEnabled(True)
    
    def SCRad(self):
        if self.SRad == 1:
            self.SRad = math.pi / 180
            self.SCAC()
            self.lineEdit_SC2.setText("Degree Mode ")
        else:
            self.SRad = 1
            self.SCAC()
            self.lineEdit_SC2.setText("Radian Mode ")
    
    def SCDec(self):
        self.SCAC()
        self.lineEdit_SC2.setText("Ans=" + str(self.SAns) + ' ')

    #Converter
    def CDDozO(self):
        self.lineEdit_Doz.insert('O')
        self.lineEdit_Dec.clear()
    def CDDozA(self):
        self.lineEdit_Doz.insert('A')
        self.lineEdit_Dec.clear()
    def CDDozB(self):
        self.lineEdit_Doz.insert('B')
        self.lineEdit_Dec.clear()
    def CDDozC(self):
        self.lineEdit_Doz.insert('C')
        self.lineEdit_Dec.clear()
    def CDDozD(self):
        self.lineEdit_Doz.insert('D')
        self.lineEdit_Dec.clear()
    def CDDozE(self):
        self.lineEdit_Doz.insert('E')
        self.lineEdit_Dec.clear()
    def CDDozF(self):
        self.lineEdit_Doz.insert('F')
        self.lineEdit_Dec.clear()
    def CDDozG(self):
        self.lineEdit_Doz.insert('G')
        self.lineEdit_Dec.clear()
    def CDDozH(self):
        self.lineEdit_Doz.insert('H')
        self.lineEdit_Dec.clear()
    def CDDozI(self):
        self.lineEdit_Doz.insert('I')
        self.lineEdit_Dec.clear()
    def CDDozK(self):
        self.lineEdit_Doz.insert('K')
        self.lineEdit_Dec.clear()
    def CDDozL(self):
        self.lineEdit_Doz.insert('L')
        self.lineEdit_Dec.clear()
    
    def CDDec0(self):
        self.lineEdit_Dec.insert('0')
        self.lineEdit_Doz.clear()
    def CDDec1(self):
        self.lineEdit_Dec.insert('1')
        self.lineEdit_Doz.clear()
    def CDDec2(self):
        self.lineEdit_Dec.insert('2')
        self.lineEdit_Doz.clear()
    def CDDec3(self):
        self.lineEdit_Dec.insert('3')
        self.lineEdit_Doz.clear()
    def CDDec4(self):
        self.lineEdit_Dec.insert('4')
        self.lineEdit_Doz.clear()
    def CDDec5(self):
        self.lineEdit_Dec.insert('5')
        self.lineEdit_Doz.clear()
    def CDDec6(self):
        self.lineEdit_Dec.insert('6')
        self.lineEdit_Doz.clear()
    def CDDec7(self):
        self.lineEdit_Dec.insert('7')
        self.lineEdit_Doz.clear()
    def CDDec8(self):
        self.lineEdit_Dec.insert('8')
        self.lineEdit_Doz.clear()
    def CDDec9(self):
        self.lineEdit_Dec.insert('9')
        self.lineEdit_Doz.clear()
    
    def CDDozDot(self):
        self.lineEdit_Doz.insert('.')
        self.pushButton_DozDot.setEnabled(False)
        self.lineEdit_Dec.clear()
    def CDDecDot(self):
        self.lineEdit_Dec.insert('.')
        self.pushButton_DecDot.setEnabled(False)
        self.lineEdit_Doz.clear()
    
    def CDDozAC(self):
        self.lineEdit_Doz.clear()
        self.pushButton_DozDot.setEnabled(True)
        self.lineEdit_Dec.clear()
    def CDDecAC(self):
        self.lineEdit_Dec.clear()
        self.pushButton_DecDot.setEnabled(True)
        self.lineEdit_Doz.clear()
    
    def CDDozOK(self):
        try:
            self.lineEdit_Dec.setText(str(float(round(DoztoDec(self.lineEdit_Doz.text()), 12))))
        except:
            self.lineEdit_Dec.setText("ERROR")
    def CDDecOK(self):
        try:
            self.lineEdit_Doz.setText(DectoDoz(float(self.lineEdit_Dec.text())))
        except:
            self.lineEdit_Doz.setText("ERROR")
    
    def RBDoz(self):
        self.pushButton_Dec0.setEnabled(False)
        self.pushButton_Dec1.setEnabled(False)
        self.pushButton_Dec2.setEnabled(False)
        self.pushButton_Dec3.setEnabled(False)
        self.pushButton_Dec4.setEnabled(False)
        self.pushButton_Dec5.setEnabled(False)
        self.pushButton_Dec6.setEnabled(False)
        self.pushButton_Dec7.setEnabled(False)
        self.pushButton_Dec8.setEnabled(False)
        self.pushButton_Dec9.setEnabled(False)
        self.pushButton_DecDot.setEnabled(False)
        self.pushButton_DecAC.setEnabled(False)
        self.pushButton_DecOK.setEnabled(False)
        self.lineEdit_Dec.clear()
        self.lineEdit_Doz.clear()
        self.pushButton_DozO.setEnabled(True)
        self.pushButton_DozA.setEnabled(True)
        self.pushButton_DozB.setEnabled(True)
        self.pushButton_DozC.setEnabled(True)
        self.pushButton_DozD.setEnabled(True)
        self.pushButton_DozE.setEnabled(True)
        self.pushButton_DozF.setEnabled(True)
        self.pushButton_DozG.setEnabled(True)
        self.pushButton_DozH.setEnabled(True)
        self.pushButton_DozI.setEnabled(True)
        self.pushButton_DozK.setEnabled(True)
        self.pushButton_DozL.setEnabled(True)
        self.pushButton_DozDot.setEnabled(True)
        self.pushButton_DozAC.setEnabled(True)
        self.pushButton_DozOK.setEnabled(True)
    def RBDec(self):
        self.pushButton_DozO.setEnabled(False)
        self.pushButton_DozA.setEnabled(False)
        self.pushButton_DozB.setEnabled(False)
        self.pushButton_DozC.setEnabled(False)
        self.pushButton_DozD.setEnabled(False)
        self.pushButton_DozE.setEnabled(False)
        self.pushButton_DozF.setEnabled(False)
        self.pushButton_DozG.setEnabled(False)
        self.pushButton_DozH.setEnabled(False)
        self.pushButton_DozI.setEnabled(False)
        self.pushButton_DozK.setEnabled(False)
        self.pushButton_DozL.setEnabled(False)
        self.pushButton_DozDot.setEnabled(False)
        self.pushButton_DozAC.setEnabled(False)
        self.pushButton_DozOK.setEnabled(False)
        self.lineEdit_Doz.clear()
        self.lineEdit_Dec.clear()
        self.pushButton_Dec0.setEnabled(True)
        self.pushButton_Dec1.setEnabled(True)
        self.pushButton_Dec2.setEnabled(True)
        self.pushButton_Dec3.setEnabled(True)
        self.pushButton_Dec4.setEnabled(True)
        self.pushButton_Dec5.setEnabled(True)
        self.pushButton_Dec6.setEnabled(True)
        self.pushButton_Dec7.setEnabled(True)
        self.pushButton_Dec8.setEnabled(True)
        self.pushButton_Dec9.setEnabled(True)
        self.pushButton_DecDot.setEnabled(True)
        self.pushButton_DecAC.setEnabled(True)
        self.pushButton_DecOK.setEnabled(True)
    
    #UI
    def connector(self):
        #Menu
        self.menuCalculator.addAction("Basic").triggered.connect(self.BCDoz)
        self.menuCalculator.addAction("Scientific").triggered.connect(self.SCDoz)
        self.menuConverter.addAction("Dozenal/Decimal").triggered.connect(self.ConvDozDec)
        #Basic Calculator
        self.pushButton_BC0.clicked.connect(self.BC0)
        self.pushButton_BC1.clicked.connect(self.BC1)
        self.pushButton_BC2.clicked.connect(self.BC2)
        self.pushButton_BC3.clicked.connect(self.BC3)
        self.pushButton_BC4.clicked.connect(self.BC4)
        self.pushButton_BC5.clicked.connect(self.BC5)
        self.pushButton_BC6.clicked.connect(self.BC6)
        self.pushButton_BC7.clicked.connect(self.BC7)
        self.pushButton_BC8.clicked.connect(self.BC8)
        self.pushButton_BC9.clicked.connect(self.BC9)
        self.pushButton_BC10.clicked.connect(self.BC10)
        self.pushButton_BC11.clicked.connect(self.BC11)
        self.pushButton_BCadd.clicked.connect(self.BCadd)
        self.pushButton_BCsub.clicked.connect(self.BCsub)
        self.pushButton_BCmul.clicked.connect(self.BCmul)
        self.pushButton_BCdiv.clicked.connect(self.BCdiv)
        self.pushButton_BCdot.clicked.connect(self.BCdot)
        self.pushButton_BCback.clicked.connect(self.BCBack)
        self.pushButton_BCAC.clicked.connect(self.BCAC)
        self.pushButton_BCeql.clicked.connect(self.BCeql)
        #Scientific Calculator
        self.pushButton_SC0.clicked.connect(self.SC0)
        self.pushButton_SC1.clicked.connect(self.SC1)
        self.pushButton_SC2.clicked.connect(self.SC2)
        self.pushButton_SC3.clicked.connect(self.SC3)
        self.pushButton_SC4.clicked.connect(self.SC4)
        self.pushButton_SC5.clicked.connect(self.SC5)
        self.pushButton_SC6.clicked.connect(self.SC6)
        self.pushButton_SC7.clicked.connect(self.SC7)
        self.pushButton_SC8.clicked.connect(self.SC8)
        self.pushButton_SC9.clicked.connect(self.SC9)
        self.pushButton_SC10.clicked.connect(self.SC10)
        self.pushButton_SC11.clicked.connect(self.SC11)
        self.pushButton_SCe.clicked.connect(self.SCe)
        self.pushButton_SCpi.clicked.connect(self.SCpi)
        self.pushButton_SCAns.clicked.connect(self.SCAns)
        self.pushButton_SCM.clicked.connect(self.SCM)
        self.pushButton_SCtoM.clicked.connect(self.SCtoM)
        self.pushButton_SCadd.clicked.connect(self.SCadd)
        self.pushButton_SCsub.clicked.connect(self.SCsub)
        self.pushButton_SCmul.clicked.connect(self.SCmul)
        self.pushButton_SCdiv.clicked.connect(self.SCdiv)
        self.pushButton_SCdot.clicked.connect(self.SCdot)
        self.pushButton_SCback.clicked.connect(self.SCBack)
        self.pushButton_SCAC.clicked.connect(self.SCAC)
        self.pushButton_SCeql.clicked.connect(self.SCeql)
        self.pushButton_SCpow.clicked.connect(self.SCpow)
        self.pushButton_SCrt.clicked.connect(self.SCrt)
        self.pushButton_SClog.clicked.connect(self.SClog)
        self.pushButton_SCP12.clicked.connect(self.SCP12)
        self.pushButton_SCmin.clicked.connect(self.SCmin)
        self.pushButton_SCinv.clicked.connect(self.SCinv)
        self.pushButton_SCfct.clicked.connect(self.SCfct)
        self.pushButton_SCexp.clicked.connect(self.SCexp)
        self.pushButton_SCsin.clicked.connect(self.SCsin)
        self.pushButton_SCcos.clicked.connect(self.SCcos)
        self.pushButton_SCtan.clicked.connect(self.SCtan)
        self.pushButton_SCsq.clicked.connect(self.SCsq)
        self.pushButton_SCcb.clicked.connect(self.SCcb)
        self.pushButton_SCln.clicked.connect(self.SCln)
        self.pushButton_SCasin.clicked.connect(self.SCasin)
        self.pushButton_SCacos.clicked.connect(self.SCacos)
        self.pushButton_SCatan.clicked.connect(self.SCatan)
        self.pushButton_SCsqrt.clicked.connect(self.SCsqrt)
        self.pushButton_SCcbrt.clicked.connect(self.SCcbrt)
        self.pushButton_SClg.clicked.connect(self.SClg)
        self.pushButton_SCRad.clicked.connect(self.SCRad)
        self.pushButton_SCDec.clicked.connect(self.SCDec)
        #Converter
        self.pushButton_Dec0.clicked.connect(self.CDDec0)
        self.pushButton_Dec1.clicked.connect(self.CDDec1)
        self.pushButton_Dec2.clicked.connect(self.CDDec2)
        self.pushButton_Dec3.clicked.connect(self.CDDec3)
        self.pushButton_Dec4.clicked.connect(self.CDDec4)
        self.pushButton_Dec5.clicked.connect(self.CDDec5)
        self.pushButton_Dec6.clicked.connect(self.CDDec6)
        self.pushButton_Dec7.clicked.connect(self.CDDec7)
        self.pushButton_Dec8.clicked.connect(self.CDDec8)
        self.pushButton_Dec9.clicked.connect(self.CDDec9)
        self.pushButton_DecDot.clicked.connect(self.CDDecDot)
        self.pushButton_DecAC.clicked.connect(self.CDDecAC)
        self.pushButton_DecOK.clicked.connect(self.CDDecOK)
        self.pushButton_DozO.clicked.connect(self.CDDozO)
        self.pushButton_DozA.clicked.connect(self.CDDozA)
        self.pushButton_DozB.clicked.connect(self.CDDozB)
        self.pushButton_DozC.clicked.connect(self.CDDozC)
        self.pushButton_DozD.clicked.connect(self.CDDozD)
        self.pushButton_DozE.clicked.connect(self.CDDozE)
        self.pushButton_DozF.clicked.connect(self.CDDozF)
        self.pushButton_DozG.clicked.connect(self.CDDozG)
        self.pushButton_DozH.clicked.connect(self.CDDozH)
        self.pushButton_DozI.clicked.connect(self.CDDozI)
        self.pushButton_DozK.clicked.connect(self.CDDozK)
        self.pushButton_DozL.clicked.connect(self.CDDozL)
        self.pushButton_DozDot.clicked.connect(self.CDDozDot)
        self.pushButton_DozAC.clicked.connect(self.CDDozAC)
        self.pushButton_DozOK.clicked.connect(self.CDDozOK)
        self.radioButton_Dec.clicked.connect(self.RBDec)
        self.radioButton_Doz.clicked.connect(self.RBDoz)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Ca=Calculator()
    sys.exit(app.exec_())
