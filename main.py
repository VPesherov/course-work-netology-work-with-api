from VkClass import VkApiHandler
from YaDiskClass import YaApiHandler
import os
from dotenv import load_dotenv
from pprint import pprint
import json
from tqdm import tqdm


def main():
    load_dotenv()

    json_dict = {"items": []}

    vk_api_token = os.getenv('VK_API_TOKEN')
    vk_api_version = os.getenv('VERSION')

    dir_name = 'vk_photo'

    user1 = VkApiHandler(vk_api_token, vk_api_version)
    owner_id = input('Введите id пользователя: ')
    count = input('Введите нужное количество фотографий: ')
    response = user1.get_all_user_photos(owner_id=owner_id, count=count)
    if response.status_code != 200:
        exit(f'Произошла ошибка при получении фотографий.\n Код ошибки {response.status_code}')
    photos_dict = user1.get_photos_with_max_size(response.json())
    print('Получен словарь с фотографиями максимального разрешения')
    # pprint(photos_dict)
    # ya_api_token = os.getenv('YA_API_TOKEN')
    ya_api_token = input('Введите токен яндекс диска: ')
    user1 = YaApiHandler(ya_api_token)
    response = user1.create_dir_on_disk(dir_name=dir_name)

    if response.status_code == 409:
        print(f'Данные будут записаны в директорию /{dir_name}')
    elif response.status_code == 201:
        print(f'Директория /{dir_name} была успешно создана')
    else:
        exit(f'Произошла ошибка при создании директории.\n Код ошибки {response.status_code}')

    print('Начинаем загрузку фотографий')

    for key, value in tqdm(photos_dict.items()):
        all_files = user1.get_files_list().json()
        for file in all_files['items']:
            if dir_name != '':
                temp_path = dir_name + '/'
            else:
                temp_path = ''
            if file['path'] == f'disk:/{temp_path}{value[0]}.jpg':
                response = user1.upload_files(key, f'{value[0]}.{value[1]}.jpg', dir_name)
                if response.status_code != 202:
                    print(f'Произошла ошибка при загрузки файла {key}.\n Код ошибки {response.status_code}')
                else:
                    json_dict['items'].append({"file_name": f'{value[0]}.{value[1]}.jpg', "size": f'{value[2]}'})
                break
        else:
            response = user1.upload_files(key, f'{value[0]}.jpg', dir_name)
            if response.status_code != 202:
                print(f'Произошла ошибка при загрузки файла {key}.\n Код ошибки {response.status_code}')
            else:
                json_dict['items'].append({"file_name": f'{value[0]}.jpg', "size": f'{value[2]}'})
    print('Фотографии были загружены')
    print('Создаём json файл')
    with open('result.json', 'w') as f:
        json.dump(json_dict, f)
    print('Записали данные в json файл с названием result.json')
    print('Работа программы окончена')


if __name__ == '__main__':
    main()
