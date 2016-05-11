import re


def process():

    f_read = open(r'C:\Users\lenovo\Desktop\str.txt', 'r')
    f_write = open(r'C:\Users\lenovo\Desktop\revise_str.txt', 'w+')

    for eachLine in f_read:
        list_line = re.split(re.compile(r'\s+'), eachLine)[0:24]
        for eachTuple in list_line:
            list_tuple = re.split(re.compile(r'/'), eachTuple)
            f_write.write("%g\t%d\t" % (float(list_tuple[0]), int(list_tuple[1])))
        f_write.write("\n")


if __name__ == '__main__':
    process()
