# Report — UnitConverter_19 GREEN FR-03~05 · Golden Approval (Logic Track 완료)

**프로젝트:** UnitConverter_19  
**일자:** 2026-06-11  
**주제:** PRD §7 FR-03~FR-05 RED→GREEN→Golden — 입력 검증·Approval Test 9건 확정  
**대상:** `tests/test_convert.py`, `src/convert.py`, `tests/golden/`, `README.md`  
**개정:** 08 — 07 B2 pass Golden 대비 **fail 검증 GREEN·전 TC Golden·테스트명 통일**

---

## 1. 요약

07 보고서 이후 Logic Track에서 FR-03(미지원 단위)·FR-04(음수)·FR-05(형식·숫자)를 RED→GREEN 순으로 완료했다. `test_fr_*` 명명으로 pass/fail TC를 PRD FR ID와 1:1 정렬했고, yard pass golden을 `T-FR-02-YARD`로 분리해 FR-03 fail용 `T-FR-03`과 충돌을 해소했다. `/golden-master`로 pass 3 + fail 6건 int[6] Approval을 `UPDATE_GOLDEN=1` 생성 후 matched PASS 확인. `test_convert.py` **9 passed, 0 failed**.

---

## 2. 배경·목표

| 항목 | 내용 |
|------|------|
| 배경 | 07에서 FR-01·FR-02 pass만 GREEN; FR-03~05 fail TC·검증 로직 미구현 |
| 목표 | PRD §7 추적표 FR-03~05 완료 + §8 Q3~Q5 + Golden Approval 전 TC 고정 |
| SSOT | `.cursorrules`, `docs/PRD.md` §3·§7·§8, `src/constants.py` |

---

## 3. 산출물·변경

| 산출물 | 경로 | 설명 |
|--------|------|------|
| FR-03~05 RED TC | `tests/test_convert.py` | fail assert 6건 (`test_fr_03_*` ~ `test_fr_05_*`) |
| 검증·변환 | `src/convert.py` | format/number/unit/negative 검증 + 3단위 변환 |
| 테스트명 통일 | `tests/test_convert.py` | `test_b*` → `test_fr_*` (FR ID 1:1) |
| yard golden rename | `tests/golden/T-FR-02-YARD.approved.txt` | 기존 `T-FR-03` yard pass 분리 |
| fail golden 6건 | `tests/golden/T-FR-03*.txt`, `T-FR-04*.txt`, `T-FR-05*.txt` | E001~E004 int[6] |
| 진행 현황 | `README.md` | §2 Logic Track FR-01~05·Golden 체크 완료 |

---

## 4. 기술 내용

### 4.1 검증 순서 (`convert()`)

1. `:` 누락 → `fail` / `format` (E001)
2. `float()` 실패 → `fail` / `number` (E002)
3. 지원 단위 + 음수 → `fail` / `negative` (E004)
4. 미지원 단위 → `fail` / `unit` (E003)
5. meter/feet/yard → pass `lines` 2줄

### 4.2 Golden Test ID 매핑

| Test ID | 입력 | status |
|---------|------|--------|
| T-FR-01 | `meter:2.5` | pass |
| T-FR-02 | `feet:8.2` | pass |
| T-FR-02-YARD | `yard:2.7` | pass |
| T-FR-03 | `meters:2.5` | fail / E003 |
| T-FR-03-CUBIT | `cubit:1` | fail / E003 |
| T-FR-04 | `meter:-1` | fail / E004 |
| T-FR-04-FEET | `feet:-1` | fail / E004 |
| T-FR-05-FORMAT | `2.5 meter` | fail / E001 |
| T-FR-05-NUMBER | `meter:abc` | fail / E002 |

### 4.3 pytest

```
python -m pytest tests/test_convert.py -v
→ 9 passed, 0 failed (matched, UPDATE_GOLDEN 없음)
```

---

## 5. 결정·갭·다음 단계

| # | 항목 | 내용 |
|---|------|------|
| 1 | 결정 | 테스트명 `test_fr_XX_*`; yard golden `T-FR-02-YARD`로 FR-03 fail ID 확보 |
| 2 | 갭 | UI Track(`main()`) 미착수; NFR OCP/SRP 리팩터 미진행; EXT P1 미착수 |
| 3 | 다음 | UI Track RED→GREEN; `/refactor-smell` Logic Track; `UnitConverter.py` Boundary 연동 |

---

*Report 08 — UnitConverter_19*
