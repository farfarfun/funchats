# Changelog

## [0.0.3] - 2026-10-15

### 修复

- 随 wheel 附带 `py.typed`（PEP 561）。已发布的 `0.0.2` 产物里没有这个标记，
  下游跑 mypy/pyright 会把整个包当作无类型信息处理并报 `import-untyped`；
  旧版本不会自动补上，必须由本版本发布才生效。

### 变更

- 包目录改为 `src/` 布局，并随包附带 `py.typed`，下游可识别类型标注。
- 补全包元信息：`description`、`license`、`authors`/`maintainers`、`project.urls`。
- 开发依赖加入 `ruff`，补充 `[tool.ruff]`（`target-version = "py310"`）配置，README 记录 lint / format / 测试命令。
- 新增 `tests/test_smoke.py` 导入冒烟测试。
- 不再跟踪 `uv.lock`（已加入 `.gitignore`），依赖锁定交由本地 `uv` 生成。
- README 改为只描述当前状态：本包已归档、不含任何公开 API、大模型调用改用
  [funai](https://github.com/farfarfun/funai)；移除 `0.0.2` 与 `0.0.3` 的版本差异说明和
  从源码安装的绕路步骤（README 会被打进 wheel 的 `METADATA` 成为 PyPI 项目页文案，
  这类过渡期描述一旦发布就会长期失准）。

### 废弃

- 本包不再继续开发，`0.0.3` 之后不再发布新版本。包内没有任何公开 API，
  因此没有需要迁移的调用；大模型统一调用请改用
  [funai](https://github.com/farfarfun/funai)。

本版本没有功能或行为变更，仍是保留 `funchats` 包名的占位包。

## [0.0.2] - 2026-09-03

### 新增

- 占位包骨架：保留 `funchats` PyPI 包名，暂无实际功能代码。
