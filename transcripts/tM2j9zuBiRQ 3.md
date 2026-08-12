---
video_id: tM2j9zuBiRQ
title: Siglent Signal Generator Fix
url: https://www.youtube.com/watch?v=tM2j9zuBiRQ
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 32, "3": 49, "4": 65, "5": 83, "6": 98, "7": 114, "8": 138, "9": 149, "10": 162, "11": 178, "12": 204, "13": 221, "14": 239, "15": 261, "16": 281, "17": 299}
---

**Dave Jones:** Hi, just a follow-up to this Siglent SDG2122X generator that failed. What what what what and I figured it might have been like, you know, the file system OS or something like that. I can't remember the details. Original video linked in down below.

**Dave Jones:** Anyway, it failed. It just fails to boot. It doesn't recognize any of the key presses or anything like that and Siglent saw my video. I didn't contact them. They just saw it and sent me an email and say, "Hey, yeah, this

**Dave Jones:** gen that they sent me is had like really early pre-release firmware in it or something. So, yeah, that's the reason why it failed. So, like a proper production version of the firmware shouldn't have failed." And sure enough, yes,

**Dave Jones:** I speculated that, you know, it might be able to update the re-initialize the thing via the micro SD card right down on the board and sure enough they sent me the latest firmware and instructions. So, thank you very much

**Dave Jones:** Siglent. Please excuse the crudity of this screen capture bit. Here we go. Basically, you prepare an SD card. They've sent me the files. You use this HP USB storage formatty thing to format the thing and then you copy the choose FAT32 blah blah blah

**Dave Jones:** blah blah and then you copy over the files. And what do you do then? Safely unplug the card, stick it in, stick it up its clacker, I think and uh Where is it? I don't know. I haven't read it yet. Disassembly blah blah blah.

**Dave Jones:** So, they've actually gone into quite some detail here of how to how to do all this. So, that's pretty impressive. Whether or not they had this Sure, maybe they did have it ready. It's probably for like you know, service agents and dealers and

**Dave Jones:** stuff like with Connect these two pads using a soldering iron. Hmm. What? To change the boot sequence. Oh, okay. Right. Hang on. Let's see if that's in there. Yep. Yep, sure enough. There it is, right down there. Ta-da! So, I've got to uh

**Dave Jones:** short those out. Could have It would have been nice to put on the silk screen there, but you know, I don't necessarily blame you. Don't want people around with that sort of stuff, I guess. Um, if you're a company selling products

**Dave Jones:** like this, and you don't want us uh pain in the ass um, curious people to dick around. So, we short that out. I'm not going to short it out with solder, that's a bit medieval. Um, and blah, you

**Dave Jones:** stick it in and you power it on, and I think it uh it does the business. Anyway, I'll read all the uh requisite details, and I'll format the SD card, and let you know. Okay. Files copied. Let's try the old

**Dave Jones:** tweezer approach. There we go. Stick it down. Hold your tongue at the right angle. Let's power it up. Woohoo! Does it It works! It's alive! Beautiful. No worries whatsoever. Short removed. SD card removed. Let's power it up. Uh by the way, I

**Dave Jones:** didn't have to use that HP uh format utility. I tried, and it gave me a a right disk write protected error. So, I didn't know how to fix that. Um Anyway, so I just copied the files over. It was already a FAT32 microSD card. Uh

**Dave Jones:** copied that over, no worries. Bob's your uncle. Bob is my uncle. Well, we'll see. Come on, boot up. Hey, we're in. Yay! It's back. It's working. It's back from the future utility. I should have the latest version. Siglent do recommend everyone is got

**Dave Jones:** this update to the latest Update to the latest version which is there you go hardware version software version 2.01.01.23 8 whatever that is. Anyway, there you go. Start up times two at reset the startup counter as well. So there you

**Dave Jones:** go. There's a little tip for you eBay scammers out there. If you want to make your instrument as new and you can actually just reflash the firmware like this and it resets the startup timer and you can say it's never been used straight out of

**Dave Jones:** box. Box look I only powered it up twice to get the photos. Anyway, yeah. Thank you very much Siglent. It works. Yes, so no fault with the actual unit itself. I don't blame like you know pre-release firmware or anything like that. So yeah,

**Dave Jones:** I they definitely sent me a pre-release version of this. So that's what it was. Anyway, there you go. Beauty. Winner winner chicken dinner. Catch you next time.
