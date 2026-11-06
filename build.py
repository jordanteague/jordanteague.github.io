#!/usr/bin/env python3
"""Generates the site's HTML pages from the content below. Run: python3 build.py"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "https://jordanteague.com"
EMAIL = "jordan@campbellteague.com"

SECTIONS = [
    # slug, number, name, one-line description
    ("building", "01", "Building", "Open-source AI tools that turn legal judgment into something agents can run."),
    ("writing", "02", "Writing", "Bloomberg Law columns, essays, and law review articles on law, AI, and governance."),
    ("speaking", "03", "Speaking", "The ANTIFIRM podcast, plus talks and panels on AI agents, DAOs, and legal engineering."),
    ("about", "04", "About", "Background, and how to reach me."),
]

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
           "%3Crect width='32' height='32' rx='6' fill='%231a1a1a'/%3E%3Ctext x='16' y='22' "
           "font-family='Georgia,serif' font-size='17' fill='%23f6f4ef' text-anchor='middle'%3EJT%3C/text%3E%3C/svg%3E")


def ext(href, text):
    return f'<a href="{href}">{text}<span class="ext" aria-hidden="true"> ↗</span></a>'


def layout(slug, title, description, body):
    pre = "" if slug == "" else "../"
    url = f"{SITE}/{slug + '/' if slug else ''}"
    nav = "".join(
        '<a href="%s%s/"%s>%s</a>' % (pre, s, ' aria-current="page"' if s == slug else "", name)
        for s, _, name, _ in SECTIONS
    )
    nxt = ""
    slugs = [s[0] for s in SECTIONS]
    if slug in slugs:
        i = slugs.index(slug)
        if i + 1 < len(SECTIONS):
            s, n, name, d = SECTIONS[i + 1]
            nxt = (f'<a class="next" href="{pre}{s}/"><span class="label accent">Next · {n} · {name}</span>'
                   f'<span class="teaser">{d}</span><span class="arrow" aria-hidden="true">→</span></a>')
        else:
            nxt = (f'<a class="next" href="{pre}"><span class="label accent">Back · Home</span>'
                   f'<span class="teaser">Return to the start.</span><span class="arrow" aria-hidden="true">→</span></a>')
    full_title = "Jordan Teague" if not slug else f"{title} · Jordan Teague"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#f8f7f3">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<link rel="canonical" href="{url}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site"><div class="wrap">
  <a class="name" href="{pre or './'}">Jordan Teague<span class="slash" aria-hidden="true"> /</span></a>
  <nav>{nav}</nav>
</div></header>
<main id="main" class="wrap">
{body}
{nxt}
</main>
<footer class="site"><div class="wrap">
  <p><a href="mailto:{EMAIL}">{EMAIL}</a> · <a href="https://www.linkedin.com/in/jordanteague">LinkedIn</a> · <a href="https://github.com/jordanteague">GitHub</a></p>
  <p>© 2026 Jordan Teague. Views are my own, not those of Campbell Teague or its clients.</p>
</div></footer>
<!-- Cloudflare Web Analytics --><script type='module' src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{{"token": "ef8682fee25f40e693a119872f97f20d"}}'></script><!-- End Cloudflare Web Analytics -->
</body>
</html>
"""


def page(num, name, rail, h1, intro, content):
    """Interior page: left rail with the section label, main column with the content."""
    return f"""<div class="page">
  <aside class="rail"><p class="label accent">{num} · {name}</p><p class="rail-note">{rail}</p></aside>
  <div class="col">
    <h1>{h1}</h1>
    <p class="lead">{intro}</p>
    {content}
  </div>
</div>"""


# ---------- Home ----------
index_rows = "".join(
    f'<li><a href="{s}/"><span class="num">{n}</span><span class="sec">{name}</span>'
    f'<span class="desc">{d}</span><span class="arrow" aria-hidden="true">→</span></a></li>'
    for s, n, name, d in SECTIONS
)
BLOOMBERG_2026 = "https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/legal-mentorship-was-already-broken-ai-just-made-it-obvious"
home = f"""
<section class="hero">
  <div class="hero-text">
  <h1 class="big">Lawyer, founder, and builder of legal AI systems.</h1>
  <a class="callout" href="{BLOOMBERG_2026}">Bloomberg Law · Legal Mentorship Was Already Broken. AI Just Made It Obvious. →</a>
  <p>I'm the founding partner and chief strategy officer of <a href="https://campbellteague.com/jordan-teague/">Campbell Teague</a>, a Chambers-ranked firm that advises emerging-technology organizations on questions without settled answers, from token issuance under MiCA to decentralized protocol governance.</p>
  <p>I also build the tools. My recent work turns legal judgment into something AI agents can apply consistently: trademark clearance, discovery review, and the playbooks behind them. All of it is open source.</p>
  <p class="label accent">Emerging technology law · Legal AI</p>
  </div>
  <figure class="portrait"><img src="images/portrait.jpg" alt="Portrait of Jordan Teague" width="460" height="460"><figcaption><span>Jordan Teague</span><span>Campbell Teague</span></figcaption></figure>
</section>

<section class="currently">
  <p class="label">Currently</p>
  <p><b>Practicing.</b> Advising emerging-technology organizations at <a href="https://campbellteague.com/jordan-teague/">Campbell Teague</a>.</p>
  <p><b>Building.</b> <a href="building/">Open-source Claude skills</a> for trademark clearance and discovery review.</p>
  <p><b>Writing.</b> On AI and the legal profession in <a href="writing/">Bloomberg Law</a>.</p>
</section>

<section class="index-wrap">
  <ul class="index">{index_rows}</ul>
</section>
"""

# ---------- Building ----------
def project(pid, name, label, meta, paras, link):
    rows = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in meta)
    ps = "".join(f"<p>{x}</p>" for x in paras)
    return f"""<article class="project" id="{pid}">
  <p class="label accent">{label}</p>
  <h2>{name}</h2>
  {ps}
  <dl class="meta">{rows}<div><dt>Source</dt><dd><a href="{link}">{link.replace("https://", "")}</a></dd></div></dl>
</article>"""

projects = "".join([
    project("tmrex", "TMrex", "Claude skill · Trademark clearance",
        [("Scope", "Screening-level U.S. clearance"), ("Searches", "USPTO register, web, domain names"), ("Released as", "Open source")],
        ["Screens a proposed mark and reports on registrability. It searches a local copy of the full USPTO register, about 14 million case files synced twice a day, plus the web and domain names for unregistered use."],
        "https://github.com/jordanteague/TMrex"),
    project("rogbuster", "ROGbuster", "Claude skill · Discovery review",
        [("Input", "The other side's discovery responses"), ("Output", "Gap list and meet-and-confer letter"), ("Released as", "Open source"), ("Website", '<a href="https://rogbuster.com">rogbuster.com</a>')],
        ["Reads the other side's discovery responses, flags every gap, and drafts the meet-and-confer letter."],
        "https://github.com/jordanteague/ROGbuster"),
    project("judgment-compiler", "Judgment Compiler", "Specification + Claude skill · AI playbooks",
        [("Input", "An interview or a starting draft"), ("Output", "Schema-validated playbooks"), ("Platform", "Neutral; ships with a Claude skill")],
        ["Compiles a lawyer's judgment into a structured playbook that AI review agents can apply consistently, so expertise is written down once and reused across workflows."],
        "https://github.com/jordanteague/judgment-compiler"),
    project("trademarkbench", "TrademarkBench", "Pilot benchmark · Evaluation",
        [("Question", "Can Claude predict USPTO examination outcomes?"), ("Sample", "90 applications examined after the model's training cutoff"), ("Status", "Pilot; results are directional")],
        ["Scores Claude's predictions against real examiner decisions, with and without trademark-register search."],
        "https://github.com/jordanteague/trademarkbench"),
])
also = f"""<article class="project" id="also">
  <p class="label accent">Also built</p>
  <ul class="plain">
    <li><b>Smart contracts.</b> Solidity contracts in <a href="https://github.com/lexDAO/LexCorpus/commits?author=jordanteague">LexDAO's contract library</a> and front-end code for a <a href="https://github.com/lexDAO/Kali/commits?author=jordanteague">DAO-formation app</a>.</li>
    <li><b>Earlier products.</b> iOS and SaaS apps shipped years before AI coding tools existed.</li>
  </ul>
</article>"""
building = page("01", "Building", "Open-source tools that encode legal judgment for AI agents.",
                "Legal AI, built in the open",
                "Each of these takes a piece of a lawyer's judgment and makes it something an AI agent can apply the same way every time.",
                projects + also)

# ---------- Writing ----------
WRITING = [
    ("Bloomberg Law", "2026", "Legal Mentorship Was Already Broken. AI Just Made It Obvious.", "https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/legal-mentorship-was-already-broken-ai-just-made-it-obvious", "AI and the profession"),
    ("LinkedIn", "2026", "Your AI Agent Gave the Right Answer. Did It Use the Right Context?", "https://www.linkedin.com/pulse/your-ai-agent-gave-right-answer-did-use-context-jordan-teague-rudte/", "AI agents"),
    ("Bloomberg Law", "2024", "Law Firms Should Ditch the Rigid Mindset for a Disruptive Model", "https://news.bloomberglaw.com/us-law-week/law-firms-should-ditch-the-rigid-mindset-for-a-disruptive-model", "Firm models"),
    ("Other Internet", "2022", "Effective Accountability for Uniswap Governance", "https://otherinter.net/research/uniswap-accountability/", "DAO governance"),
    ("The Defiant", "2022", "Starting a DAO in the USA? Steer Clear of DAO Legislation", "https://thedefiant.io/news/research-and-opinion/starting-a-dao-in-the-usa-steer-clear-of-dao-legislation", "DAO formation"),
    ("Case W. Res. J.L. Tech. &amp; Internet", "2012", "Saving the Spotify Revolution: Recalibrating the Power Imbalance in Digital Copyright", "https://scholarlycommons.law.case.edu/jolti/vol4/iss1/8/", "Copyright · law review"),
    ("Vand. J. Ent. &amp; Tech. L.", "2012", "Promoting Trademark's Ends and Means through Online Contributory Liability", "https://scholarship.law.vanderbilt.edu/jetlaw/vol14/iss2/6/", "Trademark · law review"),
]
def entries(rows):
    out = ""
    for outlet, year, title, url, note in rows:
        t = f'<a href="{url}">{title}</a>' if url else title
        n = f'<p class="note">{note}</p>' if note else ""
        when = outlet + (f" · {year}" if year else "")
        out += f'<li><p class="when">{when}</p><div><p class="t">{t}</p>{n}</div></li>'
    return f'<ul class="entries">{out}</ul>'

writing = page("02", "Writing", "Columns, essays, and law review articles.",
               "Selected writing",
               "On how lawyers and law firms should adapt to AI, earlier work on DAO governance, and two law review articles.",
               entries(WRITING))

# ---------- Speaking ----------
SPEAKING = [
    ("ANTIFIRM", "2026", "ANTIFIRM podcast", "https://antifirm.com/", "Co-host, with George Campbell. A podcast about the things that sound boring, until they're your problem."),
    ("Fordham Law School", "2024", "Building for a Bright Future from a Dark Forest", None, "Blockchain Regulatory Symposium. Panelist on AI agent personhood."),
    ("ETHDenver", "2024", "AI, agents, DAOs, and smart contracts", None, "Law at the Limits. AI-controlled capital, manipulation risk, and who bears responsibility when AI acts for a DAO."),
    ("Greenville Bar Assn.", "2024", "The Intelligence Is Artificial, but the Risks Are Real", None, "Year-end CLE on AI over-reliance and practical risk mitigation."),
    ("DAOPlanet NYC", "2023", "Legal engineering and decentralized governance", None, ""),
    ("Law of Code", "2022", "DAO structuring and legal engineering", "https://podcasts.apple.com/us/podcast/49-jordan-teague-dao-structuring-legal-engineering/id1578287932?i=1000566269454", "Podcast"),
    ("The Encrypted Economy", "2022", "Taking the “ow” out of DAOs", "https://podcasts.apple.com/us/podcast/taking-the-ow-out-of-daos-ross-campbell-and/id1541074732?i=1000555577411", "Podcast"),
    ("American Bar Assn.", "2022", "Legal Governance of Digital Autonomous Organizations", None, "CLE webinar. Panelist."),
]
speaking = page("03", "Speaking", "Talks, panels, and podcasts.",
                "Talks and panels",
                "On AI agents, decentralized governance, and the practice of legal engineering.",
                entries(SPEAKING))

# ---------- About ----------
TIMELINE = [
    ("2016–now", "Campbell Teague", "Founding Partner & Chief Strategy Officer", True),
    ("2012–2016", "Burr &amp; Forman LLP", "Associate", False),
    ("J.D.", "Vanderbilt Law School", "Senior Technology Editor, Journal of Entertainment &amp; Technology Law", False),
    ("B.S.", "Furman University", "Mathematics-Economics, magna cum laude", False),
]
tl = "".join(f'<li class="{"on" if cur else ""}"><span class="yr">{y}</span><b>{org}</b><span>{role}</span></li>' for y, org, role, cur in TIMELINE)
about = page("04", "About", f'<ul class="timeline">{tl}</ul>',
             "Background",
             "I've practiced law since 2012 and co-founded Campbell Teague in 2016.",
             f"""
<h2>Bio</h2>
<p>I'm a founding partner and the chief strategy officer of <a href="https://campbellteague.com/jordan-teague/">Campbell Teague</a>, where I focus on the firm's long-term direction: growth, innovation, and attorney development. Inside the firm I'm the self-described "nerd in the basement," the one building the systems.</p>
<p>I came to law from advertising, software development, and entrepreneurship, and have practiced across transactional work and litigation, including complex business disputes and class actions. I've won a federal bench trial and its appeal and tried an international arbitration in Paris.</p>
<p>Today I advise emerging-technology organizations on questions without settled answers: regulatory frameworks, legal personhood, governance, and which jurisdiction's law applies.</p>
<p>The thread through all of it is making expert judgment repeatable. The firm runs on a model in which project managers lead lawyer teams, and the tools I build apply the same idea to AI agents.</p>
<p>J.D., Vanderbilt University Law School, where I was Senior Technology Editor of the <i>Vanderbilt Journal of Entertainment and Technology Law</i>. B.S., magna cum laude, in Mathematics-Economics from Furman University.</p>
<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
<p class="label">Admitted in South Carolina and Alabama</p>
""")

PAGES = {
    "": ("Jordan Teague", "Lawyer, founder, and builder of legal AI systems. Co-founder of Campbell Teague.", home),
    "building": ("Building", "Open-source legal AI tools by Jordan Teague: TMrex, ROGbuster, Judgment Compiler, and TrademarkBench.", building),
    "writing": ("Writing", "Selected writing by Jordan Teague in Bloomberg Law and elsewhere.", writing),
    "speaking": ("Speaking", "Talks, panels, and podcasts by Jordan Teague.", speaking),
    "about": ("About", "Jordan Teague's practice and background.", about),
}

for slug, (title, desc, body) in PAGES.items():
    out = ROOT / slug / "index.html" if slug else ROOT / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(layout(slug, title, desc, body))
    print("wrote", out.relative_to(ROOT))
