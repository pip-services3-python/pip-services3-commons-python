#!/usr/bin/env pwsh

Set-StrictMode -Version latest
$ErrorActionPreference = "Stop"

$component = Get-Content -Path "component.json" | ConvertFrom-Json
$version = (Get-Content -Path component.json | ConvertFrom-Json).version

if ($component.version -ne $version) {
    throw "Versions in component.json and package.json do not match"
}


# Publish to global repository
Write-Output "Pushing package to pipy"
python setup.py sdist
twine upload --skip-existing dist/*