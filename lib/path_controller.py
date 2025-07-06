import os.path
import sys


def project_path_controller():
    """

    :return:
    """
    # 获取当前脚本的绝对路径
    current_path: str = os.path.abspath(__file__)
    print(f"[INFO] 当前脚本的绝对路径: {current_path}")

    # 设定项目根目录
    root_path: str = os.path.dirname(os.path.dirname(current_path))
    print(f"[INFO] 项目根目录: {root_path}")

    # 添加项目根目录到系统路径
    if root_path not in sys.path:
        sys.path.append(root_path)

    # 将根目录设置为工作目录
    if os.getcwd() != root_path:
        os.chdir(root_path)
        print(f"[INFO] 工作目录已更改为: {os.getcwd()}")
    else:
        print(f"[INFO] 工作目录已是项目根目录: {os.getcwd()}")
    return root_path


# 设置全局变量方便导入
ROOT_DIR = project_path_controller()
