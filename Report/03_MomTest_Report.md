# Mom Test 보고서 — UnitConverter_19

**프로젝트:** UnitConverter_19  
**일자:** 2026-06-11  
**방법:** Mom Test 인터뷰 (개발자 페르소나)  
**대상 코드:** `UnitConverter.py`, `README.md`  
**개정:** 03 — RGIO Role/Goal/Input/Output 정정, Input·Output 형식 명세, `convert()` 함수 계약 추가 (02 대비)

---

## 1. 페르소나

**역할:** 이 코드베이스를 실습·유지보수하면서 CLI 길이 변환을 사용하는 백엔드 개발자

**배경 (과거 사실):**
- README 요구사항(OCP, 설정 외부화, 동적 단위, JSON/CSV 출력, TC)을 보며 `UnitConverter.py`를 실행·수정해 왔음
- `meter:2.5` 형식으로 meter / feet / yard 변환 출력을 여러 번 실행함
- feet 견적을 m로 맞출 때 엑셀·계산기·스크립트를 오가며 확인한 경험 있음
- 테스트·설정 파일·동적 단위 등록은 아직 미구현 또는 일부만 시도한 상태

---

## 2. 인터뷰 요약

### Q1. 최근 이 코드에서 가장 짜증났던 점은?

**Mom test:** 준수 (약함 — “가장 짜증”은 추상화 위험)

| 시점 | 경험 |
|------|------|
| 이번 주 수요일 | cubit 추가 시 `elif` 분기·상수·출력을 손으로 추가, `3.28084`/`1.09361` 재확인 |
| 화요일 | TC 6케이스마다 `python UnitConverter.py` 재실행·재입력, 소수 자릿수 눈 대조 |
| 지난주 금요일 | `feet:-1`이 README와 달리 그대로 출력 — TC 메모로 기록 |

**현재 방식:** 1~2개 값은 스크립트, 여러 케이스는 엑셀 식 사용

---

### Q2. 코드 탐색할 때 가장 자주 다시 확인하는 정보는?

**Mom test:** 준수

| 확인 항목 | 내용 |
|-----------|------|
| 변환 비율 | README `3.28084`, `1.09361` ↔ 코드 19~21, 27~28줄 |
| 지원 단위 | `meter` / `feet` / `yard` 문자열, `unit:value` 포맷 |
| README vs 구현 | 음수 검증·설정 외부화·동적 단위·JSON 출력 구현 여부 |
| 환산 흐름 | 입력 → `meter_value` → 세 단위 출력 (meter 경유) |

---

### Q3. 마지막으로 새 단위 추가 시 수정한 파일은?

**Mom test:** 준수

- **수정:** `UnitConverter.py`만 (`elif`, meter 환산, print)
- **참조만:** `README.md` (cubit `0.4572` 비율)
- **없음:** 설정 JSON/YAML, 테스트 파일
- cubit 수정은 로컬 시도 후 되돌리거나 미커밋 상태

---

### Q4. 입력 형식과 다른 값을 넣어 불편했던 적은?

**Mom test:** 준수 (약함 — “~없어?” 부정형)

| 입력 | 결과 | 재작업 |
|------|------|--------|
| `2.5 meter` | Invalid format | `meter:2.5`로 재입력 |
| `meters:2.5` | Unknown unit | 재실행 |
| `feet 8.2` | Invalid format | 형식 재맞춤 |
| `meter:abc` | Invalid number | 단위부터 재확인 |
| `meter:-1` | 출력됨 (미검증) | TC 메모 |

---

### Q5. 동작 검증 시 불편한 점·소요 시간

**Mom test:** 준수 (약함 — “있다면” 조건문)

**지난주 화요일 오후 — TC 6케이스: 총 25~30분**

| 항목 | 시간 | 원인 |
|------|------|------|
| 케이스마다 수동 실행·재입력 | 15~18분 | `input()` 1회, 오류 시 전체 재시작 |
| 출력 소수 자릿수 대조 | 5~7분 | 엑셀 반올림 vs 긴 float 출력 |
| 형식/단위 오타 | 3~5분 | 2회 재실행 |
| README vs 코드 갭 | 5분 | `feet:-1` 음수 검증 불일치 |

**비교:** 동일 6케이스 엑셀 3~5분 vs 스크립트만 25~30분

---

## 3. 표면 문제 vs 진짜 문제

### 표면 문제 (❌ 솔루션 섞임 — 사용 금지)

| 표면 문제 | 왜 표면 문제인가 |
|-----------|------------------|
| 설정 파일(JSON)로 단위 등록 필요 | 해결책(설정 외부화) 포함 |
| OCP/SRP 리팩터링 변환기 필요 | 설계·제품 형태를 문제로 착각 |
| pytest로 TC 일괄 실행 필요 | 도구 선택이 본문 |
| 자연스러운 CLI 입력 필요 | 입력 UX 솔루션 |
| JSON/CSV 출력 옵션 필요 | 미래·기능 제안 |

### 진짜 문제 (✅ 한 문장)

> **길이 단위를 README 기준으로 맞추거나 케이스를 검증할 때, 변환 비율·단위 이름·구현 범위를 코드와 문서 사이에서 반복 확인하고, CLI를 케이스마다 수동 실행·재입력하며 출력과 엑셀 기대값을 눈으로 대조해야 해서, 오타·형식 실수·반올림 차이 때문에 같은 확인을 여러 번 다시 하고 한 세션에 25~30분까지 쓰는 일이 생긴다.**

**핵심:** 변환기/설정/테스트 프레임워크 부재가 아니라 **반복 확인 + 끊기는 검증 흐름 + 재작업**

---

## 4. Mom Test 증거 (3줄)

1. **지난주 화요일** TC 6개 — 케이스마다 `python UnitConverter.py` 재실행, `2.5 meter`·`meters:2.5` 오타 재입력 — **25~30분** (엑셀 **3~5분**)
2. **이번 주 수요일** cubit 추가 — **`UnitConverter.py`만** 수정, `elif`·상수·출력 손수 추가, README 비율 재대조
3. **`feet:-1`** 미차단 → README 음수 검증 불일치 TC 메모; 탐색 시 README 비즈니스 로직·요구사항 체크리스트 반복 확인

---

## 5. R-G-I-O

> **R-G-I-O 정의:** Role(역할) · Goal(목표) · Input(사용자 입력 형식) · Output(출력 결과물 형식·성공/실패 기준)

### 주제 (1문장)

**README 기준 길이 단위 변환을 검증·확장할 때, 반복 수동 확인과 끊기는 CLI 검증 흐름 때문에 재작업과 시간 손실이 발생한다.**

| | 내용 |
|---|------|
| **R — Role** | README 기준으로 `UnitConverter.py` CLI 길이 변환을 실행·수정·검증하는 백엔드 개발자 (§1 페르소나) |
| **G — Goal** | README 변환 결과와 구현을 빠르게 확신하고, cubit 등 신규 단위를 기존 3단위와 동일 기준으로 맞추며 README **기본·품질** 요구를 이어가는 것 |

### I — Input (사용자 입력 형식)

| 항목 | 규격 |
|------|------|
| **형식** | `단위:값` — 콜론(`:`)으로 단위명과 숫자 분리 |
| **예시 (정상)** | `meter:2.5`, `feet:8.2`, `yard:2.7` |
| **지원 단위** | `meter`, `feet`, `yard` (README 기본 2) |
| **값** | 0 이상의 실수 (README 품질 — 음수 불가) |
| **비정상 입력 (거부 대상)** | `2.5 meter` (형식 오류), `feet 8.2` (형식 오류), `meter:abc` (숫자 오류), `meters:2.5` (미지원 단위), `meter:-1` / `feet:-1` (음수) |

### O — Output (출력 결과물·성공/실패 기준)

#### 성공 — 정상 변환 출력

| 항목 | 규격 |
|------|------|
| **형식** | `{입력값} {입력단위} = {환산값} {대상단위}` (줄 단위, 입력 단위 제외한 나머지 단위 각 1줄) |
| **예시** | `meter:2.5` 입력 시 |
| | `2.5 meter = 8.2 feet` |
| | `2.5 meter = 2.7 yard` |
| **계산 기준** | `1 meter = 3.28084 feet`, `1 meter = 1.09361 yard`; feet↔yard는 meter 경유 |
| **입력 단위** | meter·feet·yard **각각** 입력 단위로 동일 형식 출력 (README 기본 1·2) |

#### 실패 — 입력 검증 출력 (README 품질)

| 입력 유형 | 예시 입력 | 기대 동작 | 기대 출력 (또는 동등 메시지) |
|-----------|-----------|-----------|------------------------------|
| 형식 오류 | `2.5 meter`, `feet 8.2` | 변환 없이 종료 | `Invalid format` 포함 — `unit:value` 안내 |
| 숫자 오류 | `meter:abc` | 변환 없이 종료 | `Invalid number` 포함 — 잘못된 값 표시 |
| 미지원 단위 | `meters:2.5` | 변환 없이 종료 | `Unknown unit` 포함 — 단위명 표시 |
| 음수 | `meter:-1`, `feet:-1` | 변환 없이 종료 | 음수 거부 (README 품질; 현재 `feet:-1` 갭 — §4 증거 3) |

#### Output 성공 판정 요약

| 판정 | 기준 |
|------|------|
| **성공** | 정상 입력 → README 예시와 일치하는 변환 줄 출력; 비율·반올림이 TC 기대값과 일치 |
| **실패** | 비정상 입력 → 변환 줄 **없음** + 위 검증 메시지(또는 동등) 출력; 음수·형식·미지원 단위 **0건** 누락 |
| **검증** | §6 성공 기준(B·L·Q·M) TC로 Input→Output 매핑 자동 확인; 6케이스 **5분 이내** |

### 함수 계약 — `convert(input_str)`

Input에 따라 Output이 결정되도록 검증·구현 단위를 함수로 명시한다.

**함수 시그니처**

```python
convert(input_str: str) -> dict
```

| 구분 | 내용 |
|------|------|
| **Input (입력)** | `input_str: str` — CLI 사용자 입력<br>형식: `단위:값` (콜론 1개)<br>지원 단위: `meter`, `feet`, `yard`<br>값: 0 이상 실수 |
| **Output (출력)** | `{ "status": "pass" \| "fail", "lines": list[str], "error": dict \| None }`<br>· `lines`: 변환 결과 문장 (pass 시만)<br>· `error`: fail 시 `{ "type": str, "message": str }`, pass 시 `None` |
| **pass** | 형식·단위·숫자·음수 검증 통과 → `status = "pass"`, `error = None`<br>입력 단위 제외, 나머지 단위마다 1줄 (`§5 O` 형식·비율·반올림)<br>예: `convert("meter:2.5")` → `lines = ["2.5 meter = 8.2 feet", "2.5 meter = 2.7 yard"]` |
| **fail — format** | `:` 없음·공백 분리 등 → `status = "fail"`, `lines = []`<br>`error = { "type": "format", "message": "Invalid format. Use unit:value (ex: meter:2.5)" }` |
| **fail — number** | 값 파싱 불가 → `status = "fail"`, `lines = []`<br>`error = { "type": "number", "message": "Invalid number: {값}" }` |
| **fail — unit** | 미등록 단위 → `status = "fail"`, `lines = []`<br>`error = { "type": "unit", "message": "Unknown unit: {단위}" }` |
| **fail — negative** | 값 < 0 → `status = "fail"`, `lines = []`<br>`error = { "type": "negative", "message": "Negative value not allowed: {값}" }` |
| **error.type** | `format` / `number` / `unit` / `negative` |

#### pass / fail 예시 (Input → Output)

| input_str | status | lines | error |
|-----------|--------|-------|-------|
| `"meter:2.5"` | `pass` | `["2.5 meter = 8.2 feet", "2.5 meter = 2.7 yard"]` | `None` |
| `"feet:8.2"` | `pass` | `["8.2 feet = 2.5 meter", "8.2 feet = 2.7 yard"]` | `None` |
| `"yard:2.7"` | `pass` | `["2.7 yard = 2.5 meter", "2.7 yard = 8.2 feet"]` | `None` |
| `"2.5 meter"` | `fail` | `[]` | `{ "type": "format", ... }` |
| `"meter:abc"` | `fail` | `[]` | `{ "type": "number", ... }` |
| `"meters:2.5"` | `fail` | `[]` | `{ "type": "unit", ... }` |
| `"feet:-1"` | `fail` | `[]` | `{ "type": "negative", ... }` |

**현재 `UnitConverter.py`와의 갭:** `main()`은 `print` 직접 출력, pass 시 입력 단위 줄 포함, 음수 미검증 — §5·함수 계약은 README 기준.

---

## 6. 성공 기준

> README **기본·품질** 요구를 RGIO **Input·Output**(§5) 및 `convert()` 함수 계약과 1:1로 매핑해 TC로 측정한다.  
> 프레임워크·설정 파일·JSON/CSV 출력 포맷 등 **솔루션은 명시하지 않는다** (§3 표면 문제 규칙).

### 기본 요구사항

| # | README | 기준 | 측정 |
|---|--------|------|------|
| B1 | 기본 1 — `단위:값` 입력 → 다른 단위 출력 | **변환 출력 확신** | `convert("meter:2.5")` → `status=pass`, `lines`가 README 예시와 일치; 엑셀 수동 대조 **0회** |
| B2 | 기본 2 — meter / feet / yard | **3단위 입력 커버** | meter·feet·yard **각각** `convert()` pass TC 1건 이상; `lines` 정확 |
| B3 | 기본 3 — 추가 시 변경 최소화 | **확장 시 기존 비침** | cubit(또는 동등 신규 단위) 추가 후 meter/feet/yard 관련 기존 로직·TC **변경 0건** |
| B4 | 기본 4 — 변환 정확성 TC | **변환 정확성 TC** | 지원 단위 쌍 `convert()` pass TC; README 비율·반올림을 기대값에 명시 |

### 비즈니스 로직

| # | README | 기준 | 측정 |
|---|--------|------|------|
| L1 | `3.28084` / `1.09361` | **비율 단일 기준** | `convert()` pass TC 기대값에 두 상수 반영 |
| L2 | feet/yard는 meter 경유 | **간접 환산 일관** | feet↔yard `convert()` pass TC가 meter 기준 환산과 일치 |

### 품질 요구사항

| # | README | 기준 | 측정 |
|---|--------|------|------|
| Q1 | OCP | **확장에 닫힘** | B3와 동일 |
| Q2 | SRP | **역할별 수정 분리** | 검증 수정 시 변환 비율·단위 목록·출력 형식을 같이 건드리지 않아도 Q3~Q5 TC 통과 |
| Q3 | 입력 검증 — 음수 | **음수 차단** | `convert("feet:-1")` → `status=fail`, `error.type=negative` |
| Q4 | 입력 검증 — 잘못된 형식 | **형식 오류 식별** | `convert("2.5 meter")` → `fail`/`format`; `convert("meter:abc")` → `fail`/`number` |
| Q5 | 입력 검증 — 없는 단위 | **미지원 단위 거부** | `convert("meters:2.5")` → `fail`/`unit` |

### Mom Test 검증 흐름 (§5 Input 형식 → Output 성공/실패)

| # | 기준 | 측정 |
|---|------|------|
| M1 | 검증 시간 | B1~B4·Q3~Q5 `convert()` TC **6케이스 이상** **5분 이내** (현재 25~30분) |
| M2 | 재작업 감소 | `convert()` 반환 dict로 케이스 단위 검증; CLI 재입력·엑셀 눈대조 **0회** |
| M3 | README↔코드 일치 | Q3~Q5 `convert()` TC 통과 = README 품질과 일치 |

### 02 대비 변경 요약

| 02 | 03 처리 |
|----|---------|
| RGIO Reality/Issue/Outcome 잔존 가능 | **Role · Goal · Input(입력 형식) · Output(출력·성공/실패)** 로 확정 |
| Output 서술형 표만 | **`convert(input_str) -> dict` 함수 계약** + pass/fail 예시 표 추가 |
| §6 TC가 CLI 출력 기준 | **`convert()` 반환값** 기준으로 B·Q·M 측정 문구 정렬 |
| — | 현재 `UnitConverter.py` 갭(음수·입력단위 줄·print) 명시 |

### 01 대비 변경 요약

| 01 # | 03 처리 |
|------|---------|
| 1~5 성공 기준 5항 | **B·L·Q·M** 4계층 + `convert()` 계약 |
| RGIO Outcome 중심 | **Input 형식 · Output 성공/실패 · 함수 계약** |

---

## 7. 설계 힌트 (솔루션 확정 아님)

| Pain | 방향 힌트 |
|------|-----------|
| 케이스마다 재실행·재입력 | `convert()` 단위로 Input→Output 일괄 검증 |
| cubit = elif·상수·출력 3곳 | 단위·비율이 한곳에 없음 |
| README↔코드 불일치 | 함수 계약·TC가 “맞는 기준”을 코드로 고정 |

---

## 8. Mom Test 질문 품질 회고

| 질문 | 평가 | 개선안 |
|------|------|--------|
| 가장 짜증났던 점 | 준수(약) | 마지막 실행·수정 시 어디서 시간이 걸렸는지 |
| 자주 확인하는 정보 | 준수 | README 맞출 때 마지막으로 다시 본 숫자·규칙 |
| 단위 추가 시 수정 파일 | 준수 | — |
| 입력 형식 불편 | 준수(약) | 막힌 마지막 경우 — 무엇을 넣었고 무엇이 나왔는지 |
| 검증 불편·시간 | 준수(약) | 지난번 TC 확인 처음~끝 몇 분, 어디서 멈췄는지 |

---

*보고서 생성: Mom Test 인터뷰 세션 기반 · 03개정: RGIO 정정 + convert() 함수 계약*
