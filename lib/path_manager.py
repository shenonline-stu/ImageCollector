"""
功能简述：管理项目路径
1. 获取项目根目录
2. 将根目录设置为工作目录
3. 如果项目根目录不存在于系统目录中，添加到系统路径中

使用方法：
    pass

@File           : path_manager.py
@Author         : Elson.L
@Created        : 2025-07-07
@Last Modified  : 2025-07-07
@Version        :
"""

from pathlib import Path
import os


class PathManager:
    # 单例模式
    _inistance = None

    def __new__(cls):
        if cls._inistance is None:
            cls._inistance = super(PathManager, cls).__new__(cls)
            # 获取项目根目录
            cls.root = Path(__file__).parent.parent.resolve()
            # 把根目录设置为工作目录
            os.chdir(str(cls.root))
        return cls._inistance

    @property
    def data_dir(self) -> Path:
        """
        获取数据目录
        :return: 数据目录路径
        """
        return self.root / "data"

    @property
    def config_dir(self) -> Path:
        """
        获取配置目录
        :return: 配置目录路径
        """
        return self.root / "config"

    def get_log_dir(self, module: str) -> Path:
        """
        获取日志目录
        :return: 日志目录路径
        """
        return self.root / "logs" / f"{module}.log"

    def get_relative(self, *paths) -> Path:
        """
        获取基于工作目录的相对路径
        """
        return Path.cwd().joinpath(*paths)
