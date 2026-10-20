{
  "title": "Investment framework"
}

# Derek's Investment Framework

**Version 5.2 Provisional | September 24, 2026**

V5 is a value-first framework for growth and innovation investing. Valuation and business evidence decide whether an investment deserves capital and how much. Technical analysis helps time and pace execution; it does not define conviction.

The numerical thresholds are provisional pending native V5 three-, six-, and twelve-month outcomes. The required 60-day migration replay is documented in `docs/Framework-V5-Provisional-Audit-2026-08-21.md`. V4.6 is preserved at `Archive/2026-08/DerekInvestmentFramework-V4.6-2026-08-24.md`; V5.0 is preserved at `Archive/2026-08/DerekInvestmentFramework-V5.0-2026-08-26.md`; V5.1 is preserved at `Archive/2026-09/DerekInvestmentFramework-V5.1-2026-09-24.md`.

V5.2 makes the V5.1 controls executable. It separates security qualification from portfolio authorization; gives operating companies and investment vehicles distinct analysis paths; defines planned, current, binary-gap, passive-sleeve, sector, and correlated risk; repairs the protected-profit floor; applies business-quality gates to every build and deteriorating holding; and adds the structured evidence required to audit the rules. V5.2 does not raise a risk ceiling merely to fit an inherited portfolio. Every new numeric threshold below remains provisional under the calibration governance in §15.

---

## Version history

| Version | Key change |
|---|---|
| V1–V3 | Fundamental, technical, macro, and industry foundations |
| V4.0–V4.6 | Sentiment, pre-profit and binary-event gates, growth architecture, catalyst reviews, and audit governance |
| **V5.0 Provisional** | **Valuation-first conviction score; technical timing separated from conviction; valuation-led pullback starters; mechanical valuation trims and protected-profit floors; diagnosis-first sector shocks; current-data and brokerage-state controls** |
| **V5.1 Provisional** | **Minimum business-quality gate and deep-value exception (value-trap protection); scenario-probability discipline and reverse-DCF check; margin-of-safety rubric; valuation override for scaling; conviction score given an operational role; portfolio open-risk budget; peak-anchored profit floor; pre-declared promotion criteria** |
| **V5.2 Provisional** | **Company/vehicle branches; two-phase security and portfolio authorization; active-risk and passive-sleeve separation; gap-aware sizing; measurable concentration; repaired profit floors; structured decision cohorts and promotion audit** |

---

## 1. Governing principles

1. **Valuation and fundamentals decide WHAT to own and the maximum exposure.**
2. **Technicals decide WHEN and HOW FAST to enter or reduce.**
3. Weak technicals may restrict scaling but cannot block a valuation-qualified starter.
4. Strong technicals cannot justify buying above the entry ceiling or delaying a mandatory valuation trim.
5. Thesis failure and credibility risk override price, score, and technical strength.
6. Macro conditions modify portfolio risk; they are not a blanket stock-selection veto unless they directly damage the thesis or valuation assumptions.
7. Every price-based trigger uses a **daily closing breach** unless explicitly labeled otherwise. Thesis-breaking news or a credibility event may require immediate action.
8. Recommendations are analytical instructions, not evidence that a brokerage trade occurred.

### Decision hierarchy

```text
Macro context /25                   portfolio-risk modifier
        ↓
Instrument branch                   operating company or investment vehicle
        ↓
Company: industry /20 + fundamentals /30 + valuation /30
Vehicle: mandate, look-through, valuation, structure, overlap, and role cap
        ↓
Catalysts and narrative             secondary evidence
        ↓
Credibility or vehicle-integrity gate
                                      pass / pending / fail
        ↓
Technical timing /25                entry and exit pacing only
        ↓
Position size, action, and monitoring map
```

---

## 2. Required analysis sequence

Every ticker review must first classify the instrument as `OPERATING_COMPANY`, `BROAD_MARKET_CORE`, `SECTOR_OR_FACTOR_FUND`, or `CONCENTRATED_THEMATIC_FUND`, then complete the applicable path in order:

1. Macro context and direct transmission to the company or vehicle
2. Industry structure and cycle
3. Company path: business, financial health, growth architecture, and management; vehicle path: mandate, index or manager process, holdings, fees, liquidity, tracking, counterparties, and look-through overlap
4. Company path: bear/base/bull intrinsic valuation; vehicle path: look-through valuation and allocation/cap test
5. Risk, thesis invalidation, and the applicable credibility or vehicle-integrity gate
6. Catalysts and ordinary narrative
7. Technical timing and structural levels
8. Security-level signal, position sizing, staged action, buy map, and sell map
9. Portfolio authorization by the portfolio-review orchestrator for every risk-increasing action

If the valuation predates the latest earnings release or a material company event, the action is **Pending Refresh**. An unconditional `Buy Starter` or `Add` is prohibited until valuation is refreshed.

---

## 3. Macro environment — separate `/25`

Score each factor `/5`:

| Factor | Core question |
|---|---|
| Interest rates | Does the cost and direction of capital support the valuation? |
| Inflation | Does inflation strengthen or pressure demand, margins, and multiples? |
| Liquidity | Is capital flowing into or out of risk assets? |
| Economic cycle | Is the company cyclical, secular, or exposed to recession risk? |
| Geopolitics and policy | Is policy a direct tailwind, headwind, or existential risk? |
| **Macro score** | **`/25`** |

### Macro sizing bands — provisional

| Macro score | Treatment |
|---:|---|
| `18–25` | Normal position limits |
| `12–17` | Cap planned size at 75% of normal |
| `0–11` | Cap at 50%; starter/add stages only |
| Any score with direct thesis damage | No entry; refresh valuation and thesis |

Market direction is reported, but it does not create a second multiplier that duplicates the macro score. A market correction may improve valuation while reducing permitted size.

---

## 4. Industry quality — `/20`

| Component | Weight | Questions |
|---|---:|---|
| Structural demand and market growth | `/6` | Is demand durable, growing, and supported by observable adoption? |
| Industry-cycle position | `/5` | Early, accelerating, mature, oversupplied, or declining? |
| Competitive structure and pricing power | `/4` | Can participants earn excess returns without commoditization? |
| Supply-chain, geopolitical, and regulatory resilience | `/3` | What can interrupt production, access, or economics? |
| Industry-wide earnings revisions | `/2` | Are estimates and order expectations improving or deteriorating? |
| **Industry quality** | **`/20`** | |

An industry score informs conviction. It blocks capital only when the industry thesis is deteriorating enough to invalidate the company valuation or when a hard sector exposure limit is reached.

---

## 5. Fundamentals — `/30`

| Component | Weight | Evidence required |
|---|---:|---|
| Revenue, earnings, and estimate trajectory | `/8` | Multi-period growth, guidance, revisions, and earnings quality |
| Competitive position and business quality | `/8` | Moat, switching costs, differentiation, customer value, and durability |
| Cash flow and balance-sheet strength | `/7` | FCF quality, liquidity, leverage, dilution needs, and runway |
| Management execution and capital allocation | `/4` | Delivery versus promises, incentives, acquisitions, buybacks, and financing |
| Evidence supporting the central thesis | `/3` | Concrete proof points rather than narrative extrapolation |
| **Fundamentals** | **`/30`** | |

### Growth architecture — required, unscored detail

Document revenue by product and end market, supply-demand constraints, technology transitions, cannibalization, vertical integration, customer concentration, and the path from current results to the forecast. This evidence feeds both fundamentals and valuation; it is not an extra score.

### Pre-profit and binary-event safeguards

- Pre-profit, negative-gross-margin, going-concern, and heavy-dilution names retain hard exposure caps.
- A HIGH binary event must be sized using plausible gap loss because a stop may not execute.
- Maximum accepted loss from a plausible overnight gap should remain below 1% of portfolio value.
- Earnings dates must be labeled `CONFIRMED`, `LIKELY`, or `UNCONFIRMED`; uncertainty increases binary risk.

### Minimum business-quality gate — value-trap protection (provisional)

A low price is not a thesis. Because V5 lets valuation upside authorize a starter, the fundamentals score carries a hard floor so a cheap, structurally deteriorating business cannot qualify on price alone:

| Fundamentals `/30` | Capital and holding treatment |
|---:|---|
| `≥15` | Eligible for starter or build on the other valuation, risk, credibility, technical-stage, and portfolio rules |
| `10–14` | Eligible only under the **deep-value exception** below and capped at starter size |
| `<10` | No new capital. Unheld names are `Watch` or `Avoid`; held names require an immediate thesis review and either `Exit` or a time-limited `Pending Refresh` |

**Deep-value exception** (all required to build a `10–14` name to starter):

1. Balance-sheet survivability: positive free cash flow **or** a fully funded runway of at least 18 months, with no going-concern flag and no forced/heavy dilution assumed in the base case.
2. Credibility gate `PASS`.
3. The bear case is documented as a valuation/cyclical drawdown, **not** a structural business-quality break (declining moat, share loss, or secular demand loss). A quality break is a thesis failure, not a discount.

The gate is re-evaluated before **every** build and after every material fundamental event. The exception raises size discipline, not conviction: a deep-value position is capped at the starter stage until fundamentals recover above `15`. A held `<10` name may remain `Pending Refresh` for no more than one ordinary review cycle only when the deficiency is explicitly missing or stale evidence rather than demonstrated structural deterioration; no capital may be added during that interval. Document the gate result, exception result, and reason explicitly.

---

## 6. Valuation and vehicle analysis

### Operating-company valuation — `/30`

For `OPERATING_COMPANY` analyses, valuation is mandatory and explicit. Relative multiples and analyst targets are supporting evidence, not substitutes for intrinsic-value scenarios.

### Scenario model

| Scenario | Operating assumptions | Probability | Fair value |
|---|---|---:|---:|
| Bear | Demand, margins, execution, and multiple downside | `__%` | `$__` |
| Base | Most probable operating path | `__%` | `$__` |
| Bull | Credible upside with stated dependencies | `__%` | `$__` |
| **Probability-weighted fair value** | `Σ(probability × fair value)` | **100%** | **`$__`** |

Every scenario must name the revenue/earnings basis, margin assumption, valuation method, discount rate or multiple, time horizon, and failure conditions. Fair value changes only when documented assumptions change. Price momentum and analyst target increases alone cannot raise fair value.

### Scenario probability discipline (provisional)

Probability-weighted fair value is only as honest as its weights. Because a single inflated bull weight can manufacture any fair value, the distribution is constrained:

- The **base case must carry the single highest weight**. If the bull or bear case is the modal outcome, that case is the base case — relabel it.
- **Bull weight `≤35%`** unless exceptional, documented, near-term evidence justifies more; state the evidence explicitly.
- **Bear weight `≥15%`** for any pre-profit, going-concern, high-dilution, or HIGH-binary name.
- Any weight outside these bounds requires a one-line written justification in the analysis body.

### Reverse-DCF / "what is priced in" check — required

Before recommending capital, state what the **current price** already implies (implied revenue CAGR, terminal margin, or exit multiple via a reverse-DCF or reverse-multiple). If the priced-in path is at or beyond the bull case, the name is not a value-first buy regardless of the weighted fair value — flag it and withhold new capital. This check guards against scenario sets that quietly assume the bull outcome.

### Valuation score

| Component | Weight | Guide |
|---|---:|---|
| Upside to probability-weighted fair value | `/12` | `≥50%: 12`; `35–49%: 10`; `25–34%: 8`; `15–24%: 6`; `0–14%: 3`; `<0%: 0` |
| Reward/risk at proposed entry | `/8` | `≥3:1: 8`; `2.5–2.99: 7`; `2–2.49: 6`; `1.5–1.99: 4`; `1–1.49: 2`; `<1:1: 0` |
| Margin of safety under the bear case | `/6` | Bear-case permanent-loss downside from proposed entry: `<10%: 6`; `10–19%: 4`; `20–29%: 2`; `≥30%: 0`. Weight toward the bear probability; score permanent impairment, not normal volatility |
| Confidence in valuation inputs | `/4` | Fresh audited results, stable model, scenario evidence, and limited unsupported assumptions |
| **Valuation** | **`/30`** | |

### Required valuation outputs

- Bear, base, bull, and probability-weighted fair values
- Reverse-DCF / reverse-multiple statement of what the current price already implies
- Current upside/downside to each
- Starter zone, add zone, and full-position ceiling
- Tactical stop and fundamental invalidation conditions
- Reward/risk at each proposed entry
- Data and valuation dates

### Investment-vehicle path

Do not score a fund on company moat, switching costs, issuer earnings, management capital allocation, or an issuer DCF. Do not compare a fund's synthetic score with company conviction `/90`. Classify the vehicle role and report:

- Mandate, benchmark, index or manager process, rebalance cadence, inception, fee, AUM, median spread, and tracking evidence
- Look-through sector and correlated-sleeve exposures using dated holdings; when holdings are unavailable, use the most conservative defensible exposure and label it
- Top-ten concentration, single-name concentration, derivatives or swap exposure, counterparty risk, foreign-market timing, premium/discount behavior, and overlap with direct holdings
- Look-through valuation using aggregate earnings, cash-flow, yield, or constituent valuation evidence; label `CHEAP`, `FAIR`, `EXPENSIVE`, or `INSUFFICIENT`
- A **vehicle-integrity gate** of `PASS`, `PENDING`, or `FAIL` for mandate, sponsor, liquidity, tracking, disclosure, and counterparty concerns
- Portfolio role, applicable position cap, allocation/rebalance range, and incremental sector/correlation effect

`BROAD_MARKET_CORE` is governed by a predeclared portfolio allocation range and a provisional `30%` broad-equity stress loss rather than a tactical stop or company sell ladder. `SECTOR_OR_FACTOR_FUND` remains inside the active open-risk budget and has a provisional per-vehicle cap of `5%`. `CONCENTRATED_THEMATIC_FUND` remains inside the active and correlated-risk budgets, has a provisional per-vehicle cap of `3%`, and counts toward the speculative cap when its structure or holdings meet the speculative definition. These are maximums, not targets.

A fund trim must be attributable to an allocation cap, look-through valuation condition, material premium/discount, vehicle-integrity event, or predeclared rebalance rule. A fabricated company-style probability-weighted fair value is not a valid trigger.

---

## 7. Catalysts and ordinary narrative — `/10`

| Component | Weight |
|---|---:|
| Specific, time-bound company catalysts | `/4` |
| Analyst-estimate direction and supporting evidence | `/2` |
| Institutional positioning and capital flows | `/2` |
| Ordinary market narrative and sentiment | `/2` |
| **Catalysts and narrative** | **`/10`** |

Weak ordinary sentiment does not block a valuation-qualified starter. It may lower conviction, reduce size, or slow scaling.

### Credibility-risk gate — separate

Classify `PASS`, `PENDING`, or `FAIL`:

- Fraud or material accounting allegations
- Material insider dumping inconsistent with ordinary diversification
- Unexplained or repeated dilution that changes per-share economics
- Governance failure or management credibility collapse
- A thesis-damaging short report supported by verifiable evidence

`PENDING` prohibits new capital until investigated. `FAIL` prohibits entry and may require exit. A short report or social allegation is not automatically true; the gate evaluates evidence and management's response.

---

## 8. Technical timing — separate `/25`

| Component | Weight | Purpose |
|---|---:|---|
| Price structure and support quality | `/7` | Define accumulation zones, invalidation, and supply overhead |
| Long-term trend | `/6` | Establish primary trend without vetoing deep-value starters |
| Volume and selling-pressure behavior | `/5` | Distinguish orderly pullbacks from distribution |
| Relative strength versus sector and market | `/4` | Identify leaders and company-specific weakness |
| Short-term momentum | `/3` | Fine-tune execution; RSI/MACD have the smallest weight |
| **Technical timing** | **`/25`** | |

Technical scoring never changes fair value or underlying conviction. The single operative stage ladder, including the valuation override, is in §10; this section defines inputs only.

---

## 9. Conviction score — `/90`

```text
Conviction /90 = Valuation /30
               + Fundamentals /30
               + Industry quality /20
               + Catalysts and narrative /10
```

Macro `/25`, technical timing `/25`, and credibility risk are always reported separately.

High/Moderate/Low score bands are **display-only and provisional** until native V5 history supports calibration. Do not reuse V4.6 combined-score thresholds. The action follows explicit valuation, risk, credibility, macro-sizing, and technical-stage rules even when the headline score appears high.

Until the bands are calibrated, company conviction still has two operational jobs, so the `/90` is never merely decorative:

1. **Capital priority.** First exclude every name that fails a hard gate. Rank the remaining operating companies by conviction `/90`, then valuation `/30`, balance-sheet strength `/7`, and finally lower incremental open/correlated risk. Every section uses this same order. Investment vehicles are ranked only against vehicles serving the same portfolio role, using look-through valuation, vehicle integrity, overlap, cost, and incremental risk.
2. **Quality corroboration.** Conviction cannot by itself authorize an action, but the fundamentals `/30` inside it drives the §5 minimum business-quality gate. A high headline conviction built almost entirely on valuation upside with fundamentals below the §5 floor is a value-trap signature, not a buy.

---

## 10. Entry and position-building rules

### Standard actions

Use exactly one primary action per ticker:

`Buy Starter`, `Add`, `Hold`, `Trim`, `Exit`, `Watch`, `Avoid`, or `Pending Refresh`.

Every review also reports a **security-level signal** and a separate **portfolio authorization**. A ticker can be individually qualified while portfolio authorization is `BLOCKED_OPEN_RISK`, `BLOCKED_SECTOR_CAP`, `BLOCKED_CORRELATED_CAP`, `BLOCKED_UNKNOWN_RISK`, or `PENDING_ORCHESTRATOR`. Only `AUTHORIZED` permits a risk-increasing action. A standalone ticker review cannot authorize portfolio risk unless it receives a current orchestrator-owned risk ledger.

### Operating-company entry ladder — provisional

| Stage | Valuation and risk requirements | Timing requirements |
|---|---|---|
| **Starter — up to 25% of planned size** | One daily close in the predeclared accumulation zone; `≥25%` upside to probability-weighted fair value; reward/risk `≥2:1`; defined structural downside; thesis intact; credibility `PASS`; fundamentals `≥15/30` (or `10–14` under the §5 deep-value exception); price not beyond the reverse-DCF bull-implied level | No technical minimum |
| **Build to 50%** | `≥20%` upside; reward/risk `≥2:1`; thesis intact; credibility `PASS`; fundamentals `≥15/30` | Three sessions without a new low, improving selling volume, technical `≥8` |
| **Build above 50%** | `≥15%` upside; reward/risk `≥2.5:1`; thesis intact; credibility `PASS`; fundamentals `≥15/30` | Technical `≥12` plus support/MA reclaim |
| **Full planned size** | Still below full-position ceiling; reward/risk `≥2.5:1`; stop `≤15%` below entry; thesis intact; credibility `PASS`; fundamentals `≥15/30` | Technical `≥15` |

If price runs beyond the permitted entry zone, do not chase to complete the position.

Investment vehicles do not use this company ladder. They may receive capital only when the applicable look-through valuation, vehicle-integrity, role cap, allocation range, active-risk, sector, and correlated-sleeve tests pass. Technicals may pace an active vehicle entry but cannot cure an integrity or cap failure.

**Valuation override for build to 50% (provisional).** The build-to-50% technical `≥8`, three-session, and selling-volume requirements may be bypassed only when reward/risk to probability-weighted fair value is `≥4:1`, the thesis is intact, credibility is `PASS`, fundamentals are `≥15/30`, the reverse-valuation check passes, and portfolio authorization is `AUTHORIZED`. It never applies above 50%. Record every use explicitly.

### Tactical risk sizing

Separate two exits:

- **Fundamental invalidation:** thesis breaks; exit regardless of price.
- **Tactical risk stop:** daily close below predeclared structural support with a volatility allowance.

Distinguish entry planning from live portfolio risk. Use:

```text
stop distance = max((planned entry price − tactical stop) / planned entry price, 0)

effective entry-risk distance =
    max(stop distance, plausible overnight gap-loss %)   # HIGH binary
    stop distance                                         # otherwise

planned incremental risk = proposed incremental weight × effective entry-risk distance

stage position fraction = 0.25% portfolio risk / effective entry-risk distance
```

A wider valid stop or gap produces a smaller position. Do not tighten a structural stop or understate a gap merely to manufacture a larger position. After a tactical stop, do not average down; re-entry requires a fresh review, a new `setup_id`, and a new qualified setup.

Each stage may use at most roughly `0.25%` planned portfolio risk and a fully built company may use at most `1%` effective risk. For HIGH-binary names, gap sizing dominates whenever it is larger than stop sizing; four nominal stop-sized stages are not presumed safe. If the stage or full-position limit would be exceeded, reduce the target size.

### Pullback buy map

Every holding and qualified watchlist name must publish:

- Starter, add, and full-position zones
- Probability-weighted fair value and upside
- Tactical stop and thesis invalidation
- Permitted starter size, planned incremental risk, and plausible gap loss
- Sector priority rank
- Security-level signal and portfolio authorization

Refresh after earnings or material news, not because price alone changed.

---

## 11. Sector shocks and portfolio concentration

Three or more correlated holdings falling more than 5% in a week triggers diagnosis, not an automatic sector sale:

| Diagnosis | Action |
|---|---|
| Valuation/macro shock; industry thesis intact | Permit portfolio-authorized starters in the top two eligible names under the §9 priority rule; maximum combined new portfolio risk `0.50%` |
| Company-specific problem | Act only on that company |
| Industry thesis deterioration | Reduce the weakest exposure and block new starters |
| Unclear | Wait for one daily close while investigating; do not make a blanket trade |

Use the single §9 capital-priority rule; do not introduce a second ranking order here.

| Portfolio constraint | Maximum |
|---|---:|
| Single sector | 30% |
| Highly correlated exposure across sectors | 40% |
| Single stock | 15% after all modifiers |
| Combined speculative positions | 15% |
| **Active-sleeve effective open risk** | **8% (provisional)** |

Measure a direct operating company at 100% of its named primary sector. Measure funds by dated look-through weights. Correlated sleeves may cross formal sectors and use declared exposure coefficients; the coefficients, source date, and unknown balance must appear in the portfolio ledger. When look-through evidence is missing, use the most conservative defensible exposure and label it. Do not omit an exposure because it is held through a fund.

If a sector is already at its cap, a new starter requires a simultaneous reduction that leaves both sector and effective risk lower, or the starter waits. Maintain roughly 5% tactical liquidity in cash or cash equivalents when practical; this is a target, not a permanent minimum.

**Current active open risk.** Use current completed-close prices, current position market values, current portfolio NAV, and current tactical stops:

```text
current stop risk = position weight × max((current close − tactical stop) / current close, 0)

current effective risk =
    max(current stop risk, position weight × plausible gap-loss %)   # HIGH binary
    current stop risk                                                # otherwise

active-sleeve open risk = Σ current effective risk
```

`BROAD_MARKET_CORE` is excluded from the tactical 8% total only when explicitly designated as strategic core. It instead reports allocation-band status and `position weight × fixed policy stress loss`. Sector/factor and concentrated thematic funds remain in active open risk.

A missing stop is `UNKNOWN`, not zero. A close at or below an unresolved stop is `BREACHED`, not newly available capacity. Any non-core `UNKNOWN` or `BREACHED` holding blocks risk-increasing authorization until reconciled. The risk ledger must state its NAV date, price date, stop date, measured total, unknown weight, and coverage percentage.

When the active total reaches `8%`, no transaction may increase total effective risk. A simultaneous rotation is permitted only when post-trade active risk and every applicable concentration sleeve are lower. A legacy breach does not itself mandate a sale; existing valuation, thesis, credibility, vehicle-integrity, and stop rules govern reductions. The `8%` figure remains provisional and may change only through a dated §15 calibration, not because the inherited portfolio already exceeds it.

---

## 12. Exit and profit-protection rules

### Operating-company valuation sell ladder

| Condition | Target action |
|---|---|
| Price reaches probability-weighted fair value and remaining reward/risk is below `1:1` | Reduce position to 75% |
| Price exceeds probability-weighted fair value by more than 15% | Reduce position to 50% |
| Price reaches credible bull-case fair value and probability-weighted expected return is zero or negative | Exit |

Technical exhaustion may accelerate the next valuation step, but technical strength cannot delay it.

### Protected-profit floor

This rule applies to operating companies and active vehicles. `BROAD_MARKET_CORE` uses its allocation/rebalance policy unless the portfolio policy explicitly opts it into profit floors. Track current weighted-average cost, highest daily closing price while held, the prior absolute protected floor, and both current floor candidates. Adding shares may change average cost in either direction, but it may never lower the absolute protected floor. A full exit resets the state.

| Maximum gain reached using highest daily close | Minimum protected gain |
|---:|---:|
| `+20%` | `+10%` |
| `+30%` | `+18%` |
| `+40%` | `+24%` |
| `+50%` | `+30%` |
| `+60%` | `+37%` |
| `+75%` | `+45%` |
| `+100%` | `+60%` |

The cost-anchored floor is inactive below a `+20%` highest-close gain. Between table rows, linearly interpolate the protected-gain percentage. At or above `+100%`, use `+60%` until a later framework version declares additional rows.

**Peak-anchored give-back cap (provisional).** The peak floor becomes eligible only after the first `+20%` cost-gain row has activated and when 20-day ATR as a percentage of close is at least `4%`. The `4%` high-volatility threshold and the band below remain provisional and must be reported in sensitivity audits. Once activated, a later fall in ATR cannot lower the ratcheted floor.

```text
peak-anchored floor price = highest daily close × (1 − give-back band)
give-back band = clamp(12%, 2.5 × 20-day ATR%, 20%)

protected floor today = max(previous protected floor,
                            active cost-floor candidate,
                            active peak-floor candidate)
```

Candidate floors may change as cost or volatility changes; the stored absolute protected floor alone ratchets. Record the activation date, highest-close date, ATR date, cost candidate, peak candidate, prior floor, and governing floor.

- First daily close below the floor: set a target no greater than 75% of the reconciled shares held immediately before the first unresolved signal.
- Second consecutive close below the floor without reclaim: set a target no greater than 50% of that same signal-reference share count.
- If the position is already at or below the applicable target, do not create another trade.
- Profit-floor signals alone preserve a 50% target floor.
- Valuation, thesis failure, or a structural stop may reduce or exit that core.

### Non-stacking rule

Signals set a target position, not additive trade quantities. Normalize simultaneous signals to the same reconciled signal-reference share count; the lowest applicable target supersedes higher targets. Store the reference share count and unresolved target so later reviews do not issue duplicate catch-up trades.

### Re-entry after trims

Do not buy trimmed shares back automatically. Re-add only after:

1. A new valuation-qualified pullback, or
2. New company evidence raises probability-weighted fair value enough to restore reward/risk of at least `2:1`, or new vehicle evidence restores its look-through valuation and allocation eligibility.

---

## 13. Monitoring and execution controls

### Required buy and sell maps

Refresh both maps whenever valuation changes. A company sell map contains probability-weighted fair value, valuation trim levels, bull-case exit, protected-profit floor, tactical stop, and thesis-invalidating conditions. A vehicle map contains allocation/cap levels, look-through valuation state, integrity triggers, applicable active-risk controls, and any opted-in floor or tactical stop.

### Cadence

- Review the daily close when price is within 5% of a buy, trim, stop, or profit-floor trigger.
- Review weekly otherwise.
- Reassess fundamentals immediately after earnings or material news.
- Refresh full valuation after every earnings release and at least quarterly.
- Run a monthly framework audit and a full quarterly calibration review.

### Data freshness

- Exact entry or sell triggers require data through the latest completed trading day.
- Intraday prices may create alerts but do not complete a closing-price trigger.
- Require two agreeing price sources for live research; disclose material differences.
- Name sources and write `N/A — insufficient data` rather than inventing values.

### Brokerage reconciliation

Exact share quantities require:

- Shares held
- Current weighted-average cost
- Last verified trade and date
- Highest daily close while held
- Current protected-profit floor
- Last brokerage verification date

Until supplied, recommendations remain percentage-based and conditional. Never infer that a prior trade was filled, and never issue duplicate catch-up trades without reconciliation.

---

## 14. Required analysis front matter

```yaml
---
ticker: TICKER
decision_date: YYYY-MM-DD
data_through: YYYY-MM-DD
valuation_as_of: YYYY-MM-DD
framework_version: V5.2-provisional
instrument_type: OPERATING_COMPANY | BROAD_MARKET_CORE | SECTOR_OR_FACTOR_FUND | CONCENTRATED_THEMATIC_FUND
vehicle_role: N/A | STRATEGIC_CORE | DIVERSIFIED_FACTOR | SECTOR_SATELLITE | THEMATIC_SATELLITE
setup_id: TICKER-YYYYMMDD-NN
recommendation: BUY_STARTER | ADD | HOLD | TRIM | EXIT | WATCH | AVOID | PENDING_REFRESH
rec_vs_prior: NEW | HOLD_AT | UPGRADE_FROM_X | DOWNGRADE_FROM_X
security_signal: BUY_STARTER | ADD | HOLD | TRIM | EXIT | WATCH | AVOID | PENDING_REFRESH
portfolio_authorization: AUTHORIZED | NOT_REQUIRED | PENDING_ORCHESTRATOR | BLOCKED_OPEN_RISK | BLOCKED_SECTOR_CAP | BLOCKED_CORRELATED_CAP | BLOCKED_UNKNOWN_RISK
portfolio_block_reason: "concise reason" | N/A
position_stage_before: NONE | STARTER | HALF | ABOVE_HALF | FULL | UNKNOWN
target_stage: NONE | STARTER | HALF | ABOVE_HALF | FULL | UNKNOWN
confidence: 1-5              # overall analyst confidence in the recommendation (distinct from valuation-input confidence below)
conviction_score: NN/90 | N/A_VEHICLE
valuation_score: NN/30 | N/A_VEHICLE
valuation_input_confidence: NN/4 | N/A_VEHICLE
fundamentals_v5_score: NN/30 | N/A_VEHICLE
industry_score: NN/20 | N/A_VEHICLE
catalysts_narrative_score: NN/10 | N/A_VEHICLE
macro_score: NN/25
technical_score: NN/25
business_quality_gate: PASS | DEEP_VALUE_EXCEPTION | FAIL | N/A_VEHICLE
deep_value_exception: PASS | FAIL | NOT_APPLICABLE
credibility_risk_gate: PASS | PENDING | FAIL | N/A_VEHICLE
vehicle_integrity_gate: PASS | PENDING | FAIL | N/A_COMPANY
lookthrough_valuation_status: CHEAP | FAIR | EXPENSIVE | INSUFFICIENT | N/A_COMPANY
applicable_vehicle_cap_pct: 0.00 | N/A_COMPANY | N/A_CORE_POLICY
probability_weighted_fv: 0.00 | N/A_VEHICLE
bear_fv: 0.00 | N/A_VEHICLE
base_fv: 0.00 | N/A_VEHICLE
bull_fv: 0.00 | N/A_VEHICLE
bear_probability: NN | N/A_VEHICLE        # whole percent; company probabilities sum to 100
base_probability: NN | N/A_VEHICLE
bull_probability: NN | N/A_VEHICLE
scenario_probability_exception: "reason" | N/A
reverse_valuation_method: DCF | REVERSE_MULTIPLE | REVERSE_REVENUE | OTHER | N/A_VEHICLE
reverse_valuation_metric: "typed metric and horizon" | N/A_VEHICLE
reverse_valuation_implied: "implied value" | N/A_VEHICLE
reverse_valuation_bull_limit: "bull-case comparator" | N/A_VEHICLE
reverse_valuation_gate: PASS | BLOCK | N/A_VEHICLE
starter_zone: "0.00-0.00" | N/A
add_zone: "0.00-0.00" | N/A
full_position_ceiling: 0.00 | N/A
tactical_stop: 0.00 | N/A
plausible_gap_loss_pct: 0.00 | N/A
proposed_incremental_risk_pct: 0.00 | N/A
scaling_override_used: Yes | No
portfolio_ledger_status: CURRENT | STALE | UNAVAILABLE | NOT_HELD
pre_profit_flag: Yes | No | N/A_VEHICLE
binary_event_risk: HIGH | MEDIUM | LOW | NONE
thesis_status: INTACT | CHALLENGED | INVALIDATED
---
```

The body must explain every applicable score, scenario or vehicle test, gate, entry/exit level, missing datum, signal, and authorization. Highest close, live floor candidates, actual open risk, sector/correlation totals, and signal-reference shares live only in the portfolio ledger; do not duplicate them as ticker-owned state. A headline score or gate without evidence is invalid.

---

## 15. Audit and governance

### As-of-date replay

Evaluate every archived `Buy`, `Add`, `Hold`, `Trim`, `Sell/Exit`, `Watch`, and `Avoid` decision. Include documented missed opportunities. Never hand-pick memorable cases.

- Use only information available on the decision date when rescoring.
- Compare absolute return, sector-relative return, and SPY-relative return.
- Record maximum adverse excursion.
- Evaluate at fixed `63`, `126`, and `252` completed trading-session horizons when mature; label them 3, 6, and 12 months respectively.
- Keep incomplete rows as **insufficient evidence**, with the reason stated.
- Treat high subsequent return with severe interim drawdown as a mixed outcome, not automatically a miss.
- Deduplicate repeated reviews by `setup_id`. A new archived document is not automatically a new decision.
- For add-before-stop path tests, use the predeclared levels and the first qualifying event. If both occur in the same daily bar and intraday order is unavailable, record the stop first as the conservative result.
- Maintain an evidenced catastrophe-event registry containing ticker, event date, event type, and source; price decline alone is not a dilution, going-concern, or credibility event.

### Native V5 calibration

V5 conviction bands and numerical entry thresholds remain provisional until native V5 decisions have at least one complete earnings cycle and 63-session outcomes. Track three cohorts separately:

1. `AUTHORIZED` security-qualified starter/add decisions.
2. Security-qualified but portfolio-blocked **shadow** decisions.
3. Business-quality, credibility, reverse-valuation, or vehicle-integrity gate-blocked negative decisions.

Shadow decisions are frozen prospectively and may calibrate selection thresholds, but they do not silently satisfy the authorized starter/add promotion minimum. Gate-blocked names belong to the miss-discipline cohort, not the positive-entry cohort. At calibration:

1. Calibrate High/Moderate/Low bands from observed outcomes.
2. Check both opportunity capture and drawdown control.
3. Preserve regression protections for catastrophic dilution, going-concern risk, fraud/credibility failures, and undocumented binary exposure.
4. Document changes in a dated audit before promoting V5 from provisional status.

### Pre-declared promotion criteria (set now to prevent post-hoc rationalization)

V5 is promoted from *provisional* to *final* only when a native V5 sample of **at least 20 distinct `AUTHORIZED` starter/add decisions with 63-session outcomes** meets **all** of the following. An authorized analytical decision is not proof of a brokerage fill; verified execution is reported separately. These bars are declared in advance; missing any one keeps V5 provisional and triggers a documented parameter review rather than promotion.

| Dimension | Metric | Provisional bar |
|---|---|---:|
| Opportunity capture | Median SPY-relative return of distinct authorized `Buy Starter`/`Add` setups at 63 sessions | `≥ 0` |
| Selection quality | Share of starters whose first event is a qualifying add stage rather than the tactical stop | `≥ 55%` reach add first |
| Drawdown control | Median 63-session maximum adverse excursion from the recorded signal price | `≤ 15%` |
| Miss discipline | Median positive forgone 63-session SPY-relative return on gate-blocked names ÷ median absolute 63-session adverse excursion on the same cohort | `≤ 1.0`; zero denominator is `insufficient evidence` |
| Tail protection | Count of catastrophic outcomes (dilution/going-concern/credibility) that passed the gates | `0` |

The audit must show each metric's numerator, denominator, cohort size, exclusions, maturity status, and authorized-versus-shadow split. If capture is strong but the miss-discipline ratio exceeds `1.0`, review whether the gates are too tight; do not automatically loosen a catastrophic-risk protection. If drawdown control fails while capture is strong, review sizing and technical scaling. Record every promotion-or-hold decision, with the measured values, in a dated audit.

### Recommendation cadence

Avoid analytical churn. A recommendation normally remains unchanged for five trading days unless earnings, material news, a precommitted closing-price trigger, or a thesis/credibility change occurs. A fresh valuation-qualified pullback may also activate a predeclared starter without waiting for a technical recovery.

---

## Appendix: key formulas

```text
Probability-weighted fair value = Σ(scenario probability × scenario fair value)

Upside to fair value = (probability-weighted FV − entry price) / entry price

Reward/risk = (probability-weighted FV − entry price)
              / (entry price − tactical stop)

Stop distance = max((planned entry − tactical stop) / planned entry, 0)

Effective entry-risk distance = max(stop distance, plausible gap loss) for HIGH binary names

Stage size = 0.25% portfolio risk / effective entry-risk distance

Planned incremental risk = proposed incremental weight × effective entry-risk distance

Current stop risk = current position weight × max((current close − stop) / current close, 0)

Current effective risk = max(current stop risk, position weight × plausible gap loss) for HIGH binary names

Active-sleeve open risk = Σ current effective risk ≤ 8% (provisional)

Broad-market-core stress contribution = position weight × fixed policy stress loss

Cost-anchored floor price = weighted-average cost × (1 + protected-gain percentage)

Peak give-back band = clamp(12%, 2.5 × 20-day ATR%, 20%)

Peak-anchored floor price = highest daily close × (1 − peak give-back band)

Protected floor today = max(previous protected floor, active cost candidate, active peak candidate)

Reverse-DCF check: growth/margin/multiple implied by current price vs. bull-case assumptions
```

ATR, RSI, MACD, moving averages, volume profile, and relative strength are technical inputs, not sources of intrinsic value.
