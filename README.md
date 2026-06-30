# Daily Job Search Tracker

Automatically pulls job postings matching your criteria once a day using the
[JSearch API](https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch) (via RapidAPI),
and logs new results to this repo.

## Setup

1. **Create this repo on GitHub** and push this code to it (see commands below).

2. **Get a JSearch API key**
   - Go to https://rapidapi.com/letscrape-6bRBa3QguO5/api/jsearch
   - Sign up / log in, subscribe to the free tier, copy your `X-RapidAPI-Key`.

3. **Add the key as a repo secret**
   - In your GitHub repo: Settings → Secrets and variables → Actions → New repository secret
   - Name: `RAPIDAPI_KEY`
   - Value: (paste your key)

4. **Adjust your search criteria**
   - Edit `criteria.json` any time. Commit and push the change — the next
     scheduled run (or a manual run) will pick it up.

   ```json
   {
     "queries": [
       {
         "search_term": "data analyst",
         "location": "Remote",
         "remote_only": true,
         "employment_types": ["FULLTIME"],
         "date_posted": "today"
       }
     ],
     "num_pages": 1,
     "exclude_companies": [],
     "exclude_keywords_in_title": ["senior", "staff"]
   }
   ```

   You can list multiple query objects in `queries` to search several titles/locations
   in one run.

5. **Schedule**
   - Runs daily at 13:00 UTC by default (see `.github/workflows/daily-job-search.yml`).
   - Edit the `cron` line to change the time, or use the "Run workflow" button
     under the Actions tab to trigger it on demand.

## Output

- `data/jobs_master.json` — every unique job ever seen (deduplicated by job ID).
- `data/<YYYY-MM-DD>.csv` — just the *new* jobs found that day, ready to open in
  Excel/Sheets or load with pandas.

## Run locally (optional)

```bash
pip install -r requirements.txt
export RAPIDAPI_KEY=your_key_here
python fetch_jobs.py
```
