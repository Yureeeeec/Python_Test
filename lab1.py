class Dict1:
    def __init__(self, too):
        self.too = too

    def concat(self):
        result = ""
        for key in self.too:
            result = result + str(self.too[key])
        return result
    
    def sum(self, keys):
        total = 0
        for key in keys:
            if key in self.too:
                total = total + self.too[key]
            else:
                total = total + 0
        return total
    
    def sum2(self, key1, key2):
        value1 = self.too[key1] if key1 in self.too else []
        value2 = self.too[key2] if key2 in self.too else []
        return sum(value1) + sum(value2)
    
dict1 = Dict1({"a": 22, "b": 44, "c": 66})
dict2 = Dict1({"x": 10, "y": 20.50, "z": 30.70})
dict3 = Dict1({"apple": 5, "banana": 10, "cherry": 15})

result1 = dict1.concat()
result2 = dict2.sum(["y", "z"])
result3 = dict3.concat()

print(result1)
print(result2)
print(result3)
