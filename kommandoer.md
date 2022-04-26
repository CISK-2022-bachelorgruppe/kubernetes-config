`cat limits.conf`

Forsøk på å finne terminalen sine begrensninger, denne kommandoen var ikke riktig:
`uname -a`

Finne alle tcp filer:
`lsof -n | grep -i tcp`

Finna antall tcp filer:
`lsof -n | grep -ic tcp`

Finne current shell sine limits: `ulimit -a`

Hard Limits: `ulimit -Hn`

Soft limits: `ulimit -Sn`

`su - username`
