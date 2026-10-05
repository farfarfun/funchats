# funchats

占位仓库，尚无实际功能代码。发布这个空壳版本只是为了在 PyPI 上保留 `funchats` 这个包名，避免被无关项目抢注；具体功能会在之后陆续补充。

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

> PyPI 上当前已发布的最新版本是 `0.0.2`，仓库里的 `0.0.3` 尚未发布。
> 两者都是没有功能代码的占位包，行为完全一致；`0.0.3` 只调整了打包结构
> （`src/` 布局、随包附带 `py.typed`、补全元信息），会在下次发版时生效。
> 需要仓库里的最新打包结构时，可从源码安装：
>
> ```bash
> git clone https://github.com/farfarfun/funchats.git
> cd funchats
> uv pip install .
> ```

## 用法

当前版本仅用于占位，除了可被正常导入外没有其他公开功能：

```python
import funchats

print(funchats.__name__)  # funchats
```

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
