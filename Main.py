import asyncio
import random
import ssl
import json
import threading
import time
import uuid


from websockets_proxy import Proxy, proxy_connect


async def ket_noi_sv(proxyvip, user_id, id, kami,reconet : int = 0 )-> None:

        
    
    device_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, proxyvip+user_id))
   
    while True:
        try:
            await asyncio.sleep(random.uniform(0.1, 1.0)) 
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            }
            ssl_context = ssl.create_default_context()
            ssl_context.check_hostname = False
            ssl_context.verify_mode = ssl.CERT_NONE
            uri = "wss://proxy2.wynd.network:4650/"

            proxy = Proxy.from_url(proxyvip)
            async with proxy_connect(uri, proxy=proxy, ssl=ssl_context, extra_headers={
                "Origin": "chrome-extension://lkbnfiajjmbhnfledhphioinpickokdi",
                "User-Agent": headers["User-Agent"] }) as websocket:
                async def ping():
                    while True:
                        send_message = json.dumps(
                            {"id": str(uuid.uuid4()), "version": "1.0.0", "action": "PING", "data": {}})
                        kami.send(f"Proxy  ->: Ping ")
                        await websocket.send(send_message)
                        await asyncio.sleep(110) 

                ping_task = asyncio.create_task(ping())
                try:
                    while True:
                        response = await websocket.recv()
                        message = json.loads(response)
                        
                        if message.get("action") == "AUTH":
                            # if kami.key != data.admin and kami.adminrun == False:      
                            auth_response = {
                                        "id": message["id"],
                                        "origin_action": "AUTH",
                                        "result": {
                                            "browser_id": device_id,
                                            "user_id": user_id,
                                            "user_agent": headers['User-Agent'],
                                            "timestamp": int(time.time()),
                                            "device_type": "extension",
                                            "version": "4.26.2",
                                            "extension_id": "lkbnfiajjmbhnfledhphioinpickokdi"
                                        }
                                    }


                           
                            await websocket.send(json.dumps(auth_response))

                        elif message.get("action") == "PONG":
                            pong_response = {"id": message["id"], "origin_action": "PONG"}
                            
                            kami.send(f"Proxy  ->: Pong ")
                            
                            # if kami.adminrun:
                            #      kami.send("ping tets admin --->")
                            await websocket.send(json.dumps(pong_response))
                except:
                     kami.send("Proxy Lỗi Mã Lỗi 506 Chi tiết Liên hệ admin nhé")
                     if 'ping_task' in locals() and not ping_task.done():
                            ping_task.cancel()
                finally:
                    if len(proxyvip) >= 5:
                        modified_url = proxyvip[:-5] + "***"
                    else:
                        modified_url = "***"
                    if 'ping_task' in locals() and not ping_task.done():
                            ping_task.cancel()
                    kami.send(f"{modified_url} ->: kiet noi lai sau 5s ")

                    await asyncio.sleep(5)
                    await ket_noi_sv(proxyvip, user_id, id, kami,reconet +1)
                    
                   

        except Exception as e:
            kami.send(f"die--> {proxyvip}")
            kami.proxy.remove(proxyvip)
            if 'ping_task' in locals() and not ping_task.done():
                    ping_task.cancel()
            kami.atc -=1
            
            return


# 160.22.174.188:16584:dien92ewgfw:giat93weg
# for i in range(1,50):
# def CTASlK(proxy, id):
#     asyncio.run(ket_noi_sv(f"http://{proxy}", "", id=id))


def CT2(proxy, Kami, id: int, userId):
    try:
            
            
            asyncio.run(ket_noi_sv(proxy, user_id=userId, id=id, kami=Kami,reconet=0))
    except Exception as e:
        ""
        print("loi chi tie ",e)
        ""
