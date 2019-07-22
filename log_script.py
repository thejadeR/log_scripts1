import logging
import sys

def my_logger():
    # 获取当前脚本的路径
    current_scripts_filename = sys.argv[0]
    # print(sys.argv)
    #只获取脚本文件名
    current_scripts_filename = current_scripts_filename.split("/")[-1]
    
    
    # 创建日志对象，及设置级别
    logger = logging.getLogger(current_scripts_filename)
    logger.setLevel(logging.DEBUG)

    # 创建文件句柄，及设置文件写入级别
    file_handler = logging.FileHandler("【%s】的日志.log"%current_scripts_filename)
    file_handler.setLevel(logging.DEBUG)
    
    # 设置日志文件数据格式化
    formatter = logging.Formatter("[%(asctime)s] - [%(name)s] - [%(levelname)s]:\n %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger
# 
# if __name__ == '__main__':
#     my_logger()
