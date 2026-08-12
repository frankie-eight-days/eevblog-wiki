---
video_id: tM2j9zuBiRQ
title: Siglent Signal Generator Fix
url: https://www.youtube.com/watch?v=tM2j9zuBiRQ
source: youtube-asr
timestamps: {"0": 1, "1": 15, "2": 25, "3": 39, "4": 63, "5": 85, "6": 96, "7": 107, "8": 124, "9": 143, "10": 155, "11": 165, "12": 182, "13": 202, "14": 209, "15": 221, "16": 236, "17": 253, "18": 281, "19": 293, "20": 303}
---

**Dave Jones:** Hi, just a follow-up to this Siglent SDG2122X generator that failed. What what what what and I figured it might have been like, you know, the file system OS or something like that.

**Dave Jones:** I can't remember the details. Original video linked in down below. Anyway, it failed. It just fails to boot. It doesn't recognize any of the key presses or anything like that and Siglent saw my video.

**Dave Jones:** I didn't contact them. They just saw it and sent me an email and say, "Hey, yeah, this gen that they sent me is had like really early pre-release firmware in it or something.

**Dave Jones:** So, yeah, that's the reason why it failed. So, like a proper production version of the firmware shouldn't have failed." And sure enough, yes, I speculated that, you know, it might be able to update the re-initialize the thing via the micro SD card right down on the board and sure enough they sent me the latest firmware and instructions.

**Dave Jones:** So, thank you very much Siglent. Please excuse the crudity of this screen capture bit. Here we go. Basically, you prepare an SD card. They've sent me the files. You use this HP USB storage formatty thing to format the thing and then you copy the choose FAT32 blah blah blah blah blah and then you copy over the files.

**Dave Jones:** And what do you do then? Safely unplug the card, stick it in, stick it up its clacker, I think and uh Where is it? I don't know. I haven't read it yet.

**Dave Jones:** Disassembly blah blah blah. So, they've actually gone into quite some detail here of how to how to do all this. So, that's pretty impressive. Whether or not they had this Sure, maybe they did have it ready.

**Dave Jones:** It's probably for like you know, service agents and dealers and stuff like with Connect these two pads using a soldering iron. Hmm. What? To change the boot sequence. Oh, okay.

**Dave Jones:** Right. Hang on. Let's see if that's in there. Yep. Yep, sure enough. There it is, right down there. Ta-da! So, I've got to uh short those out. Could have It would have been nice to put on the silk screen there, but you know, I don't necessarily blame you.

**Dave Jones:** Don't want people around with that sort of stuff, I guess. Um, if you're a company selling products like this, and you don't want us uh pain in the ass um, curious people to dick around.

**Dave Jones:** So, we short that out. I'm not going to short it out with solder, that's a bit medieval. Um, and blah, you stick it in and you power it on, and I think it uh it does the business.

**Dave Jones:** Anyway, I'll read all the uh requisite details, and I'll format the SD card, and let you know. Okay. Files copied. Let's try the old tweezer approach. There we go.

**Dave Jones:** Stick it down. Hold your tongue at the right angle. Let's power it up. Woohoo! Does it It works! It's alive! Beautiful. No worries whatsoever. Short removed. SD card removed.

**Dave Jones:** Let's power it up. Uh by the way, I didn't have to use that HP uh format utility. I tried, and it gave me a a right disk write protected error.

**Dave Jones:** So, I didn't know how to fix that. Um Anyway, so I just copied the files over. It was already a FAT32 microSD card. Uh copied that over, no worries.

**Dave Jones:** Bob's your uncle. Bob is my uncle. Well, we'll see. Come on, boot up. Hey, we're in. Yay! It's back. It's working. It's back from the future utility. I should have the latest version.

**Dave Jones:** Siglent do recommend everyone is got this update to the latest Update to the latest version which is there you go hardware version software version 2.01.01.23 8 whatever that is.

**Dave Jones:** Anyway, there you go. Start up times two at reset the startup counter as well. So there you go. There's a little tip for you eBay scammers out there. If you want to make your instrument as new and you can actually just reflash the firmware like this and it resets the startup timer and you can say it's never been used straight out of box.

**Dave Jones:** Box look I only powered it up twice to get the photos. Anyway, yeah. Thank you very much Siglent. It works. Yes, so no fault with the actual unit itself.

**Dave Jones:** I don't blame like you know pre-release firmware or anything like that. So yeah, I they definitely sent me a pre-release version of this. So that's what it was. Anyway, there you go.

**Dave Jones:** Beauty. Winner winner chicken dinner. Catch you next time.
