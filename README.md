# ios_extractor_ipa
extract ipa from jailbroken devices without using frida. Alternative to frida.

how to use:
pip install -r requirements.txt
python extractor_ipa.py

Enter iPhone IP Address: IP_Address of the Jailbroken devices
Enter the app name: can be found using filza or ssh to /var/containers/Bundle/Application and run "ls * | grep -B 2 -I '.app' | grep "App_name""
Enter root password (default: alpine): 
