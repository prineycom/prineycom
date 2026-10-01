# Pavel Donin

**AI Engineer — Agent Orchestration, LLM Tooling**

_Agent harnesses, orchestration and MCP tooling in production for a studio team and client users · 10+ years in software, 5 of them leading teams_

## Contact

[doninpr@gmail.com](mailto:doninpr@gmail.com) • [linkedin.com/in/doninpr](https://www.linkedin.com/in/doninpr) • [t.me/doninpr](https://t.me/doninpr) • [github.com/prineycom](https://github.com/prineycom) • [CV.pdf](https://github.com/prineycom/prineycom/raw/main/CV.pdf)  
Novi Sad, Serbia (CET, UTC+1) · remote, EU time zone · open to full-time AI Engineer, Agent Platform, Applied AI and Forward Deployed roles worldwide · B2B contract or EOR

## Professional Summary

AI engineer who designs agentic systems — MCP servers, subagents and agent skills — and runs them reliably in production. I moved a 7-person studio team onto agent-driven development and built its business automation: LLM agents on the open-source Hermes Agent runtime with skills, Microsoft 365 integrations over MCP and evals I wrote, on a data core an agent rolled out from my spec. For clients I designed the isolation model of an agent-hosting platform and operate a medical-data RAG assistant; I co-built the Claude Code orchestrator that runs my delivery and self-host open models for my agents. 10+ years of full-stack engineering (Python, TypeScript), 5 of them leading teams.

## AI Engineering Projects

**LLM-driven development pipeline for a production studio** (Talking Birds & Flying Fish, _Aug 2025 — Present_)

- Moved the studio team onto agent-driven delivery: added the first agent configuration in Aug 2025, and a year later it was in 22 of 33 repositories, with every 2026 project starting from it. Introduced a plan → isolated worktree → independent agent review → human acceptance → ship workflow that the team adopted, and measured the change with an evidence-tagged atlas of git, tracker and PR history.
- Ran studio work through the yokemate orchestrator: 80+ agent-written plans across 11 studio projects, from museum installations to internal systems.

**LLM agents for business-process automation** (Talking Birds & Flying Fish, _Apr 2026 — Present_)

- Deployed agents for staff on Hermes Agent (Nous Research's open-source agent runtime) with a shared skill bank I wrote — CG budget estimates from a brief to a priced spreadsheet and client PDF, estimate-template expertise, an internal database with privacy guardrails for group chats — connected to Microsoft 365 over MCP and covered by a promptfoo eval suite that checks skill triggering, tool choice and flags, with an LLM-as-judge rubric and a spend cap per run.
- Built the data layer behind them: a corporate data core designed from stakeholder discovery across every department's spreadsheets, with its 22-migration schema rolled out by an agent from a step-by-step, self-verifying prompt spec through the Supabase MCP server; an hourly Python data pipeline (Postgres → Microsoft Graph → SharePoint), in production since Sep 2026; the HR vacation tracker moved onto the database in two weeks (10 merged PRs, tests from 21 to 135).
- Built Microsoft Teams bots on the data core — a company-wide HR bot (leave, worklogs, calendar, policy search) and data bots for management (a retrieval layer over SharePoint documents is in integration).

**Aleen — medical-data AI assistant** (YokeLoop client, _Jun 2026 — Present_)

- Run in production a Hermes Agent assistant over an MCP-based retrieval (RAG) system on family health records, with per-tenant data isolation; 6 active users. Customer-facing: administer the deployment on the client's server and tune the harness and agents on their requests.

**yokemate — ticket-driven multi-repo orchestrator on Claude Code** (YokeLoop, co-built with [Ivan Hilkov](https://github.com/ivan-hilckov), _Aug 2026 — Present_; private, demo on request)

- Runs my delivery across 4 organizations and about 18 repositories, from tracker tickets (YouTrack, GitHub Issues) to merged pull requests: in its first month I put 88 tickets through it, 72 merged at a median of 16 hours from plan to merge, 1 in 5 sent back for rework at acceptance review.
- Multi-agent pipeline: read-only scout and planner subagents, implementation in an isolated worktree, an independent reviewer subagent and a human-in-the-loop merge gate; a PreToolUse guard that denies irreversible commands and names the allowed alternative lets task sessions run unattended; the model is routed per project. Grew out of the co-authored [yoke](https://github.com/yokeloop/yoke) plugin; my rebuild on the open-source pi runtime, [yokemate-pi](https://github.com/yokeloop/yokemate-pi), showed a workflow-first design was the wrong foundation and led to a memory-first successor.

**Realtime voice agent — 3 iterations** (personal R&D, _Apr 2026 — Present_) · [v1](https://github.com/prineycom/voice-agent) · [v2](https://github.com/prineycom/voice-agent-v2) · [v3](https://github.com/yokeloop/voca)

- Built a realtime speech-to-speech agent end to end — WebRTC transport, streaming STT → LLM → TTS with barge-in, and a 3D avatar whose face follows the voice's emotion — and fit the whole stack on one 12 GB GPU: cut NVIDIA Audio2Face-3D memory from 8.8 GB to ~0.4 GB by rebuilding its TensorRT engine, and facial animation from ~3 s to 81 ms per utterance with a persistent C++ inference helper.
- Gave it hands: the agent turns speech into schema-validated tool calls executed in a locked-down Docker sandbox and reports results to Telegram; v3 extends this to delegating tasks to coding agents. Every model choice — STT, LLM, TTS — passed gates I set for latency, real-time factor and VRAM, recorded across 37 ADRs; the third version was a deliberate rewrite after I judged the second over-engineered.

**Local-first agent lab** (personal, _Feb 2026 — Present_)

- Run Priney, my always-on personal assistant on Hermes Agent, self-hosted on a Raspberry Pi 5 and covering tasks, calendar, email, finances, health, knowledge and travel. Designed its Second Brain — a 226-note Obsidian vault with routing rules for where the agent reads and writes, synced through CouchDB and git — with on-device RAG over it (ONNX embeddings, SQLite vectors, incremental re-indexing), and wrote its MCP integrations and cron automations (a watchlist monitor with priorities and quiet hours, digests, backups).
- Self-hosted Qwen3.6-35B-A3B as my agents' primary model on a single 12 GB GPU (MoE expert offload, quantized KV cache, 262K context) and made the agent reliable on it: traced a silent tool-calling failure to context compression collapsing tool_call / tool_result pairs and fixed it with tool-use enforcement and compression that protects tool history, and found an upstream bug where a local LiteLLM proxy was treated as a local model, stretching stream timeouts to 30 minutes; tested LFM, Gemma and Qwen variants on the GPU and the Pi.
- Wrote [sp-cli](https://github.com/prineycom/sp-cli), an open-source Python CLI and MCP server for the Super Productivity app: 97 commands with MCP tools generated from the CLI itself, 919 tests, CI on Python 3.11–3.13; built in 2 days by an autonomous agent session on the yoke workflow.

## Professional Experience

### **YokeLoop** — **Co-founder (agent integration & client delivery)** — _Apr 2026 — Present_

_Two-founder company building LLM-agent products for small and mid-size businesses; I design the agent layer and run client deployments, my co-founder builds the hosting platform_

- Designed the least-privilege isolation model for our agent-hosting platform — a Docker sandbox per user with no Docker socket, credentials kept on the host, per-tenant data — and wrote its per-employee container guide; deploy and operate it for clients.
- Build the agent layer for clients — skill banks, MCP integrations, promptfoo evals — and co-authored the yoke Claude Code plugin and the yokemate orchestrator.

### **Talking Birds & Flying Fish** — **Tech Lead → Team Lead → Head of Development** — _Jul 2024 — Present_

_Barcelona production studio: interactive installations for corporate conference stands and museum exhibitions; clients include Microsoft. Tech Lead (Jul 2024), Team Lead (May 2025), Head of Development (Jan 2026)_

- Built the development department from scratch: started as its only web developer and grew it to 5 web and 2 Unreal Engine developers, defined the tech stack and internal packages, and set up the whole delivery process — YouTrack planning and task decomposition, an iterative cycle fitted to fixed exhibition dates, code review and CI/CD (GitHub Actions), release management, reliability engineering with e2e and soak tests for installations that run unattended for weeks, observability (Sentry, Loki, Grafana) and a documentation-first culture.
- Delivered 40 installations (25 visitor-facing) from 33 repositories — Microsoft conference stands touring 12 cities, game stations, a permanent museum exhibition — with 2,299 tracked tasks and 670 PRs, while staying hands-on (1,128 own commits); the shared `@tb-ff/web-toolkit` I co-developed is used in 18 of 33 projects.
- As developer on the museum exhibit, replaced a legacy .NET drawing recognizer with a Python OpenCV service without touching installed hardware; built a 40-case test harness, disproved my own planned fix with diagnostics and moved the remaining error class into the printed form's marker codes.

### **Sminex** — **Team Lead, Business Process Automation** — _May 2022 — Jul 2024_

- Led a team of 3 at a real-estate developer; shipped 5 web services automating construction and operational workflows, integrated with internal systems (TypeScript, NestJS, PostgreSQL, Django).

### **SU-10** — **Tech Lead, Construction Process Automation** — _Aug 2021 — May 2022_

- Led a team of 3 from process setup to MVP on the Autodesk Forge (BIM) API; 1st place at the Autodesk Forge Hackathon 2021.

**Earlier roles**: RoadAR — point-cloud and SLAM data visualization (_2022_, part-time); DataMap Geodata Laboratory — GIS web services (React, Node.js, AWS, Docker), 5+ client projects, trained 20+ students (_2018 — 2021_); frontend and web roles (_2014 — 2018_).

## Skills & Education

- **Agents & orchestration**: Claude Code (skills, subagents, hooks), Claude Agent SDK (Anthropic API), Hermes Agent, pi, MCP servers, agentic and multi-agent workflows (orchestrator-worker, reviewer loops, human-in-the-loop gates), prompt and context engineering, structured outputs, tool / function calling, model routing
- **Evals, guardrails & observability**: promptfoo with LLM-as-judge, test harnesses, PreToolUse guards, per-user sandboxes, least-privilege access, LangSmith tracing, Sentry, Loki, Grafana
- **RAG & inference**: retrieval (chunking, multilingual ONNX embeddings, vector stores, SharePoint via Microsoft Graph), llama.cpp (quantization, MoE offload, speculative decoding), TensorRT, Whisper and TTS models, ComfyUI
- **Model providers & stack**: Anthropic, OpenAI-compatible APIs via LiteLLM, open-weight Qwen / LFM / Gemma self-hosted; Python (FastAPI, pytest), TypeScript, React, Electron, PostgreSQL, Supabase, SQLite, Docker, GitHub Actions CI/CD, Dokploy, Tailscale; workstation: Arch Linux (Omarchy), Neovim, herdr
- **Education & languages**: Information Systems and Technologies, MIIGAiK, Moscow (2013 — 2017); Russian (native), English (fluent), Serbian (basic)
