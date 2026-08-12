---
video_id: sdLm08zfE4g
title: EEVblog #1361 - Dodgy Tactile Switch TEARDOWN
url: https://www.youtube.com/watch?v=sdLm08zfE4g
source: youtube-asr
timestamps: {"0": 1, "1": 11, "2": 23, "3": 44, "4": 60, "5": 83, "6": 91, "7": 103, "8": 113, "9": 123, "10": 131, "11": 148, "12": 158, "13": 172, "14": 182, "15": 198, "16": 208, "17": 218, "18": 232, "19": 242, "20": 253, "21": 268, "22": 288, "23": 303, "24": 315, "25": 326, "26": 341, "27": 361, "28": 376, "29": 404, "30": 421, "31": 436, "32": 462, "33": 473, "34": 492, "35": 507, "36": 519, "37": 525, "38": 538, "39": 547, "40": 557, "41": 570, "42": 579, "43": 589, "44": 599, "45": 612, "46": 622, "47": 642, "48": 650, "49": 665, "50": 675, "51": 685, "52": 698, "53": 710, "54": 725, "55": 738, "56": 749, "57": 760, "58": 773, "59": 785, "60": 795, "61": 814, "62": 826, "63": 836, "64": 852, "65": 859}
---

**Dave Jones:** Hi, quite a few people wanted me to do a teardown of this little pain in the ass button that failed on my aircon system. I'll link in the video if you haven't seen it.

**Dave Jones:** It was rather interesting and it has a dodgy contact in it. It varies anywhere from like, you know, a couple of like it should be like almost zero ohms really.

**Dave Jones:** But it varies anywhere from a couple of ohms even if you press it really hard up to many hundreds of ohms and it caused a major problem if you design your switch matrix in such a way that it uses a single pin on your microcontroller and then analog to digital converter switches in different resistance values in the pull-up resistor in a resistor divider in this case.

**Dave Jones:** And it it's a neat way, of course, to sort of an age-old way to get multiple switches onto a single pin of a microcontroller or over one line in this particular case and like you can do it over one line and stuff like that.

**Dave Jones:** Anyway, it's a neat way to do it, but the downside, of course, is that if this switch develops any high internal resistance due to wear, corrosion, or whatever, then you're going to come a cropper and it can in this particular case on my aircon unit, this is the on-off button that failed and it actually because it failed at a couple of hundred ohms in many cases, it

**Dave Jones:** would actually simulate and appear as though other buttons were actually being pressed. So I'd press the on-off button and my aircon would change from heating to cooling mode, for example.

**Dave Jones:** And yeah, it's just a really fascinating insight. So a lot of people said they wanted to see inside this switch. Now, I don't know. So let's zoom all the way in with my Takano.

**Dave Jones:** And here it is. Pretty good. This is not digital zoom. This is all optical zoom, by the way. Um and a lot of people wanted to see inside this.

**Dave Jones:** I'm not sure how much we're actually going to be able to see in inside this thing. That on the side is probably my soldering iron getting the thing off, so don't worry about that.

**Dave Jones:** But yeah, it doesn't look the best, is it? It's just a It's just a one-hung low job, I think. So, I wouldn't be writing home to my mom about that.

**Dave Jones:** But anyway, I thought we'd uh tear it down and see what's what. We may or may not see something. I suspect it's just corrosion. A lot of people, because you know, pesky oxygen in the air and all that sort of stuff, a lot of people uh said that oh, just squirts and squirts and contact cleaner in there and it'll last for another decade.

**Dave Jones:** Yeah, if they're corroded, not really. It might fix it for, you know, a little while. Um but then you're eventually going to come a guts up. So, anyway, um I'm not sure.

**Dave Jones:** I've never opened one of these tactile switches. Um So, I like maybe can we get in there and maybe slice off Is that a way to Is that a way to do it?

**Dave Jones:** I don't know. If you've got a full proof way of doing this, please let me know. Um I'm winging this one. So, let's let's zoom out a bit there.

**Dave Jones:** So, if my blood gushes out of my finger, you'll be able to see it. So, let's go. This I got my spongy mat under here. You can really see my This is the one that came with my Takano microscope.

**Dave Jones:** I assume it's like ESD Well, it does have an ESD point on it, yeah. It's definitely an ESD mat. Um but I haven't actually got it connected. Mm, naughty Dave.

**Dave Jones:** Anyway, uh Let's Okay, so Oh, there we go. There we go. It just popped off. Right, I thought I'd have to force that. But nope. So, oh, there you go.

**Dave Jones:** All right, this is This is going to be interesting. Oh. Let's lift that up. Oh, yeah. Oh, yeah. That looks like corrosion, doesn't it? Oh, that's the That's the snap dome on top sorry.

**Dave Jones:** No, that's the that's that's the snap dome on top. There you go. So, it just looked like rust, but anyway, I've never seen a Is that an accurate color?

**Dave Jones:** It looks like yeah, that's an accurate color what you're seeing on camera here. It like it's hard to get the lights right and everything. It's all to do with the exposure and lights and whatnot.

**Dave Jones:** Anyway, that yeah, the plunger yeah, that'll have a little knob in there and well, let's see if our disc falls out. Yeah, yeah, yeah, there we go. There we go.

**Dave Jones:** That is our corroded disc. You can definitely see that there is corrosion on both the snap dome. Yeah, you can really see the corrosion in there where it makes contact with the center of the disc, center of the snap dome makes contact.

**Dave Jones:** So, if we flip that over, that should still that should still give us a snap. Yeah, there we go. You can see it deform like that. That's why they call them tactile switches cuz they're based on these tactile domes.

**Dave Jones:** They can be different shapes. They don't have to be round like that. I've done videos going through I've got a kit of different ones. There we go. That's the best zoom I'm going to get on the Teegano microscope.

**Dave Jones:** Not bad considering 30 cm working distance of the working distance of this thing. You can see the bottom contact in there. The side the edge contacts over there which connect to the dome.

**Dave Jones:** I don't think they're the issue cuz the side of the dome looks okay. So, like the the edges are probably all right, but yeah, there you go. Center of the dome and that switch.

**Dave Jones:** So, that's causing hundreds of ohms. Um even if you like you press really hard the best I could get on it was like a couple of ohms I could not where is a brand new freshy you know it's down in like that tens of milliohms range right there they're really quite low but yeah.

**Dave Jones:** There you go. So I I was surprised that we actually got to see something decent in that not much in it is it that's a real cheaper construction I might be interesting to crack open a different type I can do that.

**Dave Jones:** All right let's get my kid of switches here I can assure you these are the cheapest possible one hung low quality cuz these are like a kit that came on eBay for like you know two bucks delivered for the whole kit just worth having right so these will be the absolute crappiest quality I got the same size switch there so let's chop this one open and have a look so I wouldn't expect

**Dave Jones:** this one to be any better at all it just looks just looks a bit fresher that's all. There you go yeah it's still got you know like it's not going to stop any crap getting into it I don't know are any of your good quality ones any better?

**Dave Jones:** Does anyone know? Sorry I don't I probably I could probably get a good quality one if I look through some of my project kits like a known good quality Alps or something but there you go there you go.

**Dave Jones:** We're in there you go. It's got a different color snappy dome but it looks almost identical doesn't it? There you go oh there you go there you go that's inside a cheapy hasn't corroded yet does that have the ring and that one's got a center ring around the center contact like a ring around the center contact is that is that the what they use in as the

**Dave Jones:** contact in there? Whereas the other one didn't have that. Only had the single center contact. So, quite a significant difference. There you go. Quite a significant difference in the designs there.

**Dave Jones:** Which one whether or not they're using that center contact I could buzz that out. Yep. Yep. So, that that outer ring is actually connected through to that inner one and then these outer bits here will be connected to the pin over here.

**Dave Jones:** Yep. So, yeah. So, there you go. That's all one. So, I guess there's possibly two contact points on that one there. Whereas opposed to whereas we had a single one there and it didn't really have a dimple in it, did it?

**Dave Jones:** Didn't really have a dimple. It was just a flat contact. Whereas this one is actually look Oh, yeah. Oh, yeah. Look at that. You can see that's really poking up there and I can I I can feel that, too.

**Dave Jones:** Okay, yeah. That one's really got a raised surface. So, that one's very different. So, it's never going to contact that outer ring. So, I'm not sure what's doing there.

**Dave Jones:** So, yeah. There you go. There's a significant difference between those two designs right there. And yeah, that's corrosion. I'm not sure you would get rid of that just by spraying some stuff in there.

**Dave Jones:** It'd probably help, you know. You know, needed to get out of trouble. Spraying it with some gunk and it'd easily get down the shaft or in the side or whatever.

**Dave Jones:** It's probably easier just to go down the shaft really and then squirt the whole thing. That'd help. It'd get you out of trouble for a bit, I suspect. But, not going to get that off in a hurry.

**Dave Jones:** Still going to be there. So, yep. That is corrosion, I suspect. Is that just poor plating? I don't know. Any plating experts out there? Any metallurgists in the audience?

**Dave Jones:** There's always someone who knows. What does that look like? Is that like a coating? I I obviously there's some wear issue there. Check that out. That's a good shot.

**Dave Jones:** Some wear issue, but yeah, those larger patches on the side, they definitely look like corrosion, don't they? So, please leave it in the comments down below if you know about your metals and your corrosions and stuff.

**Dave Jones:** Okay, I do actually have a no-name brand here. We've got a C&K, one of the uh best brands out there, but this is one of their like low-end ones, I think.

**Dave Jones:** And uh looked up the data sheet uh for this, and it they don't specify the material on it. You know, it's got 100,000 lives li- switch actuations or whatever.

**Dave Jones:** Um 100 milliohms initial on resistance, so it's nothing special. I think this is just their bare-bones, but it is a C&K. So, let's crack open a C&K, shall we?

**Dave Jones:** Yeah, it looks very similar, doesn't it? Like the construction is exactly the same, but the inside could differ substantially. So, but I suspect not, you know. Probably just got a you know, uh phosphor bronze contact or something like that plated.

**Dave Jones:** And uh silver, of course, is a common uh That That one's just not That one's not popping off without a fight, is it? All right, there we go. So, anyway, usually they're like a stainless steel top.

**Dave Jones:** Um you can get uh stainless steel material switches. And there you go, that one could be a stainless steel, but it looks very similar to the one we had over here, does it?

**Dave Jones:** Uh yeah, can't see. Huge. So, that Is that like a nickel plate? Or is that like a brushed stainless? I'm not sure. I'm not sure, cuz it doesn't actually tell you.

**Dave Jones:** So, there's your There's your dome, and there's your contact. They've just got Oh, that's a bit different. It's got a split in it. Look at that. It's got two contacts.

**Dave Jones:** That's interesting. So, there you go. So, that would likely be a silver plated Yeah, I That That That looks silver plated to me. But once again, any metallurgists out there can tell just by looking at it.

**Dave Jones:** But of course silver is silver corrodes. Um So yeah, but that that's interesting. See that's got like a jewel you know, I call that a jewel wipe kind of contact.

**Dave Jones:** There's nothing else in the dome. The dome is just the dome. There's no like little nipple in it or anything. I like a good nipple. And of course, you know, I changing the geometry of the dome and everything changes like the tactile force and the tactile feel and you know, everything.

**Dave Jones:** There's actually performance curves you can get a good good data sheets for real uh high-end switches will give you like the performance curve. You know, if you go get like your snap tron domes and things like that.

**Dave Jones:** They're for as I've shown in previous videos, they're like fully characterized and stuff. But here you go. That's inside of CMK. So uh Interesting. That's at least three reference points for you.

**Dave Jones:** I think I like, you know, the CMK looks the better I mean that contact. Like just having the jewel contact in there. I can really feel that. You can see that raised up.

**Dave Jones:** Um I really like that one. That's really nice. Um Although this one in the eBay cheap I mean this eBay cheapy it looks that you know, it it just the plating on that looks cheap, right?

**Dave Jones:** Looks cheap as compared to the CMK one. Right? Look at that. CMK on the left, eBay cheapy on the right. It's got all sorts of hairy scary stuff inside the eBay cheapy, doesn't it?

**Dave Jones:** Doesn't look that great. So But you know, that one's raised up. It's Oh, it's actually yeah, it's got a hole in the middle. You can really see that now.

**Dave Jones:** That's pretty good. Wow. Anyway, there you go. That's the difference. Any of you uh switch aficionados out there who are really into this sort of stuff, please leave it in the comments down below what your opinion is of the three switches there.

**Dave Jones:** There you go. Switch aficionados, let us know your thoughts down below. C&K, eBay cheapy in the middle, and then on your right you've got the the failed corroded one with the couple hundred ohms.

**Dave Jones:** But that's you know possibly the end life of most if you get like a silver plate or something like that. Unless you get like a high quality uh gold uh plate one.

**Dave Jones:** But yeah, it's silver corrodes, you know, nickel I guess corrodes as well. You get nickel plating ones and stuff like that. So yeah, sure there's lots of switch aficionados who'll fill us in in the comments.

**Dave Jones:** Anyway, hope you liked that video. If you did, please give it a big thumbs up cuz that was rather interesting. So thanks to everyone who suggested I do that.

**Dave Jones:** I thought it'd be boring. It's not. This is interesting, damn it. Catch you next time.
