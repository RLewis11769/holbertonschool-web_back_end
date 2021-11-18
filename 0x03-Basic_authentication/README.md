# Basic Authentication



## Server Setup

1. Make sure all required programs are installed:

```
pip3 install -r requirements.txt
```

2. Start the server-side server in one terminal

```
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

3. In another terminal, make sure the client-side server is working:

```
curl "http://0.0.0.0:5000/api/v1/status" -vvv
```
