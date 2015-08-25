'''
Created on Oct 23, 2014

@author: mrstain
'''
from PyQt4 import QtGui
import sys
from mainwindow import *
from iapws import IAPWS97
from twisted.spread.ui import tkutil
class IAPWS97Attrib:
    '''
    ['P', 'Pressure', 'MPa']
    T, Temperature, K
    g, Specific Gibbs free energy, kJ/kg
    a, Specific Helmholtz free energy, kJ/kg
    v, Specific volume, m3/kg
    rho, Density, kg/m3
    x, quality, [-]
    h, Specific enthalpy, kJ/kg
    u, Specific internal energy, kJ/kg
    s, Specific entropy, kJ/kg/K
    '''
    
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("IAPMWS97")
        self.setGeometry(200,100,820,200)
        #set T,P as default
        self.ui.la1.setText('Temperature')
        self.ui.la2.setText('Pressure')
        self.ui.la2.setToolTip('bars')
        self.ui.rbTP.setChecked(True)
        
        # Setup Functions "
        self.setupSignals()
        self.setupActions()
        self.setupMenuBar()
        self.setupVar()
        self.setupScrollArea()
        
    def setupActions(self):
        # Exit Action#
        self.exact = QtGui.QAction('Exit', self)
        self.exact.setShortcut('ctrl+Q')
        self.exact.triggered.connect(self.close)
        
        self.about = QtGui.QAction('About', self)
        self.about.triggered.connect(self.aboutfun)
        
        self.submitAct = QtGui.QAction('submit', self)
        self.submitAct.setShortcut('ENTER')
        self.submitAct.triggered.connect(self.submitFun)
        
    def setupMenuBar(self):
        self.ui.menuFile.addAction(self.exact)
        self.ui.menuHelp.addAction(self.about)
    
    def setupSignals(self):
        self.submit = self.ui.btnShow.clicked.connect(self.submitFun)

        # connect radio buttons and send whay  
        self.ui.rbTP.toggled.connect(lambda: self.radiofun('TP'))
        self.ui.rbPh.toggled.connect(lambda: self.radiofun('Ph'))
        self.ui.rbPs.toggled.connect(lambda: self.radiofun('Ps'))
        self.ui.rbhs.toggled.connect(lambda: self.radiofun('hs'))
        self.ui.rbTx.toggled.connect(lambda: self.radiofun('Tx'))
        self.ui.rbPx.toggled.connect(lambda: self.radiofun('Px'))
        
    def submitFun(self):
        self.fV = self.ui.le1.text() #frst value
        self.sV = self.ui.le2.text() # secon value
        if self.ui.le1.text() == '' or self.ui.le2.text() == '':
            QtGui.QMessageBox.about(self, 'Error','Input is empty')
            return
        try:
            #convert form string to float
            self.fV = float(self.fV) 
            self.sV = float(self.sV)
        except ValueError:
            QtGui.QMessageBox.about(self, 'Error','Input can only be a number')
            return
        try: 
            # Temperature Pressure #
            if self.ui.rbTP.isChecked():
                #first is Temp, sencond Pressure
                self.fV = self.fV + 273.15 # convert from celsius in kelvin               
                self.sV = self.sV / 10 # convert from Mpa in bar
                self.steam = IAPWS97(P=self.sV, T=self.fV)
            # Pressure h #                    
            elif self.ui.rbPh.isChecked():
                self.sV = self.sV / 10 # convert from Mpa in bar
                self.steam = IAPWS97(P=self.sV, h=self.fV)
            # Pressure s #    
            elif self.ui.rbPs.isChecked():
                self.sV = self.sV / 10 # convert from Mpa in bar
                self.steam = IAPWS97(P=self.sV, s=self.fV)
            # s h#    
            elif self.ui.rbhs.isChecked():
                self.steam = IAPWS97(h=self.sV, s=self.fV)
            # T x #    
            elif self.ui.rbTx.isChecked():
                self.fV = self.fV + 273.15
                self.steam = IAPWS97(T=self.fV, x=self.sV)
            elif self.ui.rbPx.isChecked():
                self.fV = self.fV / 10
                self.steam = IAPWS97(P=self.fV, x=self.sV)
            else:
                QtGui.QMessageBox.about(self, 'Error','Select the function of converting')
                return    
        except NotImplementedError:
                QtGui.QMessageBox.about(self, 'Error','The numbers are not in range')
                return
            
        #create table
        self.createTable()
        
    def setupScrollArea(self):
        self.w= QtGui.QWidget(self)        
        self.vbox=QtGui.QVBoxLayout(self.w)
        _l=QtGui.QHBoxLayout()
        self.allcb = QtGui.QCheckBox(self)
        self.allcb.setChecked(True)
        _l.addWidget(self.allcb)
        _l.addStretch(1)
        self.vbox.addLayout(_l)
        
 
        self.ui.scrollArea.setWidget(self.w)
 #       scrollAreaF()
        
    def scrollAreaF(self):
        self.w= QtGui.QWidget(self)        
        self.vbox=QtGui.QVBoxLayout(self.w)
        for x in self.properties:
            _l=QtGui.QHBoxLayout()
            cb = QtGui.QCheckBox(self)
            cb.setChecked(True)
            _l.addWidget(cb)
            _l.addWidget(QtGui.QLabel(self.properties[x][1], self))
            #_l.addWidget(QtGui.QComboBox(self))
            _l.addStretch(1)
            self.vbox.addLayout(_l)
 
        self.ui.scrollArea.setWidget(self.w)
        pass
    def createTable(self): # descr= Temperature, param = T
        '''create table'''    
        col = 0
        row = 0  
        tableLen = len(self.properties)
        
        #fucntions
        self.ui.tableWidget.setRowCount(tableLen)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Property','Value','Unit'])
        xy = 0
        for key in self.properties:
            if 2  == 2:
                self.ui.tableWidget.setItem(col,row, QtGui.QTableWidgetItem(self.properties[key][1]))
                try:
                    re = getattr(self.steam, key) #get steam. method from string
                except AttributeError:
                        QtGui.QMessageBox.about(self, 'Error','Propertie: '+ key + " doesen't exsist")    
                            
                self.ui.tableWidget.setItem(col, (row +1), QtGui.QTableWidgetItem(str(re)))
                self.ui.tableWidget.setItem(col, (row +2), QtGui.QTableWidgetItem(self.properties[key][2]))
                col += 1 #for table manipulation
                if col > (tableLen -1):
                    col = 0
                    if len(self.properties) > tableLen:
                        row += 3
                    else:
                        row += 1
        xy += 1                        
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.setSortingEnabled(True)
        
    def radiofun(self, par):
        if par == 'TP':
            self.ui.la1.setText('Temperature')
            self.ui.la1.setToolTip('*C')
            self.ui.la2.setText('Pressure')
            self.ui.la2.setToolTip('bars')
        elif par == 'Ph':
            self.ui.la2.setText('Pressure')
            self.ui.la1.setText('Specific enthalpy')
        elif par == 'Ps':
            self.ui.la2.setText('Pressure')
            self.ui.la1.setText('Specific entropy')
        elif par == 'hs':
            self.ui.la2.setText('Specific enthalpy')
            self.ui.la1.setText('Specific entropy')
        elif par == 'Tx':
            self.ui.la1.setText('Temperature')
            self.ui.la2.setText('Quality')
        elif par == 'Px':
            self.ui.la1.setText('Pressure')
            self.ui.la2.setText('Quality')
    def setupVar(self):
        # property = [0], name = [1], unit = [2]
        from collections import OrderedDict
        self.properties = {
               'P'    : ['P', 'Pressure', 'MPa'],
               'T'    : ['T', 'Temperature', 'K'],
               'h'    : ['h','Specific enthalpy', 'kJ/kg'],
               'g'    : ['g','Specific Gibbs free energy','kJ/kg'],
               'a'    : ['a','Specific Helmholtz free ener.','kJ/kg'],
               'v'    : ['v', 'Specific volume', 'm3/kg'],
               'rho'  : ['rho', 'Density', 'kg/m3'],
               'x'    : ['x', 'quality', '[-]'],
               'u'    : ['u', 'Specific internal energy', 'kJ/kg'],
               's'    : ['s', 'Specific entropy', 'kJ/kg.K'],
               'cp'   : ['cp', 'Specific isobaric heat capacity', 'kJ/kg.K'],
               'cv'   : ['cv', 'Specific isochoric heat capacity', 'kJ/kg.K'],
               'Z'    : ['Z', 'Compression factor.', '[-]'],
               'gamma': ['gamma', 'Isoentropic exponent', '[-]'],
               'alfav': ['alfav', 'Isobaric cubic expansion coefficient', '1/K'],
               #'kt'   : ['kt', 'Isothermal compressibility', '1/MPa' ],
               'alfap': ['alfap', 'Relative pressure coefficient', '1/K'],
                'betap' : ['betap', 'Isothermal stress coefficient', 'kg/m3' ],
                'joule' : ['joule', 'Joule-Thomson coefficient', 'K/MPa' ],
                'deltat' : ['deltat', 'Isothermal throttling coefficient', 'kJ/kg.MPa'],
                'region' :['region', 'Region', '[-]' ],
                'v0'  : ['v0', 'Ideal specific volume', 'm3/kg' ],
                'u0'  : ['u0', 'Ideal specific internal energy', 'kJ/kg'],
                'h0'  : ['h0', 'Ideal specific enthalpy', 'kJ/kg' ],
                's0'  : ['s0', 'Ideal specific entropy', 'kJ/kg.K' ],
                'a0'  : ['a0', 'Ideal specific Helmholtz free energy', 'kJ/kg' ],
                'g0'  : ['g0', 'Ideal specific Gibbs free energy', 'kJ/kg' ],
                'cp0' : ['cp0', 'Ideal specific isobaric heat capacity', 'kJ/kg.K' ],
                'cv0' :['cv0', 'Ideal specific isochoric heat capacity', 'kJ/kg.K' ],
                'w0'  : ['w0', 'Ideal speed of sound', 'm/s' ],
                'gamma0' : ['gamma0', 'Ideal isoentropic exponent', '[-]' ],
                'w'   : ['w', 'Speed of sound', 'm/s' ],
                'mu'  : ['mu', 'Dynamic viscosity', 'Pa.s' ],
                'nu'  : ['nu', 'Kinematic viscosity', 'm2/s' ],
                'k'   : ['k', 'Thermal conductivity', 'W/m.K' ],
                'alfa': ['alfa', 'Thermal diffusivity', 'm2/s' ],
                'sigma' : ['sigma', 'Surface tension', 'N/m' ],
                'epsilon' : ['epsilon', 'Dielectric constant', '[-]' ],
                'n'   : ['n', 'Refractive index', '[-]' ],
                'Prandt' : ['Prandt', 'Prandtl number', '[-]' ],
                'Tr'  : ['Tr', 'Reduced temperature', '[-]' ],
                'Pr'  : ['Pr', 'Reduced pressure', '[-]' ], 
               }
        OrderedDict(sorted(self.properties.items(), key=lambda t: t[0]))        
    def aboutfun(self):
            QtGui.QMessageBox.about(self, 'About', 'Graphic aplication for IAPMW97 \nAuthor: Matej Ferenc - MrStain [ferenc.matej@gmail.com]\nLicence: GPL2.0 Public Licence ')
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
    app.exec_loop()

    '''
        Incoming properties:

    T, Temperature, K
    P, Pressure, MPa
    

Definitions options:

    T, P (Not valid for two-phases region)
    P, h
    P, s
    h, s
    T, x (Only for two-phases region)
    P, x (Only for two-phases region)

Properties:
    


'''
'''

    P, Pressure, MPa
    T, Temperature, K
    g, Specific Gibbs free energy, kJ/kg
    a, Specific Helmholtz free energy, kJ/kg
    v, Specific volume, m3/kg
    rho, Density, kg/m3
    x, quality, [-]
    h, Specific enthalpy, kJ/kg
    u, Specific internal energy, kJ/kg
    s, Specific entropy, kJ/kg/K
    
    cp, Specific isobaric heat capacity, kJ/kg.K
    cv, Specific isochoric heat capacity, kJ/kg.K
    Z, Compression factor. [-]
    gamma, Isoentropic exponent, [-]
    alfav, Isobaric cubic expansion coefficient, 1/K
    kt, Isothermal compressibility, 1/MPa
    alfap, Relative pressure coefficient, 1/K
    betap, Isothermal stress coefficient, kg/m3
    joule, Joule-Thomson coefficient, K/MPa
    deltat, Isothermal throttling coefficient, kJ/kg.MPa
    region, Region
    v0, Ideal specific volume, m3/kg
    u0, Ideal specific internal energy, kJ/kg
    h0, Ideal specific enthalpy, kJ/kg
    s0, Ideal specific entropy, kJ/kg.K
    a0, Ideal specific Helmholtz free ener., kJ/kg
    g0, Ideal specific Gibbs free energy, kJ/kg
    cp0, Ideal specific isobaric heat capacity, kJ/kg.K
    cv0, Ideal specific isochoric heat capacity, kJ/kg.K
    w0, Ideal speed of sound, m/s
    gamma0, Ideal isoentropic exponent [-]
    w, Speed of sound, m/s
    mu, Dynamic viscosity, Pa.s
    nu, Kinematic viscosity, m2/s
    k, Thermal conductivity, W/m.K
    alfa, Thermal diffusivity, m2/s
    sigma, Surface tension, N/m
    epsilon, Dielectric constant, [-]
    n, Refractive index, [-]
    Prandt, Prandtl number, [-]
    Tr, Reduced temperature, [-]
    Pr, Reduced pressure, [-]

'''
