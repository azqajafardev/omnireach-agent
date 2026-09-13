<h1 align="center">👁️ omnireach-agent</h1>

> **Project name:** omnireach-agent. The repository URLs, star counts, sponsors, contact details, and `agent-reach` CLI commands below belong to the original Agent Reach project. Use the original command names when installing or configuring it.

<p align="center"><strong>Give your AI agent internet access in one step</strong></p>

<p align="center">We select, install, and check the most reliable connection methods available today. When platforms change, the integration can change with them.</p>

<p align="center">
  <a href="https://trendshift.io/repositories/24387"><img src="https://trendshift.io/api/badge/repositories/24387" alt="Upstream Trendshift repository ranking"></a>
  <a href="https://star-history.com/#Panniantong/Agent-Reach&Date"><img src="https://api.star-history.com/badge?repo=Panniantong/Agent-Reach" alt="Upstream star history" width="196" height="55"></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="Upstream GitHub stars"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> · <a href="#supported-platforms">Supported Platforms</a> · <a href="#design">Design</a> · <a href="docs/README_ja.md">日本語</a> · <a href="docs/README_ko.md">한국어</a>
</p>

---

## ❤️ Upstream Sponsors

> [Interested in appearing here?](mailto:pnt01@foxmail.com) Contact the original project team.

<details open>
<summary>Show or hide sponsors</summary>

<table>
<tr><td width="180" align="center"><a href="https://www.browseract.ai/Agent"><img src="docs/assets/sponsors/browseract.png" alt="BrowserAct" width="150"></a></td><td><a href="https://www.browseract.ai/Agent">BrowserAct</a> extracts data from sites such as Amazon, LinkedIn, X, and Google Maps. Describe the task in natural language; its browser agent explores the site, tests workflows, creates reusable data-collection bots, and returns structured results. It provides browser stealth, CAPTCHA handling, and residential proxies. New accounts receive 1,000 credits. <a href="https://www.browseract.ai/Agent">Try it</a>.</td></tr>
<tr><td width="180" align="center"><a href="https://www.tencentcloud.com/act/pro/intl-openclaw?referral_code=G76Y819A&amp;lang=zh&amp;pg="><img src="docs/assets/sponsors/tencent-cloud.svg" alt="Tencent Cloud OpenClaw" width="150"></a></td><td>Tencent Cloud Lighthouse offers a way to deploy OpenClaw and connect it to the upstream Agent Reach integration.</td></tr>
<tr><td width="180" align="center"><a href="https://www.coreclaw.com/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=Reach&amp;utm_term=Reach&amp;utm_id=Reach"><img src="docs/assets/sponsors/coreclaw.png" alt="CoreClaw" width="150"></a></td><td><a href="https://www.coreclaw.com/?utm_source=github&amp;utm_medium=referral&amp;utm_campaign=Reach&amp;utm_term=Reach&amp;utm_id=Reach">CoreClaw</a> provides 100+ ready-made data-collection tools for Amazon, TikTok, Google Maps, Instagram, Facebook, and YouTube. It supports JSON/CSV export and charges for successful results. A $3 test credit is advertised on its site.</td></tr>
<tr><td width="180" align="center"><a href="https://www.ucloud.cn/site/active/astraflow?ytag=geo_waituo_Agent"><img src="docs/assets/sponsors/astraflow.png" alt="UCloud AstraFlow" width="150"></a></td><td><a href="https://www.ucloud.cn/site/active/astraflow?ytag=geo_waituo_Agent">UCloud AstraFlow</a> offers access to 200+ models, including Kimi, DeepSeek, Qwen, and GLM.</td></tr>
</table>
</details>

---

## Why omnireach-agent?

AI agents can write code, edit documents, and manage projects, yet practical web access still presents obstacles:

- 📺 “Summarize this YouTube tutorial” → subtitles may not be available.
- 🐦 “Find opinions about this product on X” → search APIs may require payment.
- 📖 “Find similar bugs on Reddit” → server IPs can receive a 403 response.
- 📕 “Check reviews on Xiaohongshu” → content often requires a login.
- 📺 “Summarize this Bilibili video” → generic download tools can be blocked.
- 🔍 “Compare the latest LLM frameworks” → useful search may be costly or unreliable.
- 🌐 “Read this webpage” → a basic fetch returns hard-to-read HTML.
- 📦 “Explain this GitHub repository and its issues” → authentication can be tedious.
- 📡 “Follow these RSS feeds” → otherwise requires installing libraries and writing code.

Each platform has its own APIs, restrictions, accounts, and data formats. The original installation guide gives your agent a way to set up the appropriate tools:

```text
Install the upstream Agent Reach integration by following https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

For updates:

```text
Update the upstream Agent Reach integration by following https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

### ✅ Before You Start

| Topic | Details |
|---|---|
| 💰 **Cost** | The upstream tools are open source and its documented APIs are free; a server proxy may cost around $1/month. A local computer does not need one. |
| 🔒 **Privacy** | Cookies stay on your machine according to the upstream design; inspect the open-source code before supplying credentials. |
| 🔄 **Fallbacks** | Each platform has a preferred backend and alternatives. For example, the upstream README describes moving Bilibili from yt-dlp to bili-cli after blocks observed in June 2026. |
| 🤖 **Compatibility** | Works with agents capable of running shell commands, including Claude Code, OpenClaw, Cursor, and Windsurf. |
| 🩺 **Diagnostics** | `agent-reach doctor` reports which channels work and how to fix those that do not. |

## Supported Platforms

| Platform | Available after installation | Additional configuration | How to configure |
|---|---|---|---|
| 🌐 **Webpages** | Read webpages | — | None |
| 📺 **YouTube** | Subtitles and video search | — | None |
| 📡 **RSS** | RSS/Atom feeds | — | None |
| 🔍 **Web search** | — | Semantic web search | Automatic MCP configuration; no key documented |
| 📦 **GitHub** | Public repositories and search | Private repositories, issues, PRs, forks | Ask your agent to log in to GitHub |
| 🐦 **Twitter/X** | Individual posts | Search, timelines, long posts | Ask your agent to configure Twitter |
| 📺 **Bilibili** | Search and video details via bili-cli | Subtitles via OpenCLI | Ask your agent to configure Bilibili |
| 📖 **Reddit** | —; anonymous access is blocked in the upstream design | Posts, comments, search | OpenCLI with a desktop browser session or rdt-cli with a cookie |
| 📘 **Facebook** | — | Search, pages, feed, group lists | OpenCLI using an existing Chrome login |
| 📷 **Instagram** | — | User search, profiles, recent posts, Explore | OpenCLI using an existing Chrome login |
| 📕 **Xiaohongshu** | — | Search, reading, comments | Existing Chrome session for OpenCLI; manual Cookie-Editor export for alternative backends |
| 💼 **LinkedIn** | Public pages via Jina Reader | Profiles, company pages, job search | Ask your agent to configure LinkedIn |
| 💻 **V2EX** | Trending posts, node posts, replies, users | — | None |
| 📈 **Xueqiu** | Stock quotes, search, trending posts | — | Ask your agent to configure Xueqiu |
| 🎙️ **Xiaoyuzhou podcasts** | — | Whisper transcription | Ask your agent to configure Xiaoyuzhou; free key described upstream |

> To set up a platform, tell your agent “Help me configure [platform].” Twitter cookies must be exported manually with Cookie-Editor. The upstream integration does not sign in to Xiaohongshu on your behalf or read its browser cookies; OpenCLI uses only an existing Chrome session controlled by the user. `agent-reach configure xhs-cookies` does not inject cookies into Chrome or OpenCLI. Without an existing session, manually export cookies for xiaohongshu-mcp or another supported tool.
>
> Saving Twitter cookies only lets `agent-reach doctor` verify the configuration. To use the upstream `twitter` CLI directly, set `TWITTER_AUTH_TOKEN` and `TWITTER_CT0` in that process's environment. A local machine does not need a proxy; server deployments may need one.

## Quick Start

> ⚠️ **OpenClaw:** The upstream integration needs the agent to execute shell commands such as `pip install`, `mcporter`, and `twitter`. If OpenClaw uses its default `messaging` tools profile, enable execution first:
>
> ```bash
> openclaw config set tools.profile "coding"
> ```
>
> Alternatively, set `"tools": { "profile": "coding" }` in `~/.openclaw/openclaw.json`, restart with `openclaw gateway restart`, and start a new conversation. Other supported agents are unaffected by this OpenClaw setting.

Send your AI agent this instruction:

```text
Install the upstream Agent Reach integration by following https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

To update an existing installation:

```text
Update the upstream Agent Reach integration by following https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

By default, `agent-reach install` checks the environment without changing system packages or configuration. Ask your agent to inspect the upstream install guide first; use `agent-reach install --system` only when you explicitly intend to install dependencies and write configuration.

<details>
<summary>What does installation do?</summary>

1. Installs the `agent-reach` CLI from the upstream repository, including yt-dlp and feedparser. Do **not** install the unrelated package with the same name from PyPI.
2. Checks for Node.js, GitHub CLI (`gh`), and mcporter and reports missing dependencies.
3. Installs system dependencies and configures Exa through MCP only when `--system` is specified.
4. Detects whether the host is a local computer or a server and recommends corresponding settings.
5. Writes SKILL.md into the agent's skills directory only with `--system`.
6. Enables six zero-configuration channels by default; the agent asks before setting up login-dependent services such as Xiaohongshu, Twitter, Reddit, Facebook, or Instagram.

Run `agent-reach doctor` afterward to inspect each channel and its selected backend.
</details>

## Use It After Installation

Ask your agent in plain English:

- “Read this link” → Jina Reader via `curl https://r.jina.ai/URL`.
- “What does this GitHub repository do?” → `gh repo view owner/repo`.
- “Summarize this YouTube video” → extract subtitles with `yt-dlp`.
- “Search Bilibili for AI tutorials” → `bili search` without a login.
- “Search the web for LLM framework comparisons” → Exa semantic search.
- “Subscribe to this RSS feed” → parse it with `feedparser`.

You do not need to memorize commands. An agent that has read SKILL.md can select the appropriate tool. For login-dependent platforms, ask it to help you configure the specific service.

## Design

**omnireach-agent is a capability layer:** it selects, installs, diagnoses, and routes among upstream tools. The agent invokes those tools directly for reading and search. When one access method stops working, the preferred backend can be changed without rewriting the agent's entire workflow.

### 🔌 Preferred and Fallback Backends

`agent-reach doctor` tests candidate backends in order and identifies the first fully usable one; it does more than check whether a command exists. It also reports actionable fixes for broken configurations.

```text
channels/
├── web.py          → Jina Reader
├── twitter.py      → twitter-cli ▸ OpenCLI ▸ bird
├── youtube.py      → yt-dlp
├── github.py       → gh CLI
├── bilibili.py     → bili-cli ▸ OpenCLI ▸ search API (yt-dlp retired for Bilibili)
├── reddit.py       → OpenCLI ▸ rdt-cli (login required)
├── facebook.py     → OpenCLI (desktop browser session)
├── instagram.py    → OpenCLI (desktop browser session)
├── xiaohongshu.py  → OpenCLI ▸ xiaohongshu-mcp ▸ xhs-cli
├── linkedin.py     → mcp-server-linkedin ▸ Jina Reader
├── rss.py          → feedparser
├── exa_search.py   → Exa via mcporter
└── __init__.py     → channel registration for diagnostics
```

### Current Upstream Backend Choices

| Task | Preferred | Fallback | Reason given upstream |
|---|---|---|---|
| Read webpages | [Jina Reader](https://github.com/jina-ai/reader) | — | Free; no API key |
| Read X | [twitter-cli](https://github.com/public-clis/twitter-cli) | [OpenCLI](https://github.com/jackwener/opencli) | CLI search, with browser-session fallback |
| Reddit | [OpenCLI](https://github.com/jackwener/opencli) on desktop | [rdt-cli](https://github.com/public-clis/rdt-cli) | Anonymous access is blocked in the upstream setup |
| Facebook | [OpenCLI](https://github.com/jackwener/opencli) on desktop | — | Reuses a browser session |
| Instagram | [OpenCLI](https://github.com/jackwener/opencli) on desktop | Official Graph API for approved Business/Creator accounts | Reuses a real browser session |
| YouTube subtitles/search | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | — | Upstream's selected YouTube tool; no longer used for Bilibili |
| Bilibili | [bili-cli](https://github.com/public-clis/bilibili-cli) | OpenCLI ▸ search API | Upstream reports yt-dlp was blocked there in June 2026 |
| Web search | [Exa](https://exa.ai) via [mcporter](https://github.com/nicobailon/mcporter) | — | Semantic search through MCP |
| GitHub | [gh CLI](https://cli.github.com) | — | Official GitHub tool with broader capabilities after login |
| RSS | [feedparser](https://github.com/kurtmckee/feedparser) | — | Python feed parsing library |
| Xiaohongshu | [OpenCLI](https://github.com/jackwener/opencli) on desktop | [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) on server ▸ xhs-cli | Existing browser session or manually exported cookies |
| LinkedIn | [mcp-server-linkedin](https://github.com/stickerdaniel/linkedin-mcp-server) | Jina Reader | MCP integration or public-page reading |

These are the backend choices stated in the supplied upstream README; run `agent-reach doctor` to see what works in your environment.

## Security

| Measure | Description |
|---|---|
| 🔒 **Local credentials** | The upstream configuration stores cookies and tokens in `~/.agent-reach/config.yaml` with file permissions set to 600. |
| 🛡️ **Safe default** | `agent-reach install` checks the system; `--system` explicitly permits dependency installation and configuration writes. |
| 👀 **Open source** | Source and dependency tools can be reviewed. |
| 🔍 **Dry run** | `agent-reach install --dry-run` previews planned operations. |
| 🧩 **Modular channels** | Each platform has its own channel file. |

### 🍪 Cookie Safety

Platforms can detect automation and restrict or ban accounts. A dedicated account can reduce the impact of a ban or leaked session cookie; a cookie grants access similar to an active login. Handle cookies as sensitive credentials.

### 📦 Installation Modes

| Mode | Command | What it does |
|---|---|---|
| Default check | `agent-reach install --env=auto` | Read-only environment check; lists missing dependencies |
| Install dependencies | `agent-reach install --env=auto --system` | Modifies the machine when explicitly requested |
| Safe alias | `agent-reach install --env=auto --safe` | Same as default check |
| Preview | `agent-reach install --env=auto --dry-run` | Shows planned operations |

### 🗑️ Uninstall

```bash
agent-reach uninstall
```

This removes `~/.agent-reach/` (including tokens and cookies), the agent skill files, and mcporter MCP configuration.

```bash
# Preview removal without deleting anything
agent-reach uninstall --dry-run

# Remove skill files but preserve token configuration
agent-reach uninstall --keep-config
```

To remove the Python package: `pip uninstall agent-reach`.

## ⭐ Upstream Maintenance

The original author describes using and maintaining Agent Reach personally, adding requested channels and addressing platform or API changes. The star counts and maintenance claims in the upstream links refer to that original project.

## Acknowledgments

[OpenCLI](https://github.com/jackwener/opencli) · [twitter-cli](https://github.com/public-clis/twitter-cli) · [rdt-cli](https://github.com/public-clis/rdt-cli) · [xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp) · [xhs-cli](https://github.com/jackwener/xiaohongshu-cli) · [bili-cli](https://github.com/public-clis/bilibili-cli) · [yt-dlp](https://github.com/yt-dlp/yt-dlp) · [Jina Reader](https://github.com/jina-ai/reader) · [Exa](https://exa.ai) · [mcporter](https://github.com/nicobailon/mcporter) · [feedparser](https://github.com/kurtmckee/feedparser) · [mcp-server-linkedin](https://github.com/stickerdaniel/linkedin-mcp-server)

## Original Project Contact

- 📧 **Email:** pnt01@foxmail.com
- 🐦 **X:** [@Neo_Reidlab](https://x.com/Neo_Reidlab)
- **Original author’s business collaboration:** Contact the original author through the channels above for custom agent automation in operations, marketing, research, data handling, or other workflows. In WeChat, the original README suggests noting your business need, your builder role, or a request to join its group.

<p align="center"><img src="docs/wechat-group-qr.jpg" width="280" alt="Original project WeChat QR code"></p>

Report upstream bugs and feature requests through its [GitHub Issues](https://github.com/Panniantong/Agent-Reach/issues).

## License

[MIT](LICENSE)

## Related Upstream Links

[Agent Skills Hub](https://agentskillshub.top/) — A directory of Claude skills and MCP servers with safety and quality ratings.

[AtomGit mirror](https://atomgit.com/qq_51337814/Agent-Reach) — Mirror of the original Agent Reach repository for access in China.

## Upstream Star History

[View the original project's star history](https://star-history.com/#Panniantong/Agent-Reach&Date).
