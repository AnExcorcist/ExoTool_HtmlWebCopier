import webbrowser, requests, os, pystyle
from pystyle import *


def cls():
  os.system('cls' if os.name == 'nt' else 'clear')


banner = r"""███████╗██╗  ██╗ ██████╗     ██╗████████╗ ██████╗  ██████╗ ██╗     
██╔════╝╚██╗██╔╝██╔═══██╗   ██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     
█████╗   ╚███╔╝ ██║   ██║  ██╔╝    ██║   ██║   ██║██║   ██║██║     
██╔══╝   ██╔██╗ ██║   ██║ ██╔╝     ██║   ██║   ██║██║   ██║██║     
███████╗██╔╝ ██╗╚██████╔╝██╔╝      ██║   ╚██████╔╝╚██████╔╝███████╗
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                   """

def urlmake():
  cls()
  print(Colorate.Horizontal(Colors.rainbow, banner))

  Site = Write.Input("Enter Website Link: ", Colors.rainbow, interval=0.030)

  with open('Copied.html', "w+") as file:
    try:
      r = requests.get(Site)
    except:
      Colorate.Horizontal(Colors.rainbow, "Bad Url!")
    try:
      file.write(r.text)
    except:
      print(Colorate.Horizontal(Colors.rainbow, "Error using {}".format(Site)))

  url = 'file:///' + os.getcwd() + '/' + 'Copied.html'
  webbrowser.open(url, new=2)  # open in new tab

while(True):
  urlmake()
