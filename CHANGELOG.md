# Changelog

## [0.0.3] - 2026-10-02

### 变更

- 包目录改为 `src/` 布局，并随包附带 `py.typed`，下游可识别类型标注。
- 补全包元信息：`description`、`license`、`authors`/`maintainers`、`project.urls`。
- 开发依赖加入 `ruff`，补充 `[tool.ruff]`（`target-version = "py310"`）配置，README 记录 lint / format / 测试命令。
- 新增 `tests/test_smoke.py` 导入冒烟测试，提交 `uv.lock` 锁定开发依赖。

本版本没有功能或行为变更，仍是保留 `funchats` 包名的占位包。

## [0.0.2] - 2026-08-31

### 新增

- 占位包骨架：保留 `funchats` PyPI 包名，暂无实际功能代码。
