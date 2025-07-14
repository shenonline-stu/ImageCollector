"""
功能简述：管理项目路径
1. 获取项目根目录
2. 将根目录设置为工作目录
3. 如果项目根目录不存在于系统目录中，添加到系统路径中

使用方法：
    pass

更新内容：
1.　删除设置工作目录的步骤，工作目录会影响全局，暂时避免
2.　删除重新创建logging实例，直接获取已经生成的实例

@File           : path_manager.py
@Author         : Elson.L
@Created        : 2025-07-07
@Last Modified  : 2025-07-07
@Version        :
"""

from pathlib import Path
import os
import logging

logger = logging.getLogger("ImageCollector")


class PathManager:
    # 单例模式
    _inistance = None

    def __new__(cls):
        if cls._inistance is None:
            cls._inistance = super(PathManager, cls).__new__(cls)

            # 获取项目根目录
            cls.root = Path(__file__).parent.parent.resolve()

            # 初始化必要目录
            cls._init_directories()

            # 把根目录设置为工作目录
            # [250708] 优化删除，避免在脚本运行时改变工作目录导致路径问题
            # os.chdir(str(cls.root))

        return cls._inistance

    @classmethod
    def _init_directories(cls):
        """确保日志目录存在"""
        os.makedirs(cls.root / "config", exist_ok=True)
        os.makedirs(cls.root / "logs", exist_ok=True)

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
        return self.root.joinpath(*paths)


pm = PathManager()
