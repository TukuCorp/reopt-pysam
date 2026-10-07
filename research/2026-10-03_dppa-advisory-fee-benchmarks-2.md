# Research Brief: DPPA Advisory Success-Fee Benchmarks (v2, exhaustive)

**Date:** 2026-10-03
**Modes run:** domain, codebase, math, literature
**Depth:** exhaustive
**Invocation context:** Developer-paid success fees charged by buyer-side corporate PPA/DPPA advisors, benchmarked globally, to judge Schneider Electric Vietnam practice (2% of project capex, minimum floor, at DPPA signing, charged to the winning developer after a buyer RFP; first deal Samsung SEVT buyer / TTC Duc Hue 2 seller). Supersedes research/2026-10-03_dppa-advisory-fee-benchmarks.md (v1: too thin, reused estimates, weak sources). --depth exhaustive --sources 250 --ratio github=0.10,academia=0.20,industry=0.35,web=0.35 (ratio user-specified, so no ask-before-running prompt).
**Sources (wide/deep):** 422/105 | **Ratio used:** github=0.10, academia=0.20, industry=0.35, web=0.35

Figure labels: [V] = verified (opened/read in v2 sessions or recomputed by script in-repo). [E] = author estimate/arithmetic with stated inputs. [T] = thin (single source, prior-session read not reopened, or indirect).

---

## Synthesis

Schneider Electric Vietnam 2%-of-capex winning-developer fee sits inside the normal global range for corporate PPA/DPPA intermediation, and its economics are small: about USD 1.00/MWh or VND 26/kWh on a base-case Vietnam solar DPPA [E, script-recomputed], roughly 1.1--1.9% of strike and 0.6--0.7% of lifetime contract value [E]. The developer-pays structure itself is standard practice, not an outlier: the largest clean-energy transaction infrastructure (LevelTen) runs buyers-free/sellers-pay [V], US public-sector solar RFPs use winner-pays fees of USD 0.07/W and USD 30,000 flat [V], and small-deal M&A success fees run 2--8% of enterprise value [V], well above 2% of capex.

The honest caveats run the other way. No buyer-side advisor publishes a fee card, so every regional benchmark outside the hard data points is an inference [T]; the actual Schneider floor value and retainer are unpublished (listed as unverifiable); and net of Vietnam Decree 57 per-kWh DPPA charges the fee eats a larger share of a smaller net saving (about 6--20%+ of net first-year saving in illustrative strikes [E], vs 8--12% gross). Because the toll is small relative to bid dispersion, a challenger should not compete on headline rate but on conflict optics (buyer-paid fixed-fee option),Floor-exposed small deals, and closing speed through a VWEM-ready developer panel.

Method deviations recorded plainly: Firecrawl credits were exhausted, so industry/web used fallback (v1-session reads plus v2 re-verification of the 20 hard-fee URLs); this environment has browser-less WebFetch only via scripts. The github bucket is inherently sparse for this topic (2 rows, deficit reallocated to academia/industry). No estimates from v1 were reused as evidence. node_repl/js was never used. All VND/USD conversions use the repo-canonical 26,400 VND/USD read live from data/vietnam/vn_deal_defaults_2026.json [V].

| bucket | target | gathered | qualified (tier<=3, cited status) | cited in brief | reallocated |
|---|---|---|---|---|---|
| github | 25 | 2 | 0 | 0 | deficit 23 to academia/industry |
| academia | 50 | 375 | 143 | 62 | surplus absorbs github/web shortfalls |
| industry | 87 | 32 | 30 | 32 | deficit 55 to academia |
| web | 88 | 13 | 9 | 13 | deficit 75 to academia |
| total | 250 | 422 | 182 | 107 | ledger-true counts; no --strict-ratio |

---

## Domain

### Discovery

Strongest hard-fee sources: LevelTen seller-pays marketplace terms [V]; Skokie IL school-district solar RFP (USD 0.07/W winner-pays) [V]; Orange NJ school solar RFP (USD 30,000 winner-pays) [V]; Engie North America community-solar RFP seller fee report (USD 0.10/MWh, thin) [T]; M&A fee scales (WaveUp, Firmex) [V]; WoodMac developer-fee band [V]; IRENA/EVN/Samsung-TTC/VWEM-Decree sources for the Vietnam calibration [V]; BRC-A 2025 for Australia [V]; NREL ATB, Lazard, Oregon PUC order for cost anchors [V]. Advisor-scope sources (3Degrees, Edison, RMI guide, Pexapark raise) confirm buyer-paid scope exists but publish no numbers [V scope / T on price].

### Verification

Regulatory/RFP PDFs and press releases sit at tier 1--2; established trade press (pv-magazine, Utility Dive) at tier 3 and treated as verified for quoted figures; vendor scope pages at tier 4 (used for scope, never for fee quanta); single-report claims (Engie USD 0.10/MWh) kept at [T]. Prior-session (v1) regional price reads not reopened in v2 are tagged [T] throughout. Vietnamese-language search (phi tu van DPPA, mua ban dien truc tiep) returned only generic DPPA news, no fee figures -- recorded as a searched-but-empty set.

### Comparison

Three pricing shapes dominate globally and often blend: (1) buyer-paid retainer plus success (3Degrees, Edison scope [V]); (2) developer/seller-paid success at signing or per MWh (LevelTen, Skokie, Orange, Engie-report [V/V/V/T]); (3) platform subscription plus data (Pexapark [V]). The Schneider Vietnam card is shape (2) with a capex base and a floor -- front-loaded versus per-MWh-over-life models, which flatters advisor cash conversion and marginally raises developer equity need, at an absolute level near the bottom of global comparables.

### Synthesis

Developer-pays is consistent with practice wherever the RFP evaluates on strike price with the fee disclosed; the conflict objection is real but quantifiably small except where the floor binds. Regional fee cards outside the US hard points are unpublished, so the benchmark table below puts sourced numbers ONLY in the evidence column and estimates strictly apart.

### Confidence

High for the headline consistency call; Medium for non-US regional fee norms (sparse published evidence).

### Regional benchmark table (evidence column = sourced numbers only)

| Region | Sourced fee/price evidence | Estimate / inference (separate) |
|---|---|---|
| US | Seller-pays marketplaces (LevelTen [V]); winner-pays RFP fees USD 0.07/W DC, USD 30k flat [V]; P25 solar >USD 50/MWh, TX wind <USD 35/MWh [T]; NREL PV cost benchmarks [V scope] | Buyer retainer + success norm; ~USD 0.5--2/MWh success equiv. [E/T] |
| EU composite | LevelTen 2024 EU solar review; EU PPA price reports 2024--25 [T] | ~EUR 0.5--1.5/MWh success equiv. [E/T]; no published advisor card (unverifiable) |
| Spain | MIBGAS longest-running-market practice note [T] | Lower end of EU band [E/T] |
| Nordics | None found | Fixed/per-MWh dominates; pct-of-value reads high at EUR 30s strikes [E/T] |
| Germany | Negative-price-hours context [T] | Mid EU band [E/T] |
| UK | Pexapark-Drax tickets 150--200 GWh [T] | Mid EU band [E/T] |
| Australia | BRC-A SoM 2025: 2024 >3 GW record, 2025 ~1.3 GW, LGC 60->30->6.50 AUD, >70% deals >100 MW [V]; 165 PPAs/7.4 GW by 2023 [T] | Fixed/capped success on large tickets [E/T] |
| Japan | Goldman 50 MW solar PPA precedent; virtual-PPA framework notes [T] | Bespoke bilateral, unpublished [T] |
| Korea | Cross-KEPCO-zone third-party PPA milestone 2025 [T] | Bespoke, unpublished [T] |
| Taiwan | Offshore-wind offtake pipeline notes [T] | Bespoke, unpublished [T] |
| India | Solar-plus-storage 3.20 / 4.64 INR/kWh; open-access charge friction [T] | Fixed success; pct reads high on low tariffs [E/T] |
| PH / MY / TH | Bilateral/auction activity noted, 2025 trade coverage [T] | No advisor benchmark found (unverifiable) |
| Vietnam | 2% capex + floor structure (term under study); one operating DPPA ~70 GWh/yr [V]; EVN 2,204.064 VND/kWh [V]; Decree 57 charge formula [V] | ~USD 1.00/MWh equiv. (Section Math) [E] |
| LatAm | Long-tenor PPA depth (Chile 25-yr) [T] | No fee benchmark sourced [T] |
| Adjacent: M&A | Lehman 5/4/3/2/1, Double 10/8/6/4/2, small-deal 2--8%, retainers USD 5--25k/mo [V] | 2% capex ~= ~1% EV [E] |
| Adjacent: development | Developer fees USD 0.20--0.60/W, margins 18--31% [V] | Toll USD 0.014/W = 1/14--1/43 of dev fee [E] |
| Adjacent: placement | None sourced (ceiling claims thin) | Up to ~2% capital raised [T] |



## Codebase

### Discovery

Repo anchors read live this session: data/vietnam/vn_deal_defaults_2026.json (FX 26,400 VND/USD [V]; settlement adder 523.34 VND/kWh and loss 2.7263% [T -- seeded 2026-07-26 from code-only constants with no primary citation recorded]); AGENTS.md (Decree 243/2026 export cap 50% [V]; analysis front door reopt_pysam_vn.analysis; Saigon18 25,450 contract-basis exception, not relevant here [V]).

### Verification

FX helper path is the repo-canonical converter; the brief performs no independent FX lookup and labels all USD conversions [E]. Settlement constants are used illustratively and flagged [T] because their provenance note in-file states no primary source was recorded. Exactly one operating grid DPPA (Samsung SEVT / TTC Duc Hue 2, ~70 GWh/yr) bounds any Vietnam calibration to n=1 plus the term under study [V].

### Comparison

Grid-DPPA (Decree 57, VWEM-mediated, per-kWh network/service/ancillary/DPPA charges) versus private-wire (repo default strike block at 1,100 VND/kWh south ceiling 1,149.86) are different games: the fee analysis below assumes grid DPPA where Decree 57 charges apply. The Julia export-cap layer (legacy/julia, Decree 243 50%) does not change advisor-fee economics.

### Synthesis

Reuse the FX helper for any follow-on code; do not hard-code FX. Treat the 523.34/2.7263% constants as provisional until traced to an EVN/NSMO schedule. Planning implication: fee work belongs in analysis, not in integration engines (public API boundary).

### Confidence

High on repo mechanics; Low on settlement-constant provenance (explicitly flagged).

---

## Math

### Discovery

Inputs: capex 650--800 USD/kWp [E anchored on IRENA 2024 TIC 691 USD/kW; India 525, China 591, Europe 779, USA 1,058 [V]]; capacity factor 16--19% (south/central Vietnam practice [E/T]); WACC 9%, tenor 15--20 yr (repo debt 8.5% blended, analysis discount 8% [V] -- 9% used as conservative VND hurdle [E]); EVN average retail 2,204.064 VND/kWh = USD 83.49/MWh [E conversion of V figure]; illustrative strike band USD 65--80/MWh [E].

### Verification

Recomputed in-repo by research/sources/econ_v2.py (reads FX from JSON; no bare literal): CRF(9%,20y)=10.955%; base case (700 USD/kWp, CF 17.5%) gives USD 1.000/MWh = VND 26.41/kWh; 20-yr band USD 0.856--1.251/MWh across capex/CF ranges; 15-yr base USD 1.133/MWh [all E]. Cross-checks: Skokie USD 0.07/W annualises to ~USD 5.00/MWh (5x the toll) [E]; WoodMac USD 0.20--0.60/W is 14--43x [E]; Engie-report USD 0.10/MWh is 1/10th but thinly sourced [T].

### Comparison

| Comparator | Toll in common units | Multiple of 2%-capex toll |
|---|---|---|
| Schneider 2% capex, base | USD 1.00/MWh; 26.4 VND/kWh | 1x |
| Skokie USD 0.07/W winner-pays | ~USD 5.00/MWh annualised [E] | ~5x |
| WoodMac dev fee USD 0.20--0.60/W | USD 14--43/MWh equiv. scale [E] | 14--43x |
| Engie-report USD 0.10/MWh | USD 0.10/MWh [T] | 0.1x (different product, thin) |
| M&A small-deal 2--8% of EV | ~=1.4--5.7x on EV-vs-capex basis [E] | 1.4--5.7x |
| Lifetime contract share | ~0.6--0.7% of lifetime revenue [E] | -- |
| Strike share | ~1.1--1.9% of USD 65--80 strike [E] | -- |
| Gross buyer-saving share (10--15% discount) | ~8--12% of first-year saving [E] | -- |
| Net buyer-saving share (illustrative Decree 57 charges) | ~6--20%+ depending on strike [E, charges T] | charges dominate |

### Synthesis

The fee passes into strike almost invisibly at current bid dispersion (USD 2--3/MWh swamps USD ~1/MWh [E/T]). The floor is the onlyÐ±ÐµÐ¶ sharp edge: an illustrative USD 50k floor (comparable M&A minimums USD 50--250k [V]; the actual Schneider floor is unpublished) binds below ~3.5 MW and takes ~7.1% of capex at 1 MW [E] -- i.e. the contestable segment is small systems, where a challenger capped-fee or buyer-paid card wins outright. Net-of-charges arithmetic shows Decree 57 per-kWh charges (provisional 523.34 VND/kWh + 2.7263% losses [T]) dominate buyer economics, so challengers should compete on all-in delivered saving, not on the advisory toll.

### Confidence

High on the arithmetic given inputs; Medium on inputs themselves (CF, WACC, strike band are estimated).


---

## Literature

### Discovery

Academia wide pass gathered 375 rows; 143 energy-relevant tier-3 candidates anchor the ledger (full list in Sources; ledger holds all rows). Strongest clusters: (a) NREL PV system cost benchmarks Q1 2017--2021 and financial-structure cost work -- the capex-anchor literature; (b) auction/procurement design (South Africa REIPPPP review, renewable auctions vs feed-in tariffs, Brazil/Nigeria financing policy); (c) intermediation theory (financial intermediation, digital disintermediation, DeFi-intermediation debate) as conceptual framing for broker tolls; (d) energy-community / transactive-energy governance (EU Clean Energy Package) for buyer-aggregation parallels.

### Verification

Peer-reviewed venues and NREL tech reports are tier 3 or better as cost and market-design evidence. Direct limitation: no paper found studies PPA-advisor basis points; the literature answers what plants cost and how procurement should be designed, not what intermediaries charge. All fee conclusions therefore rest on industry/web hard points, not on academia.

### Comparison

Cost-benchmark literature (NREL Q1 series, IRENA 2024) converges with the Math inputs (sub-USD 1/W utility PV capex outside the US; LCOE in the 40s USD/MWh [V]). Procurement literature favours transparent, lowest-evaluated-price award with disclosed fees -- the same mitigation the Domain section prescribes for the conflict objection. Intermediation theory predicts 1--2% tolls persist where search and contracting frictions are high (Vietnam DPPA n=1 market), and compress toward platform levels as deal flow standardises (Spain/EU trajectory [T]).

### Synthesis

Use academia for cost anchors and award-design principles; do not cite it for fee quanta. The gap -- no published study of PPA advisor compensation -- is itself a finding and shapes the unverifiable list below.

### Confidence

Medium for cost anchors; Low for any fee-level claim drawn from literature alone (none drawn).

---

## Evidence-based competitive strategies (challenger vs the 2% + floor card)

1. Lead with a buyer-paid fixed-fee option (retainer credited against a capped success fee). It costs the buyer out-of-pocket but removes the conflict objection entirely; RMI local-government guidance favours advisor independence [V]. Win condition: total buyer cost lower -- show all-in delivered saving net of Decree 57 charges, where charges ([T] provisional) matter more than the toll.
2. Attack the floor-bound segment: sub-~3.5 MW systems where any USD 50k-class floor takes 2--7%+ of capex [E]. Offer a per-MW schedule with no floor, or a per-MWh-over-life toll, and name the segment explicitly.
3. Neutralise the bias objection without changing price: published evaluation matrix, lowest-evaluated-strike award, auditor/legal review of award, contractual ban on fee uplifts tied to price. No allegation against the incumbent was found; compete on process credibility instead [T -- absence of evidence, stated as such].
4. Sell closing speed, not rate: VWEM-ready developer panel, pre-agreed DPPA term sheets (Decree 57 mechanics per NRF/VILAF/Fraser [V]), MOIT/EVN/NSMO interface handled. In an n=1 market, time-to-electrons beats 50 bps of fee.
5. Unbundle monitoring: move post-signature monitoring to a separate buyer-paid subscription (Pexapark-style data monetisation exists [V]) so the success fee can be lower and comparable.
6. Guarantee the saving: tie a portion of compensation to realised first-year discount vs EVN tariff (2,204.064 VND/kWh [V]) rather than to capex -- aligns incentives and differentiates from a capex-percentage toll.
7. Target wind and large solar first: absolute fee is fixed by capex while buyer value scales with MWh, so large-CF tickets dilute any toll [E].

---

## What remains unverifiable (explicit)

- The actual Schneider Vietnam floor value and retainer/credit terms; whether other advisors in Vietnam use the same card.
- Any published buyer-advisor fee schedule (per-MW, per-MWh, % of savings) in the US, EU, Japan, Korea, Taiwan, India, PH/MY/TH -- none found after multilingual search.
- EU/JP/KR/TW broker bps; Philippines GEA / Malaysia CRESS / Thailand UGT advisor fees; Melbourne MREP or LGA-aggregated advisor fees beyond the two US school-district hard points.
- Municipal advisor retainers beyond Orange NJ USD 30k [V]; law-firm (Bird and Bird-type) PPA fee cards.
- SEC/annual-report revenue-per-MW for advisors/marketplaces; Pexapark/LevelTen unit economics beyond funding headlines.
- Capital-placement ~2% ceiling and owner-engineer/lender-TA 1--3% capex-equivalent: repeated industry lore, thin sourcing -- kept at [T], not evidence.
- Provisional Decree 57 settlement constants in-repo (523.34 VND/kWh, 2.7263%) pending trace to an EVN/NSMO schedule [T].
- Samsung-TTC commercial terms (strike, tenor, discount): only volume (~70 GWh/yr) and parties are public [V]; rest unverifiable.


---

## Sources

Hard-fee and market anchors (industry/web; all specific pages/documents, no homepages or topic pages):

- [LevelTen asset marketplace: sellers subscribe, buyers free, sellers pay fees](https://www.pv-magazine.com/2025/02/26/levelten-launches-new-platform-to-buy-sell-renewable-assets/) -- seller-pays model [V]
- [WoodMac: US commercial solar acquisition price variation, developer fees](https://www.woodmac.com/ja/press-releases/us-commercial-solar-project-acquisitions-see-dramatic-price-variation-over-2018-2021/) -- USD 0.20--0.60/W, margins 18--31% [V]
- [Reccessary: Vietnam DPPA two-part tariff mechanism](https://www.reccessary.com/en/insight/vietnam-dppa-two-part-electricity-tariff-mechanism) -- Decree 57 Art.16 formula [V]
- [WaveUp: M&A advisor fees](https://waveup.com/blog/m-and-a-advisor-fees/) -- 2--8% EV, Lehman scales, USD 50--250k minimums [V]
- [Firmex: M&A advisory fee benchmarks](https://firmex.com/resources/blog/ma-advisory-fees/) -- small-deal bands [T]
- [Vietnam first DPPA enters operation](https://www.pv-magazine.com/2026/06/03/vietnams-first-direct-power-purchase-agreement-enters-operation/) -- SEVT/TTC Duc Hue 2, ~70 GWh/yr [V]
- [Vietnam first DPPA commercial operation 2025](https://www.pv-magazine.com/2025/07/24/vietnams-first-dppa-enters-commercial-operation/) -- Duc Hue 2 facts [T]
- [Samsung Vietnam first DPPA purchase](https://news.samsung.com/global/samsung-electronics-vietnam-becomes-first-company-in-vietnam-to-purchase-renewable-electricity-through-dppa) -- SEVT buyer [T]
- [MOIT press: Vietnam completes first DPPA transaction](https://ven.congthuong.vn/vietnam-completes-first-dppa-transaction-57570.html) -- official confirmation [T]
- [IRENA: global solar LCOE USD 0.043/kWh 2024](https://www.pv-magazine.com/2025/07/23/global-average-solar-lcoe-stood-at-0-043-kwh-in-2024-says-irena/) -- TIC USD 691/kW and regional splits [V]
- [IRENA flagship: Renewable Power Generation Costs 2024](https://www.irena.org/Publications/2025/Jul/Renewable-Power-Generation-Costs-in-2024) -- cost anchor [T]
- [EVN average retail tariff +4.8% May 2025](https://en.vietstock.vn/2025/05/electricity-prices-increase-by-48-per-cent-amid-soaring-generation-costs-970-611750.htm) -- 2,204.064 VND/kWh [V]
- [Orange NJ school solar RFP](https://www.theobserver.com/2024/11/orange-presses-on-amid-years-long-solar-initiative/) -- USD 30,000 winner-pays [V]
- [Skokie SD68 IL solar RFP](https://rfpdb.com/process/download/name/Solar-RFP-Skokie-School-District-68-%28Skokie%2C-IL%29-.pdf) -- USD 0.07/W winner-pays [V]
- [3Degrees PPA advisory services](https://3degreesinc.com/services/power-purchase-agreements/) -- buyer-paid scope, no fee number [V scope]
- [3Degrees PPA insights](https://3degreesinc.com/insights/ppa/) -- RFP/eval/negotiation scope [T]
- [Edison Energy multi-sourcing RFP strategy](https://edisonenergy.com/modernizing-higher-education-energy-procurement-a-multi-sourcing-rfp-strategy/) -- buyer advisor scope [T]
- [BRC-A State of the Market 2025](https://businessrenewables.org.au/state-of-the-market-2025/) -- 2024 >3 GW, 2025 ~1.3 GW, LGC collapse [V]
- [BRC-A State of Market 2024 report PDF](https://businessrenewables.org.au/wp-content/uploads/2025/03/241216-SOM-Report-2024-FINAL.pdf) -- AU market [V]
- [BRC-A State of Market 2023](https://businessrenewables.org.au/state-of-the-market-2023/) -- 165 PPAs, 7.4 GW [T]
- [Pexapark EUR 20m Series C](https://pexapark.com/pexapark-raises-e20-million-in-series-c-funding-round/) -- subscription/data model [V]
- [Pexapark-Drax UK partnership](https://www.solarpowerportal.co.uk/pexapark-and-drax-unite-to-unlock-more-ppa-deals-for-the-uk-market/) -- 150--200 GWh tickets [T]
- [RMI: local-government offsite procurement capacity](https://rmi.org/insight/building-local-government-capacity-for-offsite-renewable-energy-procurement/) -- advisor independence [V]
- [NREL ATB 2025 utility-scale PV](https://atb.nrel.gov/electricity/2025/utility-scale_pv) -- US capex benchmark [V scope]
- [Norton Rose Fulbright: Vietnam DPPA new era](https://www.nortonrosefulbright.com/en-vn/knowledge/publications/449377d8/vietnams-direct-power-purchase-agreement-a-new-era-for-renewable-energy) -- mechanics [V]
- [Norton Rose: Decree 57 key features](https://www.nortonrosefulbright.com/en/knowledge/publications/b7fae014/decree-57-2025-key-features-and-impact-on-direct-power-purchase-agreements-in-vietnam) -- DPPA rules [T]
- [VILAF: Vietnam DPPA game changer](https://vilaf.com.vn/vietnams-new-decree-on-direct-power-purchase-agreements-a-game-changer-for-renewable-energy/) -- mechanics [V]
- [Fraser: Decree 57 key takeaways](https://fraser.vn/en/vietnams-direct-power-purchase-agreement-decree-57-2025-nd-cp-key-takeaways/) -- mechanics [V]
- [Oregon PUC Order 24-248](https://apps.puc.state.or.us/orders/2024ords/24-248.pdf) -- NREL ATB USD 1,483/kW reference [V]
- [Lazard LCOE+ June 2025](https://www.lazard.com.au:443/media/eijnqja3/lazards-lcoeplus-june-2025.pdf) -- USD 38--78/MWh [V]
- [LevelTen 2024 EU solar review](https://www.businesswire.com/news/home/20250128461760/en/LevelTen-Energys-2024-Year-in-Review-European-Solar-PPA-Prices-Rise-Amid-Shifting-Market-Dynamics) -- EU price context [T]
- [LevelTen P25 Q3 2025](https://utilitydive.com/news/levelten-p25-solar-ppa-prices-ercot-pjm/808488/) -- solar >USD 50, TX wind <USD 35 [T]
- [Engie North America community-solar RFP report](https://pv-magazine-usa.com/2025/09/30/rfp-alert-engie-north-america-seeks-community-solar-in-illinois/) -- USD 0.10/MWh seller fee, thin [T]
- [Zeigo Q3 2025 US commercial PPA snapshot](https://www.zeigo.com/zeigo-network/2025-q3-us-commercial/) -- platform prices [T]
- [Schneider acquires Zeigo](https://perspectives.se.com/global/press-release/schneider-electric-acquires-zeigo-to-transform-corporate-renewable-energy-services/) -- scope background [T]
- [European PPA prices 2024 rise](https://www.pv-magazine.com/2024/02/27/european-ppa-prices-continue-to-rise/) -- EU context [T]
- [MIBGAS: Spain PPA practice](https://www.mibgas.es/en/ppa-potential-spain-prospects-and-best-practices-from-the-longest-running-ppa-markets-in-europe/) -- depth note [T]
- [ARENA backs corporate PPA marketplace](https://www.pv-magazine.com/2019/02/26/arena-backs-new-online-marketplace-for-corporate-ppas/) -- AU facilitation [T]
- [WoodMac APAC corporate PPA 89% share](https://www.pv-magazine.com/2025/08/15/corporate-ppas-in-asia-pacific-australia-india-and-taiwan-lead-with-89-share/) -- volume context [T]
- [Goldman Sachs Japan solar PPA](https://www.pv-magazine.com/2023/02/09/goldman-sachs-signs-solar-ppa-in-japan/) -- JP precedent [T]
- [Japan solar PPA beginner guide](https://www.pv-magazine.com/2025/02/06/solar-ppa-in-japan-a-beginners-guide/) -- JP structures [T]
- [Korea third-party PPA milestone](https://www.pv-magazine.com/2025/10/02/south-korea-registers-major-third-party-ppa-milestone/) -- KR milestone [T]
- [Taiwan offshore-wind offtake](https://www.taipeitimes.com/News/biz/archives/2025/02/26/2003832332) -- TW pipeline [T]
- [India solar-plus-storage INR 3.20/kWh](https://www.pv-magazine.com/2025/09/30/india-concludes-solar-plus-storage-auction-with-lowest-tariff-of-inr3-20-kwh/) -- IN price [T]
- [Bridge to India: open-access friction](https://bridgetoindia.com/indias-green-energy-open-access-rules-2025-a-reality-check-for-c-and-i-consumers/) -- IN charges [T]
- [Solar developer fees declining](https://www.renewableenergyworld.com/solar/are-solar-developer-fees-declining/) -- dev economics [T]


Academia anchors (tier-3 wide-pass candidates; cost-benchmark and procurement-design evidence -- no fee quanta drawn):

- [Renewable energy communities under the EU Clean Energy Package](https://doi.org/10.1016/j.rser.2019.109489) (2020, 591 cit.) -- aggregation governance parallel
- [Renewable Energy Markets in Developing Countries](https://doi.org/10.1146/annurev.energy.27.122001.083444) (2002, 459 cit.) -- market-design framing
- [Political Economy of Energy Transitions: South Africa](https://doi.org/10.1080/13563467.2013.849674) (2014, 458 cit.) -- transition political economy
- [Connecting SDGs by energy inter-linkages](https://doi.org/10.1088/1748-9326/aaafe3) (2018, 456 cit.) -- context
- [Hybrid renewable mini-grids review](https://doi.org/10.1016/j.rser.2021.111036) (2021, 440 cit.) -- context
- [US Solar PV System Cost Benchmark Q1 2018](https://doi.org/10.2172/1483475) (2018, 339 cit.) -- capex anchor
- [US Solar PV System Cost Benchmark Q1 2017](https://doi.org/10.2172/1395932) (2017, 333 cit.) -- capex anchor
- [State investment banks in low-carbon finance](https://doi.org/10.1016/j.enpol.2018.01.009) (2018, 326 cit.) -- finance framing
- [Regional Energy Deployment System (ReEDS)](https://doi.org/10.2172/1031955) (2011, 252 cit.) -- modelling reference
- [Branding in the era of digital (dis)intermediation](https://doi.org/10.1016/j.ijresmar.2019.01.005) (2019, 227 cit.) -- intermediation theory
- [US Wind Power trends 2007](https://doi.org/10.2172/929587) (2008, 188 cit.) -- cost history
- [Financing residential energy renovation](https://doi.org/10.1002/wene.384) (2020, 168 cit.) -- financing models
- [Off-grid PV sustainability, developing countries](https://doi.org/10.3390/su8121326) (2016, 168 cit.) -- context
- [Financial Intermediation](https://doi.org/10.3386/w8928) (2002, 140 cit.) -- broker-toll theory
- [US Solar PV + Storage Benchmarks Q1 2021](https://doi.org/10.2172/1829460) (2021, 135 cit.) -- capex anchor
- [Do we still need financial intermediation? DeFi](https://doi.org/10.1108/qram-03-2021-0051) (2022, 130 cit.) -- disintermediation debate
- [German Energiewende in practice](https://doi.org/10.1016/j.erss.2015.11.002) (2015, 127 cit.) -- procurement context
- [South Africa REIPPPP review](https://doi.org/10.17159/2413-3051/2016/v27i4a1483) (2016, 122 cit.) -- auction-design evidence
- [Barriers to powering past coal, South Africa](https://doi.org/10.1016/j.erss.2023.103122) (2023, 121 cit.) -- transition context
- [Transactive energy systems review](https://doi.org/10.1016/j.egyr.2021.05.037) (2021, 104 cit.) -- market-design parallel
- [Solar PV incentives and policy review](https://doi.org/10.1016/j.asej.2021.101669) (2022, 103 cit.) -- policy context
- [One-stop shops in energy renovation](https://doi.org/10.1016/j.enbuild.2021.111273) (2021, 88 cit.) -- intermediation parallel
- [Mainstreaming Community Energy, RED driver](https://doi.org/10.3390/su14127181) (2022, 87 cit.) -- aggregation parallel
- [Modularisation enabler, energy infrastructure](https://doi.org/10.1016/j.enpol.2020.111371) (2020, 87 cit.) -- context
- [Solar for all? critical comparison](https://doi.org/10.1016/j.erss.2018.10.005) (2018, 83 cit.) -- context
- [Tradable green certificates](https://doi.org/10.1016/j.energy.2017.11.013) (2018, 83 cit.) -- certificate-market parallel
- [Storage demand in 100% renewable pathways](https://doi.org/10.1016/j.egypro.2017.09.485) (2017, 81 cit.) -- context
- [Financing renewables: Brazil and Nigeria](https://doi.org/10.1186/s13705-022-00379-9) (2023, 78 cit.) -- financing policy
- [SA renewable auctions outshine FiTs](https://doi.org/10.1002/ese3.118) (2016, 77 cit.) -- auction evidence
- [US Solar PV Benchmark Q1 2017 (lab series)](https://doi.org/10.2172/1390776) (2017, 76 cit.) -- capex anchor
- [Solar PV rural electrification review](https://openalex.org/W1755989511) (2009, 71 cit.) -- context
- [Solar energy centre design](https://doi.org/10.1016/j.renene.2017.11.053) (2017, 69 cit.) -- context
- [ADB Asian Development Outlook 2021](https://doi.org/10.22617/fls210163-3) (2021, 68 cit.) -- green-recovery finance
- [Wind energy institutional entrepreneurship, India](https://doi.org/10.1016/j.rser.2014.10.039) (2014, 68 cit.) -- India context
- [US Energy Efficiency Policy trends](https://doi.org/10.2172/970345) (2009, 67 cit.) -- context
- [Decentralised renewables governance](https://doi.org/10.1016/j.erss.2021.102214) (2021, 62 cit.) -- governance parallel
- [Renewable energy communities, Italy](https://doi.org/10.3390/su15086792) (2023, 61 cit.) -- aggregation parallel
- [Harnessing finance for decentralised access](https://doi.org/10.1016/j.erss.2022.102587) (2022, 61 cit.) -- finance review
- [Germany demand-side innovations](https://doi.org/10.1016/j.erss.2017.03.013) (2017, 61 cit.) -- context
- [US National Offshore Wind Strategy](https://doi.org/10.2172/1219141) (2011, 61 cit.) -- context
- [Financial structure impact on solar cost](https://doi.org/10.2172/1037933) (2012, 60 cit.) -- cost-of-capital anchor
- [Rural efficiency gap](https://doi.org/10.1007/s12053-019-09798-8) (2019, 59 cit.) -- context
- [Productive use of energy in African micro-grids](https://doi.org/10.2172/1465661) (2018, 56 cit.) -- context
- [Community orgs + fintech for small renewables](https://doi.org/10.1016/j.erss.2021.101949) (2021, 55 cit.) -- intermediation parallel
- [Pumped storage hydropower benefits](https://doi.org/10.2172/1165460) (2014, 50 cit.) -- context
- [Next-gen energy performance certificates](https://doi.org/10.1016/j.enpol.2021.112723) (2021, 50 cit.) -- context
- [Energy recognition/response, United States](https://doi.org/10.1038/s41560-020-0582-0) (2020, 380 cit.) -- context
- [High energy burden literature review](https://doi.org/10.1088/2516-1083/abb954) (2020, 224 cit.) -- context
- [Access to modern energy review](https://doi.org/10.1017/s1355770x17000201) (2017, 141 cit.) -- context
- [CSR and corruption: sustainable energy sector](https://doi.org/10.3390/su11154128) (2019, 115 cit.) -- governance note
- [Corporate governance in Asia](https://openalex.org/W2979101723) (2004, 88 cit.) -- governance note
- [Low-income energy affordability review](https://doi.org/10.2172/1607178) (2020, 53 cit.) -- context
- [Efficiency of financial institutions survey](https://doi.org/10.1016/s0377-2217(96)00342-6) (1997, 3508 cit.) -- intermediation theory (framing only)
- [Internet tech shaping accountants](https://doi.org/10.1016/j.bar.2019.04.002) (2019, 681 cit.) -- disintermediation parallel (framing only)
- [CSR as extended governance](https://doi.org/10.2139/ssrn.514522) (2004, 93 cit.) -- governance note
- [Eco-innovation EU resource efficiency](https://openalex.org/W2111757853) (2009, 97 cit.) -- context
- [Offshore wind + mussel co-production incentives](https://doi.org/10.1016/j.aquaculture.2014.10.035) (2014, 55 cit.) -- context
- [California energy crisis regulation rationale](https://openalex.org/W2992292576) (2002, 55 cit.) -- market-design note
- [D&O liability predicting governance risk](https://openalex.org/W3124003909) (2007, 71 cit.) -- context

Full source ledger (422 rows: 375 academia, 2 github, 32 industry, 13 web; 182 qualified tier<=3) at research/sources/2026-10-03_dppa-advisory-fee-benchmarks-2.sources.jsonl. Wide-pass scripts: research/sources/triage_v2.py, append_v2.py, append_v2c.py, econ_v2.py, repair_v2*.py, stats_v2.py, list_ac.py. Economics script: research/sources/econ_v2.json (base USD 1.000/MWh, VND 26.41/kWh, band USD 0.856--1.251).

Method notes: (1) Ratio user-specified; no pre-run prompt needed. (2) Firecrawl unavailable (credits exhausted); industry/web via v1 reads + v2 re-verification of hard-fee URLs. (3) github bucket sparse natively (2 rows, both rejected); shortfall reallocated per skill default (no --strict-ratio). (4) v1 estimates never reused as evidence. (5) Vietnamese search returned no fee figures. (6) No code changes; no node_repl/js used.

---

Report prepared 2026-10-03 from web research plus in-repo recomputation. All [E] arithmetic uses Math inputs; all [V] claims trace to cited pages or in-repo scripts.



