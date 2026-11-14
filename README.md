# skill-maizi-motion

给 [OpenFilm](https://github.com/openfilm/openfilm) 写的第一个自有品牌 skill。按官方 `openfilm/skills` 的 `template/` + `SPEC.md` 结构建，本机 0.3.2 验证。

## 一句话

以后凡是「做一条 MaiZI Motion 的片子」，agent 先整本读 `skills/maizi-motion/SKILL.md`，按里面的验收点出片，不靠每次重打一遍提示词。

## 拼写口径（2026-11-15 已定案）

**全域唯一写法 `MaiZI Motion`**（白 `MaiZI` + 紫 `Motion`）。业主 11-15 命名令「品牌名就叫: MaiZI Motion！」+「定拼写统一」覆盖 11-11 那条只管复刻片的 `MaiZi Motion`；依据与历史例外见 `F:\麦子爹知识库\20-领域\视频工坊\【规范】品牌名拼写统一-MaiZI-Motion_20261115.md`。

本仓库从第一版起就已是这个写法，官方 `check.mjs` 通过的 brief 与五语言元数据**不需要改字**。若日后要反向切回，用 `F:\OpenFilm_20261114\_test\【工具】品牌拼写一键切换_20261115.py --to maiZi --apply`，替换点：

1. `skills/maizi-motion/SKILL.md`（frontmatter + 第三节）
2. `skills/maizi-motion/openfilm.json`（title / summary / details 各语言）
3. `skills/maizi-motion/cover.jpg`（重跑封面脚本）
4. `evals/README.md`、`CHANGELOG.md`

**不替换**：`.motion`（文件格式名）、RECIPE / SECTION / EDITOR（结构术语）、GitHub Copilot / Cursor（第三方工具名）。

## 装到本机

```sh
cd F:\OpenFilm_20261114
source ./_env.sh
npx openfilm skill add F:\OpenFilm_20261114\_skills\skill-maizi-motion
npx openfilm skills                 # 看到 local/maizi-motion
npx openfilm skill local/maizi-motion   # 打印整本 brief
```

从**文件夹**安装，所以 OpenFilm 给它的全名是 `local/maizi-motion`。`openfilm.json` 的 `repository` 指向业主真实存在的 GitHub 账号 `erikzeng2008-del`（依据：MCD 大赛仓库 owner，API 查得 200），但目标新仓库 `erikzeng2008-del/skill-maizi-motion` **目前 404、尚未创建**，仓库也还没 push。

**没有进官方 `index.json`，也不会出现在 Discover 的官方列表里**。双跑对照已补做，结论是「增益可见但 brief 仍需精简」，按官方 PR #5 的门槛暂不提交；申请材料（index 条目草案、PR 正文、一键脚本）在 `F:\OpenFilm_20261114\_skills\_submission_20261115\`。

## 这个仓库

| 路径 | 放什么 |
| --- | --- |
| `skills/maizi-motion/SKILL.md` | 需求书，agent 唯一会读到的正文 |
| `skills/maizi-motion/openfilm.json` | Discover 显示的标题、摘要、版本、封面 |
| `skills/maizi-motion/cover.jpg` | 16:9 封面（自绘，非 AI 生成） |
| `evals/README.md` | 真实需求试跑记录，含「带 / 不带」对照状态 |
| `CHANGELOG.md` | 版本变化 |
| `.github/workflows/check.yml` | 推送后跑官方检查 |

## 为什么 brief 里不写排版

官方 `SPEC.md` 明令 brief 不许写风格、版面、配色、技法（「一列风格清单会变成所有片子的样子」）。本 skill 里的「MaiZI 白 / Motion 紫」是**品牌标识本身的事实约束**，放在「必须为真」里当验收点，不是教 agent 怎么设计；其余观感、字号、动效一律交给 agent 和本次素材。

## 检查

```sh
node F:\OpenFilm_20261114\_community\skills-official\scripts\check.mjs F:\OpenFilm_20261114\_skills\skill-maizi-motion
```

`check.mjs` 是 2026-11-15 从官方仓库 raw 下载的原版，不在本仓库内，避免「自己写检查自己过」。

## License

[MIT](LICENSE).
