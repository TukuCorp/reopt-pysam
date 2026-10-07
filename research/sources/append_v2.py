import json, os
LEDGER = os.path.join(os.path.dirname(__file__), '2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl')
rows = [json.loads(l) for l in open(LEDGER, encoding='utf-8') if l.strip()]
seen = set(json.dumps(r.get('url','')).lower() for r in rows)
print('before', len(rows))
ADD=[
("https://www.pv-magazine.com/2025/02/26/levelten-launches-new-platform-to-buy-sell-renewable-assets/","LevelTen launches asset marketplace: sellers subscribe, buyers free, sellers pay fees","industry",3,"verified","Seller-pays marketplace model [V]"),
("https://www.woodmac.com/ja/press-releases/us-commercial-solar-project-acquisitions-see-dramatic-price-variation-over-2018-2021/","WoodMac: US commercial solar acquisitions price variation; developer fees 0.20-0.60 USD/W","industry",2,"verified","Developer fee 0.20-0.60/W margins 18-31pct [V]"),
("https://www.reccessary.com/en/insight/vietnam-dppa-two-part-electricity-tariff-mechanism","Reccessary: Vietnam DPPA two-part tariff mechanism; Decree 57 Art 16 formula","industry",3,"verified","DPPA charge formula CKH [V]"),
("https://waveup.com/blog/m-and-a-advisor-fees/","WaveUp: M&A advisor fees; success 2-8pct EV, Lehman 5/4/3/2/1, minimums 50-250k","industry",3,"verified","M&A success scale [V]"),
("https://www.pv-magazine.com/2026/06/03/vietnams-first-direct-power-purchase-agreement-enters-operation/","Vietnam first DPPA enters operation: Samsung SEVT buyer, TTC Duc Hue 2 49MW seller, ~70GWh/yr","web",3,"verified","First DPPA facts [V]"),
("https://www.pv-magazine.com/2025/07/23/global-average-solar-lcoe-stood-at-0-043-kwh-in-2024-says-irena/","IRENA via pv-magazine: global solar LCOE 0.043 USD/kWh, TIC 691 USD/kW; India 525 China 591 USA 1058 Europe 779","industry",2,"verified","LCOE and capex anchors [V]"),
("https://en.vietstock.vn/2025/05/electricity-prices-increase-by-48-per-cent-amid-soaring-generation-costs-970-611750.htm","Vietstock: EVN avg retail tariff 2204.064 VND/kWh +4.8pct May 2025","web",3,"verified","EVN tariff [V]"),
("https://www.theobserver.com/2024/11/orange-presses-on-amid-years-long-solar-initiative/","Orange NJ school solar RFP: winning bidder pays 30000 USD professional-services fee","industry",2,"verified","Winner-pays 30k fee [V]"),
("https://3degreesinc.com/services/power-purchase-agreements/","3Degrees PPA services: strategy RFP eval negotiation monitoring; buyer-paid scope","web",4,"verified","Buyer advisor scope, no fee number [V scope]"),
("https://businessrenewables.org.au/state-of-the-market-2025/","BRC-A State of the Market 2025: record 2024 >3GW, 2025 reversion ~1.3GW, LGC collapse","industry",2,"verified","AU market context [V]"),
("https://pexapark.com/pexapark-raises-e20-million-in-series-c-funding-round/","Pexapark raises EUR 20m Series C; subscription/data model","web",4,"verified","Platform monetisation not per-deal [V]"),
("https://rmi.org/insight/building-local-government-capacity-for-offsite-renewable-energy-procurement/","RMI: building local gov capacity for offsite renewable procurement; advisor independence","industry",2,"verified","Advisor independence guidance [V]"),
("https://atb.nrel.gov/electricity/2025/utility-scale_pv","NREL ATB 2025 utility-scale PV cost benchmark","industry",1,"verified","US PV capex benchmark [V]"),
("https://www.nortonrosefulbright.com/en-vn/knowledge/publications/449377d8/vietnams-direct-power-purchase-agreement-a-new-era-for-renewable-energy","Norton Rose Fulbright: Vietnam DPPA new era; Decree 57 mechanics","industry",3,"verified","DPPA mechanics [V]"),
("https://vilaf.com.vn/vietnams-new-decree-on-direct-power-purchase-agreements-a-game-changer-for-renewable-energy/","VILAF: Vietnam new decree on DPPAs game changer","industry",3,"verified","DPPA mechanics [V]"),
("https://fraser.vn/en/vietnams-direct-power-purchase-agreement-decree-57-2025-nd-cp-key-takeaways/","Fraser: Vietnam DPPA Decree 57 key takeaways","industry",3,"verified","DPPA mechanics [V]"),
("https://rfpdb.com/process/download/name/Solar-RFP-Skokie-School-District-68-%28Skokie%2C-IL%29-.pdf","Skokie SD68 IL solar RFP: 0.07 USD/W DC winner-pays fee","industry",2,"verified","Winner-pays 0.07/W [V]"),
("https://apps.puc.state.or.us/orders/2024ords/24-248.pdf","Oregon PUC Order 24-248; NREL ATB 1483 USD/kW reference","industry",1,"verified","Regulatory cost reference [V]"),
("https://businessrenewables.org.au/wp-content/uploads/2025/03/241216-SOM-Report-2024-FINAL.pdf","BRC-A State of Market 2024 report PDF","industry",2,"verified","AU PPA market [V]"),
("https://www.lazard.com.au:443/media/eijnqja3/lazards-lcoeplus-june-2025.pdf","Lazard LCOE+ June 2025: 38-78 USD/MWh band","industry",2,"verified","LCOE band [V]"),
 ]
c=0
for a in ADD:
    key=(a[0] or "").strip().lower()
    if key in seen: continue
    seen.add(key)
    c+=1
    bid=('in-' if a[2]=='industry' else 'wb-')+str(c).zfill(3)
    rows.append({'id':bid,'bucket':a[2],'url':a[0],'title':a[1],'tier':a[3],'status':a[4],'pass':'deep'})
with open(LEDGER,'w',encoding='utf-8') as f:
    for r in rows:
        f.write(json.dumps(r,ensure_ascii=False))
        f.write(chr(10))
print(42)
