# tests/test_file_controller.py
import pytest
import yaml
from lib.file_controller import read_setting, save_setting


# 测试配置文件读取
def test_read_existing_config(tmp_path):
    # 创建临时配置文件
    config_path = tmp_path / "settings.yaml"
    config_data = {"url": ["test1.com", "test2.com"]}
    config_path.write_text(yaml.dump(config_data))

    # 测试读取
    result = read_setting(str(config_path))
    assert result == config_data  # 验证数据正确性
    assert isinstance(result, dict)  # 类型校验


def test_read_missing_config():
    # 测试不存在的配置文件
    result = read_setting("/nonexistent/config.yaml")
    assert result is None  # 应返回None
    # 可以通过caplog检查日志记录（需安装pytest-capturelog插件）
    # assert "配置文件不存在" in caplog.text


# 测试配置文件保存
def test_save_setting(tmp_path):
    config_path = tmp_path / "new_config.yaml"
    test_data = {"key": "value", "list": [1, 2, 3]}

    save_setting(str(config_path), test_data)

    # 验证文件存在
    assert config_path.exists()
    # 验证文件内容
    with open(config_path, "r") as f:
        saved_data = yaml.safe_load(f)
        assert saved_data == test_data
        # 验证缩进和Unicode支持
        assert f.read().startswith("key: value\nlist:")


def test_save_invalid_data():
    # 测试保存非字典数据
    with pytest.raises(TypeError):
        save_setting("test.yaml", "invalid data")
