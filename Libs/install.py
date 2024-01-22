import os, sys, re

libs = ['gdal', 'numpy', 'openpyxl', 'pandas', 'pyproj', 'shapely', 'xtarfile']
installed = []

# get filenames from selected directory
def Files(folder, extensions = None, target_path = None, miss_path = None):
    files = []
    if extensions is not None:
        if isinstance(extensions, (tuple, list)):
            extensions = list(extensions)
        else:
            extensions = [extensions]
        exts = ['.' + str(ext).lower().lstrip('.') for ext in extensions]
    for corner, _folders, _files in os.walk(folder):
        if miss_path:
            if re.search(miss_path, corner):
                continue
        for file in _files:
            if miss_path:
                if re.search(miss_path, file):
                    continue
            if extensions is not None:
                if all(not file.lower().endswith(ext) for ext in exts):
                    continue
            if target_path:
                if not re.search(target_path, file):
                    continue
            files.append(corner + '\\' + file)
    return files

# install GDAL
version = f"{sys.version_info.major}{sys.version_info.minor}"
for file in Files('install/GDAL'):
    if re.search(version, file):
        cmd = f"python -m pip install {file}"
        if os.system(cmd) == 0:
            installed.append('gdal')

# install other libs
for lib in libs[1:]:
    cmd = f"python -m pip install {lib}"
    if os.system(cmd) == 0:
        installed.append(lib)

# check install
non_installed = set(libs) - set(installed)
if len(non_installed) == 0:
    print('Все библиотеки установлены успешно')
else:
    print(f'Что-то пошло не так при установке библиотек: {list(non_installed)}')
