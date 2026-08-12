---
video_id: u2-ot2vWLxI
title: 121GW Range Switch Cycle Testing
url: https://www.youtube.com/watch?v=u2-ot2vWLxI
source: youtube-asr
timestamps: {"0": 0, "1": 18, "2": 36, "3": 68, "4": 101, "5": 136, "6": 165, "7": 177, "8": 190, "9": 203, "10": 218, "11": 236, "12": 265, "13": 292, "14": 308, "15": 353, "16": 371, "17": 405, "18": 441, "19": 456, "20": 471, "21": 492, "22": 506, "23": 523, "24": 558, "25": 593, "26": 609, "27": 624, "28": 645, "29": 665, "30": 682, "31": 699, "32": 719, "33": 747, "34": 779, "35": 808, "36": 828, "37": 846, "38": 871, "39": 895, "40": 921, "41": 940, "42": 975, "43": 1007, "44": 1028, "45": 1054, "46": 1087, "47": 1107, "48": 1146, "49": 1171, "50": 1209, "51": 1230, "52": 1250, "53": 1279, "54": 1308, "55": 1338, "56": 1376, "57": 1400}
---

**Dave Jones:** Okay, we're going to do some more cycle testing, but we're going to do it on a production unit with the new shim provided by UEI. Yes, it does actually have a routed out little bit in there. It's actually very nice. Those little tooling holes there are designed to get the routed edges.

**Dave Jones:** Yes, it's made out of regular FR4 fiberglass and we're going to and that is going to sit Oops, sorry. We've got actually got this hooked up. I'll show you in a second. But actually just sits over Yeah, sits over there like that.

**Dave Jones:** And that just wedges in there nicely. And it goes back in along with the new knob, of course. And we've actually hooked up some wires here to the off position of the unit. So, when it's in the off position, we'll actually be able to measure the contact resistance here. But we've actually changed our jig over here to actually measure this. So, we're using an ADC with a with a parallel resistor in the divider resistor and then a parallel resistor just in case it opens and then

**Dave Jones:** we can calculate the actual contact resistance. What does our contact resistance go up to, David? About about 10 ohms. Anyway, we've tested it and our nominal contact resistance is about 0.9 or something like that. Um So, of course we expect that to vary a lot and change as we cycle through the automated testing. But anyway, we're going to try it with the new shim, get our automated tester and whack it in there. So, let's give it a whirl. All right, so I've got the new meter together with the new knob and the

**Dave Jones:** new white plastic spring indent thing in there plus the new shim, which is 0.5 mm thickness by the way for those playing along at home. And it's still indents, but it is not as clicky as it was before. Um it just it sort of changes the nature changes the feel of the rain switch. Some people will really love that new feel, others won't. Others might want a light clicky feel. Um anyway, we've got our contact resistance here now. Uh 0.9 ohms and that's not, you know, varying at all. That's uh rock

**Dave Jones:** solid. So, I I expect that, of course, to increase. We're consistently getting um under uh 0.9 and UEI have done some tests and they're consistently getting under the 1 ohm uh mark. But, yeah, anyway, so the plan is probably we'll run 1,000 cycles on this first, take it apart again, have a look at the contacts, and then if 1,000 cycles is okay, then we'll maybe do 5,000 or something like that. Do increments. We're We're not going to go bang for 25 or 50,000 cuz that doesn't

**Dave Jones:** tell us at what point um, you know, if any contact wear starts to happen. So, let's give it a whirl. Let's push some buttons randomly. This will take a little while to set up. Just do it. Still working on the software. Still working on it.

**Dave Jones:** Oh, the software's good. Oh, there we go. Software's good. Software's good. couldn't see it. All right. There we go. All right, we're going to set up 1,000 cycles. Here we go for it. 1,000? 1,000. Let's do it. Okay.

**Dave Jones:** That's the old meter. We're just going to give the test first. Yep. Yep. And for those who are wondering, yes, it does do a full cycle all the way with LBJ from one show that. end to the other.

**Dave Jones:** lift it up now. Oh, right. And There you go. You can have a look. Have a look. Now, that's right right over it there. On the dot. It's on the dot. There you go. And yes, we'll keep an eye on it. All right. Let it recharge.

**Dave Jones:** This is way too much fun. All right, so let's have a look at the this puppy after 1,000 cycles, which is 1,000 cycles one direction, of course. So, like one sweep one way, that's one cycle back is two cycles.

**Dave Jones:** So let's check it out. We cuz we didn't want to run the whole uh uh you know like 10 or 20,000 or something without knowing what it's like after a thousand and and got to remember also this one has been run like a couple of hundred at least a couple of hundred times in various other uh just you know test jig testing and things like that. So it's not it's not a particular as well as you know other use. So it's not a particularly virgin meter in that respect. But this is the

**Dave Jones:** first time it's been run with the uh the new shim. So which uh of course puts some extra pressure on the uh range switch. So let's get this puppy open. Come on. All right. Let's have a squeeze.

**Dave Jones:** Okay. And you would have seen in the testing that there was variation in the contact resistance but it basically didn't um uh fail. There were no opens or anything like that as far as we uh saw from the data.

**Dave Jones:** So There we go. Come out. Come out wherever you are. Here we go. It's It's got to be careful cuz we want to put this back in. And Oh, all right. Let me try and get this out. Okay, that was a poor effort but I got it. Oh, contact came out. That's not unexpected. But there's not much holding those contacts in. So let's flip this over and have a look at our contacts. I'll whack the macro lens on.

**Dave Jones:** Get that under the mantis, but uh there's some uh there's some kind of crud. Hang on, I'll put it under the uh Teegano. Some other stuff in that could be fiberglass. That's from just the inside raw inside of the ring, something like that. Let me get under the uh Teegano.

**Dave Jones:** Okay, there we are under the Teegano microscope. It uh it it probably looks worse than it actually is, but you can see all that um crud around there is this certainly the fiberglass that's uh come off the edge of the hole in there. So, it would have been better if that was plated, I guess, but after a thousand cycles, so it's pushed some of that crud into there, but it's not basically we're looking for really the metal is the stuff that uh really concerns us, and that's

**Dave Jones:** not those markings on the gold pad are really huge problem, especially when the contact resistance we've proven isn't really hasn't really caused much of a drama. There we go. It's maybe some plating starting to wear off the contacts, I don't know, but uh no, they're still looking uh really good nick. So, that combined with the board it's not it's not too bad. So, the the real test that we whack in we'll do like 10,000 cycles next and uh see what happens, but don't know there's nothing seriously bad there at all. The

**Dave Jones:** contact resistance is still good, I think. We haven't run the numbers yet, but I think it's still like always under 1 ohm or something. So, that's fine. Yes, sir. Yeah, it's going to stop at two, one.

**Dave Jones:** It finished. We yeah, we programmed it to get to uh 5,000. So, So, that's what? 9,000? I guess I now I guess we now have to look at the contacts, right? I've got to shoot a video. Should I do that live?

**Dave Jones:** Yeah, this is how I make sure there's no skip steps. This is the permanent marker on the shaft and the permanent marker on the plastic. Uh, it's pretty secure. This side is set to be secure. This side's set to uh, to slip like a torque wrench, so I can't, you know, I can't put too much force manually into the dial. So, to calibrate it, I just go whoop and then it moves all the way to one side and I'm not sure if people are hearing that,

**Dave Jones:** but yep. For those who didn't hear that, it's basically, as I said before, it's hooked up those wires are hooked up to the off switch position, which is actually the reset line of the micro. The micro the like the switch also holds it in reset.

**Dave Jones:** Um, holds the holds the micro in reset. So, and when you hook instruments up to it, or when you hook pull-ups and parallel resistors and everything else, it it just screws with the pull-up on the reset line and it doesn't switch on. So, anyway, still cycles.

**Dave Jones:** Now, I want to shoot this on a regular camera. Doing stuff in this lab is hard. There's so much crap everywhere and every video requires different positions for all for gear and cameras and whatnot. All right, here we have 133 again. We've got uh, we've done 10 9,000 cycles, I think. We did 1,000 and then we checked it and then we did 5,000, but we had to we had to go that night, so we we had to take the computer away, the logging computer.

**Dave Jones:** So, we took it away and uh, we came back today and we did another 5,000, so that makes 9,000 cycles and uh, we were measuring we had a few issues with the position of the meter in the jig and that was causing a real problem with our contact resistance measurement. Um so we've got some problem we're going to get some data that's corrupted. We were getting about roughly about two point, you know, two ohms, something like that contact resistance after you know, towards the end of that. So it

**Dave Jones:** was still going good. And one cycle of course is from one off position to the next. It's not cycled all the way back. So one cycle is from here over to here. So to go back would be two cycles.

**Dave Jones:** That's how we're counting. It's just how our jig how our how our jig works. So let's pop the pop the board out. There's our little shim.

**Dave Jones:** Ah, yeah, we've got some crustiness under there. So some of the fiber glass is Yeah, just worn off that. So guess that's to be expected. Maybe we could add some lube under there or something. I don't know. Oh, actually yeah.

**Dave Jones:** I see the the problem with fiber glass shim is going to be the fiber glass dust around the outside of that. So that's going to be a problem actually. So I'd expect this isn't going to be particularly clean inside here.

**Dave Jones:** Yeah, we didn't see that after a thousand cycles. So that's a It's not entirely unexpected. I didn't know they were going to do a fiber glass um shim.

**Dave Jones:** And I don't think I, you know, plastic one I guess would be better, but they were able to route out use the fiber glass to route out a little slot in it. It's actually rather clever.

**Dave Jones:** Oh, there we go. No contacts came out this time. There we go. I know. No, there's a bit of fiberglass around the outside. But apart from that, that looks Oh, that looks okay. So, those that wear looks bad, but the contact resistance is still great.

**Dave Jones:** It's still like a couple of ohms. It's really quite nice. So, that put a bit of spit on that. So, that's like I can just wipe that. So, it's actually um you know, those contacts are pretty good after 10,000. You can see in there that uh the trace between those two contacts is uh it's worn off the um the solder mask is worn through. But But that's a lot of cycles, right? And that's continuous back and forth, back and forth, you know.

**Dave Jones:** Um at a high rate. Some people say, "Oh, it's it's too We're We're doing it too fast and it's melting. You know, it's going to melt things and stuff like that." Um I don't know. I I didn't think it's that fast. I'm not And now we'll have a look at the contacts. So, you can't say I'm not doing not taking my chances doing this live. The contacts down in there aren't you know, they're fine. There's nothing wrong with the contacts at all. I don't I don't see that as a real issue. Let me

**Dave Jones:** have a look at that on the Mantis. Sorry, I'll go back. Yeah. No, it's contacts are good. Don't worry about the contacts. I think they're great. So, there you go. That was uh 9,000 cycles. Um so, the fiberglass shim is great. We were Yeah, about 2.7 ohms on the um on the switch. So, we can put that back together and measure it. So, if I do that, we effectively have the reset line.

**Dave Jones:** Actually shorting out the the reset line of the microcontroller. Wiggle wiggle wiggle wiggle wiggle, yeah. No. See? It's all hunky-dory. So, um yeah, it's all good. So, that's done 9,000 cycles now. So, apart from the fiberglass dust in there, um 6,000 yesterday.

**Dave Jones:** Oh, 6,000. We did another thousand. Yeah, you're right. It's 11,000 cycles. Thank you. There There you go, 0.8 ohms. I mean, that that's done 11,000 cycles. 11,000 cycles and we're on point 0.85 ohms. And there's like, you know, if you wiggle it, like it changes a little bit, you know, as as you'd expect.

**Dave Jones:** But, uh and 0.9, that one's longer for some um has always been slightly higher for some reason in that position. Maybe it's got I shouldn't have longer tracks. The track tracks are only like, you know, shouldn't add much, but maybe it uses a different set of contacts or something over in that position.

**Dave Jones:** All right, we've got the um serial number 133. It's now done approximately 25,000 uh cycles with the new uh shim, and the contact resistance is still okay, but it's basically I would deem it to be failed now because it's um if we go into the diode test mode, um the knob has the problem.

**Dave Jones:** It will It will do it. Yeah, there we go. So, we've got that uh dicky contact again. So, but that's um our jig failed actually at uh 25,000 cycles. We had a problem with the drive motor and everything else. So, I'm not sure if that's put any extra force on the switch or whatnot, but uh that's what we've done now, 25,000 cycles. So, let's have a look.

**Dave Jones:** Although, it has as an actual solution um it works it seems to work very well for the contact resistance and the of course the switch wobble is uh fixed and the intermittent rain switch I fix I think all those problems are now uh I think it does actually fix those.

**Dave Jones:** So, that's good. Okay. Let's have a look. Actually, not a not much more dust than previously. Uh similar. I'd I'd I'd call that similar. Shim of course is uh uh it seems to have worn on may maybe there was a burr of plastic or or something under there that Oh, no, it was at the holes.

**Dave Jones:** Yeah, it seems to have lined up with the holes to do that. So, that's that's interesting. Okay. Let's have a look at the contacts first of all. And the contacts are actually the contacts look very good and you can see the dust caked under there, but uh for 25,000 cycles those contacts look uh really quite nice. So, that doesn't seem to be a problem. Once again, it probably looks worse than it is with the dust.

**Dave Jones:** It's a problem, but the actual uh the contacts on the PCB still look okay. I mean, you know, it's had 25,000 full cycles on it. That is quite quite violent. So, I don't have too much of a problem with that.

**Dave Jones:** Actually, with the actual wear on the contacts, it's you know, not as uh I mean, it's not perfect, but there we go. If we get rid of all that, these contacts actually look pretty good. There you go. So, it's just really the debris that's uh caused that. There's maybe some wear between there. Of course, these solder masks have worn off in there.

**Dave Jones:** But, that's pretty good. For 25,000 cycles, I've got no problems with that at all. So, even with the extra pressure from the shim, um that looks pretty decent. Now, if we actually have a closer look at the fiberglass shim here, you can see that the dust is actually not doesn't appear to be the fiberglass itself. It's a different color, and that's got to be from the um plastic of the case. So, it's not the fiberglass that's wearing down.

**Dave Jones:** It's the it's the actual case itself. So, does that mean uh you know, we could maybe have some grease in there? Might actually help some things perhaps, cuz that is definitely not the uh fiberglass dust there. That's that's coming from the uh that's coming from the plastic case.

**Dave Jones:** What is it? ABS or something like that? Has to be. That's definitely not the uh definitely not the fiberglass. Anyway, there's no wear on that uh hexagon there. Looks fine. And after cleaning up the contacts, wiping away all the crud, putting it back together after the 25,000 cycles, it's um it's still good. It's still good to go. In fact, the resistance is is I'm having a hard time um getting that to be anything but sort of rock solid that it sort of began with. So, you know, maybe if I take it

**Dave Jones:** off like rotate it a slight amount, but well, it's gone off the contact now completely, of course. Um but it it really seems quite solid. So, I'm that you know, maybe it was just, you know, a little bit of gunk in there. You just wipe the contacts and uh it's it's good to go. Let's actually uh reproduce the diode mode here.

**Dave Jones:** Try and try and do that. That's That's pretty good. Look, I can't reproduce that at all. So, that that's seems to be a res- still a rock solid solution after 25 thousand cycles. Nice.

**Dave Jones:** All right, this poor little sucker is now done, I believe 51,000 cycles, give or take. And uh well, it's still it still works. The rain switch still feels uh the same as when we put the shim in. Um let's Oh, yeah, we're in diode mode.

**Dave Jones:** And Oh, yeah, there we go. Got it to wiggle a little bit. But not a huge drama. After that number, and once again, um it last time we cleaned it, it was fine. So, that was uh wonder if that's the case.

**Dave Jones:** Now, we'll find out. Don't know how many more insertions and removals this board is going to take. Still doing okay. That was a bit brutal. Wow. Wow, can't really see the plastic again, so I guess the worst of that plastic is over. That plastic wear worst of that is It's over, is it?

**Dave Jones:** There we go. Wow, there's hardly I mean, there's some. Wow, actually there's hardly anything. So, yeah, I think they maybe there was like a burr sticking up there originally and that's what really wore down, but that looks that looks in fine condition. The switch isn't going to survive that plastic clips not going to survive too many more uh insertions. Wow.

**Dave Jones:** Wow, that looks pretty good. That's after 51,000 cycles. Yeah, I mean, it's you know, it's kind of what you'd expect, I guess. But, uh yeah, there's a lot more lot more wear on this second outer ring. Once again, we got some Yeah, some of the plastic that's not fiberglass. You can see the color in that. Yeah, I'll spit on that.

**Dave Jones:** I might give that a little wipe with some isopropyl alcohol perhaps before I put it back together, but see that that actually it's the contacts are still fine. Like, that's they seem to be okay. I mean, you know, you'd expect that sort of wear after 50,000 odd cycles. So, let's Yeah, I know it's not a huge amount of Yeah, it's a very clean. Now, wow, so it was really only that initial um number of cycles that caused the problem. They look to be in pretty good nick.

**Dave Jones:** No worries whatsoever. And there's really hardly any metal wear on that and uh the thing we're of course concerned about is you know metal scraping off either the pads and all the contacts and then getting between you know pads and shorting them out and stuff like that and we really don't see any major evidence of that really.

**Dave Jones:** So that's very impressive I think after 50,000 cycles. 51,000. Nice.
