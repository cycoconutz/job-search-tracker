#!/usr/bin/env python3
"""
Daily job search puller.

Reads criteria.json for search parameters, queries the JSearch API
(via RapidAPI), filters/dedupes results, and appends them to:
  - data/jobs_master.json   (running de-duplicated database of all jobs seen)
  - data/<YYYY-MM-DD>.csv   (snapshot of NEW jobs found today)

Requires env var RAPIDAPI_KEY.
"""

import csv
import json
import os
import sys
import time
from datetime import datetime, timezone

import requests

CRITERIA_PATH = "criteria.json"
MASTER_PATH = "data/jobs_master.json"
API_URL = "https://api.openwebninja.com/jsearch/search-v2"


def load_criteria():
    with open(CRITERIA_PATH, "r") as f:
        return json.load(f)


def load_master():
    if os.path.exists(MASTER_PATH):
        with open(MASTER_PATH, "r") as f:
            return json.load(f)
    return {}


def save_master(master):
    os.makedirs("data", exist_ok=True)
    with open(MASTER_PATH, "w") as f:
        json.dump(master, f, indent=2)


def query_jsearch(api_key, query_cfg, num_pages):
    headers = {
        "x-api-key": api_key,
    }
    params = {
        "query": f"{query_cfg['search_term']} in {query_cfg.get('location', '')}".strip(),
        "page": "1",
        "num_pages": str(num_pages),
        "date_posted": query_cfg.get("date_posted", "today"),
    }
    if query_cfg.get("remote_only"):
        params["remote_jobs_only"] = "true"
    if query_cfg.get("employment_types"):
        params["employment_types"] = ",".join(query_cfg["employment_types"])

    resp = requests.get(API_URL, headers=headers, params=params, timeout=30)
    if not resp.ok:
        print(
            f"ERROR: HTTP {resp.status_code} from JSearch API.\n"
            f"URL: {resp.url}\n"
            f"Response body: {resp.text[:500]}",
            file=sys.stderr,
        )
    resp.raise_for_status()
    return resp.json().get("data", [])


def passes_filters(job, criteria):
    title = (job.get("job_title") or "").lower()
    company = (job.get("employer_name") or "").lower()

    for kw in criteria.get("exclude_keywords_in_title", []):
        if kw.lower() in title:
            return False
    for ec in criteria.get("exclude_companies", []):
        if ec.lower() == company:
            return False
    return True


def main():
    api_key = os.environ.get("RAPIDAPI_KEY")
    if not api_key:
        print("ERROR: RAPIDAPI_KEY env var not set.", file=sys.stderr)
        sys.exit(1)

    stripped = api_key.strip()
    if stripped != api_key:
        print(
            "WARNING: RAPIDAPI_KEY has leading/trailing whitespace or a newline "
            "in the GitHub secret. Using the stripped version, but you should "
            "fix the secret itself.",
            file=sys.stderr,
        )
        api_key = stripped
    print(f"Using RAPIDAPI_KEY of length {len(api_key)} (value hidden).", file=sys.stderr)

    criteria = load_criteria()
    master = load_master()
    new_jobs = []

    queries = criteria.get("queries", [])
    failed_queries = 0

    for q in queries:
        try:
            results = query_jsearch(api_key, q, criteria.get("num_pages", 1))
        except requests.HTTPError as e:
            print(f"WARNING: query failed for '{q.get('search_term')}': {e}", file=sys.stderr)
            failed_queries += 1
            continue

        for job in results:
            job_id = job.get("job_id")
            if not job_id or job_id in master:
                continue
            if not passes_filters(job, criteria):
                continue

            record = {
                "job_id": job_id,
                "title": job.get("job_title"),
                "company": job.get("employer_name"),
                "location": job.get("job_city") or job.get("job_country"),
                "remote": job.get("job_is_remote"),
                "employment_type": job.get("job_employment_type"),
                "posted_at": job.get("job_posted_at_datetime_utc"),
                "apply_link": job.get("job_apply_link"),
                "found_on": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            }
            master[job_id] = record
            new_jobs.append(record)

        time.sleep(1)  # be polite to the API

    if queries and failed_queries == len(queries):
        print(
            f"ERROR: all {len(queries)} quer{'y' if len(queries)==1 else 'ies'} failed. "
            "Treating this as a failed run (not committing). Check the warnings above.",
            file=sys.stderr,
        )
        sys.exit(1)

    save_master(master)

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    os.makedirs("data", exist_ok=True)
    csv_path = f"data/{today}.csv"
    if new_jobs:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(new_jobs[0].keys()))
            writer.writeheader()
            writer.writerows(new_jobs)
        print(f"Found {len(new_jobs)} new jobs. Wrote {csv_path}.")
    else:
        print("No new jobs found today.")

    # Write a tiny summary file the workflow can use for the commit message
    with open("data/.last_run_summary", "w") as f:
        f.write(f"{today}: {len(new_jobs)} new job(s), {len(master)} total tracked")


if __name__ == "__main__":
    main()
Done
Now update the response parsing to handle the search-v2 format correctly:


Edited 2 files, ran a command
