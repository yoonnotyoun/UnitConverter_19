# Report — UnitConverter_19 RED ARRR 실습 (T-FR-01)

**프로젝트:** UnitConverter_19  
**일자:** 2026-06-11  
**주제:** ARRR Arrange — `/red-test-plan` · `/red-skeleton` (Logic Track, T-FR-01)  
**대상:** `tests/test_convert.py`, `src/convert.py` (참조만)  
**개정:** 05 — 04 TDD·ARRR Cursor 체계 대비 **첫 Logic RED 실습** (FR-01 pass 상태)

---

## 1. 요약

Logic Track RED 단계를 시작했다. `/red-test-plan`으로 **T-FR-01** (FR-01: `meter:2.5` → `status=pass`, `error=None`) C2C·Track B·ECB 설계표를 작성했고, `/red-skeleton`으로 `test_fr_01_meter_2_5_returns_pass` AAA 골격을 `tests/test_convert.py`에 추가했다. Assert는 `pytest.fail("RED skeleton")`로 의도적 FAIL 확인. `src/convert.py`는 ellipsis stub 그대로 — GREEN·구현 변경 없음.

---

## 2. 배경·목표

| 항목 | 내용 |
|------|------|
| 배경 | 04 보고서에서 Cursor ARRR 커맨드·Dual Track 체계 확정; 실제 pytest RED 미착수 |
| 목표 | FR-01부터 Logic Track RED→GREEN 순서로 `convert()` 계약 검증 시작 |
| SSOT | `.cursorrules`, `docs/PRD.md` §4 FR-01, §7 추적표 |

---

## 3. 산출물·변경

| 산출물 | 경로 | 설명 |
|--------|------|------|
| RED Test Plan (대화) | — | T-FR-01 C2C·Track B·테스트 플랜·ECB (파일 미생성) |
| RED Skeleton TC | `tests/test_convert.py` | `test_fr_01_meter_2_5_returns_pass` AAA 골격 |
| convert stub | `src/convert.py` | `...` ellipsis — **변경 없음** |

---

## 4. 기술 내용

### 4.1 C2C (T-FR-01)

| Rule | 내용 |
|------|------|
| Rule1 | **FR-01** · Given: `meter:2.5` · Then: 파싱 성공 → `status=pass` |
| Rule2 | `convert()`가 유효 입력에 `status="pass"`, `error=None` 반환 검증 |
| Rule3 | Given `"meter:2.5"` · When `convert(input_str)` · Then pass·error None |

### 4.2 Track · BCE

| 항목 | 값 |
|------|-----|
| Track | Logic |
| BCE | Control (`convert()` 오케스트레이션) |
| Layer (red-test-plan) | entity |
| ECB | Domain Mock 금지; E001~E005 emit 금지 |

### 4.3 pytest RED

```bash
python -m pytest tests/test_convert.py -v
# FAILED — pytest.fail("RED skeleton")
```

### 4.4 RED 범위 한정

- FR-01: `status`·`error`만 assert 예정 (`/tdd-red`)
- FR-02 `lines` 상세 assert는 **T-FR-02** 후속

---

## 5. 결정·갭·다음 단계

| # | 항목 | 내용 |
|---|------|------|
| 1 | 결정 | Logic Track 우선; 케이스 1건(T-FR-01)씩 RED 진행 |
| 2 | 갭 | `convert()` 미구현; skeleton assert 미완 |
| 3 | 다음 | `/tdd-red` → Assert 완성 → `/green-minimal` |

---

*Report 05 — UnitConverter_19*
