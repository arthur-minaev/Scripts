## Предустановка библиотек и задание директорий

### Вариант 1: установка через `install.bat`

Запустите установщик библиотек `install.bat` и дождитесь успешной установки всех необходимых библиотек. Если вам не удалось установить какую-либо библиотеку, то обратитесь к Варианту 2.

### Вариант 2: установка вручную

1.Установка gdal

1.1.Необходимо узнать версию Python в вашей системной среде. Для этого введите в командной строке команду: `python --version`. Если в переменных среды вашего ПК правильно заданы переменные, то вы получите ответ. Например: Python 3.8.17.

1.2.Необходимо узнать путь к файлу с дистрибутивами GDAL, соответствующего вашей версии Python. Если у вас установлен Python версии 3.7 и старше, то нужный дистрибутив вы можете найти в `install/GDAL` в директории проекта automat_09. Так, например, дистрибутив GDAL для Python 3.8.17 находится по пути: `C:\Users\USER_01\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\automat_09\install\GDAL\GDAL-3.4.3-cp38-cp38-win_amd64.whl`.

1.3.Непосредственно установка GDAL производится через командную строку с помощью команды: `python -m pip install *путь_к_дистрибутиву*`

Например: `python -m pip install C:\Users\USER_01\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\automat_09\install\GDAL\GDAL-3.4.3-cp38-cp38-win_amd64.whl`

Если вы выбрали правильный дистрибутив, то получите ответ: Successfully installed GDAL-3.4.3

2.Установка библиотек numpy, pandas, pyproj, shapely, openpyxl, xtarfile

Для установки этих библиотек используйте команду: `python -m pip install *название_библиотеки*`

Например: `python -m pip install numpy`

3.После установки библиотек задайте в командной строке директорию проекта с помощью команды `cd *путь_к_проекту*`

Например: `cd C:\Users\USER_01\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\automat_09`

