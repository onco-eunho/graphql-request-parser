import os
import re

from constants import UTF_8, UNICODE_ESCAPE, GRAPHQL_QUERY_ERROR_MESSAGE, GRAPHQL_BLOCK_ERROR_MESSAGE


def open_raw_file(file_path: str) -> str:
    with open(file_path, "r", encoding=UTF_8) as f:
        raw = f.read()
    return raw

def save_parsed_file(file_path: str, data: list):
    directory = os.path.dirname(file_path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    with open(file_path, "w", encoding=UTF_8) as f:
        for path in data:
            f.write(f"{path}\n")

def extract_query_block(raw_str: str) -> str:
    raw_str = raw_str.encode(UTF_8).decode(UNICODE_ESCAPE)

    match = re.search(r'"query"\s*:\s*"(.*?)"\s*,\s*"variables"', raw_str, re.DOTALL)
    if not match:
        raise ValueError(GRAPHQL_BLOCK_ERROR_MESSAGE)
    return match.group(1)

def parse_query_fields(block: str, indent=0):
    lines = block.strip().splitlines()
    stack = []
    result = []

    for line in lines:
        line = line.strip()
        if not line or line.startswith("query "):
            continue

        if line.endswith('{'):
            field = line[:-1].strip()
            stack.append(field)
        elif line == '}':
            if stack:
                stack.pop()
        else:
            full_path = '.'.join(stack + [line])
            result.append(full_path)
    return result

def parse_graphql_keys(raw: str) -> list:
    gql = bytes(raw, UTF_8).decode(UNICODE_ESCAPE)
    body_match = re.search(r'{([\s\S]+)}\s*$', gql)
    if not body_match:
        raise ValueError(GRAPHQL_QUERY_ERROR_MESSAGE)
    body = body_match.group(1)

    lines = body.strip().splitlines()
    stack = []
    result = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if line.endswith('{'):
            field = line[:-1].strip()
            field_name = field.split('(')[0]
            stack.append(field_name)
            result.append('.'.join(stack))
        elif line == '}':
            if stack:
                stack.pop()
        else:
            field_name = line.split('(')[0].split()[0]
            result.append('.'.join(stack + [field_name]))

    return result