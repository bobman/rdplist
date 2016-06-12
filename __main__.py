from tkinter import *
from tkinter import ttk
from rdplist import RDPList
from functools import partial

class App:

  def __init__(self, master):
    self.frame = ttk.Frame(master)
    self.frame.grid()
    ttk.Style().configure("TFrame", background="#ccc")
    ttk.Style().configure("TLabel", background="#ccc", foreground="#000")
    ttk.Style().configure("TButton", padding=6, relief="raised", background="#ccc", foreground="#000")
    self.rdp = RDPList()
    self.make_buttons()

  def make_buttons(self):
    col_count=0
    for myList in self.rdp.get_lists():
      label = ttk.Label(self.frame,text=myList['listname'])
      label.grid(column=col_count,row=0)
      row_count=1
      for myTarget in myList['targets']:
        #print(myList)
        button = ttk.Button(self.frame, text=myTarget['name'], command=partial(self.start_rdp,myTarget), width=12)
        button.grid(column=col_count,row=row_count)
        row_count=row_count+1
      col_count=col_count+1

  def start_rdp(self,target):
    self.rdp.start_rdp(target)

def main():
  root = Tk()
  app = App(root)
  root.title("RDPList")
  root.mainloop()
  
if __name__ == '__main__':
  main()
