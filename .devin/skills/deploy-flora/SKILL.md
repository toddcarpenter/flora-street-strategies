---
name: deploy-flora
description: Deploy the Flora Street Strategies site to the local toddl.es web root with cache-busted assets
triggers:
  - user
  - model
allowed-tools:
  - read
  - exec
permissions:
  allow:
    - Exec(powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\deploy.ps1)
    - Exec(curl.exe)
    - Exec(git status)
---

Deploy the Flora Street Strategies website from this repository.

1. Confirm the current repository is `flora-street-strategies` and `scripts/deploy.ps1` exists.
2. Run `git status --short` and report whether source changes are uncommitted, but do not block deployment.
3. Run:

   ```powershell
   powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\deploy.ps1
   ```

4. Verify these local URLs when the toddl.es server is available:
   - `http://localhost:8088/florastreetstrategies/option1/`
   - `http://localhost:8088/florastreetstrategies/option2/`
5. Confirm both deployed HTML files contain timestamped CSS and JavaScript asset versions.
6. Report the deployment version, destination, HTTP results, and any uncommitted source changes.

Do not remove preview `noindex` protections, commit changes, push Git, or alter the production launch configuration as part of this skill.
