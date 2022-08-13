$str=Get-Host
Write-Host ("test ")
write-Host($str.Name)
foreach( $i in $str)
{
    write-Host($i)
}
