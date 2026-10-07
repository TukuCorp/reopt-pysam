import json
import os
here = os.path.dirname(__file__)
deal = json.load(open(os.path.join(here, "..", "..", "data", "vietnam", "vn_deal_defaults_2026.json"), encoding="utf-8"))
FX = deal["data"]["exchange_rate"]["vnd_per_usd"]
def crf(r, n):
    return r * (1 + r) ** n / ((1 + r) ** n - 1)
out = []
for capex in (650, 700, 800):
    for cf in (0.16, 0.175, 0.19):
        for tenor, wacc in ((20, 0.09), (15, 0.09)):
            fee_kw = 0.02 * capex
            annual = fee_kw * 1000.0 * crf(wacc, tenor)
            mwh = cf * 8760.0
            usd_mwh = annual / mwh
            out.append({"capex": capex, "cf": cf, "tenor": tenor, "usd_per_mwh": round(usd_mwh, 3), "vnd_per_kwh": round(usd_mwh * FX / 1000.0, 2)})
base = [o for o in out if o["capex"] == 700 and o["cf"] == 0.175 and o["tenor"] == 20][0]
band = [o["usd_per_mwh"] for o in out if o["tenor"] == 20]
res = {"fx": FX, "base": base, "band20yr": [min(band), max(band)], "n": len(out)}
json.dump(res, open(os.path.join(here, "econ_v2.json"), "w"), indent=1)
print(json.dumps(res))
LED = os.path.join(here, "2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl")
rows = [json.loads(l) for l in open(LED, encoding="utf-8") if l.strip()]
from collections import Counter
c = Counter((x.get("bucket"), x.get("status")) for x in rows)
print("total", len(rows))
print(sorted([[str(k), v] for k, v in c.items()]))
q = [x for x in rows if (x.get("tier", 9) or 9) <= 3]
print("qualified tier<=3", len(q))
