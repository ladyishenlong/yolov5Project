import os
import shutil
from xml.dom.minidom import Document


# 获取该路径下所有文件的路径
def getPaths(path):
    paths = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        paths.append(file_path)
    return paths




if __name__ == '__main__':
    print("1")

