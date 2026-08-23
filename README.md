# AI-Claw Showcase

AI-Claw is a showcase build for an explainable, rule-guarded AI service platform for crayfish aquaculture.

The project connects multi-source production data with risk triage, accountable tasks, visual-sample review, market signals, and audit-ready evidence. The public repository is intentionally small: it is a portfolio and evaluation surface, not the private production codebase.

## What this showcase demonstrates

- A unified view of ponds, water quality, weather, tasks, risks, and market signals
- AI-assisted recommendations grounded in structured records and explicit safety rules
- A persistent low-oxygen alert moving from recommendation to assigned task, retest, and audit trail
- Data provenance, review status, and version boundaries for visual samples
- Human authorization as the boundary for device actions and operational decisions

## Demo

- [English demo script](docs/demo-script-en.md)
- [English subtitle file](media/aiclaw-demo-en.srt)
- [English narration demo video](media/aiclaw-demo-en.mp4)

The video keeps the original product capture, adds English narration, and overlays English subtitles over the original subtitle strip. Some product labels in the capture remain Chinese; a fully localized product interface is a separate workstream.

## Reference example

`examples/agent-routing-demo.py` is a deliberately small, non-production example showing how a business question can be routed through deterministic safety rules before an assistant produces an explanation. It does not contain the AI-Claw production implementation, customer data, credentials, or proprietary model prompts.

Run it with:

```bash
python3 examples/agent-routing-demo.py "What should we do first for persistent low oxygen in Pond 12?"
```

## Public/private boundary

This repository contains only public-facing documentation, a redacted media asset, and a toy reference example. The following remain private:

- Production backend and frontend implementation
- Customer, partner, competition, and institutional materials
- Real operational records, personal information, and field images
- Model gateway addresses, API keys, passwords, deployment files, and database dumps
- Unfiled patent details and unpublished research data

## Status

This is a showcase build for research communication, technical discussion, and service enquiries. It is not a production control system and does not provide legal, financial, medical, or agricultural advice. Recommendations must be reviewed by an authorized operator and qualified domain personnel.

## Collaboration and enquiries

Please open a GitHub Issue with a clear use case, deployment environment, and expected integration boundary. Commercial deployment, private customization, data integration, and operational support are separate services and are not granted by this repository.

## Licensing

The MIT License in this repository applies to the reference example code only. Demo media, product names, screenshots, and third-party materials remain subject to their respective rights and permissions. No license is granted to the private AI-Claw production platform or to data that is not included here.

