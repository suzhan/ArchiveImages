# archiveImages
整理图片视频程序V1
作者：suzhan
Email: suzhan.cn@gmail.com
功能：
可选源目录及存储目标目录，
可以整理的文件类型：.jpg, .png', .nef, .mp4, .3gp, .flv, .mkv, .mov
从文件的exif中得出拍摄日期，移动到存储目录，默认路径是 archives_[原目录名]
如果目标文件中存在与源文件的MD5,sha1，文件大小都一样的文件就忽略处理，直接删除
整理后删除源文件夹中的空目录。
