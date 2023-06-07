import json


class JsonClass:
    def create_json_file(self, json_dict):
        print('Записываем информацию в json файл')
        with open('result.json', 'w') as f:
            json.dump(json_dict, f)
        print('Записали данные в json файл с названием result.json')
