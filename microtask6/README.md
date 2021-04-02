## Micro-task 6

> Using the SortingHat GraphQL Console, create a query that fetches the data (identities, enrollments) of an individual profile.

### Query to fetch the individual profile data

```
    {
      individuals {
        entities {
          profile {
            id,
            name,
            isBot, 
            gender, 
            genderAcc,
            country {
              name
            },
          }
          
          identities {
            uuid, 
            name, 
            email, 
            username, 
            source, 
            createdAt,
          }

          enrollments {
            id, 
            start, 
            end,
            organization {
              name,
              domains {
                domain,
                isTopDomain,
              }
            }
          }
        }
      }
    }
```

### The output of the query is as shown below;

![](https://github.com/SteveKola/grimoirelab-microtasks/blob/main/microtask6/proof.gif)
