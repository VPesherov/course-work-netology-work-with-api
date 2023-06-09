import requests
from pprint import pprint


class VkApiHandler:
    base_url = 'https://api.vk.com/method/'

    def __init__(self, access_token, version='5.131'):
        self.params = {
            'access_token': access_token,
            'v': version
        }

    def get_photos_with_max_size(self, photos):
        photos_dict = {}  # url : (likes, date, size_photo)
        photo_types = 'wzyrqpoxms'
        for photo in photos['response']['items']:
            date = photo['date']
            flag = False
            for photo_type in photo_types:
                # print(photo_type, end="")
                for size in photo["sizes"]:
                    size_photo = size['type']
                    if size_photo == photo_type:
                        url = size['url']
                        flag = True
                        break
                if flag is True:
                    break

            photos_dict[url] = (photo['likes']['count'], date, size_photo)

        print('Получен словарь с фотографиями максимального разрешения')
        return photos_dict

    def get_all_user_photos(self, owner_id, count, album_id='profile', extended='1'):
        method_name = f'{self.base_url}photos.get'
        params = {'count': count, 'owner_id': owner_id, 'album_id': album_id, 'extended': extended, **self.params}
        response = requests.get(url=method_name, params=params)
        if response.status_code != 200:
            exit(f'Произошла ошибка при получении фотографий.\n Код ошибки {response.status_code}')
        return response.json()
