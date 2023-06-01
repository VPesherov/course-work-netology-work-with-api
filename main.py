from VkClass import VkApiHandler
from YaDiskClass import YaApiHandler
import os
from dotenv import load_dotenv
from pprint import pprint

def main():
    load_dotenv()
    vk_api_token = os.getenv('VK_API_TOKEN')
    vk_api_version = os.getenv('VERSION')
    user1 = VkApiHandler(vk_api_token, vk_api_version)
    data = user1.get_all_user_photos('1')
    photos_dict = user1.get_photos_with_max_size(data)
    pprint(photos_dict)
    ya_api_token = os.getenv('YA_API_TOKEN')
    user1 = YaApiHandler(ya_api_token)
    print(user1.get_files_list().json())
    print('-' * 30)
    print(user1.create_dir_on_disk())
    print('-' * 30)
    print(user1.upload_files())


if __name__ == '__main__':
    main()
