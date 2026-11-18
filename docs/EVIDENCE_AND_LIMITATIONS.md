# Evidence, Provenance & Claim Boundaries

**Public publication record | November 2026**

This document distinguishes directly inspectable evidence from archived historical observations. It is not a smart-contract security audit.

## Directly inspectable here

| Statement | Public evidence | Interpretation |
| --- | --- | --- |
| The source defines a token named Hit Coin with symbol HIT | `src/HitCoin.sol` constructor | Source-level fact |
| The constructor mints one trillion HIT using 18 decimals | `src/HitCoin.sol` (`_mint` expression and `decimals()`) | Source-level fact; not by itself a live on-chain state query |
| The ERC-20 read/write interface is implemented | `src/HitCoin.sol` | Source-level fact; no new behavioral tests asserted |
| There is no public mining, continued mint, staking, or administrator interface | `src/HitCoin.sol` | Source-level interface/code observation, not a full security audit |
| This is a faithful copy of a historical contract source | Internal archival source comparison before publication | Historical provenance preserved outside this public release |

## Historical, separately archived evidence

The original development project dates to **March 2025**. An archive of the original workspace and a later **November 4, 2026** wallet/explorer reference documents the Ethereum Mainnet deployment, source-verification observation, compilation settings, and account recovery review.

The 2026 reference describes **an exact-match source-verification status observed at that time**; no independent contract security audit was performed. The archived records are maintained separately from this public release. This public repository does not expose associated personal wallet records or transaction identifiers.

**Public verification boundary:** Because contract and transaction identifiers are omitted by design, a reader cannot independently confirm the specific Mainnet deployment from this repository alone. Do not claim otherwise, or represent a historical explorer observation as a fresh current check.

## Intentionally excluded from this public release

Personal account/deployer identifiers, transaction identifiers, wallet balances, wallet recovery documentation, underlying private archival files, unrelated account history, and bulk Remix workspace exports. No seed phrase, wallet key, or recovery secret is stored here.

These exclusions reduce direct exposure; they do **not** guarantee anonymity. Ethereum records are public, and a sufficiently motivated reader may correlate public source/code/token metadata with a historical chain deployment.

## What is not claimed

No live contract inspection in this publication process, third-party security audit, token investment or fundraising outcome, market liquidity, exchange listing, financial return, user adoption, mining platform, staking infrastructure, or production-ready decentralized application.
