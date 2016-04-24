# WebGmxChecker
Check Mail:Pass lists against validity at the Web.de/Gmx.net Web login. Using Gevent with concurrency.

Usage:
<code>python WEBgmxCh4cker.py mail_pass.txt valid_output.txt Threads</code>


    
    
    
If no parameters given default values will be used (see code).
See sample Mail:Pass list for format.


Installation of dependencies:
pip install gevent
pip install mechanize
pip install fake-useragent

In case you run into problems with using Gevent there is also a version using the standard Threading Lib.
