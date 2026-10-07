import json
import os
LEDGER = os.path.join(os.path.dirname(__file__), "2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl")
rows = [json.loads(l) for l in open(LEDGER, encoding="utf-8") if l.strip()]
seen = set((r.get("url", "") or "").strip().lower() for r in rows)
print("before", len(rows))
ADD2 = []
ADD2.append(("https://www.businesswire.com/news/home/20250128461760/en/LevelTen-Energys-2024-Year-in-Review-European-Solar-PPA-Prices-Rise-Amid-Shifting-Market-Dynamics", "LevelTen 2024 review European solar PPA dynamics", "industry", 3, "candidate", "EU PPA price context"))
ADD2.append(("https://utilitydive.com/news/levelten-p25-solar-ppa-prices-ercot-pjm/808488/", "LevelTen P25 Q3 2025 solar above 50 USD MWh Texas wind below 35", "industry", 3, "candidate", "US PPA price context"))
ADD2.append(("https://pv-magazine-usa.com/2025/09/30/rfp-alert-engie-north-america-seeks-community-solar-in-illinois/", "Engie North America community solar RFP seller success fee report", "industry", 3, "candidate", "seller fee 0.10 USD MWh report thin corroboration"))
ADD2.append(("https://www.zeigo.com/zeigo-network/2025-q3-us-commercial/", "Zeigo Network US commercial PPA price snapshot Q3 2025", "web", 4, "candidate", "platform price context"))
ADD2.append(("https://perspectives.se.com/global/press-release/schneider-electric-acquires-zeigo-to-transform-corporate-renewable-energy-services/", "Schneider Electric acquires Zeigo background", "web", 4, "candidate", "Schneider advisory scope context"))
ADD2.append(("https://edisonenergy.com/modernizing-higher-education-energy-procurement-a-multi-sourcing-rfp-strategy/", "Edison Energy multi-sourcing RFP strategy", "web", 4, "candidate", "buyer advisor scope"))
ADD2.append(("https://www.solarpowerportal.co.uk/pexapark-and-drax-unite-to-unlock-more-ppa-deals-for-the-uk-market/", "Pexapark Drax UK partnership ticket sizes", "industry", 3, "candidate", "UK ticket 150-200 GWh context"))
ADD2.append(("https://www.pv-magazine.com/2024/02/27/european-ppa-prices-continue-to-rise/", "European PPA prices continued to rise 2024", "industry", 3, "candidate", "EU price context"))
ADD2.append(("https://www.mibgas.es/en/ppa-potential-spain-prospects-and-best-practices-from-the-longest-running-ppa-markets-in-europe/", "MIBGAS Spain PPA longest running market practice", "industry", 3, "candidate", "Spain depth context"))
ADD2.append(("https://businessrenewables.org.au/state-of-the-market-2023/", "BRC-A State of Market 2023 165 PPAs 7.4 GW", "industry", 2, "candidate", "AU scale context"))
ADD2.append(("https://www.pv-magazine.com/2019/02/26/arena-backs-new-online-marketplace-for-corporate-ppas/", "ARENA backs corporate PPA marketplace", "industry", 3, "candidate", "AU facilitation precedent"))
ADD2.append(("https://www.pv-magazine.com/2025/08/15/corporate-ppas-in-asia-pacific-australia-india-and-taiwan-lead-with-89-share/", "WoodMac APAC corporate PPA volume 89pct AU IN TW", "industry", 2, "candidate", "APAC volume context"))
ADD2.append(("https://www.pv-magazine.com/2023/02/09/goldman-sachs-signs-solar-ppa-in-japan/", "Goldman Sachs solar PPA Japan precedent", "web", 3, "candidate", "JP deal precedent"))
ADD2.append(("https://www.pv-magazine.com/2025/02/06/solar-ppa-in-japan-a-beginners-guide/", "Solar PPA Japan explainer structures", "web", 3, "candidate", "JP structure context"))
ADD2.append(("https://www.pv-magazine.com/2025/10/02/south-korea-registers-major-third-party-ppa-milestone/", "Korea third-party PPA milestone cross-KEPCO zone", "web", 3, "candidate", "KR milestone"))
ADD2.append(("https://www.taipeitimes.com/News/biz/archives/2025/02/26/2003832332", "Taiwan offshore wind corporate offtake pipeline", "web", 3, "candidate", "TW pipeline"))
ADD2.append(("https://www.pv-magazine.com/2025/09/30/india-concludes-solar-plus-storage-auction-with-lowest-tariff-of-inr3-20-kwh/", "India solar plus storage 3.20 INR kWh", "industry", 3, "candidate", "IN price context"))
ADD2.append(("https://bridgetoindia.com/indias-green-energy-open-access-rules-2025-a-reality-check-for-c-and-i-consumers/", "Bridge to India open access charges friction", "industry", 3, "candidate", "IN charges friction"))
ADD2.append(("https://firmex.com/resources/blog/ma-advisory-fees/", "Firmex M and A advisory fee benchmarks", "industry", 3, "candidate", "MA fee band"))
ADD2.append(("https://www.renewableenergyworld.com/solar/are-solar-developer-fees-declining/", "Solar developer fees declining economics", "industry", 3, "candidate", "dev fee context"))
ADD2.append(("https://news.samsung.com/global/samsung-electronics-vietnam-becomes-first-company-in-vietnam-to-purchase-renewable-electricity-through-dppa", "Samsung Vietnam first DPPA purchase SEVT", "web", 3, "candidate", "VN first buyer fact"))
ADD2.append(("https://www.pv-magazine.com/2025/07/24/vietnams-first-dppa-enters-commercial-operation/", "Vietnam first DPPA commercial operation Duc Hue 2", "web", 3, "candidate", "VN first operation fact"))
ADD2.append(("https://ven.congthuong.vn/vietnam-completes-first-dppa-transaction-57570.html", "MOIT press Vietnam completes first DPPA transaction", "industry", 2, "candidate", "VN official confirmation"))
ADD2.append(("https://www.nortonrosefulbright.com/en/knowledge/publications/b7fae014/decree-57-2025-key-features-and-impact-on-direct-power-purchase-agreements-in-vietnam", "Norton Rose Decree 57 key features impact", "industry", 3, "candidate", "DPPA rules"))
ADD2.append(("https://www.irena.org/Publications/2025/Jul/Renewable-Power-Generation-Costs-in-2024", "IRENA Renewable Power Generation Costs 2024 flagship", "industry", 1, "candidate", "global cost anchor"))
c = 0
for a in ADD2:
    key = (a[0] or "").strip().lower()
    if key in seen:
        continue
    seen.add(key)
    c += 1
    bid = ("in-" if a[2] == "industry" else "wb-") + "c" + str(c).zfill(3)
    rows.append({"id": bid, "bucket": a[2], "url": a[0], "title": a[1], "tier": a[3], "status": a[4], "pass": "deep", "note": a[5]})
with open(LEDGER, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + chr(10))
print("added", c, "total", len(rows))
