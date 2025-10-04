from urllib.parse import urlparse, parse_qs

def get_all_filter_parameters(url):
    parsed_url = urlparse(url)
    return parse_qs(parsed_url.query)

