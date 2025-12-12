import json


def read_large_file(file_path):
    """
    Reads a large text file line by line and returns the content as a single string.
    Args:
        file_path (str): Path to the input text file.
    Returns:
        str: Content of the file as a single string.
    """
    content = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                content.append(line)
    except UnicodeDecodeError:
        print(f"Error: The file {file_path} contains non-UTF-8 characters.")
        return None
    return ''.join(content)


def write_json_file(content, output_path):
    """
    Writes the given content to a JSON file with a single key 'content'.
    Args:
        content (str): Content to be written to the JSON file.
        output_path (str): Path to the output JSON file.
    """
    data = {"content": content}
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def convert_text_to_json(input_path, output_path):
    """
    Converts the content of a text file to a JSON file.
    Args:
        input_path (str): Path to the input text file.
        output_path (str): Path to the output JSON file.
    """
    content = read_large_file(input_path)
    if content is None:
        content = ""
    write_json_file(content, output_path)


if __name__ == "__main__":
    input_file = "example.txt"
    output_file = "example.json"
    convert_text_to_json(input_file, output_file)
