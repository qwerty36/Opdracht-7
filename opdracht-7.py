import re
from tkinter import *

def main():
    mus = zincfingerfinder()

class zincfingerfinder:    
    def __init__(self):
        self.getdata()
     
    def getdata(self):      
        from tkinter import filedialog
        niets=Tk()
        self.file = filedialog.askopenfile()
        niets.destroy()
        niets.mainloop()        
        self.data, self.hdata, self.sdata, raw_data = '', '', '', ''
        for line in self.file:
            if '>' in line:
                self.data += '\n' + line
                self.hdata += line
                self.sdata += '\n'
                pass
            else:
                raw_data += line          
                seq = raw_data.replace(' ','').replace('\n','').replace('\r','')
                self.data += seq
                self.sdata += seq
                raw_data = ''
        self.file.close() 
        self.data = self.data[1:]
        self.formatdata()
    def zoekpatroon(self):        
        peptidedictionary, i = {}, -1    
        #pattern = re.compile('C.[DNEHQSTI]C.{4,6}[ST]..[WM][HR][RKENAMSLPGQT].{3,4}[GNEP].{3,6}C[NES][ASNR]C')
        pattern = re.compile('[AC]')        
        for item in self.slijst:
            i += 1
            if pattern.search(item):
                peptidedictionary.update({self.hlijst[i][2:12]:self.slijst[i]}) 
        print(peptidedictionary)             
    def formatdata(self):
        self.slijst, self.hlijst = [], []        
        self.slijst = self.sdata.split('\n')
        self.hlijst = self.hdata.split('\n')
        self.slijst.remove('')
        self.hlijst.remove('')
        self.zoekpatroon()

if __name__ == '__main__':
    main()         