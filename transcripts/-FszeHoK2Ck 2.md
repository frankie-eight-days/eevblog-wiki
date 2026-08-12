---
video_id: -FszeHoK2Ck
title: EEVblog #1279 - Best Dumpster PC Find Yet!
url: https://www.youtube.com/watch?v=-FszeHoK2Ck
source: youtube-asr
timestamps: {"0": 0, "1": 15, "2": 24, "3": 32, "4": 43, "5": 57, "6": 73, "7": 89, "8": 103, "9": 114, "10": 126, "11": 144, "12": 169, "13": 189, "14": 198, "15": 209, "16": 222, "17": 238, "18": 253, "19": 271, "20": 283, "21": 295, "22": 305, "23": 318, "24": 332, "25": 342, "26": 353, "27": 362, "28": 374, "29": 388, "30": 404, "31": 416, "32": 435, "33": 452, "34": 463, "35": 480, "36": 491, "37": 505, "38": 515, "39": 527, "40": 544, "41": 560, "42": 572, "43": 588, "44": 606, "45": 619, "46": 631, "47": 647, "48": 666, "49": 674, "50": 692, "51": 704, "52": 713, "53": 726, "54": 742, "55": 761, "56": 771, "57": 782, "58": 794, "59": 805, "60": 820, "61": 835, "62": 846, "63": 856, "64": 872, "65": 885, "66": 897, "67": 906, "68": 917, "69": 932, "70": 944, "71": 957, "72": 969, "73": 980, "74": 993, "75": 1011, "76": 1021, "77": 1038, "78": 1050, "79": 1067, "80": 1090, "81": 1104, "82": 1113, "83": 1128, "84": 1135, "85": 1148, "86": 1157}
---

**Dave Jones:** Hi, yes, I'm back for 2020 even though I've released uh like four videos in 2020. I actually shot those in 2019. I've been on walkabout for a couple of weeks, just got back, and I've been checking out the dumpster, of course, and this is my latest dumpster find.

**Dave Jones:** Um I thought there were a couple of monitors down there as well as a PC. I haven't really uh looked at that, but it's a Core i7. I haven't picked it up yet.

**Dave Jones:** Here's a photo from down in the dumpster room, and I thought this was just a monitor. I uh sort of like saw it from the side on, and I thought, "Oh, isn't that slim?

**Dave Jones:** Look at that. That's really sexy. Looks like an alloy case. So, I'm going to pick that up." And I picked it up, and sure enough, look at the back of it.

**Dave Jones:** It's a Lenovo jobbie. And then I saw the sticker on the front, Core i5 7th gen processor. It's the Lenovo IdeaCentre. It's one of these all-in-one PCs. Um I'm not the first time I've found something like this in the dumpster, but I haven't found one this nice.

**Dave Jones:** What is that? Probably a 22-in. It's not huge, but it's one of these all-in-one PCs. Obviously, got a grill down here. Can I feel some speakers down there? And this is a really sexy uh all-in-one monitor.

**Dave Jones:** That's absolutely fantastic. It's got uh USB, it's got Ethernet, it's got uh weird-ass power connector. I just noticed that. Yeah, damn. Just started shooting this video all excited, and I don't think I have a power connector like that.

**Dave Jones:** Oh, it's square. Look at that. Look at that weird-ass turd. Oh, I don't like it all. Anyway, external HDMI monitor for a second monitor. Wow. Uh 20 volts uh 4 amps there for those playing along at home.

**Dave Jones:** It's got all the regulatory compliance uh marks. I've done a video on that compliance marks. Do I have to do another one? Anyway, that was manufactured um 9th month, 2017.

**Dave Jones:** Wow. Like, why would somebody throw this out? There's got to be something wrong with it, you would presume. Oh, it's still got the protective cover on the Lenovo. Beautiful, like a bought one.

**Dave Jones:** And on the back as well, look at this. Oh, that's pornographic. Demonetized. So, it turns out this is a Lenovo special with a like a square pin in the middle and contacts top and bottom.

**Dave Jones:** But, it's budge time. So, what I've got one of these leaf inserts from a single inline connector and they've got the springy thing on there and it just so happens to have a nice little snug fit on I assume the top and bottom are the exact same content and I'm assuming they're ground cuz look they've used a barrel jack um thing for center positive there even though it's

**Dave Jones:** not round. It's bloody square, bloody Lenovo. Oh, and I found that this resistor fits just fine and it's important to use precision here, point double 05% 100 ohms. Thank you very much and that just so happens to fit nicely into the center like that and just be careful that doesn't short out to the chassis.

**Dave Jones:** Now, I should be able to make contact and at least power it up. And of course, if it works or I can get it repaired, then I you know, I'll buy a proper aftermarket adapter for it.

**Dave Jones:** Right, so let's power this puppy up and see if she works. I've got my power supply 20 volts, set it to 5 amp current limit. We only need 4 and 1/2, so that should be good enough for Australia.

**Dave Jones:** Let's go and switch the output on. Okay, we're getting just residual. So, where's the power button on the back? Nope. No joy. Hold down the power button. Damn. What what WHAT WHAT?

**Dave Jones:** DOPE. OKAY, I THINK I'VE goofed it. Thanks to the person on Twitter who mentioned that yeah, you might need a pull down resistor on this. As it turns out um the center pin is not power.

**Dave Jones:** It's the two outer pins on there a positive negative and the center pin is for a power detection resistor that you've got to like put it to is that even like is that symmetrical?

**Dave Jones:** Like that no, it must only plug in one way. Anyway, it's it's dumb. Bloody Lenovo like you would assume like cuz it says up here like center positive. I put positive in the center, but this is not what I'm seeing when I Google Lenovo power adapter pin out.

**Dave Jones:** All right, so first thing I'm going to do is probe these two outer contacts and see if they're shorted. Oh, they are. Okay, so that is center positive. I stand corrected.

**Dave Jones:** So that image that I've got seems to be incorrect. You can't unless there's a dead short inside there which I doubt. You can insert that either way I think by the looks of it.

**Dave Jones:** I can't see how that thing's keyed. So yeah, that makes sense that they're both outer ground. So that's okay. And just double checking that I don't have one. Nope.

**Dave Jones:** Bloody Murphy. And if I check between the HDMI shell, yep, they're both ground. So those two outer pins are definitely ground and that center one should be positive, but let me measure that.

**Dave Jones:** Yeah, 42 meg. Go the other way. Mhm. The good thing about having the HDMI connector there like that, I can just plug that in, use that outer shell. So center pin outer shell.

**Dave Jones:** Let me try that again just in case it wasn't making contact with the pin somehow. Let's do this one more time. Nope. It's dead, Jim. Aha, pays to have a second look.

**Dave Jones:** Here it is. I went down there and thoughtfully they dumped this out, and there it is. There's the Lenovo adapter. I should have had a better look down there.

**Dave Jones:** The power connector on it. Anyway, let's give this a burl, cuz there could be some smarts going on in that adapter. Oh! I can hear something. It's got a little fan.

**Dave Jones:** It's got a little It's Look at this. Nothing wrong with the screen. It's booting. Ah! Is there something wrong with it? Like, is it's touch screen as well? Ah!

**Dave Jones:** Winner, winner, chicken dinner! No. Oh, no. Touch screen. Touch screen works. Yep. Wow. Can't believe somebody would toss this out. It's not that old. Uh the set i5 7200U uh processor in it.

**Dave Jones:** It's got a benchmark of like 4500. It's still pretty good. Well, maybe there's some intermittent problem, you know, it overheats and shuts down or or something like that. But um anyway, it does have a uh password access, but uh yeah, I should be able to bypass that.

**Dave Jones:** And I just checked on eBay, and there's tons of parts available for these. Motherboards and back panels and fans and all sorts of stuff. Um fantastic. And I found one like a brand new, like new old stock, for uh 780 bucks.

**Dave Jones:** Okay, to bypass our Windows password here, let's switch it on. Then we wait, twiddle our thumbs, twiddle our thumbs until we get the little spinny Windows icon, and then press the button and wait for it to power down, and do that again a second time.

**Dave Jones:** Power it on. Wait for that again, and once again, hold down the button as soon as the spinny icon appears. Wait for it to shut down. And then wait a couple of seconds, and let's re-power it for the third time.

**Dave Jones:** And the third time we should get lucky. It should go into system recovery mode. Please wait. Haha! Ta-da! We're in system recovery mode. Now I can bypass the password.

**Dave Jones:** Hmm. See advanced repair options. Ta-da! Okay, we'll go troubleshoot. Then we'll go advanced options. Okay, we want more recovery options. We want system image Okay, we have to forgot your password or don't see your account.

**Dave Jones:** And then we can restart. Okay, I went through that sequence again and it said repairing your PC, diagnosing your PC. And we should be able to skip the user account.

**Dave Jones:** Let's go into the advanced options again. Troubleshoot, advanced options, system image recovery. Ta-da! And now we can actually Let's cancel this and we can actually select a system image.

**Dave Jones:** Next and we can actually now get in there and select the file system. So, we will get access to the file system and we can rename a few things.

**Dave Jones:** Okay, so what we want now is advanced like this and we want to install a driver, but we're not actually going to install a driver. We've got access, bingo, to our file system.

**Dave Jones:** Fantastic. So, we're looking for a file called utilman. I've actually got a mouse now, so make this a bit easier. Okay, utilman is not in there. So, we go back and by the way, we can actually access our different drives here, so you can get access to any of the file system.

**Dave Jones:** Hang on. So, it wasn't in boot system 32. Let's go into Windows system 32. Utilman, that's the one we want. We want to right click. We want to rename that and you want to rename that to anything, you know, utilman one or something.

**Dave Jones:** Doesn't matter what you rename it to. Then we want to refresh that. Utilman one. Fantastic. Now, what we want to go up to is to find our command cmd.

**Dave Jones:** There it is. Cmd and then we want to rename that utilman. Okay, command has been renamed utilman. Refresh that. We now have utilman. Okay, so what we want to do is cancel that.

**Dave Jones:** Cancel that. Cancel that. 10 exit and continue to Windows 10 and it will reboot and get access to uh the command prompt now. We should get access to ease of access down here and bingo, ease of access brings up our command prompt.

**Dave Jones:** Ta-da! utilman.exe, which is now the uh command prompt window. So we've got a full command prompt access. Now we can bypass it. Helps if I spell it right, doesn't it?

**Dave Jones:** Bloody hell. So I should find a keyboard and plug it in. Now we just want to uh reset the uh username that we want to do. So net user uh user and then the actual username and asterisks and password for the new user.

**Dave Jones:** Um you can type in any password you want. We'll just uh put enter. So enter will be the new password. Bingo. Whoop. Aha, if we get an error 8646, it means that they're not using a local Windows account, they're using a Microsoft account.

**Dave Jones:** And uh recently Microsoft have forced people to use a Microsoft account for Windows 10 Home, which is what we're using here apparently. So uh bummer. But it turns out if we just type in netplwiz, um then we can actually get up here and add uh different accounts to log in.

**Dave Jones:** Beauty. And if we disable the password here, um bingo, we can get the username and passwords. And And do now is add my own Dave account. There I am.

**Dave Jones:** And uh then change that to local group administrators. So I run netplwiz. I am now an administrator. Beauty. And bingo, I chose Dave down here. I missed that. And we're signing in as Dave.

**Dave Jones:** Come on, you can do it. Haha. And we're reset up. Beauty. We're in like Flynn. But that was a bit of an effort though because this used a Microsoft account for a login.

**Dave Jones:** So the usual way to bypass this didn't work. So I had to hack around a bit. Couldn't really find a proper thing online so I just winged it. So we don't want any of that rubbish.

**Dave Jones:** So we accept and tada! We're in like Flynn. We now have a Windows 10 PC but it looks like I've been using this for quite some time now and it's yeah, it's just working a treat.

**Dave Jones:** So doesn't seem to be any sort of thermal issue. Does it get hot on the back? Nah, not really. So a little bit warm on the side there but that's where the main processor board must be but What a that's a fantastic score from the dumpster.

**Dave Jones:** Unbelievably good. And I just removed that other pesky user and we've only got Dave left. So yeah, it's like a bought one. Uh let's plug in the interwebs. I just want to just reboot this once to make sure that uh that user is goneski and only Dave remains.

**Dave Jones:** Dave, just a moment. Thank you. And we're straight in. None of that password rubbish. And for those curious it seems to be a particularly clean machine. There's really nothing on it.

**Dave Jones:** I just Norton was installed so I'll uninstall that but apart from that yeah, it's it's been wiped. And this is what we have for those playing along at home.

**Dave Jones:** 2.5 gig i5 7200U running at just over a volt 1.1 volts there. 15 watts maximum so you know, it's not a beast but it's like it's still like 4 and a half thousand pass mark.

**Dave Jones:** It's still pretty good. There's the cache. Main board. There we go. Firmware's a bit out of date. Maybe we can get a later one. It's got 8 gig of memory.

**Dave Jones:** That'll do for those playing along at home, and graphics Uh it's Intel HD Graphics 620, so it's just built into the uh CPU, so that's all right. Let's compare it with a Ryzen Threadripper, shall we?

**Dave Jones:** And there you go, use that as a reference there. It's 80% uh because it's not multi uh cuz it's got more cores. Um but the uh the single core is only 80% of a uh Threadripper 1950X they're using this particular benchmark, you know, your mileage may vary.

**Dave Jones:** Try and keep it very concise for Speakers are a little bit tinny, but uh there you go. We're Dave got jewel Dave, but it's face tracking on Dave, too.

**Dave Jones:** So, yeah, a little bit tinny for that, but uh that's what you expect. Usable speakers in it. Nice. Oh, all right. Very quick teardown. Couple of screws on the bottom here.

**Dave Jones:** Not sure. What's this? Oh. Oh, what's that? Oh, there's extra Look at that. There's extra USB ports. Oh, wow, that's nice. These are USB 3s, too. Oh, that's that's beautiful.

**Dave Jones:** Ah, Bobby Dazzler, hats off to that. Oh, it's a camera. Look at that. That's your pop-out camera with two extra USBs. Ah, NSA spy enabled. Well, that's actually quite nice.

**Dave Jones:** There's a little uh catch there, and then it's just got plastic clips for the rest of it. And we're in like Flynn. There you go. Uh 256 gig solid state drive, you know, that's okay.

**Dave Jones:** I think there's 40 gig free, something like that. Might be able to clean up a bit more. You can always uh replace that. Little tiny fan there. Yeah, the thermals aren't great with this uh tiny little fan.

**Dave Jones:** It's all shooting out the top here. Um you know, it is uh temperature controlled, so it does uh cycle with uh various modes and stuff like that. I've got some shielding on here.

**Dave Jones:** That'll be the main uh processor. There's our power switch. Uh oh, there's our Wi-Fi antenna. These are our little speakers down here. Oh, they're little rubber baby buggy bumper compliant mount.

**Dave Jones:** That's nice. Nice attention to detail. Got two of those. Another one over there. There's the mechanism for the camera and the USBs. Nice. There you go. That was easy to get off.

**Dave Jones:** We just took off the screws. Four screws here for the stand mount. And we've got access to the main processor down in there. So, there you go. There she is down there.

**Dave Jones:** That's it. That's yeah, none of that socket rubbish and heat pipe running out over to the fan over there. Not the most efficient thing, but you know, you got to get the form factor down somehow.

**Dave Jones:** And there you go. Up upgradeable there. Not sure to how how much might be able to put 16 in there perhaps, but yeah, we've only got the one slot.

**Dave Jones:** And there's our little Wi-Fi module. It's the coax buggering off down under there around to our Wi-Fi antenna. And well, that's all she wrote. Not that exciting, is it?

**Dave Jones:** Battery backup and like it's it's 2017 model. Fantastic. So, yeah, I'm not going to tear it down any further than that. It's not warranted. It's a beauty. So, it's a very nice all-in-one design there and what felt like an alloy case is actually um yeah, ABS.

**Dave Jones:** Thank you very much for playing. There's all the marks for those playing ABS plus PETs. So, yeah, I'm not going to write home to my mom about it, but like top score.

**Dave Jones:** And I I assume there's no like long-term reliability issues, but they could be. You know, I've had things scored from the dust before and they seem to work when I get them in the lab and then I start using them for a few days and they have I've across So, anyway, I'll leave it running for a while like a burn it in.

**Dave Jones:** I might do it run a memory and a CPU burning thing just to see how it's going and yeah, maybe I can even upgrade it if I find a decent use for it.

**Dave Jones:** So I could even take it home. It could be a kids PC or maybe Mrs. EVBlog might like it. We'll see. So there you have it. That is a very nice Lenovo all-in-one touchscreeny PC thing and doesn't seem to be anything wrong with it at all.

**Dave Jones:** It was just dumped. They upgraded or whatever. It's couple of years old and yes, I really do find this stuff in the dumpster. I have to keep saying this because my building is in like a big industrial estate complex and it serves like a hundred the one dumpster room serves like you know, 80 or 100 different companies or whatever and and people just like toss this sort

**Dave Jones:** of stuff out cuz it's surplus to requirements. They got some new shiny wizbang thing and they like they couldn't even be bothered selling on eBay. Yes, you would have easily got many hundreds of dollars for this on eBay, but they just couldn't be bothered.

**Dave Jones:** It's not worth their time. So they tossed it out and well, that's a score for me. So that's that's one of the best dumpster scores I've gotten in terms of PCs.

**Dave Jones:** It's no big beast, but yeah, like the fact that it's in a brilliant case. It's touchscreen. Shame it's got a bit of a fan in it little bit of fan wear and so it's not completely silent, but at the moment actually I'm barely able to hear that at the moment.

**Dave Jones:** So in a way that is a huge score. Very happy with that. Don't know what I'm going to use it for. I mean I could sell it on eBay, I guess.

**Dave Jones:** I don't know. No, it's it's it's too good. I really like it. It's very sexy. So I'll keep that for something. So anyway, if you like that video, please give it a big thumbs up and as always you can discuss in the comments down below and please subscribe to me over on library.tv.

**Dave Jones:** That's It's the word library. It's l b r y dot t v. Always linked in down below. Got like 4,400 subscribers. I'm like the ninth biggest channel in the world.

**Dave Jones:** Woo! Wait, adding a new feature to Windows. This could take a few minutes. Oh, it's updating bloody Windows. Anyway, catch you next time.
