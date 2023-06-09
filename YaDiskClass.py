import requests
from tqdm import tqdm


class YaApiHandler:
    base_url = 'https://cloud-api.yandex.net/'

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_dir_on_disk(self, dir_name='new_folder'):
        method_name = f'{self.base_url}v1/disk/resources'
        headers = self.get_headers()
        params = {'path': f'/{dir_name}'}
        response = requests.put(method_name, headers=headers, params=params)

        if response.status_code == 409:
            print(f'Данные будут записаны в директорию /{dir_name}')
        elif response.status_code == 201:
            print(f'Директория /{dir_name} была успешно создана')
        else:
            exit(f'Произошла ошибка при создании директории.\n Код ошибки {response.status_code}')
        return response

    def upload_files(self, url, file_name, dir_name=''):
        method_name = f'{self.base_url}v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': f'{dir_name}/{file_name}', 'url': url}
        response = requests.post(method_name, headers=headers, params=params)
        return response
        # for i in photos:
        #    print(i)

    def get_files_list_in_dir(self, dir_name):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': dir_name, 'limit': 100000}
        response = requests.get(files_url, headers=headers, params=params)
        return response

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        params = {'limit': 10000000}
        response = requests.get(files_url, headers=headers, params=params)
        return response

    @staticmethod
    def append_in_dict(json_dict, response, key, value, flag=0):
        file_name = f'{value[0]}.jpg'
        if flag == 1:
            file_name = f'{value[0]}.{value[1]}'

        if response.status_code != 202:
            print(f'\nПроизошла ошибка при загрузки файла {key}.\n Код ошибки {response.status_code}')
        else:
            json_dict['items'].append({"file_name": f'{file_name}', "size": f'{value[2]}'})
        return json_dict

    def upload_vk_photos_and_return_json(self, photos_dict, dir_name):
        print('Начинаем загрузку фотографий и создание json файла')

        json_dict = {"items": []}

        for key, value in tqdm(photos_dict.items()):
            all_files = self.get_files_list_in_dir(dir_name).json()
            for file in all_files['_embedded']['items']:
                if file['name'] == str(value[0]) + '.jpg':
                    response = self.upload_files(key, f'{value[0]}.{value[1]}.jpg', dir_name)
                    json_dict = self.append_in_dict(json_dict, response, key, value, 1)
                    # заменено на функцию
                    # if response.status_code != 202:
                    #     print(f'\nПроизошла ошибка при загрузки файла {key}.\n Код ошибки {response.status_code}')
                    # else:
                    #     json_dict['items'].append({"file_name": f'{value[0]}.{value[1]}.jpg', "size": f'{value[2]}'})
                    break
            else:
                response = self.upload_files(key, f'{value[0]}.jpg', dir_name)
                json_dict = self.append_in_dict(json_dict, response, key, value, 0)
                # заменено на функцию
                # if response.status_code != 202:
                #     print(f'\nПроизошла ошибка при загрузки файла {key}.\n Код ошибки {response.status_code}')
                # else:
                #     json_dict['items'].append({"file_name": f'{value[0]}.jpg', "size": f'{value[2]}'})

        print('Фотографии были загружены')

        return json_dict
