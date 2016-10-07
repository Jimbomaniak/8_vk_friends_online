import vk
import getpass


APP_ID = 5658426  # чтобы получить app_id, нужно зарегистрировать своё приложение на https://vk.com/dev


def get_user_login():
    login = input('enter your login in vk.com: ')
    return login


def get_user_password():
    password = getpass.getpass('enter your password in vk.com: ')
    return password


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password,
        scope='friends',
    )
    api = vk.API(session)
    friends_online_ids = api.friends.getOnline()
    friends_online_info = api.users.get(user_ids=friends_online_ids)
    return friends_online_info


def output_friends_to_console(friends_online):
    print('This friends are online:')
    for user in friends_online:
        print('{first_name} {last_name}'.format(**user))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
