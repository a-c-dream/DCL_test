import os
import shutil


def file_copy(src, dest):
    print(f'copy form {src} to {dest}...')
    files = os.listdir(src)
    for file in files:
        file_path = os.path.join(src, file)
        dest_path = os.path.join(dest, file)
        shutil.copy(file_path, dest_path)


if __name__ == '__main__':
    base_src = r'G:\保研\论文\Destruction and Construction Learning for Fine-grained Image Recognition\dataset\CUB_200_2011\CUB_200_2011\CUB_200_2011\images'
    dest = r'G:\保研\论文\Destruction and Construction Learning for Fine-grained Image Recognition\code\DCL\datasets\CUB\data'
    dirs = os.listdir(base_src)
    for c_dir in dirs:
        src = os.path.join(base_src, c_dir)
        file_copy(src, dest)
