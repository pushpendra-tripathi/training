## Week 1 · Day 1 — Linux + Git Foundations

### Objectives
- Navigate Linux CLI confidently; manipulate files, permissions, and archives.
- Practice core Git: branch, commit, push, PR; resolve simple conflicts.

### Prerequisites
- Python installed; Git installed; GitHub account with SSH.

### Tasks
1) Linux essentials
   - Practice: `pwd`, `ls -la`, `cd`, `mkdir`, `rm -rf`, `cp`, `mv`.
   - Permissions: `chmod`, `chown`; check `umask`.
   - Search: `grep -R`, `find . -name "*.py"`.
   - Archives: `tar -czf logs-$(date +%F).tar.gz ./logs`.
2) Create backup script
   - Create `scripts/backup_logs.sh` that:
     - Archives a given directory to `./archives/<name>-YYYY-MM-DD.tar.gz`.
     - Keeps only the last N archives (argument), deletes older ones.
     - Prints a summary of created and deleted archives.
   - Make executable: `chmod +x scripts/backup_logs.sh`.
   - Use sample logs directory: `intern_training/data/sample_logs/`.
3) Git workflow
   - Initialize or clone your playground repo.
   - Create branch `feature/backup-script` → commit the script with a clear message.
   - Push branch and open a Pull Request with a short description and usage.

### Problem solving (45–60 min)
- LeetCode: [Two Sum](https://leetcode.com/problems/two-sum/), [Valid Anagram](https://leetcode.com/problems/valid-anagram/)

### Outcomes
- You can compress, search, and manage files; understand basic permissions.
- You can create a branch, commit, push, and open a PR.

### Deliverables
- PR titled "Add backup logs script" with:
  - `scripts/backup_logs.sh` and `scripts/README.md` (usage examples).
  - At least one screenshot or terminal snippet of running the script.

### Submission checklist
- [ ] Script executable and works for a sample folder
- [ ] Clear usage in README (inputs, outputs, retention policy)
- [ ] PR opened with descriptive title and body


