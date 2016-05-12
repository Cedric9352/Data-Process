# coding:utf-8
import re
import os
import sys


def cur_file_dir():
    path = sys.path[0]

    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(os.path.dirname(path))

current_path = cur_file_dir()
list_dir = os.listdir(current_path)
dir_status = False

for data_file in list_dir:
    if data_file.endswith(".py"):
        continue
    f_read = open(os.path.join(current_path, data_file))
    f_list = f_read.readlines()
    f_read.close()

    wave_lines = f_list[2:6]
    dir_lines = f_list[10:18]

    data_wave = dict()
    data_dir = dict()

    for wave_line in wave_lines:
        wave_pattern = re.compile(r'(\w+(\d+/\d+)?)\s+?(\d+\.\d+)')
        wave_dataList = re.findall(wave_pattern, wave_line)

        data_wave[wave_dataList[0][0]] = float(wave_dataList[0][2])
        data_wave[wave_dataList[1][0]] = float(wave_dataList[1][2])

    for dir_lines in dir_lines:
        dir_pattern = re.compile(r'D\s+(\d+\.\d).*?(\d+\.\d+)')
        dir_dataList = re.findall(dir_pattern, dir_lines)

        data_dir[dir_dataList[0][0]] = float(dir_dataList[0][1])
        data_dir[dir_dataList[1][0]] = float(dir_dataList[1][1])

    data_dir = sorted(data_dir.iteritems(), key=lambda x: float(x[0]), reverse=False)

    if not dir_status:
        parent_path = os.path.dirname(current_path)
        os.chdir(parent_path)

        if os.path.exists('MatlabData'):
            pass
        else:
            os.mkdir('MatlabData')

        os.chdir(os.path.join(parent_path, 'MatlabData'))
        dir_status = True

    new_path = os.getcwd()

    data_file = data_file.split(r".")[0]+".txt"
    f_write = open(os.path.join(new_path, data_file), 'w')

    for eachKey in data_wave:
        f_write.write("%s\t%f\n" % (eachKey, data_wave[eachKey]))

    f_write.write(" "*20+"\n")

    for eachTuple in data_dir:
        f_write.write("%f\t%f\n" % (float(eachTuple[0]), eachTuple[1]))

    f_write.close()
