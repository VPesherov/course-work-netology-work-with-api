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
        print(response)

    def upload_files(self, photos: dict = 1):
        method_name = f'{self.base_url}v1/disk/resources/upload'
        url = 'https://sun9-79.userapi.com/c10408/u4172580/-6/x_ee97448e.jpg'
        url1 = 'Загрузки'
        headers = self.get_headers()
        params = {'path': url1, 'url': url}
        response = requests.put(method_name, headers=headers, params=params)
        print(response.status_code)
        # for i in photos:
        #    print(i)

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response
