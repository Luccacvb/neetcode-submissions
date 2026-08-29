class StringIterator:

    def __init__(self, compressedString: str):
        res = []
        i = 0
        n = len(compressedString)
        while i < n:
            if compressedString[i].isalpha():
                letter = compressedString[i]
                i += 1
            
                digit = ""
                while i < n and compressedString[i].isdigit():
                    digit += compressedString[i]
                    i += 1
            
            res.append((letter, int(digit)))

        self.res = res
        self.index = 0
        self.count = 0

    def next(self) -> str:        
        if self.count == 0:
            self.letter, self.total = self.res[self.index]
            self.index += 1
            self.count = self.total

        self.count -= 1
        return self.letter

    def hasNext(self) -> bool:
        if self.index < len(self.res):
            return True
        return False

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()