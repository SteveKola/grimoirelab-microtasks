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

![image](https://user-images.githubusercontent.com/45284829/113328087-b1b4a600-9313-11eb-9561-cccbf4ba910c.png)
