import sys, os
import glob

REMOVE = True

def usage():
    print('usage: python3 cleaner.py <path>\nRepo: https://github.com/HenryQuan/folder-cleaner')

def clean(path: str):
    # never mess with the system
    if "C:\Windows" in path:
        return

    try:
        if os.path.exists(path):
            folder_path = os.path.join(path, '*')
            # check if there are anything inside
            if len(os.listdir(path)) == 0:
                if REMOVE:
                    os.removedirs(path)
                    print('Removed - {}'.format(path))
                else:
                    print(path)
            else:
                # Visit subfolders
                for d in glob.glob(folder_path):
                    if os.path.isdir(d):
                        new_path = os.path.join(path, d)
                        clean(new_path)
    except PermissionError:
        print("Permission denied - {}".format(path))
    except:
        print("Unknown error - {}".format(path))

# cleaner
length = len(sys.argv)
if length > 1:
    path = sys.argv[1]
    path = path.replace("\"", "")
    print("Start cleaning from {}".format(path))
    clean(os.path.join(path, ""))
else:
    usage()