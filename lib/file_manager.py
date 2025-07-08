"""
功能简述：文件管理控制器
1. 读取setting.yaml配置文件，返回字典
2. 更新setting.yaml配置文件

使用方法：

@File           : file_controller.py
@Author         : Elson.L
@Created        : 2025-07-07
@Last Modified  : 2025-07-07
@Version        :
"""

import os
import yaml
import logging


def read_setting(config_path: str) -> dict | None:
    if os.path.exists(config_path):
        logger.info(f"读取配置文件：{config_path}")
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    else:
        logger.error(f"配置文件 {config_path} 不存在，请检查路径或创建配置文件。")


def save_setting(config_path: str, data: dict) -> None:
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.safe_dump(data, f, allow_unicode=True, default_flow_style=False)
        logger.info(f"保存配置文件：{config_path}")


logger = logging.getLogger("ImageCollector")
