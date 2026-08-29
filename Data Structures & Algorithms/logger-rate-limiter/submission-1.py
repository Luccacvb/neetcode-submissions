class Logger:
    def __init__(self):
        self.mapp = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mapp:
            self.mapp[message] = timestamp + 10
            return True

        if timestamp >= self.mapp[message]:
            self.mapp[message] = timestamp + 10
            return True
        
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
