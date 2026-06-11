# PRD — UnitConverter_19

**버전:** 1.0  
**일자:** 2026-06-11  
**근거:** [Report/03_MomTest_Report.md](../Report/03_MomTest_Report.md), PRD→테스트 추적표, [README.md](../README.md)

---

## 1. 배경·문제

길이 단위를 README 기준으로 맞추거나 케이스를 검증할 때, 변환 비율·단위 이름·구현 범위를 코드와 문서 사이에서 반복 확인하고, CLI를 케이스마다 수동 실행·재입력하며 출력과 엑셀 기대값을 눈으로 대조해야 한다. 그 결과 오타·형식 실수·반올림 차이로 같은 확인을 여러 번 다시 하고, 한 세션에 25~30분까지 소요된다.

| 페르소나 | README 기준으로 `UnitConverter.py` CLI 길이 변환을 실행·수정·검증하는 백엔드 개발자 |
| 목표 | README 변환 결과와 구현을 빠르게 확신하고, cubit 등 신규 단위를 기존 3단위와 동일 기준으로 맞추며 README **기본·품질** 요구를 이어간다 |

---

## 2. 범위

### In Scope (P0)

- `unit:value` 형식 입력 파싱 및 meter / feet / yard 변환
- 입력 검증 (형식·숫자·미지원 단위·음수)
- `convert()` 함수 계약 기반 자동 TC
- OCP·SRP를 만족하는 기본 구조 (검증·변환·출력 역할 분리)

### Out of Scope (P1 — 추가 요구)

- 설정 파일(`units.json` 등)에서 비율 로드
- 런타임 동적 단위 등록 (`1 cubit = 0.4572 meter`)
- CLI 출력 포맷 선택 (`json` / `csv` / `table`)

---

## 3. 입력·출력 규격

### Input

| 항목 | 규격 |
|------|------|
| 형식 | `단위:값` — 콜론(`:`) 1개로 단위명과 숫자 분리 |
| 지원 단위 | `meter`, `feet`, `yard` |
| 값 | 0 이상 실수 |
| 정상 예시 | `meter:2.5`, `feet:8.2`, `yard:2.7` |
| 거부 대상 | `2.5 meter`, `feet 8.2`, `meter:abc`, `meters:2.5`, `meter:-1`, `feet:-1` |

### Output — CLI (성공)

| 항목 | 규격 |
|------|------|
| 형식 | `{입력값} {입력단위} = {환산값} {대상단위}` (줄 단위) |
| 줄 수 | 입력 단위 **제외**, 나머지 단위 각 1줄 |
| 예시 | `meter:2.5` → `2.5 meter = 8.2 feet`, `2.5 meter = 2.7 yard` |
| 비율 | `1 meter = 3.28084 feet`, `1 meter = 1.09361 yard`; feet↔yard는 meter 경유 |
| 반올림 | README 예시 기준 (소수 1자리: `8.2`, `2.7`, `2.5`) |

### Output — CLI (실패)

| 유형 | 예시 입력 | 기대 메시지 |
|------|-----------|-------------|
| 형식 오류 | `2.5 meter`, `feet 8.2` | `Invalid format` — `unit:value` 안내 |
| 숫자 오류 | `meter:abc` | `Invalid number` — 잘못된 값 표시 |
| 미지원 단위 | `meters:2.5`, `cubit:1` | `Unknown unit` — 단위명 표시 |
| 음수 | `meter:-1`, `feet:-1` | 음수 거부 메시지 |

### Output — `convert()` 함수 계약

검증·구현의 단일 진입점. CLI `main()`은 입·출력만 담당한다.

```python
convert(input_str: str) -> dict
# { "status": "pass" | "fail", "lines": list[str], "error": dict | None }
```

| status | lines | error |
|--------|-------|-------|
| `pass` | 변환 결과 문장 (입력 단위 제외) | `None` |
| `fail` | `[]` | `{ "type": str, "message": str }` |

**error.type:** `format` / `number` / `unit` / `negative`

| type | message 예시 |
|------|--------------|
| `format` | `Invalid format. Use unit:value (ex: meter:2.5)` |
| `number` | `Invalid number: abc` |
| `unit` | `Unknown unit: meters` |
| `negative` | `Negative value not allowed: -1` |

#### pass / fail 예시

| input_str | status | lines | error |
|-----------|--------|-------|-------|
| `"meter:2.5"` | pass | `["2.5 meter = 8.2 feet", "2.5 meter = 2.7 yard"]` | `None` |
| `"feet:8.2"` | pass | `["8.2 feet = 2.5 meter", "8.2 feet = 2.7 yard"]` | `None` |
| `"yard:2.7"` | pass | `["2.7 yard = 2.5 meter", "2.7 yard = 8.2 feet"]` | `None` |
| `"2.5 meter"` | fail | `[]` | `{ "type": "format", ... }` |
| `"meter:abc"` | fail | `[]` | `{ "type": "number", ... }` |
| `"meters:2.5"` | fail | `[]` | `{ "type": "unit", ... }` |
| `"feet:-1"` | fail | `[]` | `{ "type": "negative", ... }` |

---

## 4. 기능 요구사항 (FR)

| ID | 요구 | Given | Then | P |
|----|------|-------|------|---|
| FR-01 | `unit:value` 파싱 | `meter:2.5` | `value=2.5`, `unit=meter` | P0 |
| FR-02 | 전 단위 변환 출력 | `meter:2.5` | `feet≈8.2`, `yard≈2.7` (README 반올림); 원값 `feet≈8.2021`, `yard≈2.7340` | P0 |
| FR-03 | 미지원 단위 거부 | `cubit:1`, `meters:2.5` | `status=fail`, `error.type=unit`, 명확한 오류 메시지 | P0 |
| FR-04 | 음수 거부 | `meter:-1`, `feet:-1` | `status=fail`, `error.type=negative` | P0 |
| FR-05 | 잘못된 형식·숫자 거부 | `2.5 meter`, `meter:abc` | `status=fail`, `error.type=format` 또는 `number` | P0 |

---

## 5. 비기능 요구사항 (NFR)

| ID | 요구 | Given | Then | P |
|----|------|-------|------|---|
| NFR-01 | OCP (개방-폐쇄) | 신규 단위 추가 (예: `inch`) | 기존 변환기·meter/feet/yard TC **변경 0건** | P0 |
| NFR-02 | SRP (단일 책임) | 역할 분리 | `Parser` / `Registry` / `Converter` / `Printer` 책임 분리; 검증 수정 시 비율·단위 목록·출력 형식을 함께 건드리지 않아도 FR-03~05 TC 통과 | P0 |
| NFR-03 | 검증 효율 | 6케이스 이상 TC | `convert()` 기준 **5분 이내** 실행 (현재 CLI 수동 25~30분) | P0 |
| NFR-04 | README↔코드 일치 | Q3~Q5 TC | TC 통과 = README 품질 요구와 일치 | P0 |

---

## 6. 확장 요구사항 (EXT)

| ID | 요구 | Given | Then | P |
|----|------|-------|------|---|
| EXT-01 | 설정 외부화 | `units.json` | 파일에서 변환 비율 로드 | P1 |
| EXT-02 | 동적 등록 | `1 cubit = 0.4572 meter` | 등록 즉시 변환 가능 | P1 |
| EXT-03 | 출력 포맷 | `--format` 플래그 | `json` / `csv` / `table` 출력 검증 | P1 |

---

## 7. PRD → 테스트 추적표

개념(PRD)에서 코드(TC)까지 추적 가능하도록 FR·NFR·EXT와 `convert()` TC를 1:1 매핑한다.

| ID | Given (입력) | Then (기대) | TC 대상 |
|----|--------------|-------------|---------|
| FR-01 | `meter:2.5` | 파싱 성공 → pass | `convert("meter:2.5")` status=pass |
| FR-02 | `meter:2.5` | `lines`에 feet·yard 환산 (README 반올림) | `lines` 기대값 assert |
| FR-02 | `feet:8.2`, `yard:2.7` | 3단위 각각 pass, `lines` 정확 | 단위별 pass TC |
| FR-03 | `cubit:1`, `meters:2.5` | fail / unit | `error.type == "unit"` |
| FR-04 | `meter:-1`, `feet:-1` | fail / negative | `error.type == "negative"` |
| FR-05 | `2.5 meter` | fail / format | `error.type == "format"` |
| FR-05 | `meter:abc` | fail / number | `error.type == "number"` |
| NFR-01 | cubit(또는 inch) 추가 후 | meter/feet/yard TC 무변경 | 회귀 TC 0건 변경 |
| NFR-02 | 검증 로직만 수정 | 변환 비율·출력 TC 유지 | FR-02·FR-04~05 독립 통과 |
| NFR-03 | 6+ 케이스 | pytest 5분 이내 | `python -m pytest` |
| NFR-04 | FR-03~05 전체 | README 품질과 일치 | Q3~Q5 TC 일괄 |
| EXT-01 | `units.json` 존재 | 비율 파일 로드 | P1 — 별도 TC |
| EXT-02 | `1 cubit = 0.4572 m` 등록 | `cubit:1` pass | P1 — 별도 TC |
| EXT-03 | `--format json` 등 | 포맷별 출력 | P1 — 별도 TC |

---

## 8. 성공 기준

### 기본 (B)

| # | 기준 | 측정 |
|---|------|------|
| B1 | `단위:값` → 다른 단위 출력 | `convert("meter:2.5")` pass, `lines` README 일치 |
| B2 | meter / feet / yard 3단위 | 각 단위 pass TC 1건 이상 |
| B3 | 확장 시 기존 비침 | 신규 단위 추가 후 기존 로직·TC 변경 0건 |
| B4 | 변환 정확성 TC | 비율·반올림 기대값 명시 |

### 비즈니스 로직 (L)

| # | 기준 | 측정 |
|---|------|------|
| L1 | `3.28084` / `1.09361` 단일 기준 | pass TC 기대값 반영 |
| L2 | feet↔yard meter 경유 | 간접 환산 일관 TC |

### 품질 (Q)

| # | 기준 | 측정 |
|---|------|------|
| Q1 | OCP | B3 동일 |
| Q2 | SRP | 역할별 수정 분리 |
| Q3 | 음수 차단 | `convert("feet:-1")` → fail/negative |
| Q4 | 형식·숫자 식별 | `convert("2.5 meter")` → fail/format; `convert("meter:abc")` → fail/number |
| Q5 | 미지원 단위 거부 | `convert("meters:2.5")` → fail/unit |

### Mom Test (M)

| # | 기준 | 측정 |
|---|------|------|
| M1 | 검증 시간 | 6케이스 이상 **5분 이내** |
| M2 | 재작업 감소 | CLI 재입력·엑셀 눈대조 **0회** |
| M3 | README↔코드 일치 | Q3~Q5 TC 통과 |

---

## 9. 현재 구현 갭

`UnitConverter.py` 기준 (PRD·`convert()` 계약 대비):

| 항목 | 현재 | PRD 기대 |
|------|------|----------|
| 음수 검증 | `feet:-1` 출력됨 | fail / negative |
| pass 출력 줄 수 | 입력 단위 포함 3줄 | 입력 단위 제외 2줄 |
| 검증 단위 | `main()` 내 `print` | `convert()` dict 반환 |
| TC | 미구현·수동 CLI | `convert()` pytest 자동 |
| OCP / SRP | `elif` 단일 파일 | 역할 분리·확장 비침 |
| EXT-01~03 | 미구현 | P1 |

---

## 10. 코드 구조 (목표)

| 모듈 | 책임 |
|------|------|
| `src/convert.py` — `convert()` | 파싱·검증·변환. `print` 금지, dict만 반환 |
| `UnitConverter.py` — `main()` | `input()` / `print()` 입·출력만 |
| `tests/test_convert.py` | `convert()` TC — PRD 추적표 기반 |

---

*PRD 1.0 — Mom Test 03 + 추적표 + README 통합*
