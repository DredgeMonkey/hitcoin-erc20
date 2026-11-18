# HitCoin — Solidity ERC-20 Contract

**Historical smart-contract project · Public technical showcase**

HitCoin is a fixed-supply ERC-20 token written in Solidity as a potential real-world promotional companion to an original fiction project. The preserved implementation demonstrates token-constructor design, basic ERC-20 accounting and allowances, contract compilation, and an independently documented development/deployment process.

This repository is a **deliberately curated public source release**, not a full development workspace, wallet archive, trading venue, or financial product. It has its **own clean Git history**. The contract source is reproduced **byte-for-byte** from the preserved historical file; the surrounding explanatory documentation was prepared for this public release.

## Implementation at a glance

| Item | Details |
| --- | --- |
| Contract | `HitCoin` |
| Token name / symbol | Hit Coin / HIT |
| Standard | ERC-20 |
| Language | Solidity (`pragma ^0.8.20`) |
| Historical compiler | Solidity 0.8.26 |
| Historical optimizer | Enabled, 200 runs |
| Historical EVM target | Cancun |
| Decimals | 18 |
| Initial mint | 1,000,000,000,000 HIT to a constructor-provided recipient |
| Public functions | Standard balance, transfer, allowance, approval, and token metadata interface |

### Explore the code

- [`src/HitCoin.sol`](src/HitCoin.sol) — historical, self-contained Solidity source, unchanged.
- [`docs/TECHNICAL_OVERVIEW.md`](docs/TECHNICAL_OVERVIEW.md) — design, supply behavior, and meaningful limitations.
- [`docs/EVIDENCE_AND_LIMITATIONS.md`](docs/EVIDENCE_AND_LIMITATIONS.md) — evidence standard and boundaries on historical claims.
- [`docs/PORTFOLIO_COPY.md`](docs/PORTFOLIO_COPY.md) — a concise explanation suitable for a professional portfolio.
- [`SECURITY.md`](SECURITY.md) — responsible disclosure and privacy stance.

## Architecture in one minute

The `HitCoin` constructor accepts a recipient address and mints the entire supply once. The internal ERC-20 accounting tracks balances and allowances. Standard functions enable transfers and approvals. The public contract interface contains **no ongoing token-minting function, miner/mining logic, staking, rewards, pause control, or administrator/ownership methods**.

The file is **self-contained**, with OpenZeppelin-style ERC-20 logic and comments; it is not importing a maintained OpenZeppelin package. It should not be confused with a contemporary audited token template.

## Project background and evidence

The original project source was committed in **March 2025**. Separate historical records document an Ethereum Mainnet deployment and a November 2026 wallet/explorer review. To avoid linking identifiable personal wallet activity to this public showcase, **contract and transaction identifiers are intentionally not reproduced here**. The code and local design are inspectable; this public repository alone does **not** independently substantiate the historical on-chain deployment or a current source-verification badge.

Neither a security audit, a production integration, nor successful token commercialization is claimed. There was no exchange listing, token investment offering, mining infrastructure, or financial return established by this project. Nothing here constitutes financial advice or an invitation to trade.

### Portfolio relevance

A small, historically grounded example of working across application logic, established interface standards, blockchain tooling, and documentation. HitCoin is an **adjacent supporting engineering example**, not the flagship of a systems architecture portfolio or an assertion of a primary Web3 specialization.

The fictional mining and bounty economy of the associated story is separate from the actual Solidity implementation. This repository contains no manuscript material.

## Reuse and limitations

The contract carries an MIT SPDX identifier. See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md) for licensing and attribution context. This historical source is published for inspection and learning, not endorsed for reuse in production without an independent security review and appropriate testing.
