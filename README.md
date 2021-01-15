## muxinject

Some Python to inject binaries in restricted environments using tmux sessions.

Example:
--------

Open a terminal and create a tmux session, call it *exploi*

``````
tmux -2 new -s exploit
``````

Start a docker container with a restricted shell,

```
docker run -it busybox sh
```


Then open another terminal, 
and create your payload, a local file called *payload.tar.gz*.
and inject it into the *busybox* container.

``` sh

python muxinject.py
```
