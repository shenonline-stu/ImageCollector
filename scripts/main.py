"""
功能简述：从网页中保存图片到本地文件夹
1. 读取配置文件
    - 如无配置，则需要用户输入，并保存到配置文件中
    - 如有配置，直接使用配置里的参数
2. 打开浏览器
3. 最小化浏览器窗口
4. 滚动网页判断页面是否完成加载
    - 完成加载，读取所有图片列表，保存至配置文件中
    - 未完成加载，继续滚动网页

使用方法：
    ``` python

    ```

@File           : main.py
@Author         : Elson.L
@Created        : 2025-07-06
@Last Modified  : 2025-07-06
@Version        :
"""

from lib.logger_manager import setup_logger
from lib.path_manager import PathManager
from pathlib import Path


def path_init():
    """
    初始化路径管理器并打印相关路径信息
    :return : None
    """
    pm = PathManager()

    logger.info(f"项目根目录    : {pm.root}")
    logger.info(f"当前工作目录  : {Path.cwd()}")
    logger.info(f"配置文件目录  ：{pm.config_dir}")
    logger.info(f"日志文件目录  ：{pm.get_log_dir('ma')}")

    # 使用路径管理器创建文件
    log_path = pm.get_log_dir("main")
    log_path.parent.mkdir(parents=True, exist_ok=True)  # 确保日志目录存在

    with open(log_path, "w", encoding="utf-8") as f:
        f.write("[INFO] 日志记录开始...")


logger = setup_logger(log_file=Path("logs/main.log"), level="INFO", file_level="DEBUG")

if __name__ == "__main__":
    path_init()
