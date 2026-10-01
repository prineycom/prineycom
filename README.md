# Pavel Donin

**AI Engineer — Agent Orchestration, LLM Tooling**

_Builds the agent harnesses he ships with: ticket-driven multi-repo orchestration, MCP servers, eval suites for agent skills, a local-first voice agent · 10+ years in software, 5 of them leading teams_

## Contact

[doninpr@gmail.com](mailto:doninpr@gmail.com) • [linkedin.com/in/doninpr](https://www.linkedin.com/in/doninpr) • [t.me/doninpr](https://t.me/doninpr) • [github.com/prineycom](https://github.com/prineycom) • [CV.pdf](https://github.com/prineycom/prineycom/raw/main/CV.pdf)  
Novi Sad, Serbia (CET, UTC+1) · remote · open to full-time roles worldwide

## Professional Summary

Head of Development at an interactive-installation studio and co-founder of YokeLoop, where I take agent systems from specification to client deployment. My daily delivery runs through an orchestrator I co-built on Claude Code: a ticket from YouTrack or GitHub Issues goes through planning, agent implementation in an isolated worktree, an independent review and a human-confirmed merge — 46 tickets across 4 organizations in its first 6.5 weeks. Around it: Hermes agents running for real users, MCP servers, eval suites that check whether an agent picked the right skill and tool, and three iterations of a realtime voice agent on local models. I measure before I claim: eval harnesses, documented negative results, and metrics dropped when they do not survive a re-check. Underneath is 10+ years of full-stack engineering (TypeScript, React, Electron, Python) and production computer vision on physical sites — the model ships as a complete product, not a notebook.

## AI Engineering Projects

**yokemate — multi-repo AI development orchestrator on Claude Code** (YokeLoop, co-built with [Ivan Hilkov](https://github.com/ivan-hilckov), _Aug 2026 — Present_)

- One Claude Code session drives a pool of repositories across 4 organizations, with tickets from 3 YouTrack instances and GitHub Issues. Each ticket moves through /plan → /do → /review → /ship; every mode runs in its own terminal pane with its own stamped identity, and stage moves are compare-and-set transitions in SQLite.
- Safety is enforced, not requested: task tabs run unattended, and a PreToolUse guard holds the rules instead of permission prompts. The merge stays a single human decision. Read-only scout and writer subagents isolate context; each project's passport sets the model for its tickets.
- Several machines run as equal peers: state stays local, observable facts (tracker, PRs, plans, journal) travel through git.
- My instance in production: 46 tickets planned, implemented, reviewed and merged in 6.5 weeks across about 18 projects; 134 plans in the knowledge base.
- Lineage, with the failures kept: [yoke](https://github.com/yokeloop/yoke) (co-authored Claude Code plugin, the `.yoke/` artifact convention) → yokemate → a rebuild on the pi agent runtime (14k lines of TypeScript, 421 tests; dropped) → mypi, a memory-first, request-centric successor now in early design.

**Hermes agents for clients** (YokeLoop, _May 2026 — Present_)

- Specified hermes-orchestration, a platform for hosting isolated AI agents on bare metal (built by my partner): a Hermes profile per user, a Docker sandbox per profile with no Docker socket and credentials kept on the host, access through Telegram. I deploy and operate it for clients.
- **Aleen** — a medical-data assistant: a Hermes agent as the interface to an MCP-based RAG system over health records, with per-profile data isolation; 6 active users. I administer the deployment on the client's server and tune the harness and agents.
- **Talking Birds** — a skill bank rolled out to employee agent profiles (worklog export from YouTrack, budget and CG estimates, freelancer database), with an eval suite on promptfoo and the Claude Agent SDK provider: did the agent load the skill, call the right tool with the right flags, explain it correctly (LLM-as-judge), within a spend cap, without modifying the bank.
- Debugged a Hermes agent that silently stopped calling tools: context compression was collapsing tool_call / tool_result pairs into one-line summaries. Found an upstream bug where a LiteLLM proxy on localhost is treated as a local model, raising the stream timeout to 1,800 s and disabling the stale-stream detector.

**Realtime voice agent — 3 iterations** (personal R&D, _Apr 2026 — Present_) · [v1](https://github.com/prineycom/voice-agent) · [v2](https://github.com/prineycom/voice-agent-v2) · [VOCA](https://github.com/yokeloop/voca)

- v1: a hybrid on 3 nodes — Raspberry Pi 5 (LiveKit SFU, agent worker, LiteLLM, Hermes over MCP), an RTX 4070 desktop (faster-whisper large-v3-turbo STT, Qwen3-TTS) and a cloud LLM; Live2D avatar, task delegation to Hermes; 22 ADRs. Measured cloud time-to-first-token for voice and rejected models that could not meet the budget.
- v2: local-first on one host — Silero VAD → Whisper → LFM2.5-2.6B (Q4_K_M, llama.cpp) → TTS, with barge-in invalidation and correlation keys on every async boundary. Delegation through JSON-Schema-enforced decisions over 14 fixed tools, executed in a rootless Docker sandbox (all capabilities dropped, no socket). Benchmarked the model on CPU and GPU at concurrency 1–4: 213 tok/s and 3.1 s TTFT on GPU at concurrency 1, 18 tok/s on CPU — served on GPU only.
- v3 (VOCA): a deliberate rewrite after reviewing v2 as over-engineered — FastRTC, LiteLLM with LangSmith tracing, a hand-written LLM loop, and a single `delegate(agent, task)` tool to coding agents (Hermes, pi, OpenClaw); target ~500 ms voice-to-voice.

**[sp-cli](https://github.com/prineycom/sp-cli) — CLI and MCP server for Super Productivity** (_Sep 2026_)

- Edits the app's WebDAV sync file directly (op-log, vector clocks, ETag / If-Match retries, rotating backups), so changes reach the phone through normal sync with no conflict dialog. 97 commands; the MCP server generates its tools from the argparse tree, 1:1 with the CLI.
- 919 tests, CI on Python 3.11–3.13. Built in 2 days by an autonomous agent session — 15 areas, each through plan → implementation → review → fixes — and verified against a live phone sync.

## Professional Experience

### **YokeLoop** — **Co-founder** — _Apr 2026 — Present_

_Two-founder company building LLM-agent products and tooling for small and mid-size businesses; I own product, specifications and client integration, my partner owns engineering_

- Specified the agent-hosting platform and integrate it at clients (Aleen, Talking Birds); co-author of the yoke plugin and the yokemate orchestrator.

### **Talking Birds & Flying Fish** — **Head of Development** — _Jan 2026 — Present_

_Barcelona production studio: interactive installations for corporate conference stands and museum exhibitions; clients include Microsoft. Team Lead Manager from May 2025, Tech Lead Software Engineer from Jul 2024_

- Grew the web team from 2 to 5 developers and led them alongside 2 Unreal Engine developers. Over 2 years the team delivered 40 installations (25 visitor-facing) in 12 experience families from 33 repositories — Microsoft conference stands touring 12 cities, game stations, a permanent museum exhibition — with 2,299 tracked tasks and 670 pull requests.
- Brought AI-native delivery to the studio: added the first agent configuration on 28 Aug 2025; a year later it was in 22 of 33 repositories, and every 2026 project started with it. Introduced the plan → worktree → independent review → ship workflow, which the team adopted beyond my own repositories.
- Built the company's data core on self-hosted Supabase, with the schema rolled out by an agent through the Supabase MCP server under step-by-step verification. Added an hourly automation service (Python, Docker) syncing Postgres to Excel in SharePoint through Microsoft Graph, in production since Sep 2026. Researched LLM access to the studio's CG production system (API, MCP, auth), marking every capability as confirmed or not.
- As developer on the museum exhibit: replaced a legacy .NET recognizer of children's drawings with a Python service (OpenCV ArUco markers, homography, mask cut-out, FastAPI, single-exe build with a CI smoke test) without changing the installed hardware. Built a 40-case test harness (5 photos × 8 angles), disproved my own planned fix with diagnostics, reverted a regressing change, and moved the remaining error class to the printed form's marker codes, documented in an ADR.
- Set up centralized logging (Loki, Grafana) and the shared `@tb-ff/web-toolkit` library, used in 18 of 33 projects. Wrote the studio atlas: an evidence-tagged analysis of all web repositories, tracker and PR history that maps reusable mechanics to what the studio sells. 1,128 own commits in 24 of 33 repositories.

### **Sminex** — **Senior Full Stack Developer, Tech Lead** — _May 2022 — Jul 2024_

- Web services automating construction processes for a real-estate developer: architecture, integration with internal databases and services, a team of 3, hiring; shipped 5 services to client departments. TypeScript, React, Node.js (NestJS, Express), PostgreSQL, Python (Django), Autodesk Forge.

### **RoadAR** — **Frontend Developer** — _Feb 2022 — Sep 2022_ (part-time, alongside SU-10 and Sminex)

- Web visualization of point clouds and spatial data collected with SLAM and machine-learning pipelines; React, deck.gl, WebGL, Cesium.

### **SU-10** — **Full-stack Developer, Tech Lead** — _Aug 2021 — May 2022_

- Construction automation service on the Autodesk Forge API: processes built from scratch, a team of 3, MVP release. 1st place at the Autodesk Forge Hackathon 2021 (Cloud Collaboration); Autodesk Virtual Forge Accelerator participant.

### **DataMap Geodata Laboratory** — **Frontend Web Developer** — _Mar 2018 — Aug 2021_

- GIS web services and geodata collection end to end; 5+ client projects through Upwork; a year-long web application release; trained 20+ students in GIS data collection and co-organized 2 hackathons. React, Mapbox, CesiumJS, OpenLayers, Leaflet, deck.gl, Node.js, Python, Docker, AWS.

**Earlier roles**: AT Consulting — Frontend Developer, customer portal for a mobile operator (_2017 — 2018_); freelance web development (_2015 — 2016_); PHP internship (_2014_).

## Technical Skills

- **Agent engineering**: Claude Code (skills, subagents, PreToolUse and SessionStart hooks, CLAUDE.md), pi agent runtime, Hermes Agent, MCP servers (FastMCP, stdio, generated tools), agent orchestration with human-in-the-loop merge gates, model routing per project, structured outputs and tool calling
- **Evals & reliability**: promptfoo with LLM-as-judge and the Claude Agent SDK provider, test harnesses for CV and agent behavior, LangSmith tracing, failure-mode analysis, ADR-driven development
- **LLM infrastructure & local inference**: LiteLLM, Open WebUI, llama.cpp (quantization, CPU/GPU offload, MoE vs dense), LFM2.5, Qwen, Whisper, Silero, Docker sandboxes for agents, Tailscale, Dokploy, systemd
- **Voice & vision**: LiveKit, FastRTC / WebRTC, VAD → STT → LLM → TTS pipelines, barge-in; OpenCV (ArUco, homography), camera capture on installation tablets
- **Product stack**: TypeScript, React 19, Electron, Node.js, Python (FastAPI, Django), PostgreSQL, Supabase, SQLite, three.js / WebGL, PixiJS, Cesium, deck.gl, Playwright, Vitest, pytest, GitHub Actions
- **Leadership**: team building and hiring, delivery for fixed exhibition deadlines, YouTrack processes, monitoring (Loki, Grafana, Sentry), technical presentations
- **Languages**: Russian (native), English (fluent, professional working), Serbian (basic)

## Open Source

- [prineycom/voice-agent](https://github.com/prineycom/voice-agent), [voice-agent-v2](https://github.com/prineycom/voice-agent-v2), [yokeloop/voca](https://github.com/yokeloop/voca) — three generations of a realtime voice agent
- [prineycom/sp-cli](https://github.com/prineycom/sp-cli) — CLI and MCP server for Super Productivity
- [yokeloop/yoke](https://github.com/yokeloop/yoke) — Claude Code plugin and marketplace of skills for the full development loop (co-author)
- [prineycom/llama-tray](https://github.com/prineycom/llama-tray) — Windows tray controller for llama.cpp's server

## Education

**Information Systems and Technologies** — Moscow State University of Geodesy and Cartography (MIIGAiK), 2013 — 2017

## Availability

- Open to full-time AI Engineer, Agent / LLM Platform Engineer and Applied AI roles; remote, worldwide; B2B contract or employer of record.
