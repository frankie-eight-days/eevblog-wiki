---
video_id: IoRks5bJw8Y
title: Brymen BM786 Switch Fault Investigation
url: https://www.youtube.com/watch?v=IoRks5bJw8Y
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 36, "3": 51, "4": 71, "5": 90, "6": 107, "7": 126, "8": 140, "9": 155, "10": 175, "11": 190, "12": 209, "13": 225, "14": 240, "15": 268, "16": 285, "17": 302, "18": 316, "19": 336, "20": 358, "21": 376, "22": 390, "23": 410, "24": 427, "25": 451, "26": 473, "27": 491, "28": 512, "29": 530, "30": 550, "31": 573, "32": 588, "33": 606, "34": 621, "35": 639, "36": 654, "37": 672, "38": 696, "39": 726, "40": 744, "41": 762, "42": 783, "43": 813, "44": 837, "45": 852, "46": 870, "47": 882, "48": 894, "49": 909, "50": 933, "51": 948, "52": 963, "53": 984, "54": 1002, "55": 1026, "56": 1044, "57": 1062, "58": 1077, "59": 1095, "60": 1113, "61": 1131, "62": 1152, "63": 1170, "64": 1191, "65": 1206, "66": 1227, "67": 1245, "68": 1272, "69": 1302, "70": 1323, "71": 1353, "72": 1374, "73": 1392, "74": 1410, "75": 1425, "76": 1443, "77": 1464, "78": 1479, "79": 1497, "80": 1515, "81": 1530, "82": 1557, "83": 1578, "84": 1599, "85": 1617, "86": 1632, "87": 1650, "88": 1665, "89": 1680, "90": 1698, "91": 1710, "92": 1725, "93": 1740, "94": 1755}
---

**Dave Jones:** Hi, I thought I'd take a look at a couple of returned BM786 multimeters here. Let's have a look, here we go. Two of them have been returned, I've been selling it for, I don't know, three or four months, maybe now, something like that.

**Dave Jones:** And I believe I've had three faulty now. And I got two of them back, but two of them had the same fault, apparently. In that, it seemed to be something dicky with the switch, perhaps. That'd be my guess, it was like, you know, the symptoms were, like you put in, this one in particular,

**Dave Jones:** you put it in Ohm's, oh, there we go, forgot to change channel. Put it in Ohm's diode mode, and it would, like, flicker around and stuff, and if you moved the knob, it'd, like, come good, and then it would play up and all sorts of things.

**Dave Jones:** So that indicates a switch fault in the multimeter, because a lot of a multimeter's functionality is, it comes from the switch. I mean, it does an awful lot of stuff, the mechanical contacts, they can get dirty, they can, you know, lose their springiness, there could be some issue with the spring at manufacturing.

**Dave Jones:** You know, they're kind of complex little mechanical doodads, and they're not easy to get right, switches. So, you know, if something's playing up with your multimeter, take it apart, take apart the switch contacts, have a look, maybe clean up the contacts, and, you know, things like that, have a look at the springs under a microscope or something,

**Dave Jones:** you just, you know, see that everything's kosher, that there's good downward pressure on them, and all that sort of jazz. So, anyway, I, like, one, I thought, okay, you know, it happens, two, there's probably something in that, and this third one, I can show you, here, the faded digits.

**Dave Jones:** And you can certainly see that straight on here. You can certainly see the digits up here have faded. It's only these ones, and it's not so bad on an angle, looking down like this, so it's not so bad, you can probably see that there,

**Dave Jones:** you know, in that B cam shot, you know, it looks really, you know, it looks pretty good. But you bring it up, and then you can really start to, really start to see it. So, yeah, there you go. So that one, yeah, definitely faulty,

**Dave Jones:** so I just shipped a replacement one. Yeah, you can still see that one faded in there. So there's obviously something wrong with, like, the drive on that one. So, could there be, like, a failed cap in one of the drive caps, charge caps, or something like that?

**Dave Jones:** For the LCD? Something like that, perhaps? But I'm more, actually, concerned with this one here, actually, with the switch. Right, so this one here, with the switch contacts, was reported as, like, flickering between ohms and diodes and stuff like that, and only, like, after a minute it would settle down, something like that.

**Dave Jones:** I'm not seeing this, I got it out of the box, and it's all come good, fresh batteries in there, so it's not a battery issue. But I have been able to make it... Oh, there we go, got it. See? I have been able to get it to reset

**Dave Jones:** by doing, hey, by doing, like, just, you know, wobbling the switch there. So, yeah, I think it's a switch contact thing. And I have not been able to reproduce that with any other ones that I've got here in the lab. So I've been dicking around with them, and maybe...

**Dave Jones:** So it's not a systemic... I don't believe it's a systemic problem. Right, and push down on that, maybe try and pull it up, and... Nah, yeah, so I don't think it's a systemic switch problem. I think, possibly, someone at the factory just, you know,

**Dave Jones:** because it's a manual process, assembling these switches and screwing them into place, maybe someone forgot a screw, or something like that, or, yeah, something's gone wrong. So, anyway, there definitely seems to be something... Yeah, yeah, there we go, I'm making it. Sometimes I'm able to do it, sometimes I'm...

**Dave Jones:** yeah, there we go. It's doing it with regularity now. Yep, yep, so that's... it's gotta be a switch contact. Yeah, alright. Context. So let's take this sucker apart, and let's have a squiz. And, yes, Breidmans aren't perfect. I've been selling the BM-235, I've sold countless, countless thousands of those.

**Dave Jones:** And, yes, there is a failure rate, I don't... I should keep better track of these sorts of things. But it's certainly not zero. You know, it's nothing to worry about. It's kind of like normal sort of failure rate you'd expect, even if they're 100% tested at the factory.

**Dave Jones:** And everything else, you know, stuff can fail. Things go wrong. I believe we've had a few... I've done a few videos over the years of BM-235 failures. We've had a couple of, like, chip failures, where, like, it's the main chip that's failed. So some sort of, like, silicon migration issue.

**Dave Jones:** You know, something like that, perhaps. That's, like, caused the main chip failure. So there's nothing we can add. That was confirmed by Breidman, that it was a chip failure. So I believe we've had quite a few of those over the years and stuff like that.

**Dave Jones:** And, but with a report of two of these having what appears to be, based on the symptoms, the switch contacts, then, yeah, I mean, I've still sold, oh, it's probably five... Oh, how many? Yeah, no, I've probably sold like 500 of these already.

**Dave Jones:** And yeah, so we need to get in there. A few screws down in here. So yeah, with any meter, you expect a natural... Oh, jeez, that's tight as a nun's nasty. That is... what the... That one is a... that's terrible. It's really tight.

**Dave Jones:** So anyway, you can see that the switch here actually has four spacers on it, and they're actually screwed into the bottom side. Actually, what I'll do, before I do that, should have done that with the board screwed in. I'll just see if that...

**Dave Jones:** Does that wiggle, wiggle, wiggle, yeah, at all? I'm just... I don't know if that play is normal. I'll have to get another one to see, but I don't know. So anyway, I need to get in there and check those four screws, that's for sure.

**Dave Jones:** Need the fuse out. Oh, wow, these screws are so tight. Oh, springy. Okay, what I want to do on these screws here... Okay, what I want to do on these screws here... See these four screws? Well, they haven't forgotten one. So that's all right.

**Dave Jones:** Just having a look here. I'll see... oh, that one! That one in the back corner there. My imagination, or is that one not... Nah, I think it's just the shape of the screw. I thought that looked like it was a bit off. But, no.

**Dave Jones:** Okay, let's undo that. Wasn't the tightest, but I don't think it's a... I wouldn't have said it was loose. There we go, no switches falling out. Right. So let's have a look at the contacts down there. They look all right, don't they? There's no hair.

**Dave Jones:** No production hair. Which happens, you open up products and you find hairs in production. Doesn't appear to be any fingerprints or anything like that, but it appears, you know, it seemed like it was something, like, it wasn't just a bad contact. It was, like, physically not robust.

**Dave Jones:** So, I don't think it's... So I wouldn't expect to see anything there on the actual, like, you know, I wouldn't expect it to be like a contamination thing, really. And these wipe contacts, they're going to be fairly good. Wouldn't be concerned with those.

**Dave Jones:** It's just the pressure, due to they've engineered it, so that it contacts, it's all integral. Kind of like that approach. It's pretty good. And they've got, I like how they've got alignment posts here as well. Here and here, which go through a hole in the board,

**Dave Jones:** which just help align the thing. I guess that play there is normal. I think it would be. Make sure that goes back in. Part of our space in there for the switch. So, I don't know, that looked pretty good. I don't find a problem with that at all.

**Dave Jones:** So if I put it back together, and it works, and I can't force a fault on the switch, then I'm just going to say, well, maybe the screws just weren't tight enough. There we go, I've done that nicely. So maybe, that one in that corner there, it didn't feel all that tight,

**Dave Jones:** but it should have been enough. It felt like it was enough, but I could certainly tighten it up more. Maybe that's it. I'm going to give that a good extra twist on the end there, to get that back in. Extra little twist. I reckon that's all it'll take, although if you had three in,

**Dave Jones:** you would think that'd be enough. The other one would have to be left out, or be completely loosey-goosey. Oh, no, no. I can feel that. Don't know if you can see that. But, I mean, I've got to put a lot of pressure on it.

**Dave Jones:** But, you know, if I put pressure on that, it goes through, it moves through. See that? So, the whole mechanism does work. So, okay, I'll retract that comment. I think you do need all four nice and solid. One of them's probably enough to come a-gutza.

**Dave Jones:** But apart from that, like, you know, I wouldn't expect anything else. I'm sure it's a switch thing. I'd be stunned if this wasn't a switch problem. Like, it's not going to be anything else, because it wasn't like a measurement thing. It was, you know, when a metre's acting up dickily like that,

**Dave Jones:** bet your bottom dollar that it's a switch is going to be the main culprit there. Little pro-tip, doing self-tapper screws like this, just turn it back until you find the point where it drops into place. You can't get it, this one's probably too small.

**Dave Jones:** Oh, there we go, just got it. And that will line up with the existing thread. It's better with like the big self-tappers you get in like the Flukes and stuff like that. So you just wind it back half a turn, like, well, wind it back a full turn until you find that

**Dave Jones:** where you can feel it go in. It's all about the feels. It's about the only time that it's feels versus reels. But the feels are reels, in this particular case. They go in a lot easier than they came out, let me tell ya.

**Dave Jones:** That's what she said. Only problem with the BM 786, it's a great metre, but you do have to take it apart to change the fuses. So, that's a bit of a bummer. Give that screen a wipe-a-dip. Put my grubby mitts on it. Let's go, here we go.

**Dave Jones:** Oh, no, I got it to do it. Nup, look. Nup, there's something else. Nup, yep, there you go. Wow, okay. That's interesting. So it's a... Is there some production tolerance issue? Like, there could be, you know, some of the plastic mould in for the switch thing might have came out of the mould

**Dave Jones:** wrong, and there's just no fixing it, you know. Or there's, you probably could fix it if you spend ages trying to figure it out, but it's obviously the switch contact. Now I can't do this on any other metre. I cannot do it. I don't know, if you've got a BM 786,

**Dave Jones:** give it a go. Put it in own's position and try and give it a wiggle, wiggle, wiggle, yeah. And I've tried other metres as well, and I can't get it. Can't get it. So, yep. Yeah, there you go. Well, yeah, no, it's exactly the same.

**Dave Jones:** That seemed like the same amount of effort required to do that as last time. So, it wasn't the contacts. It's not contamination. It's, you know, people say, oh Dave, you should have wiped the contacts. It's like, no, there's no point. Like, there's enough pressure

**Dave Jones:** coming from those. You could have, you know, it really doesn't matter. They should be like self-wiping. Effectively. So. And, can I get that to happen in a oh, yeah, there. Can I get that to happen in millivolt position? I can hear, I don't know if you can hear that.

**Dave Jones:** Yeah. Yeah, nah, there's something wrong. I do not get the same there's no noise. There's no noise when I do that, and there's very little play in that switch. This one, yeah, it's got this noise. And there's larger play in the switch. Yeah, yeah, I just got it resetting.

**Dave Jones:** Just got it resetting based on the millivolt, yeah. I'm getting really dicky with that switch contact. So that's interesting. I don't know. Yeah, now I can hear that. I think that that was there before as well. Yeah, I'm just making it come and go.

**Dave Jones:** Ha ha ha. Wow. Yeah, there's something horribly wrong with that switch. So, but as I said, like it doesn't take much in the tolerance of the plastic moulds and stuff to actually be out on these things. And it's just, you know, the plastic kind of moulds all the time,

**Dave Jones:** and if it's out by a slight bit, that could, you know, cause other problems. I mean, what I could do is I could get a donor, you know, a known good donor unit, and I could simply transplant. The good thing about that mechanism, it's all in one.

**Dave Jones:** So I could transplant that over, and I'll see if it has that play in it and see if that fixes it. And if it does, then you know there's some, like minor, there's gotta be minor tolerance issues because it seems to work, whereas the

**Dave Jones:** whereas the viewer who had it, they said it was just sitting there and it was flickering between ohms and diodes and stuff, and I totally believe it. And I shipped a new one, and he said yeah, it works fine. You know, but it's had to ship halfway around the world

**Dave Jones:** back to me, so yeah, that's interesting. Okay. There you go. Hey! It's permanently off! Yay! I got it! I got it! It's permanently off! Ah, look! Look at that! Look at that! I just, I switched it off permanently. Am I able to do that again?

**Dave Jones:** Because the power contacts are part of, it's one of the wipes inside the switch, is the actual power contact. It's obviously, so you can figure out which actual track was doing it and stuff like that. Okay, so what I'm gonna do now is actually swap this switch mechanism

**Dave Jones:** that doesn't have an issue on the LCD, faulty LCD one over to here. I'll simply just transplant the whole thing over. So that will tell it, if it comes good, then that will tell us if, like there's something inside there, be it, you know, like a dodgy moulding

**Dave Jones:** or some other, you know, alignment type issue to do with the entire assembly. So I really don't believe it's the contacts or anything like that. So anyway, let's transplant this one over to here and see what's what. So anyway, alright, so I'll put it like that and I'll know

**Dave Jones:** to flip it back that way. So I've got to make sure I don't get this mixed up. Alright, here we go. Lift that out of there like that. And we'll flippity-doo this one over. And yeah, there's like, I'm not seeing anything on the contacts.

**Dave Jones:** I'm pretty darn sure it's nothing to do with the contacts down there. So, as I said, you know, generally, multimeter switches are pretty good at self-wiping, because they've got that contact pressure coming down. So generally, that shouldn't be a problem. Although the interesting thing is, like, looking at this

**Dave Jones:** switch mechanism here, like it could be a height thing of this. Like there's not really any, maybe even the standoff or something like that. I can just imagine that if this is like slightly higher, or like any of these are slightly higher, even these supports here,

**Dave Jones:** although that's overcome by the screws I guess, but yeah, if there's a slight, or it could even be this is slightly, like the thickness is slightly out or something like that. So there's not really much else that can go wrong. Maybe the you know, oh there could be, but if you had

**Dave Jones:** say if it was thicker than normal, and you had like extra thickness in there, it'd only push the contacts it'd only put more force on the contacts onto the PCB. So yeah, there's a few ways it can go wrong, but anyway, we won't care about the details.

**Dave Jones:** All we care about is does this make a difference? I'd be surprised if this doesn't work, because then we're talking about contacts on the PCB or some other thing. I don't believe it's going to be an electrical problem, because like we're pushing on those contacts

**Dave Jones:** and it comes a gutter. So let's put that back in. Okay, so that's back in, so I shouldn't need to put the screws back into that board just to get it, because the pressure of this board going down should make no difference to that

**Dave Jones:** in there. So I can just simply whack this back on. Ow. No, you do have to, hang on, that's not, why is that not doing anything? Yeah, I really, yep, you do have to screw the board down. Oops. I can't see why you have to screw that board

**Dave Jones:** down. I probably, I don't know because it pushes down That's kind of weird. Hmm. Surely I don't need more than two screws. These are a bit tricky to put back together. This top bit doesn't want to go in. It's really rather annoying. Got a snappity doodah

**Dave Jones:** into place. But why is that there's no snap in that range switch? What the? It's almost as if it's not making contact. What's going on? This is pushing into there. There's no play in that. That should go into the center of there. There's the

**Dave Jones:** indent mechanism like that. That should rotate and snap. Maybe I didn't get that in when I put it in. What? Somehow that shaft isn't going in. You hate it when your shaft doesn't go in. That looks like it matches up absolutely perfectly with the

**Dave Jones:** alignment there. That looks perfect. There we go. There we go. Don't know why it didn't go in before. But now this top bit won't go in. Arrgh! How do they assemble these at the factory? There's got to be a trick to this. I think my career aspirations at the Breiman factory

**Dave Jones:** are all but shot. Aha! Was it? Wasn't those screws, was it? Let me take those out completely and try that. Was it? Yep. Yep. That was it. It was the bloody screw. Wow. Okay. Okay. There you go. Self-tapping screws. Oh, there we go.

**Dave Jones:** There we go. Got it. Got it. Alright. These screws are designed to be captive, so they're not designed to come out all the way like that. But the problem is is that if you treat them captive like that, then you can come a gutser putting it back together.

**Dave Jones:** There you go. Alright. Battery pack. I'll just do up these two screws here. Just for good measure, because it's kind of around where the switch is even though it shouldn't make any difference. Alright. We're on. Okay. Everything's hunky-dory. And here we go. Yep.

**Dave Jones:** Yep. Yep. Yep. As expected. It's fixed it. Yep. Which is good, because I would have been really surprised if that didn't fix it. So yeah. I think there's something fundamentally wrong with that. I mean, the spring contacts all look good. Hey! The spring contacts all look

**Dave Jones:** all look nice. It's not like one's bent or short or anything like that. They look really good, so I'd say yeah, maybe there's a slight tolerance difference with the plastics. Yep. Oh, hang on. Did that... Nah. Nah, I can't. Oh! I got it!

**Dave Jones:** Oh, no! No, I got it! Look! I'm able to make it do it again! What? Wow! Wow! Come on! Come on! What's going on? Well, that is most remarkable. Well, there's something oddball with that. Alright. What I'm gonna do Okay. Right. I had it there for a minute.

**Dave Jones:** Okay. I'm gonna put this one back into here, and see if we can reproduce the fault on the LCD one. I doubt it. Okay? So there's something with that board. Alright, so there's the LCD unit back together with the switch mechanism from the other meter.

**Dave Jones:** Of course we're still getting the issue with the LCD. I'm not really concerned about fixing the LCD thing. I might have a look at it if I've got some time, but anyway, let's go over to the ohms, and can we get that to do anything?

**Dave Jones:** Now the problem is, is that before, I thought that was fixed, right? So let that be a lesson to you. You can come a guts up with your, you've got your hypothesis on what's causing the problem. You make the chart like I thought, you know, it'd be in that switch contact

**Dave Jones:** like I came up with some ideas about the mouldings, you know, being slightly out and stuff like that. All valid, right? Really valid hypothesis, and then you, you know, make the change over to the different meter, and then you go, and then you test it for a bit, and you think

**Dave Jones:** winner winner chicken dinner, right? My hypothesis was correct, but then you keep testing a little bit more and nah, you find that you come a guts up. So just be careful of that. Oh, no, I think I pressed a button there. Oh, hang on.

**Dave Jones:** No, I was I thought I pressed a button, but I was able to get Oh, there we go! Got it! Got it! Wow! There you go! Talking about the hypothesis thing before, that I really have to be violent with this, it's really... Anyway, we

**Dave Jones:** are a long way, even with this meter, we are a long way from the reported fault of it simply just having the switch there, and it was just switching between diode and resistance and stuff like that. So maybe there was, it might have been, a loosey-goosey

**Dave Jones:** screw in there. Oh, see, no, this one this one I can make it do it really easy. So, yeah, this one is much much harder, but I am able to make it do it, eventually. Maybe. Now it's not going to happen again, right?

**Dave Jones:** So I, yeah, I don't know. Look, I'm going to have to call it quits for this video, because you can spend you can spend countless hours investigating something like this, you know, and without having you know, getting there and actually calipers and measuring all the plastic

**Dave Jones:** parts and stuff, you know, that's more something for the manufacturer to figure out. So I might send this video to Breiman and say, hey, you know, potential issue, I've had a couple of reports of this. Potentially be it a switch. See, oh, there we go.

**Dave Jones:** Wow. No, it just, like, what? What? There's something I could not make this happen before, so did something transplant over with that switch mechanism. It could be a combination of tolerances with that particular switch mechanism in here, and in the with, that came out of here, and

**Dave Jones:** this PCB, or something. So it could be tolerance stacking or some other weird, you know, aspect like that. So, anyway, that's that is fascinating. It didn't fix it and potentially, I've transplanted the fault over to this LCD one. Kinda. Sorta. Oh, yeah, there we go.

**Dave Jones:** Yeah, got it to happen again, but it's not the same failure Oh, they, yeah, we got it to repower. There we go. It's, oh okay There's some, there's gotta be some repeatability to that. There's gotta be some, you know, because I can go like that and not do it

**Dave Jones:** right? I'm putting a lot of force, oh there we go. But and yet others, times I put the, I'm just giving different force directions here. Use the force loop. But yeah, sometimes you can get it, sometimes you can't. But I could, for the life of me, I could

**Dave Jones:** not get it happened on this or any other meter that I had here. So maybe something has transplanted The only way to be sure is to like maybe thoroughly test a third control meter like, you know, bang it for hours and make sure you can't

**Dave Jones:** do anything like that. There's no issues and then transplant the switch mechanism again from this one over to a third one and then if the, you know, if the virus transfers from here to here to here then you know you've got something in those plastics or

**Dave Jones:** something to do with the contacts or whatever. So you can hopefully see how this could be a real pain in the butt to actually troubleshoot something like this. You know, you could spend days, weeks possibly investigating an issue like this. If you're a brimer, you know

**Dave Jones:** thoroughly test. You might get, you know, 50 units or something and thoroughly, you know, even have a jig that sort of jiggle, jiggle, jiggles them and like see if you can make it happen and then I don't know, get one of these and get the, you know

**Dave Jones:** try and find a faulty one and then try and make it, you know, extensively measure and compare those ones with your tolerances for your switches, for your they'd have a drawing, for example, that specifies tolerances for all the plastics and the moulds and the contacts and everything

**Dave Jones:** else and yeah, only a brimer would have that sort of data. So in theory I could do the thorough investigation myself, but it's many, many days of work I think to really get to the bottom of something like this and you may not.

**Dave Jones:** It may require a brimer to do it. Anyway, that is fascinating. So please leave it in the comments down below if you've had an issue with your BMR-786. If you can reproduce this thing at all. I don't want people to damage their meter.

**Dave Jones:** They've really, you know really banging the switch and stuff like that. I'm only doing it in the owns position. I'm just going to treat that as a reference. You might be able to, you know, make it happen somewhere else. I just don't know.

**Dave Jones:** Or whether or not, you know, that just happens to be a susceptible position based on, you know, whatever mechanisms going wrong here. But yeah, it's definitely a physical thing. And as I said, these switch, multimeter switch mechanisms are a little complex little beastie.

**Dave Jones:** And it's not always easy to absolutely get them right. So there you go. Catch you next time.
