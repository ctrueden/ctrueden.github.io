---
title: "Trump Accounts are worse than regular IRAs"
date: 2026-06-02 18:43:00 -0600
---

Trump Accounts look like worse investments than both Traditional IRAs and Roth IRAs. Why aren't more folks in the financial sector pointing this out?

*2026-06-05 update: I have since seen one article that covers why Trump Accounts are not competitive with other existing investment options: [Trump Accounts Serve No Clear Purpose and Would Exclude Vulnerable Children](https://taxlawcenter.org/blog/trump-accounts-serve-no-clear-purpose-and-would-exclude-vulnerable-children).*

Not only is it impossible to withdraw early (unlike regular IRAs) — and not only does one have to suffer the narcissistic moniker "Trump Account" for decades in one's financial portfolio — but the math also doesn't work out.

What follows is some quick LLM-powered (LLM-tainted?) calculation of common scenarios. I honestly have not checked the math super thoroughly, but I would be surprised if the conclusions drawn here are fundamentally wrong.

## Comparison: withdrawal at age 18

### Assumptions

- Growth rate: 7% annually (nominal — conservative long-run stock index average)
- Contribution period: 18 years at $5,000/year post-tax (i.e. $90,000 total effective out-of-pocket)
- Age 18 withdrawal tax rate: 12% federal (single filer, ~$12k–$48k income range in 2024)
- Contribution-period marginal rate (for pre-tax scenario): 22%

|           Scenario            | Annual Contribution | Balance  |    Tax at Withdrawal     | Net Payout |
|-------------------------------|---------------------|----------|--------------------------|------------|
| Traditional IRA (pre-tax)     | $6,410 pre-tax      | $217,940 | $26,150 (12% on all)     | $191,790   |
| Roth IRA (post-tax)           | $5,000 post-tax     | $170,000 | $0                       | $170,000   |
| Trump Account (post-tax trad) | $5,000 post-tax     | $170,000 | $9,600 (12% on earnings) | $160,400   |

Traditional pre-tax IRA wins — by about $22,000 over Roth and $31,000 over Trump Account — when normalized to the same real cost. This is the expected result: whenever your marginal rate at contribution (22%) exceeds your rate at withdrawal (12%), the pre-tax vehicle wins because the government is effectively giving you a larger interest-free loan to invest.

The crossover point is exactly when contribution rate = withdrawal rate (e.g., both 22%). At that point, Roth and traditional pre-tax are mathematically equivalent — and Trump Accounts still lose, since they combine post-tax contributions with taxed earnings.

## Comparison: withdrawal at age 60

2026-06-05 update: "On a taxpayer’s 31st birthday, the account ceases to be a Trump account and any remaining balance is treated as distributed" [\[source\]](https://taxlawcenter.org/blog/trump-accounts-serve-no-clear-purpose-and-would-exclude-vulnerable-children). So this retirement-at-age-60 scenario is only limitedly useful.

|      Starting balance (age 18)      | Balance at age 60 |
|-------------------------------------|-------------------|
| $170,000 (Roth / Trump Account)     | $2,914,000        |
| $217,940 (Trad pre-tax, normalized) | $3,736,000        |

Since the withdrawal tax rate now determines who wins, we look at two scenarios:

At 22% withdrawal (= contribution rate — the breakeven)

|         Scenario          |  Balance   |                Tax                |    Net     |
|---------------------------|------------|-----------------------------------|------------|
| Traditional IRA (pre-tax) | $3,736,000 | $822,000 (22% on all)             | $2,914,000 |
| Roth IRA                  | $2,914,000 | $0                                | $2,914,000 |
| Trump Account             | $2,914,000 | $621,000 (22% on $2.82M earnings) | $2,293,000 |

Trad and Roth are mathematically identical when contribution rate = withdrawal rate. This is always true — the extra pre-tax contribution and the withdrawal tax cancel exactly.

At 32% withdrawal (higher bracket, large IRA distributions)

|         Scenario          |  Balance   |                Tax                |    Net     |
|---------------------------|------------|-----------------------------------|------------|
| Traditional IRA (pre-tax) | $3,736,000 | $1,196,000 (32% on all)           | $2,540,000 |
| Roth IRA                  | $2,914,000 | $0                                | $2,914,000 |
| Trump Account             | $2,914,000 | $904,000 (32% on $2.82M earnings) | $2,010,000 |

Roth wins at retirement — specifically because the $3M balance in a traditional IRA almost guarantees you'll be in a high bracket when drawing it down (or hit with RMDs), erasing the contribution-time advantage.

Trump Account loses in every scenario, by a lot. At retirement it's a $300k–$500k penalty vs. Roth on the same contributions. The longer the time horizon, the worse it looks, because more of the account is taxable earnings.

The fundamental rule: Roth is better when withdrawal rate ≥ contribution rate. Over a 60-year horizon, that's almost always the case — a $3M IRA forces large distributions regardless of lifestyle.

## The $1,000 Government Seed

But wait! I hear you say. The government is contributing $1,000 for qualifying young children! This is a pure bonus for Trump Accounts. Assuming it's deposited at birth and grows the full period:

- At age 18: $1,000 × (1.07)^18 ≈ $3,380 (tax at 12% → +$2,974 net)
- At age 60: $1,000 × (1.07)^60 ≈ $57,950 (tax at 22% → +$45,200 net; at 32% → +$39,400 net)

The seed is treated as pre-tax income (government-contributed, not from the beneficiary's after-tax dollars), so the full balance is taxable at withdrawal.

### Updated Tables

#### Age 18 withdrawal (12%)

|         Scenario          | Net (previous) | Seed bonus | Net (updated) |
|---------------------------|----------------|------------|---------------|
| Traditional IRA (pre-tax) | $191,790       | —          | $191,790      |
| Roth IRA                  | $170,000       | —          | $170,000      |
| Trump Account             | $160,400       | +$2,974    | $163,374      |

#### Age 60 withdrawal (22%)

|         Scenario          | Net (previous) | Seed bonus | Net (updated) |
|---------------------------|----------------|------------|---------------|
| Traditional IRA (pre-tax) | $2,914,000     | —          | $2,914,000    |
| Roth IRA                  | $2,914,000     | —          | $2,914,000    |
| Trump Account             | $2,293,000     | +$45,200   | $2,338,200    |

#### Age 60 withdrawal (32%)

|         Scenario          | Net (previous) | Seed bonus | Net (updated) |
|---------------------------|----------------|------------|---------------|
| Roth IRA                  | $2,914,000     | —          | $2,914,000    |
| Traditional IRA (pre-tax) | $2,540,000     | —          | $2,540,000    |
| Trump Account             | $2,010,000     | +$39,400   | $2,049,400    |

### Bottom Line

The $1,000 seed is genuinely valuable — $57,950 in nominal growth over 60 years is real money — but it doesn't come close to closing the gap. At retirement, the Trump Account still trails a Roth by ~$575,000 to ~$865,000 depending on tax bracket. The seed offsets roughly 5–8% of that deficit.

The seed is essentially a marketing feature that looks impressive ("free $1,000!") while the structural tax disadvantage of the account — post-tax contributions plus taxed earnings at withdrawal — quietly costs hundreds of thousands of dollars over a lifetime.

----------

> Provided they did not actually see the money dropping out of their pockets, nor suffer immediate physical pain, would they listen to any arguments as to the waste of money and happiness which their folly caused them. But this had an effect of which I have little reason to complain, for I was allowed almost to call them life-long self-deceivers to their faces, and they said it was quite true, but that it did not matter.

—Samuel Butler, Erewhon, Preface to Second Edition (1872)
