# ios_extractor_ipa
extract ipa from jailbroken devices without using frida. Alternative to frida.

how to use: <br/>
`pip install -r requirements.txt`  <br/>
`python extractor_ipa.py`  <br/>

Enter iPhone IP Address: IP_Address of the Jailbroken devices  <br/>
Enter the app name: can be found using filza or ssh to /var/containers/Bundle/Application and run "ls * | grep -B 2 -I '.app' | grep "App_name""  <br/>
Enter root password (default: alpine):   <br/>
