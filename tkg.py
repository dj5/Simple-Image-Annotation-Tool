from tkinter import *
import os
from tkinter import filedialog
from csv_to_pascalvoc import csv_to_pascalvoc
class GUI:
    def __init__(self):
        self.var=None
        self.checkboxlist= list()
        self.class_name=""
        self.path=""
        self.quit=False
        self.next=False
         
         
    def add_class(self,class_name):
         if class_name!="":
            c=Radiobutton(self.window, text=class_name, variable=self.var, value=class_name)
            c.grid(row=0,column=len(self.checkboxlist), sticky=W)
            f= open(os.path.join(self.path,"class.txt"),'a')
            f.writelines(class_name)
            f.close()
         else:
             print("Class Name not found")
         
         self.checkboxlist.append(class_name)
         
    def next_fn(self):
         #print("next")
         self.selected()
         self.next=True
         self.window.destroy()
    def selected(self):
         count=0
         self.class_name=self.var.get()
    def quit_fn(self):
         self.next=True
         self.quit=True
         self.window.destroy()
    def annotate_more_class(self):
         self.selected()
         self.window.destroy()
    def select_path(self):
         self.path=filedialog.askdirectory()
         self.window.destroy()
    def csv_to_pascal(self):
         if self.path!="":
            self.selected()
            csv_to_pascalvoc(self.path)
            print("Current Data convereted to Pascal VOC format. Path {0}".format(os.path.join(self.path,"Annotations")))
    def gui(self):
         self.window=Tk()
         self.window.wm_title("Image Annotation Tool")
   
         self.var= StringVar()
         e1=Entry(self.window)
         e1.grid(row=1, column=0)
         btn=[] 	 
         btn.append(Button(self.window,text="Add class",command=lambda : self.add_class(e1.get())))
         btn[0].grid(row=1,column=1)
      
         btn.append(Button(self.window,text="Next",command=self.next_fn))

         btn[1].grid(row=2,column=0)
         btn.append(Button(self.window,text="Quit",command=self.quit_fn))
         btn[2].grid(row=2,column=1)
         btn.append(Button(self.window,text="Annotate more classes",command=self.annotate_more_class))
         btn[3].grid(row=3,column=0)
        
         btn.append(Button(self.window,text="Convert CSV to Pascal Voc",command=self.csv_to_pascal))
         btn[4].grid(row=3,column=1)
         btn.append(Button(self.window,text="Select Path",command=self.select_path))
         btn[5].grid(row=4,column=0) 
         if self.path=="":
             for i in range(len(btn)-1):
                btn[i]['state']="disabled"  
         if len(self.checkboxlist)>0:
             for i in range(len(self.checkboxlist)):
                r=Radiobutton(self.window, text=self.checkboxlist[i], variable=self.var, value=self.checkboxlist[i])
                r.grid(row=0,column=i, sticky=W)
             
              
         
    
         self.window.mainloop()
