import requests


class VkApiHandler:
    base_url = 'https://api.vk.com/method/'

    def __init__(self, access_token, version='5.131'):
        self.params = {
            'access_token': access_token,
            'v': version
        }

    def get_all_user_photos(self, owner_id, album_id='profile', extended='1'):
        method_name = f'{self.base_url}photos.get'
        params = {'owner_id': owner_id, 'album_id': album_id, 'extended': extended, **self.params}
        response = requests.get(url=method_name, params=params)
        data = response.json()
        return data
