# Pavel Donin

**AI Engineer — Agent Orchestration, LLM Tooling**

_Agent systems in production for a studio team and client users · 10+ years in software, 5 of them leading teams_

## Contact

[doninpr@gmail.com](mailto:doninpr@gmail.com) • [linkedin.com/in/doninpr](https://www.linkedin.com/in/doninpr) • [t.me/doninpr](https://t.me/doninpr) • [github.com/prineycom](https://github.com/prineycom) • [CV.pdf](https://github.com/prineycom/prineycom/raw/main/CV.pdf)  
Novi Sad, Serbia (CET, UTC+1) · remote · open to full-time roles worldwide

## Professional Summary

AI engineer who builds agent systems and runs them in production: I moved a 7-person studio team onto agent-driven development, automate its business processes with Hermes agents and MCP integrations, and operate a medical-data RAG assistant for client users. I co-built the ticket-driven Claude Code orchestrator that runs my own delivery and self-host open models for my agents. 10+ years of full-stack engineering (Python, TypeScript), 5 of them leading teams.

## AI Engineering Projects

**LLM-driven development pipeline for a production studio** (Talking Birds & Flying Fish, _Aug 2025 — Present_)

- Moved the studio team onto agent-driven delivery: added the first agent configuration in Aug 2025, and a year later it was in 22 of 33 repositories, with every 2026 project starting from it. Introduced a plan → isolated worktree → independent agent review → human acceptance → ship workflow that the team adopted, and measured the change with an evidence-tagged atlas of git, tracker and PR history.
- Ran studio work through the yokemate orchestrator: 80+ agent-written plans across 11 studio projects, from museum installations to internal systems.

**Hermes agents for business-process automation** (Talking Birds & Flying Fish, _Apr 2026 — Present_)

- Deployed Hermes agents for staff with a shared skill bank I wrote — CG budget estimates from a brief to a priced spreadsheet and client PDF, estimate-template expertise, an internal database with privacy rules — connected to Microsoft 365 over MCP and covered by a promptfoo eval suite with LLM-as-judge.
- Built the data layer behind them: a corporate data core designed from an audit of every department's spreadsheets, with its 22-migration schema rolled out by an agent through the Supabase MCP server; an hourly Python sync to SharePoint via Microsoft Graph, in production since Sep 2026; the HR vacation tracker moved onto the database in two weeks (10 merged PRs, tests from 21 to 135).
- Built Microsoft Teams bots on the data core — a company-wide HR bot (leave, worklogs, calendar, policy search) and data bots for management — and a company RAG over SharePoint documents, now in integration.

**Aleen — medical-data AI assistant** (YokeLoop client, _Jun 2026 — Present_)

- Run a Hermes agent over an MCP-based RAG system on family health records, with per-user data isolation; 6 active users. Administer the deployment on the client's server and tune the harness and agents.

**yokemate — ticket-driven multi-repo orchestrator on Claude Code** (YokeLoop, co-built with [Ivan Hilkov](https://github.com/ivan-hilckov), _Aug 2026 — Present_; private, demo on request)

- Runs my delivery across 4 organizations and about 18 repositories: 88 tickets in the first month, 72 merged at a median of 16 hours from plan to merge, 1 in 5 sent back for rework at acceptance review.
- Read-only scout and planner subagents, implementation in an isolated worktree, an independent reviewer subagent and a human merge gate; a command guard lets task sessions run unattended. Grew out of the co-authored [yoke](https://github.com/yokeloop/yoke) plugin; my rebuild on the pi runtime, [yokemate-pi](https://github.com/yokeloop/yokemate-pi), showed the workflow-first design was the wrong foundation and led to mypi, a memory-first successor (early stage).

**Realtime voice agent — 3 iterations** (personal R&D, _Apr 2026 — Present_) · [v1](https://github.com/prineycom/voice-agent) · [v2](https://github.com/prineycom/voice-agent-v2) · [v3](https://github.com/yokeloop/voca)

- Built a realtime speech-to-speech agent end to end — WebRTC transport, streaming STT → LLM → TTS with barge-in, and a 3D avatar whose face follows the voice's emotion — and fit the whole stack on one 12 GB GPU: cut NVIDIA Audio2Face-3D memory from 8.8 GB to ~0.4 GB by rebuilding its TensorRT engine, and facial animation from ~3 s to 81 ms per utterance with a persistent C++ inference helper.
- Gave it hands: the agent turns speech into schema-validated tool calls executed in a locked-down Docker sandbox and reports results to Telegram; v3 extends this to delegating tasks to coding agents. Every model choice — STT, LLM, TTS — passed gates I set for latency, real-time factor and VRAM, recorded across 37 ADRs; the third version was a deliberate rewrite after I judged the second over-engineered.

**Personal agent stack** (personal, _Feb 2026 — Present_)

- Run Priney, my always-on assistant on Hermes, self-hosted on a Raspberry Pi 5, covering tasks, calendar, email, finances, health, knowledge and travel. Designed its Second Brain — an Obsidian vault of 226 notes with routing rules for where the agent reads and writes, synced through CouchDB and git — and an on-device RAG over it (ONNX embeddings, SQLite vector store, incremental re-indexing).
- Wrote its integrations with self-hosted services: MCP servers for tasks (sp-cli) and, earlier, habit and time tracking, alongside finance and bookmark services; plus cron automations — a watchlist monitor with priorities and quiet hours, digests, nightly backups.
- Self-hosted Qwen3.6-35B-A3B as my agents' primary model on a single 12 GB GPU (MoE expert offload, quantized KV cache, 262K context, tool-calling template) and tuned the agent around it — enforced tool use, compression that keeps tool-call history; tested smaller models (LFM, Gemma, Qwen, community fine-tunes) on the GPU and the Pi; built [llama-tray](https://github.com/prineycom/llama-tray) to switch model presets.

**[sp-cli](https://github.com/prineycom/sp-cli) — CLI and MCP server for the Super Productivity app** (_Sep 2026_)

- 97 commands with an MCP server generated from the CLI itself; built in 2 days by an autonomous agent session on the yoke workflow and verified against a live phone sync.

## Key Metrics (July 2025 — September 2026)

- Throughput with a quality denominator: 3,900+ commits and 368 pull requests (341 merged, 93%) across 59 repositories in 15 months; only 12 commits were reverts.
- Context engineering: about a third of commits change only Markdown or agent configuration (plans, journals, skills, CLAUDE.md); about 25 skills and 25 subagent definitions authored and versioned in git.

![Contribution graph](assets/contributions.svg)

_Drawn from local git history across my personal and work GitHub accounts; GitHub's own graph on this profile misses about 1,350 studio commits made under the work account._

## Professional Experience

### **YokeLoop** — **Co-founder (product & client delivery)** — _Apr 2026 — Present_

_Two-founder company building LLM-agent products for small and mid-size businesses; I own product, specifications and client delivery, my co-founder owns core engineering_

- Specified hermes-orchestration, a platform for hosting isolated AI agents on bare metal (a sandbox per user, credentials kept on the host); deploy and operate it for clients, including Aleen and Talking Birds.
- Co-authored the yoke Claude Code plugin and the yokemate orchestrator.

### **Talking Birds & Flying Fish** — **Tech Lead → Team Lead → Head of Development** — _Jul 2024 — Present_

_Barcelona production studio: interactive installations for corporate conference stands and museum exhibitions; clients include Microsoft. Tech Lead (Jul 2024), Team Lead (May 2025), Head of Development (Jan 2026)_

- Built the development department from scratch: hired and grew the team (web 2 → 5, plus 2 Unreal Engine developers), defined the tech stack and internal packages, and set up the whole delivery process — YouTrack planning and task decomposition, an iterative cycle fitted to fixed exhibition dates, code review and CI, release management, e2e and soak tests for installations that run unattended for weeks, monitoring (Sentry, Loki, Grafana) and a documentation-first culture.
- Delivered 40 installations (25 visitor-facing) from 33 repositories — Microsoft conference stands touring 12 cities, game stations, a permanent museum exhibition — with 2,299 tracked tasks and 670 PRs, while staying hands-on (1,128 own commits); the shared `@tb-ff/web-toolkit` I co-developed is used in 18 of 33 projects.
- Lead the studio's AI adoption: the agent-driven development pipeline and Hermes business automation above.
- As developer on the museum exhibit, replaced a legacy .NET drawing recognizer with a Python OpenCV service without touching installed hardware; built a 40-case test harness, disproved my own planned fix with diagnostics and moved the remaining error class into the printed form's marker codes.

### **Sminex** — **Senior Full-Stack Developer, Team Lead (Business Process Automation)** — _May 2022 — Jul 2024_

- Led the in-house business-process automation team of 3 at a real-estate developer (process, architecture, hiring); shipped 5 web services automating construction and operational workflows, integrated with internal systems and supported in production. _TypeScript, React, NestJS, PostgreSQL, Django, Autodesk Forge._

### **SU-10** — **Tech Lead, Construction Process Automation** — _Aug 2021 — May 2022_

- Led a team of 3 automating construction business processes on the Autodesk Forge (BIM) API, from development process to MVP in 10 months; 1st place at the Autodesk Forge Hackathon 2021 (Cloud Collaboration).

### **RoadAR** — **Frontend Developer** — _Feb 2022 — Sep 2022_ (part-time)

- Web visualization of point clouds and spatial data from SLAM and ML pipelines (React, deck.gl, WebGL, Cesium).

### **DataMap Geodata Laboratory** — **Frontend Web Developer** — _Mar 2018 — Aug 2021_

- GIS web services and geodata collection: 5+ client projects through Upwork, 5 data-collection projects; trained 20+ students and co-organized 2 hackathons.

**Earlier roles**: AT Consulting — Frontend Developer (_2017 — 2018_); freelance web development (_2015 — 2016_); PHP internship (_2014_).

## Technical Skills

- **Agents & LLM**: Claude Code (skills, subagents, hooks), Claude Agent SDK, pi, Hermes Agent, MCP servers, context engineering, orchestrator-worker pipelines with human merge gates, structured outputs and tool calling, LiteLLM
- **Evals, RAG & inference**: promptfoo with LLM-as-judge, test harnesses, RAG (chunking, multilingual embeddings, vector stores, SharePoint via Microsoft Graph), LangSmith, llama.cpp (quantization, MoE offload, speculative decoding), TensorRT, Whisper and TTS models, ComfyUI
- **Stack & workstation**: Python (FastAPI, Django, pytest), TypeScript, React, Electron, Node.js, PostgreSQL, Supabase, SQLite, OpenCV, Docker, GitHub Actions; Arch Linux (Omarchy), Neovim, herdr, pi, Claude Code
- **Languages**: Russian (native), English (fluent, professional working), Serbian (basic)

## Education

**Information Systems and Technologies** — Moscow State University of Geodesy and Cartography (MIIGAiK), 2013 — 2017

## Availability

- Open to full-time AI Engineer, Agent / LLM Platform Engineer, Applied AI and Forward Deployed Engineer roles; remote, worldwide; B2B contract or employer of record.
