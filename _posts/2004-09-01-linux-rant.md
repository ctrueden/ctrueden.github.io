---
title: "Linux rant"
date: 2004-09-01 12:46:00 -0600
mood: working
song: "(EnergyRadio.FM - Energy Dance)"
original_url: https://restless-coder.livejournal.com/780.html
---

Lately, I have really gotten into Linux. I have a KVM switch at work that allows me to switch between my PC and my new Linux box. I took the time to learn about the basics of Debian and KDE. One by one, I figured out how to duplicate my Windows workflow shortcuts on KDE, until every shortcut key I use worked the same on Linux as it did on Windows. I determined an appropriate replacement application for every one I ever use on Windows. I have completely switched over, and it is glorious.  
  
"But what about games on Linux?" everyone asks, myself included. I decided to install Linux on my laptop to find out the answer to that question, and the results have been mixed. Overall, since I have switched over, using the laptop to work from home has been a joy. SSH with public/private key pairs makes me grumble with ecstacy. Firefox and Thunderbird are pretty strong (Thunderbird occasionally crashes but then again, so did Eudora on Windows). And I feel much more secure, knowing that script kiddies and virus writers will have a much harder time fucking up my machine. I will not be switching back to Windows.  
  
By now you might be wondering, "If you like Linux so much, why is this post called 'Linux rant'?" You sense a change in tone. And you are correct.  
  
**HOWEVER**  
  
 _Why can't I install kernel modules without building my own kernel from source?!_ Certain laptop features (i.e., advanced power management, CPU throttling, and many PCMCIA wireless networking cards) require additional kernel modules. Fine, I guess. Whatever. Install your modules. It makes no difference to me.  
  
BUT WAIT! I must compile these modules from source, and link them with a kernel ALSO compiled from source? What is the meaning of this? I the user care not for this fuckery! In retribution, I must kill something, somewhere, immediately!  
  
The sin is not that you can enable such basic features on Linux by compiling your kernel from source and linking in additional modules. It is that you MUST do this. Don't get me wrong; it has come a long way since I installed Slackware on my 486-100MHz laptop back in 1998, but there is still a lot of work left to do. Just the thought of my grandmother trying to install Linux makes me nervous, because it should be easier. The thought of her trying to **fucking compile her own fucking kernel** makes several of my body parts droop with sadness.  
  
I have also had difficulties enabling graphics acceleration on my laptop. It's a rather old Sony VAIO with an ATI Rage Mobility M1 card. Now, that card is a piece of crap so I'm not expecting miracles, but unfortunately I've had difficulty finding information on how to get graphics acceleration working. My current theory is that I need to use the "mach64" driver, which is apparently extremely buggy for older cards like the M1. And I have no idea how to obtain and install the mach64 driver, since "apt-cache search mach64" turns up nothing. O gods of Debian, why wouldst thou forsake me? Surely I need not *gasp* download and install something not part of the Debian distribution?  
  
Without graphics acceleration, emulators (snes9x, gens, fceu) are exceedingly choppy, and the Veggie Copter Java shooter game I'm developing lags like a bitch. (Hmm, I suppose that simile is somewhat nonsensical, but hey, it's an idiom.) Oh yeah, and xine instantly kills my KDE session, logging me out without warning, whenever I try to play a video. How nice.  
  
On the plus side, XMMS with aRts is pretty sweet, as is logjam with XMMS music detection. So now you, dear readers, can see that I'm listening to shitty dance music on EnergyRadio.FM, and I'm sure you are all intensely pleased.  
  
Lastly, I know that the title of this LiveJournal promises shallow philosophical ravings. Rest assured they are coming. I plan to post some thoughts on [SENS](<http://www.gen.cam.ac.uk/sens/>) later tonight or tomorrow.
