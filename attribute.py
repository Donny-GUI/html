
class Attribute(object):
    """ Attributes are added to the start_tag of an element and are seperated by spaces """
    def __init__(self, name: str, value: str) -> None:
        """DataClass for creating a attribute for an html tag

        Args:
            name (str):  name of the attribute
            value (str): value of the attribute
        """
        self.name = name
        self.value = value
        self.is_integer = False
        try:
            self.value = int(self.value)
            self.is_integer = True
        except ValueError:
            pass
        
    def get(self):
        return self.value
    
    def format(self) -> str:
        if self.is_integer == False:
            return f'{self.name}="{self.value}"'
        elif self.is_integer == True:
            return f"{self.name}={self.value}"
    
    def id(self):
        return self.name
    
    def set(self, value : any) -> None:
        self.value = value
