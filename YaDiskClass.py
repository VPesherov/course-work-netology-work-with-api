import requests


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
        return response

    def upload_files(self, url, file_name, dir_name=''):
        method_name = f'{self.base_url}v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': f'{dir_name}/{file_name}', 'url': url}
        response = requests.post(method_name, headers=headers, params=params)
        return response
        # for i in photos:
        #    print(i)

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        params = {'limit': 10000000}
        response = requests.get(files_url, headers=headers, params=params)
        return response
