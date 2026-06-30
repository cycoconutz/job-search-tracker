2026-06-30T23:14:40.5624505Z Current runner version: '2.335.1'
2026-06-30T23:14:40.5660517Z ##[group]Runner Image Provisioner
2026-06-30T23:14:40.5661979Z Hosted Compute Agent
2026-06-30T23:14:40.5662994Z Version: 20260611.554
2026-06-30T23:14:40.5664278Z Commit: 5e0782fdc9014723d3be820dd114dd31555c2bd1
2026-06-30T23:14:40.5665521Z Build Date: 2026-06-11T21:40:46Z
2026-06-30T23:14:40.5667135Z Worker ID: {f9e0d935-e804-48d0-87d5-35a7a0336002}
2026-06-30T23:14:40.5668426Z Azure Region: eastus
2026-06-30T23:14:40.5669511Z ##[endgroup]
2026-06-30T23:14:40.5671995Z ##[group]Operating System
2026-06-30T23:14:40.5673060Z Ubuntu
2026-06-30T23:14:40.5674242Z 24.04.4
2026-06-30T23:14:40.5675110Z LTS
2026-06-30T23:14:40.5676822Z ##[endgroup]
2026-06-30T23:14:40.5677802Z ##[group]Runner Image
2026-06-30T23:14:40.5679080Z Image: ubuntu-24.04
2026-06-30T23:14:40.5680257Z Version: 20260622.220.1
2026-06-30T23:14:40.5682449Z Included Software: https://github.com/actions/runner-images/blob/ubuntu24/20260622.220/images/ubuntu/Ubuntu2404-Readme.md
2026-06-30T23:14:40.5685250Z Image Release: https://github.com/actions/runner-images/releases/tag/ubuntu24%2F20260622.220
2026-06-30T23:14:40.5687468Z ##[endgroup]
2026-06-30T23:14:40.5689766Z ##[group]GITHUB_TOKEN Permissions
2026-06-30T23:14:40.5692715Z Contents: write
2026-06-30T23:14:40.5693733Z Metadata: read
2026-06-30T23:14:40.5694788Z ##[endgroup]
2026-06-30T23:14:40.5698135Z Secret source: Actions
2026-06-30T23:14:40.5700056Z Prepare workflow directory
2026-06-30T23:14:40.6184395Z Prepare all required actions
2026-06-30T23:14:40.6241067Z Getting action download info
2026-06-30T23:14:40.7735526Z Download action repository 'actions/checkout@v4' (SHA:34e114876b0b11c390a56381ad16ebd13914f8d5)
2026-06-30T23:14:40.8443980Z Download action repository 'actions/setup-python@v5' (SHA:a26af69be951a213d495a4c3e4e4022e16d87065)
2026-06-30T23:14:41.0133473Z Complete job name: fetch-jobs
2026-06-30T23:14:41.0908054Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-06-30T23:14:41.0916989Z ##[group]Run actions/checkout@v4
2026-06-30T23:14:41.0917735Z with:
2026-06-30T23:14:41.0918204Z   repository: cycoconutz/job-search-tracker
2026-06-30T23:14:41.0922375Z   token: ***
2026-06-30T23:14:41.0922814Z   ssh-strict: true
2026-06-30T23:14:41.0923313Z   ssh-user: git
2026-06-30T23:14:41.0923766Z   persist-credentials: true
2026-06-30T23:14:41.0924248Z   clean: true
2026-06-30T23:14:41.0924694Z   sparse-checkout-cone-mode: true
2026-06-30T23:14:41.0925212Z   fetch-depth: 1
2026-06-30T23:14:41.0925642Z   fetch-tags: false
2026-06-30T23:14:41.0926421Z   show-progress: true
2026-06-30T23:14:41.0926929Z   lfs: false
2026-06-30T23:14:41.0927374Z   submodules: false
2026-06-30T23:14:41.0927825Z   set-safe-directory: true
2026-06-30T23:14:41.0928621Z ##[endgroup]
2026-06-30T23:14:41.1861677Z Syncing repository: cycoconutz/job-search-tracker
2026-06-30T23:14:41.1863499Z ##[group]Getting Git version info
2026-06-30T23:14:41.1864540Z Working directory is '/home/runner/work/job-search-tracker/job-search-tracker'
2026-06-30T23:14:41.1865837Z [command]/usr/bin/git version
2026-06-30T23:14:41.1926381Z git version 2.54.0
2026-06-30T23:14:41.1947699Z ##[endgroup]
2026-06-30T23:14:41.1961774Z Temporarily overriding HOME='/home/runner/work/_temp/fd7a884b-be2f-4f50-9083-b053d9a109f8' before making global git config changes
2026-06-30T23:14:41.1963682Z Adding repository directory to the temporary git global config as a safe directory
2026-06-30T23:14:41.1967050Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/job-search-tracker/job-search-tracker
2026-06-30T23:14:41.2010854Z Deleting the contents of '/home/runner/work/job-search-tracker/job-search-tracker'
2026-06-30T23:14:41.2014623Z ##[group]Initializing the repository
2026-06-30T23:14:41.2019204Z [command]/usr/bin/git init /home/runner/work/job-search-tracker/job-search-tracker
2026-06-30T23:14:41.2118970Z hint: Using 'master' as the name for the initial branch. This default branch name
2026-06-30T23:14:41.2120421Z hint: will change to "main" in Git 3.0. To configure the initial branch name
2026-06-30T23:14:41.2121431Z hint: to use in all of your new repositories, which will suppress this warning,
2026-06-30T23:14:41.2122167Z hint: call:
2026-06-30T23:14:41.2122582Z hint:
2026-06-30T23:14:41.2123103Z hint: 	git config --global init.defaultBranch <name>
2026-06-30T23:14:41.2123781Z hint:
2026-06-30T23:14:41.2124370Z hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
2026-06-30T23:14:41.2125281Z hint: 'development'. The just-created branch can be renamed via this command:
2026-06-30T23:14:41.2126007Z hint:
2026-06-30T23:14:41.2126634Z hint: 	git branch -m <name>
2026-06-30T23:14:41.2127120Z hint:
2026-06-30T23:14:41.2127758Z hint: Disable this message with "git config set advice.defaultBranchName false"
2026-06-30T23:14:41.2133824Z Initialized empty Git repository in /home/runner/work/job-search-tracker/job-search-tracker/.git/
2026-06-30T23:14:41.2144449Z [command]/usr/bin/git remote add origin https://github.com/cycoconutz/job-search-tracker
2026-06-30T23:14:41.2186968Z ##[endgroup]
2026-06-30T23:14:41.2188327Z ##[group]Disabling automatic garbage collection
2026-06-30T23:14:41.2191231Z [command]/usr/bin/git config --local gc.auto 0
2026-06-30T23:14:41.2219806Z ##[endgroup]
2026-06-30T23:14:41.2221189Z ##[group]Setting up auth
2026-06-30T23:14:41.2226844Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-06-30T23:14:41.2260343Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-06-30T23:14:41.2577403Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-06-30T23:14:41.2605027Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-06-30T23:14:41.2819362Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-06-30T23:14:41.2849998Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-06-30T23:14:41.3062120Z [command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***
2026-06-30T23:14:41.3093732Z ##[endgroup]
2026-06-30T23:14:41.3094750Z ##[group]Fetching the repository
2026-06-30T23:14:41.3102852Z [command]/usr/bin/git -c protocol.version=2 fetch --no-tags --prune --no-recurse-submodules --depth=1 origin +cbeef2a9c8e737aa0338bc4458badd0bec8aa081:refs/remotes/origin/main
2026-06-30T23:14:41.4943195Z From https://github.com/cycoconutz/job-search-tracker
2026-06-30T23:14:41.4944380Z  * [new ref]         cbeef2a9c8e737aa0338bc4458badd0bec8aa081 -> origin/main
2026-06-30T23:14:41.4982222Z ##[endgroup]
2026-06-30T23:14:41.4983597Z ##[group]Determining the checkout info
2026-06-30T23:14:41.4985254Z ##[endgroup]
2026-06-30T23:14:41.4990457Z [command]/usr/bin/git sparse-checkout disable
2026-06-30T23:14:41.5033783Z [command]/usr/bin/git config --local --unset-all extensions.worktreeConfig
2026-06-30T23:14:41.5061517Z ##[group]Checking out the ref
2026-06-30T23:14:41.5065747Z [command]/usr/bin/git checkout --progress --force -B main refs/remotes/origin/main
2026-06-30T23:14:41.5112206Z Switched to a new branch 'main'
2026-06-30T23:14:41.5115301Z branch 'main' set up to track 'origin/main'.
2026-06-30T23:14:41.5123797Z ##[endgroup]
2026-06-30T23:14:41.5175139Z [command]/usr/bin/git log -1 --format=%H
2026-06-30T23:14:41.5199517Z cbeef2a9c8e737aa0338bc4458badd0bec8aa081
2026-06-30T23:14:41.5588385Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-06-30T23:14:41.5593883Z ##[group]Run actions/setup-python@v5
2026-06-30T23:14:41.5594636Z with:
2026-06-30T23:14:41.5595113Z   python-version: 3.11
2026-06-30T23:14:41.5595707Z   check-latest: false
2026-06-30T23:14:41.5605986Z   token: ***
2026-06-30T23:14:41.5606634Z   update-environment: true
2026-06-30T23:14:41.5607302Z   allow-prereleases: false
2026-06-30T23:14:41.5607950Z   freethreaded: false
2026-06-30T23:14:41.5608505Z ##[endgroup]
2026-06-30T23:14:41.7062780Z ##[group]Installed versions
2026-06-30T23:14:41.7157008Z (node:2270) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-06-30T23:14:41.7160918Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-30T23:14:41.7162953Z Successfully set up CPython (3.11.15)
2026-06-30T23:14:41.7164201Z ##[endgroup]
2026-06-30T23:14:41.7323813Z ##[group]Run pip install -r requirements.txt
2026-06-30T23:14:41.7324897Z [36;1mpip install -r requirements.txt[0m
2026-06-30T23:14:41.7483709Z shell: /usr/bin/bash -e {0}
2026-06-30T23:14:41.7484405Z env:
2026-06-30T23:14:41.7485104Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:41.7486735Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib/pkgconfig
2026-06-30T23:14:41.7488177Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:41.7489383Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:41.7490613Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:41.7491852Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib
2026-06-30T23:14:41.7492848Z ##[endgroup]
2026-06-30T23:14:44.4233895Z Collecting requests>=2.31.0 (from -r requirements.txt (line 1))
2026-06-30T23:14:44.4869547Z   Downloading requests-2.34.2-py3-none-any.whl.metadata (4.8 kB)
2026-06-30T23:14:44.5852419Z Collecting charset_normalizer<4,>=2 (from requests>=2.31.0->-r requirements.txt (line 1))
2026-06-30T23:14:44.5893224Z   Downloading charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl.metadata (40 kB)
2026-06-30T23:14:44.6154169Z Collecting idna<4,>=2.5 (from requests>=2.31.0->-r requirements.txt (line 1))
2026-06-30T23:14:44.6197030Z   Downloading idna-3.18-py3-none-any.whl.metadata (6.1 kB)
2026-06-30T23:14:44.6452727Z Collecting urllib3<3,>=1.26 (from requests>=2.31.0->-r requirements.txt (line 1))
2026-06-30T23:14:44.6492050Z   Downloading urllib3-2.7.0-py3-none-any.whl.metadata (6.9 kB)
2026-06-30T23:14:44.6655913Z Collecting certifi>=2023.5.7 (from requests>=2.31.0->-r requirements.txt (line 1))
2026-06-30T23:14:44.6692641Z   Downloading certifi-2026.6.17-py3-none-any.whl.metadata (2.5 kB)
2026-06-30T23:14:44.6771412Z Downloading requests-2.34.2-py3-none-any.whl (73 kB)
2026-06-30T23:14:44.6878330Z Downloading charset_normalizer-3.4.7-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (214 kB)
2026-06-30T23:14:44.6997188Z Downloading idna-3.18-py3-none-any.whl (65 kB)
2026-06-30T23:14:44.7058608Z Downloading urllib3-2.7.0-py3-none-any.whl (131 kB)
2026-06-30T23:14:44.7169539Z Downloading certifi-2026.6.17-py3-none-any.whl (133 kB)
2026-06-30T23:14:44.7982756Z Installing collected packages: urllib3, idna, charset_normalizer, certifi, requests
2026-06-30T23:14:44.9862872Z 
2026-06-30T23:14:44.9872966Z Successfully installed certifi-2026.6.17 charset_normalizer-3.4.7 idna-3.18 requests-2.34.2 urllib3-2.7.0
2026-06-30T23:14:45.0341142Z ##[group]Run python fetch_jobs.py
2026-06-30T23:14:45.0341487Z [36;1mpython fetch_jobs.py[0m
2026-06-30T23:14:45.0375007Z shell: /usr/bin/bash -e {0}
2026-06-30T23:14:45.0375272Z env:
2026-06-30T23:14:45.0375552Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.0376550Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib/pkgconfig
2026-06-30T23:14:45.0377013Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.0377404Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.0377782Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.0378174Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib
2026-06-30T23:14:45.0378831Z   RAPIDAPI_KEY: ***
2026-06-30T23:14:45.0379079Z ##[endgroup]
2026-06-30T23:14:45.9135694Z WARNING: query failed for 'frontend developer': 404 Client Error: Not Found for url: https://jsearch.p.rapidapi.com/search?query=frontend+developer+in+United+States&page=1&num_pages=1&date_posted=today&remote_jobs_only=true&employment_types=FULLTIME
2026-06-30T23:14:45.9143675Z No new jobs found today.
2026-06-30T23:14:45.9342109Z ##[group]Run git config user.name "job-search-bot"
2026-06-30T23:14:45.9342527Z [36;1mgit config user.name "job-search-bot"[0m
2026-06-30T23:14:45.9342933Z [36;1mgit config user.email "actions@users.noreply.github.com"[0m
2026-06-30T23:14:45.9343287Z [36;1mgit add data/[0m
2026-06-30T23:14:45.9343531Z [36;1mif git diff --cached --quiet; then[0m
2026-06-30T23:14:45.9343828Z [36;1m  echo "Nothing new to commit."[0m
2026-06-30T23:14:45.9344085Z [36;1melse[0m
2026-06-30T23:14:45.9344437Z [36;1m  SUMMARY=$(cat data/.last_run_summary 2>/dev/null || echo "Daily job search update")[0m
2026-06-30T23:14:45.9344901Z [36;1m  git commit -m "Job search update: $SUMMARY"[0m
2026-06-30T23:14:45.9345215Z [36;1m  git pull --rebase origin main[0m
2026-06-30T23:14:45.9345478Z [36;1m  git push[0m
2026-06-30T23:14:45.9345680Z [36;1mfi[0m
2026-06-30T23:14:45.9377884Z shell: /usr/bin/bash -e {0}
2026-06-30T23:14:45.9378128Z env:
2026-06-30T23:14:45.9378429Z   pythonLocation: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.9378880Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib/pkgconfig
2026-06-30T23:14:45.9379312Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.9379687Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.9380062Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.11.15/x64
2026-06-30T23:14:45.9380436Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.11.15/x64/lib
2026-06-30T23:14:45.9380754Z ##[endgroup]
2026-06-30T23:14:45.9500350Z Nothing new to commit.
2026-06-30T23:14:45.9595502Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-06-30T23:14:45.9597495Z Post job cleanup.
2026-06-30T23:14:46.0753518Z (node:2339) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
2026-06-30T23:14:46.0755043Z (Use `node --trace-deprecation ...` to show where the warning was created)
2026-06-30T23:14:46.0946966Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
2026-06-30T23:14:46.0948245Z Post job cleanup.
2026-06-30T23:14:46.1751620Z [command]/usr/bin/git version
2026-06-30T23:14:46.1787054Z git version 2.54.0
2026-06-30T23:14:46.1825041Z Temporarily overriding HOME='/home/runner/work/_temp/31a79eac-fba9-4c0f-8ee9-8ba36cd94e4f' before making global git config changes
2026-06-30T23:14:46.1826819Z Adding repository directory to the temporary git global config as a safe directory
2026-06-30T23:14:46.1831430Z [command]/usr/bin/git config --global --add safe.directory /home/runner/work/job-search-tracker/job-search-tracker
2026-06-30T23:14:46.1868758Z [command]/usr/bin/git config --local --name-only --get-regexp core\.sshCommand
2026-06-30T23:14:46.1925323Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :"
2026-06-30T23:14:46.2146511Z [command]/usr/bin/git config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
2026-06-30T23:14:46.2170370Z http.https://github.com/.extraheader
2026-06-30T23:14:46.2181276Z [command]/usr/bin/git config --local --unset-all http.https://github.com/.extraheader
2026-06-30T23:14:46.2212128Z [command]/usr/bin/git submodule foreach --recursive sh -c "git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :"
2026-06-30T23:14:46.2430082Z [command]/usr/bin/git config --local --name-only --get-regexp ^includeIf\.gitdir:
2026-06-30T23:14:46.2458763Z [command]/usr/bin/git submodule foreach --recursive git config --local --show-origin --name-only --get-regexp remote.origin.url
2026-06-30T23:14:46.2798836Z Cleaning up orphan processes
2026-06-30T23:14:46.3283395Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
