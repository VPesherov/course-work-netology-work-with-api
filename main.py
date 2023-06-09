from JsonClass import JsonClass
from VkClass import VkApiHandler
from YaDiskClass import YaApiHandler
import os
from dotenv import load_dotenv
from pprint import pprint



def main():
    load_dotenv()
    dir_name = 'vk_photo'

    vk_api_token = os.getenv('VK_API_TOKEN')
    vk_api_version = os.getenv('VERSION')

    user1 = VkApiHandler(vk_api_token, vk_api_version)
    owner_id = input('Введите id пользователя: ')
    count = input('Введите нужное количество фотографий: ')

    photos = user1.get_all_user_photos(owner_id=owner_id, count=count)
    # print(photos)
    photos_dict = user1.get_photos_with_max_size(photos)
    # pprint(photos_dict)
    # ya_api_token = os.getenv('YA_API_TOKEN')
    ya_api_token = input('Введите токен яндекс диска: ')

    user1 = YaApiHandler(ya_api_token)
    user1.create_dir_on_disk(dir_name=dir_name)
    json_dict = user1.upload_vk_photos_and_return_json(photos_dict, dir_name)

    user1 = JsonClass()
    user1.create_json_file(json_dict)

    print('Работа программы окончена')


if __name__ == '__main__':
    main()
