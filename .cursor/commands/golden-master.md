# Golden Master — Approval Test 구축·검증

**역할:** GREEN PASS 후 대상 Test ID의 `convert()` 출력을 Golden Master(Approval Test)로 고정·대조한다.

## 필수 선언 (응답 첫 줄)

```
Phase: green | Layer: entity | Track: Logic
```

## 전제

- 대상 **Test ID** pytest **PASS** (`/green-minimal` 완료).
- 채팅·PRD §7·`tests/test_convert.py`에서 **Test ID 1건**을 자동 확정한다.

## 자율 실행

- 추가 입력·질문 없이 즉시 수행한다.
- Test ID 1건·golden 1세트만 다룬다 (Logic Track entity).

## 절차

1. **`tests/_approval.py`** — `assert_matches_golden(actual: str, golden_path: Path) -> None` 확인. **없으면 생성**한다.
   - `actual`: `convert()` 결과를 **int[6] 1-index** 고정 포맷으로 직렬화한 문자열.
   - `UPDATE_GOLDEN=1` 이면 golden 파일을 **덮어쓰기** 후 return.
   - 그 외: golden과 **전체 문자열 일치** 비교; 불일치 시 diff 요약과 함께 `AssertionError`.
2. **`tests/golden/{id}.approved.txt`** — Test ID와 1:1 연결 (예: `T-FR-01` → `tests/golden/T-FR-01.approved.txt`).
   - 해당 테스트에서 `assert_matches_golden(...)` 호출로 golden 경로를 연결한다.
3. **기준 파일 생성** — `UPDATE_GOLDEN=1` 로 pytest 실행:

   ```bash
   # bash
   UPDATE_GOLDEN=1 python -m pytest tests/test_convert.py::{test_function} -v

   # PowerShell
   $env:UPDATE_GOLDEN=1; python -m pytest tests/test_convert.py::{test_function} -v
   ```

4. **matched 확인** — `UPDATE_GOLDEN` **없이** 동일 pytest 재실행 → PASS(matched) 확인.

## Golden 포맷 — int[6] 1-index (고정)

`convert()` dict → **정확히 6줄**, 줄 번호 **1-index**. 빈 필드는 빈 줄.

| 줄 | 필드 | pass | fail |
|----|------|------|------|
| **1** | `status` | `pass` | `fail` |
| **2** | `lines[0]` | 변환 문장 1 | *(빈 줄)* |
| **3** | `lines[1]` | 변환 문장 2 | *(빈 줄)* |
| **4** | `lines[2]` | 변환 문장 3 | *(빈 줄)* |
| **5** | 에러 코드 | *(빈 줄)* | `E00n` (아래 표) |
| **6** | `error.message` | *(빈 줄)* | PRD §3 message |

**에러 코드 문자열 (줄 5 — 고정, 임의 변경 금지):**

| error.type | 줄 5 |
|------------|------|
| `format` | `E001` |
| `number` | `E002` |
| `unit` | `E003` |
| `negative` | `E004` |
| *(기타)* | `E005` |

- 줄 2~4 pass: `.cursorrules` · PRD §3 `lines` 형식 (`"{value} {unit} = {converted} {target_unit}"`).
- fail: `lines=[]` → 줄 2~4 모두 빈 줄.

## SSOT

- 출력·에러: `.cursorrules`, `docs/PRD.md` §3
- Test ID: `docs/PRD.md` §7

## 보고 형식

| 항목 | 값 |
|------|-----|
| Test ID | {T-FR-xx} |
| golden 경로 | `tests/golden/{id}.approved.txt` |
| matched | `yes` / `no` |
| diff 요약 | 불일치 시 줄 번호·기대/실제 1~2줄; 일치 시 `—` |

- pytest 결과: N passed, M failed
- 변경 파일: `tests/_approval.py`, `tests/golden/{id}.approved.txt`, `tests/test_convert.py` (golden 연결)

## 금지

- **golden 수동 편집**으로 pytest 통과 우회 (기준은 `UPDATE_GOLDEN=1` + 구현 출력만).
- int[6] 줄 수·순서·E001~E005 코드 변경.
- `src/`·`UnitConverter.py` 수정 (GREEN 완료 상태 유지).
- assert 완화 / skip / xfail.
- Test ID·golden 다중·UI Track 동시.
- 사용자에게 Test ID 선택 질문
