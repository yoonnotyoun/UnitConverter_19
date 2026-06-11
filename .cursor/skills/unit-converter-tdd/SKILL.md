---
name: unit-converter-tdd
description: UnitConverter_19 Dual Track TDD (Logic/UI) + BCE. .cursorrules·docs/PRD.md SSOT. RED→GREEN→REFACTOR, Entity/Control/Boundary. TDD·convert·main·pytest·ARRR 실습 시 사용.
---

# UnitConverter TDD — Dual Track · BCE

SSOT: `.cursorrules`, `docs/PRD.md`.

## Dual Track TDD

| Track | BCE | 역할 | 테스트 | 구현 |
|-------|-----|------|--------|------|
| **logic** | **Entity** | 단위·비율·순수 변환 규칙 | `tests/test_convert.py` | `src/` (entity) |
| **logic** | **Control** | `convert()` — 파싱·검증·변환·dict 반환 | `tests/test_convert.py` | `src/convert.py` |
| **ui** | **Boundary** | `main()` — `input`/`print`, `convert()` 호출만 | `tests/test_main.py` | `UnitConverter.py` |

- **Logic Track** = Entity + Control (비즈니스·애플리케이션)
- **UI Track** = Boundary (표현·입출력)
- **순서:** Logic RED→GREEN→REFACTOR 후 UI Track. Track 간 RED 동시 금지.

## BCE 규칙

| BCE | 할 일 | 하지 말 것 |
|-----|-------|------------|
| Entity | meter/feet/yard, 비율 3.28084·1.09361 | input/print |
| Control | `convert(input_str)->dict`, 검증·오케스트레이션 | print, CLI |
| Boundary | input, convert() 호출, lines/error print | 파싱·변환·검증 로직 |

## ARRR · 커맨드

| 단계 | 커맨드 | Track |
|------|--------|-------|
| Arrange | `/red-test-plan` | logic \| ui |
| Arrange | `/red-skeleton` | logic \| ui |
| Red | `/tdd-red` | logic \| ui |
| Green | `/green-minimal` | logic \| ui |
| Green | `/golden-master` | Logic (Layer: entity) — Approval Test |
| Refactor | `/refactor-smell` | logic \| ui |
| Refactor | `/refactor-safe` | logic \| ui |
| Report | `/export` | — |

## Phase 선언 (응답 첫 줄)

```
Phase: red | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}
Phase: green | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}
Phase: green | Layer: entity | Track: Logic          # /golden-master 전용
Phase: refactor | Target: {convert|main} | Track: {logic|ui} | BCE: {Entity|Control|Boundary}
```

`[RED]` / `[GREEN]` / `[REFACTOR]` 접두어 병행.

## Golden Master (Approval Test)

`/green-minimal` 로 대상 Test ID **PASS** 후 `/golden-master` 실행. Logic Track · Layer **entity** · Test ID 1건.

| 항목 | 내용 |
|------|------|
| 헬퍼 | `tests/_approval.py` — `assert_matches_golden` (없으면 생성) |
| golden | `tests/golden/{id}.approved.txt` (Test ID 1:1) |
| 기준 생성 | `UPDATE_GOLDEN=1 python -m pytest tests/test_convert.py::{test} -v` |
| matched | `UPDATE_GOLDEN` 없이 동일 pytest → PASS |

**int[6] 1-index** (고정 직렬화 — 줄 1~6):

| 줄 | pass | fail |
|----|------|------|
| 1 | `status` | `status` |
| 2~4 | `lines[0..2]` | 빈 줄 |
| 5 | 빈 줄 | `E001` format · `E002` number · `E003` unit · `E004` negative · `E005` 기타 |
| 6 | 빈 줄 | `error.message` (PRD §3) |

- golden **수동 편집**으로 통과 우회 금지 — 기준은 `UPDATE_GOLDEN=1` + 구현 출력만.
- 변경: `tests/_approval.py`, `tests/golden/`, `tests/test_convert.py` (golden 연결). `src/`·`UnitConverter.py` **금지**.

## Control 계약 (`.cursorrules`)

```python
convert(input_str: str) -> dict
# pass: lines 3줄, error=None | fail: lines=[], error{type, message}
# error: format | negative | unit
```

## TC 우선순위 (Logic Track — PRD §7)

FR-01→FR-05→Q3~Q5 on `test_convert.py`. UI Track: Boundary가 Control 결과를 올바르게 print.

## AAA — Logic (Control)

```python
def test_convert_xxx():
    # Arrange — input_str
    # Act — result = convert(input_str)
    # Assert — status, lines, error
```

## AAA — UI (Boundary)

```python
def test_main_xxx(capsys):
    # Arrange — stdin mock, convert stub if needed
    # Act — main()
    # Assert — capsys stdout / exit, convert 호출 여부
```

## 단계별 금지

| Track | RED 금지 | GREEN (`/green-minimal`) | GREEN (`/golden-master`) |
|-------|----------|--------------------------|---------------------------|
| logic | `src/` 수정 | `tests/` 수정 | `src/` 수정 — `tests/` Approval Test만 |
| ui | `UnitConverter.py` 수정 | `tests/` 수정 | *(Logic 전용 — UI 미적용)* |

Boundary에 Control 로직 금지. Control에 print 금지.

## pytest

```bash
pytest tests/test_convert.py tests/test_main.py -v
python -m pytest
```

## 자율 실행

커맨드 호출 시 Track·BCE·케이스를 **추가 질문 없이** 정한다. Logic 미완료 → Logic 우선.

## SSOT 충돌

1. 구현·TC → `.cursorrules`
2. FR/NFR → `docs/PRD.md`
3. 레거시 → `UnitConverter.py` (PRD §9 갭)
