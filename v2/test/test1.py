import exiftool
import os

#sPath =  'C:/Users/sulei/Desktop/exif-samples-master/exif-samples-master/jpg'

sPath = 'C:/Users/sulei/Desktop/aa'


filename_list = []
# 将需整理的文件放入数组
for root, dirs, files in os.walk(sPath, True):
    # 如果没选择子文件夹,限在根目录
    for filename in files:
        filename = os.path.join(root, filename)
        f, e = os.path.splitext(filename)
        if e.lower() not in ('.jpg', '.jpeg', '.png', '.nef', '.mp4', '.3gp', '.flv', '.mkv', '.mov'):
            continue
        filename_list.append(filename)

print(filename_list)

#files = ['C:/Users/sulei/Desktop/bb/DSC_0552.jpg', 'C:/Users/sulei/Desktop/bb/IMG_1040_2013.07.20.MOV','C:/Users/sulei/Desktop/bb/Pentax_K10D.jpg','C:/Users/sulei/Desktop/bb/DSC_1664.png']

#files = ['C:/Users/sulei/Desktop/bb/IMG_1040_2013.07.20.MOV']

with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(filename_list)
for d in metadata:
    print(d)
    #print("{:20.20} {:20.20}".format(d["SourceFile"],d["EXIF:DateTimeOriginal"]))
    #print(d["EXIF:DateTimeOriginal"])

    #print(d[])
    if d["File:FileType"] == "MOV":
        print(d["QuickTime:MediaCreateDate"])
        print(d["QuickTime:Model"])

    elif d["File:FileType"] == "JPEG":
        #print(d["EXIF:DateTimeOriginal"])
        print(d["EXIF:Model"])
        print(d["File:FileCreateDate"][:19])
        print(d["MakerNotes:Lens"])
    elif d["File:FileType"] == "MP4":
        #print(d["EXIF:Model"])
        print(d["QuickTime:CreateDate"][:19])
        #print(d["MakerNotes:Lens"])
        print(d["Composite:GPSLatitude"])
        print(d["Composite:GPSLongitude"])
    else:
        pass

