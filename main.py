class ElementDataList:
    def __init__(self, data_list = None):
        self.data_list = data_list if data_list != None else []
        if not isinstance(self.data_list, list):
            raise ValueError("The data_list must be list")
        if any(not isinstance(i, int) for i in self.data_list):
            raise ValueError("The elements in data_list must be of type int")
        
    def get(self, index = None):
        index = len(self.data_list) - 1 if index is None else index
        if not isinstance(index, int):
            if index > len(self.data_list) or index < 0:
                return None
            raise ValueError("Incorrect index value")
        return self.data_list[index]
    
    def append(self, value):
        self.data_list = ElementDataList(self.data_list + [value]).data_list
        
    def pop(self, index = None):
        index = len(self.data_list) - 1 if index is None else index
        if index > len(self.data_list) or index < 0 or not isinstance(index, int):
            raise ValueError("Incorrect index value")
        element = self.data_list[index]
        self.data_list = ElementDataList(self.data_list[:index] + self.data_list[index + 1:]).data_list
        return[element]
        
    def __repr__(self):
        return f"data_list = {self.data_list}"
        
class ElementDataMap:
    def __init__(self, data_map = None):
        self.data_map = data_map if data_map != None else {}
        if not isinstance(self.data_map, dict):
            raise ValueError("The data_map must be dict")
        if any(not isinstance(i, str) or not isinstance(self.data_map[i], int) for i in self.data_map):
            raise ValueError("The keys in data_map must be of type str and the elements in data_map must be of type int")
        
    def get(self, key):
        if not isinstance(key, str):
            raise ValueError("Incorrect key value")
        if key not in self.data_map:
            return None
        return self.data_map[key]
        
    def __repr__(self):
        return f"data_map = {self.data_map}"

class Element:
    def __init__(self, value, /, data_list = None, data_map = None):
        if not isinstance(value, int):
            raise ValueError("The value must be int")
        self.__value = value
        
        self.__data_list = ElementDataList(data_list)
        self.__data_map = ElementDataMap(data_map)
         
    @property
    def value(self):
        "Private variable. Only read-only access is possible"
        return self.__value
    
    @property
    def data_list(self):
        "Private variable. Only read-only access is possible"
        return self.__data_list 
    
    @property
    def data_map(self):
        "Private variable. Only read-only access is possible"
        return self.__data_map
    
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, int):
            raise ValueError("The value must be int")
        self.__value = new_value
        
    @data_list.setter
    def data_list(self, new_data_list):
        self.__data_list = ElementDataList(new_data_list)
        
    @data_map.setter
    def data_map(self, new_data_map):
        self.__data_map = ElementDataMap(new_data_map)
        
    @value.deleter
    def value(self):
        del self.__value
        
    @data_list.deleter
    def data_list(self):
        del self.__data_list
    
    @data_map.deleter
    def data_map(self):
        del self.__data_map
    
    
    def __repr__(self):
        return f"Element(value = {self.value}, {self.data_list}, {self.data_map})"


        
a = Element(5)
print(a)
print(a.value)
a.value = 3
a.data_list = [0, 1, 2, 3, 4, 5, 6]
print(a)
a.data_list.append(7)
print(a)
a.data_list.pop()
print(a)
