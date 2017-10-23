# archive Images v2
整理图片视频程序V2  
作者：suzhan    
Email: suzhan.cn@gmail.com    

**用途：**
将手机，单反相机拍摄的视频图像整理归档

**功能：** 
将图片视频文件按拍摄日期，相机类型，镜头类型，GPS地址整理到指定目录.

**使用方法：**
1. 下载 [exiftool](https://www.sno.phy.queensu.ca/~phil/exiftool/exiftool-10.64.zip) 
   解压得 exiftool(-k).exe 重命名为 exiftool.exe , 并复制到windows 目录下面
2. [archiveImages V2 for windows](https://github.com/suzhan/archiveImages/blob/master/archiveImagesV2.exe) 下载执行

**备注:**
1. 支持文件类型：.jpg, .nef, .mp4, .mov  
2. 从文件的exif中得出拍拍摄日期，相机类型，镜头类型，GPS地址，移动到存储目录
3. 整理存储格式 : 存储目录路径/拍摄年份/[拍摄日期，相机类型，镜头类型，GPS地址]/... 如  d:/photo/2017/D80/DES_1231.JPG  
4. 可选择是否删除原文件， 如果目标文件中存在与源文件的MD5,sha1，文件大小都一样的文件就忽略处理，直接删除       
5. 依赖 python 3.6 , pyqt5 , [exiftool](https://www.sno.phy.queensu.ca/~phil/exiftool/), google maps api ,需安装本地exiftool, 如需使用GPS分类，需确保正常使用google maps

**开源协议:** GNU General Public Licence v3

**界面图：**  
![image](https://github.com/suzhan/archiveImages/blob/master/1.PNG)
![image](https://github.com/suzhan/archiveImages/blob/master/2.PNG)


