# coding:utf-8
import re

f_read = open(r'C:\Users\lenovo\Desktop\DECdata\04120120.01A')
f_list = f_read.readlines()

wave_lines = f_list[2:6]
dir_lines = f_list[10:18]

data_wave = dict()
data_dir = dict()

for wave_line in wave_lines:
    wave_pattern = re.compile(r'(\w+(\d+/\d+)?)\s+(\d\.\d+)(\(m\)|\(s\)$)')
    wave_dataList = re.findall(wave_pattern, wave_line)

    data_wave[wave_dataList[0][0]] = float(wave_dataList[0][2])
    data_wave[wave_dataList[1][0]] = float(wave_dataList[1][2])

for dir_lines in dir_lines:
    dir_pattern = re.compile(r'D\s+(\d+\.\d).*(\d+\.\d+)%(\s*)')
    dir_dataList = re.findall(dir_pattern, dir_lines)
    print dir_dataList
    # data_dir[dir_dataList[0][0]] = float(dir_dataList[0][1])

# print data_dir
# print data_wave
