import sys
import os

directories = ['./local_storage/', './models/', './figures/']

for directory in directories:
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)
