---
date: 2019-05-16 19:50:11 +0000
title: "Neeerrrrrd!"
category: tweet
original_url: https://twitter.com/ctrueden/status/1129111823716880389
---

When has my IP change propagated? Terminal-driven alarm!

```shell
while [ "$ip" != "144.92.48.199" ]
do
  ip=$(host http://maven.imagej.net | sed 's/.* address //')
  sleep 60
done; while true; do echo -ne '\007'; sleep 1; done
```
