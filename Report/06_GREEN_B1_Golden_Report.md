# Report — UnitConverter_19 GREEN B1 · Golden Approval (PRD §8 B1~B4)

**프로젝트:** UnitConverter_19  
**일자:** 2026-06-11  
**주제:** PRD §8 기본(B) RED 스켈레톤 → `/green-minimal` B1 → Golden 불일치 수정  
**대상:** `tests/test_convert.py`, `src/convert.py`, `src/constants.py`, `tests/_approval.py`, `tests/golden/T-FR-01.approved.txt`  
**개정:** 06 — 05 RED ARRR(T-FR-01 골격) 대비 **B1 GREEN·Approval Test 확정**

---

## 1. 요약

PRD §8 **기본(B1~B4)** 성공 기준에 맞춰 Logic Track RED 스켈레톤 5건을 `tests/test_convert.py`에 구성했다. `/green-minimal`로 `meter:2.5` 최소 변환을 `src/convert.py`에 구현하고 비율 상수를 `src/constants.py`로 분리했다. Golden Approval Test(`T-FR-01`)에서 **3줄(입력 단위 포함)** 과 **PRD 2줄(입력 단위 제외)** 불일치를 확인·수정했다. `test_b1`에 `B4_EXPECTED` lines assert를 추가하고 golden을 삭제 후 `UPDATE_GOLDEN=1`로 재캡처하여 PRD·golden·구현이 일치하는 상태로 맞췄다.

---

## 2. 배경·목표

| 항목 | 내용 |
|------|------|
| 배경 | 05 보고서에서 T-FR-01 RED 골격만 존재; FR-02·B2~B4·변환 출력 미검증 |
| 목표 | B1(`meter:2.5` pass + README 반올림 lines) GREEN 및 Golden Master 기준 고정 |
| SSOT | `.cursorrules`, `docs/PRD.md` §3·§7·§8, `tests` 내 `B4_EXPECTED` |

---

## 3. 산출물·변경

| 산출물 | 경로 | 설명 |
|--------|------|------|
| B1~B4 RED 스켈레톤 | `tests/test_convert.py` | B1 assert 완료; B2~B4 `pytest.fail` 유지 |
| Approval 헬퍼 | `tests/_approval.py` | int[6] 직렬화·golden 대조 |
| Golden 기준 | `tests/golden/T-FR-01.approved.txt` | PRD 2줄 pass 출력 (재생성) |
| 비율 SSOT | `src/constants.py` | `METER_TO_FEET`, `METER_TO_YARD`, `ROUND_DECIMALS` |
| convert 최소 구현 | `src/convert.py` | `meter` 입력 → feet·yard 2줄 변환 |
| B4 기대값 상수 | `tests/test_convert.py` | `B4_EXPECTED` — 3단위 pass lines 명시 |

---

## 4. 기술 내용

### 4.1 PRD §8 → 테스트 매핑

| 기준 | 테스트 | 상태 |
|------|--------|------|
| B1 `단위:값` → 다른 단위 | `test_b1_unit_value_to_other_units_pass` | **PASS** |
| B2 3단위 각 pass | `test_b2_feet_*`, `test_b2_yard_*` | RED skeleton |
| B3 확장 비침 | `test_b3_extension_preserves_existing_meter_tc` | RED skeleton |
| B4 비율·반올림 | `test_b4_conversion_accuracy_and_rounding` | RED skeleton |

### 4.2 Golden 불일치·해결

| 구분 | 줄 2 | 줄 3 | 줄 4 |
|------|------|------|------|
| 이전 golden (잘못됨) | `2.5 meter = 2.5 meter` | `2.5 meter = 8.2 feet` | `2.5 meter = 2.7 yard` |
| PRD / B4_EXPECTED | `2.5 meter = 8.2 feet` | `2.5 meter = 2.7 yard` | *(빈 줄)* |

**조치:** `convert()` meter 분기에서 입력 단위 자기 줄 제거 → `assert result["lines"] == B4_EXPECTED["meter:2.5"]` 추가 → golden 삭제 → `UPDATE_GOLDEN=1` 재캡처.

### 4.3 int[6] Golden (T-FR-01)

```
pass
2.5 meter = 8.2 feet
2.5 meter = 2.7 yard


```

### 4.4 pytest (B1 기준)

- `test_b1_unit_value_to_other_units_pass`: **PASS**
- 전체 `test_convert.py`: **1 passed, 4 failed** (B2~B4 skeleton)

---

## 5. 결정·갭·다음 단계

| # | 항목 | 내용 |
|---|------|------|
| 1 | 결정 | pass `lines`는 PRD §3 기준 **입력 단위 제외 2줄**; golden·`B4_EXPECTED`·구현 SSOT 통일 |
| 2 | 갭 | `feet`/`yard` 분기·검증(format/number/unit/negative) 미구현; B2~B4 RED skeleton 잔존 |
| 3 | 다음 | `/tdd-red` B2(feet) → `/green-minimal` → B3/B4·FR-03~05 순차 GREEN |

---

*Report 06 — UnitConverter_19*
