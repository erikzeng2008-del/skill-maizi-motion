# Evals

只记真实跑过的需求。`skills/` 之外的内容不会装进 OpenFilm，agent 读不到这里。
官方要求：同一句真实需求，带 skill 跑一次、不带 skill 跑一次，把两版都看一遍，能量化的用脚本量，数字写在这里。

## 0.1.0 · 2026-11-15（首版，只跑了「带它」）

真实需求（原话）：「可以，试试吧。品牌名就叫:MaiZI Motion！」
成片：`F:\OpenFilm_20261114\_projects\maizi-motion-intro\maizi-motion-intro.mp4`，8.000 s · 1920×1080 · 30 fps · 240 帧 · H.264+AAC · 1.90 MB，单镜 0 切点，`look --full` 0 告警，初检抓到 1 个真告警「音轨重叠」后修复。当时**标准对照未做**，故只作本机 `local/` 使用。

## 0.1.1 · 2026-11-15（补做「带它 / 不带它」双跑）

**真实需求（原话，两组同一句）**：
「做一条能对外发的 MaiZI Motion 品牌开场，8 秒，带一句旁白。」

**固定输入（两组一致）**：BGM `hello-20s/assets/bed.mp3`（20.04 s，用 `#t=0,8` 原地裁切）；旁白台词「这一版，只讲一件事。」，百炼 `qwen3-tts-flash` / `Serena`；1920×1080 · 30 fps · 8 s · 渲染归一 -14 LUFS；同一台 Windows 机器、同一 OpenFilm 0.3.2、同一批官方通用手册。不联网找素材、不 AI 生图/生视频。

**两组怎么隔离**：
- **A（不带 skill）**：独立子 agent、干净上下文，明确禁止读 `_skills/`、上一轮成片工程、`_community/skills-official/template/skills/`、知识库品牌卡与任何含 `maizi-motion` 的既有文件；只许读 `hello-20s` 工程骨架 + `MANUAL.md` + `manual/{edit,media,canvas}/SKILL.md`。工程 `F:\OpenFilm_20261114\_projects\baseline-no-skill\`，成片 `baseline-no-skill.mp4`，独立自评报告 `【报告】基线对照A组-无skill_20261115.md`。A 组自证「一次都没查过任何品牌规范」。
- **B（带 skill）**：本会话，开工前真跑 `npx openfilm skill local/maizi-motion` 打印整本 brief，按第三节五条验收点出片。工程 `F:\OpenFilm_20261114\_projects\maizi-motion-intro-8s\`，成片 `maizi-motion-intro-8s.mp4`。

| request (word for word) | skill | with | without | seen |
| --- | --- | --- | --- | --- |
| 「做一条能对外发的 MaiZI Motion 品牌开场，8 秒，带一句旁白。」 | 0.1.1 | B：1 处白/紫品牌名、1 个切点、只用本次旁白文案 | A：单色米白 + 金色主题、同屏 2 处品牌字样、自编一句 slogan、自评「换品牌照样成立」 | 见下表逐项 + 两版成片截帧 |

### 逐项对照（脚本 `measure.py` + 截帧目视）

| # | 可检查项 | A · 不带 skill | B · 带 skill | 差异能否归因给 skill |
| --- | --- | --- | --- | --- |
| 1 | 品牌名逐字 `MaiZI Motion` | ✅ 源码出现 2 次 | ✅ 可见文本 1 次 | ❌ **需求里就写了品牌名**，两组自然都对 |
| 2 | `MaiZI` 白 / `Motion` 紫两段着色 | ❌ 单色米白 `#F5F3EE`，主色是自选暖金 `#E9B44C` | ✅ `#FFFFFF` / `#9678FF` | ✅ **明显更好** |
| 3 | 不出现 MotionGit 及衍生 | ✅ 0 处 | ✅ 0 处 | ❌ 两组都没写 |
| 4 | 一处画面内可见署名、不重复堆 | ❌ 同屏 2 处品牌字样（主名 + 全大写眉标），跨两镜头累计 4 次；**A 组自评「画面里没有任何署名」** | ✅ 全片 1 处，3.0 s 起可见 | ✅ **明显更好** |
| 5 | 内容只来自本次素材与本次文案 | ❌ 自编「把想法，做成会动的东西。」 | ✅ 画面文字只有本次旁白那句 | ✅ **明显更好** |
| 6 | 品牌名在 Studio 可编辑（HTML 文本节点） | ✅ `<h1>` 文本 | ✅ 两段 `<span>` 文本 | ❌ **agent 本来就会做** |
| 7 | 交付报时长/切点/署名秒/look 告警 | ❌ 制作全程不主动报；报告里的数字是「被任务点名要」才写 | ✅ 按 brief 第五条主动列数 | ⚠️ 弱差异：两组都被要求写报告，主动/被动不同，证据不够硬 |
| 8 | `look --full` 告警 | ✅ 0（主会话独立复跑通过） | ✅ 0 | ❌ 无差异 |
| 9 | 成片规格 | 8.000 s · 1920×1080 · 30 fps · 2,055,711 B | 8.000 s · 1920×1080 · 30 fps · 1,716,262 B | ❌ 无实质差异 |

### 实测数字

| 项 | A · 不带 skill | B · 带 skill |
| --- | --- | --- |
| 时长 / 帧 | 8.000 s / 240 帧 @30 fps | 8.000 s / 240 帧 @30 fps |
| 镜头 / 切点 | 2 镜头、1 硬切点 `at=4` | 2 镜头、1 切点 `at=3` |
| 品牌名可见次数（`measure.py`） | 源码 2 次（s1 + s2 各 1） | 可见文本 1 次 |
| 两段着色 CSS | 无（前景色 3 种，品牌名单色） | `#FFFFFF` / `#9678FF` |
| 音轨 | 2 条，BGM 0 s + 旁白 `at=1.6` | 2 条，BGM 0 s + 旁白 0 s |
| 旁白 WAV 时长 | 2.64 s | 1.92 s（同台词同模型，TTS 时长波动，属对照偏差，如实记） |
| 混音（原始 → 归一） | -24.0 LUFS → **-14.1 LUFS**，TP -2.0 dBTP | -22.9 LUFS → **-14.0 LUFS**，TP -2.8 dBTP |
| 渲染 | 4 workers · h264_nvenc · 9.6 s | 4 workers · h264_nvenc · 9.4 s |
| `look` 确定性 | ✓ 12 帧两轮乱序同帧 | ✓ 12 帧两轮乱序同帧 |
| `look --full` | ✓ 0 告警 | ✓ 0 告警 |
| 返工 | **0 次**（一版出片即过全部检查）；另有 1 次流程顺序调整：`look --full` 首次因未渲染被工具拒绝，改为先 render 再补跑，未改工程、未产生第二版成片 | **1 次**：3.1 s 切点后有约 0.15 s 空场，改成品牌名 t=0 即有 0.28 底透明，重渲染复检 0 告警 |
| 目视抽帧 | 1.0 / 3.2 / 7.6 s（A 组）+ 1.0 / 4.6 / 7.6 s（主会话独立复核） | 1.0 / 3.0 / 3.1 / 3.4 / 4.6 / 7.6 s |

> A 组有意思的一点：技术指标**一版就全过**（0 返工、0 告警），而带 skill 的 B 组反而返工 1 次（修切点空场）。差距不在「能不能出片」，在「出的是不是这个牌子」。

复跑（脚本随仓库保存，结果在 `evals/measure-result.json`）：

```sh
python evals/measure.py \
  --a-film   F:/OpenFilm_20261114/_projects/baseline-no-skill/baseline-no-skill.mp4 \
  --a-project F:/OpenFilm_20261114/_projects/baseline-no-skill \
  --b-film   F:/OpenFilm_20261114/_projects/maizi-motion-intro-8s/maizi-motion-intro-8s.mp4 \
  --b-project F:/OpenFilm_20261114/_projects/maizi-motion-intro-8s \
  --json     evals/measure-result.json
```

### 结论（照官方 `SPEC.md`「A skill ships only when it is clearly better」）

- **有可见增益，但只在 3 条上**：两段着色、一处署名不重复、只用本期素材——这三条正是 brief 第三节写的，A 组全都踩了。所以 skill 不是白写。
- **A 组自己的自评命中了 brief 第二节**：「换另一个品牌名照样成立……本质是通用开场模板，不是 MaiZI Motion 的品牌开场」。B 组有品牌专属双色与一处署名，但坦白说仍是深色底 + 居中大字的通用构图，**属「部分绑定」而非完全专属**；按 brief 第二节「只换品牌名照样成立就是没做完」的严格判据，两组都还没完全过。要真正过，得等业主给出「固定开头句 / 频道说话方式」这类只有他知道的信息——业主本轮明确说还在测试、不用管，所以没有编造。
- **有 1 条「agent 本来就会」**：Studio 可编辑。按 `SPEC.md` 第 85 行「Does an agent get it wrong without the sentence? ... if it does not, leave it out」，**这条应该从 brief 删掉**。0.1.1 为保持双跑与版本一致没删；若真要提交官方，应先出 0.1.2 精简 brief 再重跑一次对照。「交付报数」是弱差异，证据不够硬，不拿来邀功。
- **隔离局限（不吹牛）**：A、B 由同一个底层模型执行；请求原话里本来就含 `MaiZI Motion`，所以「拼写正确」不能算 skill 的功劳；A 也被实验任务要求写数字报告，所以「报数」同样不算硬证据。真正干净的对照应是「请求不含品牌名、且不给 A 任何报数要求」，本轮没做到，已如实记下。
- **旁白时长不一致**（2.64 s vs 1.92 s）是同模型 TTS 的随机波动，属对照偏差；不影响画面结论，但影响音画同步的可比性。

**因此本轮结论是「材料备齐、增益可见、brief 仍需精简与补业主专属信息」，不是「明显更好到可以直接收录」。** 按官方自己刷掉 PR #5 的门槛，这一版**不该现在提交**；加上本机无 GitHub 推送凭证、目标仓库尚未创建，**没有真发 PR**。申请材料在 `_submission_20261115/`，一键脚本默认 dry-run。

### 环境 / 版权

Windows 11 · Node 22.22.2 · OpenFilm 0.3.2 · ffmpeg 6.1.1 · agent = 本会话 Claude（A 组为独立子 agent，同模型）· 素材 = 本机已有 BGM + 百炼 TTS。别人的视频、他人肖像只留在本机，不进仓库。
