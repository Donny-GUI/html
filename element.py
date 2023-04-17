from properties import TagType, Tag, Attributes
from attribute import Attribute
from tags import AllTagClasses, HtmlTag


ElementMap = {key:value for key, value in zip(Tag.tags, AllTagClasses)}


class CSS:
    rules = [
    'background', 'background-attachment', 'background-color',
    'background-image', 'background-position', 'background-repeat',
    'border', 'border-bottom', 'border-bottom-color',
    'border-bottom-style', 'border-bottom-width', 'border-collapse',
    'border-color', 'border-left', 'border-left-color',
    'border-left-style', 'border-left-width', 'border-right',
    'border-right-color', 'border-right-style', 'border-right-width',
    'border-spacing', 'border-style', 'border-top', 'border-top-color',
    'border-top-style', 'border-top-width', 'border-width',
    'caption-side', 'clear', 'clip', 'color', 'content', 'counter-increment',
    'counter-reset', 'cursor', 'direction', 'display', 'empty-cells',
    'float', 'font', 'font-family', 'font-size', 'font-size-adjust',
    'font-stretch', 'font-style', 'font-variant', 'font-weight',
    'height', 'image-orientation', 'image-rendering', 'left', 'letter-spacing',
    'line-height', 'list-style', 'list-style-image', 'list-style-position',
    'list-style-type', 'margin', 'margin-bottom', 'margin-left',
    'margin-right', 'margin-top', 'max-height', 'max-width', 'min-height',
    'min-width', 'opacity', 'outline', 'outline-color', 'outline-offset',
    'outline-style', 'outline-width', 'overflow', 'overflow-x', 'overflow-y',
    'padding', 'padding-bottom', 'padding-left', 'padding-right',
    'padding-top', 'page-break-after', 'page-break-before', 'page-break-inside',
    'position', 'quotes', 'resize', 'right', 'table-layout', 'text-align',
    'text-decoration', 'text-indent', 'text-justify', 'text-overflow',
    'text-shadow', 'text-transform', 'top', 'transform', 'transform-origin',
    'unicode-bidi', 'vertical-align', 'visibility', 'white-space', 'width',
    'word-break', 'word-spacing', 'word-wrap', 'z-index'
    ]


class Cascading:
    pass 

class HtmlElement:
    pass

class Style(Cascading):
    def __init__(self, name: str, value: str) -> None:
        self.name = name
        self.value = value
    
    def get(self) -> str:
        return f"{self.name} : {self.value};"


class ElementStyle:
    def __init__(self, css_text:str=None) -> None:
        self.rules = {}
        self.styles = []
        if css_text is not None:
            rules = css_text.split(";")
            for rule in rules:
                name, value = rule.split("=")
                self.styles.append(Style(name=name, value=value))
                self.rules[name] = value
    
    def add_rule(self, name: str, value: str) -> None:
        self.new_style = Style(name=name, value=value)
        self.styles.append(self.new_style)
        self.rules[self.new_style.name] = self.new_style.value
    
    def add_style(self, name: str, value: str) -> None:
        self.new_style = Style(name=name, value=value)
        self.styles.append(self.new_style)
        self.rules[self.new_style.name] = self.new_style.value
        


class Element(HtmlElement):
    """ class for creating any html element """
    def __init__(self, tag_name:str, **kwargs) -> None:
        """
        initialize any html element by its tag name. 
        You may pass any tag attribute to the constructor, 
        however only attributes that the element possesses 
        will be used when create the tag class and the 
        string representation

        Args:
            tag_name (str): name of the html tag examples: body, header, a, div
            kwargs (optional): keyword attributes to be used for the element
        
        
        Element.configure:
            Description: 
                configure any attribute that the element can have  
            Args: 
                attribute (str): name of the attribute
                value     (str): value of the attribute
        
        Element.get: 
            Description:
                create an new instance of the element as an HtmlTag class. This class is 
                inside html.tags, and its name is <tag_name> ex: body = Body(HtmlTag).
            Args:
                self (self): self
            Returns:
                class instance of <tag_name>(HtmlTag)
        
        Element.read:
            Description:
                Create a string representation of the element as if it were in an HTML document
            
            Returns:
                self.element.string (str): string representation of the element

        
        """
        self.tag: str = tag_name
        self.types: list[str] = TagType.map[self.tag]
        self.attribute_names: list = Attributes.map[self.tag]
        self.attribute_values: list = [None for x in self.attribute_names]
        
        if kwargs != None:
            for kwarg in kwargs.items():
                if kwarg[0] in self.attribute_names:
                    index = self.attribute_names.index(kwarg[0])
                    self.attribute_values[index] = kwarg[1]
                
        self.attributes: dict = {key:value for key, value in zip(self.attribute_names, self.attribute_values)}
        self.__attributes: list[Attribute] = [Attribute(name=x[0], value=x[1]) for x in list(self.attributes.items())]
        self.nestable = True if self.tag in Tag.nestable else False
        self.self_closing = True if self.tag in Tag.self_closing else False
        self.element = self.get()
        
    
    def configure(self, attribute: str, value: str) -> None:
        """ Configure any attribute that the element might have

        Args:
            attribute (str): name of the attribute to configure
            value (str): value of the attribute to configure

        Raises:
            Exception: if the attribute is not a valid attribute of the tag
            
        """
        try:
            self.attribute_index = self.attribute_names.index(attribute)
            self.attributes[attribute] = value
            self.attribute_values[self.attribute_index] = value
            self.__attributes[self.attribute_index] = Attribute(name=attribute,value=value)
        except IndexError:
            raise Exception(f"{attribute} is not a valid attribute for {self.tag}")
        self.element = self.get()
    
    
    def get(self) -> HtmlTag:
        """ Get the HtmlTag Class associated with this tag

        Returns:
            self.element (HtmlTag): the corresponding tag class for the <tag_name> given 
        """
        self.attribute_values = [x.value for x in self.__attributes]
        self.html_tag: HtmlTag = ElementMap[self.tag]
        self.element:HtmlTag = self.html_tag(**self.attributes)
        return self.element
    
    def read(self) -> str:
        """ Get a string representation of the element as if it were in an html document

        Returns:
            self.element.string (str): string representation of the element 
        """
        self.element:HtmlTag = self.get()
        return self.element.get()