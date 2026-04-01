class ElementDataList:
    def __init__(self, data_list = None):
        self.data_list = data_list if data_list != None else []
        self.__checkListValues(self.data_list)
        
    def __checkListValues(self, my_list):
        if not isinstance(my_list, list):
            raise ValueError("The object must be type list")
        if any(not isinstance(i, int) for i in my_list):
            raise ValueError("The elements in list must be of type int")
        
    def get(self, index = None):
        index = len(self.data_list) - 1 if index is None else index
        if not isinstance(index, int):
            if index > len(self.data_list) or index < 0:
                return None
            raise ValueError("Incorrect index value")
        return self.data_list[index]
    
    def append(self, value):
        new_list = self.data_list + [value]
        self.data_list = ElementDataList(new_list).data_list
        
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
        self.__checkDictValues(self.data_map)
       
    def __checkDictValues(self, my_dict):
         if not isinstance(my_dict, dict):
            raise ValueError("The object must be dict")
         if any(not isinstance(i, str) or not isinstance(my_dict[i], int) for i in my_dict):
            raise ValueError("The keys in dict must be of type str and the elements in dict must be of type int")
    
    def get(self, key):
        if not isinstance(key, str):
            raise ValueError("Incorrect key value")
        if key not in self.data_map:
            return None
        return self.data_map[key]
    
    def items(self):
        list_of_items = []
        for key in self.data_map:
            list_of_items.append((key, self.data_map[key]))
        return list_of_items
    
    def values(self):
        list_of_items = []
        for key in self.data_map:
            list_of_items.append(self.data_map[key])
        return list_of_items
    
    def update(self, other_dict):
        self.__checkDictValues(other_dict)
        for key in other_dict:
            self.data_map[key] = other_dict[key]
    
        
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


        
a = Element(5, data_list=[1, 2, 3], data_map={"lol": 1, "lololo": 2, "lolo": 3})
print(a)
print(a.data_map.get("lol"))
print(a.data_map.get("lololoololo"))
print(a.data_map.items())
print(a.data_map.values())
a.data_list.pop()
a.data_map.update({"lol": 4, "lolol": 5})
print(a)
