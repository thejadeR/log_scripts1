# 导入回溯和系统包
import sys, traceback

# 导入日志脚本
from log_script import my_logger

# 创建回溯模板
traceback_template = '''Traceback (most recent call last):
 File "%(filename)s", line %(lineno)s, in %(name)s
%(type)s: %(message)s\n''' # Skipping the "actual line" item

# 尝试捕获可能发生异常的代码
try:
    # 制造异常
    a = 1 / 2
except Exception as e:
    # http://docs.python.org/2/library/sys.html#sys.exc_info

    # 获取程序结束信息
    exc_type, exc_value, exc_traceback = sys.exc_info()  # most recent (if any) by default

    # 结构化数据
    traceback_details = {
        'filename': exc_traceback.tb_frame.f_code.co_filename,   #错误文件名字
        'lineno': exc_traceback.tb_lineno,  #错误行号
        'name': exc_traceback.tb_frame.f_code.co_name,   #模块
        'type': exc_type.__name__,      #错误类型
        'message': exc_value,  # 错误的类型值 or see traceback._some_str()
    }

    # print(traceback_details)
    # print(traceback_template % traceback_details)

    # 把错误信息按照 日志模板 记录到日志里
    my_logger().error(traceback_template % traceback_details)
    
else:  #程序无错误，则日志写入无异常，可不写
    my_logger().info("无异常\n")

# 执行后面的语句
print("to be continue next code....")