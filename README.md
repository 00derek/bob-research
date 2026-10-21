# Bob Research

Dated investment research produced by Bob CFO using the published framework.

Read the site: https://00derek.github.io/bob-research/

This repository contains public report Markdown and Hugo presentation files.
It does not contain the private research agent, personal holdings or account
records. Reports are analytical assessments, not personalized advice or proof
of trades. Recorded prices are not live quotes. Always check analysis dates,
valuation dates, sources and evidence limitations.

The private authoring workspace exports reviewed content here. Do not edit this
mirror independently. Each ticker has a latest page and permanent dated reports.
Corrections create revisions rather than erasing historical analysis.

The research library and report pages use Hextra v0.13.0. Full-text search is
served locally with FlexSearch v0.8.143; licenses are included with both.
Company and fund reports follow separate framework paths. Each expanded report
identifies missing evidence in its relevant section. Reconstructed reports keep
their original research dates; expansion does not imply fresh market research.

## Build

Install the Hugo version in `.hugo-version`, then run:

```sh
python3 scripts/check_site.py .
hugo server
```

GitHub Actions validates the Markdown, builds Hugo and deploys GitHub Pages.
The framework is provisional. Republishing an old report does not refresh it.
