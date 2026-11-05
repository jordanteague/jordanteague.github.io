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
    ("speaking", "03", "Speaking", "Talks, panels, and podcasts on AI agents, DAOs, and legal engineering."),
    ("about", "04", "About", "Practice, background, and how to reach me."),
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
    pager = ""
    slugs = [s[0] for s in SECTIONS]
    if slug in slugs:
        i = slugs.index(slug)
        if i + 1 < len(SECTIONS):
            s, n, name, _ = SECTIONS[i + 1]
            pager = f'<nav class="pager"><a href="{pre}{s}/">Next · {n} · {name} →</a></nav>'
        else:
            pager = f'<nav class="pager"><a href="{pre}">Back to the start →</a></nav>'
    full_title = "Jordan Teague" if not slug else f"{title} · Jordan Teague"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#f6f4ef">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<link rel="canonical" href="{url}">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{pre}style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site">
  <a class="name" href="{pre or './'}">Jordan Teague</a>
  <nav>{nav}</nav>
</header>
<main id="main">
{body}
{pager}
</main>
<footer class="site">
  <p><a href="mailto:{EMAIL}">{EMAIL}</a> · {ext("https://www.linkedin.com/in/jordanteague", "LinkedIn")} · {ext("https://github.com/jordanteague", "GitHub")}</p>
  <p class="fine">© 2026 Jordan Teague. Personal site. Views are my own and not those of Campbell Teague or its clients. Nothing on this site is legal advice, and visiting it does not create an attorney-client relationship.</p>
</footer>
</body>
</html>
"""


def page_head(num, name, h1, intro):
    return f'<p class="eyebrow">{num} · {name}</p>\n<h1>{h1}</h1>\n<p class="intro">{intro}</p>'


# ---------- Home ----------
index_rows = "".join(
    f'<li><a href="{s}/"><span class="num">{n}</span><span class="sec">{name}</span>'
    f'<span class="desc">{d} →</span></a></li>'
    for s, n, name, d in SECTIONS
)
home = f"""
<section class="hero">
  <h1 class="big">Lawyer, founder, and builder of legal AI systems.</h1>
  <p>I co-founded {ext("https://campbellteague.com/jordan-teague/", "Campbell Teague")}, a Chambers-ranked firm that advises emerging-technology organizations on questions without settled answers, from token issuance under MiCA to decentralized protocol governance.</p>
  <p>I also build the tools. Most of my recent work turns legal judgment into something AI agents can apply consistently: clearance searches, discovery review, and the playbooks behind them.</p>
</section>

<section class="currently">
  <h2>Currently</h2>
  <dl>
    <dt>Practicing.</dt><dd>Founding Partner and Chief Strategy Officer at Campbell Teague, advising emerging-technology organizations in the U.S. and abroad.</dd>
    <dt>Building.</dt><dd><a href="building/">Open-source Claude skills</a> for trademark clearance, discovery review, and compiling lawyers' judgment into AI playbooks.</dd>
    <dt>Writing.</dt><dd>{ext("https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/legal-mentorship-was-already-broken-ai-just-made-it-obvious", "“Legal Mentorship Was Already Broken. AI Just Made It Obvious.”")} in Bloomberg Law.</dd>
  </dl>
</section>

<section>
  <h2>Contents</h2>
  <ul class="index">{index_rows}</ul>
</section>

<section>
  <h2>Selected work</h2>
  <ul class="selected">
    <li><span class="label">Claude skill · open source</span><a href="building/#tmrex">TMrex: U.S. trademark clearance →</a></li>
    <li><span class="label">Claude skill · open source</span><a href="building/#rogbuster">ROGbuster: discovery response review →</a></li>
    <li><span class="label">Specification · open source</span><a href="building/#judgment-compiler">Judgment Compiler →</a></li>
  </ul>
</section>
"""

# ---------- Building ----------
def project(pid, name, meta, paras, link):
    rows = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in meta)
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f"""<article class="project" id="{pid}">
  <h2>{name}</h2>
  <dl class="meta">{rows}</dl>
  {ps}
  <p class="links">{ext(link, "Repository")}</p>
</article>"""

building = page_head("01", "Building", "Legal AI, built in the open",
                     "Each of these encodes a piece of legal judgment so an AI agent can apply it the same way every time. All are open source.") + "\n"
building += project("tmrex", "TMrex",
    [("What", "Claude skill"), ("Practice area", "U.S. trademark clearance"), ("Scope", "Screening-level search and registrability report")],
    ["Searches a local copy of the full USPTO register, about 14 million case files, synced twice a day. It also searches the web and domain names for unregistered use, then reports on registrability issues."],
    "https://github.com/jordanteague/TMrex")
building += project("rogbuster", "ROGbuster",
    [("What", "Claude skill"), ("Practice area", "Litigation discovery")],
    ["Reviews the other side's discovery responses, flags every gap, and drafts the meet-and-confer letter."],
    "https://github.com/jordanteague/ROGbuster")
building += project("judgment-compiler", "Judgment Compiler",
    [("What", "Platform-neutral specification and Claude skill"), ("Output", "Schema-validated playbooks for AI review agents")],
    ["Compiles a lawyer's judgment, captured from an interview or a starting draft, into a structured playbook that AI review agents can apply consistently."],
    "https://github.com/jordanteague/judgment-compiler")
building += project("trademarkbench", "TrademarkBench",
    [("What", "Pilot benchmark"), ("Status", "Pilot; results are directional"), ("Sample", "90 applications examined after the model's training cutoff")],
    ["Tests whether Claude can predict USPTO trademark examination outcomes, with and without trademark-register search, scored against real examiner decisions."],
    "https://github.com/jordanteague/trademarkbench")
building += f"""
<article class="project" id="also">
  <h2>Also built</h2>
  <ul class="plain">
    <li><strong>Layered AI architecture for law firm work.</strong> Applied DRY software-design principles to Microsoft Copilot agents, separating orchestration, reusable expert playbooks, and matter-specific context.</li>
    <li><strong>Automated context pipelines.</strong> Power Automate pipelines that ingest and structure public information as client-specific context for Copilot-based legal review.</li>
    <li><strong>Clio dashboards.</strong> OAuth-integrated practice dashboards, first built conventionally and later with Claude.</li>
    <li><strong>Smart contracts.</strong> Solidity contracts in {ext("https://github.com/lexDAO/LexCorpus/commits?author=jordanteague", "LexDAO's contract library")} and front-end code for a {ext("https://github.com/lexDAO/Kali/commits?author=jordanteague", "DAO-formation app")}.</li>
    <li><strong>Earlier products.</strong> iOS and SaaS apps shipped years before AI coding tools existed.</li>
  </ul>
</article>
"""

# ---------- Writing ----------
WRITING = [
    ("Bloomberg Law", "2026", "Legal Mentorship Was Already Broken. AI Just Made It Obvious.", "https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/legal-mentorship-was-already-broken-ai-just-made-it-obvious", "AI & the profession"),
    ("LinkedIn", "2026", "Your AI Agent Gave the Right Answer. Did It Use the Right Context?", "https://www.linkedin.com/pulse/your-ai-agent-gave-right-answer-did-use-context-jordan-teague-rudte/", "AI agents"),
    ("Bloomberg Law", "2024", "Law Firms Should Ditch the Rigid Mindset for a Disruptive Model", "https://news.bloomberglaw.com/us-law-week/law-firms-should-ditch-the-rigid-mindset-for-a-disruptive-model", "Firm models"),
    ("Other Internet", "2022", "Effective Accountability for Uniswap Governance", "https://otherinter.net/research/uniswap-accountability/", "DAO governance"),
    ("The Defiant", "2022", "Starting a DAO in the USA? Steer Clear of DAO Legislation", "https://thedefiant.io/news/research-and-opinion/starting-a-dao-in-the-usa-steer-clear-of-dao-legislation", "DAO formation"),
    ("Case Western Reserve Journal of Law, Technology & the Internet", "2012", "Saving the Spotify Revolution: Recalibrating the Power Imbalance in Digital Copyright", "https://scholarlycommons.law.case.edu/jolti/vol4/iss1/8/", "Copyright"),
    ("Vanderbilt Journal of Entertainment & Technology Law", "2012", "Promoting Trademark's Ends and Means through Online Contributory Liability", "https://scholarship.law.vanderbilt.edu/jetlaw/vol14/iss2/6/", "Trademark"),
]
items = "".join(
    f'<li><p class="meta">{o.replace("&", "&amp;")} · {y}</p>{ext(u, t)}<p class="tag">{tag.replace("&", "&amp;")}</p></li>'
    for o, y, t, u, tag in WRITING
)
writing = page_head("02", "Writing", "Selected writing",
                    "Columns and essays on how law firms and lawyers should adapt to AI, earlier work on DAO governance, and two law review articles.") + f'\n<ul class="pubs">{items}</ul>'

# ---------- Speaking ----------
SPEAKING = [
    # (venue, year, title, url or None, note)
    ("Antifirm Podcast", "", "Antifirm Podcast", None, "TODO: link and one line from Jordan"),
    ("Fordham Law School Blockchain Regulatory Symposium", "2024", "Building for a Bright Future from a Dark Forest", None, "Panelist on AI agent personhood and related topics."),
    ("Law at the Limits (ETHDenver side event)", "2024", "AI, agents, DAOs, and smart contracts", None, "AI agents in DAO governance: AI-controlled capital, manipulation risk, and who bears responsibility when AI acts for a DAO."),
    ("Greenville Bar Association Year-End CLE", "2024", "The Intelligence Is Artificial, but the Risks Are Real", None, "AI over-reliance and practical risk mitigation."),
    ("DAOPlanet NYC", "2023", "Decentralized governance", None, ""),
    ("Law of Code podcast", "2022", "DAO structuring and legal engineering", "https://podcasts.apple.com/us/podcast/49-jordan-teague-dao-structuring-legal-engineering/id1578287932?i=1000566269454", ""),
    ("The Encrypted Economy podcast", "2022", "Taking the “ow” out of DAOs", "https://podcasts.apple.com/us/podcast/taking-the-ow-out-of-daos-ross-campbell-and/id1541074732?i=1000555577411", ""),
    ("American Bar Association CLE webinar", "2022", "Legal Governance of Digital Autonomous Organizations", None, "Panelist."),
]
sp = ""
for venue, year, title, url, note in SPEAKING:
    t = ext(url, title) if url else f'<span class="title">{title}</span>'
    m = venue + (f" · {year}" if year else "")
    n = f'<p class="tag">{note}</p>' if note and not note.startswith("TODO") else ""
    if note.startswith("TODO"):
        sp += f"<!-- {note} -->"
    sp += f'<li><p class="meta">{m}</p>{t}{n}</li>'
speaking = page_head("03", "Speaking", "Talks, panels, and podcasts",
                     "On AI agents, decentralized governance, and the practice of legal engineering.") + f'\n<ul class="pubs">{sp}</ul>'

# ---------- About ----------
about = page_head("04", "About", "Practice and background",
                  "I've practiced law since 2012 and co-founded Campbell Teague in 2016.") + f"""
<h2>Practice</h2>
<p>As Founding Partner and Chief Strategy Officer of {ext("https://campbellteague.com/jordan-teague/", "Campbell Teague")}, I advise U.S. and international emerging-technology organizations on regulatory frameworks, legal personhood, organizational structure, governance, and which jurisdictions' laws apply.</p>
<p>Recent work includes advising a token issuer under the EU's Markets in Crypto-Assets Regulation during its early implementation, with no precedent or settled guidance, and serving as outside general counsel to The Graph Foundation on decentralized protocol governance.</p>
<p>In litigation, I've won a federal bench trial and its appeal, tried an international arbitration in Paris, and handled a software copyright dispute spanning competing federal jurisdictions.</p>

<h2>The firm</h2>
<p>I co-founded the firm with two lawyers and grew it into a U.S. and international team of more than 14. It runs on a project-management model in which project managers lead lawyer teams. The same instinct, to make expert judgment repeatable, runs through the tools I build.</p>

<h2>Education</h2>
<p>J.D., Vanderbilt University Law School, where I was Senior Technology Editor of the <i>Vanderbilt Journal of Entertainment and Technology Law</i>.<br>B.S., Mathematics-Economics, magna cum laude, Furman University.</p>
<p class="aside">Admitted in South Carolina and Alabama.</p>

<h2>Contact</h2>
<p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
"""

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
