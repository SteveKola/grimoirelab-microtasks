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

```$ git clone https://github.com/chaoss/grimoirelab-sortinghat

$ git checkout muggle
```

### Installing the Backend

#### Requirements

##### Poetry

[Poetry](https://python-poetry.org/docs/) was used for managing the project. I installed Poetry using the command below;

```curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -```

##### mysql_config

`mysql_config` is part of both `libmysqlclient-dev` and `libmariadbclient-dev` packages. 
Since I'm using MySQL database server, I installed the MySQL-specific package using the command below;

```sudo apt install libmysqlclient-dev```

#### Installation and Configuration

I installed the dependencies via Poetry with the command below;

```$ poetry install```

The above command also created a virtual environment, which activated using;

```$ poetry shell```

Afterwards, I did the schema migrations and created a superuser:

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
