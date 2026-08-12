---
video_id: 6rn3p4YlNB4
title: EEVblog #1151 - Dumpster Dive Yamaha Receiver
url: https://www.youtube.com/watch?v=6rn3p4YlNB4
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 40, "3": 62, "4": 100, "5": 125, "6": 145, "7": 182, "8": 210, "9": 233, "10": 259, "11": 297, "12": 333, "13": 349, "14": 373, "15": 403, "16": 438, "17": 467, "18": 500, "19": 523, "20": 535, "21": 552, "22": 582, "23": 616, "24": 637, "25": 666, "26": 687, "27": 709, "28": 730, "29": 765, "30": 787}
---

**Dave Jones:** Hi, I'm in the dumpster room again. Um, somebody's been uh moving in. They got a bunch of stuff. Oh, is there a There's a microwave behind there. Throwing out some old stuff. Anyway, some carpet's gone. Someone's uh Someone's renovating.

**Dave Jones:** Or doing something. Anyway, what's What on earth is that? They got a a dice seat cube thing and some Oh, it's a rolly backpack. Okay. No worries, but here this. There's something down there. That looks like maybe some sort of big uh you know, AV receiver amp kind of, you know, surround thingo.

**Dave Jones:** I'll fish that out. Well, hello. Um, this is like a This is a Yamaha. It's got uh HDMI, Bluetooth, Wi-Fi, Pandora music streaming. Seven channel amp. I don't know how recent it is, but uh Jeez. I mean, I can't It's There's your Wi-Fi antenna.

**Dave Jones:** Unbelievable. What model is it? No idea. But, wow. Um That's fantastic. Take it back to the lab. Power it up. Crack it open. Well, this isn't too shabby at all. It's a Yamaha RX-V579. It's a pretty recent model. It does, you know, Spotify, Pandora. It's got Wi-Fi, Bluetooth, 4K uh HDMI switching, uh seven channel amp. It works with Alexa, apparently. And it's a It's like you can still kind of sort of buy it. It's probably might be officially uh discontinued or whatever, but that's pretty schmick for finding in the

**Dave Jones:** dumpster. And the back's got all the requisite stuff. We got a HDMI out and six HDMI ins. Network got all the old school uh stuff. Of course, you got all your uh binding post speaker terminals, wireless, and woohoo. So, uh yeah, forgive me. I won't tear it down. I want to see if it works. First of all, let's power it up. All right, let's see if the magic smoke escapes.

**Dave Jones:** Didn't hear a bang. So, yeah, we're going to standby LED. Josh, you might not be able to see that. Hey, main on. HDMI 2, so the processor's working. I hear all the relays clicking. And we've got HDMI input.

**Dave Jones:** DVR, AUX, Bluetooth, net net radio, network radio. USB, we can play from the USB stick, presumably. Unfortunately, no, I don't have the remote for this. Um yes, I did look in the dumpster. I always look in the dumpster. Pro dumpster diving tip, always look for the remote controls and other uh accessories and stuff like that, uh cuz people usually chuck those out as well, but on first pass, that is at least booting and doing stuff. Clicking relays. Winner winner chicken dinner. Check it out, I got uh

**Dave Jones:** direct straight through to the AUX. And uh that works. A treat. Beauty. But uh couldn't get the uh tuner working. I plugged a um like a just a wire into the back, but I am in the lab here, so maybe we don't get uh uh radio reception too great, but anyway, the output power amp is working at least on those two channels.

**Dave Jones:** Fantastic. And the HDMI switching works as well. Um it's they've just renamed it uh DVR 550H. That's obviously what they were using before. Got the computer generating that, and it's outputting. So, uh yeah, just an old PC. Don't Don't have a ready HDMI source on my bench. I tried my Rigol 7000 scope, but it didn't output anything. I don't know.

**Dave Jones:** So, at the moment, we have sound and at least on two channels and HDMI switching as well. So, it looks like it's a winner winner chicken dinner so far. At least it's useful even if there is some other fault with it. So, let's have a look inside this thing. I have found a Yamaha before in the dumpster. It was quite a few years ago now. I did a repair video on that, I'm sure. So, I'll link that in cuz that board down there is kind of

**Dave Jones:** familiar. I'm not sure if it's the same one that was in the previous repair that I did, but anyway, it does seem overly familiar. Nippon Chemicon caps, fantastic, you know, like top quality, so terrific. What else have we got? The main processor board, of course. You'll notice that, of course, because this is, you know, dense modern logic, everything else, it's multi-layer board. Well, is it four Is it two? Have they squeezed it all on two layers there? Not sure. Anyway, multi-layer board, yeah, yeah, that would be a multi-layer board. They've

**Dave Jones:** got all the differential pair traces and everything else. You wouldn't be able to just get the ground on the bottom. So, yeah, that one's your, you know, your traditional modern board, and then everything else is just your regular, like, you know, almost not phenolic base, but certainly not the same quality FR4 price. They've really got down These are all single-sided boards with the link. Here's the power amp. All the caps looking good. Nick uh they're Nichicon caps, so no worries whatsoever. So, they're all single-sided.

**Dave Jones:** So, was that just a couple of channels? That's obviously just a couple of channels there. So, and of course, the main board, huge board down the bottom, is also single-sided, and And course, the power supply is single-sided. that's a common uh place to save cost.

**Dave Jones:** Transformer looks great and there's a front panel PCB. Got another double-sided job. So, you're more traditional, got a couple of boards on the front panel, stuff like that. Everything looks fine. I'm not seeing any uh signs of distress or uh any bulging or leaking caps or anything like that. Even though they are good quality, it can still happen.

**Dave Jones:** Um So, we need to get some of the big power caps down the bottom. We have to go in and have a look at those, but anyway, there's all your uh TI Cinema DSP. That does your your DTS and uh everything else, whatnot. There it is, better look at the uh code. You got it to read the code on these chips, you often got the get the light at the right angle, stuff like that. Looks like we got our uh that's our Wi-Fi receiver there.

**Dave Jones:** Silicon Image. Uh I'm not sure that's like a Yeah, that's our HDMI uh receiver and switcher. So, anyway, that all looks good. And I really like how they've got these uh interconnection boards taking it down the bottom. There's some sort of like There's a double-sided load on that. In fact, these are single-sided boards with uh double-sided surface mount on the uh well, surface mount on the bottom, but they are actually single-sided interconnect boards that go from the big processor board down to the uh main board down the bottom there. Couple of

**Dave Jones:** nice-looking 3-W power resistors there. I like those. And then we've just got like interconnection boards and uh stuff like that. That That looks like it does absolutely nothing, but just interconnects wiring harnesses and things like that. So, they would have They would have a reason for that. Yep, I check on the back. There's no parts, no wall. They got some option links there. So, that looks like it's just a like a selection board or uh something like that maybe for different models or whatnot. I'm sure they got their reasons

**Dave Jones:** for it. And this board here is fascinating. Look, it's basically they got a white that big black wire snaking around there. That that just looks like it's just used to wrap up those cables. Um it's soldered on the back here, but there seems to be no other purpose for that. It's got a like a sock 23. Oh, no, no, it's got a little RF connector footprint on the back, which is weird. But yeah, I'm why they've gone to that sort of trouble just to keep those Once again, it could be like

**Dave Jones:** different models and it like you don't know the design of the different models and what their requirements are, but anyway, yeah, it's very nicely designed and assembled and there's no dust or anything else in here. It's clean as a whistle. Beautiful.

**Dave Jones:** And they've done that cable wrapping here, too. You can see that wire soldered on the back of the board. It just wraps around holding all that in place, and they've also done it over here as well in a couple of places.

**Dave Jones:** Neat. And other attention to detail, look at this. They've the Wi-Fi antenna cable here, look, they've cable tied it in there, which is nice, but look, they've added a little roll of foam in there just to like protect the the the wire.

**Dave Jones:** That's nice. For those curious to see the power transistors down there, none of this integrated circuit rubbish. They got discrete down there for all the channels. Everything looks in great nick, and I can't fault this thing at all. Interestingly, they're they're sort of like on an angle. That heat sink is like on an angle, which is really kind of funky. I like it. And those main power filter caps down in there, there's two of them. They look in great condition.

**Dave Jones:** They're actually Yamaha branded. Probably, you know, re-badge Nippon Chemicon or, you know, Yamaha I don't believe they make capacitors, but audio full audio wankery grade electrolytic main caps in there. And there's a whole bunch of relays and everything else. I won't get the board out cuz you got to go to a lot of effort to take this whole thing apart to show you. There's some like a bunch of smaller caps under there and stuff like that. And I can see them, but it's hard to get it on camera. But

**Dave Jones:** everything looks fine in this thing. There's no blown components, no bulging caps, no nothing. So, I'm I'm going to I'm very impressed. I can, you know, I have to do some more thorough testing maybe, but this seems to be somebody's dumped it for some reason and it seems to work just fine.

**Dave Jones:** But unfortunately, I can't like without the remote control, I don't believe I can get in maybe via the network or something perhaps, but yeah, like how to like configure it all up and set up the Wi-Fi and stream and all that sort of jazz. Check it out. I'm actually doing a remote firmware upgrade via the Wi-Fi connection. I was able to do the WPS thing to simply connect to my Wi-Fi box here. I didn't need the remote. I just pressed the button on my router over

**Dave Jones:** there. It connected. Um you hold down straight and press power to get into the like the setup menu of this thing and one of them is a either a USB or a network firmware upgrade. I was on version 1.09 it told me and now it looks like it's downloading latest firmware from the web.

**Dave Jones:** That's fantastic. All right, I I it's verifying. Let's see what happens. Oh, no. It was downloading another S Maybe it's got multiple firmware and stuff. I don't know. Verifying, verifying, verifying. It's fantastic that you can do this erasing.

**Dave Jones:** Okay, so right, it was downloading. Then it's got to verify the contents of what it's downloaded, then it's got to erase the flash No, there you go, S62. All right, so these are obviously different processory things in there that need firmware update. Update success. Woo!

**Dave Jones:** Please power off. So as I said, you press straight and you power it up, you're into the advanced setup remote ID, TV format, init, update. As I said, you can choose USB or network. Version 2.59. Wow. Yeah, I was running 1.09 before. So that's a heck of an update. So unfortunately, I can't do much else. Sorry about that. For those who want to see me repair or something, there doesn't seem to be anything wrong with it. And yes, I do actually score this stuff in the dumpster. It was

**Dave Jones:** dumped in the thing. Like it was it seemed to be like almost carefully placed on top of the box or something like that. It wasn't like, you know, thrown in or something like that, but I don't know what's wrong. Did they change their system and they didn't need it anymore? Did a Did a company move out of the corporate office complex that we've got here and didn't need it? It was surplus to requirements or something?

**Dave Jones:** I have no idea, but yeah, I could probably resell this on eBay. I don't really have a use for it myself, so not sure what I'm going to do with it. Anyway, if you like the dumpster diving video and a quick little teardown of this thing, give it a thumbs up and all that sort of jazz, cuz that always helps a lot. Catch you next time.
