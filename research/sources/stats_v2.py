import json
import os
here = os.path.dirname(__file__)
LED = os.path.join(here, "2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl")
rows = [json.loads(l) for l in open(LED, encoding="utf-8") if l.strip()]
from collections import Counter
c = Counter()
for r in rows:
    b = r.get("bucket")
    q = 1 if ((r.get("tier", 9) or 9) <= 3 and r.get("status") in ("candidate", "verified")) else 0
    c[(b, r.get("status"))] += 1
    c[(b, "qual")] += q
for k in sorted(c, key=str):
    print(str(k), c[k])
print("total", len(rows))
