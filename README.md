# dns_spoofer
This tool will spoof the dns request and redirect that request to another page
NOTE: run this command before using this tool
   you need ip tables to run these commands
    iptables -I OUTPUT -j NFQUEUE --queue-num 0
   iptables -I FORWARD -j NFQUEUE --queue-num 0
   
Steps to Run This tool:
  1. git clone https://github.com/krishpranav/dns_spoofer
  2. cd dns_spoofer
  3. sudo chmod 777 *
  4. python3 -m pip install -r requirements.txt
  5. python dns_spoofer.py
  
  THIS TOOL IS CREATED BY KRISHNA PRANAV
