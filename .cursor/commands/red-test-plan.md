# RED Test Plan — C2C 설계표 · 테스트 플랜 (Ask)

**역할:** ARRR **A**단계 (Ask = RED ③) — C2C 설계표·테스트 플랜만 작성. **`tests/`·`src/` 파일 생성·수정 금지.**

추가 입력 없이 **`/red-test-plan` 만으로도 동작**한다. 세션 주제·Test ID는 **채팅 맥락·`docs/PRD.md` §4·§7** 에서 자동 추출한다.

## 필수 선언 (응답 첫 줄)

```
Phase: red | Layer: {entity|boundary} | Track: {Logic|UI}
```

| Track | Layer | 대상 함수 | 테스트 파일 | 구현 |
|-------|-------|-----------|-------------|------|
| **Logic** | entity | `convert()` | `tests/test_convert.py` | `src/convert.py` |
| **UI** | boundary | `main()` | `tests/test_main.py` | `UnitConverter.py` |

> **Track A (boundary) 재사용:** Logic Track(entity)용 출력 4블록을 그대로 쓰되, **Layer만 `boundary`**, Track **UI**, 대상 **`main()`** · 파일 **`tests/test_main.py`** 로 바꾸면 된다. C2C·Track B·플랜·ECB 점검 구조는 동일.

## 자율 실행

- 추가 입력·질문 없이 즉시 수행한다.
- `tests/`, `docs/PRD.md` §4·§7, `.cursorrules` 로 **미커버 FR/NFR 1건**·Track·Layer를 스스로 고른다.
- **Logic 미완료 → Logic 우선.** Logic GREEN 후 UI Track.
- **케이스 1건·Track 1개**만. 양 Track 동시 금지.

## 절차

1. 채팅·PRD에서 세션 주제·미커버 Test ID 1건을 확정한다.
2. 아래 **출력 4블록**을 표 형식으로 작성한다 (파일 변경 없음).
3. 말미에 완료 한 줄을 출력한다.

## 출력 4블록 (표 형식 — 필수)

### 1. C2C (Rule1~3)

| Rule | 내용 |
|------|------|
| **Rule1** | PRD FR/NFR **인용** (ID + Given/Then 한 줄) |
| **Rule2** | 이번 RED **To-Do 1개** (검증할 행위 한 문장) |
| **Rule3** | **Test ID** + **Given / When / Then** |

예시 골격:

| 항목 | 값 |
|------|-----|
| Rule1 (PRD 인용) | FR-03: `meters:2.5` → `status=fail`, `error.type=unit` |
| Rule2 (To-Do) | `convert()` 가 미지원 단위를 unit 오류로 거부함을 검증 |
| Rule3 (Test ID · G/W/T) | **T-FR-03** · Given: `"meters:2.5"` · When: `convert(input_str)` · Then: `status=="fail"`, `error.type=="unit"` |

### 2. Track B 표

| Test ID | 대상 함수 | Given → Then | Invariant | Expected RED Failure |
|---------|-----------|--------------|-----------|----------------------|
| {T-FR-xx} | `convert()` 또는 `main()` | {입력} → {기대} | {변하지 않아야 할 계약·출력 규칙} | {pytest 실패 예상 이유 1줄 — 모듈 없음·assert 미충족 등} |

### 3. 테스트 플랜

| 항목 | 값 |
|------|-----|
| 파일 경로 | `tests/test_convert.py` (Logic) / `tests/test_main.py` (UI) |
| 함수명 (안) | `test_{test_id_snake_case}` |
| conftest 픽스처 | {필요 시 `capsys`, `monkeypatch`, stdin mock 등 — 없으면 `없음`} |
| pytest 명령 | `python -m pytest tests/test_convert.py -v` 또는 `python -m pytest tests/test_main.py -v` |
| RED 묶음 범위 | {이번 Test ID 1건 / 동일 FR 내 후속 skeleton·tdd-red 범위} |

### 4. ECB · Mock 점검

| 항목 | Logic Track (entity) | UI Track (boundary) |
|------|----------------------|---------------------|
| **E**ntity | `convert()` 실객체·실입력 — **Domain Mock 금지** | `main()` 경로; `convert()`는 stub 허용 |
| **C**ontrol | 오케스트레이션은 테스트 대상 — stub 금지 | Boundary는 I/O만 — 변환·검증 로직 주입 금지 |
| **B**oundary | `print`/`input` 테스트 범위 아님 | `capsys`·stdin mock만; Domain Mock 금지 |
| **E001~E005 emit** | **금지** — format/number/unit/negative/error dict를 테스트에서 임의 emit·하드코딩하지 않음 | 동일 |

## 금지

- `src/`·`UnitConverter.py` 수정
- **GREEN / REFACTOR** 단계 수행
- `skip` / `xfail` / assert 완화
- **`tests/`·`src/` 파일 생성·수정** (계획만; 코드는 `/red-skeleton` → `/tdd-red` 에서)
- 한 번에 여러 케이스·양 Track 동시
- 사용자에게 Track·케이스 선택 질문

## 완료 (응답 말미 한 줄)

```
/red-skeleton 으로 넘길 준비됐다
```

## 변경 파일

없음 (본 커맨드는 설계표·플랜 보고만)
