"""
功能简述：文件管理控制器
1.
2.

使用方法：
    ``` python

    ```

@File           : file_controller.py
@Author         : Elson.L
@Created        : 2025-07-07
@Last Modified  : 2025-07-07
@Version        :
"""

import os
import yaml


def read_config(config_path: str) -> dict | None:
    return (
        yaml.safe_load(open(config_path, "r", encoding="utf-8"))
        if os.path.exists(config_path)
        else None
    )
