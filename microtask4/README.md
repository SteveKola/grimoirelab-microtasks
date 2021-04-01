## Micro-task 4

> Set up the developer environment of SortingHat ([muggle branch](https://github.com/chaoss/grimoirelab-sortinghat/tree/muggle)).

**Note:** Everything I did here was done by following [this guide](https://github.com/chaoss/grimoirelab-sortinghat/tree/muggle).

The muggle branch is the developing branch of SortingHat.

### Requirements

- Python >= 3.6
- Poetry >= 1.1.0
- MySQL >= 5.7 or MariaDB 10.0
- Django = 2.2
- Django-MySQL >= 3.2.0
- Graphene-Django >= 2.0

### Installation

I cloned the repository and changed to `muggle` branch, using the following
commands;

```
$ git clone https://github.com/chaoss/grimoirelab-sortinghat
$ git checkout muggle
```

### Installing the Backend

#### Requirements

##### Poetry

[Poetry](https://python-poetry.org/docs/) was used for managing the project. I installed Poetry using the command below;

```$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -```

##### mysql_config

`mysql_config` is part of both `libmysqlclient-dev` and `libmariadbclient-dev` packages. 
Since I'm using MySQL database server, I installed the MySQL-specific package using the command below;

```$ sudo apt install libmysqlclient-dev```

#### Installation and Configuration

I installed the dependencies via Poetry with the command below;

```$ poetry install```

The above command also created a virtual environment, which activated using;

```$ poetry shell```

Afterwards, I applied the schema migrations and created a superuser:

```
$ ./manage.py makemigrations --settings=config.settings.devel
$ ./manage.py migrate --settings=config.settings.devel
$ ./manage.py createsuperuser --settings=config.settings.devel
```
**Note:** I came across this error while running the codes above;

```django.db.utils.OperationalError: (1049, "Unknown database 'sortinghat_db'")```

which I solved by creating a new database called `sortinghat_db`.

### Running the Backend

I ran the SortingHat backend Django app using;

`$ ./manage.py runserver --settings=config.settings.devel`

Below are the final results;

![image](https://user-images.githubusercontent.com/45284829/113215123-541c4d00-9272-11eb-9fba-007d326b0e60.png)

![image](https://user-images.githubusercontent.com/45284829/113215523-defd4780-9272-11eb-8550-1ce79a2693ce.png)

### Frontend

#### Requirements

##### yarn

To compile and run the frontend, `yarn` is to be installed first. 
And it can only be installed with `npm` (NodeJS Package Manager).
Since I already have `npm` installed, I ran the command below to install `yarn`;

`sudo npm install -g yarn`

#### Installation and Configuration

I installed the dependencies using;

```
$ cd ui/
$ yarn install
```

**Note:** I encountered the error below while running the above code;

```
pkg_resources.DistributionNotFound: The 'gyp==0.1' distribution was not found and is required by the application
```

which I solved by following [this guide](https://github.com/nodejs/node-gyp/issues/2273) 
and running the commands below;

```
$ sudo npm install --global npm@latest
$ sudo npm install --global node-gyp@latest
$ sudo npm config set node_gyp $(npm prefix -g)/lib/node_modules/node-gyp/bin/node-gyp.js
```
#### Running the frontend

I ran the SortingHat frontend Vue app using;

`$ yarn serve`

And I got the following results;

![image](https://user-images.githubusercontent.com/45284829/113221334-bc702c00-927c-11eb-8eb7-39f8468d498b.png)
![image](https://user-images.githubusercontent.com/45284829/113299821-2fb58480-92f5-11eb-9cf3-9cdb15d731b3.png)

### Running tests
There are unit tests in SortingHat for both frontend and backend.

#### Backend Test Suite

`$ ./manage.py test --settings=config.settings.testing`

gives the result below;

![image](https://user-images.githubusercontent.com/45284829/113223802-e7a94a00-9281-11eb-92dd-c71b5f134e63.png)


#### Frontend Test Suite

```
$ cd ui/
$ yarn test:unit -u
```

gives the result below;

![image](https://user-images.githubusercontent.com/45284829/113223199-85037e80-9280-11eb-87b0-a54782171bfc.png)


