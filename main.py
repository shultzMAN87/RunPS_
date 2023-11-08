import subprocess


arguments = [
    'powershell.exe Start-Process',
    '-FilePath \'C:\\Program Files\\Crypto Pro\\CSP\\certmgr.exe\'',
    # Получение информации о сертификатах
    # '-ArgumentList \'-list -store mmy\'',
    # Удаление сертификата
    '-ArgumentList \'-delete -store mmy -thumbprint a13f7d64728c95fcf31d57ceccd35acb173ed27e\'',
    '-Wait',
    '-NoNewWindow'
]

res = subprocess.Popen(' '.join(arguments), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

for line in res.stdout.readlines():
    line = line.strip()
    if line:
        print(line.decode('cp866'))
