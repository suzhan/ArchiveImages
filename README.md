# archive Images v1
整理图片视频程序V1  
作者：suzhan  
Email: suzhan.cn@gmail.com  

功能： 
将散乱的文件按拍摄日期整理到指定目录.

备注:
1. 支持文件类型：.jpg, .png', .nef, .mp4, .3gp, .flv, .mkv, .mov  
2. 从文件的exif中得出拍摄日期，移动到存储目录，默认路径是 archives_[原目录名]  
3. 整理存储格式 : 存储目录路径/拍摄日期/文件类型/... 如  d:/photo/2017.01.01/JPG/DES_1231.JPG  
4. 如果目标文件中存在与源文件的MD5,sha1，文件大小都一样的文件就忽略处理，直接删除   
5. 整理后删除源文件夹中的空目录。    
6. 依赖 python 3.6 , pyqt5 , hachoir3.
