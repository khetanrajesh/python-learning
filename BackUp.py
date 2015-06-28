__author__ = 'khetanr'

import os

import time

#target_dir = 'C:\\Users\khetanr\\Projects_BusinessWorks'
#source = ["C:\\Projects_BusinessWorks"]

target_dir = 'F:\Android\Androidstuff\Final\AgliBus'
source = ["F:\Android\Androidstuff\Final\AgliBus"]

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + ".zip"


if not os.path.exists(target_dir):
    os.mkdir(target_dir)

backup_command = "zip -r {0} {1}".format(target,' '.join(source));

print(backup_command)

if (os.system(backup_command))== 0 :

    print("Success")
else:

    print("failed")










