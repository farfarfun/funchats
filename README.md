# funchats

> **已归档**：本包不再继续开发。大模型调用请改用 [funai](https://github.com/farfarfun/funai)。

`funchats` 是一个可导入的空占位包，仅用于持有 PyPI 上的 `funchats` 包名、避免被无关项目抢注，不提供任何功能代码。

## 环境要求

- Python 3.10 或更高版本

## 安装

```bash
uv add funchats
```

或使用 pip：

```bash
pip install funchats
```

## 用法

包内没有任何公开 API，除了可被正常导入外没有其他行为：

```python
import funchats

print(funchats.__name__)  # funchats
```

需要大模型统一调用（DeepSeek、Moonshot 等 OpenAI 兼容接口）请用 [funai](https://github.com/farfarfun/funai)。

## 开发

```bash
uv sync --dev
uv run ruff check --fix . && uv run ruff format .
uv run pytest
```

---

## 关于 farfarfun

[farfarfun](https://github.com/farfarfun) 是一个专注于实用工具库的开源组织，
涵盖云存储、数据处理、AI、多媒体与开发工具链等方向。

- 🏠 组织主页：<https://github.com/farfarfun>
- 📦 PyPI：<https://pypi.org/user/niuliangtao/>
- 📧 联系：farfarfun@qq.com

本项目基于 [MIT](LICENSE) 协议开源。
