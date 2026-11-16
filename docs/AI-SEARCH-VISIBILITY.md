# AI search visibility — 16 November 2026

The portfolio is prepared for search and retrieval by ChatGPT, Claude, Perplexity and other assistants that use the public web. This builds on the published 40-page static website, linked professional identity, verified credits, international service descriptions and successfully processed Google/Bing sitemaps. Allowing access does not guarantee that a provider will crawl, index, cite or recommend it.

## Provider-specific implementation

| Service | Website configuration | Official reference and limits |
| --- | --- | --- |
| ChatGPT Search | Explicit `OAI-SearchBot` allow; public static content and canonical sitemap | [OpenAI crawlers](https://developers.openai.com/api/docs/bots). Search access is independent of `GPTBot` model training. |
| ChatGPT user retrieval | Explicit `ChatGPT-User` allow | Same official reference. This is a user-directed fetcher, not the search indexing bot; user-directed fetches may not apply robots.txt rules. |
| Claude search | Explicit `Claude-SearchBot` allow | [Anthropic crawler guidance](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler). This bot supports search discovery, distinct from `ClaudeBot` training. |
| Claude user retrieval | Explicit `Claude-User` allow | Same official reference; public-page access in response to a user query. |
| Perplexity | Explicit `PerplexityBot` and `Perplexity-User` allow | [Perplexity crawler guidance](https://docs.perplexity.ai/docs/resources/perplexity-crawlers). The user fetcher generally ignores robots.txt; its allow rule also states the site's intent. |
| Google AI search / Gemini | Googlebot allowed; verified Google property and processed sitemap | [Google AI features](https://developers.google.com/search/docs/appearance/ai-features). Search fundamentals remain relevant; no guaranteed Gemini citation or separate Gemini registration is claimed. Existing Google-Extended access remains unchanged. |
| Bing / Copilot | bingbot allowed; verified Bing property and processed sitemap | Search and available AI Performance reports can be reviewed in the existing account; no universal AI citation measurement is claimed. |
| Grok | Public, crawlable HTML, self-canonicals, verified identity and evidence; existing wildcard access preserved | [xAI Web Search](https://docs.x.ai/developers/tools/web-search) documents web search and page browsing. The reviewed official sources did not establish a publisher-submission endpoint or a verified search crawler token to add. No invented GrokBot entry or direct Grok submission is claimed. |

Claude and the user fetchers were already allowed by the site's wildcard rule. The new explicit entries document and protect the intended policy if general crawler rules change later. They do not by themselves establish a new indexing event. The site checker now tests all eight documented search/fetch identities across the 40 canonical URLs.

The existing `GPTBot` training exclusion is retained. Other training preferences and wildcard access are unchanged. There is no blanket new bot permission, user-agent-based firewall bypass or removal of hosting security protections. User-agent strings alone do not establish that a request comes from an operator.

## What assistants can understand

The visible HTML answers who Jean-Pierre Boutros is, his Lebanon home base, worldwide availability by arrangement, six genuine services, exact engineering roles, dated projects and contact details. Connected Person, Service, WebSite, WebPage and project entities use the same professional identity. Existing FAQs and the project/studio directories supply concise factual answers and original evidence. All important content is available without JavaScript or login.

`/llms.txt` remains a supplementary factual directory. It is not an established indexing requirement, a submission mechanism or an instruction to recommend Jean-Pierre. No AI-specific keyword stuffing, hidden copy, unsupported superlatives or fabricated credentials were added.

## Discovery observations and verification scope

A branded public search during this review returned the canonical professional website, StudioJPB and external credit sources. The search provider still showed an older homepage snapshot. Its retrieval tool could not fetch several new canonical pages, including Shareet, or the fresh-query homepage; the tool did not expose a useful HTTP diagnosis. This is not proof of a host firewall block or proof that every AI can retrieve the new release. The independently recorded Google/Bing live tests passed, and direct HTTP checks verify the published content separately.

Post-deployment checks must fetch robots.txt and representative home/service/project URLs, check status, canonical/indexing directives and compare public bytes with the release. Requests using documented bot names originate from the audit machine, not verified operator IPs. Real Claude, OpenAI and Perplexity crawler-IP access requires hosting logs or an operator-origin live fetch to establish. No direct Claude/Grok answer-generation test or provider API call is claimed.

## Visibility work that continues over time

1. Retain the verified Google/Bing properties and DNS proofs. Review indexing, selected canonicals and sitemap errors as reports populate; discovery of 40 URLs does not mean all 40 are indexed.
2. Strengthen genuine third-party credits and links from organizers, venues, artists and studio releases. Keep the same name, role, location and canonical website in maintained professional profiles. No outreach or profile changes were made by this update.
3. Publish useful, confirmed project details and photographs as work is completed. Keep FOH, monitors, recording and studio-only credits precise.
4. Review available search queries, countries, service pages, identifiable AI referrals, Bing AI Performance and qualified international inquiries. Log occasional dated AI-search samples using non-leading professional queries. Results vary; one answer is not a stable rank.
5. Recheck current official crawler documentation and investigate genuine blocked operator requests using verified IP sources before changing hosting rules. Do not disable security based on a spoofable user-agent string.

The objective is legitimate discovery and relevant inquiries. No setting can force Claude, ChatGPT, Grok or another assistant to recommend a particular engineer, and a website deployment does not update a model's training knowledge on demand.
