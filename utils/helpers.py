from urllib.parse import urlparse, parse_qs
import re

def get_all_filter_parameters(url):
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)

def extract_accent_color(element):
    style = element.get_attribute('style')
    if not style:
        return None
    match = re.search(r'--image-result-accent:\s*(#[0-9A-F]{6})', style, re.IGNORECASE)
    return match.group(1).upper() if match else None

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def is_blue_range(hex_color):
    r, g, b = hex_to_rgb(hex_color)
    return b > 150 and r < 120 and g < 180


def parse_dimensions(dimension_text):
    dimension_text = dimension_text.strip()
    match = re.search(r'(\d+)\s*[×x*]\s*(\d+)', dimension_text)
    if match:
        width = int(match.group(1))
        height = int(match.group(2))
        return width, height
    return None, None