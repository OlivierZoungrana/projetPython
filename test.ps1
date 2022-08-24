$fichier = "./test.js"

try {
    $contenuFichier = Get-Content $fichier -ErrorAction Stop
    Write-Host -ForegroundColor Green "contenu du fichier récupéré ($fichier)"
}
catch {

    
    Write-Host $_.Exception.Message -ForegroundColor Red
    New-Item -Name $fichier
    
}

finally{

}