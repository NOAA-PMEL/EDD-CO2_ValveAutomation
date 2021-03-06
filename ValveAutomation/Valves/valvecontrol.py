# -*- coding: utf-8 -*-

import sys
import valve
import syscontrol
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
import datetime as dt
import time
import csv
import pandas as pd
import os
GREEN_LED = 'if_Green Ball_38793.png'
RED_LED = 'if_Red Ball_38831.png'

SAVEFILE = 'referencegases.csv'

#fields = ['Ref1','Ref2','Ref3','Ref4','Ref5','Ref6','Ref7','Ref8']
dfields = {'Ref1':[],'Ref2':[],'Ref3':[],'Ref4':[],'Ref5':[],'Ref6':[],'Ref7':[],'Ref8':[]}
           


class ValveApp(QtWidgets.QMainWindow, valve.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        
        ## Set up variables
        self.numCycles = 0
        self.skipGas = [False]*8
        self.status = [False]*9
        self.progress = [0.0]*8
        self.timeRemaining = [0]*8
        self.flowTime = dt.timedelta()
        self.dwellTime = dt.timedelta()
        self.startTime = dt.datetime.utcnow()
        self.endTime = dt.datetime.utcnow()
        self.closeTime = dt.timedelta()
        self.override = False
        self.valveRunTime = 0
        self.fileopen = False
        self._end_program=False
        
        self.valvestate = [False]*8  ## False = Close, True = Open
        self.flowIdx = False
        
        
        ## Setup the User Interface
        self.setupUi(self)  
        
        ## Connect the start button
        self.startButton.clicked.connect(self._start)
        self.stopButton.clicked.connect(self._stop)
        ## Connect the vent button
        self.ventButton.pressed.connect(self._open_vent)
        self.ventButton.released.connect(self._close_vent)
        
        ## Connect the save reference button
        self.refButton.clicked.connect(self._save_refs)
        
        ## Clear the progress
        self._set_progress()
        
        ## Clear the remaining time 
        self._set_timeremaining()
        
        ## Set the valve index to invalid number
        self._valveIndex = -1

        ## Setup a timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._timerEvent)
        
        ## Load reference gas values and populate form (if available)
        try:
            df = pd.read_csv(SAVEFILE)
            for i in range(1,9):
                print(df['Ref{}'.format(str(i))])
                
            self.ref1.setText(str(df['Ref{}'.format(str(1))][0]))
            self.ref2.setText(str(df['Ref{}'.format(str(2))][0]))
            self.ref3.setText(str(df['Ref{}'.format(str(3))][0]))
            self.ref4.setText(str(df['Ref{}'.format(str(4))][0]))
            self.ref5.setText(str(df['Ref{}'.format(str(5))][0]))
            self.ref6.setText(str(df['Ref{}'.format(str(6))][0]))
            self.ref7.setText(str(df['Ref{}'.format(str(7))][0]))
            self.ref8.setText(str(df['Ref{}'.format(str(8))][0]))
        except:
            print("No saved file")
        
        
        
    def _start(self):
        print("Start")
        
        ## Determine if we are skipping any valves
        self.skipGas = [self.skip1.isChecked(),self.skip2.isChecked(),
                        self.skip3.isChecked(),self.skip4.isChecked(),
                        self.skip5.isChecked(),self.skip6.isChecked(),
                        self.skip7.isChecked(),self.skip8.isChecked()]
        
        ## Save all of the current input settings
        self.numCycles = self.CycleBox.value()
        self.override = self.checkBox.checkState()
        self.startTime = dt.datetime.utcnow()
        self.startTime = self.startTime.replace(microsecond=0)

       
        ## Capture Flow and Dwell Time.  
        self.flowTime = dt.timedelta(hours = self.flowTimeBox.time().hour(),
                                     minutes = self.flowTimeBox.time().minute(),
                                     seconds = self.flowTimeBox.time().second())
        self.dwellTime = dt.timedelta(hours = self.dwellTimeBox.time().hour(),
                                      minutes = self.dwellTimeBox.time().minute(),
                                      seconds = self.dwellTimeBox.time().second())
        
        ## Calculate the Total Run Time
        self.valveRunTime = self.flowTime + self.dwellTime
        
        ## Determine the valves to skip
        for i in range(len(self.skipGas)):
            if(self.skipGas[i] == False):
                self.timeRemaining[i] = self.valveRunTime.total_seconds() 
            else:
                self.timeRemaining[i] = 0
        
        ## Set the LCD values
        self._set_timeremaining()
        
        ## Setup the offset and calculate the ESTIMATED completion time 
        offsetSeconds = dt.timedelta()
        for i in range(len(self.timeRemaining)):
            offsetSeconds += dt.timedelta(seconds =self.timeRemaining[i])
        self.endTime = (self.startTime + (self.numCycles*offsetSeconds))
        
        ## Get Close Time (VALVE 9)
        self.closeTime = dt.timedelta(hours = self.closeTimeBox.time().hour(),
                                     minutes = self.closeTimeBox.time().minute(),
                                     seconds = self.closeTimeBox.time().second())
        self.exhaustCloseTime = self.valveRunTime.total_seconds() - self.closeTime.total_seconds()
        if(self.exhaustCloseTime < 0):
            self.exhaustCloseTime = 0
            
        ## Check the override
        self.override = self.checkBox.isChecked()
        
        
        ## Update the start and complete time fields
        self.startTimeBox.setText(str(self.startTime))
        self.endTimeBox.setText(str(self.endTime))
        print("Estimated completion time: " + str(self.endTime))
        
        ## Create a file with output

        ## Lock the fields
        
        for i in range(len(self.status)):
            syscontrol.CloseValve(i)
            self._set_status(i, False)
        
        
        
       
        ## Enter the run phase
        self._run()

        
        ## Unlock the fields
        
        ## Finish run
        self.endTimeBox.setText("COMPLETE")
        self._close_file()
        print("Complete Run")
        
    def _stop(self):
        
        self._end_program=True
        
        
    def _set_start_condition(self):
        pass
        
    def _run(self):
        print("run")
        self._end_program=False
        for t in range(self.numCycles):
            for i in range(8):
                self.progress[i] = 0
                if(self.skipGas[i]==True):
                    self.timeRemaining[i] = 0
                else:
                    self.timeRemaining[i] = self.valveRunTime.total_seconds()
                
            for i in range(8):
              
                self._valveIndex = i
                self.valveCompleteFlag = False
                if(self.skipGas[i]==False):
                    if(self.status[8]==False):
                        if(self.closeTime.total_seconds()>0):
                            syscontrol.OpenValve(8)
                            self._set_status(8,True)
                    syscontrol.OpenValve(i)
                    self.flowIdx = i
                    text = self._create_file_text()
                    self._write_to_file(text)
                    self.timer.start(1000)
                    self._set_status(i,True)
                    
                    while(self.valveCompleteFlag == False):
                        QtCore.QCoreApplication.processEvents()
                        if(self._end_program==True):
                            self.timer.stop()
                            return
                        time.sleep(0.25)
                    self.timer.stop()
        self._valveIndex = -1
        
    def _set_progress(self):
        self.progress1.setValue(self.progress[0])
        self.progress2.setValue(self.progress[1])
        self.progress3.setValue(self.progress[2])
        self.progress4.setValue(self.progress[3])
        self.progress5.setValue(self.progress[4])
        self.progress6.setValue(self.progress[5])
        self.progress7.setValue(self.progress[6])
        self.progress8.setValue(self.progress[7])
        QtCore.QCoreApplication.processEvents()
    def _set_timeremaining(self):
        self.lcd1.display(self.timeRemaining[0])
        self.lcd2.display(self.timeRemaining[1])
        self.lcd3.display(self.timeRemaining[2])
        self.lcd4.display(self.timeRemaining[3])
        self.lcd5.display(self.timeRemaining[4])
        self.lcd6.display(self.timeRemaining[5])
        self.lcd7.display(self.timeRemaining[6])
        self.lcd8.display(self.timeRemaining[7])
        self.show()
        QtCore.QCoreApplication.processEvents()
    def _set_status(self,valve,value = False):
        if value == True:
            led = GREEN_LED
            self.status[valve]=value
        else:
            led = RED_LED
            self.status[valve]=value
            
        if(valve == 0):
            self.status1.setPixmap(QtGui.QPixmap(led))
        elif(valve == 1):
            self.status2.setPixmap(QtGui.QPixmap(led))
        elif(valve == 2):
            self.status3.setPixmap(QtGui.QPixmap(led))
        elif(valve == 3):
            self.status4.setPixmap(QtGui.QPixmap(led))
        elif(valve == 4):
            self.status5.setPixmap(QtGui.QPixmap(led))
        elif(valve == 5):
            self.status6.setPixmap(QtGui.QPixmap(led))
        elif(valve == 6):
            self.status7.setPixmap(QtGui.QPixmap(led))
        elif(valve == 7):
            self.status8.setPixmap(QtGui.QPixmap(led))
        elif(valve == 8):
            self.status9.setPixmap(QtGui.QPixmap(led))
        QtCore.QCoreApplication.processEvents()
    def _timerEvent(self):
        if(self._valveIndex >= 0):
            self.timeRemaining[self._valveIndex] -= 1
            self._set_timeremaining()
            self.progress[self._valveIndex] = ((self.valveRunTime.total_seconds() - self.timeRemaining[self._valveIndex])/self.valveRunTime.total_seconds())*100
            self._set_progress()
            if(self.override == False):
                if(self.timeRemaining[self._valveIndex] <= self.exhaustCloseTime):
                    if(self.status[8]==True):
                        syscontrol.CloseValve(8)   
                        self._set_status(8,False)
                        
            if(self.timeRemaining[self._valveIndex] <= self.dwellTime.total_seconds()):
                if(self.status[self._valveIndex]==True):
                    syscontrol.CloseValve(self._valveIndex) 
                    self.valvestate[self._valveIndex] = True
                    self._set_status(self._valveIndex,False)
                else:
                    self.valvestate[self._valveIndex] = True
                
            if(self.timeRemaining[self._valveIndex]==0):
                self.valveCompleteFlag = True
            
            
            
            ## Connect the start button
            self.startButton.clicked.connect(self._stop)
            
            return 
        
    def _create_file_text(self):
        timestamp = time.strftime('%Y/%m/%d %H:%M:%S')
        
        ## Add User Input Serial Number 
        sernum = self.serNumText.toPlainText()
       
        gas = 'Gas#' + str(self.flowIdx+1)
        if self.flowIdx == 0:
            ppm = self.ref1.toPlainText()
        elif self.flowIdx == 1:
            ppm = self.ref2.toPlainText()
        elif self.flowIdx == 2:
            ppm = self.ref3.toPlainText()
        elif self.flowIdx == 3:
            ppm = self.ref4.toPlainText()
        elif self.flowIdx == 4:
            ppm = self.ref5.toPlainText()
        elif self.flowIdx == 5:
            ppm = self.ref6.toPlainText()
        elif self.flowIdx == 6:
            ppm = self.ref7.toPlainText()
        elif self.flowIdx == 7:
            ppm = self.ref8.toPlainText()
        
        ppm = gas + '/' + ppm + 'ppm'
                
                
    
        if(self.valvestate[self.flowIdx] == True):
            state = 'F'
        else:
            state = 'D'
            
    
            
        sendline = timestamp + ',' + sernum + ',' + ppm + ',' + state + '\n'
#        sendline = timestamp + ',' + serialnum + ',' + ppm + ',' + state
        
        
        return sendline
        
                
    def _create_file(self):
        
        filename = 'logfile_' + time.strftime('%Y%m%d_%H%M%S',time.localtime())+'.txt'
        
#        self.serNumText.setText(filename)
        self.filenameLabel.setText(filename)
        try:
            os.mkdir('Logs')
            
        except:
            #print('Path exists')
            pass
            
        try:
            path = os.path.join(os.getcwd(),'Logs')
            filename = os.path.join(path,filename)
            self.file = open(filename,"w+")
            self.fileopen = True
            
            self.file.write('Timestamp, Serial Number, Gas3/ppm, State\n')
        except:
            print("Failed to create/open log file")
            self.fileopen = False
            
            
    def _write_to_file(self,line):
        if(self.fileopen == False):
            self._create_file()
        
        print(line)
        self.file.write(line)
        
        
    def _close_file(self):
        self.file.close()
        self.fileopen = False

    def _open_vent(self):
        syscontrol.OpenValve(8)   
        self._set_status(8,True)
        QtCore.QCoreApplication.processEvents()
    def _close_vent(self):
        syscontrol.CloseValve(8)   
        self._set_status(8,False)
        QtCore.QCoreApplication.processEvents()
    
    def _save_refs(self):
        print("Save Refs")
#        values = {'Ref1':self.ref1.toPlainText(),'Ref2':self.ref2.toPlainText(),
#                  'Ref3':self.ref3.toPlainText(),'Ref4':self.ref4.toPlainText(),
#                  'Ref5':self.ref5.toPlainText(),'Ref6':self.ref6.toPlainText(),
#                  'Ref7':self.ref7.toPlainText(),'Ref8':self.ref8.toPlainText()}
        values = [self.ref1.toPlainText(),self.ref2.toPlainText(),
                  self.ref3.toPlainText(),self.ref4.toPlainText(),
                  self.ref5.toPlainText(),self.ref6.toPlainText(),
                  self.ref7.toPlainText(),self.ref8.toPlainText()]

        df = pd.DataFrame(columns=('Ref1','Ref2','Ref3','Ref4','Ref5','Ref6','Ref7','Ref8'))
#        df2 = pd.DataFrame(values)
        df.loc[1] = values
        df.to_csv(SAVEFILE)
        
def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = ValveApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    sys.exit(app.exec_())                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
    
    print("Done")
