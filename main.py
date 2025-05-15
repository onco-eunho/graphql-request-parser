import os

from functions import extract_query_block, parse_query_fields, parse_graphql_keys, open_raw_file, save_parsed_file
from constants import START_MESSAGE, FINISH_MESSAGE, ERROR_MESSAGE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    try:
        print(START_MESSAGE)

        input_path: str = os.path.join(BASE_DIR, "input", "raw_data.txt")
        raw_data: str = open_raw_file(input_path)

        query_block: str = extract_query_block(raw_data)
        field_paths: str = parse_query_fields(query_block)
        graphql_fields: list = parse_graphql_keys("\n".join(field_paths))

        output_path: str = os.path.join(BASE_DIR, "output", "parsed.txt")
        save_parsed_file(output_path, graphql_fields)

        print(FINISH_MESSAGE)
    except Exception as e:
        print(f"{ERROR_MESSAGE, e}")