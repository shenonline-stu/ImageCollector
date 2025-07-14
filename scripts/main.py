"""
功能简述：从网页中保存图片到本地文件夹
1. 读取配置文件
2. 执行图片采集流程

@File           : main.py
@Author         : Elson.L
@Created        : 2025-07-06
@Last Modified  : 2025-07-08
@Version        : 1.1
"""

from lib.logger_manager import setup_logger
from lib.path_manager import pm  # 导入路径管理器
from lib.file_manager import read_setting, save_setting

# 初始化日志器（使用路径管理器获取日志路径）
logger = setup_logger(log_file=pm.get_log_dir("main"), level="INFO", file_level="DEBUG")


def main():
    """程序主入口函数"""
    logger.info(f"{'=' * 10} 程序启动 {'=' * 10}")
    logger.info(f"当前项目目录：{pm.root}")

    # 获取配置文件路径
    config_file = pm.config_dir / "settings.yaml"
    logger.info(f"配置文件路径: {config_file}")

    # 读取配置
    settings = read_setting(str(config_file)) or {}
    logger.info(f"当前配置文件: {settings}")

    # 确保url配置存在且是列表
    if "url" not in settings or not isinstance(settings["url"], list):
        settings["url"] = []

    # 确保url列表足够长（至少2个元素）
    while len(settings["url"]) < 2:
        settings["url"].append("")

    # 更新配置
    settings["url"][1] = "baidu.com"
    logger.info(f"更新配置文件: {settings}")

    # 保存配置
    save_setting(str(config_file), settings)
    logger.info("配置保存完成")

    # 这里可以添加您的图片采集主逻辑...
    # collect_images(settings)

    logger.info("程序执行完成")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception(f"程序异常终止: {e}")
