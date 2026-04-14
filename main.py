import json
from functools import wraps

is_authenticated = False

def check_password(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        global is_authenticated
        
        if is_authenticated:
            return func(*args, **kwargs)
        
        print("Hohohoho NO")
        user_password = input("Password please:")

        with open('password.json', 'r') as file:
            config = json.load(file)
            correct_password = config['password']
        
        if user_password == correct_password:
            is_authenticated = True
            print("Bro you ara right!\n")
            return func(*args, **kwargs)
        else:
            print("FUCKING INTRUDER GET OUT\n")
            return None
    
    return wrapper


class ElementDataList:

    def __init__(self, data_list = None):
        self.data_list = data_list if data_list != None else []
        self.__checkListValues(self.data_list)
        
    def __checkListValues(self, my_list):
        if not isinstance(my_list, list):
            raise ValueError("The object must be type list")
        if any(not isinstance(i, int) for i in my_list):
            raise ValueError("The elements in list must be of type int")
        
    @check_password    
    def get(self, index = None):
        index = len(self.data_list) - 1 if index is None else index
        if not isinstance(index, int):
            if index > len(self.data_list) or index < 0:
                return None
            raise ValueError("Incorrect index value")
        return self.data_list[index]
    @check_password 
    def append(self, value):
        new_list = self.data_list + [value]
        self.data_list = ElementDataList(new_list).data_list
        
    @check_password    
    def pop(self, index = None):
        index = len(self.data_list) - 1 if index is None else index
        if index > len(self.data_list) or index < 0 or not isinstance(index, int):
            raise ValueError("Incorrect index value")
        element = self.data_list[index]
        self.data_list = ElementDataList(self.data_list[:index] + self.data_list[index + 1:]).data_list
        return[element]
    
    def __add__(self, other):
        first_list = self.data_list if len(self.data_list) >= len(other.data_list) else other.data_list
        second_list = self.data_list if len(self.data_list) < len(other.data_list) else other.data_list
        
        for i in range(len(second_list)):
            first_list[i] += second_list[i]
            
        return ElementDataList(first_list)
    
    def __sub__(self, other):
        new_list = self.data_list.copy()
        if len(self.data_list) >= len(other.data_list):
            for i in range(len(other.data_list)):
                new_list[i] -= other.data_list[i]
        else:
            new_list += [0] * (len(other.data_list) - len(self.data_list))
            for i in range(len(other.data_list)):
                new_list[i] -= other.data_list[i]
        return ElementDataList(new_list)
    
    def __repr__(self):
        return f"data_list = {self.data_list}"
        
        
    
class ElementQueue(ElementDataList):
    
    def __init__(self, data_list=None):
        if data_list is None:
            super().__init__([])
        elif isinstance(data_list, ElementDataList):
            super().__init__(data_list.data_list.copy())
        elif isinstance(data_list, list):
            super().__init__(data_list)
        else:
            raise ValueError("Data_list must be a list or ElementDataList object")
        
    @check_password 
    def get(self):
        return self.data_list[0]
    
    @check_password 
    def append(self, value):
        new_list = self.data_list + [value]
        self.data_list = ElementQueue(new_list).data_list
        
    @check_password    
    def pop(self, index = None):
        index = 0 if index is None else index
        if index > len(self.data_list) or index < 0 or not isinstance(index, int):
            raise ValueError("Incorrect index value")
        element = self.data_list[index]
        self.data_list = ElementDataList(self.data_list[:index] + self.data_list[index + 1:]).data_list
        return[element]
    
    
class ElementStack(ElementDataList):
    
    def __init__(self, data_list=None):
        if data_list is None:
            super().__init__([])
        elif isinstance(data_list, ElementDataList):
            super().__init__(data_list.data_list.copy())
        elif isinstance(data_list, list):
            super().__init__(data_list)
        else:
            raise ValueError("Data_list must be a list or ElementDataList object")
        
    @check_password 
    def get(self):
        return self.data_list[0]
    
    @check_password 
    def append(self, value):
        new_list =  [value] + self.data_list 
        self.data_list = ElementStack(new_list).data_list
        
    @check_password    
    def pop(self, index = None):
        index = 0 if index is None else index
        if index > len(self.data_list) or index < 0 or not isinstance(index, int):
            raise ValueError("Incorrect index value")
        element = self.data_list[index]
        self.data_list = ElementDataList(self.data_list[:index] + self.data_list[index + 1:]).data_list
        return[element]
    
    
class ElementDataMap:
    def __init__(self, data_map = None):
        self.data_map = data_map if data_map != None else {}
        self.__checkDictValues(self.data_map)
       
    def __checkDictValues(self, my_dict):
         if not isinstance(my_dict, dict):
            raise ValueError("The object must be dict")
         if any(not isinstance(i, str) or not isinstance(my_dict[i], int) for i in my_dict):
            raise ValueError("The keys in dict must be of type str and the elements in dict must be of type int")
    
    @check_password 
    def get(self, key):
        if not isinstance(key, str):
            raise ValueError("Incorrect key value")
        if key not in self.data_map:
            return None
        return self.data_map[key]
    
    @check_password 
    def items(self):
        list_of_items = []
        for key in self.data_map:
            list_of_items.append((key, self.data_map[key]))
        return list_of_items
    
    @check_password 
    def values(self):
        list_of_items = []
        for key in self.data_map:
            list_of_items.append(self.data_map[key])
        return list_of_items
    
    @check_password 
    def update(self, other_dict):
        self.__checkDictValues(other_dict)
        for key in other_dict:
            self.data_map[key] = other_dict[key]
    
    def __add__(self, other):
        new_dict = self.data_map.copy()
        for key in other.data_map:
            if key in new_dict:
                new_dict[key] += other.data_map[key]
            else:
                new_dict[key] = other.data_map[key]
        return ElementDataMap(new_dict)
    
    def __sub__(self, other):
        new_dict = self.data_map.copy()
        for key in other.data_map:
            if key in new_dict:
                new_dict[key] -= other.data_map[key]
                
        return ElementDataMap(new_dict)
        
    def __repr__(self):
        return f"data_map = {self.data_map}"

class Element:
    def __init__(self, value, /, data_list = None, data_map = None):
        if not isinstance(value, int):
            raise ValueError("The value must be int")
        self.__value = value
        
        if isinstance(data_list, ElementDataList):
            data_list = data_list.data_list
        if isinstance(data_map, ElementDataMap):
            data_map = data_map.data_map
        
        self.__data_list = ElementDataList(data_list)
        self.__data_map = ElementDataMap(data_map)
    @property    
    @check_password 
    def value(self):
        "Private variable. Only read-only access is possible"
        return self.__value
    
    @property
    @check_password 
    def data_list(self):
        "Private variable. Only read-only access is possible"
        return self.__data_list 
    
    @property
    @check_password 
    def data_map(self):
        "Private variable. Only read-only access is possible"
        return self.__data_map
    
    @value.setter
    @check_password 
    def value(self, new_value):  
        if not isinstance(new_value, int):
            raise ValueError("The value must be int")
        self.__value = new_value
        
        
    @data_list.setter
    @check_password     
    def data_list(self, new_data_list):
        if isinstance(new_data_list, (ElementDataList, ElementQueue)):
            self.__data_list = new_data_list
        elif isinstance(new_data_list, list):
            self.__data_list = ElementDataList(new_data_list)
        else:
            raise ValueError("data_list must be a list, ElementDataList, or ElementQueue object")
     
    @data_map.setter   
    @check_password 
    def data_map(self, new_data_map):
        self.__data_map = ElementDataMap(new_data_map)
     
    @value.deleter   
    @check_password    
    def value(self):
        del self.__value
      
    @data_list.deleter  
    @check_password     
    def data_list(self):
        del self.__data_list
    @data_map.deleter
    @check_password 
    def data_map(self):
        del self.__data_map
        
    def __add__(self, other):
        if isinstance(other, Element):
            new_data_list = self.data_list + other.data_list
            new_data_map = self.data_map + other.data_map
            return Element(self.value + other.value, data_list=new_data_list, data_map=new_data_map)
        elif isinstance(other, int):
            return Element(self.value + other, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("Broooo what the hell")
    
    def __radd__(self, other):
        if isinstance(other, Element):
            new_data_list = other.data_list + self.data_list
            new_data_map = other.data_map + self.data_map
            return Element(self.value + other.value, data_list=new_data_list, data_map=new_data_map)
        elif isinstance(other, int):
            return Element(self.value + other, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("Broooo what the hell")
        
    def __sub__(self, other):
        if isinstance(other, Element):
            new_data_list = self.data_list - other.data_list
            new_data_map = self.data_map - other.data_map
            return Element(self.value - other.value, data_list=new_data_list, data_map=new_data_map)
        elif isinstance(other, int):
            return Element(self.value - other, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("Nonono mr fish")
    
    def __rsub__(self, other):
        if isinstance(other, Element):
            new_data_list = other.data_list - self.data_list
            new_data_map = other.data_map - self.data_map
            return Element(other.value - self.value, data_list=new_data_list, data_map=new_data_map)
        elif isinstance(other, int):
            return Element(other - self.value, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("idiot")
        
    def __mul__(self, other):
        if isinstance(other, int):
            return Element(self.value * other, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("The value must be int")
    
    def __rmul__(self, other):
        if isinstance(other, int):
            return Element(self.value * other, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("The value must be int")
    
    def __floordiv__(self, other):
        if isinstance(other, int):
            return Element(self.value // other, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("The value must be int")
        
    def __rfloordiv__(self, other):
        if isinstance(other, int):
            return Element(other // self.value, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("The value must be int")
    
    def __mod__(self, other):
        if isinstance(other, int):
            return Element(self.value % other, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("The value must be int")
        
    def __rmod__(self, other):
        if isinstance(other, int):
            return Element(other % self.value, data_list=self.data_list, data_map=self.data_map)
        else:
            raise ValueError("The value must be int")
        
    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        elif isinstance(other, Element):
            return self.value == other.value
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __ne__(self, other):
        if isinstance(other, int):
            return self.value != other
        elif isinstance(other, Element):
            return self.value != other.value
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        elif isinstance(other, Element):
            return self.value < other.value
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __rlt__(self, other):
        if isinstance(other, int):
            return other < self.value
        elif isinstance(other, Element):
            return other.value < self.value 
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __gt__(self, other):
        if isinstance(other, int):
            return self.value > other
        elif isinstance(other, Element):
            return self.value > other.value
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __rgt__(self, other):
        if isinstance(other, int):
            return other > self.value
        elif isinstance(other, Element):
            return other.value > self.value 
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __le__(self, other):
        if isinstance(other, int):
            return self.value <= other
        elif isinstance(other, Element):
            return self.value <= other.value
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __rle__(self, other):
        if isinstance(other, int):
            return other <= self.value
        elif isinstance(other, Element):
            return other.value <= self.value 
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __ge__(self, other):
        if isinstance(other, int):
            return self.value >= other
        elif isinstance(other, Element):
            return self.value >= other.value
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __rge__(self, other):
        if isinstance(other, int):
            return other >= self.value
        elif isinstance(other, Element):
            return other.value >= self.value 
        else:
            raise ValueError("Incorrect value. Element objects can only be compared with Element or int objects")
        
    def __getitem__(self, key):
        if isinstance(key, int):
            return self.data_list.get(key)
        elif isinstance(key, str):
            return self.data_map.get(key)
        else:
            raise ValueError("Incorrect key value")
        
    def __setitem__(self, key, value):
        if isinstance(value, int):
            if isinstance(key, int) and 0 <= key < len(self.data_list.data_list):
                self.data_list.data_list[key] = value
            elif isinstance(key, str) and key in self.data_map.data_map:
                self.data_map.data_map[key] = value
            else:
                raise ValueError("Incorrect key value")
        else:
            raise ValueError("Incorrect value")
        
    def __delitem__(self, key):
        if isinstance(key, int):
            del self.data_list.data_list[key]
        elif isinstance(key, str):
            del self.data_map.data_map[key]
        else:
            raise ValueError("Incorrect key value")
        
    def make_queue(self):
        self.data_list = ElementQueue(self.data_list)
        
    def make_stack(self):
        self.data_list = ElementStack(self.data_list)

        
    def __repr__(self):
        return f"Element(value = {self.value}, {self.data_list}, {self.data_map})"


        
a = Element(5, data_list=[1, 2, 3], data_map={"lol": 1, "lololo": 2, "lolo": 3})
b = Element(4,  data_list=[4, 5, 6, 7], data_map={"lol": 1, "dfdfdf": 2, "dfdf": 3})
print(a)
print(b)

a.data_list.pop(1)
a.data_list.append(8)
print(a)
print(a.data_list.get())

print(a.data_map.items())
print(a.data_map.values())
a.data_map.update({"lal":90})
print(a)
print(a.data_map.get("lol"))

a.make_queue()
a.data_list.append(1)
print(a)


