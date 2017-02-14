from os import system, environ
import win32con
from win32gui import SendMessage
from winreg import (
    CloseKey, OpenKey, QueryValueEx, SetValueEx,
    HKEY_CURRENT_USER, HKEY_LOCAL_MACHINE,
    KEY_ALL_ACCESS, KEY_READ, REG_EXPAND_SZ, REG_SZ
)

def env_keys(user=True):
    if user:
        root = HKEY_CURRENT_USER
        subkey = 'Environment'
    else:
        root = HKEY_LOCAL_MACHINE
        subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    return root, subkey

# find the environ variable = name
def get_env(name, user=True):
    root, subkey = env_keys(user)
    try:
        key = OpenKey(root, subkey, 0, KEY_READ)

        value, _ = QueryValueEx(key, name)
    except WindowsError:
        return ''
    return value


def set_env(name, value, user = True):
    root, subkey = env_keys(user)

    with OpenKey(root, subkey, 0, KEY_ALL_ACCESS) as key:
        try:
            SetValueEx(key, name, 0, REG_EXPAND_SZ, value)

            SendMessage(
                win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Environment')
        except WindowsError as e:
            print(e)
        finally:
            CloseKey(key)



