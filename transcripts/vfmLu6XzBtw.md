---
video_id: vfmLu6XzBtw
title: EEVblog #841 - Microchip MPLAB X PICkit 3 Woes
url: https://www.youtube.com/watch?v=vfmLu6XzBtw
source: youtube-asr
timestamps: {"0": 1, "1": 17, "2": 29, "3": 45, "4": 60, "5": 72, "6": 88, "7": 103, "8": 117, "9": 132, "10": 147, "11": 160, "12": 176, "13": 191, "14": 210, "15": 223, "16": 237, "17": 252, "18": 264, "19": 278, "20": 290, "21": 304, "22": 321, "23": 335, "24": 349, "25": 363, "26": 377, "27": 393, "28": 409, "29": 421, "30": 434, "31": 446, "32": 462, "33": 480, "34": 497, "35": 509, "36": 523, "37": 540, "38": 557, "39": 569, "40": 583, "41": 598, "42": 614, "43": 629, "44": 642, "45": 656, "46": 667, "47": 681, "48": 697, "49": 716, "50": 732, "51": 746, "52": 761, "53": 774, "54": 790, "55": 804, "56": 819, "57": 835, "58": 850, "59": 865, "60": 883, "61": 894, "62": 912, "63": 925, "64": 941, "65": 949, "66": 960, "67": 975, "68": 992, "69": 1007, "70": 1021, "71": 1044, "72": 1059, "73": 1074, "74": 1085, "75": 1100, "76": 1123, "77": 1140, "78": 1158, "79": 1171, "80": 1185, "81": 1199, "82": 1219, "83": 1235, "84": 1251, "85": 1268, "86": 1286, "87": 1302, "88": 1316, "89": 1329, "90": 1340, "91": 1353, "92": 1373, "93": 1397, "94": 1408, "95": 1429, "96": 1441, "97": 1463, "98": 1476, "99": 1485, "100": 1498, "101": 1518, "102": 1534, "103": 1549, "104": 1571, "105": 1584, "106": 1598, "107": 1610, "108": 1631, "109": 1644, "110": 1661, "111": 1675, "112": 1697, "113": 1710, "114": 1729, "115": 1746, "116": 1762, "117": 1778, "118": 1788, "119": 1802, "120": 1816, "121": 1826, "122": 1842, "123": 1860, "124": 1882, "125": 1896, "126": 1910, "127": 1924, "128": 1940, "129": 1956, "130": 1968, "131": 1982, "132": 1998, "133": 2015, "134": 2028, "135": 2041, "136": 2051, "137": 2067, "138": 2083, "139": 2097, "140": 2119, "141": 2135, "142": 2150, "143": 2166, "144": 2180, "145": 2196, "146": 2215, "147": 2230, "148": 2246, "149": 2262, "150": 2275, "151": 2287, "152": 2305, "153": 2327, "154": 2347, "155": 2364, "156": 2380, "157": 2400, "158": 2412, "159": 2426, "160": 2442, "161": 2459, "162": 2475}
---

**Dave Jones:** Hi, just a little impromptu rant video because I'm trying to get this uh Microchip PICkit 3 actually working. I've got a new product that has a PIC24F in it. And I thought, yeah, no worries, I've got the PICkit 3, it's always

**Dave Jones:** worked for me, you know, I'll be able to program the damn thing. Wha! Big mistake. Anyway, I just wanted to uh show you this. Yes, I'm shooting this with my uh webcam cuz I'm going to going to do some uh screen capture and

**Dave Jones:** stuff like that here. So, let me uh just take you through the problem I'm actually having with this thing and the new MPLAB X uh software. So, I'll switch over to the uh desktop here, and I'm still in the bottom corner. Hello. Um by

**Dave Jones:** the way, if anyone wants to know, I'm using XSplit to uh actually record this. So, I've got my Microchip PICkit 3. Okay, let's plug it in. And um I have I've not used um the new MPLAB X, or new, it's

**Dave Jones:** it's been out for a couple of years now, but it's been a couple of years since I've done a PIC uh project. So, I've used MPLAB before that, and I also used the standalone uh software to actually uh program this

**Dave Jones:** thing as well. Um and I've, you know, I really haven't had too many issues with it. It's just kind of worked, but MPLAB X does not work uh with the thing. Now, MPLAB X, I've actually installed um it was like a 500 meg download or

**Dave Jones:** something, and rant number one, you don't get anything with it. It's just like the IDE, right? So, for a 500 meg download, it's ridiculous. So, um you don't get the compilers, you don't get any extra configuration stuff. It gives after you

**Dave Jones:** finish installing, it gives you a bunch of uh options to go to the website and download all these additional stuff. Well, bloody hell, why can't you include it anyway? What it's got now, they've they still have this standalone uh

**Dave Jones:** programming software, but it's now called the MPLAB IPE and integrated programming environment. So, here's the icon for it. I'll load it up. And it's you know, it's really quite good. It's better than the old one. It's more comprehensive. So, I've plugged in

**Dave Jones:** my PICkit 3 and you might have seen down in the bottom corner that it actually recognized it and check it out. It recognizes my PICkit 3. Okay, there's the serial number. No problems whatsoever. If I If I disconnect my

**Dave Jones:** PICkit 3, it should vanish. Yep. Okay, I'll plug it back in. So, all the drivers, everything seems to be working just fine. Uh and you know, I can choose like 24F. I can choose the device. I won't choose

**Dave Jones:** the exact device I've got cuz it doesn't matter cuz my problem um extends to the fact that it doesn't The IPE does not talk to my PICkit 3 even though it recognizes the damn thing. Now, I believe this connect button here is

**Dave Jones:** supposed to connect to the MP to the PICkit 3. And if we do that, we'll find that it just sits there and spins its wheels, does nothing, and it'll eventually come up and say cannot connect to the damn thing. Why? It's

**Dave Jones:** bloody ridiculous. Ah, unbelievable. Anyway, there it is. Connection failed. Okay, unbelievable. And I can actually and it's got the advanced mode here. Normally, it by default it puts you in simple mode. So, if we go in uh the default password is Microchip.

**Dave Jones:** Yeah, thanks for that. It's I can understand why they're doing this because it's designed to Let's remember that password. Um that's Oh, change password. No, I don't want that. Log on. Um because they put these passwords in cuz this integrated programming

**Dave Jones:** environment designed to be used for uh in a production type environment. So, you know, when you've got production workers, you don't want them going in and around with all these advanced settings. You'll notice down the side here, we've now got

**Dave Jones:** uh all of these um uh you know, settings. So, we can go in and change all sorts of things. Production mode, look at all these options, and environment settings, memory settings, aha, external power, everything, right? So, you don't want production operators

**Dave Jones:** around with this uh sort of stuff generally. You want to limit them to uh you know, what they're particularly doing. But, yeah, in my experience, I have extensive experience in the production environment, and they always find out the passwords. So, it

**Dave Jones:** doesn't matter anyway, but yeah. Um so, right. It recognizes my PICkit 3. Drivers are obviously working. It will not connect. If I go in and say manual download and so I thought, "Oh, okay. It needs to update the firmware." Even

**Dave Jones:** though I've got auto I had auto download firmware actually ticked. Okay, so it didn't recognize that my firmware was out of date. I thought, "Okay, haven't used this thing for a couple of years. Download new firmware. Sure, fine." you

**Dave Jones:** know? No problems. I expected that. Um but even when I manually go to manual download firmware, please wait while it Oh, here we uh yeah, please wait while it locates the file. Here it is, PICkit 3 firmware. jam

**Dave Jones:** file, whatever the hell that is. Anyway, it's uh going to spin its wheels again, and you'll find that it simply cannot connect to this PICkit 3. Why? Why the hell does my old PICkit 3, it's still the same PICkit 3. I believe the hardware

**Dave Jones:** hasn't changed, right? But, why can't it just detect that, you know, the firmware is old and upgrade new firmware and work. There it is, connection failed. So, and yes, I've tried to plug it in to my target device, and of course, it

**Dave Jones:** won't talk regardless of if I select it, because it's not even talking to the PICkit 3. So, I actually um you know, I searched around, went on the uh you know, went on the interwebs and looked at various forums and you know, other

**Dave Jones:** people have been having similar sorts of problems. There's talk about problems with Windows 8 and Windows 10 and stuff like that, but I'm not I'm using Windows 7. Right? So, anyway, I asked on the EEVblog forum. So, thank you for

**Dave Jones:** everyone who actually replied. EEVblog forum is the best place to ask. Like, I had a response within you know, minutes. There's There's so many people How many people are active at the moment? I mean, just as I'm recording this. Here we go.

**Dave Jones:** There's 963 guests and 215 users on online at the moment. Just you know, ready to chat and answer questions. And these are the active users in the last 60 minutes. It's just It's just crazy. So, hi to everyone on

**Dave Jones:** the EEVblog forum. Um So, I asked in here, you know, I'm getting this issue and some people are saying, "Yeah, apparently this is like you know, it's an unreliable as hell this thing. It's just you know, horrible apparently." So,

**Dave Jones:** yeah, thank you very much Microchip. Trying to use your bloody parts and PICKit 3 doesn't work. And a lot of people are saying, "Don't even bother using the PICKit 3. Just get the ICD 3. It's much better." Well, that doesn't

**Dave Jones:** bloody help me. That's couple hundred bucks and I don't have it. Um So, you know, I thought be able to use my PICKit 3. No worries. But, um now they're talking about some people Sorry, I won't go into detail here, but

**Dave Jones:** they're talking about you know, I may have to load in the old version of MPLAB cuz there's new MPLAB X, which is like they've changed you know, the whole look and feel of the thing. I'm not sure about the underlying

**Dave Jones:** code and everything, but they've changed a lot of stuff in MPLAB X. So, there's pretty much the old MPLAB and the new MPLAB X. And apparently, if you do that, then maybe I can actually download the firmware file for this. It doesn't

**Dave Jones:** recognize it. And by the way, I can't even use the PICkit the original PICkit 3 programmer software will not actually talk to this either. Like the old version that they've actually done away with now. It's been replaced by this integrated programming

**Dave Jones:** environment. It, you know, oh, did I rant about the IPE? This integrated programming environment, this is my other rant I wanted to do was that why can't you download this separately? The integrated programming environment, the IPE, some people just want to get their

**Dave Jones:** PICkit 3 and just program a PIC. That's all they want to do. They want to update their product or do whatever. They don't care about MPLAB X. They don't care about the source code. They don't care about compilers. They don't care about

**Dave Jones:** any other crap. They just want to program it. Yet you've got to download the 500 meg as far as I'm aware, the 500 meg MPLAB X just so you can get this little IPE programming software. Bloody hell. Make

**Dave Jones:** it available separately, idiots. Unbelievable. Like, I don't know. Maybe there is a way to download it separately, but I anyway. Oh, yeah. Bloody If there is, then I apologize. But if there's not, then bloody well fix it. So anyway,

**Dave Jones:** so apparently I can try somebody else also mentioned that I could try and use the MPLAB X to download this .jam firmware file manually. And then somebody else was talking about modes or something that this thing can go into

**Dave Jones:** different modes that you have to change using the IPE. But if the IPE or the old programmer software, but if it won't work if it won't talk to it in the first place, then how the hell do you change modes?

**Dave Jones:** It's just crazy. And everyone's saying, "Yeah, yeah, you know, had issues. Yeah, but it's unreliable as hell. There are some conflicts if the firmware and the if the firmware on this and the IPE do not match the auto update will

**Dave Jones:** repeatedly fail. There you go, auto update. That's what I'm failing. So, thank you very much KL27 X. You plug the device in, hit connect, it downloads new firmware, but it's broken. Yeah, like it's absolute horse Yes, thank you

**Dave Jones:** very much. My thoughts exactly KL27X. It isn't explained. It's horse that it isn't explained somewhere easily accessible document or sticky or a fact or anything like that. I know. It's just a complete and utter horse I agree. Um

**Dave Jones:** There is a so so yeah, KL27X seems to know what he's talking about. He can find the yeah, find the pickit3 jar. I know where that is. Um yeah, there we go, firmware. So, I can maybe So, what I'm going to do now

**Dave Jones:** is going to stop this. I've been ranting long enough. I'll have a play around with the MPLAB X see if I can actually People are talking about generating a dummy project file and then loading in the firmware and then trying to download

**Dave Jones:** the firmware to this manually. Um So, yeah, but why there's not an option in in, you know, the IPE to do that? Like update, you know, you saw it, right? I tried to update this thing. It's got a manual download firmware. I

**Dave Jones:** tried to do it. I selected the right file. It does not do it. So, maybe MPLAB X. And what? Have I got a failed pickit3? I don't know. Is it bricked? I don't know. Do I have to crack it open

**Dave Jones:** and somehow connect to some sort of hack into some sort of internal ICSP bus or something like that to unbrick it or whatever? I've got no idea. Anyway, I'll go now, try MPLAB X, and I'll get back to you. I won't bore you with the

**Dave Jones:** details. I'll try and do the firmware manually, but this is you know, I've already wasted like a couple of hours on this trying to freaking get this thing talking. It's ridiculous. Bloody microchip. These stupid tools. Unbelievable. All right,

**Dave Jones:** so here I am in the archives of microchips development tools because yeah, they no longer support the original MPLAB. They only support MPLAB X. So, here we go. MPLAB IDE archives. Uh And I will download Oh, where is it? I

**Dave Jones:** will download I guess I'll download the latest version 8.92. Install that and see if I can get lucky updating the firmware and then maybe the plan is if it updates the firmware in that, then it'll then talk to the newer MPLAB X and

**Dave Jones:** it'll update the firmware for the MPLAB X. That's the plan anyway. By the way, uh I didn't show you the screenshot where I actually you know, it wouldn't even connect. Here it is. It wouldn't even connect with my

**Dave Jones:** previous uh the old PICkit 3 programmer software got some stupid timeout error message or something like that. And somebody asked uh Do-It-Yourself Audio asked if I have tried a separate computer. Yes, I actually set up all these download the

**Dave Jones:** tools again on a completely on a different machine. It was fairly clean machine. And uh no, exactly the same uh problem once again running Windows uh 7. So, anyway, I'll install this, get back. And here's another little rant. I'm

**Dave Jones:** trying to download it. It's failed twice. It's 111 meg download. And for some reason my internet works. So, is it the Microchip bloody website? Now, it's only gotten to 11 meg and it's frozen. It got to like 50 meg or 70 meg

**Dave Jones:** before before it froze. Now, it's 11 meg and it'll eventually come up saying failed network error. Unbelievable. And I did actually go in here and try and create a project in MPLAB X to see if that I could like auto download the

**Dave Jones:** latest Um, firmware just before I do the MPLAB 8, the older one. And of course, um, because as I Did I rant at the beginning? Yes, it didn't come with anything, any compilers. So, when you choose your device, it says, "Yeah,

**Dave Jones:** look, there there's my PICkit 3. It's all there. Everything's hunky-dory." But, no compilers found, so I can't actually continue creating a project, not even a dummy one. I get I guess that's understandable. All right, so I'm not going to rant too much about that. So,

**Dave Jones:** I'm actually downloading the I don't know, the XC16 compiler cuz the 24Fs are a 16-bit chip, so I presume it's the X16, uh, compiler for the damn thing. It's downloading slowly. No, has that one Has that one frozen, too? I have

**Dave Jones:** download I've tried a dozen times to download the MPLAB IDE 8.92, and it keeps failing. Sometimes it gets to 10 meg, sometimes it gets to 70 meg, and it fails like a dozen times. There's nothing else wrong with my internet.

**Dave Jones:** God, I hate technology. Hate the internet. And nope, I tried uh, Firefox as well to download. No, look, it failed. Full install, uh, of the XC16 compiler. No, it got to like 40 meg or something or like 80% of the way there, and what

**Dave Jones:** Murphy'll get you every time. This is what, you know, this sort of will happen when you you know, you got to get this deadline. You got to get your project finished. You got to get your app finished or whatever. And no, it's,

**Dave Jones:** you know, before some trade show demo. No, nothing freaking works for you. Unbelievable. And there's David, too. There he is. Cameo. He's back. He's back for the new year. Finally, um, I'm installing the compiler, but only because David, too,

**Dave Jones:** actually had happened to have a copy on his, uh, laptop here. So, yeah, cuz I can't download any from bloody Microchip. Unbelievable.

**Dave Jones:** And we're just trying to uh get into the project properties here, trying to find the project properties, and uh David couldn't uh do it either. And well, now he finally figured out it's this little spanner thing here. So, that's changed from the

**Dave Jones:** original MPLAB, hasn't it? I think so. I I I think it's got a it's got like the I think they used to have a project thing up here. Anyway, it's been years since I've used it. Anyway, this tiny

**Dave Jones:** little spanner thing. So, you click on this little spanner thing, and then we get in here, and hopefully, now what do we do? Uh in PICkit 3. Ah, there we go, PICkit 3. And there's a firmware. So, if you go to

**Dave Jones:** the top in option Program options, firmware. Yep. And then Use latest firmware? It's already done. It's already ticked. Yep. So, when you load your program, it should So, I've got to have a dummy program, though. Yeah, probably. All right. Right. Okay. So, I've got to

**Dave Jones:** load in something, and um hello world program. You can do it the other way. Right. So, I can actually download Yeah, like a firmware. Yeah. So, I can Yeah. Okay. All right. We'll get back to you. Here we go. It's trying to connect to the

**Dave Jones:** PICkit 3. No, connection failed. So, yep, doesn't work in MPLAB X. All I did was hit the uh the What is it? The read device thing up here, and just no. Yeah, I think It didn't work. And finally got it, but

**Dave Jones:** uh David had to download it on his Uh notebook, and it downloaded first go. So, go figure. I've tried two different browsers on this, and I can't download anything from uh MPLAB. So, anything from Microchip at all. Uh yeah, it's

**Dave Jones:** standard location, whatever. Okay, yeah, whatever. Yeah, whatever. Yeah, whatever. Next, just install everything. Come on. Go, Silver Sovereign. Unbelievable. I've been sitting here for a couple of minutes, and it's just doing nothing. Absolutely freaking nothing.

**Dave Jones:** All right, finally got it to work. And it would like to install the device driver. I'm presuming yes, I want to install it cuz maybe it's an older driver and it will work with the PICkit 3. So, that's worth doing.

**Dave Jones:** Like it may mean that I can't talk to MPLAB X, but I can uninstall this and reinstall MPLAB X. That's fine. So, I'll I think I'll go install. Or will Murphy get me and I've chosen the wrong option? Anyway,

**Dave Jones:** we'll see. Uh-oh, this doesn't look good. 4 bytes expected, 0 bytes received, failed to properly connect the PICkit 3.

**Dave Jones:** Yeah, target device. Yeah, I might set up and now set up a project and see if it does it, etc. But as it stands, nope, I installed MPLAB 8, which it previously worked with. I think I was using 8.something or other.

**Dave Jones:** And it previously worked and failed to and it just does not connect anymore. So, hell, Microchip tools seriously suck.

**Dave Jones:** Hold on to your hats. We realized that we were using a really old version of the PICkit programming software, like version 1. And but that's what was on the Microchip website. That was their version, but we got version 3.1.

**Dave Jones:** And Google archives. So, we'll install that and uh maybe Bob'll be our uncle. Here we go. We might have it. This is what we're hoping for. Look at this. The PICkit 3 operating system version 2.00 must be updated. You bet

**Dave Jones:** your ass we want to update it. This is the one. Yep, I remember using this one. Version 3, there you go. PICkit 3 operating system must be updated before it can be used, blah blah blah. Download new operating system. You bet your ass.

**Dave Jones:** We've actually got it bare bare board. We were getting desperate. We were going to actually hook up a PICkit 2 to the inserted serial programming port on this thing, which is the wrong pitch. Sorry, my lead's not long enough to show you.

**Dave Jones:** It's the wrong bloody pitch. Uh pin pitch is not 0.1 in. Um bastards. Anyway, uh but apparently the clones you can buy on eBay, you can get like $16 clones or something delivered from Hong Kong. They have the correct pin pitch, apparently.

**Dave Jones:** Okay. Download. Let's see if this works. Oh, come on. Yes, yes, I heard it. Yes, it a rebooty sound. Oh, we might have it. Yes. Come on. Victory dance. Victory dance. It just worked. Victory dance. Do a dance.

**Dave Jones:** I don't dance. Oh, yeah. Engineers don't dance. Woohoo! Yeah, there we go. Ooh, look at that. Big gangly arms there. Bingo, that was it. All we had to do, well, okay, well, no, we still haven't tried it with the uh

**Dave Jones:** MPLAB X and everything else, but um at least we're getting somewhere. We've updated the firmware. Well, it was never going to do them do them. Yeah, no, no, it wouldn't know. completely Sweet. All right. All right, here we go. This I should

**Dave Jones:** have remembered this. I remember Now I remember using PICkit version 3. PICkit 3 programmer software version 3. And um yeah, anyway, I've now got it hooked up. So, I've now got it done a long I'll show you the pin pitch by the way.

**Dave Jones:** There's the stupid Where is it? Yeah, there it is. Check it out. stupid pin pitch. Look at that. It's not 0.1 inch. That's the internal in-circuit programming header. So, I'm going to plug this into my product. My super secret product.

**Dave Jones:** I can't tell you about. That uses a PIC24F VDD on PICkit 3. So, we'll turn it on. And then we can um try and uh it should detect a device if I remember rightly. Here we go. So, let's just choose the

**Dave Jones:** PIC24. Can I just do a read? No. No, okay. Now I'm just bumming around trying to use this thing. Haven't used it for years. Used to use it all the time. It's amazing how you forget things, you know?

**Dave Jones:** If you don't use them for a while. I mean, you know, it's a couple of years. Used to use it extensively to develop for and program all my micro watches and stuff. Uh anyway, I'll get back to you. Uh no

**Dave Jones:** device detected. So, yeah, I'll find a board that that could be the product. I haven't tried to connect to it before. So, um yeah, we'll try and find something to connect to and then we'll try it on MPLAB X. This is going What

**Dave Jones:** have we been going for at least half an hour now in recorded footage, but we've like spent all day on this. Seriously, stupid. I can't shut down the bloody software.

**Dave Jones:** Ah. And David 2 can't do it either. Why? Unbelievable. All right, here we go. I'm back in the MPLAB X IPE. All these terms are confusing. Anyway, it's just detected the PICkit 3. Let's see if it can connect.

**Dave Jones:** Uh Uh No. Looks like we got the same No. Looks like we've upgraded back to the software. No. That doesn't work. Connection failed. Great. What? The target circuit may require more power, blah, blah, blah. Yep, but but did it update?

**Dave Jones:** Could not be restarted. No, I don't think it updated. If it updated the firmware, it would have gone do do do do do with the USB connect thing again, probably. So, no, I don't think anything magic happened there.

**Dave Jones:** Okay, back to MPLAB X. Uh sorry, MPLAB 8. Uh this is just so bad. No, even MPLAB 8 can't connect to it. Download PICkit operating system. SURE. OH, OH, OH. OH, WE FORGOT TO DO THAT. OH. DUMB. OH, I wish we had that all

**Dave Jones:** Oh, no, we're we're we're still recording. We're still recording. Hang on. Hold on to your hats. We forgot about one thing. This mode. You remember we told you about the mode at the start? How this thing had different modes. Here

**Dave Jones:** we go. Look at this. Revert to MPLAB mode. Here we go. Clicking okay will program the so that it will restart into bootloader mode. This allows communication with MPLAB software. Oh. Are you me? This mode can alternatively activated by holding down

**Dave Jones:** the PICkit 3 button during USB plugin. I didn't know that. Nobody told us that. We just said what? There you go. You can hold that cuz there's a button on the front of this stupid thing that you can hold it down.

**Dave Jones:** Do you want to hit cancel and try to do that like that? No, no, no. I want it No, I want No, it's telling us it can do it. I want to try and do it. No change is mode to the

**Dave Jones:** program image. It's just a mode, right? So, you hold down the button. If you're having problems connecting, hold down the button. This could be it. This could be the holy grail. Keep Hold it down during USB plugin. And maybe you get some different LEDs

**Dave Jones:** flash or something. Here we go. What is that? There we go. Yep, I heard it reconnect. Yep. Yep. Has been reverted to converted to MPLAB mode. Exiting GUI. Crash. I'm like and the only way to shut it down is

**Dave Jones:** to go into to actually kill it in task manager. This is unbelievable. And and it won't and it'll And you have to do it a couple of times cuz it puts up a fight. All right, so you got to yep.

**Dave Jones:** Wow. Okay, now where do we go from here? MPLAB IPE perhaps. Let's go straight into the new IPE, the integrated programming environment.

**Dave Jones:** And let's see if we can connect. Yes. YES. WOO! YEAH. WE did it. Woo! That's it. Probably after like a day of around with this thing, I reckon all we had to do was probably hold down the button on

**Dave Jones:** this thing to put it it wasn't going put in put in at all before. Oh no, well, yeah, maybe some firmware. Okay. firmware. Yeah, all right. All right, maybe it was old firmware, but so the key I think here

**Dave Jones:** Oh, hang on, failed to download firmware. Connection failed. Hang on, but at least we actually connect to it with the new IPE MPLAB X. So this is a big step. Oh, two target device. Oh, yeah, okay, yes, yes, we

**Dave Jones:** don't Yeah, cuz I don't have a target device hooked up. That's fine. Yeah, no, no, that's that's that's good. I think we're rock I think we're cooking with gas. So the I So the trick was this thing with the whatever firmware was

**Dave Jones:** programmed into here, would only talk to the PICkit 3 programmer software version 3.1. It would not talk and connect to anything else. Okay, I'm going for broke. I've got it hooked up to my new product. And uh yeah, apparently in the JAR file

**Dave Jones:** that we looked at before, it contains all of all these different hex files. The JAM file was apparently like it was just a list of the text list of the those files. So, um the hex files, there was all all different modes. So,

**Dave Jones:** depending on which chip you want to program, it looks like this thing will download programming firmware to your PICkit 3 to then program your target device. So, that's why we're getting this failed to download firmware down here. So,

**Dave Jones:** here we go. I have now selected the correct device. It is plugged Oh, no, hang on. I haven't applied power. So, let's apply um power target circuit from the tool. You bet. All right. So, we're going to apply power

**Dave Jones:** and we are going to connect. Let's see what happens. See what happens. Just got those damn asterisks again. The target circuit may uh we're still getting that error message. Okay, may require more power. Nah. Okay. Well, that could be

**Dave Jones:** That that could be true. So, I don't know if I can actually power the target on here. Um haven't actually tried it. All right, we'll try another board. Try another target. Here's an annoying quirk of this software. Any time time you change the

**Dave Jones:** target device, it resets this power target circuit from tool check box. Ah. Geez, thanks, Microchip. Um yeah, it's a safety measure. Sure it was decided by committee. So, I'm I'm actually trying to connect to a Digilent chip kit. Um

**Dave Jones:** So, hopefully we got the pinouts correct. Cuz it's a bit of a, uh, bit of a mess. There we go. Um, No. No, it doesn't like that. It's downloading the software. We might have success. Can we show that

**Dave Jones:** to the webcam? Yeah. Here we go. It's going to be sure, hang on. I'll go full screen. Go full screen. Sorry, we're using Dave's, what is this? Microsoft Surface? Yeah. Yeah. thing. And it's downloaded. This is MPLAB X.

**Dave Jones:** Yeah? Yeah, MPLAB X. Yeah. And it's downloaded the new firmware. Because it wasn't, there we go. Look, it's doing stuff. YES! OH! IT'S DONE. THAT'S A WIN. Because we think it was in MPLAB mode, which of course wouldn't

**Dave Jones:** work with the IPE or whatever. I can't believe It's reading It's reading the chip. There we go. IT. WOO!

**Dave Jones:** WHAT IS THIS? WE WON. WE ACTUALLY READ IT'S flashing an LED. It's flashing it. Now, we have We have won. We have spoken We have spoken to our them to like it, download it, whatever you want. We have

**Dave Jones:** spoken to our chipkit. And yep. So, we can now read. Yep, I got to read complete. Now we can have a look at what's on there, if you want. Seriously, this has been a solid day's work. It's probably been a day and a

**Dave Jones:** half. Well, we haven't worked on it all day today, have we Dave? We've been around with Yeah. other things. Uh, we we got a new scope. That was exciting. New scope turned up. No, I should be able to do it now. So,

**Dave Jones:** let's disconnect it. Let's Let's go live. Sorry about this super duper long video. Let's plug it in. I'll load up MPLAB MPLAB X IDE. Sorry, I got to switch back to the, uh, screen here. And Can Can we edit the existing one to

**Dave Jones:** change it or is Oh, take take longer just go file new. Yep. File new, microchip embedded, blah blah blah. Yep. 32 And then scroll to That one. Yeah. Sweet. Pickit 3. Pickit Yep. Woo. That'll do. That software will do.

**Dave Jones:** Microchip sucks two. Or just M. Finish. All right. There we go. Okay. So, we're in like Flynn. And now we just read, right? Yeah. We just go read device memory. Connecting the programmer. So, was it just Yep. There we go. There we go. Yeah, cuz

**Dave Jones:** it doesn't it firmware is fine, so it doesn't have download new it download firmware before, right? firmware. Okay. It automatic cuz we had the configuration setting to set to auto download firmware. There you go. So, it works. Ridiculous number of steps to get that

**Dave Jones:** working. I know. Crazy. We spent all day. Both of us had a shot. Um yeah, the all the stuff on the forum helped, but ultimately it didn't do the business until we misleading. Well, no no a few people were right

**Dave Jones:** about the mode that mode setting. That mode setting made a lot of difference, but right. But we had Yeah, yeah. But we had to the key was to download the 3.1 programmer software in order for it to update the

**Dave Jones:** firmware to actually rec talk to it to update the firmware chicken and egg thing. Um and because that's probably last software I used with my Pickit 3 would have been that version 3.1 programming software probably 4 years ago or something.

**Dave Jones:** Yeah. Right? That you know, that would have been the last thing I used and obviously it had the firmware on it and nothing else liked it. So, Woo. So, read complete. Weird. Woo. This is great. This is great. So, now how do I call

**Dave Jones:** Where's my Microchip sucks project up here? Let's go into my Microchip Do I have to load it or am I just in like Flynn? How do I Set as Set as current or something. Yeah, set as current or active pro- Set

**Dave Jones:** as main project. There we go. Boom. Right, 24F. I'll plug it back into my product now, yeah? Can't let you see it. Secret. It's pretty cool though, isn't it, Dave, my new project? Yeah. Yeah, and it's getting cooler as the the

**Dave Jones:** days go by. How how long until it's cooler? Uh no, it's another prototype's due in a couple of week- yeah, another few weeks I'll get another prototype. But there was a big goof with it. Um anyway, I'm uh

**Dave Jones:** developing a product in conjunction with somebody. Um All right, company who shall remain nameless. Anyway, let's uh So, that is that, right? So, it's connected now. All we got to do is um we want to go into the spanner thing.

**Dave Jones:** Right, because we want the PICkit 3, and we do want to apply power. So, we go in the ah power target circuit. It kept that setting. Beauty. Something works in Microchip. All right. X is actually really a lot better.

**Dave Jones:** You are you're you're an MPLAB X fanboy. It's a lot better. It's a lot better. A lot of people complain about MPLAB X. I've only ever heard complaints about it. are horrible. All right, okay. All right. like But once you're used to it, it's

**Dave Jones:** fine. Right. Yeah, okay. So, that's it. So, I've selected that. So, let me try and read.

**Dave Jones:** Oh, yeah, I got to scroll down here. Hang on. Uh-oh. Yeah, it's downloaded new firmware. Oh, for the different Yes, for the different cuz this is a 24F as opposed to a 32F, completely different series. So, the the PICkit I mean, that's just dumb. I

**Dave Jones:** mean, you know, like I actually Now that I recall, I think it has to do this. I vaguely remember because the target device does not match expected device. Would you Oh. Oh. Okay. So, that it gives me some weird hex

**Dave Jones:** code. Would I like to continue? Well, I'm just reading. It's not like I'm programming it. Right? So, let's just go okay. I wouldn't. Why? You wuss? I'm a wuss. You're a wuss. I'm going to read. Come on. All right, here you go. This is

**Dave Jones:** actually a photo of the uh PIC24FJ in my product. Um and it you can see it is exactly the same as what I've got set over here. 24FJ 64GA 310. Right? Yet it's telling us uh would you like to

**Dave Jones:** continue? Well, let's cancel. Let's do it again. So, let's read. Read device memory. Main project. And it says the IDs do not match. Why, Microchip? This is more Microchip funny business. Here we go. Would I like to continue? You bet your ass I want to

**Dave Jones:** continue. And if it ruins the firmware in my product, I'm not going to be a happy camper. Um of course, now that I've supposedly got a working MP I can re-download it, but uh I've only got the source code. I have to

**Dave Jones:** recompile. Read complete. There you go. Yep. Okay. Sweet. So, it it well, it talks. It's talking. Bingo. The uh that's the end of the video, folks. All done and dusted. That took um like a day's I pissed away a day

**Dave Jones:** day and a half trying to get this stupid PICkit 3 working. I mean, that's just disgusting. And everyone on the forum says like similar um things in various other forums. That's a pain in the ass. All these different firmware versions

**Dave Jones:** and and and modes and crap like that. It's just uh it's ridiculous. Yeah, when it works, you have no problem. Like before, I I really have never had um any major problems with uh PIC um things in the past and using um I

**Dave Jones:** developed several projects with uh PICs, many actually, and programmed using the PICkit 3. Or not many, you know, three or four. And no problems whatsoever. But yeah, when I dragged this old PICkit 3 out of the uh out of the junk bin, it um caused no end

**Dave Jones:** of problems. And that was completely non-obvious. That was a lot of around, but we finally got it. So, sorry, that's probably like 45-minute video. And like I was hoping it'd be pretty quick. But no, it wasn't. So, there you have

**Dave Jones:** it. Microchip. Uh man, everything's a dog's breakfast, it really is. All the development stuff for this, it's a mess. So, PICkit 3, I mean and how old is it? 5 years? When did I do my original rant on this thing? Um yeah, it was for like

**Dave Jones:** the video 20 or something. Um it was like five good 5 years ago, and they haven't come up with an update for it. It's ridiculous. And Microchip are are on the verge of buying um Atmel as well. So, all you Atmel fanboys out there,

**Dave Jones:** well, you might be forced to eat some of this uh MPLAB X uh dog food. But yeah, anyway, um it worked in the end. And now that I've got the correct firmware on here, I'm sure it'll give no more problems

**Dave Jones:** whatsoever, and it'll probably work a treat. Um I'll load my source code in, everything will work fine, cuz David too says MPLAB X works fine. He's developed several projects with it. It's fine. It's fine. There you go. He says it's

**Dave Jones:** fine. They should put their link back on THEIR SITE. OH, YES. OH MY GOSH. YES. YEAH, because yeah, like the only software that worked here was version 3.1 of of programmer software, which is not on Microchip's website. Where is it? Where's the

**Dave Jones:** Where's the bloody Here it is. Here's all their archive stuff. Here it is. Down the bottom. Stand-alone program pick Oh, I can't poking to it. There's my cursor. PICkit 3 stand-alone programmer app version 1. OH!

**Dave Jones:** We didn't see it. That's really funny. That's funny. All right. Sorry, Microchip. There it is. PICkit 3 programmer app and scripting tool version 3.1. That's embarrassing, Dave. Scripting tool? And scripting tool. That's why like I didn't like I just went programmer app.

**Dave Jones:** That's what I wanted. Stand-alone programmer app. Okay. Sorry. I apologize, Microchip. Maybe I'll edit that out. I don't know. Uh but yeah, no, it's there. Okay. So, if I used that would have saved Oh, actually, I might have saved most of

**Dave Jones:** today's most of the most of the work today, probably. If we downloaded that, it would have talked to it. Damn it! Yep. Downloaded the I downloaded the stand-alone programmer app when I should have downloaded the programmer app and

**Dave Jones:** scripting tool version 3.1. Wow. Okay. Yep. Fail. Sorry, Microchip. Didn't mean to bag you that much, but yeah, like your stuff is still crap. Actually, we just realized David 2 made exactly the same mistake downloading that stand-alone programmer software as

**Dave Jones:** I did. So, he didn't have any pre-existing thing. I just told him download the stand-alone programmer app and try it on his machine. And he downloaded the wrong one, too. So, you know, and and it was familiar to me. I

**Dave Jones:** didn't even twig because it was it looked like the programmer stand-alone programmer tool I was all familiar with. It wasn't the correct one, but ultimately, this is a failure of MPLAB X and and the older MPLAB as well to

**Dave Jones:** properly recognize, you know, this this firmware having like different modes and firmware and crap that doesn't talk to each other. You've got to have it in some stupid mode and there's no universal, you know, obvious like big, you know, bold text on the on the

**Dave Jones:** website that says you must do this or in the It's just not. Anyway, and many people on the forum ultimately could help in some respects, but ultimately didn't nail it down either. So, that's with the collective nerd power of

**Dave Jones:** some people on my forum as well. So, jeez, what Like unless I didn't follow somebody's instructions precisely, but I tried to, but yeah, it's ultimately MPLAB X is just needs to handle the firmware for this thing better. It's just ridiculous.

**Dave Jones:** Crazy. Catch you next time.
