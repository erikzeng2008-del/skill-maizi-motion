#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""可复跑的对照度量（官方 SPEC「Trying it」：能量化的用脚本量，谁都能再跑一次）。

只量「静态可测」的部分：成片规格、时间轴结构、品牌拼写、两段着色、文本可编辑性、
旧名残留。观感、署名是否真的被观众看见、交付有没有报数，仍需看片 + 读报告，脚本不假装能测。

用法（Windows / macOS / Linux，需 ffprobe、python3）：
  python evals/measure.py \
    --a-film   <无 skill 成片.mp4> --a-project <无 skill 工程目录> \
    --b-film   <带 skill 成片.mp4> --b-project <带 skill 工程目录> \
    --json     evals/measure-result.json

退出码恒为 0；它只报告，不替人判定「哪个更好」。
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys

EXACT = "MaiZI Motion"
OLD = "MaiZi Motion"


def probe(film: pathlib.Path) -> dict:
    if not film.exists():
        return {"error": f"成片不存在: {film}"}
    cmd = ["ffprobe", "-v", "error", "-show_entries",
           "format=duration,size:stream=codec_name,width,height,r_frame_rate",
           "-of", "json", str(film)]
    try:
        d = json.loads(subprocess.check_output(cmd, text=True, timeout=60))
    except Exception as e:
        return {"error": f"ffprobe 失败: {e}"}
    fmt = d.get("format", {})
    vs = next((s for s in d.get("streams", []) if s.get("width")), {})
    return {
        "duration_s": round(float(fmt.get("duration", 0)), 3),
        "size_bytes": int(fmt.get("size", 0)),
        "width": vs.get("width"),
        "height": vs.get("height"),
        "fps": vs.get("r_frame_rate"),
        "video_codec": vs.get("codec_name"),
    }


def scan_project(project: pathlib.Path) -> dict:
    if not project.is_dir():
        return {"error": f"工程目录不存在: {project}"}
    htmls = sorted(p for p in project.glob("*.html") if p.is_file())
    film_html = project / "film.html"
    film = film_html.read_text(encoding="utf-8") if film_html.exists() else ""
    iframes = re.findall(r"<iframe\b[^>]*>", film)
    ats = re.findall(r'\bat="([\d.]+)"', film)
    audios = re.findall(r"<audio\b", film)
    sections = re.findall(r"<section\b", film)

    body = "\n".join(p.read_text(encoding="utf-8", errors="replace") for p in htmls)
    # 「观众看到的文字」= 去掉 script/style/标签后的可见文本。
    # 只看源码连续串会误判：拆成两个 span 的写法源码里没有 "MaiZI Motion" 这个连续串。
    visible = re.sub(r"<script\b.*?</script>", " ", body, flags=re.S | re.I)
    visible = re.sub(r"<style\b.*?</style>", " ", visible, flags=re.S | re.I)
    visible = re.sub(r"<[^>]+>", " ", visible)
    visible = re.sub(r"\s+", " ", visible)
    visible_exact = visible.count(EXACT)
    visible_old = visible.count(OLD)
    source_exact = body.count(EXACT)
    source_old = body.count(OLD)
    motiongit = len(re.findall(r"motiongit", body, re.I))
    # 两段着色：.a / .b 规则的 color；同时列出全部前景色，供人工判断是否真的分了两段
    ca = re.search(r"\.a\s*\{[^}]*color:\s*([^;]+)", body)
    cb = re.search(r"\.b\s*\{[^}]*color:\s*([^;]+)", body)
    colours = [x.group(1).strip() for x in (ca, cb) if x]
    all_colours = sorted(set(v.strip() for v in re.findall(
        r"color:\s*(#[0-9a-fA-F]{3,8}|rgb\([^)]*\)|[a-zA-Z]+)", body)))
    spans = len(re.findall(r"<span\b[^>]*>\s*MaiZ[Ii]\s*</span>", body))
    return {
        "html_files": [p.name for p in htmls],
        "sections": len(sections),
        "picture_clips": len(iframes),
        "cuts": max(0, len(iframes) - 1),
        "clip_starts_s": ats,
        "audio_clips": len(audios),
        "visible_brand_exact_count": visible_exact,
        "visible_brand_old_count": visible_old,
        "source_literal_exact_count": source_exact,
        "source_literal_old_count": source_old,
        "motiongit_hits": motiongit,
        "two_part_colours": colours,
        "css_foreground_colours": all_colours,
        "colours_distinct": len(set(colours)) > 1 if len(colours) > 1 else None,
        "brand_split_spans": spans,
        # 品牌名出现在可见文本里 = HTML 文本节点，不是烧进位图 / canvas
        "brand_is_editable_text": visible_exact > 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a-film", required=True, help="无 skill 组（基线）成片")
    ap.add_argument("--a-project", required=True, help="无 skill 组工程目录")
    ap.add_argument("--b-film", required=True, help="带 skill 组成片")
    ap.add_argument("--b-project", required=True, help="带 skill 组工程目录")
    ap.add_argument("--json", dest="out")
    a = ap.parse_args()

    result = {
        "说明": "A = 不带 skill 基线，B = 带 skill。脚本只量静态可测项；观感与交付行为见 evals/README.md。",
        "A_无skill": {"成片": probe(pathlib.Path(a.a_film)), "工程": scan_project(pathlib.Path(a.a_project))},
        "B_带skill": {"成片": probe(pathlib.Path(a.b_film)), "工程": scan_project(pathlib.Path(a.b_project))},
    }
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    if a.out:
        out = pathlib.Path(a.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text + "\n", encoding="utf-8")
        print(f"\n→ 已写 {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
