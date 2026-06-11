# ARRR 실습 Checklist — UnitConverter_19 (Dual Track · BCE)

**일자:** YYYY-MM-DD  
**Track:** logic □ / ui □  
**BCE:** Entity □ / Control □ / Boundary □  
**케이스:** {FR/NFR ID} — `{input_str}`

---

## Logic Track (Entity · Control)

### Arrange
- [ ] `/red-test-plan` — Track: logic, BCE·기대값 확정
- [ ] `/red-skeleton` — `tests/test_convert.py` (선택)

### Red · Green · Refactor
- [ ] `/tdd-red` — Logic 실패 TC 1건
- [ ] `/green-minimal` — `src/convert.py` 최소 구현
- [ ] `/golden-master` — Boundary↔Control 갭 (필요 시)
- [ ] `/refactor-smell` → `/refactor-safe` — BCE 경계 유지

---

## UI Track (Boundary)

### Arrange
- [ ] `/red-test-plan` — Track: ui, `main()` 입·출력 케이스
- [ ] `/red-skeleton` — `tests/test_main.py` (선택)

### Red · Green · Refactor
- [ ] `/tdd-red` — UI 실패 TC 1건
- [ ] `/green-minimal` — `UnitConverter.py` `main()` 만
- [ ] `/refactor-smell` → `/refactor-safe` — Boundary에 로직 없음 확인

---

## Report
- [ ] `/export`

---

## 케이스 기록

| 항목 | 값 |
|------|-----|
| Track / BCE | |
| Target | convert / main |
| 테스트 파일 | |
| 테스트 함수명 | |
| Phase | red □ green □ refactor □ |

---

## 금지 확인

- [ ] RED: 해당 Track 구현 미수정
- [ ] GREEN: `tests/` 미수정
- [ ] BCE: Boundary↔Control 역할 침범 없음
- [ ] 한 Track·한 케이스씩

---

*UnitConverter_19 Dual Track · BCE Checklist*
