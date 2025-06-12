### There will be a list of JSON objects such as - [{"a": 3, "b": 2, "c": 5}, {"a": 2, "b": 3}, {"c": 5}]. The output will be a JSON object as - {"a": 5, "b": 5, "c": 10}

def json_sum(my_arr: list) -> object:
    freq_json = {}
    for obj in my_arr:
        for keys, values in obj.items():
            if keys in freq_json.keys():
                freq_json[keys] += values
            else:
                freq_json[keys] = values
    
    return freq_json

print(json_sum([{"a": 13, "b": 2, "c": 5}, {"a": 2, "b": 33}, {"c": 5}]))