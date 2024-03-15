import os
import shutil


def clear(img_name):
    path_1 = "image/" + img_name + ".jpg"  # this is image file
    path_2 = "detect/" + img_name  # this is folder contain sub files

    # remove path1 and path2(want to remove all contains)
    if os.path.exists(path_1):
        os.remove(path_1)
    if os.path.exists(path_2):
        shutil.rmtree(path_2)
