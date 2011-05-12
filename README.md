# Dorothy is a Tornado deployer. #

## Usage:##
 
Start a Tornado application on a set of ports:

    $ dorothy 'python /path/to/app.py' -l:PORT1 -l:PORT2 start
 
Stop a Tornado application by specifying the port:

    $ dorothy -l:PORT1 stop
 
Restart an application

    $ dorothy 'python /path/to/app.py' -l:PORT2