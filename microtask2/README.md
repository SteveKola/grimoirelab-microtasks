## Microtask 2

> Execute micro-mordred to collect, enrich and visualize data from Git repositories. 
> 
After setting up my dev environment for Grimoirelab, as specified by 
[microtask1](https://github.com/SteveKola/grimoirelab-microtasks/tree/main/microtask0%261), 
I proceeded to execute micro-mordred by defining up the setup.cfg and projects.json. And afterwards, running the following two commands;

```
micro.py --raw --enrich --cfg ./setup.cfg --backends git cocom
micro.py --panels --cfg ./setup.cfg
```

## Troubleshooting

I spent the bulk of my time on this issue as I encountered lots of issues.
