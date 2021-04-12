
### Troubleshooting:

while loading the data into the SortingHat database using GraphQL, I came across this <403> error;

![image](https://user-images.githubusercontent.com/45284829/114392909-51362c00-9b91-11eb-9e4f-9c2d68fd3ab3.png)

And I solved it by commenting out this line https://github.com/chaoss/grimoirelab-sortinghat/blob/muggle/config/settings/devel.py#L24.
