# 연결(엣지) 목록

> `scripts/build.py`가 `data/edges.csv`에서 자동 생성합니다. 직접 수정하지 마세요.

`A → B`: B가 A를 백본·데이터·비교 대상 등으로 사용함.

## 백본으로 사용 (`backbone`, 15)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| MANO → Hand4DGS | 원문 |  |
| HaMeR → HaWoR | 원문 |  |
| DROIDSLAM → HaWoR | 원문 |  |
| MANO → HaWoR | 원문 |  |
| VGGT → EgoXperience | 확인 | VGGT의 피드포워드 재구성 패러다임 확장 |
| MANO → EgoXperience | 확인 | MANO 관절 회전 표현 |
| VGGT → SpatialMLLM | 원문 |  |
| FastVGGT → NeverLookBack | 원문 | 포즈 추정기 |
| NVILA → EgoVLA | 원문 |  |
| MANO → EgoVLA | 원문 |  |
| HaWoR → EgoRecovery | 원문 | 손 재구성 |
| VGGT → VGGTDP | 확인 | VGGT를 시각 인코더로 채택 |
| HaMeR → UniHand | 확인 | 2D 손 관절 라벨링 |
| MANO → GazeHandPred | 추정 |  |
| MANO → Gaze2HOI | 확인 | MANO 별도 라이선스 필요 |

## 직접 확장 (`extends`, 9)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| VGGT → FastVGGT | 원문 |  |
| VGGT → RegVGGT | 원문 |  |
| VITRA → MINT | 원문 |  |
| OSNOM → Whareformer | 원문 | OSNOM 과제의 첫 학습 기반 해법 |
| EgoXGen → EgoExoWM | 원문 |  |
| MMTwin → UniHand | 확인 | 같은 저자 그룹 |
| MADiff → MMTwin | 추정 | 같은 저자 그룹 계보 |
| HOISynth → HOISynthExt | 확인 | 같은 파이프라인·벤치마크의 확장 |
| Phantom → Masquerade | 확인 | Phantom의 데이터 편집 파이프라인을 야생 영상으로 확장 |

## 학습 데이터 (`trains_on`, 12)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| Ego4D → MINT | 원문 |  |
| EgoDex → MINT | 원문 |  |
| HOT3D → EgoXperience | 확인 | 평가는 확인, 학습 사용은 원문 기준 |
| HOT3D → EgoVLA | 원문 |  |
| EgoDex → ACEEgo0 | 원문 |  |
| EgoDex → QwenVLA | 원문 |  |
| Xp10M → QwenVLA | 원문 |  |
| Xp10M → RopediaW0 | 원문 |  |
| EgoDex → RopediaW0 | 원문 |  |
| EgoDex → DexWM | 확인 |  |
| DROIDdata → DexWM | 확인 |  |
| EgoExo4D → EgoMAN | 확인 |  |

## 평가 데이터 (`evaluates_on`, 21)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| EgoExo4D → EgoPOV3DGS | 원문 |  |
| HOT3D → StableHand | 원문 |  |
| HOT3D → MINT | 원문 |  |
| HOT3D → EgoHand | 확인 | 제로샷 평가 |
| HDEPIC → Whareformer | 원문 |  |
| HDEPIC → NeverLookBack | 확인 |  |
| UCSBench → NeverLookBack | 확인 | DirectMe 메모리도 비교 대상 |
| Ego4D → NeverLookBack | 확인 | VQ3D |
| HOT3D → EgoMAN | 확인 | 분포 밖 평가 |
| HOT3D → DPDeGauss | 확인 |  |
| EPICFields → DPDeGauss | 확인 |  |
| HOT3D → ACEEgoHand | 확인 |  |
| Ego4D → GLC | 확인 |  |
| Ego4D → CSTS | 확인 |  |
| ADT → Scanpath3D | 확인 | 184 시퀀스 |
| AEA → EgoSpanLift | 확인 | FoVS-Aria 구성 |
| EgoExo4D → EgoSpanLift | 확인 | FoVS-EgoExo 구성 |
| EgoExo4D → ARGaze | 확인 |  |
| HOT3D → ReViV | 확인 |  |
| ADT → ReViV | 확인 |  |
| EgoExo4D → OmniEgoCap | 확인 |  |

## 비교 기준선 (`compares`, 25)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| STream3R → DynStream | 원문 |  |
| MonST3R → STream3R | 원문 |  |
| EgoGaussian → IA4DGS | 확인 |  |
| HaWoR → StableHand | 원문 |  |
| DynHaMR → StableHand | 원문 |  |
| EgoDex → EgoHand | 확인 | 블라인드 선호 평가 77.0% |
| Xp10M → EgoHand | 확인 | 블라인드 선호 평가 95.5% |
| AMEGO → Whareformer | 원문 |  |
| HaWoR → EgoXperience | 원문 |  |
| DynHaMR → EgoXperience | 원문 |  |
| MINT → EgoXperience | 원문 |  |
| AMEGO → NeverLookBack | 확인 |  |
| OSNOM → NeverLookBack | 확인 |  |
| EmbVideoAgent → NeverLookBack | 확인 |  |
| EgoScale → ACEEgo0 | 원문 |  |
| EgoControl → SparseHandJoints | 원문 |  |
| GenReality → HandsOnWorld | 원문 |  |
| EgoGenesis → P3WAM | 원문 |  |
| MMTwin → EgoMAN | 확인 |  |
| HaWoR → MINT | 추정 |  |
| STream3R → IGGT4D | 추정 | 스트리밍 재구성 기준선과 비교했다고 보고, STream3R 포함 여부는 미확인 |
| HOISynth → EgoInteract | 추정 | EgoInteract가 정지 이미지 한계로 언급한 기존 합성 HOI 파이프라인으로 추정 |
| EgoXGen → Exo2EgoHOI | 추정 | 엑소→에고 생성 선행 연구 |
| GLC → CSTS | 확인 | GLC를 기준선으로 비교 |
| GLC → ARGaze | 추정 |  |

## 개념 연결 (`cross`, 38)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| HOT3D → Whareformer | 원문 |  |
| Xp10M → EgoXperience | 원문 | 같은 Ropedia 데이터 생태계, 부록 인용 |
| EgoXperience → RopediaW0 | 원문 | 같은 조직·같은 날 공개, 직접 의존 미확인 |
| Whareformer → NeverLookBack | 원문 | 인용, 같은 문제 계보 |
| AMEGO → MEMORA | 원문 |  |
| MEMORA → AtlasVLA | 원문 | 지속형 상태를 VLA로 |
| EgoMimic → EgoScale | 원문 |  |
| EgoVLA → EgoRecovery | 원문 |  |
| PEVA → GenReality | 원문 |  |
| SparseHandJoints → EgoGenesis | 확인 | EgoGenesis 참고문헌 인용 |
| HandsOnWorld → EgoGenesis | 원문 |  |
| EgoGenesis → MultiAgentEgoWM | 원문 | 메모리 개념 공유 |
| HaWoR → P3WAM | 원문 | Perceive 모드 = 축 2 과제 |
| DexWM → P3WAM | 원문 |  |
| DWM → DexWM | 추정 | 동시기 dexterous 월드 모델 |
| EgoMAN → EgoHandICL | 추정 |  |
| Ego1K → Hand4DGS | 추정 | 다시점 손–물체 GT 후보 |
| World2VLM → R3D | 추정 | 같은 축의 대안 접근 |
| IGGT4D → NeverLookBack | 추정 | 정체성을 유지하는 스트리밍 4D가 물체 메모리의 백본이 될 수 있음 |
| EgoInteract → EgoInfinity | 추정 | 둘 다 손–물체 상호작용 학습 데이터를 대량으로 만드는 엔진(합성 시뮬레이션 대 웹 영상) |
| IndSynthHOI → HOISynth | 추정 | 같은 계열의 합성 에고 HOI 데이터 생성 |
| EgoGen → EgoInteract | 추정 | 합성 에고 데이터 생성기 계보 |
| Masquerade → EgoMatrix | 추정 | 사람 영상 → 로봇 시연 변환 |
| DexWM → Wh0 | 추정 | 생성 월드 모델을 데이터원으로 활용하는 반대 방향 |
| Xp10M → Wh0 | 추정 | 실제 대규모 에고 데이터 대 생성 데이터 |
| CSTS → Scanpath3D | 추정 | 2D 시선 예측 → 3D 고정점 예측으로 확장 (공저자 Ryan) |
| EgoSpanLift → Scanpath3D | 추정 | 3D 시야 범위 vs 3D 고정점 시퀀스 (공저자 Murdock) |
| GLC → G3Ego | 추정 | 시선을 보조 입력이 아닌 그래프 구성 기준으로 사용 |
| GazeHandPred → Gaze2HOI | 추정 | 시선 기반 손 동작·의도 예측 계보 |
| LookFocusAct → TAVIS | 추정 | 시선 예측형 능동 시각 모방학습 |
| EgoMI → TAVIS | 추정 | 머리/시선 능동 시각 |
| Scanpath3D → Gaze2HOI | 추정 | 미래 3D 시선 → 상호작용 의도 단서 |
| EgoGen → ReViV | 추정 | 같은 그룹(ETH VLG)·공저자 Lyu·Li |
| EgoXperience → ReViV | 추정 | 카메라·손·장면 공동 피드포워드 복원이라는 같은 목표 |
| EgoSpanLift → ReViV | 추정 | ReViV가 시선까지 함께 복원 (축 9 연결) |
| Nymeria → OmniEgoCap | 추정 | 에고 전신 동작 데이터 계보 |
| EgoBody3M → OmniEgoCap | 추정 | 에고 기기 기반 전신 추적 |
| OmniEgoCap → ReViV | 추정 | 착용자(viewer) 몸 복원이라는 공통 과제 |

## 인용 (`cites`, 5)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| EgoHOI → EgoGenesis | 확인 |  |
| EgoDex → EgoGenesis | 확인 |  |
| DexWM → EgoExoWM | 확인 |  |
| DWM → EgoSim | 확인 |  |
| EgoExo4D → EgoSim | 확인 |  |

## 구성 요소 (`part_of`, 1)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| EgoXData6M → EgoXperience | 확인 |  |

## 캡처 장비 (`captures`, 1)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| HOMIEGen2 → EgoXData6M | 원문 |  |

## 산출물 (`produces`, 1)

| source → target | 근거 | 메모 |
| --- | --- | --- |
| MINT → MINTEgoPipe | 원문 |  |

