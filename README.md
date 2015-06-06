# pyrawebs
### Twitter script to send protest tweets to politicians

#### Dependencies  
https://github.com/tweepy/tweepy

#### Install tweepy
    pip install tweepy

#### Setup
**Using OAuth Authentication:**
Download or clone pyrawebs into your directory

    git clone https://github.com/Karlheinzniebuhr/pyrawebs

To begin the process we need to register our client application with Twitter. Create a new application [here](https://apps.twitter.com/ "here"). 

Once you are done you should have your consumer token and secret. 
![](https://raw.githubusercontent.com/Karlheinzniebuhr/pyrawebs/master/images/img3.PNG)
![](https://raw.githubusercontent.com/Karlheinzniebuhr/pyrawebs/master/images/img4.PNG)

Enter these in your keys.py   

![](https://raw.githubusercontent.com/Karlheinzniebuhr/pyrawebs/master/images/img1.PNG)

import your keyfile into pyrawebs.py

![](https://raw.githubusercontent.com/Karlheinzniebuhr/pyrawebs/master/images/img2.PNG)

Start the party

#### Usage

    python pyrawebs.py tweets.txt diputados.txt
    python pyrawebs.py tweets.txt senadores.txt
