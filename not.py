import Kcl
import threading
import sys , asyncio
if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

class Userkami:
        def __init__(self, id ):
                
                self.kami = Kcl.Kami(id,None,True)
        def login(self, proxy):
                
                for i in proxy:
                       self.kami.addproxy(i)

def split_list(input_list, chunk_size=20000):
    return [input_list[i:i + chunk_size] for i in range(0, len(input_list), chunk_size)] 
k ='''
proxy :
if type http
http://ip:port or http://user:password@ip:port
type socks5:
socks5:// .... 


'''
print(k)
file = input("Nhập tiên file proxy :")
iduser = input("iduser : ")
try:
    with open(file, 'r',encoding='utf-8') as file:
        proxies = file.readlines()
except:
      print("lỗi mở file không có file sai tiên file")
      sys.exit(0)
proxies = [proxy.strip() for proxy in proxies]   
proxies = split_list(proxies)
kami = Userkami(iduser)
for i in proxies:
      threading.Thread(target=kami.login(i,))
# kami.login(proxies)
              
