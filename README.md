# html
Html python module for creating webpages programmatically. Has handy dataclasses for css properties and their available values. Has classes for every html tag.  classes: css.CSSRule, css.Property, element.Element, attribute.Attribute, element.Style, element.ElementStyle, and etc]


# Getting Started

```bash
# cd to your project directory
git clone https://github.com/Donny-GUI/html.git
```

# Usage

### Creating Elements

```python3
from html import css, element, properties, tags, attribute

body = element.Element("body")
button = element.Element("button", width=20, height=10)

```

### Creating CSS Rules and Properties

```python3
from html.css import Rule, Property
red = Property("color", "red")
button_css = Rule(selector='my-button', red)
button_css.get()
#my-button {
#    color: red;
#}

```

### Tag, Attribute and Tag type Data

```python3
from properties import Tag, Attributes, TagType

# demonstating dataclasses

print("all tags: ", Tag.tags)
print("self closing: ", Tag.self_closing)
print("types: ", Tag.types)
print("nestable tags: ", Tag.nestable)

print("=========")

# demonstrating Attributes dataclass

print("button attributes: ", Attributes.button)
print("script tag attributes: ", Attributes.script)

# Demonstrating TagType dataclass

print("article tag types: ", TagType.article)

```

### Getting CSS Information

```python3
from html.css import CSS, CSSRuleMap

print("all css rules: ", CSS.rules)
print("css colors: ", CSS.named_colors)
print("css color hex values: ", CSS.hex_colors)
print("css rule builtin values: ", CSS.rule_values)
print("css align-content properties: ", CSSRuleMap['align-content'])

```
