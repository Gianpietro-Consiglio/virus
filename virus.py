import os
import pyscreenshot
import webbrowser as wb

cont = 0
while True:
    cont += 1
    try:
        #os.mkdir(f"C:\\arquivo{cont}")
        #os.chdir(f"C:\\arquivo{cont}")
        print(f"Processo -> {cont}")
              
    except:
        pass
    
    else:
        wb.open('https://baidu-antivirus.br.uptodown.com/windows/download')
        #image = pyscreenshot.grab(bbox=(10, 10, 50, 50))
        #image.show()
        continue
    