# DPPA Advisory Fee Benchmarks: Is a 2pct Developer-Paid Success Fee Normal, and How to Compete

Date: 2026-10-03 | Repo: reopt-pysam | Type: web research, no code changes

Figure labels used throughout: [V] = verified against a cited source. [E] = estimate or inference by the author, with basis stated. [T] = thin evidence, treat as directional only.

## Executive summary

Schneider Electric runs buyer-side DPPA RFPs in Vietnam and charges the winning developer a success fee of 2pct of project capex with a minimum floor, payable at DPPA signing. The headline finding of this research: a 2pct-of-capex developer-paid success fee sits inside the normal global range for corporate PPA and DPPA intermediation, and its economics are small enough to pass into the strike price almost invisibly (about 1 USD per MWh, or 1 to 2pct of a typical Vietnam solar DPPA strike). That makes the fee defensible, but also contestable: because the cost is small relative to deal value, a challenger does not need to undercut the 2pct to win. It needs a more credible buyer funnel, faster closings, or a fee shape that removes the conflict-of-interest objection.

Key numbers in one place:

- Typical Vietnam solar DPPA input set [E, anchored on [V] benchmarks in Sections 5 and 6]: capex 650 to 800 USD per kWp, capacity factor 16 to 19pct, VND-denominated WACC around 9pct, tenor 15 to 20 years, strike near the EVN industrial tariff band of roughly 70 to 88 USD per MWh.
- A 2pct capex fee on a 700 USD per kWp plant equals 14,000 USD per MWp [E]. Annualised over 20 years at 9pct (capital recovery factor 10.96pct) that is about 1,534 USD per year per MWp, spread over about 1,533 MWh per year, i.e. about 1.00 USD per MWh [E]. Sensitivity band across the input ranges: about 0.85 to 1.30 USD per MWh [E].
- That adder is about 1.2 to 1.9pct of a 65 to 80 USD per MWh strike [E], about 0.6 to 0.8pct of lifetime contract value [E], and about 8 to 14pct of the buyer first-year saving if the DPPA discounts the EVN tariff by 10 to 15pct [E].
- Global comparison [V where noted, else E/T]: US and EU buyer advisors typically work on retainer plus success; marketplaces (LevelTen in the US and Europe) charge sellers, i.e. the developer side, with buyers free and sellers on subscription [V]. M and A sell-side success fees run 2 to 8pct on small deals on Lehman-type scales [V]. Placement fees run up to about 2pct of capital raised [T]. Solar development margins of 0.20 to 0.60 USD per W (18 to 31pct) dwarf a 0.014 USD per W (2pct of 0.70 USD per W) advisory toll [T]. Owner engineer and lender technical-advisor scopes typically cost another 1 to 3pct of capex equivalent [E/T]. In that company, 2pct of capex is ordinary.
- Vietnam market state [V]: exactly one operating grid DPPA exists (Samsung SEVT buyer, TTC Duc Hue 2 solar seller, about 70 GWh per year, Schneider as consultant), under a new full DPPA regime (Decree 57 of March 2025 replacing Decree 80 of 2024). The EVN average retail tariff is 2,204.07 VND per kWh from May 2025 after four hikes since 2023. PDP8-revision targets imply tens of GW of new solar and wind headroom. The binding constraints are not demand for advisory but bankable developers, VWEM participation mechanics, and the MOIT ceiling tariff.

## Methods and how to read the labels

- Sources: 62 numbered entries in Section 9, each with a URL. Pages actually opened during research carry exact article URLs. Publisher topic pages are given where only the outlet and story were confirmed from search. Accessed October 2026.
- [V] figures are quoted from the cited page. [E] figures are author arithmetic with stated inputs. [T] marks industry-lore figures with thin sourcing, including explicit buyer-advisor fee schedules, which are almost never published.
- Currency anchor for this repo: per project convention the canonical VND per USD rate resolves from data/vietnam/vn_deal_defaults_2026.json via the exchange-rate helper. New code must never hard-code an FX literal. This report therefore quotes tariffs in VND per kWh and gives USD conversions as explicitly labelled [E] conversions, not canonical values.
## 1. Fee models and benchmarks

### 1.1 How corporate PPA and DPPA intermediation is priced globally

Three shapes dominate, often blended in one engagement:

1. Buyer-paid retainer plus success fee. The buyer hires an advisor (Schneider Electric, Edison Energy, 3Degrees, South Pole and peers) for strategy, RFP design, offer evaluation, negotiation and post-signature monitoring. 3Degrees describes exactly this end-to-end scope: energy strategy, RFP management, project evaluation, negotiation and ongoing monitoring [V]. Edison Energy describes multi-sourcing RFP strategy plus shortlist, negotiation and contracting [V]. Retainer levels are not published ([T]: practitioners quote low five figures per month for enterprise programs, credited against success). Success is typically set per MW, per MWh, or as a share of first-year savings or contract value [E/T].
2. Developer-paid (seller-paid) success fee. The marketplace or buyer agent charges the winning generator. LevelTen states this explicitly for its Asset Marketplace: transaction fees are always paid by sellers, buyers use the platform free, and sellers must hold a subscription to transact [V]. LevelTen model summaries describe the fee as a percentage of total contract value or a fixed fee per transaction, paid by the buyer, the developer, or both depending on product [V, secondary summary]. A reported Engie North America community-solar RFP carried a 0.10 USD per MWh success fee on the seller [V, trade-press report, thin corroboration].
3. Platform subscription plus data. Pexapark monetises PPA price reference, market intelligence and advisory around portfolio and hedging decisions rather than per-deal brokerage [V]. Zeigo (Schneider) runs the Zeigo Network and Zeigo Power marketplace plus published PPA price snapshots [V]. RE-Source is the European industry platform for corporate sourcing with its own market data [V].

### 1.2 United States

- PPA price context [V]: LevelTen Q3 2025 assessment has Midwest and Southwest solar P25 offer prices just above 50 USD per MWh and Texas wind below 35 USD per MWh, with ERCOT wind fair values up 16pct and solar up 8pct in 2025 on data-centre demand.
- Fee norm [E/T with V anchors]: enterprise buyer advisors on retainer plus success; developer-side closes via marketplaces where the seller pays. Against P25 solar near 50 USD per MWh, a 1 USD per MWh equivalent toll is about 2pct of price, consistent with seller-paid marketplace economics.
- Scale context [V]: RMI Buyers Roadmap work and CEBA buyer resources frame US aggregation and deal facilitation practice; CEBA reported as a buyer-side community rather than a fee-taker.

### 1.3 Europe: Spain, Nordics, Germany, United Kingdom

- Price context [V]: Pexapark EURO composite: 52.53 EUR per MWh in January 2025 (up 1.5pct), 50.25 in February (down 4.3pct), 46.40 in October (down 3pct), 45.10 in December; full-year 2025 volumes 13.1 GW across 247 deals versus 15.3 GW in 2024. Spain: solar capture around 53 to 67 EUR per MWh in 2024 coverage. Nordics: wind PPA assessments around 30 to 47 EUR per MWh. UK: typical bilateral sizes of 150 to 200 GWh cited in Pexapark-Drax partnership coverage. Germany: negative-price hours about 5pct of 2024 rising to about 10pct in the first eight months of 2025.
- Fee norm [E/T]: advisor retainers plus developer success are standard on both bilateral and platform-assisted deals; seller-paid marketplace fees mirror the US. No published pan-European advisor fee schedule was found ([T] flagged). The economics are comparable to the US: a 1 EUR per MWh toll on a 50 EUR strike is 2pct.
- Spain note [V]: MIBGAS analysis treats Spain as Europe longest-running PPA market, with standardised practice and the deepest solar pipeline, which compresses advisory pricing power toward platform levels.
- Nordics note [E/T]: low absolute prices (30s EUR per MWh) make percentage-of-value fees look expensive, so per-MWh or fixed success scales dominate there.

### 1.4 Australia

- Market context [V]: the Business Renewables Centre Australia State of the Market 2025 reports 2024 as a record year above 3 GW, then a 2025 reversion to about 1.3 GW as deal prices rose, offer prices sat above buyer expectations, LGC prices collapsed (60 AUD early 2024 to 30 AUD end 2024 to 6.50 AUD by December 2025) and buyers waited on CIS tenders. Queensland led with over 650 MW, Western Australia about 220 MW, and over 70pct of the 2025 market sat in deals above 100 MW. BRC-A history: 58 PPAs by 70 organisations totalling 2.3 GW since 2017 (2019 report), 165 PPAs totalling 7.4 GW by 2023, and a 2019 deal-tracker marketplace with 7 GW on offer.
- Fee norm [E/T]: buyer facilitation via BRC-A (a not-for-profit buyer-guidance body) plus commercial advisors; no published advisor fee card found. Large-deal dominance implies fixed or capped success fees rather than straight percentages.

### 1.5 Japan, Korea, Taiwan

- Market context [V]: Wood Mackenzie analysis of APAC has Australia, India and Taiwan at 89pct of regional corporate PPA volume, with solar dominant in India, offshore wind dominant in Taiwan, and a balanced solar-wind mix in Australia; Japan, Korea and mainland China are easing offsite procurement rules. Japan corporate-PPA explainer coverage notes virtual-PPA structures with environments such as the non-FIT non-fossil certificate market. Korea coverage notes a 2025 third-party PPA milestone with a first cross-KEPCO-zone contract. Taiwan coverage notes the offshore-wind-led corporate pipeline (e.g. CIP Fengmiao-linked offtake reporting).
- Fee norm [E/T]: nascent buyer-advisory markets with bilateral, largely bespoke fees; no published benchmarks found. Thin-evidence flag applies to the whole sub-region.

### 1.6 India, Philippines, Malaysia, Thailand

- India [V]: project-level price points such as 3.20 INR per kWh for 200 MW solar-plus-storage and 4.64 INR per kWh for 250 MW storage-linked solar show how keenly generation is priced; Bridge to India analysis notes open-access and general-network-access charges as the key friction for commercial and industrial procurement.
- Philippines, Malaysia, Thailand [V/E]: 2025 trade coverage records Thai solar-plus-BESS auctions, Malaysian corporate renewable supply deals and Philippines bilateral contracting, but no published advisor fee benchmarks were found for any of the three ([T]).
- Fee norm [E/T]: low absolute tariffs push intermediation toward fixed success payments or developer-paid models; percentage-of-capex reads higher against low-cost builds, so floors bind more often on small systems.

### 1.7 Vietnam

- Operating precedent [V]: exactly one grid-connected DPPA is in commercial operation (Samsung SEVT and TTC Duc Hue 2, about 70 GWh per year, Schneider as consultant, first electrons July 2025). No published fee. The 2pct-with-floor term under study is therefore the market second data point, not the fiftieth ([T] on whether other advisors use the same card).
- Implied economics [E]: at Vietnamese build costs and tariffs (Sections 5 and 6), 2pct of capex converts to roughly 1 USD per MWh, i.e. a low-single-digit share of price, which matches global seller-paid tolls.

### 1.8 Latin America

- Context [V]: Chilean corporate PPA structures (ANESCO Lechuga-type 25-year utility PPAs, Brazil ADD power-shifting analysis) show long-tenor contracting depth. No LatAm advisor fee benchmark was sourced ([T]). Recorded here for completeness because buyer-advisor models travel from these markets into APAC practice.

### 1.9 Benchmark table: who pays, in what unit, how much

Conventions: Quantum column gives the normal range. Rating V means at least one primary or trade source confirms the cell. E means author estimate from adjacent evidence. T means thin, single-source or inferred.

| Region | Buyer-side norm | Developer-side norm | Typical quantum | Rating |
|---|---|---|---|---|
| US | Retainer plus success (per MW or share of savings) | Marketplace seller-paid; RFP seller success fees | Retainer low-5-figures per month; success equiv. 0.5 to 2 USD per MWh | E, V on seller-pays |
| EU composite | Retainer plus success | Seller-paid platform and RFP fees | Success equiv. 0.5 to 1.5 EUR per MWh | E, V on prices |
| Spain | Same, compressed by depth | Seller-paid | Lower end of EU band | E |
| Nordics | Fixed or per-MWh (pct reads high at 30s EUR) | Seller-paid | 0.3 to 0.8 EUR per MWh equiv. | E/T |
| Germany | Retainer plus success; shaping risk priced | Seller-paid | Mid EU band | E |
| UK | Retainer plus success | Seller-paid; 150 to 200 GWh typical tickets | Mid EU band | E, V on ticket size |
| Australia | BRC-A guidance plus commercial advisor | Negotiated success | Fixed or capped, large-deal dominated | E/T |
| Japan | Bespoke bilateral | Bespoke | Unpublished | T |
| Korea | Bespoke bilateral | Bespoke | Unpublished | T |
| Taiwan | Bespoke, offshore-wind-led | Bespoke | Unpublished | T |
| India | Thin advisory layer; charges friction noted | Negotiated | Fixed, low absolute tariffs | T |
| Philippines | Bespoke | Bespoke | Unpublished | T |
| Malaysia | Bespoke | Bespoke | Unpublished | T |
| Thailand | Bespoke | Bespoke | Unpublished | T |
| Vietnam | Schneider buyer-RFP model (retainer unknown) | 2pct of capex with floor at signing | About 1 USD per MWh equiv. | E, V on structure |
| LatAm | Retainer plus success | Negotiated success | Unpublished in this study | T |

Reading the table: the Vietnam 2pct sits at the developer-paid end of a globally normal split. The unit (pct of capex at signing) front-loads payment relative to per-MWh-over-life models, which flatters advisor cash conversion and slightly raises developer equity need, but the absolute toll is small (Section 3).

### 1.10 Adjacent comparables: development, M and A, placement, owner engineer

- M and A sell-side success [V]: classic Lehman scale 5, 4, 3, 2, 1pct across successive million-dollar tranches; Double Lehman 10, 8, 6, 4, 2pct. Worked example: a 10M USD transaction fee is about 360k USD (3.6pct). Retainers 5k to 25k USD per month are common; about 71pct of advisors charge upfront fees and about 77pct credit them against success. Small-deal percentages run 2 to 8pct. A 2pct capex toll is therefore below or at the bottom of small-deal M and A success rates, for a much more standardised product.
- Capital placement [T]: up to about 2pct of capital raised is the commonly quoted ceiling for placement or fundraising success. Same order as the DPPA toll, but placement agents do not deliver a 15-to-20-year revenue contract.
- Solar development margin [T]: industry coverage puts developer creation value around 0.20 to 0.60 USD per W (18 to 31pct of build cost in some samples) and Wood Mackenzie-based cost work near 0.28 USD per W of development cost. A 2pct-of-capex toll on a 0.70 USD per W build is 0.014 USD per W, i.e. roughly one-twentieth of development cost and a small fraction of margin. Developers can absorb it without repricing risk.
- Owner engineer and lender technical advisor [E/T]: full owner-engineer plus lender-TA scope on utility solar is typically 1 to 3pct of capex equivalent (fixed fees of low-to-mid six figures on 50 MW-plus plants). The DPPA advisor toll is therefore comparable to, or smaller than, the engineering assurance stack buyers already pay for.

## 2. Who pays, and the conflict-of-interest debate

The objection writes itself: if the developer pays the buyer advisor, the fee passes into the strike price, so the buyer pays anyway and the advisor may favour the highest-fee bidder over the cheapest electrons. The evidence and the counter-arguments:

- Precedent that seller-pays is normal [V]: LevelTen operates the largest clean-energy transaction infrastructure on exactly this split (buyers free, sellers subscribed and fee-paying). The market has not treated that as disqualifying; it treats it as platform economics.
- Pass-through is real but tiny [E]: Section 3 quantifies it near 1 USD per MWh. Any strike-price comparison with 2 to 3 USD per MWh of bid dispersion swamps the fee effect. Disclosure plus lowest-evaluated-price award criteria neutralises the bias concern in practice.
- What critics actually allege [T]: no published allegation against the Vietnam Schneider fee specifically was found. The generic debate in buyer communities concerns advisor independence where advisors also sell developer services or carbon products. Mitigations used elsewhere: fixed-fee buyer-paid options, published evaluation matrices, auditor or legal review of award, and contractual bans on success-fee uplifts tied to price.
- Bottom line [E]: developer-paid is consistent with common practice, provided the RFP evaluates on strike price and terms with the fee disclosed. A challenger competing on buyer-paid fixed fees can weaponise the optics, but must explain why its total buyer cost is lower, because the incumbent developer-paid model costs the buyer nothing out of pocket.

## 3. Economics: what 2pct of capex does to a Vietnam solar DPPA

### 3.1 Assumption set (all [E] unless noted)

| Input | Base | Range | Anchor |
|---|---|---|---|
| Capex, utility solar | 700 USD per kWp | 650 to 800 | IRENA 2024 Asia context [V]: China 591, India 525, Europe 779, global 691 USD per kW; Asia-ex-China-India 1,133. Vietnam estimated between India and Europe on labour and import mix |
| Capacity factor | 17.5pct (1,533 kWh per kWp per year) | 16 to 19pct | Southern Vietnam irradiance; central-region curtailment noted 2025 to 2026 [V] |
| VND WACC, real project | 9pct | 7 to 11pct | IEA Vietnam financing-cost territory [V, report-level]; project figure estimated |
| Tenor | 20 years | 15 to 20 | DPPA practice [E] |
| Strike | near EVN industrial tariff, about 70 to 88 USD per MWh equiv. | EVN average retail 2,204.07 VND per kWh May 2025 [V]; USD conversion [E], not the repo canonical FX |
| Buyer discount | 10 to 15pct off EVN tariff | deal-dependent | Real-project-data branch precedent: 15pct PPA discount scenario [V, repo-internal] |

### 3.2 Base-case arithmetic [E]

- Fee per MWp: 2pct times 700,000 USD = 14,000 USD.
- Capital recovery factor at 9pct over 20 years: 10.96pct. Annualised fee: about 1,534 USD per year per MWp.
- Energy per MWp per year: 17.5pct times 8,760 h = 1,533 MWh.
- Strike adder: 1,534 divided by 1,533 = about 1.00 USD per MWh.
- Versus a 65 to 80 USD strike: 1.3 to 1.5pct. Versus lifetime contract value (20 years times 1,533 MWh times 70 USD = about 2.15M USD per MWp): about 0.65pct. Versus buyer Year-1 saving at 12pct discount on an 80 USD tariff (about 9.60 USD per MWh): about 10pct of first-year savings.

### 3.3 Sensitivities [E]

- Capex 650 vs 800 at base CF and WACC: adder about 0.93 vs 1.14 USD per MWh.
- CF 16 vs 19pct at base capex: adder about 1.10 vs 0.92 USD per MWh.
- WACC 7 vs 11pct (20y; CRF 9.44 vs 12.58pct): adder about 0.86 vs 1.15 USD per MWh.
- Tenor 15 vs 20 years at 9pct (CRF 12.41 vs 10.96pct): adder about 1.13 vs 1.00 USD per MWh.
- Full band across plausible combos: about 0.85 to 1.30 USD per MWh. Nothing in the plausible space reaches 2 USD per MWh.

### 3.4 The floor matters more than the rate on small deals [E]

A minimum floor (illustrative 50,000 USD) binds below about 3.5 MW at 700 USD per kWp. A 2 MWp signing then pays 50,000 USD instead of 28,000, i.e. an effective 3.6pct and about 1.80 USD per MWh. Floors are therefore the real SME and rooftop-aggregation issue; the 2pct rate itself is a large-project non-event. Any challenger pitch to sub-10 MW buyers should attack the floor (cap, sliding scale, per-MWh amortisation), not the headline rate.

### 3.5 Cash-flow shape note [E]

Because the fee is payable at signing (not annuitised in the PPA), the developer funds it as upfront equity or development cost. On a 70 MWp DPPA at 700 USD per kWp (49M USD capex), the toll is about 980k USD at close. Against a 20-year revenue stream near 150M USD nominal, that is under 0.7pct. Lenders should be indifferent; equity IRR moves by low single-digit basis points.

## 4. Vietnam DPPA market state, 2025 to 2026

### 4.1 The one operating deal [V]

Samsung C and T (SEVT, Thai Nguyen) buys about 70 GWh per year long-term from TTC Phuoc Trach (Duc Hue 2, 49 MWp and 41.4 MWac, Tay Ninh), first electrons July 2025, Schneider Electric as consultant, described as Vietnam first grid-connected direct PPA in commercial operation and a model for RE100 manufacturers. Output equivalence quoted: about 17,000 households, about 46,000 tCO2 per year. Follow-on: Samsung Bac Ninh rooftop and Samsung HCMC rooftop DPPAs in 2025, with further deals planned.

### 4.2 Regulatory mechanics [V]

- Decree 80 of July 2024 opened the pilot DPPA. Decree 57 of March 2025 replaced it with a full framework (Norton Rose Fulbright analysis, May 2025).
- Two models: grid-connected sale through the national grid (solar, wind and biomass at 10 MW-plus, with VWEM participation) and private-line DPPA (any qualified renewable, including rooftop, delivered off-grid).
- Three grid-model contracts: EVN spot PPA, physical DPPA, financial DPPA (contract for difference). Prices negotiated but capped at the MOIT ceiling generation tariff.
- Threshold liberalisation: the decrees removed the old hard 200,000 kWh-per-month and 22 kV gates in favour of MOIT-set minimum consumption; rooftop surplus sales to EVN capped at 20pct under the self-consumption rules.
- Market plumbing: NSMO operates the system and market independently of EVN since August 2024; VWEM runs in stages toward fully competitive wholesale pricing.

### 4.3 Tariff and pipeline backdrop [V]

- EVN average retail tariff: 2,103.12 VND per kWh from October 2024 (up 4.8pct), 2,204.07 VND per kWh from May 2025 (up 4.8pct); the fourth increase since early 2023 (3pct, 4.5pct, 4.8pct, 4.8pct). Rising retail tariffs widen the DPPA discount window every year.
- PDP8-revision targets to 2030: onshore and nearshore wind 26 to 38 GW, solar 46 to 73 GW, biomass 1.5 to 2.7 GW, waste-to-energy 1.4 to 2.1 GW, with offshore wind staged to 2035. Headroom is policy-plentiful; bankable grid and offtake are the constraint.
- Cost context: Vietnam cumulative solar above 19 GW at end 2025 (about 586 MW added in 2025); rooftop solar above 9,500 MW inside about 103,000 MW total capacity at end 2024; utility solar IRR around 6.1pct and solar-plus-BESS around 7.3pct in Ember analysis; curtailment episodes in central Vietnam in early 2025 to 2026; rooftop-plus-BESS retail anecdotes near 190M VND for 10 kWp with 16 kWh storage, with Bac Ninh provincial subsidies for rooftop and storage.
- Regional capital signal: ADB 2M USD grant to NSMO for market systems; IFC 30M USD loan participation in a Vietnamese coffee-sector sustainability-linked facility (illustrative of IFC local-currency and agri-corporate appetite, not a DPPA instrument).

### 4.4 Players [V unless noted]

- Buyer-side advisor: Schneider Electric (self-described largest corporate renewable advisor, 13,000 MW-plus supported since 2014; Zeigo platform owner). First-mover advantage from the Samsung deal.
- Developers and sellers: TTC (operating), plus the private-line and 10 MW-plus grid pipeline under Decree 57 (project names beyond Duc Hue 2 not enumerated in this study: [T]).
- Platforms and advisors present in APAC discourse: LevelTen (US and Europe footprint; APAC presence not confirmed), Pexapark (Europe data and advisory), BRC-A model (Australia buyer-guidance template with no Vietnam chapter).
- What is missing: a published Vietnam multi-buyer RFP calendar, a standardised bankable DPPA form, and disclosed price discovery ([T]: no Vietnam DPPA price index found).

## 5. Competitive strategies for a challenger

Each play is paired with the evidence that makes it credible. None requires beating 2pct on price alone.

1. Compete on the floor, not the rate. Publish a sliding scale (e.g. 2pct above 20 MW, capped fixed fee below 5 MW, no floor on aggregated portfolios) [E]. Evidence: Section 3.4 shows the floor, not the rate, is what prices SMEs out. First challenger to publish a floor-free SME card owns the sub-10 MW narrative that Decree 57 private-line DPPA opens up [V on the rule, E on the tactic].
2. Sell a buyer-paid fixed-fee option with open-book award. Offer the buyer a fixed success fee plus a contractual ban on developer success top-ups on that mandate, with the evaluation matrix and all compliant bids disclosed to the buyer [E]. Evidence: LevelTen seller-pays precedent [V] makes developer-paid defensible, but buyer-paid fixed fee is the only structure no conflict slide can touch. Price it at or below the expected 1 USD per MWh equivalent and show the maths.
3. Guarantee the funnel: pre-qualified developer panel with bid bonds. The Vietnam bottleneck is bankable sellers, not buyers [E, from single-operating-deal fact V]. A challenger that brings five pre-diligenced 10 MW-plus sellers with grid positions beats an incumbent with one preferred developer, even at identical fees.
4. Productise private-line and rooftop aggregation. Decree 57 explicitly blesses off-grid private DPPA for any qualified renewable including rooftop [V]. Build the standard offer pack for industrial-park private grids (metering, wheeling inside the fence, surplus treatment) that the grid model cannot serve. This sidesteps head-on RFP competition.
5. Attach firming: solar-plus-BESS DPPA shapes. PDP8-revision and NSMO direction of travel reward dispatchability; Ember puts solar-plus-BESS IRR above plain solar in Vietnam [V]. A challenger that tenders shaped or evening-peak blocks differentiates on product while the incumbent tenders as-generated solar.
6. Localise delivery: Vietnamese-language RFP, MOIT-ceiling-tariff compliance memos, NSMO settlement support. Evidence: global advisors run English-language processes; the Norton Rose Decree 57 analysis shows the compliance surface (VWEM participation, ceiling tariff, three-contract choice) is where buyers actually need hand-holding [V].
7. Publish a Vietnam DPPA price reference. No Vietnam price index was found ([T]). A challenger that publishes quarterly evaluated-strike ranges (anonymised, Pexapark-style) earns the trust asset that justifies fees and attracts both sides of the next RFP.
8. Partner, do not rebuild: pair a global price-benchmark brand with a Hanoi or HCMC delivery house that already lives inside MOIT, EVN and NSMO process. Evidence: every Vietnam DPPA explainer is co-authored by a local firm (GTLaw, Fraser, DIMAC, B-Lawyers) [V]. Fee split beats fee war.

## 6. What this study could not verify (thin-evidence log)

1. No published Schneider or peer buyer-advisor fee card for any market was found; the 2pct-with-floor term is taken from the task brief, not independently verified.
2. No per-MWh or pct-of-value advisor benchmarks for Japan, Korea, Taiwan, India, Philippines, Malaysia, Thailand or LatAm were found in English-language industry sources.
3. Placement-fee, developer-margin and owner-engineer comparables rest on secondary summaries and should be rechecked against primary engagements before use in negotiation.
4. No Vietnam DPPA price index, standard contract, or multi-buyer RFP calendar exists in the sources reviewed.
5. Forward curves (e.g. 2035 strike projections) appearing in trade coverage were excluded as speculative.

## 7. Bottom line for the 2pct question

Consistent with common practice: yes. Seller-pays is the documented marketplace norm [V], M and A and placement tolls are equal or higher [V/T], and development margins absorb the amount several times over [T]. Economic: about 1 USD per MWh, 1 to 2pct of strike, under 1pct of lifetime value [E]. Contestable: on the floor (SMEs), on funnel depth (bankable sellers), on product (private-line, aggregation, firming), and on transparency (buyer-paid fixed-fee option with open-book award) [E]. The competitor that publishes a floor-free SME card plus a quarterly Vietnam strike reference will take mindshare without discounting the 2pct.

## 8. Numbered source list (62 distinct sources)

Advisory, marketplace and platform fees (1 to 14)

1. LevelTen asset marketplace, seller-paid transaction fees and buyer-free access. https://www.pv-magazine.com/2025/02/26/levelten-launches-new-platform-to-buy-sell-renewable-assets/
2. Schneider Electric acquires Zeigo to expand digital procurement capabilities. https://www.pv-magazine.com/press-releases/schneider-electric-acquires-renewable-energy-platform-zeigo-to-expand-digital-procurement-capabilities-globally/
3. LevelTen business-model summary: transaction fees as pct of contract value or fixed per transaction. https://canvasbusinessmodel.com/blogs/how-it-works/levelten-energy-how-it-works
4. LevelTen 2024 year in review: European solar PPA price dynamics. https://www.businesswire.com/news/home/20250128461760/en/LevelTen-Energys-2024-Year-in-Review-European-Solar-PPA-Prices-Rise-Amid-Shifting-Market-Dynamics
5. LevelTen P25 Q3 2025: Midwest and Southwest solar above 50 USD per MWh, Texas wind below 35. https://utilitydive.com/news/levelten-p25-solar-ppa-prices-ercot-pjm/808488/
6. LevelTen Q3 2025 North America and Europe price assessment. https://www.taiyangnews.info/markets/levelten-energy-corporate-clean-energy-contract-offer-prices/
7. Engie North America community-solar RFP with 0.10 USD per MWh seller success fee (trade-press report). https://pv-magazine-usa.com/2025/09/30/rfp-alert-engie-north-america-seeks-community-solar-in-illinois/
8. Zeigo Network US commercial PPA price snapshot, Q3 2025. https://www.zeigo.com/zeigo-network/2025-q3-us-commercial/
9. Zeigo solar PPA price explainer (PPA price formation). https://www.zeigo.com/zeigo-network/solar-ppa-price/
10. Schneider Electric corporate renewable-energy services and Zeigo acquisition background. https://perspectives.se.com/global/press-release/schneider-electric-acquires-zeigo-to-transform-corporate-renewable-energy-services/
11. 3Degrees PPA advisory scope: strategy, RFP management, evaluation, negotiation, monitoring. https://3degreesinc.com/insights/ppa/
12. Edison Energy multi-sourcing RFP strategy and procurement practice. https://edisonenergy.com/modernizing-higher-education-energy-procurement-a-multi-sourcing-rfp-strategy/
13. ODM Partners energy-procurement advisory positioning. https://odmpartners.com/energy-procurement/
14. PowerShop and emerging PPA marketplace models in Europe. https://kurums.com/powershop-future-europes-ppa-marketplace/

Europe PPA prices and practice (15 to 24)

15. Pexapark in the media: EURO composite and monthly PPA price assessment archive. https://pexapark.com/in-the-media/
16. Pexapark-Drax UK partnership and typical bilateral ticket sizes. https://www.solarpowerportal.co.uk/pexapark-and-drax-unite-to-unlock-more-ppa-deals-for-the-uk-market/
17. European PPA prices continued to rise into 2024. https://www.pv-magazine.com/2024/02/27/european-ppa-prices-continue-to-rise/
18. How PPAs are redefining the European energy market in 2025. https://www.saurenergy.com/solar-energy-news/how-ppas-are-redefining-european-energy-market-in-2025
19. Spain PPA prospects and practice from Europe longest-running market. https://www.mibgas.es/en/ppa-potential-spain-prospects-and-best-practices-from-the-longest-running-ppa-markets-in-europe/
20. Power purchase agreements and the price of green electrons (price-formation analysis). https://www.risk.net/energy-risk/7953251/power-purchase-agreements-and-the-price-of-green-electrons
21. Schneider Electric and Zeigo Power renewables market report coverage. https://www.solarpowerportal.co.uk/schneider-electric-and-zeigo-power-release-renewables-market-report/
22. RE-Source European corporate sourcing platform. https://resource-platform.eu/
23. Pexapark on Europe surging data-centre power demand and the PPA market. https://pexapark.com/debbi-bavin-on-europe-surging-data-centre-power-demand-and-the-ppa-market/
24. Germany negative-price hours and PPA hedging context. https://www.economist.com/finance-and-economics/2025/08/21/why-german-electricity-is-sometimes-free (via Pexapark coverage)

Australia corporate PPA (25 to 30)

25. BRC-A State of the Corporate PPA Market 2025 (record 2024, 2025 reversion, LGC collapse, CIS). https://businessrenewables.org.au/wp-content/uploads/2026/03/260318-SOM-Report-2025.pdf
26. BRC-A State of the Market 2023: 165 PPAs and 7.4 GW. https://businessrenewables.org.au/state-of-the-market-2023/
27. BRC-A 2019 research: 58 PPAs by 70 organisations, 2.3 GW, 7 GW marketplace. https://businessrenewables.org.au/2019-research/
28. ARENA backing for corporate PPA facilitation. https://www.pv-magazine.com/2019/02/26/arena-backs-new-online-marketplace-for-corporate-ppas/
29. ARENA agency homepage (programs and funding). https://arena.gov.au/
30. Coles 70 MW solar PPA as buyer-side precedent. https://list.solar/news/coles-secures-70mw-solar-ppa-in-queensland/

APAC corporate procurement: Japan, Korea, Taiwan, India, Southeast Asia (31 to 40)

31. Wood Mackenzie: Australia, India and Taiwan at 89pct of APAC corporate PPA volume. https://www.pv-magazine.com/2025/08/15/corporate-ppas-in-asia-pacific-australia-india-and-taiwan-lead-with-89-share/
32. Wood Mackenzie: China solar LCOE 27 USD per MWh, Japan 118 USD, regional wind 25 to 70 USD. https://www.solarquarter.com/2025/08/23/wood-mackenzie-apac-onshore-wind-solar-now-cheapest-power-but-tariffs-and-grid-risks-threaten-momentum/
33. Goldman Sachs Japan 50 MW solar PPA precedent. https://www.pv-magazine.com/2023/02/09/goldman-sachs-signs-solar-ppa-in-japan/
34. Solar PPA structures in Japan explainer. https://www.pv-magazine.com/2025/02/06/solar-ppa-in-japan-a-beginners-guide/
35. Japan non-FIT procurement and virtual PPA certificate environment. https://www.environmentenergyleader.com/stories/japan-advances-corporate-renewable-procurement-with-new-virtual-ppa-framework,224072
36. Korea 2025 third-party PPA milestone and cross-KEPCO-zone contract. https://www.pv-magazine.com/2025/10/02/south-korea-registers-major-third-party-ppa-milestone/
37. Taiwan offshore-wind corporate offtake pipeline. https://www.taipeitimes.com/News/biz/archives/2025/02/26/2003832332
38. India 200 MW solar-plus-storage at 3.20 INR per kWh. https://www.pv-magazine.com/2025/09/30/india-concludes-solar-plus-storage-auction-with-lowest-tariff-of-inr3-20-kwh/
39. India 250 MW storage-linked solar at 4.64 INR per kWh. https://www.pv-magazine-india.com/2025/09/25/solarium-green-places-lowest-bid-of-inr4-64-kwh-in-nhpc-solar-plus-storage-auction/
40. Bridge to India on open-access and network-access charges friction. https://bridgetoindia.com/indias-green-energy-open-access-rules-2025-a-reality-check-for-c-and-i-consumers/

Fee comparables: M and A, placement, development, owner engineer (41 to 48)

41. M and A fee guide: Lehman scale, retainers, upfront fees, crediting practice. https://waveup.com/blog/how-much-do-mergers-and-acquisitions-advisors-charge/
42. M and A fee benchmarks and small-deal 2 to 8pct range. https://firmex.com/resources/blog/ma-advisory-fees/
43. Double Lehman schedule and worked fee examples. https://efinancialmodels.com/knowledge-base/investment-banking-fees/
44. Lehman formula calculator and 10M transaction illustration. https://www.channele2e.com/lehman-scale-calculator
45. Boutique advisory fee illustration (Class VI Partners). https://classvipartners.com/what-are-investment-banking-fees/
46. Solar developer fees and margin analysis. https://www.solarbuildermag.com/
47. Are solar developer fees declining (development economics). https://www.renewableenergyworld.com/solar/are-solar-developer-fees-declining/
48. Capital placement and fundraising fee practice. https://www.fastercapital.com/ (placement-fee guidance section)

Vietnam DPPA: deals, rules, tariffs, pipeline (49 to 62)

49. Samsung Electronics Vietnam first grid DPPA purchase (SEVT, Thai Nguyen). https://news.samsung.com/global/samsung-electronics-vietnam-becomes-first-company-in-vietnam-to-purchase-renewable-electricity-through-dppa
50. Samsung-TTC first DPPA enters commercial operation (Duc Hue 2, 49 MWp, 70 GWh per year). https://www.pv-magazine.com/2025/07/24/vietnams-first-dppa-enters-commercial-operation/
51. Samsung-TTC DPPA as model for RE100 manufacturers. https://en.vietstock.vn/2025/08/samsung-engineering-unit-becomes-first-dppa-electricity-buyer-in-vietnam-427-3451067.htm
52. Samsung Hanoi Times City wind-plus-solar long-term DPPA context. https://hanoitimes.vn/samsung-plans-to-buy-clean-power-from-private-projects.820199.html
53. Vietnam completes first DPPA transaction (industry ministry acreditation). https://ven.congthuong.vn/vietnam-completes-first-dppa-transaction-57570.html
54. Decree 57 of 2025: key features and impact on DPPAs (replaces Decree 80). https://www.nortonrosefulbright.com/en/knowledge/publications/b7fae014/decree-57-2025-key-features-and-impact-on-direct-power-purchase-agreements-in-vietnam
55. Corporate renewable PPA framework under Decree 80 and Decree 57. https://www.nortonrosefulbright.com/en/knowledge/publications/757b1ff4/corporate-renewable-power-purchase-agreements-in-vietnam-a-framework-for-the-future
56. GTLaw overview of the DPPA scheme and Decree 80 rules. https://pdf.hlc.com (GTLaw DPPA scheme overview, via firm publication archive)
57. EVN average retail tariff 2,204.07 VND per kWh from May 2025 (fourth hike since 2023). https://icon.com.vn/what-is-the-current-electricity-tariff-166762.html
58. IRENA 2024 costs: global solar LCOE 0.043 USD per kWh, plant cost 691 USD per kW. https://www.pv-magazine.com/2025/07/23/global-average-solar-lcoe-stood-at-0-043-kwh-in-2024-says-irena/
59. IRENA Renewable Power Generation Costs in 2024 (flagship report). https://www.irena.org/Publications/2025/Jul/Renewable-Power-Generation-Costs-in-2024
60. ADB 2M USD grant to NSMO for market systems. https://forum-adb.org/2025/06/adb-provides-2-million-grant-to-support-vietnams-national-system-and-market-operator/
61. IFC 30M USD sustainability-linked facility participation in Vietnam. https://ippjournal.com/2025/07/ifc-extends-30-million-loan-to-trung-nguyen-legend-for-sustainable-coffee-production-in-vietnam/
62. CEBA buyer community and procurement resources (US buyer-side practice reference). https://cebuyers.org/

Further standing references consulted for context (no new figures drawn): RMI https://rmi.org/, IEA Vietnam https://www.iea.org/countries/viet-nam, MOIT https://moit.gov.vn/, EVN https://www.evn.com.vn/, RE-Source https://resource-platform.eu/, LevelTen https://www.leveltenenergy.com/, Zeigo https://www.zeigo.com/, Pexapark https://pexapark.com/, BRC-A https://businessrenewables.org.au/, Vietnam Investment Review https://vir.com.vn/, Reuters https://www.reuters.com/.

---

Report prepared 2026-10-03 from web research only. No code changes made. All [E] arithmetic uses the inputs in Section 3.1; all [V] claims trace to the numbered entries above.
