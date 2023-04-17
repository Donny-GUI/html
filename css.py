import dataclasses


@dataclasses.dataclass(slots=True)
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
    named_colors = [
    'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure',
    'beige', 'bisque', 'black', 'blanchedalmond', 'blue',
    'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse',
    'chocolate', 'coral', 'cornflowerblue', 'cornsilk',
    'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod',
    'darkgray', 'darkgrey', 'darkgreen', 'darkkhaki', 'darkmagenta',
    'darkolivegreen', 'darkorange', 'darkorchid', 'darkred',
    'darksalmon', 'darkseagreen', 'darkslateblue',
    'darkslategray', 'darkslategrey', 'darkturquoise', 'darkviolet',
    'deeppink', 'deepskyblue', 'dimgray', 'dimgrey', 'dodgerblue',
    'firebrick', 'floralwhite', 'forestgreen', 'fuchsia',
    'gainsboro', 'ghostwhite', 'gold', 'goldenrod', 'gray',
    'grey', 'green', 'greenyellow', 'honeydew', 'hotpink',
    'indianred', 'indigo', 'ivory', 'khaki', 'lavender',
    'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue',
    'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray',
    'lightgrey', 'lightgreen', 'lightpink', 'lightsalmon',
    'lightseagreen', 'lightskyblue', 'lightslategray',
    'lightslategrey', 'lightsteelblue', 'lightyellow', 'lime',
    'limegreen', 'linen', 'magenta', 'maroon', 'mediumaquamarine',
    'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen',
    'mediumslateblue', 'mediumspringgreen', 'mediumturquoise',
    'mediumvioletred', 'midnightblue', 'mintcream', 'mistyrose',
    'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive',
    'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod',
    'palegreen', 'paleturquoise', 'palevioletred', 'papayawhip',
    'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple',
    'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon',
    'sandybrown', 'seagreen', 'seashell', 'sienna', 'silver',
    'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow',
    'springgreen', 'steelblue', 'tan', 'teal', 'thistle',
    'tomato', 'turquoise', 'violet', 'wheat', 'white',
    'whitesmoke', 'yellow', 'yellowgreen'
    ]
    hex_colors = {
    'aliceblue': '#f0f8ff', 'antiquewhite': '#faebd7', 'aqua': '#00ffff',
    'aquamarine': '#7fffd4', 'azure': '#f0ffff', 'beige': '#f5f5dc',
    'bisque': '#ffe4c4', 'black': '#000000', 'blanchedalmond': '#ffebcd',
    'blue': '#0000ff', 'blueviolet': '#8a2be2', 'brown': '#a52a2a',
    'burlywood': '#deb887', 'cadetblue': '#5f9ea0', 'chartreuse': '#7fff00',
    'chocolate': '#d2691e', 'coral': '#ff7f50', 'cornflowerblue': '#6495ed',
    'cornsilk': '#fff8dc', 'crimson': '#dc143c', 'cyan': '#00ffff',
    'darkblue': '#00008b', 'darkcyan': '#008b8b', 'darkgoldenrod': '#b8860b',
    'darkgray': '#a9a9a9', 'darkgrey': '#a9a9a9', 'darkgreen': '#006400',
    'darkkhaki': '#bdb76b', 'darkmagenta': '#8b008b',
    'darkolivegreen': '#556b2f', 'darkorange': '#ff8c00',
    'darkorchid': '#9932cc', 'darkred': '#8b0000', 'darksalmon': '#e9967a',
    'darkseagreen': '#8fbc8f', 'darkslateblue': '#483d8b',
    'darkslategray': '#2f4f4f', 'darkslategrey': '#2f4f4f',
    'darkturquoise': '#00ced1', 'darkviolet': '#9400d3',
    'deeppink': '#ff1493', 'deepskyblue': '#00bfff', 'dimgray': '#696969',
    'dimgrey': '#696969', 'dodgerblue': '#1e90ff', 'firebrick': '#b22222',
    'floralwhite': '#fffaf0', 'forestgreen': '#228b22', 'fuchsia': '#ff00ff',
    'gainsboro': '#dcdcdc', 'ghostwhite': '#f8f8ff', 'gold': '#ffd700',
    'goldenrod': '#daa520', 'gray': '#808080', 'grey': '#808080',
    'green': '#008000', 'greenyellow': '#adff2f', 'honeydew': '#f0fff0',
    'hotpink': '#ff69b4', 'indianred': '#cd5c5c', 'indigo': '#4b0082',
    'ivory': '#fffff0', 'khaki': '#f0e68c', 'lavender': '#e6e6fa',
    'lavenderblush': '#fff0f5', 'lawngreen': '#7cfc00', 'lemonchiffon': '#fffacd',
    'lightblue': '#add8e6', 'lightcoral': '#f08080', 'lightcyan': '#e0ffff', 
    'lightgoldenrodyellow': '#fafad2', 'lightgray': '#d3d3d3',
    'lightgrey': '#d3d3d3', 'lightgreen': '#90ee90', 'lightpink': '#ffb6c1',
    'lightsalmon': '#ffa07a', 'lightseagreen': '#20b2aa', 'lightskyblue': '#87cefa',
    'lightslategray': '#778899', 'lightslategrey': '#778899', 'lightsteelblue': '#b0c4de',
    'lightyellow': '#ffffe0', 'lime': '#00ff00', 'limegreen': '#32cd32',
    'linen': '#faf0e6', 'magenta': '#ff00ff', 'maroon': '#800000',
    'mediumaquamarine': '#66cdaa', 'mediumblue': '#0000cd', 'mediumorchid': '#ba55d3',
    'mediumpurple': '#9370db', 'mediumseagreen': '#3cb371', 'mediumslateblue': '#7b68ee',
    'mediumspringgreen': '#00fa9a', 'mediumturquoise': '#48d1cc', 'mediumvioletred': '#c71585',
    'midnightblue': '#191970', 'mintcream': '#f5fffa', 'mistyrose': '#ffe4e1',
    'moccasin': '#ffe4b5', 'navajowhite': '#ffdead', 'navy': '#000080',
    'oldlace': '#fdf5e6', 'olive': '#808000', 'olivedrab': '#6b8e23',
    'orange': '#ffa500', 'orangered': '#ff4500', 'orchid': '#da70d6',
    'palegoldenrod': '#eee8aa', 'palegreen': '#98fb98', 'paleturquoise': '#afeeee',
    'palevioletred': '#db7093', 'papayawhip': '#ffefd5', 'peachpuff': '#ffdab9',
    'peru': '#cd853f', 'pink': '#ffc0cb', 'plum': '#dda0dd',
    'powderblue': '#b0e0e6', 'purple': '#800080', 'rebeccapurple': '#663399',
    'red': '#ff0000', 'rosybrown': '#bc8f8f', 'royalblue': '#4169e1',
    'saddlebrown': '#8b4513', 'salmon': '#fa8072', 'sandybrown': '#f4a460',
    'seagreen': '#2e8b57', 'seashell': '#fff5ee', 'sienna': '#a0522d',
    'silver': '#c0c0c0', 'skyblue': '#87ceeb', 'slateblue': '#6a5acd',
    'slategray': '#708090', 'slategrey': '#708090', 'snow': '#fffafa',
    'springgreen': '#00ff7f', 'steelblue': '#4682b4', 'tan': '#d2b48c',
    'teal': '#008080', 'thistle': '#d8bfd8', 'tomato': '#ff6347',
    'turquoise': '#40e0d0', 'violet': '#ee82ee', 'wheat': '#f5deb3',
    'white': '#ffffff', 'whitesmoke': '#f5f5f5', 'yellow': '#ffff00',
    'yellowgreen': '#9acd32'}
    rule_values = [
    'auto', 'none', 'initial', 'inherit', 'unset', 'normal', 'hidden', 'visible',
    'collapse', 'center', 'top', 'bottom', 'left', 'right', 'static', 'fixed',
    'absolute', 'relative', 'transparent', 'solid', 'dotted', 'dashed', 'double',
    'groove', 'ridge', 'inset', 'outset', 'thin', 'medium', 'thick', 'italic',
    'oblique', 'bold', 'bolder', 'lighter', 'smaller', 'larger', 'serif', 'sans-serif',
    'monospace', 'cursive', 'fantasy', 'capitalize', 'uppercase', 'lowercase',
    'nowrap', 'pre', 'pre-wrap', 'pre-line', 'baseline', 'middle', 'sub', 'super',
    'text-top', 'text-bottom', 'underline', 'overline', 'line-through', 'clip',
    'ellipsis', 'circle', 'decimal', 'decimal-leading-zero', 'lower-roman', 'upper-roman',
    'lower-greek', 'lower-latin', 'upper-latin', 'armenian', 'georgian', 'lower-alpha',
    'upper-alpha', 'hebrew', 'hiragana', 'hiragana-iroha', 'katakana', 'katakana-iroha',
    'inside', 'outside', 'no-repeat', 'repeat', 'repeat-x', 'repeat-y', 'scroll',
    'fixed', 'local', 'global', 'ltr', 'rtl', 'both', 'clear', 'block', 'inline',
    'inline-block', 'table', 'inline-table', 'table-row', 'table-column', 'table-cell',
    'table-caption', 'flex', 'inline-flex', 'column', 'row', 'wrap', 'nowrap', 'wrap-reverse',
    'row-reverse', 'column-reverse', 'stretch', 'baseline', 'center', 'flex-start',
    'flex-end', 'space-between', 'space-around', 'space-evenly', 'smooth', 'step-start',
    'step-end', 'steps', 'ease', 'ease-in', 'ease-out', 'ease-in-out', 'linear', 'alternate',
    'alternate-reverse', 'running', 'paused', 'infinite', 'both', 'horizontal', 'vertical',
    'uppercase', 'lowercase', 'none', 'full-width', 'full-size', 'contain', 'cover',
    'crosshair', 'default', 'pointer', 'move', 'text', 'wait', 'help', 'url', 'ltr',
    'rtl', 'inline', 'block', 'inline-block', 'none', 'visible', 'hidden', 'scroll',
    'always', 'avoid', 'break-word', 'nowrap', 'pre-wrap', 'pre-line', 'auto',
    'cross', 'not-allowed', 'pointer', 'progress', 'default', 'help', 'wait',
    'cell', 'column', 'row', 'nowrap', 'wrap', 'wrap-reverse', 'from-image', 'auto',
    'hidden', 'no-content', 'no-display', 'no-frames', 'no-paged', 'all', 'print',
    'screen', 'invert', 'grayscale', 'sepia', 'saturate', 'hue-rotate', 'opacity',
    'brightness', 'contrast', 'blur', 'drop-shadow', 'none', 'width', 'height',
    'min-width', 'max-width', 'min-height', 'max-height', 'margin', 'margin-top', 'margin-right',
    'margin-bottom', 'margin-left', 'padding', 'padding-top', 'padding-right', 'padding-bottom',
    'padding-left', 'border', 'border-top', 'border-right', 'border-bottom', 'border-left',
    'border-width', 'border-top-width', 'border-right-width', 'border-bottom-width', 'border-left-width',
    'border-style', 'border-top-style', 'border-right-style', 'border-bottom-style', 'border-left-style',
    'border-color', 'border-top-color', 'border-right-color', 'border-bottom-color', 'border-left-color',
    'border-radius', 'border-top-left-radius', 'border-top-right-radius', 'border-bottom-left-radius',
    'border-bottom-right-radius', 'outline', 'outline-width', 'outline-style', 'outline-color',
    'outline-offset', 'background', 'background-color', 'background-image', 'background-repeat',
    'background-position', 'background-size', 'background-clip', 'background-origin', 'background-attachment',
    'font', 'font-style', 'font-variant', 'font-weight', 'font-size', 'line-height', 'font-family',
    'color', 'text-align', 'text-decoration', 'text-transform', 'text-shadow', 'white-space',
    'overflow', 'overflow-x', 'overflow-y', 'z-index', 'position', 'top', 'right', 'bottom', 'left',
    'float', 'clear', 'display', 'visibility', 'direction', 'unicode-bidi', 'columns',
    'column-count','column-count', 'column-fill', 'column-gap', 'column-rule', 'column-rule-color',
    'column-rule-style', 'column-rule-width', 'column-span', 'content', 'counter-increment',
    'counter-reset', 'cursor', 'direction', 'display', 'empty-cells', 'filter', 'flex',
    'flex-basis', 'flex-direction', 'flex-flow', 'flex-grow', 'flex-shrink', 'flex-wrap',
    'float', 'font', 'font-family', 'font-feature-settings', 'font-kerning', 'font-language-override',
    'font-size', 'font-size-adjust', 'font-stretch', 'font-style', 'font-synthesis', 'font-variant',
    'font-variant-alternates', 'font-variant-caps', 'font-variant-east-asian', 'font-variant-ligatures',
    'font-variant-numeric', 'font-variant-position', 'font-weight', 'grid', 'grid-area', 'grid-auto-columns',
    'grid-auto-flow', 'grid-auto-rows', 'grid-column', 'grid-column-end', 'grid-column-gap', 'grid-column-start',
    'grid-gap', 'grid-row', 'grid-row-end', 'grid-row-gap', 'grid-row-start', 'grid-template',
    'grid-template-areas', 'grid-template-columns', 'grid-template-rows', 'hanging-punctuation', 'height',
    'hyphens', 'image-orientation', 'image-rendering', 'isolation', 'justify-content', 'justify-items',
    'justify-self', 'left', 'letter-spacing', 'line-break', 'line-height', 'list-style', 'list-style-image',
    'list-style-position', 'list-style-type', 'margin', 'margin-bottom', 'margin-left', 'margin-right',
    'margin-top', 'mask', 'mask-image', 'mask-mode', 'mask-position', 'mask-repeat', 'mask-size',
    'mask-type', 'max-height', 'max-width', 'min-height', 'min-width', 'mix-blend-mode', 'object-fit',
    'object-position', 'offset-distance', 'offset-path', 'offset-rotate', 'opacity', 'order', 'orphans',
    'outline', 'outline-color', 'outline-offset', 'outline-style', 'outline-width', 'overflow',
    'overflow-wrap', 'overflow-x', 'overflow-y', 'padding', 'padding-bottom', 'padding-left', 'padding-right',
    'padding-top', 'page-break-after', 'page-break-before', 'page-break-inside', 'perspective', 'perspective-origin',
    'pointer-events', 'position', 'quotes', 'resize', 'right', 'scroll-behavior', 'scroll-margin',
    'scroll-margin-block', 'scroll-margin-block-end', 'scroll-margin-block-start', 'scroll-margin-bottom',
    'scroll-margin-inline', 'scroll-margin-inline-end', 'scroll-margin-inline-start', 'scroll-margin-left',
    'scroll-margin-right', 'scroll-margin-top', 'scroll-padding', 'scroll-padding-block', 'scroll-padding-block-end',
    'scroll-padding-block-start', 'scroll-padding-bottom', 'scroll-padding-inline', 'scroll-padding-inline-end',
    'scroll-padding-inline-start', 'scroll-padding-left', 'scroll-padding-right', 'scroll-padding-top',
    'scroll-snap-align', 'scroll-snap-stop', 'scroll-snap-type', 'shape-image-threshold', 'shape-margin',
    'shape-outside', 'tab-size', 'table-layout', 'text-align', 'text-align-last', 'text-combine-upright',
    'text-decoration', 'text-decoration-color', 'text-decoration-line', 'text-decoration-skip',
    'text-decoration-skip-ink', 'text-decoration-style', 'text-emphasis', 'text-emphasis-color',
    'text-emphasis-position', 'text-emphasis-style', 'text-indent', 'text-justify', 'text-orientation',
    'text-overflow', 'text-rendering', 'text-shadow', 'text-size-adjust', 'text-transform', 'text-underline-position',
    'top', 'touch-action', 'transform', 'transform-box', 'transform-origin', 'transform-style', 'transition',
    'transition-delay', 'transition-duration', 'transition-property', 'transition-timing-function', 'unicode-bidi',
    'user-select', 'vertical-align', 'visibility', 'white-space', 'widows', 'width', 'will-change',
    'word-break', 'word-spacing', 'word-wrap', 'writing-mode', 'z-index']
    
    
class CSSRules:
    def get_values(self, rule: str):
        return CSSRuleMap[rule]


CSSRuleMap = {'align-content': ['center', 'flex-start', 'flex-end', 'space-between', 'space-around', 'stretch'], 'align-items': ['baseline', 'center', 'flex-end', 'flex-start', 'stretch'], 'align-self': ['auto', 'baseline', 'center', 'flex-end', 'flex-start', 'stretch'], 'animation': ['animation-name', 'animation-duration', 'animation-timing-function', 'animation-delay', 'animation-iteration-count', 'animation-direction', 'animation-fill-mode', 'animation-play-state'], 'backface-visibility': ['visible', 'hidden'], 'background': ['background-color', 'background-image', 'background-repeat', 'background-attachment', 'background-position', 'background-size'], 'border': ['border-width', 'border-style', 'border-color'], 'border-bottom': ['border-bottom-width', 'border-bottom-style', 'border-bottom-color'], 'border-bottom-color': ['color', 'transparent'], 'border-bottom-left-radius': ['length', 'percentage'], 'border-bottom-right-radius': ['length', 'percentage'], 'border-bottom-style': ['none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'], 'border-bottom-width': ['thin', 'medium', 'thick', 'length'], 'border-color': ['color', 'transparent'], 'border-left': ['border-left-width', 'border-left-style', 'border-left-color'], 'border-left-color': ['color', 'transparent'], 'border-left-style': ['none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'], 'border-left-width': ['thin', 'medium', 'thick', 'length'], 'border-radius': ['length', 'percentage'], 'border-right': ['border-right-width', 'border-right-style', 'border-right-color'], 'border-right-color': ['color', 'transparent'], 'border-right-style': ['none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'], 'border-right-width': ['thin', 'medium', 'thick', 'length'], 'border-style': ['none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'], 'border-top': ['border-top-width', 'border-top-style', 'border-top-color'], 'border-top-color': ['color', 'transparent'], 'border-top-left-radius': ['length', 'percentage'], 'border-top-right-radius': ['length', 'percentage'], 'border-top-style': ['none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'], 'border-top-width': ['thin', 'medium', 'thick', 'length'], 'bottom': ['auto', 'length', 'percentage'], 'box-shadow': ['none', 'h-shadow v-shadow blur spread color', 'inset h-shadow v-shadow blur spread color'], 'box-sizing': ['content-box', 'border-box'], 'caption-side': ['top', 'bottom'], 'clear': ['none', 'left', 'right', 'both'], 'clip': ['auto', 'shape'], 'color': ['color', 'transparent'], 'column-count': ['integer', 'auto'], 'column-gap': ['normal', 'length', 'percentage'], 'column-rule': ['column-rule-width', 'column-rule-style', 'column-rule-color'], 'column-rule-color': ['color', 'transparent'], 'column-rule-style': ['none', 'hidden', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'], 'column-rule-width': ['thin', 'medium', 'thick', 'length'], 'column-span': ['none', 'all'], 'column-width': ['auto', 'length', 'percentage'], 'content': ['normal', 'none', 'attr(attribute)', 'open-quote', 'close-quote', 'no-open-quote', 'no-close-quote', 'url(url)'], 'counter-increment': ['none', 'id number'], 'counter-reset': ['none', 'id number'], 'cue': ['cue-before', 'cue-after'], 'cue-after': ['attr()'], 'cue-before': ['none', 'url(url)'], 'cursor': ['alias', 'all-scroll', 'auto', 'cell', 'col-resize', 'context-menu', 'copy', 'crosshair', 'default', 'e-resize', 'ew-resize', 'grab', 'grabbing', 'help', 'move', 'n-resize', 'ne-resize', 'nesw-resize', 'no-drop', 'none', 'not-allowed', 'ns-resize', 'nw-resize', 'nwse-resize', 'pointer', 'progress', 'row-resize', 's-resize', 'se-resize', 'sw-resize', 'text', 'vertical-text', 'w-resize', 'wait', 'zoom-in', 'zoom-out'], 'direction': ['ltr', 'rtl'], 'display': ['block', 'contents', 'flex', 'grid', 'inline', 'inline-block', 'inline-flex', 'inline-grid', 'inline-table', 'list-item', 'none', 'run-in', 'table', 'table-caption', 'table-cell', 'table-column', 'table-column-group', 'table-footer-group', 'table-header-group', 'table-row', 'table-row-group'], 'empty-cells': ['hide', 'show'], 'filter': ['blur()', 'brightness()', 'contrast()', 'drop-shadow()', 'grayscale()', 'hue-rotate()', 'invert()', 'opacity()', 'saturate()', 'sepia()'], 'flex-basis': ['auto', 'content', 'fit-content', 'max-content', 'min-content', 'none'], 'flex-direction': ['column', 'column-reverse', 'row', 'row-reverse'], 'flex-grow': ['0', '1'], 'flex-shrink': ['0', '1'], 'flex-wrap': ['nowrap', 'wrap', 'wrap-reverse'], 'float': ['left', 'none', 'right'], 'font-family': ['font name', 'serif', 'sans-serif', 'monospace', 'cursive', 'fantasy'], 'font-size': ['xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large', 'smaller', 'larger'], 'font-style': ['normal', 'italic', 'oblique'], 'font-weight': ['normal', 'bold', 'bolder', 'lighter', '100', '200', '300', '400', '500', '600', '700', '800', '900'], 'height': ['auto', 'length', 'initial', 'inherit'], 'justify-content': ['center', 'flex-end', 'flex-start', 'space-around', 'space-between'], 'left': ['auto', 'length', 'initial', 'inherit'], 'letter-spacing': ['normal', 'length'], 'line-height': ['normal', 'number', 'length', 'initial', 'inherit'], 'list-style-image': ['none', 'url()'], 'list-style-position': ['inside', 'outside'], 'list-style-type': ['none', 'disc', 'circle', 'square', 'decimal', 'decimal-leading-zero', 'lower-roman', 'upper-roman', 'lower-greek', 'lower-latin', 'upper-latin', 'armenian', 'georgian', 'lower-alpha', 'upper-alpha', 'none'], 'margin': ['<length>', '<percentage>', 'auto'], 'margin-bottom': ['<length>', '<percentage>', 'auto'], 'margin-left': ['<length>', '<percentage>', 'auto'], 'margin-right': ['<length>', '<percentage>', 'auto'], 'margin-top': ['<length>', '<percentage>', 'auto'], 'max-height': ['<length>', '<percentage>', 'none'], 'max-width': ['<length>', '<percentage>', 'none'], 'min-height': ['<length>', '<percentage>', 'auto'], 'min-width': ['<length>', '<percentage>', 'auto'], 'opacity': ['<number>'], 'order': ['<integer>'], 'outline-color': ['<color>', 'invert'], 'outline-style': ['none', 'dotted', 'dashed', 'solid', 'double', 'groove', 'ridge', 'inset', 'outset'], 'outline-width': ['<length>', 'thin', 'medium', 'thick'], 'overflow': ['visible', 'hidden', 'scroll', 'auto'], 'padding': ['<length>', '<percentage>'], 'padding-bottom': ['<length>', '<percentage>'], 'padding-left': ['<length>', '<percentage>'], 'padding-right': ['<length>', '<percentage>'], 'padding-top': ['<length>', '<percentage>'], 'page-break-after': ['auto', 'always', 'avoid', 'left', 'right'], 'page-break-before': ['auto', 'always', 'avoid', 'left', 'right'], 'page-break-inside': ['auto', 'avoid'], 'perspective-origin': ['x-axis', 'y-axis', 'z-axis', 'length', 'initial', 'inherit'], 'pointer-events': ['auto', 'none', 'visiblePainted', 'visibleFill', 'visibleStroke', 'visible', 'painted', 'fill', 'stroke', 'all', 'inherit'], 'position': ['static', 'relative', 'absolute', 'fixed', 'sticky', 'initial', 'inherit'], 'quotes': ['none', 'initial', 'inherit', 'auto', 'string'], 'resize': ['none', 'both', 'horizontal', 'vertical', 'initial', 'inherit'], 'right': ['auto', 'length', 'initial', 'inherit'], 'table-layout': ['auto', 'fixed', 'inherit'], 'text-align': ['left', 'right', 'center', 'justify', 'initial', 'inherit'], 'text-align-last': ['auto', 'left', 'right', 'center', 'justify', 'start', 'end', 'initial', 'inherit'], 'text-decoration': ['none', 'underline', 'overline', 'line-through', 'blink'], 'text-decoration-color': ['color', 'transparent'], 'text-decoration-line': ['none', 'underline', 'overline', 'line-through', 'blink'], 'text-decoration-style': ['solid', 'double', 'dotted', 'dashed', 'wavy'], 'text-indent': ['length', 'percentage', 'inherit'], 'text-justify': ['auto', 'inter-word', 'inter-character', 'none'], 'text-overflow': ['clip', 'ellipsis', 'string'], 'text-shadow': ['h-shadow v-shadow blur-radius color', 'none', 'initial', 'inherit'], 'text-transform': ['none', 'capitalize', 'uppercase', 'lowercase', 'initial', 'inherit'], 'top': ['auto', 'length', 'initial', 'inherit'], 
'transform': ['none', 'matrix()', 'matrix3d()', 'translate()', 'translate3d()', 'translateX()', 'translateY()', 'translateZ()', 'scale()', 'scale3d()', 'scaleX()', 'scaleY()', 'scaleZ()', 'rotate()', 'rotate3d()', 'rotateX()', 'rotateY()', 'rotateZ()', 'skew()', 'skewX()', 'skewY()', 'perspective()'], 'unicode-bidi': ['normal', 'embed', 'isolate', 'bidi-override', 'isolate-override', 'plaintext'], 'vertical-align': ['baseline', 'sub', 'super', 'text-top', 'text-bottom', 'middle', 'top', 'bottom'], 'visibility': ['visible', 'hidden', 'collapse'], 'white-space': ['normal', 'nowrap', 'pre', 'pre-wrap', 'pre-line', 'break-spaces'], 'widows': ['<integer>'], 'width': ['<length>', '<percentage>', 'auto'], 'word-break': ['normal', 'break-all', 'keep-all', 'break-word'], 'word-spacing': ['normal', '<length>'], 'word-wrap': ['normal', 'break-word'], 'writing-mode': ['horizontal-tb', 'vertical-rl', 'vertical-lr', 'sideways-rl', 'sideways-lr', 'sideways', 'horizontal-bt'], 'z-index': ['auto', '<integer>']}


class CSSObject:
    pass


class Property(CSSObject):
    def __init__(self, name:str, value:str) -> None:
        self.name: str = name
        self.value: str = value
    

class Rule(CSSObject):
    def __init__(self, selector:str,  property:Property) -> None:
        self.selector = selector
        self.properties = {}
        self.properties[property.name] = property.value
        self.__properties = [property]
    
    def add_property(self, name:Property.name, value: Property.name):
        self.new_property = Property(name, value)
        self.__properties.append(self.new_property)
        self.properties[self.new_property.name] = self.new_property.value
    
    def change_value(self, name: Property.name, value: Property.value):
        self.new_property = Property(name, value)
        self.properties[self.new_property.name] = self.new_property.value
        
    def change_selector(self, name:str):
        self.selector = name
    
    def get(self) -> str:
        self.prop_strings = [f"\n\t{x}: {self.properties[x]};" for x in self.properties.keys()]
        self.property_string = "".join(self.prop_strings)
        self.rbracket = "{"
        self.lbracket = "}"
        return f"{self.selector}{self.rbracket}{self.property_string}\n{self.lbracket}"        

