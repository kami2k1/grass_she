
import threading, data
import asyncio
import random , time
from concurrent.futures import ThreadPoolExecutor, TimeoutError , as_completed
id = 0


class Kami:
    def __init__(self, key, socketio , adminrun : bool = False) -> None:
        self.adminrun = adminrun
        self.proxy = []
        self.key = key
        self.socketio = socketio
        self.listhread = {}
        self.let = 0
       
        self.atc = 0
        self.all = 0 
        self.loc = []
        self.up =  self.ctreasub()
        # self.loop = threading.Thread(target=self.update).start()
    
              
    def ctreasub(self):
        # Tạo ThreadPoolExecutor với số worker lớn
        executor = ThreadPoolExecutor(max_workers=99999)
        return executor

         
    # def update(self):
    #   try: 
    #     with ThreadPoolExecutor(max_workers=99999) as executor:
         
    #           while True:
    #                if self.loc:
    #                     # print("new proxy ")
    #                     proxy = self.loc[0]
    #                     import Main
    #                     self.loc.remove(proxy)

    #                     executor.submit(Main.CT2, proxy, self, data.id, self.key)
                        
                       
    #                     self.atc +=1
    #   except Exception as e :
    #        print("loi tai ",e)
    #        self.send(f"loi tai ham update len he admin de fixc chi tiet \n {e}")
     

         
    def addproxy(self, proxy):


        
        if proxy not in self.proxy:
            ""
            self.atc +=1
            #print("class add proxy")
            if self.up._shutdown:
                 self.up = self.ctreasub()
            self.all +=1
            self.proxy.append(proxy)
            
            
            
            # t1 =
            # t1.start()
            data.id +=1
            import Main
            self.up.submit(Main.CT2, proxy, self, data.id, self.key)
                      
                 
    #                     #threading.Thread(target=Main.CT2, args=(proxy, self, data.id, self.key)).start()
           
            # import Main
            # t2 = threading.Thread(target=))
            # t2.start()

            
           
            data.savefile("proxy_log9.txt", proxy)
            # if proxy not in self.listhread:
            #     self.listhread[proxy] = []

            # self.listhread[proxy].append(t1)

            # return {"code": 0}

    def send(self, msg):
        if self.adminrun:
             print(f"admin : {self.key}  --> {msg}  :{self.atc}")
             return
        try:
            if self.key in data.clinet:
                items = data.clinet[self.key]
                for id in items:
                    thread = self.atc
                    # try:
                    #         if id not in self.socketio.server.eio.sockets:
                    #              data.clinet[self.key].remove(id)
                    #              continue
                    # except:
                    #      print("lỗi Tại Hàm Send")

                    User = len(data.clinet)
                    Th = len(threading.enumerate())
                    #self.socketio.emit("kami", {"code": 1, "User": User, "th": Th})
                    self.socketio.emit("receive_log", {"msg": msg, "thread": thread , "all":self.all }, to=id)
        except:
             print("loio send ")
                # break
    # def checkproxy(self):
        
    #     with ThreadPoolExecutor(max_workers=500) as executor:
    #         futures = []
    #         while True:
    #             import Main
    #             if self.proxyoid and len(futures) <=500:
    #                 proxy = self.proxyoid[0]
    #                 self.proxyoid.remove(proxy)
    #                 data.id += 1
    #                 self.pro[proxy] = True
    #                 future = executor.submit(Main.CT2, proxy, self, data.id, self.key)
                    
    #                 self.atc += 1  
    #                 #time.sleep(5)
    #                 if future.done():
    #                      self.atc -= 1
    #                      continue
    #                 else:
    #                     for futurez in futures:
    #                         if futurez.done():
    #                             self.atc -= 1 

    #                             futures.remove(futurez)
    #                     futures.append(future)
    #                     p = random.randint(10,25)
    #                 self.atc = len(futures)
    #                     #time.sleep(p)
    #             else:
    #                 for futurez in futures:
    #                         if futurez.done():
                               

    #                             futures.remove(futurez)
    #                 self.atc = len(futures)
    #                 time.sleep(5)
                    
                
                

                

               
         