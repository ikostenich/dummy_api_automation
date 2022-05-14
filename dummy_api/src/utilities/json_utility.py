import logging as logger
from jsonpath_ng import parse


def extract_json(json_string, json_path):
    try:
        response_json = json_string
        jsonpath_expression = parse(json_path)
        result = [match.value for match in jsonpath_expression.find(response_json)]
        return result[0] if len(result) == 1 else result
    except LookupError:
        logger.error(f'{json_path} is not in response json path' + json_string)
        return None
