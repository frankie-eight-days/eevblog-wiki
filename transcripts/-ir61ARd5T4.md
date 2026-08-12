---
video_id: -ir61ARd5T4
title: WTF is Wrong with my Rigol DL3021 Electronic Load?
url: https://www.youtube.com/watch?v=-ir61ARd5T4
source: youtube-asr
timestamps: {"0": 1, "1": 21, "2": 34, "3": 43, "4": 57, "5": 72, "6": 86, "7": 99, "8": 111, "9": 124, "10": 136, "11": 153, "12": 168, "13": 182, "14": 199, "15": 213, "16": 229, "17": 242, "18": 260, "19": 276, "20": 292, "21": 307, "22": 321, "23": 335, "24": 352, "25": 369, "26": 378, "27": 393, "28": 409, "29": 427, "30": 446, "31": 462, "32": 476}
---

**Dave Jones:** Hi, yet another follow up video on this Goal Zero Yeti battery, but this one isn't really about that. It's about this Ryobi deal 3021 electronic load here, and it's a rather interesting problem. Look at this. So, I was just going to

**Dave Jones:** use this like to test the battery capacity cuz it's got a battery mode on it where you know, so you go and say it's got the regular constant current constant voltage constant resistance constant power everything else. But, it's got a battery test app

**Dave Jones:** which will give you the amp and which will give you the amp hours and the watt hours as well, and you can set like cut off voltages and what constant current you want to test at, right? And very

**Dave Jones:** cool stuff, okay? So, let's see what happens when I hook it up to my Goal Zero here. Okay, it's almost finished charging. The great Oh, there we go. So, I switch on the 12-V output, and you can see that the 12-V output you can

**Dave Jones:** actually see the 12-V output the battery charging up here, right? Because this 12-V output on the Goal Zero is basically direct is basically connected directly across the battery. There's not a 12-V regulator in there cuz this is a

**Dave Jones:** what a nominal 12.8-V pack or what whatever it said on it, right? So, it should like charge up to that. It's currently 91% there. It's charging at you know, 70 W or whatever. And so, it'll eventually get up to you

**Dave Jones:** know, whatever the cut off voltage of charge controller in there and deems to be the maximum voltage. But, let's just say 12.8 or something. So, when you actually power stuff on here, it's acting like just like a car battery

**Dave Jones:** really cuz you've got the 12-V cigarette lighter here like a car, and that's connected directly across your car battery. So, it'll be like 13.8 V when your alternator's running, and you know, and then when your car's off and you're

**Dave Jones:** powering something from it, then it's just going to be the 12-V nominal 12-V and then it's going to drop. So, I guess that's the idea there rather than have a regulator in there like a you know a SEPIC like a

**Dave Jones:** buck booster converter in there to actually do it anyway. Right, so we can see all right we've got great resolution on here. We can see that, okay? Now, I've got this set for 1 amp, okay? So, we can actually switch this on so it'll

**Dave Jones:** be 1 amp constant current and we can switch this on, okay? And it should be and why it's drawing 0.1 amp I don't know, okay? So, I was able to actually get it to draw 1 amp. If I can set one again

**Dave Jones:** like that, whoop it goes up to 1 amp. So, what the heck, right? Right there there's an issue with it, right? This is just crazy. Anyway, so bug number one um so it's now drawing an amp, okay? And then and this is all

**Dave Jones:** hunky-dory. I was just you know experimenting with this before. Now, watch what happens I think if I just um simply switch it off here. If I switch it off this is turned red and I can I can hear some like buzzing

**Dave Jones:** in there or something. Something's going on. If I try and hit that again green, it just goes instantly to red, right? And if I disconnect that it's green. So, it's like this thing is loading it down and sure enough watch

**Dave Jones:** this. If I get my ohmmeter here oh oh and I'll turn on the electric field probe. There we go. Can you see that? Yes, you can. So, what I'm going to do now is like is just measure the ohms directly across uh

**Dave Jones:** right the input, basically the input of this electronic load, which is supposed to be off. It is supposed to be off, okay? Look. It's like it's 1 point LIKE IT'S 1 OHM. LIKE HALF AN OHM. It's shorted. No wonder this thing I like I

**Dave Jones:** thought oh there's something wrong with the Goal Zero battery. It's you know, it's chucking a wobbly or whatever. No, it was just protecting itself. It's obviously got a resettable overcurrent fuse limit in there, and it was it was

**Dave Jones:** just just protecting itself from the bloody short circuit that this thing is presenting even though it's off. It's literally off. And there's a short circuit across the input there. I mean, you know, I can I can probe directly across the inputs.

**Dave Jones:** There we go, directly across the inputs. It's a dead short, a dead short, and the only way to fix this is to is like literally to turn the power off then on again, right? And because this is not like a physical short, it's a

**Dave Jones:** like, you know, it's switched on a giant MOSFET. There you go, 28k now it's fine. So, there's like some big crowbar thing either there's some big crowbar thing or it's deliberately like going into constant resistance mode and it's assuming No, well, see see? It

**Dave Jones:** just went to zero ohms there. Reverse connected. Reverse connected. It thinks because I've got a little bit of voltage. Sorry, yeah, that that's probably my fault. Okay, I probably shouldn't have done that because it was thinking because the

**Dave Jones:** ohmmeter is actually actually presenting a voltage across here. So, yeah, it it really didn't like that and I've got it back-to-front or whatever. Doesn't matter. Anyway, so Oh, yeah, there we go. Reverse connected yet again. Okay, so we

**Dave Jones:** go okay. So, I swap the probes around and there you go. That's better. It's not going to complain now. So, but you can see it's not shorted now. But if I do that Right, so I'll I'll just Let's just

**Dave Jones:** try this. I haven't tried tried this yet. Look, I turned it on and it's a dead short. Oh, sorry. No, cuz we're in constant load kind of zero ohms, right? But let's let's go to the battery app. It's still zero ohms, right? We're in

**Dave Jones:** the battery app. Off. Off. It's a bloody short circuit across the input. What the hell's going on? Now, I do actually recall seeing this like I thought that so you know I was using this to load up something. I can't remember what it was.

**Dave Jones:** It was quite a long time ago. That was probably the last time I've used it. I thought, "That's weird." I might Did I even do a video on it? I'm not sure, but anyway, like a like a second channel

**Dave Jones:** video maybe saying there's something weird going on here, but anyway, there's definitely something bloody weird with this DL3021. That is ridiculous. Now, I I know that if we go back to say constant current, right? And I'm not sure why if we're in

**Dave Jones:** constant current mode, it's showing zero ohms anyway, right? I mean, that's just like whatever. Like but it's like it's shorting the output. Like if we go into constant resistance, constant resistance mode is currently set to two ohms down

**Dave Jones:** there, right? So, I'm not sure what the like what the hell? What the hell? Your load, electronic load, should not present a short circuit across the thing unless you have it in constant resistance mode and you set this to 0.000

**Dave Jones:** ohms and you switch it on. Unbelievable. And yes, I've checked it's got the latest firmware. This is like 1.05 or whatever and I checked it seemed to be the latest firmware. So, what the heck? What the heck's going on? Anyway, if you

**Dave Jones:** got one of these turds, then let me know in the comments down below if yours does a similar behavior to that cuz I'm not sure if this thing's bloody got a fault or whether or not it's just it's like I I believe that this would be

**Dave Jones:** like normal operation of this turd. I I just cannot believe it. I don't get it. Anyway, thoughts and comments down below. I think for these tests I'm going to switch over to my old BK Precision here. I think that's got a battery

**Dave Jones:** mode as well. So, anyway, it's really annoying when you can't even trust your bloody test gear to man, I just like I'm thinking about getting the wire lacerator on this sucker. Catch you next time.
