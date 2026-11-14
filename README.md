# skill-maizi-motion

给 [OpenFilm](https://github.com/openfilm/openfilm) 写的第一个自有品牌 skill。按官方 `openfilm/skills` 的 `template/` + `SPEC.md` 结构建，本机 0.3.2 验证。当前版本 **0.1.2**。

## 一句话

以后凡是「做一条 MaiZI Motion 的片子」，agent 先整本读 `skills/maizi-motion/SKILL.md`，按里面的验收点出片，不靠每次重打一遍提示词。

## 拼写口径（2026-11-15 已定案）

**全域唯一写法 `MaiZI Motion`**。业主 11-15 命名令「品牌名就叫: MaiZI Motion！」+「定拼写统一」覆盖 11-11 那条只管复刻片的 `MaiZi Motion`；依据与历史例外见 `F:\麦子爹知识库\10-项目\OpenFilm\【规范】品牌名拼写统一-MaiZI-Motion_20261115.md`（11-15 已迁到独立项目区）。

**白 `MaiZI` + 紫 `Motion` 是业主的品牌资产**，保留在本 README 与那张决议卡里，**不写进 `SKILL.md`**——官方 `SPEC.md` 禁止 brief 规定配色（见下节）。两者不冲突：brief 只钉「名字逐字怎么写」这个可检查事实，画面长相由业主素材和 agent 决定。

本仓库从第一版起就已是这个写法，官方 `check.mjs` 通过的 brief 与五语言元数据**不需要改字**。若日后要反向切回，用 `F:\OpenFilm_20261114\_test\【工具】品牌拼写一键切换_20261115.py --to maiZi --apply`，替换点：`SKILL.md`（frontmatter + 第三节）、`openfilm.json`（五语言）、`cover.jpg`、`evals/README.md`、`CHANGELOG.md`。

**不替换**：`.motion`（文件格式名）、RECIPE / SECTION / EDITOR（结构术语）、GitHub Copilot / Cursor（第三方工具名）。

## 装到本机

```sh
cd F:\OpenFilm_20261114
source ./_env.sh
npx openfilm skill add F:\OpenFilm_20261114\_skills\skill-maizi-motion
npx openfilm skills                     # 看到 local/maizi-motion
npx openfilm skill local/maizi-motion   # 打印整本 brief（开工前必跑）
```

从**文件夹**安装，所以 OpenFilm 给它的全名是 `local/maizi-motion`。0.1.2 已同步到三处：本仓库 `skills/maizi-motion/`、本机 `F:\OpenFilm_20261114\Skills\maizi-motion\`、专家包 `openfilm-studio/skills/maizi-motion/`，版本号一致。

## 官方索引状态（2026-11-15 06:xx）

`openfilm.json` 的 `repository` 目前是**占位值**；正式提交时由一键脚本从 GitHub 授权后的**真实账号现场读取并改写**，不再靠任何项目 owner 推断。目标公开仓库尚未创建、尚未 push。

**内容质量已达标、材料齐备，可以提交**：0.1.2 brief 删掉了 agent 本来就会的「Studio 可编辑」和官方禁止的配色规则，官方 `check.mjs --no-fetch` 通过；重跑了一组更干净的「带 / 不带」对照（请求不含品牌名、A 组不要求报数、两组同源素材同一份 WAV），A2 零文字零署名、B2 一处逐字品牌署名且只用本期文案，差异可归因给 brief。详见 `evals/README.md` 的 0.1.2 节与 `evals/measure-result-012.json`。

**唯一阻塞是 GitHub 写入身份**：网络层实测全通（`api.github.com` 200、`git ls-remote` 拿到官方 HEAD），但本机 GitHub 连接器 `auth-required`、无 `gh` / token / git 身份，重连需业主在界面亲自点授权。按规矩不硬塞凭证、不绕路。材料、tag 与一键脚本已备到「授权恢复后一条命令跑完」：`F:\OpenFilm_20261114\_skills\_submission_20261115\`。

## 这个仓库

| 路径 | 放什么 |
| --- | --- |
| `skills/maizi-motion/SKILL.md` | 需求书，agent 唯一会读到的正文（约 450 字） |
| `skills/maizi-motion/openfilm.json` | Discover 显示的标题、摘要、版本、封面 |
| `skills/maizi-motion/cover.jpg` | 16:9 封面（自绘，非 AI 生成） |
| `evals/README.md` | 真实需求试跑记录，含 0.1.1 / 0.1.2 两次「带 / 不带」对照 |
| `evals/measure.py`、`measure-result*.json` | 可复跑的量化脚本与两次结果 |
| `CHANGELOG.md` | 版本变化 |
| `.github/workflows/check.yml` | 推送后跑官方检查 |

## 为什么 brief 里不写排版

官方 `SPEC.md` 的 Leave out 明令：**styles / looks / layout / type / color / motion / techniques / steps / 「check it again」/ 手册里已有的内容，一律不写进 brief**——「一列风格清单会变成所有片子的样子」，而且「the look has to come from the person's own material and the agent's ideas, never from the skill」。

0.1.1 还留着「白 MaiZI + 紫 Motion、两段着色不同」和「Studio 里可编辑」；前者违反配色禁令，后者按 SPEC 的「Does an agent get it wrong without the sentence? ... if it does not, leave it out」必须删（0.1.1 双跑里不带 skill 的 A 组也做到了）。**0.1.2 两条都删了**，第三节从 5 条收到 4 条，落在 SPEC 要求的 3–5 条区间。0.1.2 的 B2 组仍用了白/紫，那是 agent 自己的视觉决定，不是 brief 的命令。

## 检查

```sh
node F:\OpenFilm_20261114\_community\skills-official\scripts\check.mjs F:\OpenFilm_20261114\_skills\skill-maizi-motion
```

`check.mjs` 是 2026-11-15 从官方仓库 raw 下载的原版，不在本仓库内，避免「自己写检查自己过」。索引提案另有一份 `--no-fetch` 副本在 `_submission_20261115/_official-check/`。

## License

[MIT](LICENSE).
