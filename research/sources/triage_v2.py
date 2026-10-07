import json, os, re
LEDGER = os.path.join(os.path.dirname(__file__), "2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl")
rows = [json.loads(l) for l in open(LEDGER, encoding="utf-8") if l.strip()]
print("in:", len(rows))
REL = re.compile(r"ppa|photovoltaic|solar|wind|renewable|energy|electricity|tariff|intermediation|broker|auction|corporate procur|project financ|development fee|power purchase|green power|offtake|open access|wheeling|certificate|LGC|REC", re.I)
kept = 0
for r in rows:
    t = (r.get("title", "") or "")
    if REL.search(t):
        kept += 1
        if r.get("tier", 3) == 3:
            r["tier"] = 3
        r["status"] = "candidate"
    else:
        r["tier"] = 5
        r["status"] = "rejected"
        r["note"] = "off-topic wide-pass row; retained for audit trail"
print("relevant academia kept:", kept)
json.dump({"relevant": kept}, open(os.path.join(os.path.dirname(__file__), "triage_v2_counts.json"), "w"))
with open(LEDGER, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("wrote", LEDGER)
