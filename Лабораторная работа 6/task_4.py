import json

def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    ...  # TODO реализовать конвертер из csv в json
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.rstrip(new_line).split(delimiter))

        headers = lines[0]
        rows = lines[1:]

        dict_list = [{headers[i]: value for i, value in enumerate(row)} for row in rows]

        return(dict_list)


INPUT_FILE = "input.csv"

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
