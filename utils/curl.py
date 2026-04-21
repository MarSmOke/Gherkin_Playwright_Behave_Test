import re
import requests

def parse_headers(curl_command):
    headers = {}
    matches = re.findall(r'(?:-H|--header)\s+["\']([^"\']+)["\']', curl_command)
    for header_line in matches:
        if ':' in header_line:
            k, v = header_line.split(':', 1)
            headers[k.strip()] = v.strip()
    return headers

def parse_payload(curl_command):
    method_match = re.search(r'(?:-X|--request)\s+(\w+)', curl_command)
    method = method_match.group(1).upper() if method_match else 'GET'
    url_match = re.search(r'[\'"]?(https?://[^\s\'"]+)[\'"]?', curl_command)
    url = url_match.group(1) if url_match else None
    return method, url

def execute_curl(curl_command):
    method, url = parse_payload(curl_command)
    headers = parse_headers(curl_command)
    if not url:
        raise ValueError("URL not found in curl command")
    response = requests.request(method, url, headers=headers)
    return response

def curl_resolver(context, curl_command):
    resolved = curl_command
    for key, value in context.__dict__.items():
        if isinstance(value, str):
            resolved = resolved.replace(f'{{{key}}}', value)
    return resolved

def compose_request_object(context, resolved_curl, response_name):
    if not hasattr(context, 'requests'):
        context.requests = {}
    context.requests[response_name] = resolved_curl

def compose_response_object(context, response_name, result):
    if not hasattr(context, 'responses'):
        context.responses = {}
    context.responses[response_name] = result
