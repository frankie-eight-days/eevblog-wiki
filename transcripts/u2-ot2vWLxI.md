---
video_id: u2-ot2vWLxI
title: 121GW Range Switch Cycle Testing
url: https://www.youtube.com/watch?v=u2-ot2vWLxI
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 31, "3": 49, "4": 64, "5": 79, "6": 95, "7": 109, "8": 124, "9": 138, "10": 154, "11": 167, "12": 178, "13": 191, "14": 206, "15": 218, "16": 236, "17": 250, "18": 260, "19": 276, "20": 303, "21": 320, "22": 338, "23": 355, "24": 369, "25": 386, "26": 401, "27": 420, "28": 434, "29": 447, "30": 456, "31": 471, "32": 481, "33": 491, "34": 504, "35": 516, "36": 530, "37": 554, "38": 571, "39": 585, "40": 602, "41": 620, "42": 642, "43": 662, "44": 682, "45": 699, "46": 716, "47": 731, "48": 746, "49": 759, "50": 774, "51": 788, "52": 804, "53": 823, "54": 839, "55": 854, "56": 871, "57": 888, "58": 907, "59": 921, "60": 937, "61": 966, "62": 980, "63": 1000, "64": 1017, "65": 1036, "66": 1052, "67": 1072, "68": 1091, "69": 1107, "70": 1126, "71": 1143, "72": 1160, "73": 1176, "74": 1209, "75": 1227, "76": 1248, "77": 1270, "78": 1292, "79": 1311, "80": 1332, "81": 1349, "82": 1367, "83": 1385, "84": 1400}
---

**Dave Jones:** Okay, we're going to do some more cycle testing, but we're going to do it on a production unit with the new shim provided by UEI. Yes, it does actually have a routed out little bit in there. It's actually very

**Dave Jones:** nice. Those little tooling holes there are designed to get the routed edges. Yes, it's made out of regular FR4 fiberglass and we're going to and that is going to sit Oops, sorry. We've got actually got this hooked up. I'll show you in a second.

**Dave Jones:** But actually just sits over Yeah, sits over there like that. And that just wedges in there nicely. And it goes back in along with the new knob, of course. And we've actually hooked up some wires here to the off position

**Dave Jones:** of the unit. So, when it's in the off position, we'll actually be able to measure the contact resistance here. But we've actually changed our jig over here to actually measure this. So, we're using an ADC with a with a parallel resistor in the

**Dave Jones:** divider resistor and then a parallel resistor just in case it opens and then we can calculate the actual contact resistance. What does our contact resistance go up to, David? About about 10 ohms. Anyway, we've tested it and our nominal contact

**Dave Jones:** resistance is about 0.9 or something like that. Um So, of course we expect that to vary a lot and change as we cycle through the automated testing. But anyway, we're going to try it with the new shim, get our automated tester and

**Dave Jones:** whack it in there. So, let's give it a whirl. All right, so I've got the new meter together with the new knob and the new white plastic spring indent thing in there plus the new shim, which is 0.5 mm

**Dave Jones:** thickness by the way for those playing along at home. And it's still indents, but it is not as clicky as it was before. Um it just it sort of changes the nature changes the feel of the rain switch. Some people will really love

**Dave Jones:** that new feel, others won't. Others might want a light clicky feel. Um anyway, we've got our contact resistance here now. Uh 0.9 ohms and that's not, you know, varying at all. That's uh rock solid. So, I I expect that, of course,

**Dave Jones:** to increase. We're consistently getting um under uh 0.9 and UEI have done some tests and they're consistently getting under the 1 ohm uh mark. But, yeah, anyway, so the plan is probably we'll run 1,000 cycles on this first, take it apart again, have a

**Dave Jones:** look at the contacts, and then if 1,000 cycles is okay, then we'll maybe do 5,000 or something like that. Do increments. We're We're not going to go bang for 25 or 50,000 cuz that doesn't tell us at what point um, you know, if

**Dave Jones:** any contact wear starts to happen. So, let's give it a whirl. Let's push some buttons randomly. This will take a little while to set up. Just do it. Still working on the software. Still working on it. Oh, the software's good.

**Dave Jones:** Oh, there we go. Software's good. Software's good. couldn't see it. All right. There we go. All right, we're going to set up 1,000 cycles. Here we go for it. 1,000? 1,000. Let's do it. Okay. That's the old meter. We're just going

**Dave Jones:** to give the test first. Yep. Yep. And for those who are wondering, yes, it does do a full cycle all the way with LBJ from one show that. end to the other. lift it up now. Oh, right. And

**Dave Jones:** There you go. You can have a look. Have a look. Now, that's right right over it there. On the dot. It's on the dot. There you go. And yes, we'll keep an eye on it. All right. Let it recharge.

**Dave Jones:** This is way too much fun. All right, so let's have a look at the this puppy after 1,000 cycles, which is 1,000 cycles one direction, of course. So, like one sweep one way, that's one cycle back is two cycles.

**Dave Jones:** So let's check it out. We cuz we didn't want to run the whole uh uh you know like 10 or 20,000 or something without knowing what it's like after a thousand and and got to remember also this one has been

**Dave Jones:** run like a couple of hundred at least a couple of hundred times in various other uh just you know test jig testing and things like that. So it's not it's not a particular as well as you know other

**Dave Jones:** use. So it's not a particularly virgin meter in that respect. But this is the first time it's been run with the uh the new shim. So which uh of course puts some extra pressure on the uh range switch. So

**Dave Jones:** let's get this puppy open. Come on. All right. Let's have a squeeze. Okay. And you would have seen in the testing that there was variation in the contact resistance but it basically didn't um uh fail. There were no opens or anything

**Dave Jones:** like that as far as we uh saw from the data. So There we go.

**Dave Jones:** Come out. Come out wherever you are. Here we go. It's It's got to be careful cuz we want to put this back in. And Oh, all right. Let me try and get this out. Okay, that was a poor effort but I got

**Dave Jones:** it. Oh, contact came out. That's not unexpected. But there's not much holding those contacts in. So let's flip this over and have a look at our contacts. I'll whack the macro lens on. Get that under the mantis, but uh

**Dave Jones:** there's some uh there's some kind of crud. Hang on, I'll put it under the uh Teegano. Some other stuff in that could be fiberglass. That's from just the inside raw inside of the ring, something like that. Let me

**Dave Jones:** get under the uh Teegano. Okay, there we are under the Teegano microscope. It uh it it probably looks worse than it actually is, but you can see all that um crud around there is this certainly the fiberglass that's uh come off

**Dave Jones:** the edge of the hole in there. So, it would have been better if that was plated, I guess, but after a thousand cycles, so it's pushed some of that crud into there, but it's not basically we're looking for really the metal is

**Dave Jones:** the stuff that uh really concerns us, and that's not those markings on the gold pad are really huge problem, especially when the contact resistance we've proven isn't really hasn't really caused much of a drama. There we go. It's maybe

**Dave Jones:** some plating starting to wear off the contacts, I don't know, but uh no, they're still looking uh really good nick. So, that combined with the board it's not it's not too bad. So, the the real test that we whack in we'll do like

**Dave Jones:** 10,000 cycles next and uh see what happens, but don't know there's nothing seriously bad there at all. The contact resistance is still good, I think. We haven't run the numbers yet, but I think it's still like always under

**Dave Jones:** 1 ohm or something. So, that's fine. Yes, sir. Yeah, it's going to stop at two, one.

**Dave Jones:** It finished. We yeah, we programmed it to get to uh 5,000. So, So, that's what? 9,000? I guess I now I guess we now have to look at the contacts, right? I've got to shoot a video. Should I do that live?

**Dave Jones:** Yeah, this is how I make sure there's no skip steps. This is the permanent marker on the shaft and the permanent marker on the plastic. Uh, it's pretty secure. This side is set to be secure. This side's set to

**Dave Jones:** uh, to slip like a torque wrench, so I can't, you know, I can't put too much force manually into the dial. So, to calibrate it, I just go whoop and then it moves all the way to one side and

**Dave Jones:** I'm not sure if people are hearing that, but yep. For those who didn't hear that, it's basically, as I said before, it's hooked up those wires are hooked up to the off switch position, which is actually the reset line of the micro. The micro the

**Dave Jones:** like the switch also holds it in reset. Um, holds the holds the micro in reset. So, and when you hook instruments up to it, or when you hook pull-ups and parallel resistors and everything else, it it just screws with

**Dave Jones:** the pull-up on the reset line and it doesn't switch on. So, anyway, still cycles. Now, I want to shoot this on a regular camera. Doing stuff in this lab is hard. There's so much crap everywhere and every video

**Dave Jones:** requires different positions for all for gear and cameras and whatnot. All right, here we have 133 again. We've got uh, we've done 10 9,000 cycles, I think. We did 1,000 and then we checked it and then we did 5,000, but we had to we had to go

**Dave Jones:** that night, so we we had to take the computer away, the logging computer. So, we took it away and uh, we came back today and we did another 5,000, so that makes 9,000 cycles and uh, we were measuring we had a few

**Dave Jones:** issues with the position of the meter in the jig and that was causing a real problem with our contact resistance measurement. Um so we've got some problem we're going to get some data that's corrupted. We were getting about

**Dave Jones:** roughly about two point, you know, two ohms, something like that contact resistance after you know, towards the end of that. So it was still going good. And one cycle of course is from one off position to the next. It's not cycled all the way back.

**Dave Jones:** So one cycle is from here over to here. So to go back would be two cycles. That's how we're counting. It's just how our jig how our how our jig works. So let's pop the pop the board out.

**Dave Jones:** There's our little shim. Ah, yeah, we've got some crustiness under there. So some of the fiber glass is Yeah, just worn off that. So guess that's to be expected. Maybe we could add some lube under there or something. I don't know.

**Dave Jones:** Oh, actually yeah. I see the the problem with fiber glass shim is going to be the fiber glass dust around the outside of that. So that's going to be a problem actually. So I'd expect this isn't going to be

**Dave Jones:** particularly clean inside here. Yeah, we didn't see that after a thousand cycles. So that's a It's not entirely unexpected. I didn't know they were going to do a fiber glass um shim.

**Dave Jones:** And I don't think I, you know, plastic one I guess would be better, but they were able to route out use the fiber glass to route out a little slot in it. It's actually rather clever.

**Dave Jones:** Oh, there we go. No contacts came out this time. There we go. I know. No, there's a bit of fiberglass around the outside. But apart from that, that looks Oh, that looks okay. So, those that wear looks bad, but the

**Dave Jones:** contact resistance is still great. It's still like a couple of ohms. It's really quite nice. So, that put a bit of spit on that. So, that's like I can just wipe that. So, it's actually um you know, those contacts are pretty good

**Dave Jones:** after 10,000. You can see in there that uh the trace between those two contacts is uh it's worn off the um the solder mask is worn through. But But that's a lot of cycles, right? And that's continuous back and forth, back

**Dave Jones:** and forth, you know. Um at a high rate. Some people say, "Oh, it's it's too We're We're doing it too fast and it's melting. You know, it's going to melt things and stuff like that." Um I don't know. I I didn't think it's that

**Dave Jones:** fast. I'm not And now we'll have a look at the contacts. So, you can't say I'm not doing not taking my chances doing this live. The contacts down in there aren't you know, they're fine. There's nothing wrong with

**Dave Jones:** the contacts at all. I don't I don't see that as a real issue. Let me have a look at that on the Mantis. Sorry, I'll go back. Yeah. No, it's contacts are good. Don't worry about the contacts. I think

**Dave Jones:** they're great. So, there you go. That was uh 9,000 cycles. Um so, the fiberglass shim is great. We were Yeah, about 2.7 ohms on the um on the switch. So, we can put that back together and measure it. So, if I

**Dave Jones:** do that, we effectively have the reset line. Actually shorting out the the reset line of the microcontroller. Wiggle wiggle wiggle wiggle wiggle, yeah. No. See? It's all hunky-dory. So, um yeah, it's all good. So, that's done 9,000 cycles now. So, apart from the

**Dave Jones:** fiberglass dust in there, um 6,000 yesterday. Oh, 6,000. We did another thousand. Yeah, you're right. It's 11,000 cycles. Thank you. There There you go, 0.8 ohms. I mean, that that's done 11,000 cycles. 11,000 cycles and we're on point 0.85

**Dave Jones:** ohms. And there's like, you know, if you wiggle it, like it changes a little bit, you know, as as you'd expect. But, uh and 0.9, that one's longer for some um has always been slightly higher for some reason in that position. Maybe it's got

**Dave Jones:** I shouldn't have longer tracks. The track tracks are only like, you know, shouldn't add much, but maybe it uses a different set of contacts or something over in that position.

**Dave Jones:** All right, we've got the um serial number 133. It's now done approximately 25,000 uh cycles with the new uh shim, and the contact resistance is still okay, but it's basically I would deem it to be failed now because it's

**Dave Jones:** um if we go into the diode test mode, um the knob has the problem. It will It will do it. Yeah, there we go. So, we've got that uh dicky contact again. So, but that's um our jig failed actually at uh 25,000

**Dave Jones:** cycles. We had a problem with the drive motor and everything else. So, I'm not sure if that's put any extra force on the switch or whatnot, but uh that's what we've done now, 25,000 cycles. So, let's have a look.

**Dave Jones:** Although, it has as an actual solution um it works it seems to work very well for the contact resistance and the of course the switch wobble is uh fixed and the intermittent rain switch I fix I think all those problems are now

**Dave Jones:** uh I think it does actually fix those. So, that's good. Okay. Let's have a look. Actually, not a not much more dust than previously. Uh similar. I'd I'd I'd call that similar. Shim of course is uh uh it

**Dave Jones:** seems to have worn on may maybe there was a burr of plastic or or something under there that Oh, no, it was at the holes. Yeah, it seems to have lined up with the holes to do that. So, that's

**Dave Jones:** that's interesting. Okay. Let's have a look at the contacts first of all. And the contacts are actually the contacts look very good and you can see the dust caked under there, but uh for 25,000 cycles those contacts look uh

**Dave Jones:** really quite nice. So, that doesn't seem to be a problem. Once again, it probably looks worse than it is with the dust. It's a problem, but the actual uh the contacts on the PCB still look okay. I mean, you know, it's had 25,000

**Dave Jones:** full cycles on it. That is quite quite violent. So, I don't have too much of a problem with that. Actually, with the actual wear on the contacts, it's you know, not as uh I mean, it's not perfect, but

**Dave Jones:** there we go. If we get rid of all that, these contacts actually look pretty good. There you go. So, it's just really the debris that's uh caused that. There's maybe some wear between there. Of course, these solder masks have worn off

**Dave Jones:** in there. But, that's pretty good. For 25,000 cycles, I've got no problems with that at all. So, even with the extra pressure from the shim, um that looks pretty decent. Now, if we actually have a closer look at the fiberglass shim here, you can see

**Dave Jones:** that the dust is actually not doesn't appear to be the fiberglass itself. It's a different color, and that's got to be from the um plastic of the case. So, it's not the fiberglass that's wearing down. It's the it's the actual case itself. So, does

**Dave Jones:** that mean uh you know, we could maybe have some grease in there? Might actually help some things perhaps, cuz that is definitely not the uh fiberglass dust there. That's that's coming from the uh that's coming from the plastic case.

**Dave Jones:** What is it? ABS or something like that? Has to be. That's definitely not the uh definitely not the fiberglass. Anyway, there's no wear on that uh hexagon there. Looks fine. And after cleaning up the contacts, wiping away all the crud, putting it

**Dave Jones:** back together after the 25,000 cycles, it's um it's still good. It's still good to go. In fact, the resistance is is I'm having a hard time um getting that to be anything but sort of rock solid that it sort of began

**Dave Jones:** with. So, you know, maybe if I take it off like rotate it a slight amount, but well, it's gone off the contact now completely, of course. Um but it it really seems quite solid. So, I'm that you know, maybe it was just, you

**Dave Jones:** know, a little bit of gunk in there. You just wipe the contacts and uh it's it's good to go. Let's actually uh reproduce the diode mode here. Try and try and do that.

**Dave Jones:** That's That's pretty good. Look, I can't reproduce that at all. So, that that's seems to be a res- still a rock solid solution after 25 thousand cycles. Nice.

**Dave Jones:** All right, this poor little sucker is now done, I believe 51,000 cycles, give or take. And uh well, it's still it still works. The rain switch still feels uh the same as when we put the shim in. Um let's Oh, yeah, we're in

**Dave Jones:** diode mode. And Oh, yeah, there we go. Got it to wiggle a little bit. But not a huge drama. After that number, and once again, um it last time we cleaned it, it was fine. So, that was uh

**Dave Jones:** wonder if that's the case. Now, we'll find out. Don't know how many more insertions and removals this board is going to take. Still doing okay. That was a bit brutal. Wow. Wow, can't really see the plastic again, so I guess

**Dave Jones:** the worst of that plastic is over. That plastic wear worst of that is It's over, is it? There we go. Wow, there's hardly I mean, there's some. Wow, actually there's hardly anything. So, yeah, I think they maybe there was like a burr sticking up

**Dave Jones:** there originally and that's what really wore down, but that looks that looks in fine condition. The switch isn't going to survive that plastic clips not going to survive too many more uh insertions. Wow. Wow, that looks pretty good. That's

**Dave Jones:** after 51,000 cycles. Yeah, I mean, it's you know, it's kind of what you'd expect, I guess. But, uh yeah, there's a lot more lot more wear on this second outer ring. Once again, we got some Yeah, some of the plastic

**Dave Jones:** that's not fiberglass. You can see the color in that. Yeah, I'll spit on that. I might give that a little wipe with some isopropyl alcohol perhaps before I put it back together, but see that that actually it's the contacts are

**Dave Jones:** still fine. Like, that's they seem to be okay. I mean, you know, you'd expect that sort of wear after 50,000 odd cycles. So, let's Yeah, I know it's not a huge amount of Yeah, it's a very clean. Now, wow, so it

**Dave Jones:** was really only that initial um number of cycles that caused the problem. They look to be in pretty good nick. No worries whatsoever. And there's really hardly any metal wear on that and uh the thing we're of course concerned

**Dave Jones:** about is you know metal scraping off either the pads and all the contacts and then getting between you know pads and shorting them out and stuff like that and we really don't see any major evidence of that really.

**Dave Jones:** So that's very impressive I think after 50,000 cycles. 51,000. Nice.
