import json
import os
import re
here = os.path.dirname(__file__)
LEDGER = os.path.join(here, "2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl")
rows = [json.loads(l) for l in open(LEDGER, encoding="utf-8") if l.strip()]
REL = re.compile(r"ppa|photovoltaic|solar|wind|renewable|energy|electricity|tariff|intermediation|broker|auction|corporate procur|project financ|development fee|power purchase|green power|offtake|open access|wheeling|certificate|LGC|REC", re.I)
n_ac_rel = 0
for r in rows:
    b = r.get("bucket")
    if b == "academia":
        t = r.get("title", "") or ""
        if REL.search(t):
            r["tier"] = 3
            r["status"] = "candidate"
            n_ac_rel += 1
        else:
            r["tier"] = 5
            r["status"] = "rejected"
VT20 = {"in-001": 3, "in-002": 2, "in-003": 3, "in-004": 3, "in-005": 2, "in-006": 3, "in-007": 2, "in-008": 4, "in-009": 2, "in-010": 4, "in-011": 2, "in-012": 1, "in-013": 3, "in-014": 3, "in-015": 3, "in-016": 2, "in-017": 1, "in-018": 2, "in-019": 2, "in-020": 2}
for r in rows:
    rid = r.get("id", "")
    if rid in VT20:
        r["tier"] = VT20[rid]
        r["status"] = "verified"
        r["pass"] = "deep"
W4 = ["wb-001", "wb-002", "wb-003", "wb-004"]
WT = {"wb-001": 3, "wb-002": 3, "wb-003": 4, "wb-004": 3}
for r in rows:
    rid = r.get("id", "")
    if rid in W4:
        r["tier"] = WT[rid]
        r["status"] = "verified"
        r["pass"] = "deep"
for r in rows:
    rid = r.get("id", "") or ""
    if len(rid) > 3 and rid[3] == "c":
        r["status"] = "candidate"
        r["pass"] = "deep"
        if (r.get("tier", 9) or 9) > 4:
            r["tier"] = 3
with open(LEDGER, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + chr(10))
from collections import Counter
c = Counter((x.get("bucket"), x.get("status")) for x in rows)
print("academia relevant", n_ac_rel)
print("total", len(rows))
print(sorted([[str(k), v] for k, v in c.items()]))
q = [x for x in rows if (x.get("tier", 9) or 9) <= 3]
print("qualified", len(q))
