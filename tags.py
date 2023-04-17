from attribute import Attribute


class HtmlTag:
    def get(self):
        pass

class A(HtmlTag):
    type     = ['content']
    attributes   = ['class', 'id', 'style', 'title', 'aria-label', 'aria-labelledby', 'aria-describedby']
    name     = 'a'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None, aria_label:str=None, aria_labelledby:str=None, aria_describedby:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.aria_label: Attribute = Attribute(name='aria-label', value=aria_label)
        self.aria_labelledby: Attribute = Attribute(name='aria-labelledby', value=aria_labelledby)
        self.aria_describedby: Attribute = Attribute(name='aria-describedby', value=aria_describedby)
        self.all = [self.class_, self.id, self.style, self.title, self.aria_label, self.aria_labelledby, self.aria_describedby]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        return self.retv

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Abbr(HtmlTag):
    type     = []
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'abbr'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Address(HtmlTag):
    type     = ['semantic']
    attributes   = ['alt', 'coords', 'download', 'href', 'hreflang', 'media', 'rel', 'shape', 'target', 'type', 'ping', 'class', 'id', 'style', 'title']
    name     = 'address'
    self_closing = False
    nestable     = False

    def __init__(self, alt:str=None, coords:str=None, download:str=None, href:str=None, hreflang:str=None, media:str=None, rel:str=None, shape:str=None, target:str=None, type:str=None, ping:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.alt: Attribute = Attribute(name='alt', value=alt)
        self.coords: Attribute = Attribute(name='coords', value=coords)
        self.download: Attribute = Attribute(name='download', value=download)
        self.href: Attribute = Attribute(name='href', value=href)
        self.hreflang: Attribute = Attribute(name='hreflang', value=hreflang)
        self.media: Attribute = Attribute(name='media', value=media)
        self.rel: Attribute = Attribute(name='rel', value=rel)
        self.shape: Attribute = Attribute(name='shape', value=shape)
        self.target: Attribute = Attribute(name='target', value=target)
        self.type: Attribute = Attribute(name='type', value=type)
        self.ping: Attribute = Attribute(name='ping', value=ping)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.alt, self.coords, self.download, self.href, self.hreflang, self.media, self.rel, self.shape, self.target, self.type, self.ping, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Area(HtmlTag):
    type     = ['void']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'area'
    self_closing = True
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Article(HtmlTag):
    type     = ['semantic']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'article'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Aside(HtmlTag):
    type     = ['semantic']
    attributes   = ['autoplay', 'controls', 'crossorigin', 'loop', 'muted', 'preload', 'src', 'class', 'id', 'style', 'title']
    name     = 'aside'
    self_closing = False
    nestable     = True

    def __init__(self, autoplay:str=None, controls:str=None, crossorigin:str=None, loop:str=None, muted:str=None, preload:str=None, src:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.autoplay: Attribute = Attribute(name='autoplay', value=autoplay)
        self.controls: Attribute = Attribute(name='controls', value=controls)
        self.crossorigin: Attribute = Attribute(name='crossorigin', value=crossorigin)
        self.loop: Attribute = Attribute(name='loop', value=loop)
        self.muted: Attribute = Attribute(name='muted', value=muted)
        self.preload: Attribute = Attribute(name='preload', value=preload)
        self.src: Attribute = Attribute(name='src', value=src)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.autoplay, self.controls, self.crossorigin, self.loop, self.muted, self.preload, self.src, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Audio(HtmlTag):
    type     = ['content']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'audio'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class B(HtmlTag):
    type     = []
    attributes   = ['href', 'target']
    name     = 'b'
    self_closing = False
    nestable     = False

    def __init__(self, href:str=None, target:str=None) -> None:
        super().__init__()
        self.href: Attribute = Attribute(name='href', value=href)
        self.target: Attribute = Attribute(name='target', value=target)
        self.all = [self.href, self.target]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Base(HtmlTag):
    type     = ['void']
    attributes   = ['dir', 'class', 'id', 'style', 'title']
    name     = 'base'
    self_closing = True
    nestable     = False

    def __init__(self, dir:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [dir, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Bdi(HtmlTag):
    type     = []
    attributes   = ['dir', 'class', 'id', 'style', 'title']
    name     = 'bdi'
    self_closing = False
    nestable     = False

    def __init__(self, dir:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [dir, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Bdo(HtmlTag):
    type     = []
    attributes   = ['cite', 'class', 'id', 'style', 'title']
    name     = 'bdo'
    self_closing = False
    nestable     = False

    def __init__(self, cite:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.cite: Attribute = Attribute(name='cite', value=cite)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.cite, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Blockquote(HtmlTag):
    type     = []
    attributes   = ['onafterprint', 'onbeforeprint', 'onbeforeunload', 'onhashchange', 'onlanguagechange', 'onload', 'onmessage', 'onmessageerror', 'onoffline', 'ononline', 'onpagehide', 'onpageshow', 'onpopstate', 'onrejectionhandled', 'onstorage', 'onunhandledrejection', 'onunload', 'class', 'id', 'style', 'title']
    name     = 'blockquote'
    self_closing = False
    nestable     = False

    def __init__(self, onafterprint:str=None, onbeforeprint:str=None, onbeforeunload:str=None, onhashchange:str=None, onlanguagechange:str=None, onload:str=None, onmessage:str=None, onmessageerror:str=None, onoffline:str=None, ononline:str=None, onpagehide:str=None, onpageshow:str=None, onpopstate:str=None, onrejectionhandled:str=None, onstorage:str=None, onunhandledrejection:str=None, onunload:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.onafterprint: Attribute = Attribute(name='onafterprint', value=onafterprint)
        self.onbeforeprint: Attribute = Attribute(name='onbeforeprint', value=onbeforeprint)
        self.onbeforeunload: Attribute = Attribute(name='onbeforeunload', value=onbeforeunload)
        self.onhashchange: Attribute = Attribute(name='onhashchange', value=onhashchange)
        self.onlanguagechange: Attribute = Attribute(name='onlanguagechange', value=onlanguagechange)
        self.onload: Attribute = Attribute(name='onload', value=onload)
        self.onmessage: Attribute = Attribute(name='onmessage', value=onmessage)
        self.onmessageerror: Attribute = Attribute(name='onmessageerror', value=onmessageerror)
        self.onoffline: Attribute = Attribute(name='onoffline', value=onoffline)
        self.ononline: Attribute = Attribute(name='ononline', value=ononline)
        self.onpagehide: Attribute = Attribute(name='onpagehide', value=onpagehide)
        self.onpageshow: Attribute = Attribute(name='onpageshow', value=onpageshow)
        self.onpopstate: Attribute = Attribute(name='onpopstate', value=onpopstate)
        self.onrejectionhandled: Attribute = Attribute(name='onrejectionhandled', value=onrejectionhandled)
        self.onstorage: Attribute = Attribute(name='onstorage', value=onstorage)
        self.onunhandledrejection: Attribute = Attribute(name='onunhandledrejection', value=onunhandledrejection)
        self.onunload: Attribute = Attribute(name='onunload', value=onunload)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.onafterprint, self.onbeforeprint, self.onbeforeunload, self.onhashchange, self.onlanguagechange, self.onload, self.onmessage, self.onmessageerror, self.onoffline, self.ononline, self.onpagehide, self.onpageshow, self.onpopstate, self.onrejectionhandled, self.onstorage, self.onunhandledrejection, self.onunload, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Body(HtmlTag):
    type     = ['structural']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'body'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}

        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Br(HtmlTag):
    type     = ['void', 'structural']
    attributes   = ['autofocus', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'name', 'type', 'value', 'class', 'id', 'style', 'title']
    name     = 'br'
    self_closing = True
    nestable     = False

    def __init__(self, autofocus:str=None, disabled:str=None, form:str=None, formaction:str=None, formenctype:str=None, formmethod:str=None, formnovalidate:str=None, formtarget:str=None, name:str=None, type:str=None, value:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.autofocus: Attribute = Attribute(name='autofocus', value=autofocus)
        self.disabled: Attribute = Attribute(name='disabled', value=disabled)
        self.form: Attribute = Attribute(name='form', value=form)
        self.formaction: Attribute = Attribute(name='formaction', value=formaction)
        self.formenctype: Attribute = Attribute(name='formenctype', value=formenctype)
        self.formmethod: Attribute = Attribute(name='formmethod', value=formmethod)
        self.formnovalidate: Attribute = Attribute(name='formnovalidate', value=formnovalidate)
        self.formtarget: Attribute = Attribute(name='formtarget', value=formtarget)
        self.name: Attribute = Attribute(name='name', value=name)
        self.type: Attribute = Attribute(name='type', value=type)
        self.value: Attribute = Attribute(name='value', value=value)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.autofocus, self.disabled, self.form, self.formaction, self.formenctype, self.formmethod, self.formnovalidate, self.formtarget, self.name, self.type, self.value, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Button(HtmlTag):
    type     = ['content', 'meta']
    attributes   = ['width', 'height', 'class', 'id', 'style', 'title']
    name     = 'button'
    self_closing = False
    nestable     = True

    def __init__(self, width:str=None, height:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.width: Attribute = Attribute(name='width', value=width)
        self.height: Attribute = Attribute(name='height', value=height)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.width, self.height, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Canvas(HtmlTag):
    type     = []
    attributes   = ['align', 'class', 'id', 'style', 'title']
    name     = 'canvas'
    self_closing = False
    nestable     = False

    def __init__(self, align:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Caption(HtmlTag):
    type     = ['form']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'caption'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Cite(HtmlTag):
    type     = []
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'cite'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Code(HtmlTag):
    type     = []
    attributes   = ['span', 'class', 'id', 'style', 'title']
    name     = 'code'
    self_closing = False
    nestable     = False

    def __init__(self, span:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.span: Attribute = Attribute(name='span', value=span)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.span, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Col(HtmlTag):
    type     = ['void', 'form']
    attributes   = ['span', 'class', 'id', 'style', 'title']
    name     = 'col'
    self_closing = True
    nestable     = False

    def __init__(self, span:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.span: Attribute = Attribute(name='span', value=span)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.span, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Colgroup(HtmlTag):
    type     = ['form']
    attributes   = ['value', 'class', 'id', 'style', 'title']
    name     = 'colgroup'
    self_closing = False
    nestable     = False

    def __init__(self, value:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.value: Attribute = Attribute(name='value', value=value)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.value, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Data(HtmlTag):
    type     = []
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'data'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Datalist(HtmlTag):
    type     = ['meta']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'datalist'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Dd(HtmlTag):
    type     = ['table']
    attributes   = ['cite', 'datetime', 'class', 'id', 'style', 'title']
    name     = 'dd'
    self_closing = False
    nestable     = True

    def __init__(self, cite:str=None, datetime:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.cite: Attribute = Attribute(name='cite', value=cite)
        self.datetime: Attribute = Attribute(name='datetime', value=datetime)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.cite, self.datetime, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Del(HtmlTag):
    type     = []
    attributes   = ['open', 'class', 'id', 'style', 'title']
    name     = 'del'
    self_closing = False
    nestable     = False

    def __init__(self, open:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.open: Attribute = Attribute(name='open', value=open)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.open, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Details(HtmlTag):
    type     = ['semantic']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'details'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Dfn(HtmlTag):
    type     = []
    attributes   = ['open', 'class', 'id', 'style', 'title']
    name     = 'dfn'
    self_closing = False
    nestable     = False

    def __init__(self, open:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.open: Attribute = Attribute(name='open', value=open)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.open, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Dialog(HtmlTag):
    type     = []
    attributes   = ['id', 'class', 'style', 'title', 'data-']
    name     = 'dialog'
    self_closing = False
    nestable     = False

    def __init__(self, id:str=None, class_:str=None, style:str=None, title:str=None, data:str=None) -> None:
        super().__init__()
        self.id: Attribute = Attribute(name='id', value=id)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.data: Attribute = Attribute(name='data-', value=data)
        self.all = [self.id, self.class_, self.style, self.title, self.data]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Div(HtmlTag):
    type     = ['structural']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'div'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Dl(HtmlTag):
    type     = ['table']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'dl'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Dt(HtmlTag):
    type     = ['table']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'dt'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Em(HtmlTag):
    type     = []
    attributes   = ['src', 'type', 'width', 'height', 'class', 'id', 'style', 'title']
    name     = 'em'
    self_closing = False
    nestable     = False

    def __init__(self, src:str=None, type:str=None, width:str=None, height:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.src: Attribute = Attribute(name='src', value=src)
        self.type: Attribute = Attribute(name='type', value=type)
        self.width: Attribute = Attribute(name='width', value=width)
        self.height: Attribute = Attribute(name='height', value=height)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.src, self.type, self.width, self.height, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Embed(HtmlTag):
    type     = ['void', 'list']
    attributes   = ['disabled', 'form', 'name', 'class', 'id', 'style', 'title']
    name     = 'embed'
    self_closing = True
    nestable     = False

    def __init__(self, disabled:str=None, form:str=None, name:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.disabled: Attribute = Attribute(name='disabled', value=disabled)
        self.form: Attribute = Attribute(name='form', value=form)
        self.name: Attribute = Attribute(name='name', value=name)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.disabled, self.form, self.name, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Fieldset(HtmlTag):
    type     = ['meta']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'fieldset'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Figcaption(HtmlTag):
    type     = ['semantic']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'figcaption'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Figure(HtmlTag):
    type     = ['semantic']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'figure'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Footer(HtmlTag):
    type     = ['semantic']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'footer'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Form(HtmlTag):
    type     = ['content', 'meta']
    attributes   = ['align', 'class', 'id', 'style', 'title']
    name     = 'form'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class H1(HtmlTag):
    type     = ['content']
    attributes   = ['align', 'class', 'id', 'style', 'title']
    name     = 'h1'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class H2(HtmlTag):
    type     = ['content']
    attributes   = ['align', 'class', 'id', 'style', 'title']
    name     = 'h2'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class H3(HtmlTag):
    type     = ['content']
    attributes   = ['align', 'class', 'id', 'style', 'title']
    name     = 'h3'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class H4(HtmlTag):
    type     = ['content']
    attributes   = ['align', 'class', 'id', 'style', 'title']
    name     = 'h4'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class H5(HtmlTag):
    type     = ['content']
    attributes   = ['align', 'class', 'id', 'style', 'title']
    name     = 'h5'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class H6(HtmlTag):
    type     = ['content']
    attributes   = ['profile', 'class', 'id', 'style', 'title']
    name     = 'h6'
    self_closing = False
    nestable     = True

    def __init__(self, profile:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.profile: Attribute = Attribute(name='profile', value=profile)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.profile, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Head(HtmlTag):
    type     = ['structural']
    attributes   = ['class', 'id', 'style', 'title']
    name     = 'head'
    self_closing = False
    nestable     = True

    def __init__(self, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Header(HtmlTag):
    type     = ['semantic']
    attributes   = ['align', 'color', 'noshade', 'size', 'width', 'class', 'id', 'style', 'title']
    name     = 'header'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, color:str=None, noshade:str=None, size:str=None, width:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.color: Attribute = Attribute(name='color', value=color)
        self.noshade: Attribute = Attribute(name='noshade', value=noshade)
        self.size: Attribute = Attribute(name='size', value=size)
        self.width: Attribute = Attribute(name='width', value=width)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.align, self.color, self.noshade, self.size, self.width, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Hr(HtmlTag):
    type     = ['void', 'structural']
    attributes   = ['manifest', 'class', 'id', 'style', 'title']
    name     = 'hr'
    self_closing = True
    nestable     = False

    def __init__(self, manifest:str=None, class_:str=None, id:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.manifest: Attribute = Attribute(name='manifest', value=manifest)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.manifest, self.class_, self.id, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Html(HtmlTag):
    type     = ['structural']
    attributes   = ['accesskey', 'class', 'contenteditable', 'data-*', 'dir', 'draggable', 'hidden', 'id', 'lang', 'style', 'tabindex', 'title', 'translate']
    name     = 'html'
    self_closing = False
    nestable     = True

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, data:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.data: Attribute = Attribute(name='data-', value=data)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.data, self.dir, self.draggable, self.hidden, self.id, self.lang, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class I(HtmlTag):
    type     = []
    attributes   = ['allow', 'allowfullscreen', 'allowpaymentrequest', 'allowtransparency', 'class', 'loading', 'sandbox', 'src', 'srcdoc', 'style', 'title']
    name     = 'i'
    self_closing = False
    nestable     = False

    def __init__(self, allow:str=None, allowfullscreen:str=None, allowpaymentrequest:str=None, allowtransparency:str=None, class_:str=None, loading:str=None, sandbox:str=None, src:str=None, srcdoc:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.allow: Attribute = Attribute(name='allow', value=allow)
        self.allowfullscreen: Attribute = Attribute(name='allowfullscreen', value=allowfullscreen)
        self.allowpaymentrequest: Attribute = Attribute(name='allowpaymentrequest', value=allowpaymentrequest)
        self.allowtransparency: Attribute = Attribute(name='allowtransparency', value=allowtransparency)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.loading: Attribute = Attribute(name='loading', value=loading)
        self.sandbox: Attribute = Attribute(name='sandbox', value=sandbox)
        self.src: Attribute = Attribute(name='src', value=src)
        self.srcdoc: Attribute = Attribute(name='srcdoc', value=srcdoc)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.allow, self.allowfullscreen, self.allowpaymentrequest, self.allowtransparency, self.class_, self.loading, self.sandbox, self.src, self.srcdoc, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Iframe(HtmlTag):
    type     = ['list']
    attributes   = ['alt', 'border', 'class', 'crossorigin', 'decoding', 'height', 'importance', 'intrinsicsize', 'ismap', 'loading', 'referrerpolicy', 'sizes', 'src', 'srcset', 'style', 'title', 'usemap', 'width']
    name     = 'iframe'
    self_closing = False
    nestable     = False

    def __init__(self, alt:str=None, border:str=None, class_:str=None, crossorigin:str=None, decoding:str=None, height:str=None, importance:str=None, intrinsicsize:str=None, ismap:str=None, loading:str=None, referrerpolicy:str=None, sizes:str=None, src:str=None, srcset:str=None, style:str=None, title:str=None, usemap:str=None, width:str=None) -> None:
        super().__init__()
        self.alt: Attribute = Attribute(name='alt', value=alt)
        self.border: Attribute = Attribute(name='border', value=border)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.crossorigin: Attribute = Attribute(name='crossorigin', value=crossorigin)
        self.decoding: Attribute = Attribute(name='decoding', value=decoding)
        self.height: Attribute = Attribute(name='height', value=height)
        self.importance: Attribute = Attribute(name='importance', value=importance)
        self.intrinsicsize: Attribute = Attribute(name='intrinsicsize', value=intrinsicsize)
        self.ismap: Attribute = Attribute(name='ismap', value=ismap)
        self.loading: Attribute = Attribute(name='loading', value=loading)
        self.referrerpolicy: Attribute = Attribute(name='referrerpolicy', value=referrerpolicy)
        self.sizes: Attribute = Attribute(name='sizes', value=sizes)
        self.src: Attribute = Attribute(name='src', value=src)
        self.srcset: Attribute = Attribute(name='srcset', value=srcset)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.usemap: Attribute = Attribute(name='usemap', value=usemap)
        self.width: Attribute = Attribute(name='width', value=width)
        self.all = [self.alt, self.border, self.class_, self.crossorigin, self.decoding, self.height, self.importance, self.intrinsicsize, self.ismap, self.loading, self.referrerpolicy, self.sizes, self.src, self.srcset, self.style, self.title, self.usemap, self.width]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Img(HtmlTag):
    type     = ['void', 'content']
    attributes   = ['accept', 'accesskey', 'alt', 'autocomplete', 'autofocus', 'capture', 'checked', 'class', 'contenteditable', 'dir', 'dirname', 'disabled', 'form', 'formaction', 'formenctype', 'formmethod', 'formnovalidate', 'formtarget', 'height', 'hidden', 'id', 'inputmode', 'ismap', 'lang', 'list', 'max', 'maxlength', 'min', 'minlength', 'multiple', 'name', 'pattern', 'placeholder', 'readonly', 'required', 'size', 'spellcheck', 'src', 'step', 'style', 'tabindex', 'title', 'translate', 'type', 'usemap', 'value', 'width']
    name     = 'img'
    self_closing = True
    nestable     = False

    def __init__(self, accept:str=None, accesskey:str=None, alt:str=None, autocomplete:str=None, autofocus:str=None, capture:str=None, checked:str=None, class_:str=None, contenteditable:str=None, dir:str=None, dirname:str=None, disabled:str=None, form:str=None, formaction:str=None, formenctype:str=None, formmethod:str=None, formnovalidate:str=None, formtarget:str=None, height:str=None, hidden:str=None, id:str=None, inputmode:str=None, ismap:str=None, lang:str=None, list:str=None, max:str=None, maxlength:str=None, min:str=None, minlength:str=None, multiple:str=None, name:str=None, pattern:str=None, placeholder:str=None, readonly:str=None, required:str=None, size:str=None, spellcheck:str=None, src:str=None, step:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None, type:str=None, usemap:str=None, value:str=None, width:str=None) -> None:      
        super().__init__()
        self.accept: Attribute = Attribute(name='accept', value=accept)
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.alt: Attribute = Attribute(name='alt', value=alt)
        self.autocomplete: Attribute = Attribute(name='autocomplete', value=autocomplete)
        self.autofocus: Attribute = Attribute(name='autofocus', value=autofocus)
        self.capture: Attribute = Attribute(name='capture', value=capture)
        self.checked: Attribute = Attribute(name='checked', value=checked)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.dirname: Attribute = Attribute(name='dirname', value=dirname)
        self.disabled: Attribute = Attribute(name='disabled', value=disabled)
        self.form: Attribute = Attribute(name='form', value=form)
        self.formaction: Attribute = Attribute(name='formaction', value=formaction)
        self.formenctype: Attribute = Attribute(name='formenctype', value=formenctype)
        self.formmethod: Attribute = Attribute(name='formmethod', value=formmethod)
        self.formnovalidate: Attribute = Attribute(name='formnovalidate', value=formnovalidate)
        self.formtarget: Attribute = Attribute(name='formtarget', value=formtarget)
        self.height: Attribute = Attribute(name='height', value=height)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.inputmode: Attribute = Attribute(name='inputmode', value=inputmode)
        self.ismap: Attribute = Attribute(name='ismap', value=ismap)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.list: Attribute = Attribute(name='list', value=list)
        self.max: Attribute = Attribute(name='max', value=max)
        self.maxlength: Attribute = Attribute(name='maxlength', value=maxlength)
        self.min: Attribute = Attribute(name='min', value=min)
        self.minlength: Attribute = Attribute(name='minlength', value=minlength)
        self.multiple: Attribute = Attribute(name='multiple', value=multiple)
        self.name: Attribute = Attribute(name='name', value=name)
        self.pattern: Attribute = Attribute(name='pattern', value=pattern)
        self.placeholder: Attribute = Attribute(name='placeholder', value=placeholder)
        self.readonly: Attribute = Attribute(name='readonly', value=readonly)
        self.required: Attribute = Attribute(name='required', value=required)
        self.size: Attribute = Attribute(name='size', value=size)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.src: Attribute = Attribute(name='src', value=src)
        self.step: Attribute = Attribute(name='step', value=step)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.type: Attribute = Attribute(name='type', value=type)
        self.usemap: Attribute = Attribute(name='usemap', value=usemap)
        self.value: Attribute = Attribute(name='value', value=value)
        self.width: Attribute = Attribute(name='width', value=width)
        self.all = [self.accept, self.accesskey, self.alt, self.autocomplete, self.autofocus, self.capture, self.checked, self.class_, self.contenteditable, self.dir, self.dirname, self.disabled, self.form, self.formaction, self.formenctype, self.formmethod, self.formnovalidate, self.formtarget, self.height, self.hidden, self.id, self.inputmode, self.ismap, self.lang, self.list, self.max, self.maxlength, self.min, self.minlength, self.multiple, self.name, self.pattern, self.placeholder, self.readonly, self.required, self.size, self.spellcheck, self.src, self.step, self.style, self.tabindex, self.title, self.translate, self.type, self.usemap, self.value, self.width]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Input(HtmlTag):
    type     = ['void', 'content', 'meta']
    attributes   = ['cite', 'class', 'datetime', 'style', 'title']
    name     = 'input'
    self_closing = True
    nestable     = False

    def __init__(self, cite:str=None, class_:str=None, datetime:str=None, style:str=None, title:str=None) -> None:
        super().__init__()
        self.cite: Attribute = Attribute(name='cite', value=cite)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.datetime: Attribute = Attribute(name='datetime', value=datetime)
        self.style: Attribute = Attribute(name='style', value=style)
        self.title: Attribute = Attribute(name='title', value=title)
        self.all = [self.cite, self.class_, self.datetime, self.style, self.title]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Ins(HtmlTag):
    type     = []
    attributes   = ['class', 'contenteditable', 'data-*', 'dir', 'hidden', 'id', 'lang', 'style', 'tabindex', 'title', 'translate']
    name     = 'ins'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, contenteditable:str=None, data:str=None, dir:str=None, hidden:str=None, id:str=None, lang:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.data: Attribute = Attribute(name='data-', value=data)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.class_, self.contenteditable, self.data, self.dir, self.hidden, self.id, self.lang, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Kbd(HtmlTag):
    type     = []
    attributes   = ['accesskey', 'class', 'contenteditable', 'for', 'form', 'hidden', 'id', 'lang', 'style', 'tabindex', 'title', 'translate']
    name     = 'kbd'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, for_:str=None, form:str=None, hidden:str=None, id:str=None, lang:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.for_: Attribute = Attribute(name='for', value=for_)
        self.form: Attribute = Attribute(name='form', value=form)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.for_, self.form, self.hidden, self.id, self.lang, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Label(HtmlTag):
    type     = ['meta']
    attributes   = ['accesskey', 'align', 'class', 'contenteditable', 'dir', 'hidden', 'id', 'lang', 'style', 'tabindex', 'title', 'translate']
    name     = 'label'
    self_closing = False
    nestable     = True

    def __init__(self, accesskey:str=None, align:str=None, class_:str=None, contenteditable:str=None, dir:str=None, hidden:str=None, id:str=None, lang:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.align: Attribute = Attribute(name='align', value=align)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.align, self.class_, self.contenteditable, self.dir, self.hidden, self.id, self.lang, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Legend(HtmlTag):
    type     = ['meta']
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'hidden', 'id', 'lang', 'style', 'tabindex', 'title', 'translate', 'type', 'value']
    name     = 'legend'
    self_closing = False
    nestable     = True

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, hidden:str=None, id:str=None, lang:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None, type:str=None, value:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.type: Attribute = Attribute(name='type', value=type)
        self.value: Attribute = Attribute(name='value', value=value)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.hidden, self.id, self.lang, self.style, self.tabindex, self.title, self.translate, self.type, self.value]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Li(HtmlTag):
    type     = ['content', 'table']
    attributes   = ['href', 'hreflang', 'media', 'rel', 'sizes', 'type']
    name     = 'li'
    self_closing = False
    nestable     = True

    def __init__(self, href:str=None, hreflang:str=None, media:str=None, rel:str=None, sizes:str=None, type:str=None) -> None:
        super().__init__()
        self.href: Attribute = Attribute(name='href', value=href)
        self.hreflang: Attribute = Attribute(name='hreflang', value=hreflang)
        self.media: Attribute = Attribute(name='media', value=media)
        self.rel: Attribute = Attribute(name='rel', value=rel)
        self.sizes: Attribute = Attribute(name='sizes', value=sizes)
        self.type: Attribute = Attribute(name='type', value=type)
        self.all = [self.href, self.hreflang, self.media, self.rel, self.sizes, self.type]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Link(HtmlTag):
    type     = ['void']
    attributes   = []
    name     = 'link'
    self_closing = True
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Main(HtmlTag):
    type     = ['semantic']
    attributes   = ['name']
    name     = 'main'
    self_closing = False
    nestable     = False

    def __init__(self, name:str=None) -> None:
        super().__init__()
        self.name: Attribute = Attribute(name='name', value=name)
        self.all = [self.name]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Map(HtmlTag):
    type     = []
    attributes   = []
    name     = 'map'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}


        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Mark(HtmlTag):
    type     = ['semantic']
    attributes   = ['charset', 'content', 'http-equiv', 'name']
    name     = 'mark'
    self_closing = False
    nestable     = False

    def __init__(self, charset:str=None, content:str=None, http_equiv:str=None, name:str=None) -> None:
        super().__init__()
        self.charset: Attribute = Attribute(name='charset', value=charset)
        self.content: Attribute = Attribute(name='content', value=content)
        self.http_equiv: Attribute = Attribute(name='http-equiv', value=http_equiv)
        self.name: Attribute = Attribute(name='name', value=name)
        self.all = [self.charset, self.content, self.http_equiv, self.name]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.inner_content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.inner_content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.inner_content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Meta(HtmlTag):
    type     = ['void', 'structural']
    attributes   = ['form', 'high', 'low', 'max', 'min', 'optimum', 'value']
    name     = 'meta'
    self_closing = True
    nestable     = False

    def __init__(self, form:str=None, high:str=None, low:str=None, max:str=None, min:str=None, optimum:str=None, value:str=None) -> None:
        super().__init__()
        self.form: Attribute = Attribute(name='form', value=form)
        self.high: Attribute = Attribute(name='high', value=high)
        self.low: Attribute = Attribute(name='low', value=low)
        self.max: Attribute = Attribute(name='max', value=max)
        self.min: Attribute = Attribute(name='min', value=min)
        self.optimum: Attribute = Attribute(name='optimum', value=optimum)
        self.value: Attribute = Attribute(name='value', value=value)
        self.all = [self.form, self.high, self.low, self.max, self.min, self.optimum, self.value]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Meter(HtmlTag):
    type     = []
    attributes   = []
    name     = 'meter'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Nav(HtmlTag):
    type     = ['semantic']
    attributes   = []
    name     = 'nav'
    self_closing = False
    nestable     = True

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Noscript(HtmlTag):
    type     = []
    attributes   = ['data', 'form', 'height', 'name', 'type', 'usemap', 'width']
    name     = 'noscript'
    self_closing = False
    nestable     = False

    def __init__(self, data:str=None, form:str=None, height:str=None, name:str=None, type:str=None, usemap:str=None, width:str=None) -> None:
        super().__init__()
        self.data: Attribute = Attribute(name='data', value=data)
        self.form: Attribute = Attribute(name='form', value=form)
        self.height: Attribute = Attribute(name='height', value=height)
        self.name: Attribute = Attribute(name='name', value=name)
        self.type: Attribute = Attribute(name='type', value=type)
        self.usemap: Attribute = Attribute(name='usemap', value=usemap)
        self.width: Attribute = Attribute(name='width', value=width)
        self.all = [self.data, self.form, self.height, self.name, self.type, self.usemap, self.width]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Object(HtmlTag):
    type     = ['list']
    attributes   = ['reversed', 'start', 'type']
    name     = 'object'
    self_closing = False
    nestable     = False

    def __init__(self, reversed:str=None, start:str=None, type:str=None) -> None:
        super().__init__()
        self.reversed: Attribute = Attribute(name='reversed', value=reversed)
        self.start: Attribute = Attribute(name='start', value=start)
        self.type: Attribute = Attribute(name='type', value=type)
        self.all = [self.reversed, self.start, self.type]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Ol(HtmlTag):
    type     = ['content', 'table']
    attributes   = ['disabled', 'label']
    name     = 'ol'
    self_closing = False
    nestable     = True

    def __init__(self, disabled:str=None, label:str=None) -> None:
        super().__init__()
        self.disabled: Attribute = Attribute(name='disabled', value=disabled)
        self.label: Attribute = Attribute(name='label', value=label)
        self.all = [self.disabled, self.label]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Optgroup(HtmlTag):
    type     = ['meta']
    attributes   = ['disabled', 'label', 'selected', 'value']
    name     = 'optgroup'
    self_closing = False
    nestable     = True

    def __init__(self, disabled:str=None, label:str=None, selected:str=None, value:str=None) -> None:
        super().__init__()
        self.disabled: Attribute = Attribute(name='disabled', value=disabled)
        self.label: Attribute = Attribute(name='label', value=label)
        self.selected: Attribute = Attribute(name='selected', value=selected)
        self.value: Attribute = Attribute(name='value', value=value)
        self.all = [self.disabled, self.label, self.selected, self.value]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Option(HtmlTag):
    type     = ['meta']
    attributes   = ['for', 'form', 'name']
    name     = 'option'
    self_closing = False
    nestable     = True

    def __init__(self, for_:str=None, form:str=None, name:str=None) -> None:
        super().__init__()
        self.for_: Attribute = Attribute(name='for', value=for_)
        self.form: Attribute = Attribute(name='form', value=form)
        self.name: Attribute = Attribute(name='name', value=name)
        self.all = [self.for_, self.form, self.name]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Output(HtmlTag):
    type     = ['meta']
    attributes   = []
    name     = 'output'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class P(HtmlTag):
    type     = ['content']
    attributes   = ['name', 'type', 'value', 'valuetype']
    name     = 'p'
    self_closing = False
    nestable     = True

    def __init__(self, name:str=None, type:str=None, value:str=None, valuetype:str=None) -> None:
        super().__init__()
        self.name: Attribute = Attribute(name='name', value=name)
        self.type: Attribute = Attribute(name='type', value=type)
        self.value: Attribute = Attribute(name='value', value=value)
        self.valuetype: Attribute = Attribute(name='valuetype', value=valuetype)
        self.all = [self.name, self.type, self.value, self.valuetype]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Param(HtmlTag):
    type     = ['void', 'list']
    attributes   = []
    name     = 'param'
    self_closing = True
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Picture(HtmlTag):
    type     = []
    attributes   = []
    name     = 'picture'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Pre(HtmlTag):
    type     = []
    attributes   = ['max', 'value']
    name     = 'pre'
    self_closing = False
    nestable     = False

    def __init__(self, max:str=None, value:str=None) -> None:
        super().__init__()
        self.max: Attribute = Attribute(name='max', value=max)
        self.value: Attribute = Attribute(name='value', value=value)
        self.all = [self.max, self.value]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Progress(HtmlTag):
    type     = []
    attributes   = ['cite']
    name     = 'progress'
    self_closing = False
    nestable     = False

    def __init__(self, cite:str=None) -> None:
        super().__init__()
        self.cite: Attribute = Attribute(name='cite', value=cite)
        self.all = [self.cite]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Q(HtmlTag):
    type     = []
    attributes   = []
    name     = 'q'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Rp(HtmlTag):
    type     = []
    attributes   = []
    name     = 'rp'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Rt(HtmlTag):
    type     = []
    attributes   = []
    name     = 'rt'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Ruby(HtmlTag):
    type     = []
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'ruby'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class S(HtmlTag):
    type     = []
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 's'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Samp(HtmlTag):
    type     = []
    attributes   = ['async', 'charset', 'class', 'defer', 'integrity', 'language', 'src', 'type']
    name     = 'samp'
    self_closing = False
    nestable     = False

    def __init__(self, async_:str=None, charset:str=None, class_:str=None, defer:str=None, integrity:str=None, language:str=None, src:str=None, type:str=None) -> None:
        super().__init__()
        self.async_: Attribute = Attribute(name='async', value=async_)
        self.charset: Attribute = Attribute(name='charset', value=charset)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.defer: Attribute = Attribute(name='defer', value=defer)
        self.integrity: Attribute = Attribute(name='integrity', value=integrity)
        self.language: Attribute = Attribute(name='language', value=language)
        self.src: Attribute = Attribute(name='src', value=src)
        self.type: Attribute = Attribute(name='type', value=type)
        self.all = [self.async_, self.self.charset, self.class_, self.defer, self.integrity, self.language, self.src, self.type]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Script(HtmlTag):
    type     = []
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'script'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Section(HtmlTag):
    type     = ['semantic']
    attributes   = ['accesskey', 'autofocus', 'class', 'contenteditable', 'dir', 'disabled', 'form', 'hidden', 'id', 'lang', 'multiple', 'name', 'required', 'size', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'section'
    self_closing = False
    nestable     = True

    def __init__(self, accesskey:str=None, autofocus:str=None, class_:str=None, contenteditable:str=None, dir:str=None, disabled:str=None, form:str=None, hidden:str=None, id:str=None, lang:str=None, multiple:str=None, name:str=None, required:str=None, size:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.autofocus: Attribute = Attribute(name='autofocus', value=autofocus)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.disabled: Attribute = Attribute(name='disabled', value=disabled)
        self.form: Attribute = Attribute(name='form', value=form)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.multiple: Attribute = Attribute(name='multiple', value=multiple)
        self.name: Attribute = Attribute(name='name', value=name)
        self.required: Attribute = Attribute(name='required', value=required)
        self.size: Attribute = Attribute(name='size', value=size)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.autofocus, self.class_, self.contenteditable, self.dir, self.disabled, self.form, self.hidden, self.id, self.lang, self.multiple, self.name, self.required, self.size, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Select(HtmlTag):
    type     = ['meta']
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'select'
    self_closing = False
    nestable     = True

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Small(HtmlTag):
    type     = []
    attributes   = ['media', 'sizes', 'src', 'srcset', 'type']
    name     = 'small'
    self_closing = False
    nestable     = False

    def __init__(self, media:str=None, sizes:str=None, src:str=None, srcset:str=None, type:str=None) -> None:
        super().__init__()
        self.media: Attribute = Attribute(name='media', value=media)
        self.sizes: Attribute = Attribute(name='sizes', value=sizes)
        self.src: Attribute = Attribute(name='src', value=src)
        self.srcset: Attribute = Attribute(name='srcset', value=srcset)
        self.type: Attribute = Attribute(name='type', value=type)
        self.all = [self.media, self.sizes, self.src, self.srcset, self.type]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Source(HtmlTag):
    type     = ['void', 'list']
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'source'
    self_closing = True
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Span(HtmlTag):
    type     = ['structural']
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'span'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Strong(HtmlTag):
    type     = []
    attributes   = ['media', 'scoped', 'type']
    name     = 'strong'
    self_closing = False
    nestable     = False

    def __init__(self, media:str=None, scoped:str=None, type:str=None) -> None:
        super().__init__()
        self.media: Attribute = Attribute(name='media', value=media)
        self.scoped: Attribute = Attribute(name='scoped', value=scoped)
        self.type: Attribute = Attribute(name='type', value=type)
        self.all = [self.media, self.scoped, self.type]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Style(HtmlTag):
    type     = []
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'style'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Sub(HtmlTag):
    type     = []
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'sub'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Summary(HtmlTag):
    type     = ['semantic']
    attributes   = ['accesskey', 'class', 'contenteditable', 'dir', 'draggable', 'hidden', 'id', 'lang', 'spellcheck', 'style', 'tabindex', 'title', 'translate']
    name     = 'summary'
    self_closing = False
    nestable     = False

    def __init__(self, accesskey:str=None, class_:str=None, contenteditable:str=None, dir:str=None, draggable:str=None, hidden:str=None, id:str=None, lang:str=None, spellcheck:str=None, style:str=None, tabindex:str=None, title:str=None, translate:str=None) -> None:
        super().__init__()
        self.accesskey: Attribute = Attribute(name='accesskey', value=accesskey)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.contenteditable: Attribute = Attribute(name='contenteditable', value=contenteditable)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.draggable: Attribute = Attribute(name='draggable', value=draggable)
        self.hidden: Attribute = Attribute(name='hidden', value=hidden)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.spellcheck: Attribute = Attribute(name='spellcheck', value=spellcheck)
        self.style: Attribute = Attribute(name='style', value=style)
        self.tabindex: Attribute = Attribute(name='tabindex', value=tabindex)
        self.title: Attribute = Attribute(name='title', value=title)
        self.translate: Attribute = Attribute(name='translate', value=translate)
        self.all = [self.accesskey, self.class_, self.contenteditable, self.dir, self.draggable, self.hidden, self.id, self.lang, self.spellcheck, self.style, self.tabindex, self.title, self.translate]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Sup(HtmlTag):
    type     = []
    attributes   = ['class', 'height', 'id', 'style', 'viewBox', 'width', 'xmlns']
    name     = 'sup'
    self_closing = False
    nestable     = False

    def __init__(self, class_:str=None, height:str=None, id:str=None, style:str=None, viewBox:str=None, width:str=None, xmlns:str=None) -> None:
        super().__init__()
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.height: Attribute = Attribute(name='height', value=height)
        self.id: Attribute = Attribute(name='id', value=id)
        self.style: Attribute = Attribute(name='style', value=style)
        self.viewBox: Attribute = Attribute(name='viewBox', value=viewBox)
        self.width: Attribute = Attribute(name='width', value=width)
        self.xmlns: Attribute = Attribute(name='xmlns', value=xmlns)
        self.all = [self.class_, self.height, self.id, self.style, self.viewBox, self.width, self.xmlns]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Svg(HtmlTag):
    type     = []
    attributes   = ['align', 'bgcolor', 'border', 'cellpadding', 'cellspacing', 'class', 'dir', 'frame', 'height', 'id', 'lang', 'rules', 'style', 'summary', 'width']
    name     = 'svg'
    self_closing = False
    nestable     = False

    def __init__(self, align:str=None, bgcolor:str=None, border:str=None, cellpadding:str=None, cellspacing:str=None, class_:str=None, dir:str=None, frame:str=None, height:str=None, id:str=None, lang:str=None, rules:str=None, style:str=None, summary:str=None, width:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.bgcolor: Attribute = Attribute(name='bgcolor', value=bgcolor)
        self.border: Attribute = Attribute(name='border', value=border)
        self.cellpadding: Attribute = Attribute(name='cellpadding', value=cellpadding)
        self.cellspacing: Attribute = Attribute(name='cellspacing', value=cellspacing)
        self.class_: Attribute = Attribute(name='class', value=class_)
        self.dir: Attribute = Attribute(name='dir', value=dir)
        self.frame: Attribute = Attribute(name='frame', value=frame)
        self.height: Attribute = Attribute(name='height', value=height)
        self.id: Attribute = Attribute(name='id', value=id)
        self.lang: Attribute = Attribute(name='lang', value=lang)
        self.rules: Attribute = Attribute(name='rules', value=rules)
        self.style: Attribute = Attribute(name='style', value=style)
        self.summary: Attribute = Attribute(name='summary', value=summary)
        self.width: Attribute = Attribute(name='width', value=width)
        self.all = [self.align, self.bgcolor, self.border, self.cellpadding, self.cellspacing, self.class_, self.dir, self.frame, self.height, self.id, self.lang, self.rules, self.style, self.summary, self.width]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Table(HtmlTag):
    type     = ['content', 'form']
    attributes   = ['align', 'bgcolor', 'char', 'charoff', 'valign']
    name     = 'table'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, bgcolor:str=None, char:str=None, charoff:str=None, valign:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.bgcolor: Attribute = Attribute(name='bgcolor', value=bgcolor)
        self.char: Attribute = Attribute(name='char', value=char)
        self.charoff: Attribute = Attribute(name='charoff', value=charoff)
        self.valign: Attribute = Attribute(name='valign', value=valign)
        self.all = [self.align, self.bgcolor, self.char, self.charoff, self.valign]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Tbody(HtmlTag):
    type     = ['form']
    attributes   = ['abbr', 'align', 'axis', 'bgcolor', 'char', 'charoff', 'colspan', 'headers', 'height', 'nowrap', 'rowspan', 'scope', 'valign', 'width']
    name     = 'tbody'
    self_closing = False
    nestable     = False

    def __init__(self, abbr:str=None, align:str=None, axis:str=None, bgcolor:str=None, char:str=None, charoff:str=None, colspan:str=None, headers:str=None, height:str=None, nowrap:str=None, rowspan:str=None, scope:str=None, valign:str=None, width:str=None) -> None:
        super().__init__()
        self.abbr: Attribute = Attribute(name='abbr', value=abbr)
        self.align: Attribute = Attribute(name='align', value=align)
        self.axis: Attribute = Attribute(name='axis', value=axis)
        self.bgcolor: Attribute = Attribute(name='bgcolor', value=bgcolor)
        self.char: Attribute = Attribute(name='char', value=char)
        self.charoff: Attribute = Attribute(name='charoff', value=charoff)
        self.colspan: Attribute = Attribute(name='colspan', value=colspan)
        self.headers: Attribute = Attribute(name='headers', value=headers)
        self.height: Attribute = Attribute(name='height', value=height)
        self.nowrap: Attribute = Attribute(name='nowrap', value=nowrap)
        self.rowspan: Attribute = Attribute(name='rowspan', value=rowspan)
        self.scope: Attribute = Attribute(name='scope', value=scope)
        self.valign: Attribute = Attribute(name='valign', value=valign)
        self.width: Attribute = Attribute(name='width', value=width)
        self.all = [self.abbr, self.align, self.axis, self.bgcolor, self.char, self.charoff, self.colspan, self.headers, self.height, self.nowrap, self.rowspan, self.scope, self.valign, self.width]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Td(HtmlTag):
    type     = ['content', 'form']
    attributes   = ['content', 'id']
    name     = 'td'
    self_closing = False
    nestable     = True

    def __init__(self, content:str=None, id:str=None) -> None:
        super().__init__()
        self.content: Attribute = Attribute(name='content', value=content)
        self.id: Attribute = Attribute(name='id', value=id)
        self.all = [self.content, self.id]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.inner_content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.inner_content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.inner_content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Template(HtmlTag):
    type     = []
    attributes   = ['autocomplete', 'autofocus', 'cols', 'dirname', 'disabled', 'form', 'maxlength', 'minlength', 'name', 'placeholder', 'readonly', 'required', 'rows', 'wrap']
    name     = 'template'
    self_closing = False
    nestable     = False

    def __init__(self, autocomplete:str=None, autofocus:str=None, cols:str=None, dirname:str=None, disabled:str=None, form:str=None, maxlength:str=None, minlength:str=None, name:str=None, placeholder:str=None, readonly:str=None, required:str=None, rows:str=None, wrap:str=None) -> None:
        super().__init__()
        self.autocomplete: Attribute = Attribute(name='autocomplete', value=autocomplete)
        self.autofocus: Attribute = Attribute(name='autofocus', value=autofocus)
        self.cols: Attribute = Attribute(name='cols', value=cols)
        self.dirname: Attribute = Attribute(name='dirname', value=dirname)
        self.disabled: Attribute = Attribute(name='disabled', value=disabled)
        self.form: Attribute = Attribute(name='form', value=form)
        self.maxlength: Attribute = Attribute(name='maxlength', value=maxlength)
        self.minlength: Attribute = Attribute(name='minlength', value=minlength)
        self.name: Attribute = Attribute(name='name', value=name)
        self.placeholder: Attribute = Attribute(name='placeholder', value=placeholder)
        self.readonly: Attribute = Attribute(name='readonly', value=readonly)
        self.required: Attribute = Attribute(name='required', value=required)
        self.rows: Attribute = Attribute(name='rows', value=rows)
        self.wrap: Attribute = Attribute(name='wrap', value=wrap)
        self.all = [self.autocomplete, self.autofocus, self.cols, self.dirname, self.disabled, self.form, self.maxlength, self.minlength, self.name, self.placeholder, self.readonly, self.required, self.rows, self.wrap]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Textarea(HtmlTag):
    type     = ['content', 'meta']
    attributes   = ['align', 'bgcolor', 'char', 'charoff', 'valign']
    name     = 'textarea'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, bgcolor:str=None, char:str=None, charoff:str=None, valign:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.bgcolor: Attribute = Attribute(name='bgcolor', value=bgcolor)
        self.char: Attribute = Attribute(name='char', value=char)
        self.charoff: Attribute = Attribute(name='charoff', value=charoff)
        self.valign: Attribute = Attribute(name='valign', value=valign)
        self.all = [self.align, self.bgcolor, self.char, self.charoff, self.valign]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Tfoot(HtmlTag):
    type     = ['form']
    attributes   = ['abbr', 'align', 'axis', 'bgcolor', 'char', 'charoff', 'colspan', 'headers', 'height', 'nowrap', 'rowspan', 'scope', 'valign', 'width']
    name     = 'tfoot'
    self_closing = False
    nestable     = False

    def __init__(self, abbr:str=None, align:str=None, axis:str=None, bgcolor:str=None, char:str=None, charoff:str=None, colspan:str=None, headers:str=None, height:str=None, nowrap:str=None, rowspan:str=None, scope:str=None, valign:str=None, width:str=None) -> None:
        super().__init__()
        self.abbr: Attribute = Attribute(name='abbr', value=abbr)
        self.align: Attribute = Attribute(name='align', value=align)
        self.axis: Attribute = Attribute(name='axis', value=axis)
        self.bgcolor: Attribute = Attribute(name='bgcolor', value=bgcolor)
        self.char: Attribute = Attribute(name='char', value=char)
        self.charoff: Attribute = Attribute(name='charoff', value=charoff)
        self.colspan: Attribute = Attribute(name='colspan', value=colspan)
        self.headers: Attribute = Attribute(name='headers', value=headers)
        self.height: Attribute = Attribute(name='height', value=height)
        self.nowrap: Attribute = Attribute(name='nowrap', value=nowrap)
        self.rowspan: Attribute = Attribute(name='rowspan', value=rowspan)
        self.scope: Attribute = Attribute(name='scope', value=scope)
        self.valign: Attribute = Attribute(name='valign', value=valign)
        self.width: Attribute = Attribute(name='width', value=width)
        self.all = [self.abbr, self.align, self.axis, self.bgcolor, self.char, self.charoff, self.colspan, self.headers, self.height, self.nowrap, self.rowspan, self.scope, self.valign, self.width]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Th(HtmlTag):
    type     = ['content', 'form']
    attributes   = ['align', 'bgcolor', 'char', 'charoff', 'valign']
    name     = 'th'
    self_closing = False
    nestable     = True

    def __init__(self, align:str=None, bgcolor:str=None, char:str=None, charoff:str=None, valign:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.bgcolor: Attribute = Attribute(name='bgcolor', value=bgcolor)
        self.char: Attribute = Attribute(name='char', value=char)
        self.charoff: Attribute = Attribute(name='charoff', value=charoff)
        self.valign: Attribute = Attribute(name='valign', value=valign)
        self.all = [self.align, self.bgcolor, self.char, self.charoff, self.valign]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Thead(HtmlTag):
    type     = ['form']
    attributes   = ['datetime']
    name     = 'thead'
    self_closing = False
    nestable     = False

    def __init__(self, datetime:str=None) -> None:
        super().__init__()
        self.datetime: Attribute = Attribute(name='datetime', value=datetime)
        self.all = [self.datetime]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Time(HtmlTag):
    type     = ['semantic']
    attributes   = []
    name     = 'time'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Title(HtmlTag):
    type     = ['structural']
    attributes   = ['align', 'bgcolor', 'char', 'charoff', 'valign']
    name     = 'title'
    self_closing = False
    nestable     = False

    def __init__(self, align:str=None, bgcolor:str=None, char:str=None, charoff:str=None, valign:str=None) -> None:
        super().__init__()
        self.align: Attribute = Attribute(name='align', value=align)
        self.bgcolor: Attribute = Attribute(name='bgcolor', value=bgcolor)
        self.char: Attribute = Attribute(name='char', value=char)
        self.charoff: Attribute = Attribute(name='charoff', value=charoff)
        self.valign: Attribute = Attribute(name='valign', value=valign)
        self.all = [self.align, self.bgcolor, self.char, self.charoff, self.valign]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Tr(HtmlTag):
    type     = ['content', 'form']
    attributes   = ['default', 'kind', 'label', 'src', 'srclang']
    name     = 'tr'
    self_closing = False
    nestable     = True

    def __init__(self, default:str=None, kind:str=None, label:str=None, src:str=None, srclang:str=None) -> None:
        super().__init__()
        self.default: Attribute = Attribute(name='default', value=default)
        self.kind: Attribute = Attribute(name='kind', value=kind)
        self.label: Attribute = Attribute(name='label', value=label)
        self.src: Attribute = Attribute(name='src', value=src)
        self.srclang: Attribute = Attribute(name='srclang', value=srclang)
        self.all = [self.default, self.kind, self.label, self.src, self.srclang]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Track(HtmlTag):
    type     = ['void']
    attributes   = []
    name     = 'track'
    self_closing = True
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class U(HtmlTag):
    type     = []
    attributes   = ['type']
    name     = 'u'
    self_closing = False
    nestable     = False

    def __init__(self, type:str=None) -> None:
        super().__init__()
        self.type: Attribute = Attribute(name='type', value=type)
        self.all = [self.type]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Ul(HtmlTag):
    type     = ['content', 'table']
    attributes   = []
    name     = 'ul'
    self_closing = False
    nestable     = True

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Var(HtmlTag):
    type     = []
    attributes   = ['autoplay', 'controls', 'crossorigin', 'height', 'loop', 'muted', 'playsinline', 'poster', 'preload', 'src', 'width']
    name     = 'var'
    self_closing = False
    nestable     = False

    def __init__(self, autoplay:str=None, controls:str=None, crossorigin:str=None, height:str=None, loop:str=None, muted:str=None, playsinline:str=None, poster:str=None, preload:str=None, src:str=None, width:str=None) -> None:
        super().__init__()
        self.autoplay: Attribute = Attribute(name='autoplay', value=autoplay)
        self.controls: Attribute = Attribute(name='controls', value=controls)
        self.crossorigin: Attribute = Attribute(name='crossorigin', value=crossorigin)
        self.height: Attribute = Attribute(name='height', value=height)
        self.loop: Attribute = Attribute(name='loop', value=loop)
        self.muted: Attribute = Attribute(name='muted', value=muted)
        self.playsinline: Attribute = Attribute(name='playsinline', value=playsinline)
        self.poster: Attribute = Attribute(name='poster', value=poster)
        self.preload: Attribute = Attribute(name='preload', value=preload)
        self.src: Attribute = Attribute(name='src', value=src)
        self.width: Attribute = Attribute(name='width', value=width)
        self.all = [self.autoplay, self.controls, self.crossorigin, self.height, self.loop, self.muted, self.playsinline, self.poster, self.preload, self.src, self.width]
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Video(HtmlTag):
    type     = ['content']
    attributes   = []
    name     = 'video'
    self_closing = False
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}
        self.content = []

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")


class Wbr(HtmlTag):
    type     = ['void']
    attributes   = []
    name     = 'wbr'
    self_closing = True
    nestable     = False

    def __init__(self) -> None:
        super().__init__()
        self.all = []
        self.map = {key:value for key, value in zip(self.attributes, self.all)}

    def __call__(self):
        return self.__str__()
    
    def __dict__(self):
        self.map_values = [x.value for x in list(self.map.values())]
        self.map_names = [x.name for x in list(self.map.values())]
        return {key: value for key, value in zip(self.map_names, self.map_values)}

    def __str__(self) -> str:
        self.part1 = f"<{self.name}"
        self.attr_str = " ".join([f'{x.name}="{x.value}"' for index, x in enumerate(self.all) if x.value != None])
        self.part2 = f"</{self.name}>" if self.self_closing == False else " />"
        self._content = "\t\n".join(self.content) if self.nestable == True else ""
        self.string = f"{self.part1}{self.attr_str}>{self._content} {self.part2}"
        return self.string 

    def add_element(self, content:str) -> None:
        if self.nestable == True:
            self.content.append(content)
    
    def get_attribute(self, attribute: str) -> str:
        try:
            self.retv = self.map[attribute].value 
        except KeyError:
            self.retv = None 
        

    def configure(self, attribute:str, value: str) -> None:
        try:
            self.change: Attribute = self.map[attribute]
            self.change.value = value
            self.map[attribute] = self.change
        except KeyError:
            raise Exception(f"{attribute} is not a valid attribute for {self.name}")

AllTagClasses = [A, Abbr, Address, Area, Article, Aside, Audio, B, Base, Bdi, Bdo, Blockquote, Body, Br, Button, Canvas, Caption, Cite, Code, Col, Colgroup, Data, Datalist, Dd, Del, Details, Dfn, Dialog, Div, Dl, Dt, Em, Embed, Fieldset, Figcaption, Figure, Footer, Form, H1, H2, H3, H4, H5, H6, Head, Header, Hr, Html, I, Iframe, Img, Input, Ins, Kbd, Label, Legend, Li, Link, Main, Map, Mark, Meta, Meter, Nav, Noscript, Object, Ol, Optgroup, Option, Output, P, Param, Picture, Pre, Progress, Q, Rp, Rt, Ruby, S, Samp, Script, Section, Select, Small, Source, Span, Strong, Style, Sub, Summary, Sup, Svg, Table, Tbody, Td, Template, Textarea, Tfoot, Th, Thead, Time, Title, Tr, Track, U, Ul, Var, Video, Wbr]