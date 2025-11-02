# Install Neuro Language - Make it work like Node, Ruby, Python
Write-Host "Installing Neuro Programming Language" -ForegroundColor Cyan
Write-Host "Making Neuro work like a real language: just type 'neuro file.neuro'" -ForegroundColor Gray
Write-Host ""

$neuroPath = "C:\Users\elena\OneDrive\Documents\GitHub\Neuro"

# Get current user PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")

# Check if already in PATH
if ($currentPath -like "*$neuroPath*") {
    Write-Host "[OK] Neuro is already in PATH" -ForegroundColor Green
} else {
    Write-Host "Adding Neuro to system PATH..." -ForegroundColor Yellow
    
    # Add to PATH
    $newPath = $currentPath + ";" + $neuroPath
    [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
    
    Write-Host "[OK] Neuro added to PATH" -ForegroundColor Green
}

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "NEURO IS NOW INSTALLED!" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Usage (like a REAL language):" -ForegroundColor White
Write-Host "  neuro my_job_search.neuro" -ForegroundColor Cyan
Write-Host "  neuro examples/neural_network.neuro" -ForegroundColor Cyan
Write-Host "  neuro any_file.neuro" -ForegroundColor Cyan
Write-Host ""
Write-Host "NO MORE:" -ForegroundColor Red
Write-Host "  python run_neuro.py file.neuro  [X]" -ForegroundColor DarkGray
Write-Host ""
Write-Host "JUST USE:" -ForegroundColor Green
Write-Host "  neuro file.neuro  [OK]" -ForegroundColor Cyan
Write-Host ""
Write-Host "IMPORTANT: Close and reopen your terminal for PATH changes to take effect" -ForegroundColor Yellow
Write-Host ""
Write-Host "Then test it:" -ForegroundColor White
Write-Host "  neuro my_job_search.neuro" -ForegroundColor Cyan
