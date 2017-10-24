#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


def file_or_dir(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return "dir"
        elif os.path.isfile(path):
            return "file"
    else:
        return False


def alt_num(num):
    return num.zfill(3)
    # return "%03d" % num


def re_name(path):
    filelist = os.listdir(path)
    for filename in filelist:
        # path = path + "/" + filename
        if file_or_dir(path + "/" + filename) == "file":
            splitName = filename.split("_")
            if len(splitName) == 3:
                name = splitName[0]
                num = alt_num(splitName[1])
                postfix = splitName[2]
                newName = name + "_" + num + "_" + postfix
                os.rename(path + "/" + filename, path + "/" + newName)
            else:
                name = splitName[0]
                num = alt_num(splitName[1].split(".")[0])
                postfix = splitName[1].split(".")[1]
                newName = name + "_" + num + "." + postfix
                os.rename(path + "/" + filename, path + "/" + newName)
        else:
            re_name(path + "/" + filename)


def main():
    path = "./testFile"
    re_name(path)
    print("File name change successfully!")

if __name__ == '__main__':
    main()
