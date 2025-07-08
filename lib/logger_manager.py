"""
功能简述：
1.
2.

使用方法：

@File           : logger_manager.py
@Author         : Elson.L
@Created        : 2025-07-07
@Last Modified  : 2025-07-07
@Version        :
"""

import logging
import sys
from pathlib import Path


def setup_logger(log_file: Path, level="INFO", file_level="DEBUG") -> logging.Logger:
    """
    创建并配置日志记录器
    :param  log_file: 日志文件路径(默认不写入文件)
            level: 控制台日志级别(INFO, DEBUG, WARNING, ERROR, CRITICAL)
            file_level: 文件日志级别(DEBUG, INFO, WARNING, ERROR, CRITICAL)
    :return: 配置好的日志记录器
    """

    # 创建日志记录器
    logger = logging.getLogger("ImageCollector")
    logger.setLevel(logging.DEBUG)  # 设置日志记录器的最低级别为DEBUG

    # 创建格式器
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 控制台处理器
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, level.upper(), logging.INFO))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 文件处理器
    if log_file:
        # 确保日志目录存在
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)

        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setLevel(getattr(logging, file_level.upper(), logging.DEBUG))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
