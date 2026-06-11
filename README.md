
## Unit Converter (Python)
![unit-converter](./unit-converter.jpg)
### Overview
- 사용자가 입력한 길이(`단위:값`)를 기반으로, 해당 값을 다른 모든 단위로 변환해 출력하는 프로그램.
- 새로운 단위를 추가할 때 기존 코드의 변경이 최소화되도록 설계한다.
- 각 단위 변환 로직은 테스트 코드로 검증한다.

### 가상환경 설정 및 실행
```bash
# 가상환경 생성
python -m venv venv

# 가상환경 활성화 (Windows)
venv\Scripts\activate

# 가상환경 활성화 (macOS/Linux)
source venv/bin/activate

# 실행
python UnitConverter.py

# 가상환경 비활성화
deactivate
```

### 기본 요구사항
1. 사용자 입력 예시:
   ```
   meter:2.5
   ```
   → 출력:
   ```
   2.5 meter = 8.2 feet
   2.5 meter = 2.7 yard
   ...
   ```

2. 현재 지원 단위:
   - meter
   - feet
   - yard

3. 새로운 단위가 추가될 때도 기존 코드의 변경이 최소화되도록 할 것.

4. 각 단위 간 변환이 정확히 계산되도록 테스트 코드를 작성할 것.

### 비즈니스 로직
- `1 meter = 3.28084 feet`
- `1 meter = 1.09361 yard`
- feet/yard 간의 비율은 meter 기반으로 계산.

### 품질 요구사항
- OCP를 만족하는 설계
- SRP를 만족하는 클래스 구성
- 입력 값 검증 (음수, 잘못된 형식, 없는 단위)

### 추가 요구사항
- **설정 외부화**
   - 변환 비율을 외부 설정 파일(JSON/YAML)에서 로드
- **동적으로 단위와 비율을 등록할 수 있도록 한다**
   - 사용자 입력으로 `1 cubit = 0.4572 meter`를 등록하고 사용 가능
- **출력 포맷 선택 기능** 
   - JSON / CSV / 표 형태 출력


## 진행 계획 (Todo)

> SSOT: `.cursorrules`, `docs/PRD.md` · **Dual Track TDD** (Logic → UI) · **BCE** · **ARRR** (케이스당 RED → GREEN → REFACTOR)

### TDD 진행 원칙

- **케이스 1건씩:** Arrange → Red → Green → Refactor (한 번에 여러 FR 금지)
- **Logic Track 먼저** (`tests/test_convert.py` → `src/convert.py`), **전 케이스 GREEN 후 UI Track**
- **커맨드 순서:** `/red-test-plan` → `/tdd-red` → `/green-minimal` → `/refactor-smell` → `/refactor-safe`

| ARRR | 커맨드 | RED/GREEN |
|------|--------|-----------|
| Arrange | `/red-test-plan`, `/red-skeleton` | RED 준비 |
| **Red** | `/tdd-red` | **실패 TC** (`tests/` 만) |
| **Green** | `/green-minimal` | **최소 구현** (`src/` 또는 `UnitConverter.py`) |
| Refactor | `/refactor-smell`, `/refactor-safe` | 동작 유지 개선 |
| Report | `/export`, `/golden-master` | 기록·갭 대조 |

---

### 1. 분석·준비 (0.5시간) — 완료

- [x] 레거시 코드 구조·로직 파악 (`UnitConverter.py`)
- [x] Mom Test · RGIO · `convert()` 계약 (`Report/01~03_*`)
- [x] PRD · 추적표 (`docs/PRD.md`)
- [x] `.cursorrules`, ARRR 커맨드·스킬, pytest 골격

---

### 2. Logic Track — ARRR (Entity · Control)

> `tests/test_convert.py` RED 먼저 → `src/convert.py` GREEN. **케이스마다 RED 완료 후 GREEN.**

| FR | Arrange·Red | Green | Golden | Refactor |
|----|-------------|-------|--------|----------|
| FR-01 | [x] `test_fr_01_meter_2_5_returns_pass` | [x] meter 분기 | [x] T-FR-01 | [ ] |
| FR-02 | [x] `test_fr_02_feet_8_2_*`, `test_fr_02_yard_2_7_*` | [x] feet·yard 분기 | [x] T-FR-02, T-FR-02-YARD | [ ] |
| FR-03 | [x] `test_fr_03_meters_*`, `test_fr_03_cubit_*` | [x] unit 검증 | [x] T-FR-03, T-FR-03-CUBIT | [ ] |
| FR-04 | [x] `test_fr_04_meter_*`, `test_fr_04_feet_*` | [x] negative 검증 | [x] T-FR-04, T-FR-04-FEET | [ ] |
| FR-05 | [x] `test_fr_05_format_*`, `test_fr_05_number_*` | [x] format·number 검증 | [x] T-FR-05-FORMAT, T-FR-05-NUMBER | [ ] |

- [x] Logic Track 전 FR **RED → GREEN** 완료 (PRD §7) — `pytest tests/test_convert.py` **9 passed**
- [x] `/golden-master` — pass 3 + fail 6건 int[6] Approval (yard golden `T-FR-02-YARD`로 명칭 정리)
- [ ] NFR-01 OCP · NFR-02 SRP — `/refactor-smell` → `/refactor-safe`

---

### 3. UI Track — ARRR (Boundary)

> **Logic Track GREEN 후** 시작. `tests/test_main.py` RED → `UnitConverter.py` `main()` GREEN.

| 케이스 | Arrange·Red | Green | Refactor |
|--------|-------------|-------|----------|
| pass 출력 | [ ] `/tdd-red` stdout 변환 줄 | [ ] `/green-minimal` `main()` | [ ] |
| fail 출력 | [ ] `/tdd-red` 에러 메시지·변환 없음 | [ ] `/green-minimal` | [ ] |

- [ ] Boundary에 변환·검증 로직 없음 (`convert()` 호출·print 만)

---

### 4. 추가 요구사항 (2시간) — P1 · ARRR 동일

- [ ] EXT-01 설정 외부화 — RED → GREEN → REFACTOR
- [ ] EXT-02 동적 단위 등록 — RED → GREEN → REFACTOR
- [ ] EXT-03 출력 포맷 — RED → GREEN → REFACTOR

---

### 5. 회고 및 발표 (1시간)

- [x] Cursor Export (`Report/04_*` ~ `08_*`, `Prompting/04_*` ~ `08_*`)
- [x] Logic Track Golden Approval — FR-01~FR-05 전 TC matched
- [ ] UI Track (`tests/test_main.py`) — Logic GREEN 후 시작
- [ ] 실습 목표·달성도·AI·TC·리팩터링 회고 및 발표

---

## 생성형AI를 활용한 Activities (6 시간)

1. 문제 코드 및 기본 요구사항 분석 (0.5시간)
   - 기본 코드구조, 로직 이해
2. 기본 요구사항 및 품질 요구사항 구현 (2시간)
   - OCP를 만족하는 인터페이스 구현 
   - SRP를 만족하도록 클래스 구현 
   - 입력값 검증을 위한 구현
3. TC 구현 (0.5시간)
   - 단위변환 기능 검증 및 입력 값 검증 TC 작성 
4. 추가 요구사항 구현 (2시간)
   - 3개 요구사항 구현 및 TC 작성 
5. 회고 및 발표 (1시간)
   - 실습 목표와 달성도
   - AI를 어떻게 활용했나? 도움이 된 순간과 한계는?
   - TC를 추가해보면서 개선에 미친 영향, TC 작성 팁
   - 클린코드와 리팩토링에서 느낀 장점과 어려운점
