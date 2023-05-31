from VkClass import VkApiHandler
import os
from dotenv import load_dotenv
from pprint import pprint

def main():
    load_dotenv()
    vk_api_token = os.getenv('VK_API_TOKEN')
    vk_api_version = os.getenv('VERSION')
    user1 = VkApiHandler(vk_api_token, vk_api_version)
    data = user1.get_all_user_photos('1')
    pprint(data)


if __name__ == '__main__':
    main()
