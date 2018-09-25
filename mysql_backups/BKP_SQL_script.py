import os
import datetime
from zipfile import ZipFile

DAYS_TO_KEEP_BACKUP = 3

BACKUP_DIR_NAME = "/home/fme/miDjangoProyecto/mysql_backups/"
FILE_PREFIX = "DB_backup_"
FILE_SUFFIX_DATE_FORMAT = "%d-%m-%Y_%H.%M.%S"
USERNAME_LONG = "fme"
USERNAME_SHORT = "fme"
DBNAME = USERNAME_SHORT+"$BaseDatos1"

# get today's date and time
timestamp = datetime.datetime.now().strftime(FILE_SUFFIX_DATE_FORMAT)
backup_filename = BACKUP_DIR_NAME+"/"+FILE_PREFIX+timestamp+".sql"

os.system("mysqldump -u "+USERNAME_SHORT+" -h "+USERNAME_LONG+".mysql.pythonanywhere-services.com '"+DBNAME+"'  > "+backup_filename)

# creating zip file
#zip_filename = BACKUP_DIR_NAME+"/"+FILE_PREFIX+timestamp+".zip"
#with ZipFile(zip_filename, 'w') as zip:
#    zip.write(backup_filename, os.path.basename(backup_filename))

#os.remove(backup_filename)

# deleting old files

list_files = os.listdir(BACKUP_DIR_NAME)

back_date = datetime.datetime.now() - datetime.timedelta(days=DAYS_TO_KEEP_BACKUP)
back_date = back_date.strftime(FILE_SUFFIX_DATE_FORMAT)

length = len(FILE_PREFIX)

# deleting files older than DAYS_TO_KEEP_BACKUP days
for f in list_files:
    filename = f.split(".")[0]
    if "zip" == f.split(".")[1]:
        suffix = filename[length:]
        if suffix < back_date:
            print("Deleting file : "+f)
            os.remove(BACKUP_DIR_NAME + "/" + f)
