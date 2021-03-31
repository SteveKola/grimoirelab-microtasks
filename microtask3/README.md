## Microtask 3

> Based on the elasticsearch documents produced by micro-mordred and source code of chaoss/grimoirelab-elk, 
> try to answer the following questions:

> **- What is the meaning of the JSON attribute `author_id`?**
> 
- Author identifier from SortingHat, for each different identity provided by SortingHat.
- And they are usually grouped into a single author_uuid.

> **What is the meaning of the JSON attribute `author_org_name`?**
> 
- The organization to which the author is affliated to, 
- and it's usually used to aggregate contributors and contributions across organization.

> **What is the meaning of the JSON attribute `author_uuid`?**
> 
- Used to identify and count authors across various data sources, so it's a unique author identifier.

> **What is the meaning of the JSON attribute `author_domain`?**
> 
- The associated domain to the author's SorthingHat profile.

> **What is the meaning of the JSON attribute `uuid`?**
> 
- uuid is a unique identifier that keeps track of how many unique profiles are been stored.

> **What is the meaning of the JSON attribute `utc_commit`?**
> 
- Commit date in UTC. 

> **What is the meaning of the JSON attribute `origin`?**
> 
- The source from which the data is retrieved from.

**PS:** The answers were gotten by going through [GrimoireLab-Elk's sourcecode](https://github.com/chaoss/grimoirelab-elk/blob/master/README.md) 
and checking the data at [chaoss.biterg.io](chaoss.biterg.io).
