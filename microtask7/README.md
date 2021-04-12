## Microtask 7

> Create a script that can parse the [gitdm](https://github.com/cncf/gitdm) developer affiliation files and load the data in a SortingHat database using GraphQL.

As instructed I got a [developer affiliation file](https://github.com/SteveKola/grimoirelab-microtasks/blob/main/microtask7/developers_affiliations1.txt) from 
[gitdm](https://github.com/cncf/gitdm). Afterwards, I wrote a Python script that'd parse the developer affiliation file by retrieving each developer's name, 
email addresses, and organizations they're affiliated to.

Then I loaded each developer's info into the SortingHat's database using GraphQL. 

The steps I took are shown in the gif below;

![](https://github.com/SteveKola/grimoirelab-microtasks/blob/main/microtask7/proof.gif)

Here is the final result after all the data has been uploaded onto the database;

![image](https://user-images.githubusercontent.com/45284829/114403012-5056c780-9b9c-11eb-9d08-f028f8aa5346.png)

### Troubleshooting:

While loading the data into the SortingHat database using GraphQL, I came across this <403> error;

![image](https://user-images.githubusercontent.com/45284829/114392909-51362c00-9b91-11eb-9e4f-9c2d68fd3ab3.png)

And I solved it by commenting out this line https://github.com/chaoss/grimoirelab-sortinghat/blob/muggle/config/settings/devel.py#L24.
