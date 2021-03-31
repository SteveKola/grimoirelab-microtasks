### Microtask-0

> Download PyCharm and get familiar with it. 

I downloaded Pycharm from the [official site](https://www.jetbrains.com/pycharm/) and familliarized with it using [this tutorial](https://www.jetbrains.com/help/pycharm/meet-pycharm.html).

## Microtask-1

> Set up a dev environment to work on GrimoireLab.
> 
**Note:** Everything I did here was done by following 
[this guide](https://github.com/chaoss/grimoirelab-sirmordred/blob/master/Getting-Started.md#getting-started-).

### Setting up the repositories locally

To setup the dev environment for Grimoirelab, 
I forked and cloned all the Grimoirelab's components repositories into a target folder (i.e. sources);

- [SirModred](https://github.com/chaoss/grimoirelab-sirmordred)
- [ELK](https://github.com/chaoss/grimoirelab-elk)
- [Graal](https://github.com/chaoss/grimoirelab-graal)
- [Perceval](https://github.com/chaoss/grimoirelab-perceval)
- [Perceval for Mozilla](https://github.com/chaoss/grimoirelab-perceval-mozilla)
- [Perceval for OPNFV](https://github.com/chaoss/grimoirelab-perceval-opnfv)
- [Perceval for Puppet](https://github.com/chaoss/grimoirelab-perceval-puppet)
- [Perceval for FINOS](https://github.com/Bitergia/grimoirelab-perceval-finos)
- [SortingHat](https://github.com/chaoss/grimoirelab-sortinghat)
- [Sigils](https://github.com/chaoss/grimoirelab-sigils)
- [Kidash](https://github.com/chaoss/grimoirelab-kidash)
- [Toolkit](https://github.com/chaoss/grimoirelab-toolkit)
- [Cereslib](https://github.com/chaoss/grimoirelab-cereslib)
- [Manuscripts](https://github.com/chaoss/grimoirelab-manuscripts)

I also had to set the original repo as the upstream branch, and my forked repo as the remote branch. 
I did this using an [automation script](https://gist.github.com/vchrombie/4403193198cd79e7ee0079259311f6e8), written by @vchrombie.

To use the script, I ran this on my terminal after downloading the script;

```$ python3 glab-dev-env-setup.py --create --token xxxx --source sources```

where **token** is my Github Personal Access Token which ****must*** be granted access to create/delete repos. 
And **sources** is the target folder to store the cloned repositories.

### Setting up Pycharm

After downloading Pycharm, as per microtask-1, I created a project in the grimoirelab-sirmordred directory. 
PyCharm automatically created a virtual env, where I installed the dependencies listed in each (grimoirelab's components) requirements.txt, 
**excluding** the ones concerning the grimoirelab components.

To install the dependencies, you I clicked on ```File -> Settings -> Project -> Project Interpreter```, 
and then the ```+``` located on the top right corner.

Once I did that, I'd type in the name of the package I wish to install. It'd bring it up and I'll click on `install`.

Here is the end result after doing that;

![image](https://user-images.githubusercontent.com/45284829/113125924-07ebf100-920f-11eb-8b29-ff9361c4f85e.png)

Afterwards, I added the dependencies to the grimoirelab components via `File -> Settings -> Project -> Project Structure`. 
Then I navigated to the `sources` folder, and click on all the components' repo except `grimoirelab-sirmordred`.

Here is how the final results look like;

![image](https://user-images.githubusercontent.com/45284829/113126421-86489300-920f-11eb-80ca-02548a5a5f30.png)
