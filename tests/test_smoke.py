"""占位包冒烟测试：确认包可被正常导入。

funchats 目前是保留 PyPI 包名用的占位仓库，尚无实际功能代码，
因此测试只覆盖当前唯一的公开行为——包本身可以被导入。
后续补充真实功能时需要在这里补充对应的用例。
"""

import funchats


def test_import() -> None:
    """包必须能被正常导入。"""
    assert funchats is not None
