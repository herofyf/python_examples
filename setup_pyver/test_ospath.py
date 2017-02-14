import sys
from sys_enviroment import *

import win32api, win32con, win32security, ntsecuritycon

root = win32con.HKEY_LOCAL_MACHINE
subkey = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'

sys_path = get_env("PATH", False)

new_privs = ((win32security.LookupPrivilegeValue('',ntsecuritycon.SE_SECURITY_NAME),win32con.SE_PRIVILEGE_ENABLED),
             (win32security.LookupPrivilegeValue('',ntsecuritycon.SE_TCB_NAME),win32con.SE_PRIVILEGE_ENABLED),
             (win32security.LookupPrivilegeValue('', ntsecuritycon.SE_SYSTEM_ENVIRONMENT_NAME), win32con.SE_PRIVILEGE_ENABLED))

ph = win32api.GetCurrentProcess()
# to get current process security token
th = win32security.OpenProcessToken(ph,win32security.TOKEN_ALL_ACCESS|win32con.TOKEN_ADJUST_PRIVILEGES)
# to change new privilege
win32security.AdjustTokenPrivileges(th,0,new_privs)

'''

'''


hkey=win32api.RegOpenKey(root, subkey,0,win32con.KEY_ALL_ACCESS)
win32api.SetValueEx(hkey, "PATH", 0, win32api.REG_EXPAND_SZ, sys_path)
win32api.RegCloseKey(hkey)


# the following would be change the registery key secutity token object value. when there had operation on it,
# this object properties would be checked with operation owner
if False:
    admin_sid = win32security.LookupAccountName('','Administrator')[0]
    # what kind of operations
    sacl=win32security.ACL()
    sacl.Initialize()
    sacl.AddAuditAccessAce(win32security.ACL_REVISION,win32con.GENERIC_ALL,admin_sid,1,1)

    # who can access
    sd=win32security.SECURITY_DESCRIPTOR()
    sd.Initialize()
    sd.SetSecurityDescriptorOwner(admin_sid, False)
    sd.SetSecurityDescriptorSacl(1,sacl,1)
    win32api.RegSetKeySecurity(hkey,win32con.SACL_SECURITY_INFORMATION,sd)
    # win32security.SetFileSecurity(path, win32security.DACL_SECURITY_INFORMATION, sd)





#set_env("PATH", sys_path, False)