# Changelog

## 0.1.2 · 2026-11-15

**这是 brief 第一次真正改字**，目标是对齐官方 `SPEC.md` 的「Keeping a sentence」六问，把 agent 本来就会做的事和官方明令禁止写的风格规则请出去。

- 删掉第三节第 4 条「品牌名、文案与时间点在 Studio 里可编辑」——0.1.1 双跑里 A 组**不带 skill 也做到了**（`<h1>` 文本节点），按 SPEC「Does an agent get it wrong without the sentence? ... if it does not, leave it out」必须删。
- 删掉「白 `MaiZI` + 紫 `Motion`、两段着色不同」以及 frontmatter 里同样的描述——`SPEC.md` 的 Leave out 明确列了 **rules for layout, type, color or motion**。配色属于业主品牌资产，留在知识库决议卡与本仓库 README，**不写进 agent 每次都会读的 brief**；画面长相由业主本次素材与 agent 决定。
- 第一段删「片子要在 Studio 里能继续改」（OpenFilm 手册已有，SPEC 要求不重复手册）；第四段删掉会过时的本机数字（6 模型 / 49 音色 / 14 模板 / 具体模型名），改成不随版本失效的一句「已连的语音与生图服务」。
- 第三节由 5 条收到 4 条，落在 SPEC 要求的 3–5 条区间；brief 从约 800 字缩到约 450 字，更接近「one screen」。
- 元数据版本 0.1.1 → 0.1.2；五语言文案、封面、LICENSE、CI workflow 均未改。
- 重跑一组**更干净**的「带 / 不带」对照：请求不再含品牌名、不再要求 A 组报数，详见 `evals/README.md` 的 0.1.2 节。

## 0.1.1 · 2026-11-15

**brief 正文与 0.1.0 完全相同**，没有新增任何风格、版面、技法或步骤。变化只在证据与口径：

- 品牌拼写由「两处并存、待拍板」定为全域唯一 `MaiZI Motion`，依据见知识库《【规范】品牌名拼写统一-MaiZI-Motion_20261115》。
- `evals/README.md` 补上官方要求的「带它 / 不带它」同需求双跑对照（无 skill 组由独立 agent 在干净目录完成）。
- 补齐官方收录材料：`index.json` 条目草案、PR 正文、本地 git 仓库与版本 tag、可复跑的度量脚本。
- 元数据版本号 0.1.0 → 0.1.1；封面、五语言文案、brief 正文均未改字。

## 0.1.0 · 2026-11-15

第一版。按官方 `openfilm/skills` 的 `template/` 与 `SPEC.md` 建成，五段式 brief，只写可检查的事实与验收点。

- 钉死品牌拼写 `MaiZI Motion` 与两段着色（白 / 紫），禁旧名 MotionGit 及衍生。
- 要求一处、画面内可见、可编辑的署名，禁止自动沿用上一期素材。
- 要求交付报数字（时长、切点、署名秒、look 告警）。
- 元数据五语言（en / zh-CN / ja / ko / es），16:9 自绘封面。
- 明确：标准「带 / 不带」对照未做，只作本机 `local/` 使用，不申请官方索引。
