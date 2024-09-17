# Test

## Q1
#### > When a signal is sent, the connected receivers functions are executed in the same thread and at the same time as the signal is sent. This means the sender waits for all receivers to finish before continuing.
For this i have made a function create_user_view which create new user at that time signal will be sent to slow_handler that take signal and make signal slow by our code .
Output:
Creating user...
Signal received! Processing...
Signal processing completed.
User created!

## Q2
#### > Yes, by default, Django signals run in the same thread as the caller. The signal handlers are executed in the same thread that triggered the signal.
By using inbuilt we have checked both caller and signal handler which are showing same id.
Output:
Caller thread ID: 20612
Signal handler thread ID: 20612

## Q3
#### > By default, Django signals do run in the same database transaction as the caller, when triggered within a view or function wrapped by a database transaction .
Output:
Caller: Creating user...
Signal received! Processing...
Signal processing completed.
Signal handler thread ID: 17212
Signal: Creating profile...
Signal: Profile created.
Caller: User created.



## You are tasked with creating a Rectangle class with the following requirements:
File views.py for code which is post method api and its url in urls.py file 
Output:
[
    {
        "length": 5
    },
    {
        "width": 10
     }
]

