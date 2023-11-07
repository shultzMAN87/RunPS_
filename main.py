import subprocess
import sys

p = subprocess.Popen(
    'powershell.exe Start-Process -FilePath \'C:\Program Files\Crypto Pro\CSP\certmgr.exe\' -ArgumentList \'-list -store mmy\' -Wait -NoNewWindow',
    stdout=sys.stdout,
)

p.communicate()