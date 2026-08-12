---
video_id: MkQisz2VF8I
title: EEVblog 1739 - UNUSUAL FAULT! in a Beelink Ryzen 9 Mini PC
url: https://www.youtube.com/watch?v=MkQisz2VF8I
source: youtube-asr
timestamps: {"0": 0, "1": 19, "2": 32, "3": 48, "4": 62, "5": 77, "6": 92, "7": 106, "8": 120, "9": 139, "10": 157, "11": 174, "12": 192, "13": 207, "14": 223, "15": 239, "16": 254, "17": 271, "18": 281, "19": 298, "20": 313, "21": 325, "22": 344, "23": 369, "24": 389, "25": 408, "26": 427, "27": 438, "28": 456, "29": 470, "30": 484, "31": 499, "32": 519, "33": 533, "34": 553, "35": 568, "36": 580, "37": 592, "38": 607, "39": 616, "40": 636, "41": 652, "42": 669, "43": 686, "44": 703, "45": 722, "46": 737, "47": 747, "48": 759, "49": 771, "50": 788, "51": 805, "52": 817, "53": 828, "54": 842, "55": 855, "56": 867, "57": 882}
---

**Dave Jones:** Hi. Yes, my camera looks a bit different today because I had to budge in a little old SJCAM 5000 webcam thing because I normally use this Canon HFM 400 which was my old B-roll camera, but the stupid plug pack

**Dave Jones:** thing on it looks like it's died. It's like 8.4 volts at 1.5 amps. So, yeah, it's deadski. So, yeah, not something I can easily open. Anyway, I've just budged this camera in so it's got all the crap on the screen. Whatever.

**Dave Jones:** Anyway, I've got this BLink mini PC here. I can't remember the exact model number, but it's got a Ryzen 9 6900HX. It's the most powerful mini PC I have here in the lab and Sagan was actually using this as his home PC, but he

**Dave Jones:** upgraded. He discovered one of my my old video editing desktop machine in the dungeon and he said, "I want that." So, he's now got the with an RTX 2060 graphics card and everything else. So, he's thrilled with that. So, he's done

**Dave Jones:** with this, but at the time this thing had actually failed. So, I've got it actually plugged in here, okay, and it is drawing power. I've actually measured that it actually draws, you know, a watt or something like that. And there's a little little

**Dave Jones:** power LED there. And if I press it, wah wah wah wah and yeah, I've held it down, blah blah blah, all the rest of it and I cannot get this stupid thing to do anything. Now, I did actually I've taken

**Dave Jones:** it apart once before and then I put it back together and it magically booted up once, but once only. It only booted up the once and it's never booted again. So, I don't know what the heck is going

**Dave Jones:** on with this thing. I just noticed is that is that a reset hole? It's not marked with anything. Have a look down in there. Does that look like a reset button? That looks like That could be a resety thing.

**Dave Jones:** So, maybe I can try giving that a poke. Yeah, there is a BIOSy reset button there. No. Still nothing. Do I have to hold it down? Maybe. I'm going to leave it there for 10 seconds. Okay. No, still nothing.

**Dave Jones:** So, I'm not sure what's doing there. Um not happy at all. So, I'll just plug it back in. Oh, my camera died. So, anyway, I got no idea what's wrong here. I think um Sagan was actually upgrading something at the time. He was upgrading

**Dave Jones:** some memory or something. And I think it After that, it worked, but then it failed. So, I'm not sure what mechanism actually um caused it. So, I'm going to get this board here out. And so, let's disconnect the power. So, we'll take

**Dave Jones:** this out. This this is a modular thing. Yeah, there's a screw under there. And yeah, it's weird, but I did get it to work once. Um and it just never worked again. Unbelievable. So, anyway, yeah, so I've taken the

**Dave Jones:** memory out of this thing. And we can see under there. It's got the Wi-Fi card. Um I've I've taken the memory out of here. I've tried doing that, and it makes no difference. Um yeah, so I'm just clutching at straws at the

**Dave Jones:** moment. Check stuff like the ribbon cable. I mean, he didn't ever like never touched any of this down here. So, I don't think it's got anything to do with that ribbon cable at all. Like, it's not like there's anything

**Dave Jones:** broken there or something like that. But that would be your first port of call is like, you know, have has something happened to the pins? I'll have a look at the connection under here. He said he did take this connection off, I believe,

**Dave Jones:** because he thought that to access the second um slot under here that he had to take this board out, but he quickly realized that that wasn't the case. All of our connections on there look hunky-dory, don't they? No problem

**Dave Jones:** whatsoever. There's nothing doing there at all. That looks beautiful. That looks fantastic, doesn't it? That's a Bobby Doesler. There's no issues there whatsoever. Don't even have to give that a blow job. That is clean as a whistle. Jesus,

**Dave Jones:** there's not much solder on that poor pin, is there? So, is that some reset controller 46032417?

**Dave Jones:** I don't think he said that he took out the header here, but I'm going to have a squiz at that one, too. Just in case. That's clean as a whistle. Flat flex connector, again, looks really good. No issue there at all. I'll get the

**Dave Jones:** bottom of this flat flex out, just as a matter of course, though he assures me he did not touch that. So, I can't see how he's broken anything in here. I don't see how that's a thing. Again, that looks beautiful. Focus, you

**Dave Jones:** bastard. That looks great, doesn't it? So, no drama there whatsoever. Sorry, the camera's died again. Just going [clears throat] to put it all back together because I don't think the power supply has died. I might be able to like

**Dave Jones:** measure a power rail on that reset, what I presume is that reset chip there. Sorry, that stupid SJCAM camera's completely died in the ass. No, doesn't do anything. Okay, I'm just going to see if there's any voltage across

**Dave Jones:** a cap in here. There's not this side, 0.4 volts. Wow, check this out. Watch. When I What Watch the power light up there. I just put pressure on there and it powers up. I release pressure. What the heck?

**Dave Jones:** What the heck is that? Look at that. >> [laughter] >> Bingo. Sorry, my camera My stupid camera's not working. Can't see the expression on my face. That's very interesting. There is something wrong with And yes, I don't know where the other

**Dave Jones:** screw for that is. Um, maybe that's it. Maybe there's your problem. There we go. I can't even remember how this uh, actually connects into onto the main board. Whether there's a board-to-board interconnect or whatever, but anyway, there's the bottom. It's got the main

**Dave Jones:** switching supply. Oh, oops. Look, screw missing. Screw missing. There's only one screw up under there. Was that a me problem? I didn't assemble this power supply back, but he used this PC for ages. So, I don't know what why that would

**Dave Jones:** have been a problem or why this lines up here. Okay, there was that one screw missing there. Um, I don't know where that that uh, left over from when I did the teardown of this thing, but it worked

**Dave Jones:** for ages after that. But, there's that one screw missing there. Is it using that standoff as a way to connect? Ah, are they using Yes. Yes, test point. It's a test point. That is Sorry, you can't see the

**Dave Jones:** expression on my face. That is a test point. It's simply a screw. They're using that standoff to get Yeah. Yeah. Look at that. Yep. It's a pad down there. They're using that screw. That's it. That's why when I

**Dave Jones:** put finger pressure on there, the thing powers up. Damn. That's all it was. That's all it was. So, I don't know why this Sorry, I wish I could get this stupid camera working. Ha, we're back. I changed it to my Sony

**Dave Jones:** ZV1 camera. I haven't looked at how to get the info off the screen or even if you can. Um presume you can. It's a pretty modern camera as opposed to the other one. Yeah. This is interesting. That that is

**Dave Jones:** That's just not to hold down the board. That is they're getting the output power from that. There's an output power MOSFET there and they're using that to get the power down. So, maybe maybe Sagan took when he was upgrading this thing, he

**Dave Jones:** took that mistakenly took that screw out and then forgot about it. Either that or I forgot to put that screw back in when I did the teardown. But this computer had had been working flawlessly forever. For months and months. Ever since when I

**Dave Jones:** did the review of this thing and Sagan didn't use this home PC. Um So, yeah. That's There's your problem right there. That's why when I put my finger and pressure on there, it it makes contact down there and switches this thing on. Damn. That's

**Dave Jones:** all it was. Oh, it's so obvious. >> [laughter] >> There's probably people screaming at me that they saw that. Oh, yeah, saw that straight away. Um you know, I just assumed because Sagan did say that he he thought he had to take out

**Dave Jones:** this IO board. So, he took out this IO board to access, you know, the lower to get access down to the lower M.2 cuz it's got two. It's got one there and one right down in in there. Now, it's easy

**Dave Jones:** enough to think that. Um and um yeah, cuz these are these are rather delicate little connectors. So, I thought, "Oh, there might be something wrong with the connector when you put it back on." But, no. No, there's nothing wrong with that

**Dave Jones:** at all. It's a missing screw. Damn. Unbelievable. All right, so I'm just going to have to find a screw that goes in there, I guess. Um right. >> [laughter] >> Where do I get one? Well, I've got my

**Dave Jones:** big screw collection downstairs, but uh no, I'll just find one here on the bench. Probably got one here lying here.

**Dave Jones:** There you go. Just found one lying there. >> [laughter] >> I don't know if that's uh let's see if that is size. Looks a bit long, but What What's going on? No worries. Oh, look at that. Bobby Dazzler. There you go. It was just

**Dave Jones:** sitting here on the bench. I'm not going to show you the bench. It's pretty terrible. So, does this other one over here need it? That looks more like a traditional mechanical mount, that one. But, anyway, I'm going to

**Dave Jones:** find another screw for that one as well. But, we've got our protective cover here. So, I'm so confident this is going to work that I'm going to put my memory back in there. There you go. And PCI 3

**Dave Jones:** times four for those playing along at home. And oh, I need to screw that down in there. Screw that back in. No wuckers. And this has to There's a little thing under there that's got to hook under. Okay, I don't have a second

**Dave Jones:** one, so we'll just put that there. All right, here we go. I have now >> [laughter] >> put it back together. Trust me, that screw is is under there and let's Oh. I can hear the fan already. It's already

**Dave Jones:** powered on. There it is. No wackers and I'm sure yep. You can't hear it. I can hear that fan permanently on. That is repaired. >> [laughter] >> There you go. These things happen. Like I don't know if that was me after I did

**Dave Jones:** the teardown and I didn't put that screw back in. Uh but that wouldn't explain why it's lasted so long. Sagan could have like inadvertently taken that screw out and just forgot like I you know got him to mentally reverse the process of what he

**Dave Jones:** did and stuff like that. But even after he put it back together like it worked cuz he did the upgrade and it worked and then one day it just stopped working. So we went you know asked him go back

**Dave Jones:** through the process and I thought maybe you know some damage to the flat flex or something like that but no. No. It was just a missing screw under there on the power supply and they were using as I

**Dave Jones:** was going to say in the video, they I didn't know how they got the power through from that board whether or not there's a pin header on there or whatever. No, they're using the standoffs to transfer all of that power.

**Dave Jones:** That is the main power rail and that's why it didn't work. And when I put my thumb on there, that made contact and boom, it started up. Isn't that fascinating? There you go. Completely come a gutser there but that

**Dave Jones:** is fixed. We solved We solved that. No worries. There we go. Fan's off. Now it's gone into power down mode. So yeah, that works fine such a simple thing but that is just I'm we're lucky that it was like an

**Dave Jones:** obscure fault like that. If it was just a oh we damaged a pin on there or whatever. Like, you know, this is way more fascinating that they were transferring power through the standoff. If you didn't put the screw in, if you forgot that as an

**Dave Jones:** assembly step, for example, at the factory, if you're at the B-Link factory and you forgot to put that screw in, then it might make contact and pass the test, but when it gets shipped to the customer, for example, oh, and my my

**Dave Jones:** computer doesn't work because you've got an intermittent contact on there. So, that's certainly like that is possible. And when you do a repairs on this thing, you know the old curse of oh, I've got some screws left over. When you do a

**Dave Jones:** when you take something apart, you repair it or do a teardown or upgrade or whatever, you've got a couple of screws left over. In this case, it mattered and it mattered a lot. That is fascinating, is it not? Anyway,

**Dave Jones:** hope you enjoyed that and found it useful. If you did, please give it a big thumbs-up. As always, discuss down below and check out the EV blog store for the merch cuz YouTube ain't paying much these days. Catch you next time.

**Dave Jones:** Oh, by the way, my plan for this machine was that I was going to run Open Claws on it and see if I can do anything fun with Open Claws. Anyway, maybe a video to come on that.

**Dave Jones:** >> [music]
