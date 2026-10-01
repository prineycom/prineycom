# Pavel Donin

**AI Engineer — Agent Orchestration, LLM Tooling**

_Agent systems in production for a studio team and client users · 10+ years in software, 5 of them leading teams_

## Contact

[doninpr@gmail.com](mailto:doninpr@gmail.com) • [linkedin.com/in/doninpr](https://www.linkedin.com/in/doninpr) • [t.me/doninpr](https://t.me/doninpr) • [github.com/prineycom](https://github.com/prineycom) • [CV.pdf](https://github.com/prineycom/prineycom/raw/main/CV.pdf)  
Novi Sad, Serbia (CET, UTC+1) · remote · open to full-time roles worldwide

## Professional Summary

AI engineer who designs agent systems and runs them in production. I moved a 7-person studio team onto agent-driven development and built its business automation: LLM agents on the open-source Hermes Agent runtime with skills, Microsoft 365 integrations over MCP and evals I wrote, on a data core an agent rolled out from my spec. For clients I designed the isolation model of an agent-hosting platform and operate a medical-data RAG assistant. I self-host open models for my agents, build realtime voice pipelines, and co-built the Claude Code orchestrator that runs my delivery. 10+ years of full-stack engineering (Python, TypeScript), 5 of them leading teams.

## AI Engineering Projects

**LLM-driven development pipeline for a production studio** (Talking Birds & Flying Fish, _Aug 2025 — Present_)

- Moved the studio team onto agent-driven delivery: added the first agent configuration in Aug 2025, and a year later it was in 22 of 33 repositories, with every 2026 project starting from it. Introduced a plan → isolated worktree → independent agent review → human acceptance → ship workflow that the team adopted, and measured the change with an evidence-tagged atlas of git, tracker and PR history.
- Ran studio work through the yokemate orchestrator: 80+ agent-written plans across 11 studio projects, from museum installations to internal systems.

**LLM agents for business-process automation** (Talking Birds & Flying Fish, _Apr 2026 — Present_)

- Deployed agents for staff on Hermes Agent (Nous Research's open-source agent runtime) with a shared skill bank I wrote — CG budget estimates from a brief to a priced spreadsheet and client PDF, estimate-template expertise, an internal database with privacy rules — connected to Microsoft 365 over MCP and covered by a promptfoo eval suite with LLM-as-judge.
- Built the data layer behind them: a corporate data core designed from an audit of every department's spreadsheets, with its 22-migration schema rolled out by an agent through the Supabase MCP server; an hourly Python sync to SharePoint via Microsoft Graph, in production since Sep 2026; the HR vacation tracker moved onto the database in two weeks (10 merged PRs, tests from 21 to 135).
- Built Microsoft Teams bots on the data core — a company-wide HR bot (leave, worklogs, calendar, policy search) and data bots for management — and a company RAG over SharePoint documents, now in integration.

**Aleen — medical-data AI assistant** (YokeLoop client, _Jun 2026 — Present_)

- Run a Hermes Agent assistant over an MCP-based RAG system on family health records, with per-user data isolation; 6 active users. Administer the deployment on the client's server and tune the harness and agents.

**yokemate — ticket-driven multi-repo orchestrator on Claude Code** (YokeLoop, co-built with [Ivan Hilkov](https://github.com/ivan-hilckov), _Aug 2026 — Present_; private, demo on request)

- Runs my delivery across 4 organizations and about 18 repositories, from tracker tickets (YouTrack, GitHub Issues) to merged pull requests.
- Read-only scout and planner subagents, implementation in an isolated worktree, an independent reviewer subagent and a human merge gate; a command guard lets task sessions run unattended. Grew out of the co-authored [yoke](https://github.com/yokeloop/yoke) plugin; my rebuild on the open-source pi coding-agent runtime, [yokemate-pi](https://github.com/yokeloop/yokemate-pi), showed the workflow-first design was the wrong foundation and led to mypi, a memory-first successor (early stage).

**Realtime voice agent — 3 iterations** (personal R&D, _Apr 2026 — Present_) · [v1](https://github.com/prineycom/voice-agent) · [v2](https://github.com/prineycom/voice-agent-v2) · [v3](https://github.com/yokeloop/voca)

- Built a realtime speech-to-speech agent end to end — WebRTC transport, streaming STT → LLM → TTS with barge-in, and a 3D avatar whose face follows the voice's emotion — and fit the whole stack on one 12 GB GPU: cut NVIDIA Audio2Face-3D memory from 8.8 GB to ~0.4 GB by rebuilding its TensorRT engine, and facial animation from ~3 s to 81 ms per utterance with a persistent C++ inference helper.
- Gave it hands: the agent turns speech into schema-validated tool calls executed in a locked-down Docker sandbox and reports results to Telegram; v3 extends this to delegating tasks to coding agents. Every model choice — STT, LLM, TTS — passed gates I set for latency, real-time factor and VRAM, recorded across 37 ADRs; the third version was a deliberate rewrite after I judged the second over-engineered.

**Local-first agent lab** (personal, _Feb 2026 — Present_)

- Run Priney, my always-on personal assistant on Hermes Agent, self-hosted on a Raspberry Pi 5 and covering tasks, calendar, email, finances, health, knowledge and travel. Designed its Second Brain — a 226-note Obsidian vault with routing rules for where the agent reads and writes, synced through CouchDB and git — with on-device RAG over it (ONNX embeddings, SQLite vectors, incremental re-indexing), and wrote its MCP integrations and cron automations (a watchlist monitor with priorities and quiet hours, digests, backups).
- Self-hosted Qwen3.6-35B-A3B as my agents' primary model on a single 12 GB GPU (MoE expert offload, quantized KV cache, 262K context) and tuned the agent around it — enforced tool use, compression that keeps tool-call history; tested LFM, Gemma and Qwen variants and community fine-tunes on the GPU and the Pi.
- Wrote [sp-cli](https://github.com/prineycom/sp-cli), a CLI and MCP server for the Super Productivity app: 97 commands, with MCP tools generated from the CLI itself; built in 2 days by an autonomous agent session on the yoke workflow and verified against a live phone sync.

## Key Metrics (July 2025 — September 2026)

- Agent delivery: in its first month the orchestrator took 88 tickets, merged 72 at a median of 16 hours from plan to merge, and returned 1 in 5 for rework at acceptance review.
- Engineering output: 3,900+ commits and 368 pull requests (93% merged) across 59 repositories; about a third of the commits are agent context — plans, skills, CLAUDE.md — with around 25 skills and 25 subagents written.

## Professional Experience

### **YokeLoop** — **Co-founder (agent integration & client delivery)** — _Apr 2026 — Present_

_Two-founder company building LLM-agent products for small and mid-size businesses; I design the agent layer and run client deployments, my co-founder builds the hosting platform_

- Designed the isolation model for our agent-hosting platform — a Docker sandbox per user with no Docker socket, credentials kept on the host, per-user data — and wrote its per-employee container guide; deploy and operate it for two clients, Aleen and Talking Birds.
- Build the agent layer for clients — skill banks, MCP integrations, promptfoo evals — and co-authored the yoke Claude Code plugin and the yokemate orchestrator.

### **Talking Birds & Flying Fish** — **Tech Lead → Team Lead → Head of Development** — _Jul 2024 — Present_

_Barcelona production studio: interactive installations for corporate conference stands and museum exhibitions; clients include Microsoft. Tech Lead (Jul 2024), Team Lead (May 2025), Head of Development (Jan 2026)_

- Built the development department from scratch: started as its only web developer and grew it to 5 web and 2 Unreal Engine developers, defined the tech stack and internal packages, and set up the whole delivery process — YouTrack planning and task decomposition, an iterative cycle fitted to fixed exhibition dates, code review and CI, release management, e2e and soak tests for installations that run unattended for weeks, monitoring (Sentry, Loki, Grafana) and a documentation-first culture.
- Delivered 40 installations (25 visitor-facing) from 33 repositories — Microsoft conference stands touring 12 cities, game stations, a permanent museum exhibition — with 2,299 tracked tasks and 670 PRs, while staying hands-on (1,128 own commits); the shared `@tb-ff/web-toolkit` I co-developed is used in 18 of 33 projects.
- Led the studio's AI adoption: the agent-driven development pipeline and business-process agents above.
- As developer on the museum exhibit, replaced a legacy .NET drawing recognizer with a Python OpenCV service without touching installed hardware; built a 40-case test harness, disproved my own planned fix with diagnostics and moved the remaining error class into the printed form's marker codes.

### **Sminex** — **Team Lead, Business Process Automation** — _May 2022 — Jul 2024_

- Led a team of 3 at a real-estate developer; shipped 5 web services automating construction and operational workflows, integrated with internal systems (TypeScript, NestJS, PostgreSQL, Django).

### **SU-10** — **Tech Lead, Construction Process Automation** — _Aug 2021 — May 2022_

- Led a team of 3 from process setup to MVP on the Autodesk Forge (BIM) API; 1st place at the Autodesk Forge Hackathon 2021.

**Earlier roles**: RoadAR — point-cloud and SLAM data visualization (_2022_, part-time); DataMap Geodata Laboratory — GIS web services, 5+ client projects, trained 20+ students (_2018 — 2021_); AT Consulting — frontend (_2017 — 2018_); freelance web and a PHP internship (_2014 — 2016_).

## Technical Skills

- **Agents & LLM**: Claude Code (skills, subagents, hooks), Claude Agent SDK, pi, Hermes Agent, MCP servers, context engineering, orchestrator-worker pipelines with human merge gates, structured outputs and tool calling, LiteLLM
- **Evals, RAG & inference**: promptfoo with LLM-as-judge, test harnesses, RAG (chunking, multilingual embeddings, vector stores, SharePoint via Microsoft Graph), LangSmith, llama.cpp (quantization, MoE offload, speculative decoding), TensorRT, Whisper and TTS models, ComfyUI
- **Stack & workstation**: Python (FastAPI, Django, pytest), TypeScript, React, Electron, Node.js, PostgreSQL, Supabase, SQLite, OpenCV, Docker, GitHub Actions; Arch Linux (Omarchy), Neovim, herdr, pi, Claude Code
- **Languages**: Russian (native), English (fluent, professional working), Serbian (basic)

## Education

**Information Systems and Technologies** — Moscow State University of Geodesy and Cartography (MIIGAiK), 2013 — 2017

## Availability

- Open to full-time AI Engineer, Agent / LLM Platform Engineer, Applied AI and Forward Deployed Engineer roles; remote, worldwide; B2B contract or employer of record.
