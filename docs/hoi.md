# 번외 · 물리 기반 잡기/HOI 합성

> `scripts/build.py`가 `data/hoi.csv`에서 자동 생성합니다. 직접 수정하지 마세요.
> 에고센트릭 지형도와 별개인 번외 정리입니다. 그래프·통계·검토 대기·데일리 스캔에 포함되지 않습니다.

## 정지 잡기 생성·접촉 보정 (4)

| 연구 | 게재처 | arXiv | 대상 | 방식 | 물리 고려 | 관련성 |
| --- | --- | --- | --- | --- | --- | --- |
| GRAB: A Dataset of Whole-Body Human Grasping of Objects (GrabNet) | ECCV 2020 | [2008.11200](https://arxiv.org/abs/2008.11200) | SMPL-X 전신 + MANO 손 | 전신 잡기 모캡 데이터셋과 정지 잡기 생성기 GrabNet | 없음 (운동학) | D-Grasp 등 물리 RL이 목표 잡기 자세(reference)로 가져다 쓰는 출발점 |
| Hand-Object Contact Consistency Reasoning for Human Grasps Generation (GraspTTA) | ICCV 2021 | [2104.03304](https://arxiv.org/abs/2104.03304) | MANO 손 | 생성한 잡기를 시험 시점에 손-물체 접촉 일관성(자기지도)으로 보정. 처음 보는 물체에서 효과 큼 | 간접적 (시뮬레이션 안정성으로 평가) | 물리 RL 전에 목표 잡기 품질을 올리는 전처리 후보 |
| ContactOpt: Optimizing Contact to Improve Grasps | CVPR 2021 | [2104.07267](https://arxiv.org/abs/2104.07267) | MANO 손 | DeepContact가 접촉 위치 예측 → DiffContact로 손 자세를 경사 최적화. 연조직을 흉내 내 약간의 관통 허용 | 간접적 (접촉 품질, 관통·떠 있음 감소) | 영상 추정 손 자세를 물리 시뮬레이터에 넣기 전 정리 |
| FLEX: Full-Body Grasping Without Full-Body Grasps | CVPR 2023 | [2211.11903](https://arxiv.org/abs/2211.11903) | SMPL-X 전신 + 오른손 | 사전학습된 오른손 잡기 모델과 전신 포즈 prior의 잠재 공간을 3D 기하 제약(접촉·관통·지면 등)으로 함께 탐색해 전신 잡기 자세 생성. 3D 전신 잡기 데이터 불필요 | 없음 (운동학·기하 제약) | 전신 데이터 없이 전신 목표 잡기 자세를 만들 수 있음. 물리 기반 전신 제어기(Braun et al., Omnigrasp 계열)에 넣을 목표 자세 후보 |

## MANO 손 + 물리 강화학습 (4)

| 연구 | 게재처 | arXiv | 대상 | 방식 | 물리 고려 | 관련성 |
| --- | --- | --- | --- | --- | --- | --- |
| D-Grasp: Physically Plausible Dynamic Grasp Synthesis for Hand-Object Interactions | CVPR 2022 | [2112.03028](https://arxiv.org/abs/2112.03028) | MANO 손 (물리 시뮬레이터) | 정지 잡기 하나를 목표로 받아 강화학습으로 잡고 목표 6D 포즈까지 옮김. 저수준 잡기 + 고수준 동작 계층 구조 | 잡기 + 들어 올리기·이동을 물리로 성공시키는 것이 목표 | 계보의 출발점. 목표 잡기는 데이터셋·생성기·영상 추정 어디서든 받을 수 있음 |
| ArtiGrasp: Physically Plausible Synthesis of Bi-Manual Dexterous Grasping and Articulation | 3DV 2024 | [2309.03891](https://arxiv.org/abs/2309.03891) | MANO 양손 | D-Grasp 확장. 정책 하나로 양손 잡기와 관절 물체(뚜껑·서랍 등) 조작. 잡음 섞인 영상 추정 자세로도 동작 | 물리 기반 (RaiSim) | 양손·관절 물체 작업이 필요할 때 |
| GraspXL: Generating Grasping Motions for Diverse Objects at Scale | ECCV 2024 | [2403.19649](https://arxiv.org/abs/2403.19649) | MANO 손 + 로봇손 | 물체 58개로 학습한 RL 정책 하나로 처음 보는 물체 50만 개 이상을 82.2% 성공률로 잡고 움직임. 손-물체 상호작용 데이터 불필요 | 물리 기반 | 가장 유력. 물체별 학습 없이 쓰거나, 공개된 50만+ 물체 생성 동작을 바로 가져다 쓸 수 있음 |
| PiHand: Latent Hand-Object Interaction Priors for Physics-Based Policy Learning | — | [2610.31299](https://arxiv.org/abs/2610.31299) | 손 (MANO 사용 여부 미확인) | 모캡 추종 전문가 정책들을 목표 조건 VAE로 증류해 잠재 HOI prior를 만들고, 그 잠재 공간에서 잔차 탐색으로 조작 과제 해결. 단일 보상·커리큘럼 없음 | 물리 기반 | 최신(10월). 손 동작 prior를 재사용하는 방식이라 새 과제 적응이 빠를 가능성 |

## 미분 가능 물리·영상→물리 보정 (4)

| 연구 | 게재처 | arXiv | 대상 | 방식 | 물리 고려 | 관련성 |
| --- | --- | --- | --- | --- | --- | --- |
| Grasp'D: Differentiable Contact-rich Grasp Synthesis for Multi-fingered Hands | ECCV 2022 | [2208.12250](https://arxiv.org/abs/2208.12250) | MANO 손 + 로봇손 | 미분 가능 시뮬레이션으로 잡기 자세 최적화. 해석적 방법보다 접촉이 4배 이상 조밀 | 접촉력과 안정성을 최적화에 직접 반영 | 정적 잡기 품질 기준. 동작(시간축)은 다루지 않음 |
| Fast-Grasp'D: Dexterous Multi-finger Grasp Generation Through Differentiable Simulation | — | [2306.08132](https://arxiv.org/abs/2306.08132) | 로봇손 (3·4·5지) | Grasp'D 가속 (GraspIt! 대비 10배, Grasp'D 대비 20배). Grasp'D-1M 데이터셋 공개 | 물리 기반 (미분 가능) | 로봇손 쪽이라 참고용 |
| Hand-Object Interaction Controller (HOIC): Deep Reinforcement Learning for Reconstructing Interactions with Physics | — | [2405.02676](https://arxiv.org/abs/2405.02676) | 손 + 물체 (RGBD 입력) | 단일 RGBD 카메라 관측을 물리 안에서 강화학습 제어기로 따라가며 손-물체 동작을 복원 | 물리 기반 | 영상 → 물리 복원의 RL 버전 |
| Grasp-and-Lift: Executable 3D Hand-Object Interaction Reconstruction via Physics-in-the-Loop Optimization | — | [2601.18121](https://arxiv.org/abs/2601.18121) | MANO 손 (영상 복원 결과) | 영상으로 복원한 손-물체 시연을 시뮬레이터 안 블랙박스 최적화로 보정. 잡고 들어 올리기 성공을 최대화하면서 원래 시연과의 차이는 최소화 | 물리 성공(잡기·들기)을 직접 목표로 함 | 영상에서 얻은 HOI를 물리적으로 실행 가능하게 만드는 후처리. DexYCB·HO-3D |

## 전신 휴머노이드 + 물리 (8)

| 연구 | 게재처 | arXiv | 대상 | 방식 | 물리 고려 | 관련성 |
| --- | --- | --- | --- | --- | --- | --- |
| Physically Plausible Full-Body Hand-Object Interaction Synthesis | 3DV 2024 | [2309.07907](https://arxiv.org/abs/2309.07907) | SMPL-X 계열 전신 + 손 | 몸·손 스킬 prior를 따로 학습한 뒤 그 잠재 공간에서 고수준 정책을 RL로 학습. 적대적 스타일 보상 + 과제 보상 | 물리 기반 | 전신 + 손 + 물리를 처음 묶은 작업. Omnigrasp의 비교 대상 |
| PhysHOI: Physics-Based Imitation of Dynamic Human-Object Interaction | — | [2312.04393](https://arxiv.org/abs/2312.04393) | 휴머노이드 | 운동학 HOI 시연을 물리 안에서 모방. 신체 부위-물체 접촉 그래프 보상이 핵심. BallPlay(농구 8개 기술) 데이터셋 | 물리 기반 | 물체 다양성보다 동작 모방이 목적 |
| Omnigrasp: Grasping Diverse Objects with Simulated Humanoids | NeurIPS 2024 | [2407.11385](https://arxiv.org/abs/2407.11385) | SMPL-X 전신 휴머노이드 + 양손 | 사전학습한 범용 동작 표현(PULSE-X)을 행동 공간으로 써서, 1,200개 이상 물체를 집고 무작위 궤적으로 옮김. 짝지은 전신-물체 데이터 불필요 | 물리 기반 (Isaac Gym) | 전신(SMPL-X) + 손 + 물리라 최종 목표와 가장 비슷함 |
| SkillMimic: Learning Basketball Interaction Skills from Demonstrations | CVPR 2025 | [2408.15270](https://arxiv.org/abs/2408.15270) | 휴머노이드 | PhysHOI 후속. 손으로 설계한 기술별 보상 없이 한 설정으로 여러 HOI 기술 학습 | 물리 기반 | PhysHOI 계열. 후속 SkillMimic-V2 (2505.02094) |
| MaskedMimic: Unified Physics-Based Character Control Through Masked Motion Inpainting | SIGGRAPH Asia 2024 | [2409.14393](https://arxiv.org/abs/2409.14393) | 휴머노이드 | 캐릭터 제어를 동작 인페인팅으로 정식화해, 희소한 관절 목표 등 다양한 조건에서 하나의 모델로 제어 | 물리 기반 | 범용 전신 제어기. 아래 MaskedManipulator의 기반 |
| MaskedManipulator (MaskedMimic의 전신 물체 조작 확장) | — | [2505.19086](https://arxiv.org/abs/2505.19086) | 전신 휴머노이드 + 손 | MaskedMimic을 전신 물체 조작으로 확장 | 물리 기반 | 전신 조작 제어기 후보 |
| InterReal: A Unified Physics-Based Imitation Framework for Learning Human-Object Interaction Skills | — | [2603.07516](https://arxiv.org/abs/2603.07516) | 휴머노이드 (실제 로봇 포함) | 물리 기반 HOI 모방을 실제 휴머노이드 로봇까지 확장 | 물리 기반 | PhysHOI 계열의 실로봇 방향 |
| CoorDex: Coordinating Body and Hand Priors for Continuous Dexterous Humanoid Loco-Manipulation | — | [2606.23680](https://arxiv.org/abs/2606.23680) | 전신 휴머노이드 + 손 | 몸·손 prior를 고정 잠재 행동 공간으로 두고 잔차 RL로 이동하며 조작 | 물리 기반 | Omnigrasp와 가장 가까운 2026년 후속 방향 (잡기보다 연속 이동 조작) |

## 사람 손 → 로봇손 전이 (4)

| 연구 | 게재처 | arXiv | 대상 | 방식 | 물리 고려 | 관련성 |
| --- | --- | --- | --- | --- | --- | --- |
| QuasiSim: Parameterized Quasi-Physical Simulators for Dexterous Manipulations Transfer | ECCV 2024 | [2404.07988](https://arxiv.org/abs/2404.07988) | 사람 손 → 로봇손 | 준물리 시뮬레이터 커리큘럼으로 사람 조작 동작을 로봇손이 따라가게 전이 | 물리 기반 | 로봇 쪽 |
| DexTrack: Towards Generalizable Neural Tracking Control for Dexterous Manipulation from Human References | ICLR 2025 | [2502.09614](https://arxiv.org/abs/2502.09614) | 사람 손 → 로봇손 | 사람 참조 동작-로봇 행동 쌍을 대량으로 모아 범용 추종 제어기 학습 | 물리 기반 | 로봇 쪽. QuasiSim 후속 |
| ManipTrans: Efficient Dexterous Bimanual Manipulation Transfer via Residual Learning | CVPR 2025 | [2503.21860](https://arxiv.org/abs/2503.21860) | 사람 양손 → 로봇 양손 | 범용 궤적 모방기 사전학습 + 상호작용 제약 하 잔차 모듈 미세조정. DexManipNet(3.3K 에피소드) 구축 | 물리 기반 | 로봇 쪽이라 목적과는 거리가 있음 |
| DexMachina: Functional Retargeting for Bimanual Dexterous Manipulation | ICML 2026 (NVIDIA 페이지 표기) | [2505.24853](https://arxiv.org/abs/2505.24853) | 사람 손 → 로봇 양손 | 시연 하나에서 물체 상태를 따라가도록 학습. 점점 약해지는 가상 물체 제어기 커리큘럼 | 물리 기반 | 로봇 쪽 |

## 로봇손 잡기 (참고) (3)

| 연구 | 게재처 | arXiv | 대상 | 방식 | 물리 고려 | 관련성 |
| --- | --- | --- | --- | --- | --- | --- |
| DexGraspNet: A Large-Scale Robotic Dexterous Grasp Dataset for General Objects Based on Simulation | ICRA 2023 | [2210.02697](https://arxiv.org/abs/2210.02697) | 로봇손 (ShadowHand) | 물체 5,355개에 대한 잡기 132만 개를 Isaac Gym에서 검증한 데이터셋 | 물리 기반 | 사람 손이 아님. 물체 다양성 참고 |
| UniDexGrasp: Universal Robotic Dexterous Grasping via Learning Diverse Proposal Generation and Goal-Conditioned Policy | CVPR 2023 | [2303.00938](https://arxiv.org/abs/2303.00938) | 로봇손 | 잡기 제안 생성 + 목표 조건 정책 2단계 | 물리 기반 (RL) | 사람 손이 아님 |
| UniDexGrasp++: Improving Dexterous Grasping Policy Learning via Geometry-aware Curriculum and Iterative Generalist-Specialist Learning | ICCV 2023 | [2304.00464](https://arxiv.org/abs/2304.00464) | 로봇손 | 기하 인지 커리큘럼 + 일반-전문 정책 반복 학습. 학습/시험 성공률 85.4/78.2% | 물리 기반 (RL) | 사람 손이 아님 |

## 연결

| source → target | 관계 | 근거 | 메모 |
| --- | --- | --- | --- |
| GRAB → D-Grasp | 백본으로 사용 | 추정 | 정지 잡기를 목표 자세(reference)로 사용 |
| D-Grasp → ArtiGrasp | 직접 확장 | 확인 | 양손·관절 물체로 확장 (같은 그룹) |
| D-Grasp → GraspXL | 직접 확장 | 추정 | 같은 그룹, 물체 규모 확장 |
| ArtiGrasp → GraspXL | 개념 연결 | 추정 | 같은 그룹 후속 |
| D-Grasp → Braun et al. | 개념 연결 | 추정 | 손 → 전신으로 확장 (공저자 Christen) |
| GRAB → Braun et al. | 평가 데이터 | 확인 | GRAB 기준 평가 |
| Braun et al. → Omnigrasp | 비교 기준선 | 확인 | Omnigrasp의 비교 대상 |
| Omnigrasp → CoorDex | 개념 연결 | 추정 | 몸·손 prior를 행동 공간으로 쓰는 방향 |
| GRAB → PiHand | 평가 데이터 | 확인 | GRAB·DexYCB 평가 |
| D-Grasp → PiHand | 개념 연결 | 추정 | MANO 손 물리 RL 계보 |
| PhysHOI → SkillMimic | 직접 확장 | 추정 | 같은 1저자 후속 |
| PhysHOI → InterReal | 개념 연결 | 추정 | HOI 모방을 실로봇으로 |
| MaskedMimic → MaskedManipulator | 직접 확장 | 확인 | 전신 물체 조작으로 확장 |
| MaskedManipulator → CoorDex | 개념 연결 | 추정 | 전신 조작 제어기 |
| Grasp'D → Fast-Grasp'D | 직접 확장 | 확인 | 20배 가속 |
| ContactOpt → GraspTTA | 개념 연결 | 추정 | 접촉 기반 잡기 보정 |
| ContactOpt → Grasp-and-Lift | 개념 연결 | 추정 | 영상 추정 HOI 보정 (접촉 → 물리 성공) |
| HOIC → Grasp-and-Lift | 개념 연결 | 추정 | 영상 → 물리 복원 |
| GraspTTA → UniDexGrasp | 비교 기준선 | 확인 | UniDexGrasp의 기준선 |
| DexGraspNet → UniDexGrasp | 학습 데이터 | 추정 |  |
| UniDexGrasp → UniDexGrasp++ | 직접 확장 | 확인 | 성공률 +11%p |
| QuasiSim → DexTrack | 직접 확장 | 추정 | 같은 그룹 후속 |
| QuasiSim → ManipTrans | 비교 기준선 | 추정 |  |
| ManipTrans → DexMachina | 비교 기준선 | 추정 |  |
| Grasp'D → GraspXL | 개념 연결 | 추정 | MANO + 로봇손 양쪽 대상 |
| GRAB → FLEX | 백본으로 사용 | 추정 | GrabNet 계열 손 잡기 모델과 GRAB 물체를 사용한 것으로 보임 |
| FLEX → Braun et al. | 개념 연결 | 추정 | 운동학 전신 잡기 → 물리 전신 잡기 |
