import sys
from sys_enviroment import *

def to_usever(verval):
    path_val = get_env("Anaconda", user= True)

    path_list = set(path_val.split(';'))

    newpathstr = ""
    find_str = "anaconda"
    for path in path_list:
        lc_path = path.lower()

        pos = lc_path.find(find_str)
        if (pos > 0):
            old_v = path[pos+ len(find_str)]

            if old_v.isdigit():
                path_list = list(path)
                path_list[pos+ len(find_str)] = str(verval)

                path = ""
                for ch in path_list:
                    path += ch

        newpathstr += path + ";"

    newpathstr.rstrip(";")

    isright = input("new python is (y/n?) " + newpathstr)
    if (isright.lower() == 'y'):
        set_env("Anaconda", newpathstr, True)

if __name__ == '__main__':
    if (len(sys.argv) != 2 or (sys.argv[1] != str(2) and sys.argv[1] != str(3))):
        print("Usage python change_pythonver.py <2, 3> for anaconda2,3")
    else:
        to_usever(int(sys.argv[1]))



