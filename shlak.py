class Element:
    def __init__(self, value, /, data_list = None, data_map = None):
        if not isinstance(value, int):
            raise ValueError("The value must be int")
        self.__value = value
        
        self.__data_list = data_list if data_list != None else []
        if not isinstance(self.__data_list, list):
            raise ValueError("The data_list must be list")
        self.__data_map = data_map if data_map != None else {}
        if not isinstance(self.__data_map, dict):
            raise ValueError("The data_map must be dict")
         
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
        if not isinstance(new_data_list, list):
            raise ValueError("The data_list must be list")
        self.__data_list = new_data_list
        
    @data_map.setter
    def data_map(self, new_data_map):
        if not isinstance(new_data_map, dict):
            raise ValueError("The data_map must be dict")
        self.__data_map = new_data_map
        
    @value.deleter
    def value(self):
        del self.__value
    
    @data_list.deleter
    def data_list(self):
        del self.__data_list
        
    @data_map.deleter
    def data_map(self):
        del self.__data_map
        
    def get(self, index):
        if index > len(self.data_list) or index < 0 or not isinstance(index, int):
            raise ValueError("Incorrect index value")
        return self.data_list[index]
    
    
    def __repr__(self):
        return f"Element(value = {self.value}, data_list = {self.data_list}, data_map = {self.data_map})"


        
a = Element(5)
print(a)
print(a.value)
a.value = 3
a.data_list = [1, 2, 3]
print
a.data_map = {1: 2}
print(a)
