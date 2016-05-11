# coding:utf-8
import re
import os

current_path = os.getcwd()
list_dir = os.listdir(current_path)
dir_status = False

for data_file in list_dir:
    if not data_file.endswith(".py"):
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

    for new_file in list_dir:
        new_file = new_file.split(r".")[0]+".txt"
        f_write = open(os.path.join(new_path, new_file), 'w')

        keys_wave = data_wave.keys()
        keys_dir = data_dir.keys()

        for i in range(8):
            for eachList in keys_wave, keys_dir:
                f_write.write("%s\t%d\t\t\t\t" % (eachKey, data_wave[eachKey]))
                f_write.write("%d\t%d\n" % (eachKey, data_dir[eachKey]))

        f_write.close()
