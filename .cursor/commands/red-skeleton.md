# RED Skeleton — AAA 골격 · pytest.fail (Arrange)

**역할:** ARRR **A**단계 (Ask = RED ④) — **`/red-test-plan` 설계표 기준** `pytest.fail` 스켈레톤만 작성. **`src/`·`UnitConverter.py` 수정 금지.**

추가 입력 없이 **`/red-skeleton` 만으로도 동작**한다. Test ID·Track·Layer는 **직전 `/red-test-plan` 출력·채팅 맥락·`docs/PRD.md` §4·§7** 에서 자동 추출한다.

> **Skill 참조:** `unit-converter-tdd` Skill이 있으면 자동 따름 (Dual Track · BCE · ARRR · ECB 규칙).

## 필수 선언 (응답 첫 줄)

```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
```

| Track | Layer | 대상 함수 | 테스트 파일 | 구현 |
|-------|-------|-----------|-------------|------|
| **Logic** | entity | `convert()` | `tests/test_convert.py` | `src/convert.py` |
| **UI** | boundary | `main()` | `tests/test_main.py` | `UnitConverter.py` |

> **Track B (boundary) 재사용:** Logic Track(entity)용 절차·템플릿을 그대로 쓰되, **Layer만 `boundary`**, Track **UI**, 대상 **`main()`** · 파일 **`tests/test_main.py`** 로 바꾸면 된다.

## 자율 실행

- 추가 입력·질문 없이 즉시 수행한다.
- **`/red-test-plan` Rule3 Test ID 1건** (없으면 PRD §7 미커버 1건)을 골격으로 작성한다.
- **Logic 미완료 → Logic 우선.** Logic GREEN 후 UI Track.
- **케이스 1건·Track 1개**만. 양 Track 동시 금지.

## 절차

1. 설계표에서 **Test ID · Given / When / Then** 을 확정한다.
2. 해당 테스트 파일에 **AAA 주석 (Given / When / Then)** 골격 1개를 추가한다.
3. **Then** 은 `pytest.fail("RED: {Test ID} — …")` **한 줄만** 둔다 (아래 템플릿).
4. Arrange 데이터(입력·기대 상수)는 **`entity/constants.py` import** — 픽스처·테스트 데이터만; 비율·단위명 등 매직넘버 하드코딩 금지.
5. `tests/conftest.py` 에 **`meter_input`** 픽스처가 없으면 추가한다 (PRD §3 정상 pass 입력 1건).
6. pytest 실행 후 FAIL 을 확인·보고한다.

## AAA 규칙

| 구간 | 주석 | 허용 내용 |
|------|------|-----------|
| **Given** | `# Given — …` | 입력 문자열·상수 import·픽스처(`meter_input` 등) |
| **When** | `# When — …` | `convert(input_str)` 또는 `main()` 호출 1줄 |
| **Then** | `# Then — …` | **`pytest.fail("RED: {Test ID} — …")` 한 줄만** |

### Then 금지

- `assert` 본문 (완전한 검증 → `/tdd-red`)
- `skip` / `xfail` / 통과 더미 (`pass`, 빈 assert, `assert True`)
- E001~E005 error dict·lines 기대값 하드코딩 (emit 금지 — ECB)

## conftest — `meter_input`

| 항목 | 값 |
|------|-----|
| 파일 | `tests/conftest.py` |
| 픽스처명 | `meter_input` |
| 형식 | PRD §3 정상 pass 입력 — **`"meter:2.5"`** (`unit:value`) |
| SSOT | `entity.constants.INPUT_METER_25` (리터럴 중복 금지) |
| 용도 | Logic Track Given — pass TC 골격의 대표 입력 |

```python
import pytest

from entity.constants import INPUT_METER_25


@pytest.fixture
def meter_input():
    return INPUT_METER_25  # "meter:2.5"
```

> UI Track(boundary): pytest 내장 **`capsys`** · stdin **`monkeypatch`** 만. Domain Mock 금지.
## 상수 — `entity/constants.py`

- Arrange·픽스처 **데이터만** import — 테스트 본문에 매직넘버·입력 문자열 리터럴 금지.
- SSOT: **`entity/constants.py`** (프로젝트 루트 또는 `tests/` 하위 `entity/` — **`src/` 수정 금지**).
- import 예: `from entity.constants import INPUT_METER_25`
- 비율·단위명·B4 `lines` 기대값 등 도메인 상수도 동 파일에서만 참조.

## 템플릿 예시 (Logic · entity)

함수명: `test_{test_id_snake_case}` 또는 PRD §8 접두 **`test_b1_{내용}`** (설계표 Test ID와 1:1).

```python
from convert import convert


def test_b1_unit_value_to_other_units_pass(meter_input):
    """B1 / T-FR-01: unit:value → 다른 단위 pass (FR-01)"""
    # Given — meter_input (INPUT_METER_25)
    input_str = meter_input

    # When — convert(input_str)
    result = convert(input_str)

    # Then — RED skeleton (assert는 /tdd-red)
    pytest.fail("RED: T-FR-01 — pass status·lines assert 미구현")
```

### UI Track (boundary) 골격

```python
def test_main_xxx(capsys):
    """{Test ID}: …"""
    # Given — stdin mock (필요 시 convert stub)
    # When — main()
    # Then
    pytest.fail("RED: {Test ID} — CLI 출력 assert 미구현")
```

## pytest

```bash
python -m pytest tests/test_convert.py -v
# UI Track:
python -m pytest tests/test_main.py -v
```

## 보고 형식 (응답 말미)

| 항목 | 내용 |
|------|------|
| Test ID | `{T-FR-xx}` 또는 PRD §8 `{Bx}` |
| pytest | **FAIL** — `{한 줄 이유}` (예: `pytest.fail` 의도적 RED) |
| 변경 파일 | `tests/` 만 (예: `tests/test_convert.py`, `tests/conftest.py`, `tests/entity/constants.py`) |

## 금지

- `src/`·`UnitConverter.py` 수정
- **GREEN / REFACTOR** 단계 수행
- Then 에 `assert` 본문·`skip`·`xfail`·통과 더미
- 설계표와 무관한 Test ID·Track 임의 선택
- 한 번에 여러 케이스·양 Track 동시
- 사용자에게 Track·케이스 선택 질문

## 완료 (응답 말미 한 줄)

```
/tdd-red 으로 넘길 준비됐다
```

## 다음 단계

| 커맨드 | 역할 |
|--------|------|
| `/red-test-plan` | RED ③ — C2C 설계표 (파일 변경 없음) |
| **`/red-skeleton`** | **RED ④ — pytest.fail 골격 (`tests/`만)** |
| `/tdd-red` | RED — 완전한 assert, 여전히 FAIL 목표 |
