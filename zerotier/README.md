# ZeroTier Help

https://zerotier.atlassian.net/wiki/spaces/SD/pages/7241787/PORT+ERROR+on+Mac

```bash
sudo launchctl unload /Library/LaunchDaemons/com.zerotier.one.plist
```

```bash
sudo launchctl load /Library/LaunchDaemons/com.zerotier.one.plist
```



> It looks like some operating systems try to deny any unexpected incoming traffic, so you can turn that off with this

```bash
sudo sed -i "s/ALL: ALL/#ALL: ALL/g" /etc/hosts.deny
```

> Just use this to turn it back on:

```bash
sudo sed -i "s/#ALL: ALL/ALL: ALL/g" /etc/hosts.deny
```

sudo nmap -sS -T5 -v <_IP ADDRESS_>

