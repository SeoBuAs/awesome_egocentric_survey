#!/usr/bin/env python3
"""data/*.csv → index.html(임베디드 JSON), data/graph.json, docs/*.md, README 통계 블록.

사용법: python3 scripts/build.py          # 빌드
        python3 scripts/build.py --check  # 검증만 (파일 변경 없음)
"""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs"

AXIS_ORDER = ["B", "1", "2", "1∩2", "3", "4", "5", "6", "7", "8", "9"]
REL_KO = {
    "backbone": "백본으로 사용", "extends": "직접 확장", "trains_on": "학습 데이터",
    "evaluates_on": "평가 데이터", "compares": "비교 기준선", "cross": "개념 연결",
    "cites": "인용", "part_of": "구성 요소", "captures": "캡처 장비", "produces": "산출물",
}
STATUSES = {"검증됨", "2차 확인", "원문 기준", "미확인"}
EVIDENCE = {"원문", "확인", "추정"}
REVIEW_STATUSES = {"대기", "보류", "반영", "제외"}
HOI_GROUPS = {
    "A": "정지 잡기 생성·접촉 보정", "B": "MANO 손 + 물리 강화학습", "C": "미분 가능 물리·영상→물리 보정",
    "D": "전신 휴머노이드 + 물리", "E": "사람 손 → 로봇손 전이", "F": "로봇손 잡기 (참고)",
}


def read(name):
    with open(DATA / f"{name}.csv", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def validate(nodes, edges, axes):
    errs = []
    ids = [n["id"] for n in nodes]
    errs += [f"중복 노드 id: {i}" for i, c in Counter(ids).items() if c > 1]
    axis_ids = {a["axis"] for a in axes}
    idset = set(ids)
    for n in nodes:
        if n["axis"] not in axis_ids:
            errs.append(f"{n['id']}: 알 수 없는 axis '{n['axis']}'")
        for a in filter(None, (s.strip() for s in n["axis2"].split(","))):
            if a not in axis_ids:
                errs.append(f"{n['id']}: 알 수 없는 axis2 '{a}'")
        if n["status"] not in STATUSES:
            errs.append(f"{n['id']}: 알 수 없는 status '{n['status']}'")
        if n["isNew"] not in {"Y", "N"}:
            errs.append(f"{n['id']}: isNew는 Y/N")
        if n["arxiv"] and not re.fullmatch(r"\d{4}\.\d{4,5}", n["arxiv"]):
            errs.append(f"{n['id']}: arXiv 형식 이상 '{n['arxiv']}'")
    for e in edges:
        for k in ("source", "target"):
            if e[k] not in idset:
                errs.append(f"엣지 {e['source']}→{e['target']}: 없는 노드 '{e[k]}'")
        if e["rel"] not in REL_KO:
            errs.append(f"엣지 {e['source']}→{e['target']}: 알 수 없는 rel '{e['rel']}'")
        if e["evidence"] not in EVIDENCE:
            errs.append(f"엣지 {e['source']}→{e['target']}: 알 수 없는 evidence '{e['evidence']}'")
    return errs


def validate_review(review, nodes, axes):
    errs = []
    axis_ids = {a["axis"] for a in axes}
    seen = set()
    for r in review:
        a = r["arxiv"]
        if not re.fullmatch(r"\d{4}\.\d{4,5}", a):
            errs.append(f"review: arXiv 형식 이상 '{a}'")
        if a in seen:
            errs.append(f"review: 중복 arXiv '{a}'")
        seen.add(a)
        for f in ("axis_guess", "axis2_guess"):
            for x in filter(None, (t.strip() for t in r[f].split(","))):
                if x not in axis_ids:
                    errs.append(f"review {a}: 알 수 없는 {f} '{x}'")
        if r["status"] not in REVIEW_STATUSES:
            errs.append(f"review {a}: 알 수 없는 status '{r['status']}'")
    return errs


def validate_hoi(hoi, hoi_edges):
    errs = []
    ids = [r["id"] for r in hoi]
    for e in hoi_edges:
        for k in ("source", "target"):
            if e[k] not in ids:
                errs.append(f"hoi 엣지 {e['source']}→{e['target']}: 없는 노드 '{e[k]}'")
        if e["rel"] not in REL_KO:
            errs.append(f"hoi 엣지 {e['source']}→{e['target']}: 알 수 없는 rel '{e['rel']}'")
        if e["evidence"] not in EVIDENCE:
            errs.append(f"hoi 엣지 {e['source']}→{e['target']}: 알 수 없는 evidence '{e['evidence']}'")
    errs += [f"hoi: 중복 id '{i}'" for i, c in Counter(ids).items() if c > 1]
    for r in hoi:
        if r["group"] not in HOI_GROUPS:
            errs.append(f"hoi {r['id']}: 알 수 없는 group '{r['group']}'")
        if r["arxiv"] and not re.fullmatch(r"\d{4}\.\d{4,5}", r["arxiv"]):
            errs.append(f"hoi {r['id']}: arXiv 형식 이상 '{r['arxiv']}'")
        if r["status"] not in STATUSES:
            errs.append(f"hoi {r['id']}: 알 수 없는 status '{r['status']}'")
    return errs


def hoi_md(hoi, hoi_edges):
    out = ["# 번외 · 물리 기반 잡기/HOI 합성", "",
           "> `scripts/build.py`가 `data/hoi.csv`에서 자동 생성합니다. 직접 수정하지 마세요.",
           "> 에고센트릭 지형도와 별개인 번외 정리입니다. 그래프·통계·검토 대기·데일리 스캔에 포함되지 않습니다.", ""]
    for g, name in HOI_GROUPS.items():
        rows = sorted((r for r in hoi if r["group"] == g), key=lambda r: r["year"])
        if not rows:
            continue
        out += [f"## {name} ({len(rows)})", "",
                "| 연구 | 게재처 | arXiv | 대상 | 방식 | 물리 고려 | 관련성 |",
                "| --- | --- | --- | --- | --- | --- | --- |"]
        out += [f"| {md_cell(r['title'])} | {md_cell(r['venue'])} | {arxiv_link(r['arxiv'])} | {md_cell(r['subject'])} | "
                f"{md_cell(r['method'])} | {md_cell(r['physics'])} | {md_cell(r['relevance'])} |" for r in rows]
        out.append("")
    label = {r["id"]: r["label"] for r in hoi}
    out += ["## 연결", "", "| source → target | 관계 | 근거 | 메모 |", "| --- | --- | --- | --- |"]
    out += [f"| {label[e['source']]} → {label[e['target']]} | {REL_KO[e['rel']]} | {e['evidence']} | {md_cell(e['note'])} |" for e in hoi_edges]
    return "\n".join(out)


def review_md(review):
    out = ["# 검토 대기 논문", "",
           "> `scripts/build.py`가 `data/review.csv`에서 자동 생성합니다. 직접 수정하지 마세요.",
           "> arXiv 데일리 스캔이 찾은, 아직 지형도에 배치하지 않은 논문입니다. 축은 잠정입니다.", "",
           "| 발견일 | arXiv | 제목 | 잠정 축 | 상태 | 메모 |", "| --- | --- | --- | --- | --- | --- |"]
    for r in sorted(review, key=lambda r: (r["found"], r["arxiv"]), reverse=True):
        ax = ", ".join(filter(None, [r["axis_guess"], r["axis2_guess"]])) or "미정"
        out.append(f"| {r['found']} | {arxiv_link(r['arxiv'])} | {md_cell(r['title'])} | {ax} | {r['status']} | {md_cell(r['note'])} |")
    return "\n".join(out)


def md_cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def arxiv_link(a):
    return f"[{a}](https://arxiv.org/abs/{a})" if a else "—"


def papers_md(nodes, axes):
    by_axis = {a["axis"]: a for a in axes}
    out = ["# 축별 논문·데이터셋 목록", "",
           "> `scripts/build.py`가 `data/nodes.csv`에서 자동 생성합니다. 직접 수정하지 마세요.", ""]
    for ax in AXIS_ORDER:
        rows = sorted((n for n in nodes if n["axis"] == ax), key=lambda n: n["date"])
        if not rows:
            continue
        out += [f"## 축 {ax} · {by_axis[ax]['name']} ({len(rows)})", "",
                "| id | 제목 | 연월 | 게재처 | arXiv | 함께 걸친 축 | 검증 | 신규 |",
                "| --- | --- | --- | --- | --- | --- | --- | --- |"]
        for n in rows:
            out.append("| " + " | ".join([
                md_cell(n["id"]), md_cell(n["title"]), n["date"], md_cell(n["venue"]),
                arxiv_link(n["arxiv"]), n["axis2"] or "—", n["status"],
                "✓" if n["isNew"] == "Y" else "",
            ]) + " |")
        out.append("")
    return "\n".join(out)


def edges_md(edges):
    out = ["# 연결(엣지) 목록", "",
           "> `scripts/build.py`가 `data/edges.csv`에서 자동 생성합니다. 직접 수정하지 마세요.", "",
           "`A → B`: B가 A를 백본·데이터·비교 대상 등으로 사용함.", ""]
    for rel, ko in REL_KO.items():
        rows = [e for e in edges if e["rel"] == rel]
        if not rows:
            continue
        out += [f"## {ko} (`{rel}`, {len(rows)})", "",
                "| source → target | 근거 | 메모 |", "| --- | --- | --- |"]
        out += [f"| {e['source']} → {e['target']} | {e['evidence']} | {md_cell(e['note']) or ''} |" for e in rows]
        out.append("")
    return "\n".join(out)


def axes_md(axes, nodes):
    cnt = Counter(n["axis"] for n in nodes)
    out = ["# 축별 목표와 과제", "",
           "> `scripts/build.py`가 `data/axes.csv`에서 자동 생성합니다. 직접 수정하지 마세요.", ""]
    for a in sorted(axes, key=lambda a: int(a["order"])):
        out += [f"## 축 {a['axis']} · {a['name']} (노드 {cnt[a['axis']]}개)", "",
                f"- **핵심 문제**: {a['problem']}",
                f"- **최종 목표**: {a['goal']}",
                f"- **남은 과제**: {a['challenges']}",
                f"- **평가 지표·벤치마크**: {a['benchmarks']}",
                f"- **다른 축과의 연결**: {a['connections']}", ""]
    return "\n".join(out)


def stats_block(nodes, edges, axes):
    axis_of = {n["id"]: n["axis"] for n in nodes}
    cross = sum(axis_of[e["source"]] != axis_of[e["target"]] for e in edges)
    cnt = Counter(n["axis"] for n in nodes)
    names = {a["axis"]: a["name"] for a in axes}
    lines = [f"노드 **{len(nodes)}**개 · 연결 **{len(edges)}**개 · 축 **{len(axes)}**개 · "
             f"축 사이 연결 **{cross}**개 · 2026년 9월 이후 신규 **{sum(n['isNew'] == 'Y' for n in nodes)}**개", "",
             "| 축 | 이름 | 노드 수 |", "| --- | --- | --- |"]
    lines += [f"| {a} | {names[a]} | {cnt[a]} |" for a in AXIS_ORDER if a in names]
    return "\n".join(lines)


def main():
    nodes, edges, axes, review, hoi = read("nodes"), read("edges"), read("axes"), read("review"), read("hoi")
    hoi_edges = read("hoi_edges")
    errs = validate(nodes, edges, axes) + validate_review(review, nodes, axes) + validate_hoi(hoi, hoi_edges)
    if errs:
        print("검증 실패:\n  " + "\n  ".join(errs), file=sys.stderr)
        sys.exit(1)
    print(f"검증 통과: 노드 {len(nodes)}, 엣지 {len(edges)}, 축 {len(axes)}, 검토 대기 {len(review)}, 번외 HOI {len(hoi)}/{len(hoi_edges)}")
    if "--check" in sys.argv:
        return

    for a in axes:
        a["order"] = int(a["order"])
    graph = {"nodes": nodes, "edges": edges, "axes": axes, "review": review,
             "hoi": hoi, "hoi_edges": hoi_edges, "hoi_groups": [{"group": g, "name": n} for g, n in HOI_GROUPS.items()]}
    (DATA / "graph.json").write_text(json.dumps(graph, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    html_path = ROOT / "index.html"
    html = html_path.read_text(encoding="utf-8")
    payload = json.dumps(graph, ensure_ascii=False).replace("</", "<\\/")
    html, n = re.subn(r'(<script type="application/json" id="eg-data">).*?(</script>)',
                      lambda m: m.group(1) + payload + m.group(2), html, count=1, flags=re.S)
    if n != 1:
        sys.exit("index.html에서 eg-data 스크립트 태그를 찾지 못했습니다")
    html_path.write_text(html, encoding="utf-8")

    DOCS.mkdir(exist_ok=True)
    (DOCS / "papers.md").write_text(papers_md(nodes, axes) + "\n", encoding="utf-8")
    (DOCS / "edges.md").write_text(edges_md(edges) + "\n", encoding="utf-8")
    (DOCS / "axes.md").write_text(axes_md(axes, nodes) + "\n", encoding="utf-8")
    (DOCS / "review.md").write_text(review_md(review) + "\n", encoding="utf-8")
    (DOCS / "hoi.md").write_text(hoi_md(hoi, hoi_edges) + "\n", encoding="utf-8")

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    text, n = re.subn(r"(<!-- STATS:START -->\n).*?(<!-- STATS:END -->)",
                      lambda m: m.group(1) + stats_block(nodes, edges, axes) + "\n" + m.group(2), text, flags=re.S)
    if n != 1:
        sys.exit("README.md에서 STATS 마커를 찾지 못했습니다")
    readme.write_text(text, encoding="utf-8")
    print("생성 완료: index.html, data/graph.json, docs/*.md, README.md")


if __name__ == "__main__":
    main()
