
class MathDojo:
    # Attributes
    def __init__(self):
        self.result = 0

    # Methods
    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n 
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n 
        return self

# Instance
md = MathDojo() 

# Test
x = md.add(2).add(2, 5, 1).subtract(3, 2).result 

# Print
print(x) 


