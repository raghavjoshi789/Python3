$ ### WHAT IS __main__ IN PYTHON AND HOW WORKS? ###
$ 
$ ### WHERE I AM STAY  ###
$ 
$ pwd
/home/mana/Work
$ 
$ ### OKAY. THANKS ###
$ ### please show my main file ###
$ cat hello.py 
print(__name__)

if __name__ == "__main__":
    main
$ 
$ ### OKAY. HOW YOU call to me ###
$ ### WAIT. we call to as word saylhello ###
$ ### show sayhello ###
$ 
$ cat sayhello.py 
import hello

print('Main file is:',__name__)
print('Where is main file:',hello)

$ 
$ ### Thanks. Now run sayheolle ###
$ python3 sayhello.py 
hello
Main file is: __main__
Where is main file: <module 'hello' from '/home/mana/Work/hello.py'>
$ 
