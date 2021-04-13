## Microtask 2

> Execute micro-mordred to collect, enrich and visualize data from Git repositories. 
> 
After setting up my dev environment for Grimoirelab, as specified in 
[microtask1](https://github.com/SteveKola/grimoirelab-microtasks/tree/main/microtask0%261), 
I proceeded to execute micro-mordred by defining up the setup.cfg and projects.json. And afterwards, running the following two commands;

```
micro.py --raw --enrich --cfg ./setup.cfg --backends git cocom
micro.py --panels --cfg ./setup.cfg
```

## Troubleshooting

I spent the bulk of my time on this issue as I encountered lots of issues. I list most of the errors I encountered and how I solved them below;

### Sending HTTP requests to HTTPS servers

>  2021-03-23 13:51:14,296 Retrying (Retry(total=15, connect=21, read=8, redirect=5, status=None)) after connection broken by 'SSLError(SSLError(1, '[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1123)'))': /
>  
I solved it by changing the `https` in ES' collection and enrichment URLs to `http`.

### MySQL Server start failure

> sortinghat.exceptions.DatabaseError: Can't connect to MySQL server on '127.0.0.1' ([Errno 111] Connection refused) (err: 2003)
> 
Apparently, installing MySQL Server via `docker-compose.yml` was not working for me. So I opened my bash and ran the following commands;

```
sudo apt --purge remove mariadb-server
sudo apt --purge remove mysql
sudo apt autoremove
sudo apt autoclean
sudo apt update
sudo apt install mariadb-server
mysql -V
echo -e "\n\nchecking status\npress q to quit\n\n"
sudo systemctl status mariadb
sudo mysql_secure_installation
```

### Running micro-mordred via Project Structure not working on Terminal

As stated in the guide, I ran the below command on the terminal after adding all the grimoirelab's components to
Project Structure;

`python utils/micro.py --raw --enrich --cfg ./setup.cfg --backends git cocom`

And I got the following error;

```
Traceback (most recent call last):
 File "utils/micro.py", line 30, in <module>
   from sirmordred.config import Config
ModuleNotFoundError: No module named 'sirmordred'
```

For some reason I couldn't fathom out, it seems it is a path problem. I worked around it by adding a configuration to `micro.py`
and running it, as stated [here](https://www.google.com/url?q=https://github.com/chaoss/grimoirelab-sirmordred/blob/master/Getting-Started.md%23execution-&sa=D&source=hangouts&ust=1618387267099000&usg=AFQjCNGL3LmXUVdCniglJjNkiG9yT4M9Hg).

### `Test_sh` database not initialized

![image](https://user-images.githubusercontent.com/45284829/114519974-d7597d80-9c38-11eb-97f1-fcac08d2fdef.png)

I solved it by opening MySQL shell and creating the `test_sh` database manually.

### ElasticSearch not working

By running `micro.py --panels --cfg ./setup.cfg` to visualize the panels, I discovered that Kibiter was not running, which is due to its dependency on ElasticSearch. 
ElasticSearch was the main culprit here. 

![image](https://user-images.githubusercontent.com/45284829/114520577-80a07380-9c39-11eb-802d-2f161ca50d14.png)

#### Solution

I tried many things here, including;

- Using the SearchGuard version of ES docker-compose.
- Increasing the virtual memory of my machine to 262144.
- Decreasing ES' JVM's heap size from 4GB to 512MB.
- Increasing my Docker machine's memory from 1G to 8G.
- Creating swap spaces of up to 24GB.

None of them worked! 😥

I later found the that the main reason was because my PC's free memory is quite low (less than 25GB) 
and installing ElasticSearch and Kibiter via Docker-compose doesn't give me the flexibility to tweak their 
configurations so as for them to accomodate my low memory issue.

I solved this by installing the `tar.gz` files of ElasticSearch-6.8.6 and Kibiter-6.8.6, and it finally worked!

![image](https://user-images.githubusercontent.com/45284829/114522110-f0632e00-9c3a-11eb-91c1-384a6840735d.png)

#### But it didn't work fully...

![image](https://user-images.githubusercontent.com/45284829/114522272-230d2680-9c3b-11eb-82e2-63eb66f26313.png)

I got a blank page when I went to check the dashboards. 

I checked Kibiter settings to see if any index was being created.

![image](https://user-images.githubusercontent.com/45284829/114522675-7d0dec00-9c3b-11eb-9d8d-5cb22809e2d5.png)

Then I checked if the dashboards were created, and they were.

![image](https://user-images.githubusercontent.com/45284829/114522571-6798c200-9c3b-11eb-9020-230798f1d05a.png)

I was spending way too much time on this particular task so I had to abort and move on.
