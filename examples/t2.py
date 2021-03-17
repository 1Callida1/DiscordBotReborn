import vk_api
from vk_audio import audio
import urllib.request

login = '79994461067'  # Номер телефона
password = 'Slololoshka123'  # Пароль
my_id = '601203289'

def auth_handler():
    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device

vk_session = vk_api.VkApi(login=login, password=password, auth_handler=auth_handler)
vk_session.auth()
audio_obj = audio(vk_session)

map_audio_object = audio_obj.get(need_list=True)
for _audio in map_audio_object:
    urllib.request.urlretrieve(_audio.url, "{}-{}.mp3".format(_audio.title, _audio.artist))