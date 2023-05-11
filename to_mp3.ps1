Get-ChildItem -Recurse -Filter *.wav |
Foreach-Object {
    Write-Host $_.Name
    docker run -v ${pwd}:/app/ to_mp3 python to_mp3.py -i $_.Name
}