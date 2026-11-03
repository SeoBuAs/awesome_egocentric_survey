# 검토 대기열 48편 재정리 — 출간 여부 · 관계 연결 · 연구의 빈칸

작성 2026-11-01 · 대상 `data/review.csv`의 대기 48편 · 저장소 파일은 수정하지 않음

## 한눈에

| 항목 | 결과 |
|---|---|
| 출간 여부 | 출간 1 · 채택(학회 미개최) 3 · 기술 보고서 2 · 프리프린트 42 |
| 프리프린트 근거 강도 | 2중 확인 24 · 1회 확인 5 · 존재만 확인 13 |
| 관계 | 115개 (대기열↔대기열 25, 대기열↔지도 90) · 근거 원문 24 / 확인 16 / 추정 75 |
| 같은 연구 | 1쌍: 2610.00438 ↔ 2610.18950 (λ0) — 하나로 합치기를 권함 |
| 연구의 빈칸 | 18개 — 열려 있음 1 · 부분적으로 채워짐 17 · 이미 채워짐 0 (모두 웹 검색으로 반례 확인) |
| 범위 판단(참고) | 범위 밖 후보 6 · 경계 12 · 내용 미확인 9 — 배치는 직접 판단하실 몫으로 남김 |

> 주의: 이 환경에서 arxiv.org·alphaxiv·huggingface·neurips.cc·aclanthology는 직접 열 수 없어, 근거는 웹 검색 결과(링크 제목·요약)와 github.com 페이지가 전부입니다. "프리프린트"는 '학회 근거를 찾지 못함'이지 '학회에 안 냈음'의 증명이 아닙니다.

## 1. 출간 여부

### 1.1 프리프린트가 아닌 6편

| 논문 | arXiv | 판정 | 학회 | 근거 |
|---|---|---|---|---|
| EgoVoice | 2610.12248 | **출간 (본 학회)** | EMNLP 2026 main | ACL Anthology 2026.emnlp-main.1277 항목이 독립 검색 2회에서 이 제목으로 나옴. 페이지 원문은 네트워크 제한으로 직접 열지 못함 |
| NavAble | 2610.19330 | **채택 (공식 목록 등재, 학회 미개최)** | NeurIPS 2026 Evaluations & Datasets Track | neurips.cc/virtual/2026/poster/138983 포스터 페이지가 같은 제목으로 검색됨 + 공저자 게시물·HF 데이터셋명 'NeurIPS_2026_BLV_Subset'. 학회는 12월 |
| HuRo | 2609.10706 | **채택 표기 (저자 표기, 학회 미개최)** | CoRL 2026 | arXiv Comments 'Accepted at CoRL 2026'(검색 요약 경유), 저자 측 GitHub About '(CoRL 2026)'. BibTeX는 아직 @misc. 학회는 11/9–12 |
| Stream4D | 2610.31320 | **채택 표기 (검색 요약 1회, 재확인 실패)** | ACM Multimedia 2026 | 10/28 스캔 때 검색 도구 요약에 'accepted to ACM Multimedia 2026'. 이후 세 차례 재검증에서 논문 자체가 다시 잡히지 않아 확인 못 함 |
| λ0 (기술 보고서판) | 2610.18950 | **기술 보고서** | — (학회 없음) | 공식 GitHub: 저자 'Lambda-humanoid Team', 'please cite our report', @misc arXiv eprint. 같은 연구의 논문판이 2610.00438 |
| RoboCap | 2610.07217 | **기술 보고서** | — (학회 없음) | 회사(Grounded Superintelligence) X 게시물 'RoboCap suite Technical report'. 직접 열람은 못 했고 2차 검사는 논문을 다시 찾지 못함 |

정리하면 **실제로 학회 proceedings에 실린 것은 EgoVoice 1편뿐**이고, NavAble·HuRo는 채택됐지만 학회가 아직 열리지 않았습니다. Stream4D의 ACM MM 표기는 한 번 본 검색 요약뿐이라 원문 Comments 확인이 필요합니다.

### 1.2 프리프린트 42편 (근거 강도별)

**2중 확인 — 독립 검사 2회 모두 논문을 보고, 학회·채택 근거를 찾지 못함** (19편)

| 논문 | arXiv | 축(제안) | 범위 판단 |
|---|---|---|---|
| λ0 논문판 (Towards a General Humanoid…) | 2610.00438 | 5 | 핵심 |
| HuGe | 2610.34186 | 5 | 핵심 |
| V-JEPA Hand | 2610.26780 | 2 | 핵심 |
| DewHand | 2610.29936 | 2 | 핵심 |
| InfiniHand | 2609.35743 | 2 | 핵심 |
| EgoFound3R | 2610.01210 | 2 | 핵심 |
| EgoContact | 2610.39167 | 5 | 경계 (2D 접촉점) |
| RESELF (Seeing the World and the Self) | 2609.01276 | 1∩2 | 핵심 |
| MEgoVista | 2609.16684 | 2 | 핵심 |
| EventEgoHands++ | 2609.17189 | 2 | 핵심 |
| EgoPathBench | 2609.16610 | 4 | 핵심 |
| Plan-Bench | 2610.18836 | — | 범위 밖 후보 (1인칭·3D 근거 없음) |
| VISTA | 2610.22822 | 4 | 경계 (깊이·SLAM 미사용 시 밖) |
| Ego2Act | 2610.01092 | 6 | 경계 (3D 요소 미확인) |
| GNR (Generative Neural Retargeting) | 2610.12440 | 5 | 경계 (에고 특이성 약함) |
| EgoLAP | 2610.08726 | 5 | 핵심 |
| EgoWild2Dex | 2609.23755 | 5 | 핵심 |
| DR-VLA | 2610.18373 | 5 | 경계 (사족보행 내비, 3D 불분명) |
| ESCAPE | 2610.23943 | 5 | 범위 밖 후보 (‘egocentric’=로봇 몸 깊이 센서) |

**2중 확인 (미러·2차 출처 기준) — arXiv 원문 대신 deeplearn.org 미러·기사로 봄. ID↔제목은 이전 스캔의 arxiv.org 링크로 확인** (5편)

| 논문 | arXiv | 축(제안) | 범위 판단 |
|---|---|---|---|
| EgoAlign | 2610.16176 | 4 | 경계 (3D 장면 QA, 에고 영상 입력 아님) |
| EgoOmniWorld | 2610.18499 | 4 | 범위 밖 후보 (3D 요소 없음) |
| ProactEgoMem | 2610.30089 | 7 | 경계 (3D 기하 미확인) |
| LEGO | 2610.12442 | 6 | 핵심 |
| APM-Bench | 2609.37559 | 7 | 경계 (3D 기하 미확인) |

**1회 확인 — 한 검사만 논문을 보고 학회 근거 없음** (5편)

| 논문 | arXiv | 축(제안) | 범위 판단 |
|---|---|---|---|
| EXE | 2610.33685 | 5 | 핵심 |
| EgoRayFormer | 2610.26641 | 2 | 핵심 |
| EgoCPT | 2610.17572 | 5 | 핵심 |
| EgoJEPA | 2610.20904 | 5 | 핵심 |
| EgoWholeView | 2610.16256 | 2 | 핵심 |

**존재만 확인 — 이전 스캔에서 arxiv.org 링크로 존재는 확인. 이후 3차례 검색에 다시 잡히지 않아 학회 확인과 내용 검증이 약함** (13편)

| 논문 | arXiv | 축(제안) | 범위 판단 |
|---|---|---|---|
| EgoP²C | 2610.22681 | 4 | 내용 미확인 (축은 제목 기준) |
| From Sight to Foresight | 2610.04139 | 4 | 내용 미확인 (축은 제목 기준) |
| EgoExo-Next | 2610.04506 | 4 | 내용 미확인 (축은 제목 기준) |
| GazeLens | 2610.28502 | 4 | 경계 (3D 비중 낮음) |
| SOMA | 2610.36384 | 4 | 내용 미확인 (축은 제목 기준) |
| EgoProbe | 2610.17128 | 7 | 경계 (내용 미확인) |
| 에고 영상 임베딩+IMU 행동 인식 | 2610.12926 | — | 범위 밖 후보 (임베딩+IMU 행동 인식) |
| 에고·엑소 절차 이해 프레임워크 | 2610.00069 | — | 범위 밖 후보 (절차 이해, 3D 없음) |
| Decoupling Action (월드 시뮬레이션) | 2610.27946 | 6 | 내용 미확인 (축은 제목 기준) |
| Robotizing Human Videos (물리 일관) | 2610.06137 | 8 | 내용 미확인 (축은 제목 기준) |
| Ego-CEVR | 2610.37509 | 5 | 내용 미확인 (축은 제목 기준) |
| IronMind | 2609.39403 | 5 | 내용 미확인 (축은 제목 기준) |
| ActiveAlign | 2610.36859 | 5 | 내용 미확인 (축은 제목 기준) |

### 1.3 대기열 기록에서 고칠 만한 점 (수정은 하지 않았습니다)

- **2610.00438 ↔ 2610.18950**: 같은 HumanVerse-500(500시간·32,993 에피소드)과 같은 λ0 3단계 레시피. 논문판(09-30, 1저자 Chongyang Xu)과 팀 명의 기술 보고서판(10-13). 지도에 올릴 때 한 노드로 합치고 ID 둘을 적는 편이 맞습니다.
- **2610.04139 제목의 "(SpatialMind)" 꼬리표**: SpatialMind는 다른 논문(2506.03642, NeurIPS 2025)입니다. 이 논문이 그 이름을 쓰는지 확인되지 않아 혼동일 가능성이 큽니다.
- **2610.31320 Stream4D 메모의 "(ACM MM 2026)"**: 검색 요약 1회 근거. 이름이 같은 다른 논문(2608.19556, 비디오 확산)이 있어 혼동 주의.
- **2610.26641 EgoRayFormer 메모 "10/19 제출"**: 발견일(10-29)과 어긋나고, 메모의 "EgoPoseFormer 대비 −9.09 mm"는 공식 README에서 확인되지 않았습니다(README 수치: UnrealEgo2 17.64 mm, UnrealEgo-RW 49.55 mm). 저장소: github.com/BodenAI/EgoRayFormer.
- **EgoAlign 이름 충돌**: λ0 저장소의 "EgoAlign(동작 정렬)"은 대기열의 2610.16176 EgoAlign(상황 3D QA)과 다른 대상입니다.
- **ESCAPE(2610.23943)**: 제목의 "egocentric"은 로봇 몸에 단 깊이 센서를 뜻해 사람 1인칭 영상과 무관합니다.

## 2. 관계 연결

규칙은 지도와 같습니다: source = 상류(쓰이거나 비교되는 쪽), target = 하류. 동시기 개념 연결은 `cross`로 먼저 나온 쪽을 source로 둡니다. 제안 간선은 클러스터별로 별도 검토자가 '유지/수정/삭제'를 판정했고 삭제된 간선은 뺐습니다.

### 2.1 계보와 하위 그룹

**손·몸·4D (축 2·1∩2·3)**

- **월드 좌표 손+카메라 단일 단계 복원** — InfiniHand(09-28) → EgoFound3R(10-01) → V-JEPA Hand(10월) → DewHand(10-21). HaWoR(SLAM 다단계) → StableHand·MINT를 잇는 계보로, 넷 다 "SLAM·최적화 없이 한 번의 forward"를 내세웁니다. 백본은 VGGT-Ω(EgoFound3R·DewHand 공유), LingBot-Map(InfiniHand), V-JEPA 2.1(V-JEPA Hand)로 갈립니다. HOT3D·ARCTIC(V-JEPA Hand·DewHand·InfiniHand), HOI4D(InfiniHand·EgoFound3R), TACO(EgoFound3R·DewHand)에서 겹치지만 서로를 기준선으로 두지 않습니다(→ 빈칸 G2).
- **머리 착용 다중 카메라 캡처 리그** — MEgoVista(어안 3대+IMU, 손·머리 메트릭 4D), RoboCap(6캠 모자형 + SLAM·깊이·손 API), EgoWholeView(광각 6대, SMPL-X 몸 + MANO 손). 모두 "하드웨어+추정기"를 함께 내고 로봇 시연 수집과 닿습니다. 지도에서는 EgoKit·HOMIE Gen2·EgoBody3M이 가장 가깝습니다.
- **착용자 몸·자기 복원** — RESELF는 지도의 ReViV와 같은 1∩2 과제(장면+착용자 전신). EgoRayFormer는 스테레오 어안 몸 포즈로 UnrealEgo·EgoPoseFormer 계열인데, 이 계열 노드가 지도에 없습니다.
- **특수 센서·접촉** — EventEgoHands++(이벤트 카메라, 실데이터 EEH-R), EgoContact(2D 접촉점 → 로봇 grasp, 경계 사례).

**VLM 공간추론·시선 (축 4·9)**

- 내용이 확인된 축 4 정식 후보는 **EgoPathBench**(기하 검증된 1인칭 웨이포인트 경로) 하나입니다. Plan-Bench는 1인칭·3D 근거가 없어 범위 밖 후보입니다.
- EgoP²C·Sight→Foresight(방법), EgoExo-Next·SOMA(벤치), GazeLens(시선 토큰 감축)는 존재만 확인되어 제목 기준 분류만 가능합니다. EgoExo-Next·EgoOmniWorld·Foresight는 "행동 뒤 다음 상태 추론"이라는 소그룹을 이룰 수 있습니다.
- 지도 노드를 원문으로 지목한 간선이 하나도 없어 이 클러스터 간선은 모두 추정입니다.

**메모리·어시스턴트 (축 7·미분류)**

- **스트리밍 에고 메모리 벤치 3종** — APM-Bench(세션 간 지속), ProactEgoMem(능동 기억), EgoProbe(장거리 정확 기억, 내용 미확인). 같은 평가 공간의 동시기 벤치지만 3D 기하 요소가 확인되지 않아 축 7의 주변부입니다.
- **보조 응용** — EgoVoice(능동 음성), VISTA(BLV 보조, Aria), NavAble(BLV 보행 데이터). 관찰 주제 "시각장애인 보조"가 실제 군집을 이룹니다.
- **엑소→에고 생성** — LEGO는 3D 리프팅 없이 LVSM 새 시점 합성으로 EgoX 계열을 대체하며, 지도의 Exo2EgoHOI와 동시기 경쟁입니다(축 6+8).

**생성·데이터·리타게팅 (축 6·8)**

- **사람 영상 로봇화** — 지도의 Phantom → Masquerade 선을 HuRo(63만 에피소드, CoRL 2026)가 잇고, 2610.06137(물리 일관)이 같은 갈래의 후속으로 보입니다(내용 미확인). HuGe의 팔 재렌더링도 같은 발상입니다.
- **정교 손 리타게팅 대립** — GNR(학습형 flow matching, 223k 시연) 대 EgoCPT(시연별 접촉 인지 최적화). 둘 다 EgoMatrix와 같은 문제를 다룹니다.
- **에고 생성 평가** — Ego2Act(110과제·2,640영상, 목표 완수 판정기). Decoupling Action은 제목만 확인.

**로봇 학습 (축 5)**

- **휴머노이드 전신** — λ0(=2610.00438)와 HuGe가 같은 설계(SONIC 모션 토큰 + 손 명령, EgoDex·EgoVerse 사전학습)로 직접 경쟁하지만 벤치마크가 달라(SIMPLE·G1 4과제 대 HumanoidArena) 수치 비교가 안 됩니다(→ G6). IronMind도 이 계열로 보입니다.
- **리타게팅을 넘는 중간 표현** — EgoLAP(언어 행동 CoT), EgoJEPA(JEPA 잠재 행동), EXE(분해 잠재 행동), Ego-CEVR(체현 간 시각 표현). 상류는 EgoVLA·ACE-Ego-0, 대조점은 GNR·EgoCPT. 지켜보던 "축 5 분할"(리타게팅 기반 대 리타게팅 생략)이 실제로 뚜렷하며, 두 갈래를 같은 조건에서 맞붙인 비교는 없습니다(→ G13).
- **겉모습·시점 격차** — HuGe(팔 재렌더링), EgoWild2Dex(GeoFormer 시점 정렬, 야생 에고 538.9시간).
- **주변부** — DR-VLA(사족보행 내비), ESCAPE(범위 밖), ActiveAlign(능동 지각, 내용 미확인).

### 2.2 대기열 ↔ 대기열 (25개)

| source → target | 관계 | 근거 | 이유 |
|---|---|---|---|
| HuRo → Robotizing Human Videos (물리 일관) | cross | 추정 | 제목에 'Robotizing Human Videos'라는 같은 표현이 들어 있다. 2610.06137은 제목상 '물리적으로 일관된 상호작용'을 강조해, HuRo류 시각 오버레이의 물리 불일치를 다루는 후속 연구로 보인다. 제목과 제출 시기가 달라 … |
| HuRo → HuGe | cross | 추정 | HuGe의 팔 외형 재렌더링(arm re-rendering)은 HuRo의 시각 로봇화처럼 사람과 로봇의 겉모습 차이를 데이터 편집으로 메우는 아이디어다(HuGe 축 제안에도 보조 8로 적혀 있음). HuGe가 HuRo를 인용하는지는 확인하지 못했다. |
| EgoPathBench → DR-VLA | cross | 추정 | EgoPathBench의 1인칭 웨이포인트·경로 선택(Embodied Path 과제 포함)과 DR-VLA의 1인칭 웹 영상 기반 사족보행 내비게이션은 '1인칭 시점 경로 의사결정'이라는 과제를 공유합니다. 한쪽은 VLM 평가, 다른 쪽은 로봇 정책 … |
| MEgoVista → RoboCap | cross | 추정 | 둘 다 다중 카메라와 IMU를 단 머리 착용 캡처 장치로 메트릭 손 추적을 하는 하드웨어+알고리즘 연구입니다(MEgo View 어안 3대+IMU 대 RoboCap 카메라 6대+IMU 2개). MEgoVista(09-15)가 먼저입니다. |
| MEgoVista → EgoWholeView | cross | 추정 | EgoWholeView는 내용을 확인하지 못했습니다. review.csv 메모상으로는 머리 장착 다중 카메라로 몸과 양손을 캡처하는 연구여서, 다시점 머리 착용 손 모션 캡처인 MEgoVista와 같은 계열로 보입니다. |
| InfiniHand → EgoFound3R | cross | 추정 | 사전학습된 3D 기하 파운데이션 모델(LingBot-Map 대 VGGT-Ω) 위에 손 헤드를 붙여 월드 공간 손을 한 번에 복원한다는 설계가 같고, 둘 다 HOI4D에서 평가합니다. InfiniHand(09-28)가 먼저입니다. |
| InfiniHand → V-JEPA Hand | cross | 추정 | 둘 다 별도 SLAM 없이 단일 피드포워드로 손과 카메라 궤적을 함께 추정하고, 같은 ARCTIC·HOT3D에서 경쟁합니다. InfiniHand(09-28)가 먼저입니다. |
| APM-Bench → EgoProbe | cross | 추정 | EgoProbe는 내용을 확인하지 못했습니다. 제목상 스트리밍 에고 영상의 장거리·정확 기억을 평가하는 벤치마크로 보여, 세션 간 지속 메모리를 평가하는 APM-Bench와 같은 평가 공간에 있다고 추정합니다. 제출 순서(2609 → 2610)에 … |
| APM-Bench → ProactEgoMem | cross | 추정 | 둘 다 스트리밍 에고 어시스턴트의 기억을 평가하는 동시기 벤치마크이고, 개체(물체) 상태 추적 과제를 공유합니다. 구성이 104개 궤적·549개 세션 대 300+100개 클립으로 달라 같은 연구는 아닙니다. APM-Bench(2609)가 먼저 제출돼 … |
| IronMind → HuGe | cross | 추정 | 두 논문 모두 에고 사전학습으로 휴머노이드 정책(정교 조작/범용 VLA)을 확장합니다. IronMind는 내용을 확인하지 못해 제목만 보고 판단했습니다. |
| λ0 논문판 (Towards a General Humanoid…) → EgoWholeView | cross | 추정 | 두 연구 모두 머리 장착 장비로 착용자의 몸과 양손 동작을 캡처해 로봇 시연용 데이터를 만듭니다. EgoWholeView는 내용을 확인하지 못해 제목과 review.csv 메모만으로 추정했습니다. |
| λ0 논문판 (Towards a General Humanoid…) → λ0 (기술 보고서판) | cross | 확인 | 같은 연구: 두 항목이 같은 HumanVerse(-500) 데이터(500시간, 32,993 에피소드, 8,700만 포즈 프레임)와 3단계로 학습하는 휴머노이드 전신 VLA λ0를 설명합니다. 2610.00438(2026-09-30 제출, 1저자 … |
| EgoFound3R → DewHand | cross | 추정 | EgoFound3R와 DewHand는 같은 고정 VGGT-Ω 기하 백본 위에 손 전용 헤드를 얹은 월드 공간 손 복원 모델이고, 둘 다 TACO에서 평가합니다. EgoFound3R(10-01)가 먼저입니다. |
| RoboCap → EgoWholeView | cross | 추정 | RoboCap(카메라 6대 모자형)과 EgoWholeView(메모상 머리 장착 광각 RGB 6대)는 같은 6카메라 머리 착용 구성이고, 둘 다 로봇 시연 데이터가 목적입니다. EgoWholeView는 내용을 확인하지 못했고, 같은 연구인지도 확인하지 … |
| EgoLAP → EgoJEPA | cross | 추정 | 두 논문 모두 사람 손 포즈를 로봇 명령으로 직접 옮기는 방식을 버리고 중간 표현을 둡니다. EgoLAP은 언어 행동과 동작 수준 추론, EgoJEPA는 잠재 행동입니다. EgoLAP(10-06)이 먼저 나왔습니다. |
| EgoVoice → ProactEgoMem | cross | 추정 | 둘 다 연속 에고 스트림에서 어시스턴트가 스스로 개입하는 '능동성(proactivity)'을 다룹니다. EgoVoice는 언제·무엇을 말할지를, ProactEgoMem은 알림·개입 수준의 기억 확보를 다룹니다. 상호 인용 여부는 확인하지 못했습니다. |
| GNR (Generative Neural Retargeting) → EgoCPT | cross | 추정 | 사람→로봇 정교 손 리타게팅이라는 같은 문제에 대조적으로 접근한다. GNR은 시연마다 최적화를 다시 푸는 대신 학습된 flow matching 생성 모델을 쓰고, EgoCPT는 시연 한 편마다 접촉 인지 최적화(포즈 정제·힘 배분 교대)를 수행한다. … |
| GNR (Generative Neural Retargeting) → EgoJEPA | cross | 추정 | 사람 손을 로봇 손으로 옮기는 같은 문제에서 반대 전략을 씁니다. GNR은 리타게팅을 생성 모델로 개선하고, EgoJEPA는 규칙 기반 리타게팅 자체를 잠재 행동으로 대체합니다. |
| EgoWholeView → EgoRayFormer | cross | 추정 | 머리 장착 하향 카메라로 착용자 몸을 추정하는 동시기 연구 (EgoWholeView 10-12 → EgoRayFormer 10월 말) |
| EgoCPT → EgoJEPA | cross | 추정 | 둘 다 에고 영상에서 정교 조작을 배우지만 리타게팅에 대한 입장이 반대다. EgoCPT는 접촉 인지 최적화로 리타게팅을 개선하고, EgoJEPA는 기하 매핑 리타게팅이 손 추적 오차를 제어로 전파한다며 잠재 행동으로 우회한다. 서로 비교했는지는 … |
| λ0 (기술 보고서판) → HuGe | cross | 추정 | 두 연구는 같은 설계를 씁니다. 사람 에고 데이터로 사전학습한 휴머노이드 VLA가 SONIC 전신 제어기의 모션 토큰과 손 명령을 출력하고, 둘 다 EgoDex·EgoVerse를 씁니다. λ0가 비교한 Ψ0를 HuGe는 정책 구조로 씁니다. 같은 … |
| NavAble → VISTA | cross | 추정 | 둘 다 시각장애·저시력(BLV) 사용자 보조라는 같은 응용 주제입니다(review.csv 메모의 관찰 주제 '시각장애인 보조'). NavAble은 2D 분할용 데이터·합성 파이프라인이고 VISTA는 VLM 보조 벤치마크라서 같은 연구가 아닙니다. … |
| EgoJEPA → EXE | cross | 추정 | 두 논문 모두 사람 에고 영상에서 체현 무관 '잠재 행동'을 학습해 로봇 정책으로 옮깁니다. EgoJEPA는 JEPA식 효과 인지 잠재 행동, EXE는 분해된 잠재 행동을 씁니다. 같은 시기의 경쟁 접근입니다. |
| V-JEPA Hand → DewHand | cross | 추정 | 두 논문 모두 단일 단계 월드 공간 손·카메라 추정 모델이고, 같은 HOT3D·ARCTIC에서 경쟁하는 동시기 연구입니다. arXiv ID 기준으로 V-JEPA Hand가 먼저 제출됐습니다. 서로 인용했는지는 확인하지 못했습니다. |
| EXE → Ego-CEVR | cross | 추정 | 두 논문 모두 사람 에고 영상으로 체현 간(cross-embodiment) 전이를 노립니다. EXE는 행동 표현, Ego-CEVR은 시각 표현을 다룹니다. Ego-CEVR은 내용을 확인하지 못해 제목만으로 추정했습니다. |

### 2.3 지도 노드와의 연결 (90개, 대기열 논문별)

`노드(관계·근거)` 형식. 지도 노드가 source인 간선은 "노드 → 이 논문", 대기열 논문이 source인 간선은 ↗로 표시했습니다.

| 논문 | 지도 노드 연결 |
|---|---|
| λ0 (기술 보고서판) (2610.18950) | EgoDex(trains_on·원문), EgoVerse(trains_on·원문), HOT3D(trains_on·원문), VITRA(trains_on·추정), ↗RopediaW0(cross·추정) |
| λ0 논문판 (Towards a General Humanoid…) (2610.00438) | EgoDex(trains_on·확인), EgoMI(cross·추정), EgoVerse(trains_on·확인), HOT3D(trains_on·확인) |
| HuGe (2610.34186) | EgoDex(trains_on·확인), EgoVerse(trains_on·확인), Masquerade(cross·추정), Xp10M(trains_on·확인) |
| V-JEPA Hand (2610.26780) | Ego4D(trains_on·원문), HOT3D(evaluates_on·원문), HaWoR(cites·원문), MANO(backbone·원문), MINT(cross·추정) |
| DewHand (2610.29936) | HOT3D(evaluates_on·원문), MINT(cross·추정), StableHand(compares·원문), VGGT(backbone·추정) |
| InfiniHand (2609.35743) | DynHaMR(compares·확인), EgoDex(evaluates_on·원문), HOT3D(evaluates_on·원문), HaWoR(compares·원문), LingBotMap(backbone·원문), MANO(backbone·원문), MINT(cross·추정) |
| EgoFound3R (2610.01210) | MANO(backbone·원문), MINT(cross·추정), VGGT(backbone·추정) |
| EgoContact (2610.39167) | Ego4D(evaluates_on·원문), Gaze2HOI(cross·추정) |
| RESELF (Seeing the World and the Self) (2609.01276) | EgoExo4D(trains_on·원문), OmniEgoCap(cross·추정), ReViV(cross·추정), VGGT(compares·원문) |
| EgoWholeView (2610.16256) | EgoBody3M(cross·추정), MANO(backbone·원문), OmniEgoCap(cross·추정) |
| MEgoVista (2609.16684) | DynHaMR(compares·원문), HaMeR(cites·원문), HaWoR(compares·원문), MANO(backbone·원문) |
| RoboCap (2610.07217) | EgoKit(cross·추정), MANO(backbone·원문), ↗HOMIEGen2(cross·추정) |
| EgoRayFormer (2610.26641) | EgoBody3M(cross·추정), OmniEgoCap(cross·추정) |
| EventEgoHands++ (2609.17189) | HOT3D(evaluates_on·추정) |
| Stream4D (2610.31320) | DynStream(cross·추정), STream3R(cross·추정) |
| From Sight to Foresight (2610.04139) | World2VLM(cross·추정) |
| EgoAlign (2610.16176) | Ego3DBench(cross·추정) |
| EgoPathBench (2609.16610) | Ego3DBench(cross·추정) |
| GazeLens (2610.28502) | G3Ego(cross·추정), LookFocusAct(cross·추정) |
| ProactEgoMem (2610.30089) | NeverLookBack(cross·추정), UCSBench(cross·추정), Whareformer(cross·추정) |
| APM-Bench (2609.37559) | UCSBench(cross·추정), ↗NeverLookBack(cross·추정) |
| VISTA (2610.22822) | R3D(cross·추정) |
| LEGO (2610.12442) | EgoXGen(compares·추정), Exo2EgoHOI(cross·추정) |
| Ego2Act (2610.01092) | Wh0(cross·추정) |
| Robotizing Human Videos (물리 일관) (2610.06137) | Phantom(cross·추정) |
| HuRo (2609.10706) | DROIDSLAM(backbone·확인), Ego4D(trains_on·확인), EgoDex(trains_on·확인), EgoVerse(trains_on·확인), HaWoR(backbone·확인), MANO(backbone·확인), Masquerade(cross·추정), Phantom(cross·추정), VITRA(cross·추정), ↗EgoMatrix(cross·추정) |
| GNR (Generative Neural Retargeting) (2610.12440) | HOT3D(evaluates_on·확인) |
| EgoCPT (2610.17572) | EgoDex(evaluates_on·확인), ↗EgoMatrix(cross·추정) |
| EXE (2610.33685) | ACEEgo0(cross·추정), EgoVLA(cross·추정) |
| EgoLAP (2610.08726) | EgoVLA(cross·추정) |
| EgoJEPA (2610.20904) | DexWM(cross·추정) |
| IronMind (2609.39403) | ACEEgo0(cross·추정) |
| EgoWild2Dex (2609.23755) | EgoScale(cross·추정), Masquerade(cross·추정) |
| DR-VLA (2610.18373) | VITRA(cross·추정) |
| ActiveAlign (2610.36859) | EgoMI(cross·추정) |

### 2.4 연결되지 않은 논문 (9편)

검토자가 근거 부족으로 간선을 모두 지웠거나 처음부터 붙일 관계가 없던 논문입니다. 대부분 범위 밖 후보이거나 내용 미확인입니다.

- EgoP²C (2610.22681) — 내용 미확인 (축은 제목 기준)
- EgoExo-Next (2610.04506) — 내용 미확인 (축은 제목 기준)
- EgoOmniWorld (2610.18499) — 범위 밖 후보 (3D 요소 없음)
- SOMA (2610.36384) — 내용 미확인 (축은 제목 기준)
- Plan-Bench (2610.18836) — 범위 밖 후보 (1인칭·3D 근거 없음)
- 에고 영상 임베딩+IMU 행동 인식 (2610.12926) — 범위 밖 후보 (임베딩+IMU 행동 인식)
- 에고·엑소 절차 이해 프레임워크 (2610.00069) — 범위 밖 후보 (절차 이해, 3D 없음)
- Decoupling Action (월드 시뮬레이션) (2610.27946) — 내용 미확인 (축은 제목 기준)
- ESCAPE (2610.23943) — 범위 밖 후보 (‘egocentric’=로봇 몸 깊이 센서)

## 3. 연구의 빈칸

4개 관점(축 내부·축 교차·평가와 데이터·성숙도와 재현성)에서 제안한 빈칸을 18개로 합치고, 비평가가 웹에서 "이미 채운 연구"를 찾아 판정했습니다. 웹 확인 결과 처음에 "열려 있음"이던 것 대부분이 **부분적으로 채워짐**으로 바뀌었고, 각 빈칸은 남은 부분으로 좁혔습니다.

| ID | 우선 | 판정 | 축 | 빈칸 |
|---|---|---|---|---|
| G2 | 높음 | 열려 있음 | 2·1∩2·3·B | 월드 좌표 에고 손·카메라 복원의 공용 평가 키트와 리더보드: 고정 분할, 정렬 방식별 지표, 학습 사용 표기, 같은 GPU 속도 |
| G1 | 높음 | 부분적으로 채워짐 | 2·5·3·8 | 사람 손 라벨 오차(통제 잡음·2026년 추정기·헤드 리그)가 로봇 정책 성공률을 얼마나 바꾸는지 잰 용량-반응 곡선 |
| G3 | 높음 | 부분적으로 채워짐 | 1∩2·1·2 | 착용자 몸·손가락 단위 양손·물체·장면을 한 월드 좌표에서 함께 채점하는 공개 프로토콜과 물리적 상호 일관성 지표 |
| G4 | 높음 | 부분적으로 채워짐 | 2·5·1∩2·3 | 에고 3D 접촉 GT·물리 지표, 접촉 전 메트릭 3D 접촉점 예측, 2D 대 3D 접촉 prior의 로봇 grasp 통제 비교 |
| G5 | 높음 | 부분적으로 채워짐 | 7·1∩2·2·4·1 | 주방 밖 여러 세션의 메트릭 3D 물체 이동 GT 벤치마크와, 사전 스캔 없이 손 잡기·놓기로 갱신하는 온라인 물체 원장 |
| G6 | 높음 | 부분적으로 채워짐 | 5·1∩2·B | 휴머노이드 에고 VLA(λ0·HuGe·EgoHumanoid·Ψ0) 교차 평가와, 트래커·비공개 전신 데이터를 단안 에고 몸+장면 의사라벨로 대체하는 통제 비교 |
| G7 | 높음 | 부분적으로 채워짐 | 6·5·2 | 에고 손·카메라 조건 월드 모델의 3D 행동 충실도 공통 벤치마크와, 에고 월드 모델을 정책 평가기로 쓸 때의 순위 상관 검증 |
| G8 | 높음 | 부분적으로 채워짐 | 1·B·2·7 | 에고 스트림에서 정적 배경·양손·물체 인스턴스를 인과적으로 함께 내는 메트릭 4D 재구성과, 연산 등급별 정확도-지연 평가 규칙 |
| G9 | 높음 | 부분적으로 채워짐 | 1∩2·1·2·3 | 물체 마스크 없이 관절·변형 물체까지 다루는 에고 손-물체 4D 통합 모델과 기하 GT 벤치마크 |
| G10 | 중간 | 부분적으로 채워짐 | 3·2·B | 머리 리그 구성(대수·배치·화각)을 통제 비교하고 실외·장시간·다인 메트릭 손·몸 GT를 갖춘 교차 기기 캡처 벤치마크 |
| G11 | 중간 | 부분적으로 채워짐 | 9·7 | 시선 체류·재방문으로 '무엇을 기억할지' 정하는 예산 제한 3D 물체 단위 메모리 (축 9 × 축 7) |
| G12 | 중간 | 부분적으로 채워짐 | 6·7 | 손이 옮긴 물체가 재방문 때도 그 자리에 있는가: 실제 에고 손 조작 사건 기반 재방문 일관성 평가와 접촉 이벤트 메모리 월드 모델 (축 6 × 축 7) |
| G13 | 중간 | 부분적으로 채워짐 | 5·2·8 | 사람→로봇 정교 조작 전이 갈래(리타게팅, 리타게팅 생략, 영상 로봇화 편집)를 같은 사람 데이터·같은 로봇 손·같은 정책에서 맞붙인 비교 |
| G14 | 중간 | 부분적으로 채워짐 | B·1·2 | 기하 백본 선택과 근접 손 가림 견고성: 손 헤드를 고정하고 백본만 바꾼 통제 실험과 손 점유율 구간별 스트레스 평가 |
| G16 | 중간 | 부분적으로 채워짐 | 4·9·2·7 | 3D 시선으로 지시 대상을, 착용자 몸 자세로 머리/몸통 기준틀을 정하는 자기중심 메트릭 질의 벤치마크 ('이거 얼마나 멀어?', '내 왼쪽 뒤의 컵') |
| G17 | 중간 | 부분적으로 채워짐 | 8·6·2 | 손·카메라 제어 생성 월드 모델의 에고 영상을 조건 라벨째 3D 손·기하 지각 모델 학습에 쓰고 실제 벤치마크 향상을 검증하는 연구 |
| G15 | 낮음 | 부분적으로 채워짐 | 4·1·1∩2·B | 에고 손·옮겨진 물체에 대한 메트릭 4D 질의에서 같은 기반 VLM의 도구 호출형 대 내재화형 비교 |
| G18 | 낮음 | 부분적으로 채워짐 | 9·1·3 | Aria 밖으로 3D 시선 넓히기: 4D 재구성으로 2D 시선·시선 광선을 손·든 물체 위 3D 고정점으로 올리고, 비Aria 평가 세트와 공통 3D 지표 만들기 |

#### G2. 월드 좌표 에고 손·카메라 복원의 공용 평가 키트와 리더보드: 고정 분할, 정렬 방식별 지표, 학습 사용 표기, 같은 GPU 속도

*열려 있음 · 우선 높음 · 축 2·1∩2·3·B*

월드 좌표 에고 손 복원 방법들(V-JEPA Hand, DewHand, InfiniHand, EgoFound3R, MEgoVista, StableHand, MINT, EgoHand 등)을 같은 분할·같은 정렬 방식·같은 하드웨어로 다시 돌려 한 표에 올리는 공용 키트나 리더보드가 없습니다. 논문마다 분할(ARCTIC 공식 validation, HaWoR의 HOT3D validation 분할, EgoStandard, OakInk-v2·TACO·HOI4D), 지표(coverage-aware MPJPE, WA-MPJPE, PA, W-MPJPE), 학습 사용 여부, 속도 조건(클립 입력 93.4 FPS 대 스트리밍 11.19 FPS)이 달라 수치를 비교할 수 없습니다. HOT3D에는 숨긴 테스트 GT와 eval.ai 서버를 쓰는 Multiview Egocentric Hand Tracking Challenge가 있지만, 입력이 동기화된 흑백 스트림 2~4개인 다시점 손 추적용이라 단안 월드 궤적, 카메라 ATE·스케일, 화면 이탈 처리, 속도는 채점하지 않습니다. 논문들이 쓰는 'HaWoR HOT3D validation split'은 학습 참가자에서 떼어 낸 분할로 보여(추정) 공식 테스트와도 이어지지 않습니다.

부분적으로 채운 연구:

- HOT3D 공식 테스트 분할 + Multiview Egocentric Hand Tracking Challenge (https://github.com/facebookresearch/hot3d , https://github.com/facebookresearch/hand_tracking_toolkit ; 지도 노드 HOT3D, arXiv 2411.19167) (GT 비공개 테스트 참가자 분할과 eval.ai 평가 서버, 포즈·형상 두 트랙. 흑백 다시점 입력용이고 공식 검증 세트 없음)
- EgoXperience (arXiv 2610.26625, 지도 노드 EgoXperience, Ropedia 기술 보고서) (한 논문 안에서 HaWoR·Dyn-HaMR·MINT를 같은 조건으로 비교)
- StableHand → DewHand 비교 사슬 (arXiv 2605.18553 지도 노드 StableHand, arXiv 2610.29936 대기열) (신작끼리의 직접 비교 일부. DewHand 보고 기준 StableHand 대비 HOT3D 32.9→28.4 mm, ARCTIC 76.2→36.2 mm)
- V-JEPA Hand (arXiv 2610.26780, 대기열, 프리프린트) (HaWoR의 HOT3D validation 분할을 재사용해 사실상의 공용 분할 일부를 형성)
- EgoSurgHands (https://neurips.cc/virtual/2026/poster/139540 , NeurIPS 2026 포스터) (손 복원기 6개를 같은 조건으로 평가한 에고 3D 손 벤치마크. 개방 수술 훈련 분야 한정, 월드 좌표 평가 여부 미확인)

**채우려면** — (1) 분할 고정: HOT3D 공식 테스트(숨긴 GT와 평가 서버 유지)에 단안 RGB 월드 좌표 트랙을 추가하고, ARCTIC 에고 뷰·EgoDex·H2O·HOI4D·TACO·OakInk-v2의 test 분할을 고정하며 방법마다 '학습 사용/제로샷' 표기를 의무화합니다. (2) 지표 묶음: 정렬 없는 W-MPJPE(메트릭 스케일 포함), 시퀀스 강체 정렬 WA-MPJPE, 프레임 PA-MPJPE, 화면 안/밖 프레임별 오차와 손 존재 검출 F1·coverage, 카메라 ATE·스케일 오차, 지터, 분당 드리프트. (3) 속도: 같은 GPU·같은 해상도에서 클립 처리와 인과적 스트리밍 처리를 나눠 잽니다. (4) 공개 체크포인트로 재실행 가능한 결과만 등록하고, 첫 판으로 HaWoR, Dyn-HaMR, StableHand, MINT, V-JEPA Hand, DewHand, InfiniHand, EgoFound3R를 같은 조건에서 다시 돌린 단일 표를 냅니다. 이 표는 G1의 라벨 품질 축과 G7·G17의 고정 재추정기 선택에도 쓰입니다.

#### G1. 사람 손 라벨 오차(통제 잡음·2026년 추정기·헤드 리그)가 로봇 정책 성공률을 얼마나 바꾸는지 잰 용량-반응 곡선

*부분적으로 채워짐 · 우선 높음 · 축 2·5·3·8*

영상과 정책 레시피를 고정하고 사람 손 행동 라벨에 위치·손목 회전·지터·결측·스케일 오차를 단계적으로 넣었을 때 로봇 성공률이 어떻게 변하는지 보여 주는 용량-반응 곡선이 없습니다. 'What Matters When Cotraining…'(2606.06627)은 EgoExo4D 다시점 삼각측량 라벨(TriHands)과 단안 HaWoR 라벨을, HumanEgo(2605.24934)는 손 추적기 선택(검출률 66.5%인 MediaPipe는 실로봇 0%)을 비교했지만, 둘 다 라벨 출처 몇 개를 바꾼 비교이지 오차 크기를 연속으로 바꾼 실험이 아닙니다. 2026년 월드 좌표 추정기(MINT, EgoHand, DewHand, InfiniHand, V-JEPA Hand)와 헤드 리그 라벨(RoboCap, MEgoVista, EgoWholeView)을 같은 정책에서 비교한 결과, 파지와 손가락 정교 조작의 민감도 차이, 시간당 수집 비용도 보고된 적이 없습니다. HumanEgo는 포즈 정확도만으로는 하류 정책 성공을 잘 예측하지 못한다고 보고해, x축에 MPJPE 하나만 두면 안 된다는 점도 드러났습니다.

부분적으로 채운 연구:

- What Matters When Cotraining Robot Manipulation Policies on Everyday Human Videos? (arXiv 2606.06627, 2026-06, 게재처 미확인) (EgoExo4D 요리 영상 532개에서 삼각측량한 손 라벨 TriHands와 단안 HaWoR 라벨을 비교해 '멀티뷰 대 단안 라벨' 부분을 다룸. 조건별 성공률 수치는 보지 못함)
- HumanEgo (arXiv 2605.24934, 게재처 미확인) (손 추적기 선택 → 정책 성공률 비교. 정렬 후 관절 오차가 비슷한 두 추정기, 검출률 66.5% MediaPipe의 실로봇 0%)
- EgoCPT (arXiv 2610.17572, 대기열, 프리프린트) (잡음 있는 EgoDex 재구성 입력과 깨끗한 TACO 모캡 입력에서 접촉 인지 최적화 리타게팅을 평가. 입력 품질 두 수준이 있으나 데이터가 서로 달라 라벨 오차만 바꾼 통제 비교는 아님)
- EgoContact (arXiv 2610.39167, 대기열, 프리프린트) (정책 RAM을 고정하고 메모리 뱅크 데이터만 바꿔 실로봇 grasp 16%→58%. 바꾼 것은 2D 접촉점이라 3D 손 라벨 오차는 변수가 아님)
- λ0 (arXiv 2610.18950, 대기열, 기술 보고서) (1·2단계 제거 시 62.5%→15.0%. 사람 데이터 유무 효과이지 라벨 품질 효과가 아님)
- 상대 손목 이동 기사 (https://aiweekly.co/alerts/relative-wrist-translation-triples-bimanual-robot-success-rate , 원 논문 미확인) (잡음 많은 6DoF 손 포즈 대신 상대 손목 이동을 쓰자 양팔 성공률 12.50%→38.33%. 라벨 잡음의 간접 영향)

**채우려면** — 영상(EgoDex 부분집합 등)과 정책 레시피(VITRA·EgoVLA 또는 λ0식 3단계)를 고정하고 행동 라벨만 바꿔 사전학습합니다. 라벨 조건은 (1) EgoDex 장비 라벨 (2) HaWoR (3) MINT·EgoHand·DewHand·InfiniHand·V-JEPA Hand (4) 헤드 리그 다시점 라벨(RoboCap·MEgoVista식) (5) 모캡 GT가 있는 구간의 GT (6) 기준 라벨에 위치 5/10/20 mm, 손목 회전 오차, 시간 지터, 화면 밖 결측, 스케일 오차를 단계별로 넣은 버전입니다. 같은 시뮬레이션·실로봇 과제에서 성공률을 재고, x축에 W-MPJPE와 함께 검출률·coverage·시간 안정성을 둔 다변량 민감도 분석을 보고합니다. 파지 과제와 손가락 정교 조작 과제를 나누고 시간당 수집 비용(리그 대 단안)을 함께 내며, 'What Matters'의 TriHands 대 HaWoR 결과와 HumanEgo의 추적기 비교를 이 곡선 위의 점으로 재현해 일관성을 확인합니다. 라벨 품질 축은 G2 키트로 잽니다.

#### G3. 착용자 몸·손가락 단위 양손·물체·장면을 한 월드 좌표에서 함께 채점하는 공개 프로토콜과 물리적 상호 일관성 지표

*부분적으로 채워짐 · 우선 높음 · 축 1∩2·1·2*

단안 에고 RGB에서 카메라·조밀 깊이·손가락 관절 양손·물체·착용자 몸을 한 메트릭 월드 좌표로 함께 채점하는 공개 평가 분할과 스크립트가 없습니다. ADT(2306.06362)에는 기기 6DoF·물체 398개 6DoF·3D 사람 포즈·깊이·3D 시선·디지털 트윈이 함께 있지만 검색 결과에서 손가락 관절 손 GT는 보이지 않았고, HOT3D는 손·물체·카메라는 있으나 몸·장면 GT가 보이지 않았으며, EgoXperience의 EgoX-Bench는 몸이 없고 데이터(EgoXData6M)가 'coming soon'입니다. 그래서 EgoXperience·ReViV·RESELF·DewHand가 각자 다른 데이터(EgoX-Bench·HOT3D / ADT·HOT3D / EE4D-JSM / HOT3D·ARCTIC)로 평가되어 서로 비교되지 않습니다. 손-물체 관통 지표는 HOI 문헌(ContactOpt)에 있지만, 복원된 장면과 복원된 손·몸 사이의 관통·접촉 시 거리·발-지면 접촉·스케일 일치도를 공용으로 정의해 함께 보고하는 프로토콜은 찾지 못했습니다.

부분적으로 채운 연구:

- ADT (arXiv 2306.06362, 지도 노드 ADT, ICCV 2023 오픈액세스 PDF 기준) (카메라 6DoF·물체 398개 6DoF·3D 사람 포즈·깊이 지도·3D 시선·메트릭 디지털 트윈을 한 좌표계에 제공. 손가락 관절 손 GT는 확인 못 함)
- HOT3D (arXiv 2411.19167, 지도 노드 HOT3D, 원문 CVPR 2025) (19명·강체 물체 33개의 손·물체·카메라 3D 포즈와 3D 모델 GT. 몸·장면 GT는 검색 결과에 없음)
- EgoXperience / EgoX-Bench (arXiv 2610.26625, 지도 노드 EgoXperience·EgoXData6M, Ropedia 기술 보고서) (카메라·장면·손·물체 공동 평가 전용 세트. 몸 없음, 데이터 미공개)
- ReViV (arXiv 2607.17790, 지도 노드 ReViV, ECCV 2026) (몸·손·깊이·카메라·시선을 함께 복원하는 공개 기준선, ADT·HOT3D 평가. 물체 없음)
- RESELF (arXiv 2609.01276, 대기열, 프리프린트) (깊이·카메라·착용자 SMPL-X 전신 공동 복원과 EE4D-JSM 평가. 손·물체 채점 없음)
- ContactOpt (arXiv 2104.07267, CVPR 2021, data/hoi.csv) (손-물체 관통·떠 있음 지표. 장면·몸에는 적용되지 않음)
- EgoFound3R (arXiv 2610.01210, 대기열, 프리프린트) (월드 좌표 손의 점 단위 접촉 여부·접촉면 거리 예측. 지표로 보고하지는 않음)

**채우려면** — (1) ADT 장면에 HOT3D 수준의 손가락 관절 손 GT를 더해(같은 공간·기기로 추가 녹화하거나 기존 시퀀스 일부에 다시점 손 주석) 카메라·깊이·양손·전신·물체 6DoF가 한 시퀀스에 모두 있는 공개 평가 분할을 만듭니다. (2) 새 촬영 전이라도 ADT·HOT3D·EE4D-JSM을 한 평가 스크립트로 묶어 카메라 ATE, 깊이 AbsRel, 손 W-MPJPE, 몸 MPJPE, 물체 ADD를 같은 월드 좌표 표에 보고하고, EgoXperience·ReViV·RESELF·DewHand를 같은 입력으로 재평가합니다. (3) 상호 일관성 지표로 손-장면 관통 깊이, 접촉 시 손-표면 거리, 발-지면 접촉 일관성(미끄러짐), 손·몸·장면 스케일 일치도를 정의해 ContactOpt식 손-물체 관통과 같은 형식으로 보고합니다. 물체에는 '첫 프레임 마스크 제공/미제공' 조건을 두고, 이 표 위에서 몸·손·물체·장면을 동시에 내는 단일 피드포워드 기준선을 만듭니다.

#### G4. 에고 3D 접촉 GT·물리 지표, 접촉 전 메트릭 3D 접촉점 예측, 2D 대 3D 접촉 prior의 로봇 grasp 통제 비교

*부분적으로 채워짐 · 우선 높음 · 축 2·5·1∩2·3*

에고 영상에서 접촉이 일어나기 전에 물체 표면 위 손가락별 접촉점을 메트릭 3D(mm)로 예측하고 채점하는 과제, 그리고 같은 정책에 2D 접촉 prior와 3D 접촉 prior를 각각 넣어 grasp 성공률을 비교한 통제 실험이 없습니다. MAPLE(2504.06084)은 접촉 전 프레임에서 접촉점과 3D 손 포즈를 예측해 다지 로봇 손 정책에 썼지만 접촉점은 이미지 좌표로 보이고, EgoChoir(2405.13659)는 3D 접촉·affordance 영역을 예측하지만 3D 물체를 입력으로 받는 영역 단위 추정이며, EgoContact(2610.39167)는 2D 픽셀 접촉점만으로 실로봇 grasp 16%→58%를 보였습니다. 또 HOT3D·ARCTIC·OakInk-v2의 물체 메시로 만든 프레임별 3D 접촉 GT와 접촉 precision/recall·관통 깊이 지표를 월드 좌표 에고 손 방법들(EgoFound3R, DewHand, InfiniHand, V-JEPA Hand)에 같은 기준으로 적용한 평가판이 없어, 관절 오차가 낮으면 접촉도 맞는지 알 수 없습니다.

부분적으로 채운 연구:

- MAPLE (arXiv 2504.06084, 2025, 게재처 미확인) (접촉 프레임에서 HaMeR로 MANO 손 포즈를 구하고 접촉 위치를 이른 예측 프레임까지 추적해, 이미지 한 장에서 접촉점과 3D 손 포즈를 예측하는 인코더를 학습하고 다지 로봇 손 확산 정책에 사용. 접촉점은 이미지 좌표로 보임)
- EgoChoir (arXiv 2405.13659, NeurIPS 2024) (Ego-Exo4D·GIMO 에고 영상에 3D 사람 접촉·물체 affordance 영역 라벨을 붙이고 예측. 3D 물체 입력 필요, 영역 단위)
- EgoContact (arXiv 2610.39167, 대기열, 프리프린트) (Ego4D 이벤트 22,523개의 2D 접촉점, RAM 메모리 뱅크 교체로 grasp 시뮬 14.2%→31.2%, 실로봇 16%→58%)
- EgoFound3R (arXiv 2610.01210, 대기열, 프리프린트) (현재 프레임의 손 점 단위 3D 접촉 여부·접촉면 거리 예측. 평가는 MPJPE·속도뿐)
- Gaze2HOI (arXiv 2610.27877, 지도 노드 Gaze2HOI) (접촉 기하를 먼저 예측하는 접촉 전 예측의 일부. 3D 손·물체·장면 입력 필요, 로봇 실험 없음)
- Grasp-and-Lift (arXiv 2601.18121, data/hoi.csv) (영상 복원 손-물체 시연의 잡기·들기 물리 성공을 지표로 사용. DexYCB·HO-3D 기준)
- EgoCPT (arXiv 2610.17572, 대기열, 프리프린트) (에고 영상 한 편과 기준 손 포즈에서 포즈 정제와 힘 배분을 번갈아 푸는 접촉 인지 최적화로 로봇 손이 실행할 접촉·힘·운동을 다시 찾음. 5개 조작 과제. 2D 대 3D prior 비교는 아님)

**채우려면** — (a) 평가판: HOT3D·ARCTIC·OakInk-v2의 물체 메시와 손 GT로 프레임별 3D 접촉 영역 GT를 만들고 접촉 precision/recall, 관통 깊이, 접촉 시작·종료 시점 오차, 접촉 지속 지표를 정의해 EgoFound3R·DewHand·InfiniHand·V-JEPA Hand를 같은 기준으로 채점하며, 관절 오차와 접촉 정확도의 상관을 보고합니다. (b) 과제: EgoContact와 같은 이벤트 정의로 접촉 0.5초·1초 전 프레임에서 물체 메시 없이 RGB(필요하면 시선 추가)만으로 손가락별 메트릭 3D 접촉점을 예측하게 하고 mm 오차로 채점합니다. EgoContact 이벤트 일부를 월드 좌표 손 복원과 VGGT 계열 깊이로 3D로 올린 'EgoContact-3D' 부분집합을 만들고, 리프팅 오차는 HOT3D·ARCTIC에서 검증합니다. (c) 통제 실험: 같은 RAM 파이프라인(또는 MAPLE식 확산 정책)에 2D 접촉 prior와 3D 접촉 prior를 각각 넣어 평행 그리퍼와 다지 손(2610.12440·EgoCPT가 겨냥하는 방향)에서 grasp 성공률을 비교합니다.

#### G5. 주방 밖 여러 세션의 메트릭 3D 물체 이동 GT 벤치마크와, 사전 스캔 없이 손 잡기·놓기로 갱신하는 온라인 물체 원장

*부분적으로 채워짐 · 우선 높음 · 축 7·1∩2·2·4·1*

집 전체·사무실·작업장처럼 주방 밖 공간을 며칠·여러 세션에 걸쳐 녹화하고 물체별 메트릭 3D 위치 GT와 손 이동 이벤트 라벨을 붙인 벤치마크가 없습니다. HD-EPIC(2502.04144)은 주방 9곳·여러 날·41시간에 물체 이동 2만 건을 3D 디지털 트윈에 정렬했지만 주방에 한정되고 평가가 VQA 형식이며, Lost & Found(2411.19162)는 손 위치·카메라 포즈로 상호작용 구간을 찾아 옮겨진 물체의 6DoF로 3D 장면 그래프를 갱신하지만 사전 3D 스캔이 필요하고 물체 9개·96 시퀀스 규모입니다. APM-Bench·ProactEgoMem 같은 세션 간·스트리밍 메모리 벤치는 QA 형식이고 3D 기하 요소가 약해, 이동 판정 precision·recall(정지 물체 오탐 포함), 재배치 후 3D 위치 오차, 시간당 메모리·프레임당 지연을 QA 정확도와 분리해 재는 지표가 없습니다. 사전 스캔 없이 스트리밍 월드 좌표 손과 스트리밍 기하 백본으로 장시간 물체 원장을 온라인 갱신하는 시스템도 찾지 못했습니다.

부분적으로 채운 연구:

- Lost & Found (arXiv 2411.19162, 검색 요약 기준 IEEE RA-L 2025) (Aria 에고 영상의 손 위치·카메라 포즈로 상호작용 구간을 찾고 옮겨진 물체 6DoF를 추적해 3D 장면 그래프 갱신, 차선 대비 이동 오차 34%·회전 오차 56% 감소. 사전 스캔 필요, 물체 9개·96 시퀀스)
- HD-EPIC (arXiv 2502.04144, 지도 노드 HDEPIC, CVPR 2025) (주방 9곳·여러 날·41시간, 고정물 413개 디지털 트윈, 물체 이동 2만 건과 3D로 올린 물체 마스크 3.7만 개를 트윈에 정렬. 주방 한정, VQA 평가)
- Whareformer (arXiv 2607.08537, 지도 노드, ECCV 2026) · OSNOM (arXiv 2404.05072, 지도 노드, 3DV 2025) (긴 에고 영상에서 무엇이 어디 있는지 추적. 손 이벤트 사용·온라인 여부 미확인)
- APM-Bench (arXiv 2609.37559, 대기열, 2차 기사 기준) (104 궤적·549 세션·2,719 문항의 세션 간 메모리 벤치, 개체 상태 추적 포함. 3D 기하 요소 약함)
- ProactEgoMem (arXiv 2610.30089, 대기열, 2차 출처 요약) (스트리밍 에고 영상에서 물체 상태 추적·물체 위치 추적 과제와 능동성 단계. 메트릭 3D 요소 미확인)
- IGGT4D (arXiv 2607.19228, 지도 노드) (가림·재등장에도 물체 정체성을 유지하는 스트리밍 기하 백본. 에고 특화 아님)
- NeverLookBack (arXiv 2610.10538, 지도 노드, 프리프린트) (FastVGGT 포즈 위 오프라인 3D 물체 메모리, VQ3D 중앙값 0.99 m)

**채우려면** — 벤치마크: 디지털 트윈 GT를 만들 수 있는 주방 밖 공간(집 전체, 사무실, 작업장)을 며칠에 걸쳐 여러 세션으로 녹화하고 공통 지도에 정렬해, 물체별 3D 위치 GT와 손으로 옮긴 사건마다 '집은 위치·놓은 위치·시각' 이벤트 라벨을 붙입니다. 프레임을 한 번만 보는 온라인 조건에서 (1) 세션 간 재위치추정 성공률 (2) 이동 판정 precision·recall·F1과 정지 물체 오탐률 (3) 재배치 후 3D 위치 오차와 '어디 뒀지' 질의 오차 (4) 시간당 메모리 크기·프레임당 지연을 QA 정확도와 분리해 보고합니다. 시스템: 스트리밍 월드 좌표 손(InfiniHand류)과 점 단위 접촉(EgoFound3R류)으로 잡기·놓기를 검출하고, LingBot-Map·IGGT4D 좌표계의 물체 원장을 사전 스캔 없이 갱신합니다. 같은 데이터에서 Lost & Found(사전 스캔), NeverLookBack(오프라인), Whareformer, UCS-Bench DirectMe와 비교하고 손 이벤트 유무와 카메라 좌표 손 대 월드 좌표 손을 어블레이션합니다.

#### G6. 휴머노이드 에고 VLA(λ0·HuGe·EgoHumanoid·Ψ0) 교차 평가와, 트래커·비공개 전신 데이터를 단안 에고 몸+장면 의사라벨로 대체하는 통제 비교

*부분적으로 채워짐 · 우선 높음 · 축 5·1∩2·B*

에고 사람 데이터로 사전학습한 휴머노이드 VLA들을 같은 전신 제어기·같은 미세조정 예산으로 같은 벤치마크에서 평가한 교차표가 없습니다. λ0(2610.18950)는 SIMPLE 90.0%·실제 4과제 62.5%를, HuGe(2610.34186)는 HumanoidArena 평균 66.67/65.00/54.05를 보고하고, EgoHumanoid(2602.10106)는 자기 G1 과제 4개에서 로봇 전용 기준과만 비교해, 확인된 상호 비교는 λ0 대 Ψ0 정도입니다. 또 단안 에고 영상에서 착용자 전신과 메트릭 장면을 복원하는 RESELF·ReViV는 복원 지표로만 평가되었고, 그 의사라벨이 트래커·비공개 데이터(HumanVerse 500시간, EgoHumanoid 장비 기록)를 대체·보강할 수 있는지 정책 성공률로 검증한 연구는 없습니다. VideoMimic(2505.03729)은 단안 영상의 몸+장면 복원을 G1 전신 정책으로 옮겼지만 3인칭 영상·이동 기술이고 VLA가 아니라 이 빈칸을 채우지 않습니다.

부분적으로 채운 연구:

- EgoHumanoid (arXiv 2602.10106, 2026-02, 게재 미확인) (VR 헤드셋·몸 트래커·머리 카메라로 로봇 없이 모은 에고 전신 시연과 소량 로봇 데이터를 시점·행동 정렬로 공동학습. G1 in-the-wild 4과제에서 로봇 전용 대비 일반화 최대 51% 향상)
- Ψ0 (arXiv 2603.12263, 검색 요약만 확인) (대규모 에고 사람 영상 사전학습 → 로봇 사후학습. λ0가 비교 대상으로 써서 에고 사전학습 VLA끼리의 비교 일부가 생김)
- VideoMimic (arXiv 2505.03729, 게재처 미확인) (단안 3인칭 영상에서 사람 동작과 장면을 같은 월드 좌표로 복원하고 시뮬 RL로 G1 전신 정책 학습, 영상 123개로 계단·앉기)
- Towards a General Humanoid Loco-Manipulation Model… (arXiv 2610.00438, 대기열, 프리프린트, λ0와 같은 연구) (전신 사람 데이터가 늘수록 검증 손실 감소·실제 진행도 향상이라는 스케일링 분석. 비공개 데이터라 재현 불가)
- HuGe (arXiv 2610.34186, 대기열, 프리프린트) (공개 에고 데이터에 시뮬 재생 의사 고유감각과 팔 재렌더링을 붙여 사람 영상에 없는 신호를 의사라벨로 보충)
- MINT EgoPipeline (지도 노드 MINTEgoPipe) · EgoSim (arXiv 2604.01001, 지도 노드) (공개 에고 영상의 손·카메라 의사라벨 1,021시간 / 장면·카메라·손 의사라벨 파이프라인. 몸·휴머노이드로 이어지지 않음)

**채우려면** — (1) 교차표: λ0, HuGe, EgoHumanoid, Ψ0(IronMind는 내용 확인 후)와 π0.5·GR00T N1.6을 같은 SONIC 전신 제어기와 같은 미세조정 예산으로 SIMPLE과 HumanoidArena 양쪽에서 평가합니다(체크포인트 공개 여부부터 확인). (2) 대체 실험: RESELF·ReViV를 EgoExo4D·EgoDex 같은 공개 에고 영상에 돌려 SMPL-X 전신·메트릭 장면·카메라 의사라벨을 만들고 SONIC 모션 토큰으로 바꿔, λ0의 2단계 데이터(또는 EgoHumanoid식 트래커 데이터)를 같은 시간 분량으로 대체·보강했을 때 SIMPLE과 실제 G1 성공률을 비교합니다. (3) 공개 데이터만으로 λ0 레시피를 재현해 사람 데이터 0/50/200/500/2,000시간 스케일링 곡선을 냅니다. (4) 발 미끄러짐·장면 관통·스케일 오차가 이동 과제와 조작 과제에 주는 영향을 나눠 재고, 수 미터 이상 이동하는 실외 과제를 평가에 넣습니다.

#### G7. 에고 손·카메라 조건 월드 모델의 3D 행동 충실도 공통 벤치마크와, 에고 월드 모델을 정책 평가기로 쓸 때의 순위 상관 검증

*부분적으로 채워짐 · 우선 높음 · 축 6·5·2*

3D 손(MANO)·카메라 궤적을 조건으로 받는 에고 월드 모델의 생성 영상에서 고정 추정기로 손과 카메라를 다시 추정해 조건 대비 W-MPJPE·카메라 ATE·접촉 이벤트 일치를 재는 공통 벤치마크가 없습니다. EgoForge의 X-Ego 벤치는 PSNR·SSIM·LPIPS·FVD·flow MSE를, Ego2Act는 참조 없는 목표 완수 판정기를, H2R-Bench는 5개 차원 평가를, 2610.12464는 2D 손·물체 마스크 IoU를 써서 3D 행동 충실도를 직접 재지 않습니다. 월드 모델 안의 정책 성공률이 실제 성공률·순위와 맞는지는 WorldEval(Pearson 0.79)·WEAVER(ρ=0.870)·WorldGym·OSCAR 등 로봇 영상 월드 모델에서 이미 검증되었지만, 사람 에고 손 조건이나 에고 영상 사전학습 월드 모델에서 같은 검증을 한 결과는 찾지 못했습니다. 44k시간 에고 영상으로 사전학습한 DreamDojo도 정책 평가를 응용으로 들 뿐 README·평가 문서에 상관 수치가 없었습니다.

부분적으로 채운 연구:

- WorldEval (arXiv 2505.19017) (로봇 월드 모델 롤아웃으로 매긴 정책 성능과 실제 성능의 Pearson 0.79, 순위 일치 지표 MMRV)
- WEAVER (arXiv 2606.13672) (실제 하드웨어 5개 조작 과제에서 정책 평가 결과와 실제 성공률 ρ=0.870)
- WorldGym (arXiv 2506.00613) · OSCAR (arXiv 2606.04463) · dWorldEval (arXiv 2604.22152) · GigaWorld-1 (arXiv 2607.02642) (로봇 정책 평가기 계열과 실제·월드 모델 성공률 순위 상관의 지표화)
- DreamDojo (arXiv 2602.06949, README 기준 ICML 2026) (44k시간 사람 에고 영상 사전학습 후 로봇 행동 공간으로 후학습한 월드 모델, 정책 평가를 응용으로 제시. 상관 수치는 보지 못함)
- Ego2Act (arXiv 2610.01092, 대기열, 프리프린트) (실제 과제 110개·영상 2,640개로 1인칭 손 조작 생성의 목표 완수·물리 타당성을 Ego2ActJudge로 평가, 2차 요약 기준 판정기-인간 상관 0.69. 3D 재추정 없음)
- EgoForge (arXiv 2603.20169) (Nymeria·Ego-Exo4D 기반 X-Ego 벤치, 지표는 PSNR·SSIM·LPIPS·FVD·flow MSE)
- H2R-Bench (arXiv 2608.13049) (사람→로봇 조작 영상 생성의 과제 목표·행동 동역학·기능적 접촉·체현 일관성·영상 품질 평가)
- 2610.12464 (제목 미확인) (에고 미래 예측에서 손·조작 물체 마스크 IoU로 2D 행동 충실도 측정, 손 골격 프롬프트 효과 보고)

**채우려면** — (1) 행동 충실도 벤치마크: HOT3D·ARCTIC 클립의 GT 카메라 궤적과 MANO 손 궤적을 공통 조건 세트로 DWM·HandsOnWorld·GenReality·SparseHandJoints·EgoGenesis·P3WAM 등에 넣고, 생성 영상에 고정된 손·카메라 추정기 하나(G2 키트에서 선택)를 돌려 조건 대비 W-MPJPE, 카메라 ATE, 접촉 시작·종료 이벤트 일치율을 FVD와 함께 보고합니다. (2) 정책 평가기 검증: 실로봇 성공률이 측정된 정책 여러 개(사람 손 행동을 내는 EgoVLA 계열 등, 행동 공간은 확인 필요)를 ADT·HOT3D 디지털 트윈 장면 조건으로 에고 월드 모델(DreamDojo 포함)에서 롤아웃하고, 생성 영상에서 손·물체 포즈를 재추정해 성공을 판정한 뒤 WorldEval식 Pearson·MMRV와 Spearman·Kendall 순위 상관을 보고합니다. 행동 충실도가 낮은 롤아웃을 걸렀을 때 상관이 얼마나 오르는지도 봅니다. (3) 각 모델의 생성 영상으로 같은 정책을 학습시켜(Wh0식) FVD·행동 충실도·성공률의 상관을 검증합니다.

#### G8. 에고 스트림에서 정적 배경·양손·물체 인스턴스를 인과적으로 함께 내는 메트릭 4D 재구성과, 연산 등급별 정확도-지연 평가 규칙

*부분적으로 채워짐 · 우선 높음 · 축 1·B·2·7*

단안 에고 스트림을 인과적으로 처리하면서 정적 배경, 양손 MANO, 물체 인스턴스(6DoF 또는 기하)를 한 모델에서 동시에 내는 연구가 없습니다. Hand3R(2602.03200)는 손 궤적과 메트릭 조밀 장면을 온라인으로 함께 복원한다고 주장하지만 물체 인스턴스를 내지 않고, EgoXperience는 카메라·손·깊이·물체를 내지만 스트리밍 여부가 기록에 없으며, IGGT4D는 스트리밍 인스턴스 기하를 내지만 에고 특화가 아니고 손 prior가 없고, InfiniHand는 손·카메라만 스트리밍으로 냅니다. 속도 보고도 V-JEPA Hand 93.4 FPS(클립 입력, RTX A6000), EgoFound3R 28.69 FPS(H20), InfiniHand 11.19 FPS(스트리밍), Hand-4DGS 약 60 FPS, DewHand 'SLAM 기반보다 2.6–3.7배'처럼 미래 프레임 사용 여부와 하드웨어가 섞여 비교할 수 없습니다. 입력 인과성(허용 지연 k프레임)을 명시하고 연산 등급별 p50·p99 지연, 장시간 메모리 증가, 프레임당 에너지를 정확도와 함께 재는 평가 규칙도 없습니다.

부분적으로 채운 연구:

- Hand3R (arXiv 2602.03200, 2026-02, 게재처 미확인) (단안 스트림에서 손 궤적과 메트릭 조밀 장면을 한 번의 forward pass로 온라인 공동 복원한다고 주장. 물체 인스턴스 없음, 에고 특화·속도 미확인)
- EgoXperience (arXiv 2610.26625, 지도 노드) (카메라·손·깊이·물체 포즈를 한 모델에서 출력, 자체 보고 카메라 68.9%·손 65.6%·깊이 42.9% 오차 감소. 스트리밍·인과 처리 여부 기록 없음)
- IGGT4D (arXiv 2607.19228, 지도 노드) (카메라·기하·물체 정체성을 프레임 단위로 스트리밍 갱신. 비에고, 손 prior 없음)
- InfiniHand (arXiv 2609.35743, 대기열, 프리프린트) (LingBot-Map 기하 메모리로 손·MANO·카메라를 스트리밍 피드포워드 추정, 11.19 FPS. 장면·물체 출력 없음)
- UniHOI / EgoMono4D (arXiv 2411.09145) (에고 손-물체 영상의 카메라 내부 파라미터·포즈·깊이를 피드포워드로 추정, 최적화 대비 약 30배 빠름. 손·물체 분리 없음)
- Hand-4DGS (arXiv 2606.19156, 지도 노드 Hand4DGS) (에고 동적 손 4D를 피드포워드로 약 60 FPS 복원. 손만)
- ReViV (arXiv 2607.17790, 지도 노드, ECCV 2026) (몸·손·깊이·카메라·시선을 한 번에 출력. 물체 없음, 온라인 여부 미기록)

**채우려면** — LingBot-Map·STream3R 같은 인과 스트리밍 백본(또는 Hand3R)에 MANO 손 헤드와 인스턴스 물체 헤드를 붙여, 프레임마다 정적 배경 포인트맵·양손 메시·물체 포즈를 함께 갱신하는 온라인 모델을 만듭니다. HOT3D·ADT 긴 시퀀스에서 배경 깊이 AbsRel, 손 W-MPJPE, 물체 6DoF 오차(ADD), 시간에 따른 ATE 증가율을 보고하고, 같은 백본에서 학습 없는 동적 분리(Stream4D·IGGT4D 방식)와 MANO 헤드를 맞비교합니다. 평가 규칙은 입력 인과성 또는 허용 지연 k프레임을 명시하게 하고, 연산 등급(서버 GPU / Jetson Orin급 / 모바일 NPU)마다 p50·p99 지연, 1시간 스트림 최대 메모리, 프레임당 에너지(J)를 정확도와 함께 보고하게 합니다. 이 규칙으로 Hand3R·InfiniHand·V-JEPA Hand·Hand-4DGS·RegVGGT·LingBot-Map을 다시 측정한 첫 표를 냅니다.

#### G9. 물체 마스크 없이 관절·변형 물체까지 다루는 에고 손-물체 4D 통합 모델과 기하 GT 벤치마크

*부분적으로 채워짐 · 우선 높음 · 축 1∩2·1·2·3*

단안 에고 RGB에서 양손 MANO와 함께 관절 물체의 부품 포즈·관절 각, 변형 물체의 표면 기하를 물체 마스크 없이 피드포워드로 내는 통합 모델이 없습니다. ArtiPoint(2509.01708)는 RGB-D 영상에서, PAWS(2603.25539)는 에고 영상에서 손 상호작용을 단서로 관절을 추정하지만 손 메시·물체 기하·관절 각 추적을 함께 내는지는 확인되지 않았고, EgoPhys(2606.16202)는 변형 물체 물리 디지털 트윈을 만들지만 손 공동 복원과 3D·4D 표면 GT 여부가 확인되지 않았습니다. 관절 각과 변형 표면의 4D 점 대응 GT를 손 GT와 함께 갖추고 Chamfer 거리·scene flow EPE·관절 각 오차 같은 기하 지표로 채점하는 에고 벤치마크도 없어, DPDeGauss처럼 렌더링 지표(PSNR)로 평가된 동적 장면 방법의 기하 오류가 가려집니다. 그 결과 λ0 실제 과제(커튼·서랍·냉장고·노트북)처럼 로봇 쪽은 관절·변형 물체를 다루는데 지각 쪽 평가는 강체 6DoF(EgoXperience, ComPose)에 머무는 어긋남이 남아 있습니다.

부분적으로 채운 연구:

- ArtiPoint / Arti4D (arXiv 2509.01708, CoRL 2025, https://github.com/robot-learning-freiburg/ArtiPoint) (손 추적으로 상호작용 구간을 찾아 실환경 RGB-D에서 관절 추정. Arti4D는 4개 장면 분할에 축 유형·상호작용 구간·GT 카메라 오도메트리·TSDF 메시 제공, 관절 각 GT는 README에서 확인 못 함)
- PAWS (arXiv 2603.25539) (에고 영상의 손-관절 가구 상호작용에서 관절을 대규모 지각, HD-EPIC·Epic-Fields 평가, ArtiPoint 대비 정확도 향상 보고)
- EgoPhys (arXiv 2606.16202) (RGB 에고 영상에서 변형 물체 물리 디지털 트윈과 변형 물체 조작 데이터 구축. 표면 GT·손 복원 여부 미확인)
- UniHOI (arXiv 2411.09145) (라벨 없는 HOI 영상으로 학습해 마스크 없이 장면 전체 깊이·카메라를 조밀 추정. 물체 단위 분리·관절·변형 없음)
- EgoFound3R (arXiv 2610.01210, 대기열, 프리프린트) (물체 메시 없이 손 점 단위 가시성·접촉·접촉면 거리만 출력)

**채우려면** — 모델: 단안 에고 RGB에서 카메라·깊이·양손 MANO에 더해 강체 물체 6DoF, 관절 물체의 부품 포즈·관절 각, 변형 물체의 표면 점 궤적을 내는 피드포워드 모델(가중치 공개)입니다. 물체는 첫 프레임 마스크 대신 손 접촉 단서(EgoFound3R식)나 open-vocabulary 검출로 모델이 직접 찾게 하고 '마스크 제공/미제공'을 함께 보고합니다. 벤치마크: Ego-1K식 다시점 리그로 서랍·문·노트북(관절)과 천·봉지·케이블(변형) 조작 장면을 찍어 관절 각 GT, 물체 표면 4D 점 대응 GT, 손 GT를 만듭니다. 지표는 표면 Chamfer 거리, scene flow EPE, 관절 각 오차, 물체 ADD, 손-물체 관통·접촉 일관성이고 렌더링 지표와의 상관도 봅니다. Arti4D·HD-EPIC 관절 클립(PAWS 평가 세트)과 EgoPhys 데이터를 보조 평가로 쓰고, DPDeGauss·EgoXperience·ReViV·ArtiPoint·PAWS·Stream4D를 같은 시퀀스에서 비교합니다.

#### G10. 머리 리그 구성(대수·배치·화각)을 통제 비교하고 실외·장시간·다인 메트릭 손·몸 GT를 갖춘 교차 기기 캡처 벤치마크

*부분적으로 채워짐 · 우선 중간 · 축 3·2·B*

같은 피험자·같은 과제를 카메라 대수·배치·화각이 다른 '머리' 리그로 찍고, 손가락 단위 손·몸·SLAM 정확도와 무게·전력을 통제 비교한 실측 벤치마크가 없습니다. EgoSim(2502.18373)은 카메라 위치·내부 파라미터를 바꿔 렌더링하는 시뮬레이터와 GoPro 6대·Xsens 몸 GT의 MultiEgoView를 냈지만 몸 여러 곳에 단 카메라·하체 포즈 중심이고, HOT3D는 Aria와 Quest 3 두 기기로 다시점이 단일 시점보다 낫다는 결과를 냈지만 실내 통제 환경입니다. 대기열의 헤드 리그(RoboCap 6대, MEgoVista 어안 3대+IMU, EgoRayFormer 스테레오 어안, EgoWholeView 6대)는 각자 한 가지 구성만 평가하고, MEgoVista의 다인 장면 착용자/타인 손 구분은 정성 평가뿐입니다. 실외와 여러 방을 오가는 10분 이상 시퀀스에서 단안 월드 좌표 손의 분당 드리프트를 잰 결과도 찾지 못했습니다.

부분적으로 채운 연구:

- EgoSim: An Egocentric Multi-view Simulator and Real Dataset for Body-worn Cameras… (arXiv 2502.18373, 게재처 미확인, 지도 EgoSim 2604.01001과 다른 논문) (카메라 배치·내부 파라미터를 바꾸는 렌더링 시뮬레이터 + 실측 MultiEgoView 13명·5시간·GoPro 6대·Xsens 몸 GT. 머리 리그 아님, 손가락 GT 없음)
- HOT3D (arXiv 2411.19167, 지도 노드 HOT3D) (Aria·Quest 3 두 헤드셋 녹화, 다시점이 단일 시점보다 크게 낫다는 실내 비교)
- RoboCap (arXiv 2610.07217, 대기열, 기술 보고서) (OptiTrack 마커 GT가 붙은 야외 손 데이터셋을 UmeTrack·MANO 형식으로 공개, UnrealEgo2·DexYCB·OakInk·HO3D 공개 벤치에서도 평가)
- MEgoVista (arXiv 2609.16684, 대기열, 프리프린트) (어안 3대+IMU 헤드셋과 26대 광학 모캡 기준 손 PA-MPJPE 4.29 mm, 다인 장면 착용자/타인 손 구분은 정성)
- EgoRayFormer (arXiv 2610.26641, 대기열, 프리프린트, 공식 GitHub README 기준) (머리 장착 스테레오 어안 몸 포즈를 공개 UnrealEgo2·UnrealEgo-RW에서 평가: MPJPE 17.64 mm·49.55 mm, UnrealEgo2 사전학습 후 RW 47.57 mm. 리그 구성 변화 없음)
- OmniEgoCap (arXiv 2512.19283, 지도 노드, NeurIPS 2026 프로젝트 페이지 표기) (OmniEgoDB에 여러 소비자 에고 기기와 GT 동작. 몸 중심)

**채우려면** — 2단계 설계를 제안합니다. 1단계: EgoSim(2502.18373)식 시뮬레이터에 머리 장착 위치를 추가해 카메라 1·2·3·6대, 전방·측방·하향 배치, 화각 조합별 손·몸·SLAM 정확도를 먼저 비교해 후보 리그를 좁힙니다. 2단계: 남은 소수 리그(Aria Gen2, 6카메라 헤드 리그, 스테레오 어안 헤드셋, 단안 GoPro)를 같은 피험자에게 동시 또는 반복 착용시키고, 광학 모캡(실외는 일부 구간 모캡으로 교정한 휴대형 GT)으로 실외와 여러 방을 오가는 10분 이상 시퀀스와 2인 이상 상호작용(물건 건네주기)을 찍습니다. (1) 리그 트랙: 구성별 SLAM ATE, 손 PA-MPJPE·W-MPJPE, 몸 MPJPE, 깊이 오차와 무게·전력 대비 정확도 곡선. (2) 단안 트랙: 전방 카메라만으로 InfiniHand·MINT·DewHand·V-JEPA Hand의 분당 W-MPJPE 드리프트, 화면 밖 지속 시간(0–1 s, 1–5 s, 5 s 이상)별 오차, 손 소유자(착용자/타인) 분류 정확도. HOT3D 두 기기 결과를 실내 기준점으로 두고 상업 이용 가능한 라이선스로 공개합니다.

#### G11. 시선 체류·재방문으로 '무엇을 기억할지' 정하는 예산 제한 3D 물체 단위 메모리 (축 9 × 축 7)

*부분적으로 채워짐 · 우선 중간 · 축 9·7*

고정된 메모리 예산(물체 슬롯 수·바이트) 아래 3D 시선 고정점의 체류 시간과 재방문 횟수로 물체 단위 3D 메모리의 쓰기·유지 우선순위를 정하고, 그 효과를 몇 분~수십 분 뒤의 3D 위치 오차와 예산 대비 재현율로 잰 연구가 없습니다. Gaze Archive(2511.16214)는 스마트 글래스 시선으로 기억할 장면을 골라 압축 저장·자연어 회상을 하고 EPIC(2606.15859)은 시선·자세·관성 신호로 영상을 걸러 메모리를 평균 27.5배 줄였지만, 둘 다 장면·프레임 단위 기록이며 물체 3D 위치 질의를 채점한다는 근거는 보지 못했습니다. 반대로 NeverLookBack(VQ3D 중앙값 0.99 m)·Whareformer 같은 3D 물체 메모리는 시선 입력이 없고, G3Ego는 시선으로 2D 장면 그래프를 거르는 행동 인식용입니다. 그래서 시선 기반 쓰기 정책이 균등 샘플링·검출 신뢰도·손 접촉 정책보다 3D 위치 회상에서 나은지는 비교된 적이 없습니다.

부분적으로 채운 연구:

- Gaze Archive (arXiv 2511.16214, 게재처 미확인) (스마트 글래스 시선 추적으로 의도에 맞는 장면을 기록하고 압축된 의도 정렬 메모리 인코딩과 자연어 회상 수행. 3D 위치·예산 대비 재현율 미확인)
- EPIC (arXiv 2606.15859, 게재처 미확인) (AR 글래스에서 시선·자세·관성 신호로 영상을 걸러 메모리 평균 27.5배·에너지 24.3배 절감, 정확도 대체로 유지. 물체 단위 메모리 여부 미확인)
- Towards an Embodied Semantic Fovea (arXiv 1807.10561) (시선점마다 3D 물체 표현을 묶어 재방문 시 같은 물체로 등록하는 2018년 원형)
- NeverLookBack (arXiv 2610.10538, 지도 노드) (오프라인 3D 물체 메모리 기준선, VQ3D 중앙값 0.99 m, 시선 입력 없음)
- G3Ego (arXiv 2608.20157, 지도 노드) (시선이 가리키지 않는 엔티티를 장면 그래프에서 제거. EGTEA Gaze+·MECCANO 2D 행동 인식용)
- ReViV (arXiv 2607.17790, 지도 노드) · EgoSpanLift (arXiv 2511.18470, 지도 노드) (단일 RGB 시선 복원 / SLAM 키포인트 3D 시선 리프팅으로 3D 시선 신호 공급)

**채우려면** — (1) 데이터: 3D 시선 GT가 있는 Aria 계열(EgoExo4D·ADT·AEA) 장시간 시퀀스에 '몇 분~수십 분 뒤 X는 어디 있나' 질의와 3D 위치 GT를 붙입니다(검색 요약에서 이름만 본 SuperMemory-VQA가 시선·SLAM 궤적을 함께 공개하는지 먼저 확인). (2) 실험: 물체 슬롯 수나 바이트로 예산을 고정하고 쓰기·유지 정책을 균등 샘플링, 검출 신뢰도, 손 접촉 이벤트, 3D 시선 체류 시간·재방문 횟수, 이들의 조합, 프레임 단위 시선 필터(EPIC·Gaze Archive식)로 바꿔 VQ3D식 3D 위치 오차, 예산 대비 재현율, 지연을 비교합니다. 기준선은 NeverLookBack(0.99 m)입니다. (3) 시선 센서가 없는 기기를 위해 ReViV 복원 시선이나 깊이로 3D로 올린 ARGaze 예측을 측정 시선 대신 넣었을 때 이득이 얼마나 남는지 잽니다(Scanpath3D는 과거 3D 시선을 입력으로 받아 대체 신호가 아님).

#### G12. 손이 옮긴 물체가 재방문 때도 그 자리에 있는가: 실제 에고 손 조작 사건 기반 재방문 일관성 평가와 접촉 이벤트 메모리 월드 모델 (축 6 × 축 7)

*부분적으로 채워짐 · 우선 중간 · 축 6·7*

실제 에고 영상에서 손이 물체를 P에서 Q로 옮긴 뒤 시야를 벗어났다 돌아오는 구간을 잘라, 실제 카메라·손 궤적을 조건으로 생성한 재방문 프레임에서 물체가 Q에 있는지, 3D 위치 오차, 옮기지 않은 물체가 바뀌는 오탐률을 재는 벤치마크가 없습니다. MemoBench(V-D-R, 재등장 점수 모두 0.6 미만)·WorldMemBench(다중 재방문)·MBench(Exit-and-Reenter)·R2M-Bench(MemoryGain) 같은 범용 월드 모델 메모리 벤치는 2026년에 이미 나왔지만, 에고 영상이나 손 조작 사건을 쓰는지 확인되지 않았고 3D 위치 오차는 쓰지 않는 것으로 보입니다. 에고 쪽 EgoSim(3D 장면 상태 지속 갱신)·EgoGenesis(투영 메모리)·MultiAgentEgoWM(메모리 개념 공유)은 손이 옮긴 물체를 물체 단위로 갱신하는지와 재방문 일관성을 정량 평가하는지가 확인되지 않았습니다. 손 잡기·놓기 이벤트로 물체 슬롯을 갱신하는 에고 월드 모델도 찾지 못했습니다.

부분적으로 채운 연구:

- MemoBench (arXiv 2606.27537) (Visible→Disappeared→Reappear 방식으로 물리 과정을 겪은 물체의 재등장 복원 평가, 모든 모델 Object Reappearance Score 0.6 미만. 에고·손 여부 미확인)
- WorldMemBench (arXiv 2610.19063) (통제된 카메라 이탈·다중 재방문, 정적 유지와 동적 상태 변화 성능이 갈리고 첫 재방문 뒤 메모리 저하)
- MBench (arXiv 2606.00793) (Exit-and-Reenter, VLM으로 화면 이탈 확인 후 SAM 2·DINOv2로 재등장 일관성 채점)
- R2M-Bench (arXiv 2608.27328) (간격을 맞춘 비재방문 쌍 대비 상대 지표 MemoryGain)
- EgoSim (arXiv 2604.01001, 지도 노드) (연속 시뮬레이션용 3D 장면 상태 지속 갱신, 실제 손 상호작용 50클립. 물체 단위 갱신·재방문 평가 미확인)
- EgoGenesis (arXiv 2607.28243, 지도 노드) (온라인 앵커 투영 메모리를 쓰는 에고 world-action 모델. 손이 옮긴 물체 갱신 여부 미기록)
- Ego2Act (arXiv 2610.01092, 대기열, 프리프린트) (에고 손 조작 생성의 목표 완수·물리 타당성 평가. 재방문·메모리 평가 없음)

**채우려면** — (1) 벤치마크: HOT3D(물체 6DoF GT)와 HD-EPIC(물체 이동 2만 건, G5 참조)에서 'A를 P→Q로 옮김 → 시야 이탈 → 재방문' 구간을 잘라 실제 카메라·손 궤적을 조건으로 재방문 프레임을 생성하게 합니다. MemoBench의 V-D-R·재등장 점수와 WorldMemBench의 다중 재방문 프로토콜을 옮기고, 범용 벤치에 없는 (i) 물체가 Q에 있는지 (ii) 3D 위치 오차 (iii) 옮기지 않은 물체의 상태 변화 오탐률 (iv) R2M식 간격 보정을 더합니다. 채점기는 MBench식 SAM 2 마스크에 IGGT4D 같은 정체성 유지 3D 추적을 결합합니다. (2) 비교: 메모리 없음, EgoGenesis식 투영 메모리, EgoSim식 3D 장면 상태 갱신, 범용 메모리 월드 모델. (3) 제안 모델: 손 잡기·놓기 이벤트(G5의 검출기 재사용)로만 물체 슬롯을 갱신하는 에고 월드 모델을 위 지표로 검증합니다.

#### G13. 사람→로봇 정교 조작 전이 갈래(리타게팅, 리타게팅 생략, 영상 로봇화 편집)를 같은 사람 데이터·같은 로봇 손·같은 정책에서 맞붙인 비교

*부분적으로 채워짐 · 우선 중간 · 축 5·2·8*

행동 쪽 갈래(최적화·생성형 리타게팅, 카메라 좌표 손 행동, 잠재 행동 사전학습)와 시각 쪽 갈래(인페인팅+로봇 오버레이, 물리 일관 편집, 팔 재렌더링)를 같은 사람 데이터·같은 다섯 손가락 로봇 손·같은 정책 구조에서 맞붙인 비교가 없습니다. Phantom(2503.00779)은 같은 로봇·과제에서 편집 방식 4가지(Hand Inpaint·Hand Mask·Red Line·Vanilla)를, HuRo(2609.10706)는 로봇 오버레이 유무와 '시각만 전이' 대 '리타게팅 행동까지 쓰는 end-to-end'를 비교했지만 모두 시각 편집 갈래 안의 자체 비교입니다. 생성형 리타게팅(2610.12440)은 MPC·운동학적 리타게팅과 시뮬레이션에서만 비교했고, EgoJEPA(2610.20904)는 리타게팅이 체현마다 재보정이 필요하고 손 추적 오차를 전파한다고 지적하며 3개 체현·5개 실과제를 보고하지만 리타게팅 기준선과의 같은 조건 비교는 확인되지 않았습니다. 손 라벨의 3D 노이즈를 통제했을 때 갈래별 민감도가 어떻게 다른지도 측정된 적이 없습니다.

부분적으로 채운 연구:

- Phantom (arXiv 2503.00779, 지도 노드 Phantom, CoRL 2025) (같은 로봇·과제에서 Hand Inpaint·Hand Mask·Red Line·Vanilla 편집 비교: Inpaint·Mask 비슷(Pick/Place 0.92), Red Line·Vanilla 과제 미완수. 프로젝트 페이지 검색 요약 기준, 과제별 수치는 근사)
- HuRo (arXiv 2609.10706, 대기열, CoRL 2026 채택 표기) (사전학습 데이터를 늘리면 완료율 51.5%→80.3%, OOD 34.9%→72.2%. 자체 ablation에서 로봇 오버레이 유무와 시각만 전이 대 리타게팅 행동 포함 end-to-end 비교)
- Generative Neural Retargeting (arXiv 2610.12440, 대기열, 프리프린트) (flow matching 생성형 리타게팅 대 MPC·운동학적 리타게팅, 3.3k 형상·223k 시연, 시뮬레이션 전용)
- EgoJEPA (arXiv 2610.20904, 대기열, 프리프린트) (규칙 기반 리타게팅 없이 손 동작 차이에 조건화된 JEPA식 잠재 행동과 미래 시각 동역학을 학습해 로봇에 적응, 3개 체현·5개 실과제)
- EgoCPT (arXiv 2610.17572, 대기열, 프리프린트) (접촉 인지 최적화 리타게팅, 잡음 있는 EgoDex 재구성·깨끗한 TACO 모캡 입력, 5개 과제)
- HuGe (arXiv 2610.34186, 대기열, 프리프린트) (팔 재렌더링 에고 시연 추가 유무의 자체 어블레이션, G1 pick-and-drop)
- EXE (arXiv 2610.33685, 대기열, 프리프린트) (분해 잠재 행동 사전학습, 검색 요약 기준 EXE_base 60% 대비 80%)

**채우려면** — 같은 사람 데이터(EgoDex·HOT3D 부분집합 등), 같은 다섯 손가락 로봇 손, 같은 정책 구조에서 행동 쪽 (a) 최적화 리타게팅(EgoCPT식) (b) 생성형 리타게팅(2610.12440식) (c) 카메라 좌표 손 행동 직접 예측(IronMind식, 내용 확인 후) (d) 잠재 행동 사전학습 + 소량 로봇 미세조정(EgoJEPA·EXE식) (e) 언어 행동 추론(EgoLAP식)과, 시각 쪽 (f) 원본 (g) Phantom식 인페인팅+오버레이 (h) 물리 일관 편집(HuRo·2610.06137식) (i) HuGe식 팔 재렌더링 (j) 기하 시점 정렬(EgoWild2Dex의 GeoFormer식)을 요인 설계로 비교합니다. 변수는 로봇 시연 수(0·10·50개), 손 라벨에 주입한 3D 노이즈(mm, G1과 같은 설정), 접촉이 많은/적은 과제입니다. 실로봇 성공률과 접촉 위반·관통률을 재고, 편집 영상 품질 지표로 로봇 손-물체 3D 접촉 일치율과 편집 영상에서 재추정한 그리퍼 궤적과 원래 손 궤적의 차이를 보고해 '언제 리타게팅·편집이 필요한가'에 답하는 표를 냅니다.

#### G14. 기하 백본 선택과 근접 손 가림 견고성: 손 헤드를 고정하고 백본만 바꾼 통제 실험과 손 점유율 구간별 스트레스 평가

*부분적으로 채워짐 · 우선 중간 · 축 B·1·2*

손 헤드와 학습 데이터를 고정하고 기하 백본(DROID-SLAM, VGGT, VGGT-Ω, LingBot-Map, Pi3X, V-JEPA 2.1 등)만 바꿔 손 월드 오차(W-MPJPE)가 어떻게 달라지는지 잰 통제 실험이 없습니다. 지금 있는 비교는 반대 방향이거나 평균 지표뿐입니다: HaWoR는 DROID-SLAM 계열 카메라를 두고 손 추정기만 바꾼 비교(W-MPJPE 33.20 대 156.03·154.30)와 깊이 모듈 교체 ablation을 했고, RESELF는 EE4D-JSM 하나에서 VGGT·CUT3R·Pi3X·EM4D를 깊이·카메라 평균 지표로, DewHand는 VGGT-Ω와 카메라 스케일·궤적만 비교했습니다. 범용 E3D-Bench는 피드포워드 백본을 한 표에서 비교하지만 에고·손 가림 장면 포함 여부가 확인되지 않았고, 에고 3D 벤치 EFM3D는 이 백본들을 평가하지 않습니다. 그래서 손 점유율·손까지 깊이·머리 각속도 구간별로 백본이 얼마나 무너지고 그 오차가 손 정확도로 얼마나 번지는지 알 수 없습니다.

부분적으로 채운 연구:

- HaWoR (arXiv 2501.02973, 지도 노드 HaWoR, CVPR 2025) (손 마스킹 SLAM, 메트릭 깊이 모델 교체와 AdaSM 제거 ablation(ATE 15.86 대 22.38), 카메라 쪽 고정·손 추정기 교체 비교 W-MPJPE 33.20 대 156.03·154.30. 리뷰 사이트 요약 기준)
- RESELF (arXiv 2609.01276, 대기열, 프리프린트) (EE4D-JSM에서 VGGT·CUT3R·Pi3X·EM4D와 깊이·카메라 추적 비교, Pi3X 에고 적응 전후(RESELF-s1))
- DewHand (arXiv 2610.29936, 대기열, 프리프린트) (고정 백본 VGGT-Ω와 카메라 스케일·궤적 정확도 비교)
- E3D-Bench (arXiv 2506.01933, 게재 미확인) (DUSt3R·MASt3R·MonST3R·VGGT·CUT3R 범용 비교, 메트릭 스케일 깊이와 극단적 도메인 이동이 여전히 어렵다는 결론)
- ACE-Ego-Hand (arXiv 2608.20308, 지도 노드 ACEEgoHand) (가림 견고 손 복원: ARCTIC MPJPE-p 30%·HOT3D 40% 감소. 백본 비교 아님)

**채우려면** — GT 카메라가 있는 에고 시퀀스(HOT3D, ADT, ARCTIC, EgoDex)에서 프레임마다 손 마스크 점유율(예: 30% 이상/미만), 손까지 깊이, 머리 각속도로 구간을 나누고, DROID-SLAM·VGGT·VGGT-Ω·LingBot-Map·STream3R·Pi3X·V-JEPA 2.1별 구간 카메라 ATE/RPE, 깊이 AbsRel, 메트릭 스케일 오차를 보고합니다(E3D-Bench 지표 정의를 따르되 에고 근접 구간 추가). 손 영역 마스킹 입력(HaWoR식)과 에고 미세조정(RESELF-s1식) 전후도 비교합니다. 이어서 손 헤드(MANO 회귀 + 월드 궤적 디코더)와 학습 데이터를 고정하고 백본만 바꿔 구간별 W-MPJPE를 재면, HaWoR의 '카메라 고정·손 헤드 교체'와 대칭인 '손 헤드 고정·백본 교체' 결과가 생겨 축 B 오차가 축 2로 전파되는 정도가 드러납니다. 인과 스트리밍 백본과 오프라인 백본의 정확도·지연 절충은 G8 규칙으로 함께 잽니다.

#### G16. 3D 시선으로 지시 대상을, 착용자 몸 자세로 머리/몸통 기준틀을 정하는 자기중심 메트릭 질의 벤치마크 ('이거 얼마나 멀어?', '내 왼쪽 뒤의 컵')

*부분적으로 채워짐 · 우선 중간 · 축 4·9·2·7*

3D 시선 고정점으로 '이거·저거'의 지시 대상을 정하고, 착용자 몸 자세로 머리 기준틀과 몸통 기준틀을 분리·통제하며, 시야 밖 대상까지 포함해 거리·방향의 메트릭 정답을 요구하는 에고 질의 벤치마크가 없습니다. EgoGazeVQA(2509.07447, NeurIPS 2025 D&B)는 시선 유도 프롬프트로 에고 의도 QA를 평가하고 시선 추정 오차의 영향까지 분석하지만, 시선이 3D인지와 메트릭 정답 여부는 확인되지 않았습니다. 기준틀 쪽은 COMFORT·ViewSpatial-Bench·Allocentric Perceiver·SCOPE가 일반 이미지에서 모호성을 다루고, 지도의 Ego3D-Bench는 왼쪽·오른쪽을 몸 기준으로 정의하지만 차량형 다시점이라 카메라와 몸이 강체로 묶여 머리-몸통 어긋남이 없습니다. 착용자 상태를 공급할 수 있는 ReViV·RESELF도 축 4 질의응답과 연결된 적이 없습니다.

부분적으로 채운 연구:

- EgoGazeVQA (arXiv 2509.07447, NeurIPS 2025 Datasets and Benchmarks, 검색 기준) (일상 에고 영상에서 시선 유도 프롬프트로 사용자 의도 QA 평가, 시선 추정 정확도가 프롬프트 효과에 주는 영향 분석. 3D·메트릭 정답 미확인)
- COMFORT (arXiv 2410.17385) (VLM의 공간 기준틀 모호성 평가, 자기중심 상대 기준틀에서 반사 변환 선호. 일반 이미지)
- ViewSpatial-Bench (https://www.themoonlight.io/en/review/viewspatial-bench-evaluating-multi-perspective-spatial-localization-in-vision-language-models) (카메라 시점과 이미지 속 사람 시점의 혼동 평가, 3인칭 이미지)
- Allocentric Perceiver (arXiv 2602.05789, ICML 2026 투고 표기) (같은 '~의 왼쪽'이 기준틀에 따라 참·거짓이 갈리는 기준틀 격차와 학습 없는 재고정 방법)
- SCOPE (https://aclanthology.org/2026.acl-long.1514.pdf , ACL 2026) (자기중심·타자중심 시점 사이 공간추론 일관성 평가)
- Ego3D-Bench (arXiv 2509.06266, 지도 노드 Ego3DBench) (왼쪽·오른쪽을 에이전트 몸 기준 고정 방향으로 정의. 카메라-몸 분리 없음)
- EgoAlign (arXiv 2610.16176, 대기열, 2차 출처 요약) (에이전트 중심 좌표 3D-LLM, 수치 포즈에서 공간 맥락을 구성. 입력은 에고 영상이 아닌 3D 장면으로 보임)
- Gaze2HOI (arXiv 2610.27877, 지도 노드) · GazeHandPred (arXiv 2504.01024, 지도 노드) (시선으로 상호작용 대상·잡기 의도를 가려내는 하위 문제)
- ReViV (arXiv 2607.17790, 지도 노드) (단일 에고 RGB에서 시선·몸·손을 함께 복원해 '추정 착용자 상태' 조건 공급 가능)

**채우려면** — ADT·AEA·EgoExo4D의 3D 시선 GT로 지시 대상을 정하고, Nymeria와 EgoExo4D(EE4D-JSM)의 몸 동작 GT로 몸통 방향을 얻습니다. 머리와 몸통 방향이 크게(예: 30° 이상) 어긋난 순간과 대상이 시야 밖에 있는 순간을 골라 '지금 보는 컵까지 몇 m야?', '이거랑 그 옆 상자 중 뭐가 더 커?', '내 몸 기준 왼쪽 뒤에 뭐가 있어?' 질의와 메트릭 정답을 붙입니다. 조건은 시선 쪽(없음 / 2D 시선점 / 3D 고정점 / ReViV 복원 시선 / 깊이로 올린 ARGaze 예측)과 몸 쪽(VLM 단독 / 카메라 포즈만 / ReViV·RESELF 추정 몸 / GT 몸)으로 나눕니다. 지시 대상 정확도, 방향 정확도, 거리 RMSE, MRA를 머리-몸통 각도 차이별·시야 밖 여부별로 보고하고 시선 오차(각도·깊이)가 답 오차로 번지는 정도를 잽니다. EgoGazeVQA의 시선 프롬프트를 기준선으로, COMFORT·ViewSpatial-Bench의 기준틀 평가 방식을 함께 써서 직접 비교합니다.

#### G17. 손·카메라 제어 생성 월드 모델의 에고 영상을 조건 라벨째 3D 손·기하 지각 모델 학습에 쓰고 실제 벤치마크 향상을 검증하는 연구

*부분적으로 채워짐 · 우선 중간 · 축 8·6·2*

손·카메라를 제어하는 생성 월드 모델(DWM, HandsOnWorld, EgoSim, GenReality, SparseHandJoints)로 에고 영상을 만들고, 조건으로 준 MANO 궤적과 카메라 궤적을 라벨로 삼아 시간적으로 일관된 월드 좌표 손 추정기나 기하 백본을 학습해 HOT3D·ARCTIC에서 향상을 검증한 연구가 없습니다. 조건부 생성의 조건을 공짜 3D 라벨로 쓰는 아이디어는 HandBooster(2403.18575, CVPR 2024)가 단일 이미지·3인칭 손 메시 복원(HO3D·DexYCB)에서 이미 보였지만, 보충 자료에서 생성 프레임 사이 손 겉모습 일관성이 보장되지 않아 다중 프레임 복원에 쓰기 어렵다고 밝힙니다. 생성 월드 모델 출력을 데이터로 쓴 Wh0는 VLA(축 5)에 썼고, EgoGen·NVIDIA EgoHand-v1은 생성이 아닌 렌더링 합성, LEGO는 엑소→에고 영상 생성이라 3D 라벨 학습과 무관합니다. 생성 영상의 기하 일관성과 자동 주석 품질 검증이라는 축 8 과제가 풀리지 않아, 재추정 필터 기준도 정해져 있지 않습니다.

부분적으로 채운 연구:

- HandBooster (arXiv 2403.18575, CVPR 2024) 및 후속 HandBooster+ (IEEE TPAMI 2025, 검색 요약 기준) (손-물체 조건 확산 생성 이미지와 공짜 3D 주석으로 여러 손 메시 복원기의 HO3D·DexYCB 성능 향상. 단일 이미지·3인칭)
- Wh0 (arXiv 2606.22136, 지도 노드 Wh0) (생성 월드 모델 에고 손 조작 영상 5만 에피소드를 덱스터러스 VLA 학습에 사용. 지각 모델 아님)
- EgoGen (arXiv 2401.08739, 지도 노드 EgoGen, CVPR 2024 Oral) (시뮬레이터 합성 헤드마운트 데이터로 에고 카메라 추적·몸 메시 복원 개선. 생성 모델·손 아님)
- NVIDIA EgoHand-v1 (https://huggingface.co/nvidia/EgoHand-v1) (합성 렌더와 실제 데이터로 학습해 HOT3D에서 평가한 에고 손 추정기, 검색 스니펫 기준. 생성 모델 아님, 합성 기여 ablation 미확인)
- HandsOnWorld (arXiv 2607.02075, 지도 노드) · SparseHandJoints (arXiv 2603.11755, 지도 노드) (야생 에고 영상에 3D 손 주석을 붙인 생성용 데이터 파이프라인. 지각 모델 학습 검증 없음)
- Generative Neural Retargeting (arXiv 2610.12440, 대기열) (flow matching 생성으로 3.3k 형상·223k 시연의 3D 궤적 라벨 대량 생산. 영상 아님, 로봇용)

**채우려면** — DWM·HandsOnWorld·EgoSim에 MANO 궤적과 카메라 궤적을 조건으로 줘서 에고 클립을 대량 생성하고, 고정 추정기(HaWoR·DewHand 등, G2 키트에서 선택)로 재추정한 손·카메라가 조건과 기준 이하로 일치하는 클립만 남깁니다(G7 행동 충실도 지표 공유). 남은 클립과 조건 라벨을 실제 데이터와 여러 비율로 섞어 월드 좌표 손 추정기를 학습하고 HOT3D·ARCTIC W-MPJPE와 화면 이탈·근접 가림 구간 오차 변화를 보고합니다. 비교 기준으로 (a) 이미지 단위 생성 증강(HandBooster식) (b) 렌더링 합성(EgoHand-v1·EgoGen식) (c) 실제 영상 의사라벨 엔진(MINT EgoPipeline, EgoInfinity)을 같은 양으로 두어 '영상 생성 월드 모델'만의 기여(시간 일관성)를 가르고, 생성 데이터 양에 따른 스케일링 곡선과 '필터 없음 대 재추정 필터'를 함께 냅니다.

#### G15. 에고 손·옮겨진 물체에 대한 메트릭 4D 질의에서 같은 기반 VLM의 도구 호출형 대 내재화형 비교

*부분적으로 채워짐 · 우선 낮음 · 축 4·1·1∩2·B*

에고 영상에서 '방금 냄비를 몇 cm 옮겼나', '오른손이 손잡이에 닿을 거리인가' 같은 손·이동 물체 메트릭 질의를 대상으로, 같은 기반 VLM의 도구 호출형(4D 재구성 출력 호출)과 내재화형(같은 출력으로 만든 QA 미세조정·기하 인코더 주입)을 맞붙이고 분포 이동 일반화와 질의당 비용까지 비교한 연구가 없습니다. 두 절반은 지도 밖에서 따로 채워졌습니다: EgoDynamic4D(2508.07251)는 4D 박스·인스턴스 마스크를 갖춘 에고 동적 QA(동적 과제 12종, v3 927K 쌍)로 손·이동 물체 질의를 다루고, SpaceTools(2512.04069, CVPR 2026)는 같은 Qwen2.5-VL-3B·같은 VQA 수로 도구 학습이 도구 없는 미세조정보다 낫다고 보고합니다. 그러나 EgoDynamic4D가 메트릭 거리 문항을 MRA·RMSE로 채점하는지와 실제 데이터인지는 확인되지 않았고, SpaceTools·SpatialCLI·Seeing Is Not Measuring 같은 도구 비교는 로봇·정적 공간추론 위주입니다. 지도 안에서는 1×4·1∩2×4 교차의 노드·엣지가 0개이고 축 4 안에 compares 엣지가 없습니다.

부분적으로 채운 연구:

- EgoDynamic4D (arXiv 2508.07251, 게재 미확인) (에고 동적 4D 장면 QA: RGB-D·카메라 포즈·인스턴스 마스크·4D 박스, 사람-물체 상호작용·궤적 예측 포함 동적 과제 12종, 손 3D 좌표·물체 이동을 근거로 한 문항, v3 927K QA. 메트릭 거리 채점·실제/합성 여부 미확인)
- SpaceTools (arXiv 2512.04069, CVPR 2026) (같은 Qwen2.5-VL-3B·같은 VQA 수에서 도구 사용 학습 대 도구 없는 미세조정 비교, 2차 노트 기준 RoboSpatial +12~16%. 로봇·정적)
- SpatialCLI (arXiv 2607.27703) (도구로 추론을 배운 뒤 도구 없이 추론하는 전환을 다룸. 비교 결과 미확인)
- Seeing Is Not Measuring (arXiv 2609.29073) (가중치 고정 VLM + 도구 체인 메트릭 공간추론, 눈으로 답할 수 있어 보이는 질문에서 도구를 부르지 않는 약점 분석)
- VLM4D (arXiv 2508.02095) (물체 이동·회전·시점 이동·시간 일관성 질의, 영상의 37.5%가 Ego4D. 메트릭 4D GT 채점 미확인)
- EgoReasoner (arXiv 2603.06561) (물체 이동 경로 추적·정지 물체 위치 찾기 등 에고 4D 추론 방법. 지표·도구 비교 미확인)
- Spatial-MLLM (arXiv 2505.23747, 지도 노드 SpatialMLLM) (VGGT 인코더를 넣는 내재화형. 도구 호출형 비교 없음)
- NeverLookBack (arXiv 2610.10538, 지도 노드) (FastVGGT 기하 모듈 기반 메모리로 HD-EPIC 29.7%→42.6%. 같은 기반의 내재화형 비교 없음)

**채우려면** — (1) 벤치마크 확장: EgoDynamic4D의 동적 문항 형식을 HOT3D·ARCTIC처럼 손·물체 3D GT가 있는 실제 에고 시퀀스로 옮겨, 물체 이동 거리(cm), 시점 t의 손-물체 거리, 현재 손 위치에서의 도달 가능성, 'X를 마지막으로 만진 손' 문항을 템플릿으로 만들고 사람이 검수해 MRA와 거리 RMSE로 채점합니다. (2) 비교: 기반 VLM 하나를 고정하고 (a) 도구 호출형(VGGT·깊이·검출기 또는 EgoXperience·ReViV 4D 출력을 질의 때 호출, SpaceTools식 RL 포함) (b) 내재화형(같은 도구 출력으로 만든 QA 미세조정, Spatial-MLLM식 기하 인코더) (c) SpatialCLI식 도구→무도구 전환 (d) World2VLM식 증류를 비교합니다. (3) 이 벤치마크와 EgoDynamic4D, Ego3D-Bench, R3D, EgoProx에서 평가하고 실외 에고·다른 착용 기기·시야 밖 물체 같은 분포 이동 일반화와 질의당 지연·토큰 비용을 함께 보고합니다. 결과가 축 4 노드 사이의 첫 compares 엣지가 됩니다.

#### G18. Aria 밖으로 3D 시선 넓히기: 4D 재구성으로 2D 시선·시선 광선을 손·든 물체 위 3D 고정점으로 올리고, 비Aria 평가 세트와 공통 3D 지표 만들기

*부분적으로 채워짐 · 우선 낮음 · 축 9·1·3*

장면 기하 위의 3D 시선 고정점 GT는 여전히 Aria 계열(ADT·AEA·EgoExo4D)에만 있고, 지도의 3D 시선 연구(Scanpath3D, EgoSpanLift, ARGaze, EgoCampus, ReViV)도 모두 Aria 데이터로 평가됩니다. Aria 밖 EgoTraj(2605.19004, Quest Pro 실외 보행 75명·약 10.7시간)는 프레임별 3D 시선 원점·방향을 주지만 고정점이 아닌 광선이고 깊이·포인트 클라우드가 없으며, EyeNavGS는 VR, Semantic Fovea(1807.10561)는 2018년 정적 장면 연구입니다. EgoSpanLift는 정적 SLAM 키포인트로 시선을 올려 움직이는 손·든 물체 위 고정점을 표현하지 못하고, 2D 시선점을 동적 표면 위 3D 고정점으로 올리거나 Ego4D 2D 시선을 3D 의사라벨로 바꾼 연구는 찾지 못했습니다. 3D 시야 IoU(EgoSpanLift)와 고정점 거리 오차(Scanpath3D)를 함께 계산하는 공통 평가 스크립트도 없습니다.

부분적으로 채운 연구:

- EgoTraj (arXiv 2605.19004, README 기준 ECCV 2026, https://github.com/yehiahmad/EgoTraj) (Meta Quest Pro 실외 도시 보행, 75명·약 10.7시간·약 115만 프레임, 프레임별 3D 시선 원점·방향과 30 Hz 6DoF 머리 포즈. 고정점·깊이 없음)
- ReViV (arXiv 2607.17790, 지도 노드, ECCV 2026) (단안 에고 4D 복원과 시선을 함께 출력. Aria 계열 평가, 동적 표면 고정점 여부 미확인)
- EgoSpanLift (arXiv 2511.18470, 지도 노드) (SLAM 키포인트로 시선을 3D로 올리는 리프팅 선례. 정적 배경, AEA·EgoExo4D)
- EgoMono4D (arXiv 2411.09145, ICCV 2025, 검색 기준) (라벨 없는 에고 영상의 카메라 내부 파라미터·포즈·비디오 깊이 자기지도 추정. 리프팅 기반 후보, 시선 평가 없음)
- EyeNavGS (https://symmru.github.io/EyeNavGS/) (Quest Pro로 3DGS 장면 12곳을 VR 탐색한 46명의 머리 포즈·시선. 실제 1인칭 영상 아님)
- Towards an Embodied Semantic Fovea (arXiv 1807.10561) (에고 RGB-D 매핑 + 머리 장착 안구 추적기로 3D 시선점 추정. 정적 장면)

**채우려면** — (1) 파이프라인: 2D 시선점(또는 EgoTraj식 시선 광선)을 정적·동적 분리 4D 재구성(EgoMono4D, DynStream, IGGT4D, Stream4D)과 결합해 정적 배경과 움직이는 손·든 물체 위의 3D 고정점을 얻습니다. (2) 검증: EgoExo4D·ADT에서 Aria MPS 3D 시선과 비교해 고정점 거리 오차를 정적 대상과 동적 대상으로 나눠 보고하고, SLAM 키포인트 리프팅(EgoSpanLift식)과 대조합니다. (3) 효과: Ego4D·EGTEA Gaze+로 의사 3D 시선 데이터를 만들어 Scanpath3D·EgoSpanLift류 모델을 추가 학습했을 때 ADT·FoVS 지표가 오르는지 잽니다. (4) 비Aria 평가: EgoTraj에 4D 재구성을 붙여 실외 고정점 세트를 만들고, 실내 조작 장면은 Aria가 아닌 안구 추적 안경과 독립 SLAM으로 새로 찍어 Aria로 학습한 모델을 제로샷 평가합니다. 고정점 시퀀스를 시야 격자로 바꿔 IoU와 거리 오차를 함께 계산하는 공통 스크립트를 공개하고, 같은 데이터로 2D 지표(F1)와 3D 지표의 불일치를 분석합니다.

## 4. 방법과 한계

- **실행** — 워크플로 3회, 에이전트 135개. (1) 논문별 메타·출간 검사 + 독립 2차 출간 검사 + 불일치 시 재판정. (2) 클러스터 5개별 간선 제안 → 반박 검토. (3) 빈칸 4관점 제안 → 병합 → 웹 반례 검색 → 최종 정리.
- **1차 실행 실패** — 웹 검색 한도(턴당 200회, 에이전트 공용)가 일찍 소진되어 36편이 검증되지 않은 채 "확인 불가"로 나왔습니다. 에이전트별 검색 상한을 두고 2·3차로 다시 돌렸습니다.
- **존재 확인** — 2·3차에서도 13편은 검색에 다시 잡히지 않았습니다. 그래서 이 세션의 이전 스캔 기록을 대조해, 48편 모두 실제 검색 결과에 제목과 함께 arxiv.org(abs·html·pdf) 링크로 나왔던 것을 확인했습니다. ID를 지어낸 항목은 없습니다.
- **간선 근거** — 간선은 검색 없이 검증된 요약(백본·데이터·비교 필드)만으로 판정했고, 요약에 이름이 직접 나오지 않으면 `추정`으로 낮췄습니다. 내용 미확인 13편의 간선은 모두 추정입니다.
- **빈칸 확인** — 빈칸 반례 검색은 빈칸마다 2~4회로 제한했습니다. "열려 있음"은 '못 찾음'이지 '없음'의 증명이 아닙니다.
- **지도 쪽에서 덤으로 발견한 것** — 지도 노드 53개의 venue 칸이 비어 있습니다. 또 비평 과정에서 두 가지 확인 요청이 나왔습니다. 하나는 DWM(2512.17907)과 같은 제목의 CVPR 2026 포스터 페이지가 검색됐다는 점이고, 다른 하나는 arXiv 2411.09145가 UniHOI와 EgoMono4D 두 제목으로 기록된 점입니다.
