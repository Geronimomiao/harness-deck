# 聊聊 Harness — 网页版分享 PPT

「人类早期驯服野马指南」分享的网页版幻灯片，共 56 个播放步骤（含 1 页扉页和 1 组页内分步切换）。

## 新开 Feature 的流程

每个 feature 使用独立的 Git worktree，避免影响本地 `main` 和其他正在进行的改动。

1. 在主工作区中，基于本地 `main` 创建功能分支和 worktree：

   ```bash
   git worktree add -b codex/<feature-name> ../harness-deck-<feature-name> main
   ```

2. 进入新 worktree，并从该目录启动项目。端口被占用时换一个端口即可：

   ```bash
   cd ../harness-deck-<feature-name>
   python3 serve.py 8093
   ```

3. 启动后，同时提供本机和局域网访问地址：

   ```text
   本机：http://localhost:8093
   局域网：http://<本机局域网 IP>:8093
   ```

   macOS 通常可用 `ipconfig getifaddr en0` 查询当前 Wi-Fi 的局域网 IP。`serve.py` 监听 `0.0.0.0`，同一局域网内的设备可以直接访问。

## 本地运行

```bash
python3 serve.py 8092
# 打开 http://localhost:8092 ；同一局域网设备可通过本机 IP 访问
```

`serve.py` 对 HTML 禁缓存（改完刷新即生效）、图片缓存 5 分钟。也可以直接双击 `index.html` 打开（纯静态、无依赖）。

## 操作

| 按键 | 作用 |
| --- | --- |
| ↑ / ↓、PgUp / PgDn、空格、Enter | 翻页 |
| Home / End | 首页 / 末页 |
| F | 切换 填充（铺满裁边）/ 适应（完整留边），选择会记住 |
| 地址栏 `#页码` | 直达某页（如 `/#30`），刷新不丢页 |

滚轮、触屏滑动同样可以翻页。窗口比例不是 16:9 时，纯色页面使用同色背景填充，其他页面使用当前页的模糊晕染填充。

## 目录结构

- `index.html` — 全部逻辑（单文件，无构建）
- `assets/slides/slide-N.webp` — 56 页原稿（2560×1440，源自 5760×3240 PNG 导出）
- `assets/slides/blur-N.webp` — 各页氛围模糊底图（160px）
- `assets/cover/` — 扉页分层素材：`cover-bg`（AI 修复的干净背景）、`cover-laptop`（无马电脑帧）、`cover-horse`（Keynote 原稿抽出的马图层，透明）。后两张当前未使用，留作日后动效
- 素材源文件：`~/Downloads/猫分享/`（截图）与 `~/Desktop/猫分享 (1).key`（Keynote 原稿，`Data/` 内含全部图层素材）

## 待办

- [ ] 需要动效的页面逐页重建（分步动画机制在 git 历史 `4095254^` 可参考）
- [ ] 部署 Cloudflare Pages（拿公开链接）
