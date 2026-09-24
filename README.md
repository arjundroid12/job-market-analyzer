# Job Market Analyzer

Which skills do Python developer jobs actually ask for? This project scrapes public Python job postings, cleans them, stores them in a database, and shows the answers on an interactive dashboard.

## Features
- **Scraper** — collects Python developer job postings from public job boards (`requests` + `BeautifulSoup`), politely: rate-limited, cached, robots.txt respected
- **Cleaning** — normalizes titles, locations, salaries, and required skills with `pandas`
- **Storage** — saves clean postings to SQLite
- **Dashboard** — Streamlit app showing the most in-demand skills, salary ranges, and hiring trends

## Tech Stack
Python · requests · BeautifulSoup · pandas · SQLite · Streamlit · matplotlib

## Roadmap
- [ ] Scrape one page of postings
- [ ] Pagination + polite scraping (delays, retries, cache)
- [ ] Clean and normalize with pandas
- [ ] Store in SQLite
- [ ] Skill-frequency analysis
- [ ] Streamlit dashboard
- [ ] Scheduled daily refresh

## Author
Arjun Vashishtha · [GitHub](https://github.com/arjundroid12) · [Portfolio](https://arjunv.is-a.dev)
