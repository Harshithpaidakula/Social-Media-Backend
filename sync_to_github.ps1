$ErrorActionPreference = "Stop"

Set-Location $PSScriptRoot

$branch = (git branch --show-current).Trim()
if ($LASTEXITCODE -ne 0 -or -not $branch) {
    throw "Could not determine the Git branch."
}

git add --all
if ($LASTEXITCODE -ne 0) {
    throw "Could not stage project changes."
}

git diff --cached --quiet
$diffExitCode = $LASTEXITCODE
$message = "Development update"
if ($diffExitCode -eq 1) {
    git commit -m $message
    if ($LASTEXITCODE -ne 0) {
        throw "Could not create the automatic sync commit."
    }
} elseif ($diffExitCode -ne 0) {
    throw "Could not inspect staged project changes."
} else {
    $today = Get-Date -Format "yyyy-MM-dd"
    $lastUpdate = git log -1 --format="%ad|%s" --date=format:%Y-%m-%d
    if ($LASTEXITCODE -ne 0) {
        throw "Could not inspect the latest commit."
    }
    if ($lastUpdate -ne "$today|$message") {
        git commit --allow-empty -m $message
        if ($LASTEXITCODE -ne 0) {
            throw "Could not create the daily contribution commit."
        }
    }
}

git push --set-upstream origin $branch
if ($LASTEXITCODE -ne 0) {
    throw "GitHub push failed. Check internet access and GitHub authentication; the next scheduled run will retry."
}