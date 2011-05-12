# Dorothy is a Tornado deployer. #

 -------------------------------------------------------------------

## Usage:##
 
_Start a Tornado application on a set of ports:_

    $ dorothy 'python /path/to/app.py' -l:PORT1 -l:PORT2 start
 
_Stop a Tornado application by specifying the port:_

    $ dorothy -l:PORT1 stop
 
_Restart an application_

    $ dorothy 'python /path/to/app.py' -l:PORT2