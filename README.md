# NinjaGame-backend-game
The backend game server for my ninja game school project

Status:
right now the project is a chat app using channels and redis

# To run the development server:
make a virtual enviroment
```
python -m venv env
```
then activate the enviroment
```
env\Scripts\activate
```
go into the project directory:
```
cd .\chatty\
```
install the required dependencies:
```
pip install -r requirements.txt
```
run a redis container:
```
docker run -p 6379:6379 -d redis:5
```
migrate the database:
```
python manage.py migrate
```
run the development server:
```
python manage.py runserver 8008
```

# To make a docker container:
```
docker build --tag ninjagame-backend-game .
```
and then to run the container:
```
docker run --publish 8008:8008 ninjagame-backend-game
```
