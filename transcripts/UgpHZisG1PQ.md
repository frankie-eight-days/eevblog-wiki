---
video_id: UgpHZisG1PQ
title: EEVblog 1573 - TEARDOWN: How a Rotary (Angle) Pulse Encoder Works
url: https://www.youtube.com/watch?v=UgpHZisG1PQ
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 37, "3": 55, "4": 67, "5": 79, "6": 94, "7": 108, "8": 124, "9": 138, "10": 152, "11": 165, "12": 184, "13": 195, "14": 210, "15": 225, "16": 239, "17": 255, "18": 272, "19": 289, "20": 302, "21": 314, "22": 331, "23": 350, "24": 367, "25": 380, "26": 397, "27": 410, "28": 434, "29": 449, "30": 462, "31": 473, "32": 486, "33": 503, "34": 516, "35": 536, "36": 552, "37": 565, "38": 576, "39": 594, "40": 609, "41": 624, "42": 638, "43": 652, "44": 669, "45": 684, "46": 701, "47": 717, "48": 730, "49": 748, "50": 766, "51": 781, "52": 799, "53": 816, "54": 831, "55": 851, "56": 862, "57": 877, "58": 884, "59": 897, "60": 913, "61": 928, "62": 943, "63": 960, "64": 974, "65": 986, "66": 1001}
---

**Dave Jones:** Hi, by popular request, we're going to attempt to take apart this rotary encoder, this oddball rotary encoder from the Haefely Trench PE SD 1600 gun that I've got. And of course, I've done I'll link in the video if you haven't seen it. Somebody

**Dave Jones:** eventually found you can still actually buy this. Let's check it out. Made by a company called EBE, a German company, and it's basically a dream impulse Goofing that one. But yeah, it is different to your usual, you know,

**Dave Jones:** three-pin phase quadrature encoder that you're used to. You know, these are dime a dozen. This one actually goes in different directions. So you can see that it's got three pins here, and you've got it like a single pole double throw

**Dave Jones:** thing on either side. And it only, you can see down here, it only goes in when you turn the one direction, only one side of it actually toggles when you move it. And then when you go in the

**Dave Jones:** other direction, so this one toggles, wiggle wiggle wiggle, yeah, back and forth, but this one stays still while you're going one direction. And then when you go in the other direction, this one wiggles and this one stays still.

**Dave Jones:** It's It It I I don't know how it works physically inside. So it's rather interesting. So let's tear it down. As far as I know, please leave it in the comments, but I'm not aware of another rotary encoder that works like this. Was

**Dave Jones:** this like an old school thing that was, you know, this is like early '90s, early to mid '90s vintage, but apparently like they still make it or whatever. So anyway, we're going to tear it down. Now, it doesn't look like

**Dave Jones:** it's going to be easy. We've got four little plastic studs there that looks like a heat um welded like in place. So, we're probably going to have to drill those out. I can actually get a blade down the side here,

**Dave Jones:** but it's not going to come out unless I drill those, I suspect. All right. Uh handy tool for this is a uh pin vise. So, um just like a little handheld drill thing. I've got it on an angle here, so

**Dave Jones:** hopefully you can see it. That's not optimum for me. Hang on, I'll get my higher res glasses on. I do actually have two um pairs of glasses. These are my regular ones, which are 1.25 times magnification. Not very much, but you

**Dave Jones:** know, I I need them these days. Um and these are I got these um my optometrist to optometrist to give me these uh which are 1.75 times. So, for close-up work, they're just more betterer. Anyway, um some people have said like they've got

**Dave Jones:** five times or something. Jeez, that's like that's like Poindexter stuff. Anyway, um let's let's go. We'll we'll give it a go. And you want it oversized. Yeah, it's hard when they're like round on top. It's cutting away. There you go. Yeah.

**Dave Jones:** It's going to take a bit. Might have to get in there later with a smaller one, but let's let's try and get the bulk of it out. And of course, I don't care about damaging this now because I you can buy

**Dave Jones:** these for 6 euros each on eBay in Germany, only in Germany, and you could only find the data on this if you were a German speaker and you knew the correct correct German search term. Cuz the rest of the

**Dave Jones:** the rest of the interwebs, the rest of my audience could not find it. But if you were in Germany, went, "Ah, if I In German, this means this term." I won't pronoun- I can't pronounce it, but anyway, um yeah, they're able to find it

**Dave Jones:** within minutes of of knowing the correct German search terms. So, please, yeah, leave it in the comments down below. If you've ever used a rotary encoder that works like this, where you only get where the contacts only work in one

**Dave Jones:** direction. It would make decoding easier because, you know, there's a bit of a like art in writing your algorithm to decode your quadrature output. Everyone just uses a library these days, right? It's built into your Arduinos or whatnot. But for anyone who's had to and

**Dave Jones:** I've had to do this, had to write your own little algorithm that detects the direction of operation. Uh on your regular quadrature output, I won't bother putting up details there. You can Google a quadrature or phase-based rotary encoder or just

**Dave Jones:** how how a rotary Oh. Oh, look at that. That one just popped out. Oh, look at that. Wow. Wow. So, that one was a bit how you doing? Anyway, yeah, I did further damage this. It It only had the one pin broken. I

**Dave Jones:** think it was this one here. Uh like it was just open and the rest the others were um and uh fine. And then although No, they're a bit dodgy cuz it's supposed to be a Just changing drill bits. It's

**Dave Jones:** supposed to be a um one where it, you know, it just alternates back and forth like that, right? Just back and forth, back and forth, back and forth like that. But when I turned it in the direction that

**Dave Jones:** worked, the other one didn't seem to do it every every click. It just So, yeah, there was something something there. So, let me change to a smaller drill bit here. Yeah, so I think the whole rotary encoder was just just cactus.

**Dave Jones:** Tongue at the right angle. Always important. I've actually got to put a lot of force onto that. Fingers get quite sore after doing four of those. I was going to do an everyday carry shootout between my Victorinox Mini champ, uh which is my be my daily

**Dave Jones:** carry for like 15 years now, and this cheapy one, I can't remember the brand. No, it's the Olight. Olight, they make like torches and stuff. And the Gerber, I can't remember which Gerber it is, but yeah, I I was going to do a shoot out, and then

**Dave Jones:** I recently lent my Gerber to Mrs. EE Vlog. She was using it to actually use the bottle cap opener to open some paint stuff. Never saw my Gerber again. So, I don't know what happened to the Gerber. I was

**Dave Jones:** going to do a shoot out, damn it. Anyway, never loan your tools to to the misses. So, let's see if we can get some that knife in there. Does that Is that now going to lift up? No. No. Oh, hang on.

**Dave Jones:** Yeah, I Can I see that move? This is not 3D, but yeah, yeah, yeah, yeah. Yeah, we got it. Spoiler alert for the shoot out. I think the mini champ would have won.

**Dave Jones:** It's just it it's far superior quality. Oh, look, look, poppity do dah. Poppity do dah. Oh, oh, look, there's a Oh, look. Look at that. Look at that. There you go. It's That's of course. Of course, that's how it's going TO WORK.

**Dave Jones:** YES, HERE IT IS HERE. Sorry for the yellow background. That's a post-it note, cuz I've got a new stand for my Taganau microscope here, so I can actually lift my Taganau microscope up. Yeah, you can see it. I can actually

**Dave Jones:** lift it up now. And yeah, yeah, you can physically see it moving there. So, I've got a lab jack. I've got a lab I got a Vivo lab jack. I put this on Twitter. And But, so now now put like larger objects

**Dave Jones:** over there under there to focus, but the problem is is that now the minimum focus is not not at bench level, so I've actually got a So, if I put this down here, right down here like this, it

**Dave Jones:** won't focus. It won't focus it when it's zoomed in. So, yeah, unfortunately, it's out of the focus range, so I've actually got to lift that up now, but it does allow me to put The advantage is that allows me to put

**Dave Jones:** bigger stuff under there. Anyway, there we go. I'll put that on top of my Post-it note. Now, yeah, of course. That makes sense, right? You've got just a lever that just flips between there and and there, right? So, and there's a

**Dave Jones:** little plastic I'll show you the plastic cam in a second that goes in there and then just puts force across there and boom boom boom boom it it just it it just switches between like that. So, this inside of

**Dave Jones:** here as it turns must have Like, this thing can't obviously spin around, but it must because of the shape of that the inner bit there must cause this to just back and forth between these two here, so there doesn't seem to be anything wrong

**Dave Jones:** with the contact in there, right? Cuz the contact goes straight through to the pin unless that's physically unless that's physically broken. I can actually measure that and I can buzz that out. Let's buzz it out. Yeah, it's still in play, but that was

**Dave Jones:** the good Was that the good one? Ah, ah, yeah, there you go. It's open, right? So, it's on there, yeah? But, it doesn't connect. Oh, no. No, it does actually connect. There you go. So, that pin it's sort of like sitting in

**Dave Jones:** the middle, so I reckon is that just like worn out and it just sits in the middle and it wasn't Yeah, it I don't think Yeah, that was bent. I reckon that arm there was bent and it was never

**Dave Jones:** making contact. So, as this thing spins around in here and is supposedly supposed to flip it over, it just didn't have enough force to contact on there. So, these contacts through here are okay, but I reckon that is that is what happened. Now, if

**Dave Jones:** we try and place that in there, obviously that was sitting in there like that. So, yeah, if you turn in one direction, it's just it's just there's something that goes in there, the shape of that, and that's just going to go boom boom boom

**Dave Jones:** as you go in one direction, and then boom boom boom like that as you go in the other direction, and obviously that was not enough force. There was not enough contact on there cuz that that arm's intact, everything's intact. So,

**Dave Jones:** you know, I I expected some sort of like surface contact thing like you'll get like rotary encoders, surface contact, but this one it I you know, it's kind of clever, but maybe maybe they're just not reliable. And like does anyone else use

**Dave Jones:** this method or is it patented by this company? I don't know. Why is this not more popular? I I don't know. Well, the phasing coder thing uses less pins, but like you don't have to have the double throw

**Dave Jones:** um thing. Yeah, and there was this in here which unfortunately I never saw where that got to, and there's another contact which has fallen down in there. So, I'm not sure how that worked. Ah, that's okay. That's a

**Dave Jones:** spring. That's the spring. Okay, so the spring sits in there. It's all fallen out. This is how the indent system works. That obviously sits in there somehow, metal in here, and they're all nicely gold plated, and you know,

**Dave Jones:** they're not going to like there's no wear on that. No, that looks pretty good. You know, it doesn't look to be any major wear on that, so anyway, that is interesting, huh? Cuz this is called an angle pulse encoder. So, I

**Dave Jones:** guess we'll call it an angle pulse encoder, right? It's very simple and I like it. Like, there's no like surface contacts and you know, cuz the usual encoder has a brush on a like a contact wiping over a wiper going over a surface

**Dave Jones:** contact. And this one's not that. And by the way, for those who want to know, yes, you can actually see through this thing. So, you can actually put a cleaner through and no, cleaner didn't help me in this regard. There was this

**Dave Jones:** bar here, so I'm not sure what that's doing, where that was. Maybe that was cuz it seems too long to go as part of that. So, I'm not sure where that actually, I don't know. Leave it in the comments if you got an idea

**Dave Jones:** where that one went. All right, so I've put the shaft back in here and this is seems to be how it works. It looks like this indent here uh keeps a force on this plastic bit. So, that then goes into the shaft.

**Dave Jones:** So, I'll try and turn it at the same time. Sorry, this is not easy, but I'll try and keep a hold on this and you can see it. It's not very good, but you can see each time it clicks

**Dave Jones:** over like that, it pushes it in and pushes the the contact across that outer post and then when it slips back, it the springiness will bring it back like that and it will contact the other one. So, effectively, like that's the normally

**Dave Jones:** closed one and that's the normally opened. And it's just, yeah, the slippage in the thing like that. So, it's not like mine wore out due to like just the wearing down of the teeth in there, the cogs. But, yeah,

**Dave Jones:** it's I I can only presume mine failed because of the like the springiness in the metal just eventually went. So, you can really see, hopefully in this like how the tolerance in this thing really matters. So, maybe that's why I

**Dave Jones:** seemingly nobody actually uses this anymore because well, it's I don't know. Leave it in the comments down below if you know of one of another encoder that still uses this rotary pulse uh encoder mechanism cuz it's really quite clever, but um yeah, I I just

**Dave Jones:** think yeah, the devil's in the devil's in the manufacturing detail. And oh, yeah, that is that contact there now? Benter, is it supposed to be like that? I don't think it was that at the front start of the video, was it? Oops.

**Dave Jones:** Something's But, yeah. Yeah, this is really clever, isn't it? It's like the slippage in the in the cog once it once forces over to the contact and then once the tooth rotates past that bit there, it slips back out and and it contacts

**Dave Jones:** back. So, you get a brief contact over there and then it slips back to the normally closed and so on and so on. And it only goes in the one direction. If you go in the other direction, of

**Dave Jones:** course, it mainly swings over this side. It's pretty clever, huh? Huh. It's quite It doesn't have to move much, right? But, it's rather clever. But, yeah, you can probably see how this is a little bit dicky, maybe, if you

**Dave Jones:** don't really design and manufacture it absolutely perfectly. So, I don't know. Leave it in the comments down below if you think this is brilliant. And uh I think it's quite uh clever, but reliability compared to a regular uh

**Dave Jones:** wipe rotary encoder, I don't know. Uh leave it in the comments down below. But, anyway, hope you found that interesting. That's an angle pulse encoder. I bet you've never seen inside one of those before. That is That is rather unusual. Yeah, as I said,

**Dave Jones:** leave it in the comments down below if you know of one that actually works with this dual um single pole double throw thing instead of like a phase uh wiper contact thing cuz it it'd be easier to decode software wise, I think,

**Dave Jones:** um than a regular rotary encoder, a regular quadrature rotary encoder. But, yeah, I I just think this is neat. It is neat. It just failed on me. So, yeah, this one uh completely come a gutser. And um it's lucky I was able to find a

**Dave Jones:** replacement. Otherwise, yeah, I would have had to cuz the software would have been expecting the the double pole action in there. So, I would have had to like have a little micro that converts a regular rotary encoder or a toggle

**Dave Jones:** switch into that action of flipping de- de- de- depending on which direction you're moving it. Uh it wouldn't have been hard, but you know, it's it's just something that I didn't have to do in the end cuz I was able to get a

**Dave Jones:** replacement one. And I got a spare one as well. So, I've got two replacement ones in the mail. So, hopefully, um that fixes it. But, there you go. That's an angle impulse encoder and how it works. I think that is quite novel. So,

**Dave Jones:** anyway, hope you enjoyed that. If you did, please give it a big thumbs up. As always, toss some comments down below. EEVblog.com uh website and forum as well. Catch you next time.
