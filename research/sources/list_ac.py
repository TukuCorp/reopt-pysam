import json
import os
here = os.path.dirname(__file__)
LED = os.path.join(here, "2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl")
rows = [json.loads(l) for l in open(LED, encoding="utf-8") if l.strip()]
ac = [r for r in rows if r.get("bucket") == "academia" and r.get("status") == "candidate"]
def cit(r):
    s = r.get("signal") or {}
    return s.get("citations", 0) or 0
ac.sort(key=cit, reverse=True)
for r in ac[:60]:
    s = r.get("signal") or {}
    print(r.get("id"), "|", s.get("year"), "|", cit(r), "|", (r.get("title", "") or "")[:90], "|", r.get("url"))
