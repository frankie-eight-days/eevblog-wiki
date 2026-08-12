---
video_id: Qt-lTpa1pJk
title: EEVblog #1281 - Garmin GPS Repair
url: https://www.youtube.com/watch?v=Qt-lTpa1pJk
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 32, "3": 48, "4": 69, "5": 81, "6": 94, "7": 107, "8": 126, "9": 145, "10": 161, "11": 175, "12": 189, "13": 206, "14": 222, "15": 237, "16": 252, "17": 266, "18": 280, "19": 293, "20": 305, "21": 318, "22": 333, "23": 343, "24": 353, "25": 369, "26": 385, "27": 400, "28": 416, "29": 430, "30": 450, "31": 466, "32": 477, "33": 493, "34": 508, "35": 522, "36": 540, "37": 555, "38": 571, "39": 590, "40": 613, "41": 629, "42": 643, "43": 657, "44": 669, "45": 680, "46": 693, "47": 706, "48": 721, "49": 738, "50": 758, "51": 770, "52": 785, "53": 799, "54": 812, "55": 828, "56": 846, "57": 867, "58": 881, "59": 896, "60": 908, "61": 924, "62": 936, "63": 952, "64": 967, "65": 981, "66": 992, "67": 1003, "68": 1017, "69": 1030, "70": 1045, "71": 1056, "72": 1068}
---

**Dave Jones:** Hi, just a quick video. This a Garmin GPS, what model is it for those playing along at home? The nüvi 2597 LMT. There's so many bloody models. Anyway, it is relatively old and this died on our road trip recently. It's

**Dave Jones:** well, it didn't die. It's the problem is is that this loosey-goosey USB connector which is used for charging of course. It does have its own building battery but so once it's charged it lasts you know a day or something but

**Dave Jones:** then it's dead unless you can charge the sucker up again. So I tried multiple leads when I was out on the road and sure enough it seems to be the connector in there and that's probably just right angle PCB mounted and that that feels

**Dave Jones:** really loose tail. Anyway, let's crack this sucker open. We've got four little itty-bitty torxies here and maybe some plastic uh there as self-tappers. Now that threaded threaded insert rubbish straight into plastic. No wackers, got to get the price down. A

**Dave Jones:** few plastic clips around the outside as well. I don't expect that to just come off. Nope. And I thought there might be a screw under the barcode there but no, you get in there and that looks like just

**Dave Jones:** injection molded port for the plastic. And tada! Oh, that's uh nice little compact battery, isn't it? It's not one of those It's got a ton of plastic molding in the case there. That's uh that's really quite nice. I

**Dave Jones:** like it. Um yeah, there's a reasonable size speaker that they can get in there and of course you got the LCD but it's all happening under here and we've got a can. Can we get that up? Of course we

**Dave Jones:** can. There we go. We're in like Flynn. But unpopulated footprint there. Wonder what that one's for? Don't know. Not really fussed what processors are used. Is that one of That's one of those TI um uh application processor jobbies. That's

**Dave Jones:** an upside down MediaTek. So, all the electrons are going to fall out and that would Is that the GPS? And these little spongy things here just ground connections through to the metal back in plate, nice on the LCD.

**Dave Jones:** They do that for compliance reasons and as yeah, external microSD card and not much else. Anyway, we need to get that board out. Tell you what I do like that they use the same screws. That one's under a bit of sticky tape

**Dave Jones:** um as the outer case. That's just, you know, nice touch when you're designing something, you know, to use all the one type of screw, reduces your bill of materials. Uh you know, number of items on there that you can potentially uh

**Dave Jones:** screw up or or not find or whatever. And like assembly, you don't have to change tools and disassembly and repair, you don't have to change tools. It's a win-win-win. And there's our patch antenna. We've got more goodness on the

**Dave Jones:** bottom. Let's crack that open. Ta-da! There we go. So, we've got our memory. Yeah, more memory. Not too fussed about the details. But what what we're interested in that socket. And let's give it a bit of a wiggle, wiggle, wiggle, yeah, shall

**Dave Jones:** we? And Oh, yeah. Look, there you go, all the data pins. Wow, all the data pins have come up. All of them. That's actually good. I can just reuse that. I should just be able to resolder that. But oh, it might No, have the pads

**Dave Jones:** lifted? I need to get closer. Look at that. Wow, every one of those joints is broken. Every one of them, which is quite unusual cuz solder a lot of people think um solder is, you know, not supposed to

**Dave Jones:** be used as a mechanical strain relief, but that's its two main purposes. It's uh electrical connection, of course, and then uh mechanical rigidity of the component to the board joining it. And well, look, all of them are cracked. So, yeah,

**Dave Jones:** bloody lead-free rubbish, is it? Um but yeah, wow, there you go. But that's actually really good. It means that the connector is not damaged. Um get you know, cuz I don't carry one of these in stock, let alone one with that actual uh

**Dave Jones:** you know, right-angle surface-mount footprint. Might be able to rustle up one that's a standard right angle, but not a sorry, a vertical uh one like this. But there you go. So, that's actually a good thing. Um it looks like the ground pad over here has

**Dave Jones:** lifted, though. But that's no big deal. Still got the other ground pad connection over there, and that's not the end of the world. Even if both of those were broken, or even if you needed to, um you could fix

**Dave Jones:** that. But yeah, I reckon I just uh solder wick all that off and just put on some fresh solder, and uh Bob's your uncle. All right, let's check this sucker out under the Teegano here. You can see that, wow, that's really

**Dave Jones:** remarkable, isn't it? And this GPS is like uh quite old. It's been there for many years. Just, you know, the vibration and the stretching um the uh stress from the leads and stuff like that has just really caused that to

**Dave Jones:** completely come agatha. I don't know what those little um you know, dendritey type things there. I'm not sure what the deal deal is there, but anyway, I've got to hold this thing up at an angle, otherwise the damn thing focuses on the

**Dave Jones:** uh top of the top of the connector. Just clean it up first. You know, you could argue you just take off the whole thing first, and then clean up the pads. Maybe I'll do that. Should just lift out. It's

**Dave Jones:** got a cutout in the board. And then uh once that's done, then you can get in there, clean up the pads, and flip the flip the connector over, and get on the bottom side of the pins um cuz it's

**Dave Jones:** quite hard that inductor's in the way. Little pain in the ass there. There we go. Now it's all in focus. It's one of those depth of field things. See if we can heat this sucker up. And remove that.

**Dave Jones:** Yep, no wackers. Oh, pad came off. Look at that. Oh, no. Sorry, I thought that was a pad. Uh it's it's not. Um it's just a gap between the other one. Pad over here, that one's come completely off. But no wackers to that. No, it's

**Dave Jones:** not. Oh, yeah. Yeah, it's connected. Yep, there's some vias there. And the one on the other side there, that's connected, too. This ground plane here with this cap and over to the inductor here. So, whether or not we need that,

**Dave Jones:** see where she's going. So, it's these two here. So, yeah, it's going into there. So, yeah, we might have to uh uh reattach that. I wouldn't like to think that we can get away with that. We might. Anyway, we can put a little mod

**Dave Jones:** wire on there. But uh now we can get into our little connector. See the copper pads pulled off there? Nothing you can do about that. That wasn't me. And there's some coppery goodness also peeled off on that side again. Once

**Dave Jones:** again, that wasn't me. That's all the flexing over the years. So, good way to do this is just to maybe put some freshy stuff on there like that. And then potentially wick that off. There we go. Get rid of that other crap, too. Now we

**Dave Jones:** get our nice little cleaned up connector that we can reuse there. Beauty. Because I you know, I buy a one like that. I You probably can. Um it's probably an off-the-shelf uh vertical mini B, but anyway, and I'll clean up pads on here. Bloody

**Dave Jones:** speaker wires, they're soldered on. So, that makes it uh really rather annoying. I got to like flip it over like that before we can work on it. Now, here's where you want to uh drop your temperature down a bit.

**Dave Jones:** So, I've just dropped it down to 330 from 370, so we don't want to lift any more pads. And I'll apply some fresh stuff there. And then we'll just wick it off. And you really don't want to scrape the

**Dave Jones:** wick because that can lift your pads, too. So, here you go. And I forgot the ground plane. Nicely cleaned up. Sorry for the overexposure there. Too much light. Can never have too much light. Might have noticed I'm changing

**Dave Jones:** my glasses here. I've actually got a special higher magnification uh pair, which um it allows it's better for working like this. I just thought I'd swap. But, it's fine. See it. See it before. Can see it without. No

**Dave Jones:** problems, but, you know, it's better for uh more better. Put that puppy back in there like that. And you're ready to solder that sucker. Inductor's really quite annoying. Sometimes you get ones in the way like that. I use my .38 mm

**Dave Jones:** stuff here. Yes, I'm using the lead-free rubbish. I keep forgetting the instructions for the Takano remote control thing. I'm going to have to like print out the and leave it. You can do some stuff with it. It's not um it's not the best user

**Dave Jones:** interface, let me tell you. Get one of the grounds grounds in place first. There we go. I'll hold it there. Yeah, this is uh I might have to change my tip here. So, I just pull it out while it's hot.

**Dave Jones:** Got my silicone mat. No wackers. For those curious, I'm using my Pace uh ADS 200 here. Here we go. Going to a smaller chisel. Inductor is annoying little turd there. I just freshly tinned my tip there. It's always important to keep your tip

**Dave Jones:** clean. You're rather annoying. Yeah, I got to get all the way from the other side there. But yeah. Ah. Too much solder. Nice. Other side. Here we go. Looks a bit ugly. Flux residue on there, but uh there you go. That looks like a bought

**Dave Jones:** one down in there. This turd, ah, how can we do that? Get a mod wire over the other side of the board cuz um there's or just scrape it right scrape those vias there. My bloody scalpel's gone walkabout. Wow.

**Dave Jones:** That's really hard to do. Could of course remove the inductor. Clean little vias. I think it's going to be easier just to scrape this top pad here off. It's a bit how you doing? And I'll just run a mod wire. There's

**Dave Jones:** actually room down there to run a mod wire if you had to. I could actually go from the top of the frame there over to there. That's doable. I'm actually using the mod wire to prop my little webcam up here. That's

**Dave Jones:** annoying. I could solder just a short length onto that. The problem with that is is that the heat just conducts straight down uh the wire and it's just going to heat up both pads and it's just going to like

**Dave Jones:** fall off. It'd be really annoying. So, what I'm going to do is actually uh just make a short little jumper wire. Even if you have to fold it back on itself, it's just going to make the soldering easy.

**Dave Jones:** Just going to put a bit of flux in there. Here we go. That pad looks like it's taken. Here we go. Good enough for Australia. So, that does look uh like long and uh boggy there, but yeah, trust me that was easier than

**Dave Jones:** trying to like bodgy in a tiny little wire across there like that. It it the whole thing it just heat up and it it just fall off. Nice colors in that. All right, so that's all back in. Close the

**Dave Jones:** case. Let's see what's what. And of course I'll have to check that it communicates with does the serial comms. But because that's how you update the maps and then the power up. Oh, I have a problem. I think there

**Dave Jones:** might be a short in there actually cuz this connector was heating up. Oh, wow, did I completely screw that? There could be people screaming at me. Those two vertical ones is it the horizontal ones like that at the END OF

**Dave Jones:** AH NO, I'VE CHOSEN the wrong pads. Oh, dumb ass Dave. Too busy. Worrying about the shoot, that's power. OH THOSE TWO THERE. IDIOT. It's like just the orientation. I just saw the two pads right next to each other. Two little

**Dave Jones:** vias right next to each other and oh. So, yes, I looked at the other side and it goes to the inductor. It's the power. I don't even have to measure that. So, yeah. Dumb ass Dave. That's what happens when

**Dave Jones:** you don't engage engage your brain. So, I'm debating whether or not we'd even need to put that back at all actually. I'll just flip the board back out. Okay, that's our wonky one. It is No, it goes down

**Dave Jones:** through those two vias and there's nothing down there. I don't think there's a trace that goes under the inductor. And of course this one's this one's connected over here and then the vias go everywhere else and everything's hunky-dory. Yeah, check it out. Look at

**Dave Jones:** those vias don't go anywhere. They're just vias next to the pad. This thing's fine. I don't think it needs any wire there at all. I was mistaken I I mixed up the other two vias and thought that it actually went

**Dave Jones:** somewhere when it didn't. I get some light under there. Yeah, it doesn't seem to be going anywhere. There's two vias there. Seem to be flapping around in the breeze. There you go. Once again, you get light behind that. Nope. They're going

**Dave Jones:** nowhere. Don't see any other shorts in there. Yeah, I need to clean this thing up. It's a bit messy, but those pads don't go anywhere. Something weird happening here. It's just sort of like rebooting. It's very strange. It's not supposed to do that.

**Dave Jones:** Mhm. No. Oh, flicker flicker. No, something's going on. You are not going to believe this. I am copping Murphy today. Wow, unbelievable. All that sort of like weird resetting stuff and like glitching on display and all that was caused by not anything I

**Dave Jones:** did, a bloody dodgy little mini B. Look at that piss ant little cable on that. Unbranded, not marked, not rated, not anything. And ah, toss that straight in the bin. That was just dodgy as. So, that was like

**Dave Jones:** causing voltage drop and the processor just wasn't getting enough and it was resetting and hiccuping and doing whatnot. And like I replaced the cable and I just tested it on the PC and it's fine. It connects. It So, everything's winner winner chicken

**Dave Jones:** dinner. I could have really chased a red herring down a rabbit hole there all because of a bloody USB cable. You know, you would think that that was something that I just did. Like so, I could have gone down I could have spent ages on

**Dave Jones:** that, but no, it was the bloody cable. Like I knew I visually inspected it. Everything looks fine. This sucker should work. And sure enough, I did actually suspect the cable and that was it. Unbelievable. So, you can you can really

**Dave Jones:** come a gusset there very easily thinking It's not the first time it's happened. God, if I had a dollar for every time it's happened, probably Murphy's got me like that where I've like done something, you know, I'm repairing

**Dave Jones:** something, designing, building, troubleshooting, testing, doing whatever. It turns out to be nothing that I did, but, you know, some other equipment, a cable, a connection, or something like that. Um no, won't get any satellites in here. So, GPS simulator is turned on. Awesome.

**Dave Jones:** Um so, there you go. That works fine. It's now charging up. It's talking. It's communicating. It's doing whatever. Yeah, I could probably like put some epoxy in there. I might actually do that maybe. Put some epoxy on that connector just to

**Dave Jones:** really put it in place because, yeah, it's it's not the best design really that USB connector. It is relying on those pads, and they really can be quite solid, but as you saw, one of them was barely connected to nothing. Just had

**Dave Jones:** some vias there, went through to the other side. No, you know, but when they're actually connected to large pads spread out over the board, and you got lots of pads, then, you know, they can be really structurally sound, but you

**Dave Jones:** know, vibration, it's in the car, of course, and it's vibrating. It's over the years, and it's going to get a lot of stress. You plug it in, plug it out, move your GPS around cuz this wasn't like permanently mounted. It was kind of

**Dave Jones:** like It's just like down in the center console kind of thing, bit flapping around in the breeze. And yes, I get a lot got a lot of stress that connector, but anyway, that's fixed. So, there you go. Oh, man, I

**Dave Jones:** and I'm not going to edit out that goof I've me doing that cuz hopefully you'll learn something from that. That it's easy to make a goof like that when you just assume. You know, assumptions are the mother of all screw-ups, and

**Dave Jones:** well, that just, yeah, happened there. I shorted out the the power. So, the connector got hot. It's a good my uh USB uh pack, you know, it handled that the fine. It must have a uh resettable uh poly switch in there.

**Dave Jones:** Anyway, I think it continued to dump the power in, actually, cuz that you know, the cable got quite hot. It's not like it just uh you know, stopped. Guess that happened, but noticed it pretty quick and uh no

**Dave Jones:** damage done and that's a repaired GPS. So, anyway, if you like that and if you like my screw up, please give it a big thumbs up and as always discuss uh down below and the EEVblog forum and EEVblog.tv

**Dave Jones:** domain, which now links to my Library channel. So, check that out and subscribe. Trying to hit 5,000. Maybe I can do it by this video. Catch you next time.
