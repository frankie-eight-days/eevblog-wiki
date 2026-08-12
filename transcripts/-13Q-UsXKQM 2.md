---
video_id: -13Q-UsXKQM
title: EEVblog #112 - GSM vs The Fluke 87V Multimeter
url: https://www.youtube.com/watch?v=-13Q-UsXKQM
source: youtube-asr
timestamps: {"0": 0, "1": 39, "2": 73, "3": 90, "4": 118, "5": 134, "6": 161, "7": 177, "8": 201, "9": 230, "10": 249, "11": 267, "12": 285, "13": 305, "14": 327, "15": 358, "16": 384, "17": 395, "18": 423, "19": 464, "20": 486, "21": 505, "22": 527, "23": 554, "24": 567, "25": 586, "26": 605, "27": 627, "28": 641, "29": 661, "30": 686, "31": 696, "32": 725, "33": 743, "34": 760, "35": 782, "36": 802, "37": 821, "38": 841, "39": 869}
---

**Dave Jones:** Hi, welcome to the blog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi. Why do I have the lab coat on today? Well, it's myth busting time. Okay, not so much a myth really because this comes from a real problem that I saw on the EE blog forum. Now, it started one of the EE blog members Twistex, he actually reported that his Fluke 87 V multimeter started playing up when it was near his wireless router.

**Dave Jones:** And well, okay, you know, nothing unusual there, you know, meters and all sorts of equipment are susceptible to electromagnetic interference. In fact, the Fluke 87 V is rated to keep its accuracy up to around 3 V per meter. Now, I'm not sure what a wireless router actually puts out. I haven't done my research on this, but you know, you can expect, okay, it plays up. But, another user, Kerim Cos, he actually decided to get his mobile phone, got his mobile phone and he put it next to his Fluke 87 V

**Dave Jones:** and it killed it. It bricked it. So, yeah, I thought I'd sacrifice my 87 V and try it out cuz this is really interesting. Let's see what happens. Okay, first up, let's try the router. I've got a D-Link wireless router here.

**Dave Jones:** It's a DIR-300, pretty standard sort of router. I've set it to 100% output transmit power and as you can see, it's wireless. I'm actually streaming a YouTube video here on my notebook, so it's all transmitting. I've got a Fluke 87 V as you can see and let's put it near the antenna and see what happens.

**Dave Jones:** Yeah, it's certainly going up, jumping up to 33 millivolts AC, but it's certainly not doing anything unusual. Um, I'll zoom in on that and um see if you can see it. And yeah, it's not doing anything, you know.

**Dave Jones:** There's no weird stuff happening at all. So, uh yeah. No problem whatsoever. Test passed. Okay, I know what you're thinking. I didn't have the probes attached, so tada, I got the probes attached. Here we go. Yeah, it's much higher now, 300 millivolts AC. I mean, you know, that that figure's just meaningless. It's just picking up anything, but it's certainly not doing anything unusual.

**Dave Jones:** Um, at all. It's not causing any uh damage to the meter, no weird digits as was uh as was reported, so there you go. No problems. Now, just before we try the mobile phone, I thought I'd uh try just a standard cordless phone. It's a Doro.

**Dave Jones:** Um, don't know the model, but doesn't matter. Let's put it about a foot away, shall we? And I'm going to call it. And it's answering, it's transmitting, okay? It's transmitting and uh it should I'm definitely got my mobile phone about a meter away. Um, and there we go. Uh, no problems at all on the no problems at all with the Fluke.

**Dave Jones:** You know, it's it's picking up something, but it's certainly not uh killing it or doing anything unusual. So, um a cordless phone, perfectly fine. And now for the big test, a mobile phone. This is a Nokia uh E71 as you see, and it is um not 3G at the moment cuz I get uh 3G coverage here, but okay. I'm going to put it about a foot away and I'm going to ring it. Let's try it and see what happens. Okay, we're answering and we're talking, so the

**Dave Jones:** mobile phone is active as you can see. Um, I'm getting you know, I'm I'm getting full bars on there. But as you can see it's not 3G, okay? It's just standard GSM, but it's actually we're in the middle of a call, so let's put it near it. Wow, yes.

**Dave Jones:** Something's happening here folks. Something's happening. Watch. See if I can get Let's see if we can get this. Well, yeah. Oh, yeah. Look, something's going on. See that on the display? I'm definitely recording this. Wow. Look at that.

**Dave Jones:** Look at that. So it has to get Looks like it has to get reasonably close. Looks like it's got to get within say 6 in before it before it starts to do something.

**Dave Jones:** And wow, yeah, it's completely neutering it. Look at that. There it is. There it is. Confirmed, it does screw up, but it's not bricking it. It's not bricking it.

**Dave Jones:** It's it's fully recovering. Wow. Yeah, it's really really doing some weird stuff, all right. But yeah, it seems the it doesn't seem to do anything on the right hand side here. On the top, nothing.

**Dave Jones:** But on the left hand side here, definitely. Look at that. Wow. Check it out. Awesome. Yeah, there's something there's something that's susceptible that causes susceptibility on that left-hand side. Um, in fact, let's leave it in the middle of the call. Okay, we're still on the call and let's switch it on, shall we?

**Dave Jones:** Uh, it just really screws up the display and that's about it. Okay, I've just got a small collection of meters here, the cheap Vici, BK Precision, Extech, German Gossen Metrawatt, and the Fluke 87. And as you can see, we're still uh calling here. It's exactly the same call. I haven't um changed it. It's not uh 3G, it's just standard GSM. And let's put them near these other meters.

**Dave Jones:** No problems on the Vici at all. Let's try the Extech. No problems on the Extech.

**Dave Jones:** No, none. BK Precision. None whatsoever. There's a Yeah, nothing. Gossen Metrawatt. Uh, get that on screen there. Nothing on the Gossen Metrawatt at all. Not a thing. Perfect. And our friend the Fluke 87. Ta-da! Oh, look at that.

**Dave Jones:** Wow. Wow, that's really That's really something. It doesn't happen at all on the right-hand side. Not a thing. But left-hand side within Yeah, I don't know, a couple of inches, it's really starts to play up. Crazy. But we haven't bricked it. So, um yeah, I guess um I don't know. I'm just You know, this either hasn't You know, I'm uh uh it's just different output power or something like that to the transmit tower or something like that. But yeah, there's definitely a problem with the Fluke 87 with near field um

**Dave Jones:** EM high energy EM sources like that. And let's just try another transmitter source. This is a little uh Uniden UHF uh walkie-talkie and let's put it right beside it. Let's put the antenna right there and um see if we can do it. Here's the other receiving one and let's transmit.

**Dave Jones:** Check check one two. No, it's just going up a bit, but it doesn't uh doesn't do anything. I'm pressing the press-to-talk, so it's definitely transmitting. As you can see, there's a little transmit uh transmit symbol there on the display and nothing.

**Dave Jones:** Nothing at all. So, that's okay. That's not not high enough at all, but the mobile phone There it is. I'm still on the call. The mobile phone really Whoa, hang on. Whoa. Look. Look. I killed it. Look. It's switched off. The display totally switched off.

**Dave Jones:** Huh. Check it out. My my call's been disconnected. Not sure why, but look. Let's switch it off. No, it recov- Phew. It looks like it's recovered. So, yeah. But it You saw that. It It literally locked up the processor enough to not recover at all. Crazy.

**Dave Jones:** Let's see if we can reproduce that. It's calling again. Wait. There we go. Look. Straight up. It switched off straight away that time. Straight away.

**Dave Jones:** Yeah, it's come back. It hasn't killed the firmware like it did in poor Kyriakos's Fluke 87, but as you can see, I can I can easily picture what happened to his happening to other people's because yeah, look, it switches the damn meter off. That's crazy.

**Dave Jones:** Okay, I've called it. We've taken it out of the rubber holster and I've got it on loudspeaker as well. Oy, there we go. Feedback. And it's really it's really killing the display. All of them are lit up. Woah.

**Dave Jones:** Upside down. Check it out. Wow, it really affects it, but we haven't bricked it. There you go. And we're doing the same thing with the Gossman meter. Not a thing.

**Dave Jones:** No, nothing. It's a great effect. I love it. But yeah, no, definitely the Fluke the Fluke is buggered. CHECK IT OUT.

**Dave Jones:** WOOHOO. FANTASTIC. OKAY, let's try another phone. I've got a Nokia 6300 here, not 3G, but I'm I'm on the call at the moment. It's actually transmitting as you can see, and let's give this a try, shall we?

**Dave Jones:** Hey, yeah. There we go. Oh, yeah, boom. Yeah, look at that. Got him. But it still recovers. And let's just do one more, a Nokia something or other. I don't know the model, but we're on the call. It's actually transmitting and let's give it a go. Hey, there we go, straight away. Boom, gone. Gonski.

**Dave Jones:** And we couldn't leave it at that. I had to drive around until I found 3G coverage to get out of the black hole I live in. So, let's give it a go. Okay, I've gone outside. I found 3G reception.

**Dave Jones:** There it is, 3G, and let's try it out. I'm transmitting, of course. Here it is. Ta-da! Oh, look. Check it out, 3G. 3G doesn't do anything. Wow. Look at that. So, it looks like it's it's specifically the GSM frequency. Go figure.

**Dave Jones:** No, nothing. Nothing at all. 3G doesn't do a thing. And just as a control, I've turned off 3G, so I've just got GSM now, standard GSM as we had back in the lab, and let's try it again. So, let's just under control conditions. There it goes.

**Dave Jones:** Yep. There we go. So, it's definitely definitely the GSM frequency doing that. Yep. What?

**Dave Jones:** Oh, yeah, there it goes. There it goes, switched off. And it just so happens I have the Fluke 87 V's twin cousin, the Fluke 28 Series II. Let's give that a go, shall we? Once again, I've got the I'm back on GSM again. Okay, let's give it a go. Here we go.

**Dave Jones:** Nothing. The Fluke 28 II doesn't do it, which is an identical Well, you know, it's an upgraded design, but it's essentially identical to the 87 V. Um no problems at all.

**Dave Jones:** No, nothing. Not a thing. Not a thing at all, whereas if we bring in the 87-5 again, here we go. As a comparison, there we go. Boop. Boop. Display just goes berserk straight away. So, the 87-5 is definitely something to this.

**Dave Jones:** So, there you have it. It's not a myth. The Fluke 87-5 is susceptible to near field EM high level EM radiation, particularly on this left-hand side next to the LCD. It's a real problem that Fluke need to look into. Now, I wasn't able to brick mine like uh Kyriakos was, and he lost his firmware and everything.

**Dave Jones:** Um I wasn't able to do that, but certainly able to lock it up real easy with a GSM signal. Who would have thought? And I didn't see any effect on any of the any of the other meters I had. So, it's particular, and including the Fluke 28. So, it's particular to the Fluke 87-5. There's a vulnerability there. Fluke need to look into it. And let's see if uh Fluke live up to their uh uh stand by their lifetime warranty and replace Kyriakos's unit. We'll find out, but don't try that at home with

**Dave Jones:** your Fluke 87, kitties. Leave it to the professionals. See you next time. And if you are going to try this at home, remember, kitties, wear protection.
