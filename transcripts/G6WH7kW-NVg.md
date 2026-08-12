---
video_id: G6WH7kW-NVg
title: EEVblog #19 - Rigol caught with their pants down!
url: https://www.youtube.com/watch?v=G6WH7kW-NVg
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EE blog. I'm your host Dave Jones and this is episode number 19. Now in previous blogs I've mentioned the Rigol DS1052E oscilloscope and what great value for money it is in the bottom range end of

**Dave Jones:** scopes and and the excellent quality that Rigol have been able to build into these things for the price. And well, I still think that's the case. But I've been alerted to an issue with this scope by one of my blog viewers,

**Dave Jones:** Whyman. So thanks Whyman. Now Whyman pointed me to a post on a avr.com forum by a member there called Kit Dog and he's actually taken apart his um Rigol DS1052E and he found some interesting things which I I couldn't let go. I've got to

**Dave Jones:** comment on this. It looks like Rigol have been caught a bit with their pants down. As it turns out it looks like they're the ADC chips used in this DS1052E scope are being overclocked. Yes, they're actually overclocking these

**Dave Jones:** parts. They're actually 40 megasample per second parts. They use multiple ones. I'll explain that later but they're 40 They're using the dash 40 megasample per second parts and they're running them it looks like at 100 megahertz. So go figure Rigol are

**Dave Jones:** overclocking. Hmm, something suss here. Let's investigate. Now I'm not going to take my Rigol scope apart because it's still got the uh warranty void if removed sticker and you know, it's this is my own personal one so I probably won't take it apart unless I

**Dave Jones:** get really desperate but we've got some photos from I from the forum member Kit Dog who's taken his apart. So let's examine these photos and see what's inside this little puppy and and what's going on. Now, I was of the understanding that

**Dave Jones:** Rigol actually had their own 1 gig samples per second front-end sampler. They actually developed it themselves, but that that doesn't look like it's the case, at least not in the DS1052 AE. Now, if you take a look at this

**Dave Jones:** inside photo of the main board, you can actually see that they use five analog devices AD9288 -40 analog-to-digital converter chips. And each one of those is a dual ADC, so that gives them a total of 10 ADCs for the front end. And

**Dave Jones:** obviously, they're using these in a sequential sampling mode to get their 1 gig samples per second. Now, you can tell just from the photos. You don't actually need the circuit diagrams to actually see how this thing works. You can tell

**Dave Jones:** from the photos. They've got five of these chips, three on the top, two on the bottom. There's two ADCs per chip. That's a total of 10 analog-to-digital converters. And so, to get 1 gig sample per second, each one of those

**Dave Jones:** ADCs must run, obviously, at 100 meg samples per second or 100 MHz. And quite clearly, the photo of this board shows that the um the chip is actually the -40 part, the 40 MHz version. Now, it is possible

**Dave Jones:** to actually get away with this quite often cuz a lot of the um parts they make, they're they're actually exactly the same die depending on the different speed version. And it's it's likely I I don't know this for

**Dave Jones:** sure, but it's likely that the 100 MHz die is exactly the same as the 40 MHz die. If Rigol have done their own in-house testing on a on a whole bunch of sample of these 40 MHz parts and they

**Dave Jones:** they think they can get away with 100 MHz. Well, obviously they can because the scope works. So, you know, if they've done their own thorough in-house testing then it's it's probably not too bad. It's actually it might have be quite smart to use a 40

**Dave Jones:** MHz part at 100 MHz and save that money. And that's how they get the real low cost in these scopes. But yeah, it's you know, it's got dodgy written all over it. If you don't know what you're doing and you don't take

**Dave Jones:** care. Pre-prepared a thing here of how I believe it's working actually inside. What they've got is five of these AD9288-40 chips which are actually running at 100 MHz. They've got five of these and inside each one is a dual ADC. Two

**Dave Jones:** separate ADCs with their own clocks. And these are clearly going into right next to it. They're going into a Cyclone III FPGA. So, this is a you know, it's a it's a low cost sort of bottom of the bottom of the

**Dave Jones:** range FPGA, but it's got five internal phase locked loops. Five PLLs which can actually be you can actually set the phase output of these in increments of 98 picoseconds. So, that's that's really remarkable. And obviously, I'll explain more of that later, but if

**Dave Jones:** you're running 10 ADCs like this, what you do is if you the clock line for each ADC down here, if you can see it, they actually stagger the clock for each one. So, So got the the clock for each ADC

**Dave Jones:** one through to 10. The they're actually slightly staggered and to get one gig samples per second you stagger them at one nanosecond. And if you drive them the analog input has to drive identically drive each ADC input and that's fairly

**Dave Jones:** critical. Um it's you have to ensure that the analog signal arrives at each ADC at precisely the same uh time for this uh system to actually work. And um inside the FPGA they've obviously got the 8-bit data latches on the output of

**Dave Jones:** each analog to digital converter. And if you stagger the clocks at one nanosecond intervals um and then store them in the internal RAM and that might be a bit tricky actually stagger um actually staggering the storage into the internal

**Dave Jones:** um SRAM. That might be a bit uh tricky but they obviously figured out a way to do that somehow. And so this system can work. You can actually um stagger clocks like this um but you have to be very

**Dave Jones:** careful. Your clocks have to be um spot on. Uh you can't have much uh jitter cuz any jitter in the clock um signals manifest themselves in the sampling. So then when you do your FFT functions in your scope and things like that you can

**Dave Jones:** get errors in your in in your signal and all it's not a it's not a huge deal in a low-end um scope really. So it's but uh you do have to put a lot of care into this system and uh actually refining it

**Dave Jones:** and um you know tweaking it just right so that the um you get very low jitter and highly accurate one nanosecond spaced clocks on the output. And Rigol have obviously able to uh do this. They've actually tweaked the system well enough so that

**Dave Jones:** it works. And you know there's nothing inherently wrong with that. Now I've I've actually contacted the uh Rigol general manager about this. And um I haven't got a response as yet, so it'll be very interesting to see if they

**Dave Jones:** actually respond on this issue and if they've got anything to say about it. Um I'd also like to know if it's um common among scopes or whether it was in an early version or whether or not um current. So if you know, so if you've

**Dave Jones:** got one of these scopes and you want to open it and uh verify, then um that could be you know, that'd be great. Let us know. The other interesting thing is if you look at the photo of the ADCs, um it looks like

**Dave Jones:** they've tried to rub the numbers off. And this is not uncommon um for you know, you sort of hide your trade secrets of how you actually design things. And one of the common methods is to scrub the numbers off. And that's

**Dave Jones:** what it looks like here. I'm not entirely sure, but um you know, that looks like what was going on. But they obviously didn't do it well enough on this chip here, which you can see. And um it clearly shows the dash 40 part.

**Dave Jones:** And and by you know, doing some simple math, they simply must be running at 100 MHz. There's no other way to do it. So looks like Rigol have been caught with their pants down. I wonder what they have to say about it.

**Dave Jones:** Now, you know, my opinion of Rigol is still still quite high. I think they make some really good low-cost gear. The value for money's incredible. And they do work quite well and they're high quality. If you look at

**Dave Jones:** the some other internal photos, the the scope is actually built and laid out very nice. It's quite professional. I I I do actually like the layout of this of the board and everything. It does look really well done. A lot of thought's gone into it.

**Dave Jones:** It's certainly not a slap together um chippy. And which is not surprising considering that Agilent rebadge these scopes as well. So obviously you know, they've got to meet you know, a fairly high standard for Agilent to do that. So, Ryedale still makes some

**Dave Jones:** quality gear, but caught with their pants down. How about that? Go figure. I'm sure we'll hear more about this, and if I do get a reply from Ryedale, I'll let you know.
