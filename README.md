# archive Images v2
整理图片视频程序V2  
作者：suzhan  
Email: suzhan.cn@gmail.com  

功能： 
将图片视频文件按拍摄日期,相机类型,镜头类型, GPS 整理到指定目录.

备注:
1. 支持文件类型：.jpg,  .nef, .mp4,  .mov  
2. 从文件的exif中得出拍摄日期,相机类型,镜头类型, GPS，移动到指定存储目录 
3. 整理存储格式 : 存储目录路径/拍摄年份/[摄日期/相机类型/镜头类型/地址]/... 如  d:/photo/2017/[摄日期/相机类型/镜头类型/地址]/DES_1231.JPG  
4. 如果目标文件中存在与源文件的MD5,sha1，文件大小都一样的文件就忽略处理，直接删除     
5. 依赖 python 3.6 , pyqt5 , exiftool , google maps api


开源协议: GNU General Public Licence v3
