# WebGmxChecker
Check Mail:Pass lists against validity at the Web.de/Gmx.net Web login. Using Gevent with concurrency.

Usage:
"python WEBgmxCh4cker.py mail_pass.txt valid_output.txt Threads"
Example:
"python WEBgmxCh4cker.py mail_pass.txt valid_output.txt 128"
    
    
    
If no parameters given default values will be used (see code).
See sample Mail:Pass list for format.


Installation of dependencies:
pip install gevent
pip install mechanize
pip install fake-useragent
