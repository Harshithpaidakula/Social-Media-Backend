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
    Write-Output "No project changes to commit."
}

git push --set-upstream origin $branch
if ($LASTEXITCODE -ne 0) {
    throw "GitHub push failed. Check internet access and GitHub authentication; the next scheduled run will retry."
}