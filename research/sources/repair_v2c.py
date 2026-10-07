import json
import os
import re
here = os.path.dirname(__file__)
LEDGER = os.path.join(here, "2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl")
rows = [json.loads(l) for l in open(LEDGER, encoding="utf-8") if l.strip()]
REL = re.compile(r"ppa|photovoltaic|solar|wind|renewable|energy|electricity|tariff|intermediation|broker|auction|corporate procur|project financ|development fee|power purchase|green power|offtake|open access|wheeling|certificate|LGC|REC", re.I)
for r in rows:
    if r.get("bucket") in ("academia", "github"):
        rid = r.get("id", "") or ""
        parts = rid.split("-")
        if len(parts) == 2 and len(parts[1]) == 3 and parts[1].isdigit():
            t = r.get("title", "") or ""
            if r.get("bucket") == "academia" and REL.search(t):
                r["tier"] = 3
                r["status"] = "candidate"
            else:
                r["tier"] = 5
                r["status"] = "rejected"
            r["pass"] = "wide"
with open(LEDGER, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + chr(10))
from collections import Counter
c = Counter((x.get("bucket"), x.get("status")) for x in rows)
print(sorted([[str(k), v] for k, v in c.items()]))
q = [x for x in rows if (x.get("tier", 9) or 9) <= 3]
print("qualified", len(q), "total", len(rows))
