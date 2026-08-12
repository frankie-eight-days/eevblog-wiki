---
video_id: cO45J-8qTZ4
title: EEVblog 1593 - 16kV ESD Tester REPAIR - Part 2
url: https://www.youtube.com/watch?v=cO45J-8qTZ4
source: youtube-asr
timestamps: {"0": 0, "1": 33, "2": 62, "3": 93, "4": 124, "5": 141, "6": 156, "7": 194, "8": 220, "9": 240, "10": 264, "11": 281, "12": 300, "13": 326, "14": 346, "15": 366, "16": 385, "17": 406, "18": 434, "19": 458, "20": 481, "21": 499, "22": 519, "23": 561, "24": 590, "25": 609, "26": 628, "27": 661, "28": 695, "29": 708, "30": 732, "31": 750, "32": 771, "33": 794, "34": 833, "35": 848, "36": 872, "37": 885, "38": 912, "39": 930, "40": 955, "41": 968, "42": 1006, "43": 1026, "44": 1045, "45": 1071, "46": 1093, "47": 1123, "48": 1143, "49": 1169, "50": 1189, "51": 1201, "52": 1231, "53": 1252, "54": 1272, "55": 1286, "56": 1323, "57": 1353, "58": 1387, "59": 1419, "60": 1456, "61": 1486, "62": 1523, "63": 1556, "64": 1593, "65": 1623}
---

**Dave Jones:** Hi. Well, this repair video's taken a while. It's been 3 months since I uploaded uh the teardown and part one uh repair of this uh hateful trench uh ESD 1600 gun uh ESD tester gun. And then I did actually post a part two of this where we actually discovered that the fault was uh this special snowflake rotary encoder here. It would only operate in one direction. And so, it would only go down, I think. It wouldn't go up. And of course, this has a digital readout. You

**Dave Jones:** can adjust it uh from 2 kV up to 16 kV output. And it worked. The gun actually worked, but I couldn't get it up above the 2 kV. Anyway, I'll link in the video up here and down below if you haven't seen it. And also, an interesting follow-up video of a teardown of the actual rotary encoder here, which is a really unusual type. It's not your usual rotary encoder. So, I won't go through the details again. You can watch that video. But anyway, um this rotary

**Dave Jones:** encoder is only a single-source. You can't get it anywhere else. But I found a company in Germany on eBay that sold like new old stock of these. And you know, they sold them two at a time at a reasonable price. So, I ordered them straight away. And a month went by or something, and I didn't get them. And well, I mucking around and trying to trace it all. It turns out, nope, lost in the post. So, completely lost. So, I just ordered uh two more of them, and they did turn up.

**Dave Jones:** And I'm back from holiday. So, now I actually got these this time. So, I've got two of these bad boys. So, let's actually take a look. You can see here that they're a single-pole double-throw here either side. And each side here operates in one direction only. So, this is the uh common here. So, it'll toggle between these two pins like this when you rotate it in one direction and if you rotate in the other direction it doesn't do anything at all. It'll just stay there. And likewise, this one here

**Dave Jones:** will toggle between that those uh two pins as you rotate it. So, let's actually connect this up. I think this one is the Yeah, that one's the normally closed. So, let's actually rotate this. I'll go counterclockwise like that. It does nothing.

**Dave Jones:** Counterclockwise according to the bottom, but if I go clockwise, bingo. There you go. It does the business and that other pin will be That'll just be normally open and that one will close when I go in that direction.

**Dave Jones:** Oh, no, occasionally it stays on. I think. No, it should or shouldn't? Not sure. No, it shouldn't. But even if it does accidentally stay on anyway, it's the impulses that matter that the microcontroller is looking for. So, let's try the other pair over here like this. And yeah, normally closed and if we go in the counterclockwise direction, it is beeping and going the other direction it's not. And the other pin, counterclockwise direction, yep, it goes like that and yeah, Bob's your uncle. No worries. Works a treat. So, this should

**Dave Jones:** fix the gun. Right, so here's the PCB that we got out of this thing and if you saw the teardown video, it's really annoying cuz I had this metal plate with all these switches on it and had to desolder all of those to get in there to the digital pot. Where is it? It's up here. So, have all my holes been sucked out? Desolder that one's a bit how you doing. Might have to open up that one a bit, but anyway, let's see if we can get

**Dave Jones:** that back in there and resolder that sucker. So, yeah, unbelievable. A special snowflake. Wouldn't it be my luck. Murphy, of course. This used a special snowflake thing that's available from one source on eBay in Germany, new old stock. Um yeah, it's just nuts.

**Dave Jones:** Yeah, of course, you know, ultimately, if I couldn't get it, I would have designed a little uh plug-in board or something that just converted a regular rotary encoder encoding scheme into this encoding scheme, and it wouldn't have been too hard. In fact, that would have been an interesting video, but I was able to get this. Let's just re suck that one, shall we?

**Dave Jones:** Beautiful. Look at that. Bobby Dazzler, classic solder sucker. There we go. Got it. Got it. Sorry, we're zoomed in. Solder that back in place. Bob's your uncle. Look at that. Oh, hang on. One of the pins didn't make it. Oh, you kidding me?

**Dave Jones:** Oh, I bent one. Oh, what what what what? I just soldered it. I should have checked. I just soldered it. All four of those. Oh. Bloody hell. It's not even Monday. Yeah. Look at that. I squished it. Oh, unbelievable. I thought I had it in.

**Dave Jones:** Oh, that's what she said. Luckily, I do have a spare, but I might get one more shot at this. Oh, no. OH, IT'S FLOPPY. THAT'S WHAT SHE SAID AGAIN. I'll have to watch the teardown video again, but why they manufacture this with two soft little piddly pissing pins and four big thumpin' solid machine ones?

**Dave Jones:** I'll never know, but anyway, uh gosh, try it again. I've probably got one shot at this. Always double-check before you stick your pins into the hole. Once again, she's saying a lot today. Oh, that. Okay, that one I did not put any pressure on that that time.

**Dave Jones:** I did not put any pressure on. And I think I see two pins. Winner winner chicken dinner. Okay, you can see them. There and that one there. You were probably all screaming at me before, right? Cuz you There we go. Cuz you saw it on your whiz-bang screens you're watching this on.

**Dave Jones:** Sorry, I got to put this on an angle. I don't know. I can probably use my third hand. Three hands on a pivot here. No, I couldn't be bothered getting out of a holder. One pin there. Okay, I'll get I'll get this bad boy over here.

**Dave Jones:** There we go. That's one of the pins over there. No worries. And that is the other one there. Ooh, you can rotate the board easily when you got it sitting on just a shaft like that. Once again, that's what she said.

**Dave Jones:** And sorry about the contrast here. It's always a problem, contrast, when you're trying to record video like that. And yeah, I got the fresh rosin fumes. Anyway, there you go. So now it's in. Unbelievable that There you go. 4893 classic for the win. Now, I got to make sure these pins are not No, these are These are pretty solid.

**Dave Jones:** They're solid as. They should go in. Hopefully, I've got It's It's hard to tell where the holes are. But yeah, there, there, there, there, and there. They all look good, don't they? So I should be able to Problem is, you got to line up You got to line up 12 pins perfectly before it all drops into place.

**Dave Jones:** And it's And they're attached to this side like They're attached to this side. So, you've got it like This is the only way to do it. Like What engineer is responsible for this horrible abomination of an assembly process? No, that's terrible, Muriel. And they wobble from side to side.

**Dave Jones:** That's why it's not going in. Oh, and that one's pushed out. Like oh, oh, no. Can I actually take that I think I can Yeah, I can take that out. I can take that out and Oh, yeah. Yeah, some of them have come out, so let me push them all flush.

**Dave Jones:** Yeah. Look at that. So, they're all flush now. I don't know why some of them have this little um a plastic ring on it. Um doesn't seem to be insulating anything of note. So, all right. Here you go. So, what you got to do is you got to give a wiggle, wiggle, wiggle, yeah to some of them before they'll go in.

**Dave Jones:** There we go. That's the trick. I'm ready for my job at the Hafli Hafli Hafli assembly line. Two pins. Okay, they don't go all the Okay. It's Oh, that See that that that metal plate I don't know whether or not the metal plate's supposed to sit on those spaces or what. Don't know what the deal is there. Rather unusual and annoying construction, but my my pins are all the way through, right? So, as long as those switches are pushed flush with that and I eyeball them that they're all good,

**Dave Jones:** don't know what the metal plate does. Does it just flap around in the breeze? That one there's it Look, that one there's higher than the other ones. So, what's going on there? Oh, it's the plastic It's the plastic spacer. Okay. I'm not totally sure what the height's supposed to be. I might go check the fit in the front panel. I don't think it's going to matter actually. Yeah, it's it's not going to matter at all if like one of them sticking up slightly more than the others.

**Dave Jones:** It's just rather annoying. Like cuz some of them have that plastic spacer and some don't. So, I don't know. Not sure what the deal is. Maybe I can just a light pull them up to align them all at the right height manually. All right, I think I've got that. So, that's going to be good enough for Australia.

**Dave Jones:** So, let's go in here and resolder these. I know I should not be on the side like that. I should have flipped it around like that cuz it had the elongated pad and that's just the correct thing to do. Don't you hate it when your solder bends like that?

**Dave Jones:** You need a bit of extra there for the ground plane. Don't pay the ferryman till he gets you to the other side. All right, we are good to go. So, I will now reassemble the whole kit and caboodle and this part should magically work. Um, I can't just power this up on its own. It's got to be all sort of like hand assembled before you can fire up anything. It's it's a terrible design as you saw in the teardown video.

**Dave Jones:** Okay, now I have to remember how this all goes back together. All these loosey-goosey wires here, um, they solder onto points on the main board, I believe. Um, I do have a Post-it note somewhere. I recorded it when I tore it down. So, let me find the details. Okay, so this has a board-to-board interconnect which goes in there and all these wires are out of the way here and then we got some solder tags here as well. They have to be uh no, they go back in with screws and

**Dave Jones:** then there's spacers as well. I've got all my assorted bits in here. I just have to remember it's been 3 months. I have to remember how they went back on. Maybe I should have documented it a bit better, but she'll be right.

**Dave Jones:** Check it out. It's pretty horrible. You've got a board which sits on a right angle spade lug soldered onto the chassis like that and then this spacer here is supposed to go in there like that. And then you're supposed to screw it in from the front panel.

**Dave Jones:** It's It's just awful. I'm sure you this is truly horrendous. It really is. Look, I've got one in but then the other one barely lines up and you've got to try and but I can't It doesn't go back. It doesn't go back.

**Dave Jones:** It's in in and under in and under. Um uh don't design your products like this, kiddies, please. This is ridiculous. Now, you've got to manipulate that until that lines up there. It all hinges on this bent spade lug here and now the board's come out again.

**Dave Jones:** So, now I've got to try and get the No. Line up all the pins again cuz there's too much solder on there. It's a nightmare. Now, I'm going to have to bend that spade lug more. This is ridiculous. This is the worst physically designed product I've ever seen. This is just insane. And all the while I've got to be careful not to like bend the pins.

**Dave Jones:** Thankfully, it's a double row. They're fairly solid, but you know, you could easily easily bust one. Maybe I can cut off a bit of the solder there. Be less thick. Now, here's where you want a pair of reverse flush cutters like this. These are reverse ones. So that should allow me to get in there and just trim off that solder a bit so that board fits in there a bit better without me having to attack like a actually resolder this stupid thing cuz then it'll all come out of

**Dave Jones:** alignment. So there you go. So I've trimmed off some solder on there. Sorry, I'm not getting the best camera angles here but hopefully you're getting the idea of what a real pain this is. A lot of excess solder on there.

**Dave Jones:** So yeah, that should give me a bit more margin cuz I was really pushing that board across to fit in the socket. Ah, that goes in the socket much easier now. Yep, I'm liking that. Hey, I think I can see the hole now. And after all that I just realized I've got the wrong spacer on here. The wrong spacer. I have to put a screw from the back there.

**Dave Jones:** And not that that's hasn't caused me much grief but it is a pain. So what I need to do is get that screw through there and then get the spacer. There we go. Got the spacer in there like that.

**Dave Jones:** And then that goes back to doesn't quite line up now. Aha, I just realized I should watch my teardown video. Maybe I can uh uh realize how it went in. That is spaced off there because the PCB slides under there. So I was flogging a dead horse before trying to get that in. So yeah, there you go. That's the trick.

**Dave Jones:** But now I've got the problem of trying to get the board-to-board interconnect in there and slide in it under there at the same time. Okay, let's get this board in here. Lines. Woah, the first pin's a bit how you doing?

**Dave Jones:** How about that? It goes in. Aha, yep. I think I got it. Yeah. Let that be a lesson to you. Document your teardowns a bit better or watch your own teardown videos and maybe it's in there somewhere. But uh we're good. We're good to go now, I think. Put the spacer and the LCD back on.

**Dave Jones:** And last screw for the LCD. Turns out I didn't have to take that off, I don't think, to get the board out. But didn't know that at the time. It's actually easier once you've done one of these once.

**Dave Jones:** As as is always the case. But yeah, nah. Doesn't excuse this horrible design. Now comes another really tricky part. I have to actually can't see it, but that is a four-pin connector and this brown wire flapping around in the breeze has to be soldered on that rear pin right down in there. What a uh what a nightmare. So, I almost have to flip the whole thing out, um solder it in, and then sort of flip the whole thing back in, I think. Yeah, so what I got to do is kind of like flip

**Dave Jones:** this whole thing out, then I can access the solder that pin down there, and then I can flip it all back in, and this um spacer has to go between the boards there, but I can take that out from the other side. So, that's not too much of a drama. Um uh uh It's not pretty. I'll get back to you.

**Dave Jones:** This is where the long pair of needle-nose pliers comes in handy. And well, get that black wire in there. Don't burn any of the buttons? Been there, done that. Any bit of surrounding plastic and and there we go.

**Dave Jones:** Threading a needle. Wow, got the trigger button. And then, there's just enough hopefully this sits in there properly. There's just enough lead length to solder on Uh sorry, you can't see it, but solder on the output terminal. Yep, there we go.

**Dave Jones:** And that is some surgery. The front panel, that just sits like that. They actually go into self-tappers into the plastic. Oh, no, I forgot the stud up here. There you go. So, I've got to put the stud back in Oh, no. Oh, did I forget?

**Dave Jones:** I think I forgot. I think I forgot. There is a giant stud which goes through here. Like this. Oh, no. And I've got to somehow screw that back in. This just gets better and better. Yeah, needle-nose pliers again. Yeah, I can remember this from the teardown. I had to get that out before I could get the uh the board and the chassis.

**Dave Jones:** Well, the chassis out and then the board's out. There is a special place in hell for whoever designed this. Actually, before I get this back together, I've plugged it in. So, no touching of any of the uh scary bits, of course, but uh operate. There we go.

**Dave Jones:** Tada. And let's see if it goes up. It does. It goes up. Yay. Oh, sorry, it starts at 200 V, not 2 kilovolts. There you go. Works in both directions. Winner, winner, chicken dinner. Well, I haven't tested the sparks yet. Can't do that. You got to hook up the grounds and everything. And with enough patience, you can actually get that in.

**Dave Jones:** Oh, man. I'm sure you get used to it at the factory, but that's ridiculous. There's got to be a better way to do that. That's just crazy. Anyway, that is one of the studs like you don't like you can hook the ground up to either that stud there or that one there. It's all connected by the same chassis, but yeah.

**Dave Jones:** That's just crazy. Ah, there we go. Tight as a nun's nasty. Okay, the last thing I want to actually uh repair in this thing is uh the nickel metal hydride uh batteries. I think I said NiCad uh in the previous video.

**Dave Jones:** They are are actually nickel metal hydride, made in Japan. All the best stuff's made in Japan. And um yeah, they've come a gutser over the years. So, uh we've got That's a uh six-series uh cell design, and it does have a little uh thermal fuse in there. So, I'm not going to crack open my pack and actually uh replace that. But anyway, I've got a uh nickel metal hydride 2200 milliamp hour um six-cell uh pack. And also, I will They're just like dodgyly soldered onto there. So, I will just um

**Dave Jones:** and that's a temp sensor um down in there. So, I'll just uh cut a hole in the top of that. I'll stick the temp sen- temp sensor down in the middle, and I'll just cut these off and bodge them in. So, yeah. Nothing much to it. Well, wasn't entirely straightforward. Did have to dig that out of there, but there you go. So, there she comes out.

**Dave Jones:** I'll just stick that down the clacker of the new pack. No worries. She'll be right. And there we have it. I'll just manage those cables in there. Now, the interesting thing is this is already charged up. So, you got to be careful when you soldering these in not to touch any of the high-voltage stuff, cuz technically, you could turn it on. Let's try it. Yay!

**Dave Jones:** Look at that. Works. Unfortunately, it's only set to 200 V, but you know, never be too careful. Anyway, I'll put the cover back on and Bob's your uncle. We'll test her out. Let's put the nylon spacer screws back in.

**Dave Jones:** Use nylon screws, of course, just cuz you don't want any exposed metal in your 16 kV ESD generator. Cuz uh yeah, you could come a cropper, and that could ruin your day. Unfortunately, our calibration is now void. Gosh darn it. Though, they do have plastic self-tappers on there to hold on the outside thing here, but no worries, because well, it just goes into the plastic case, and it's all on the low-voltage side anyway, so I'll just turn that back, let it drop in place, find the thread.

**Dave Jones:** So, pro tip with metal screws into plastic, just rotate it back until you find the point where it slightly drops in place to the existing thread, and then you can screw it back in, and then you're not cutting a new thread in your plastic, but don't overtighten that. There you go. Look at that. It's like a bought one. Now, please excuse the crudity of the model. Didn't have time to build it to scale or to paint it. I'm going to use my trolley here.

**Dave Jones:** I've got my ESD mine now. A functioning ESD gun. Look, it's actually functioning with the battery now, so I can actually turn the wick up and down. How novel. Um so, yeah, I've got my grounding strap. It's going back to my power supply over there, and the trolley's connected over there. Yeah, it's not exactly an IEC 61000-4-2 standard setup. Leave it in the comments down below if you want me to, and I probably will anyway, but definitely leave it in the comments down below if you want me to build a like IEC

**Dave Jones:** compliant or you know, one that's at least good enough for Australia, compliant bench for ESD testing cuz we've got the proper gun, we've got the two different adapters. This one's for an air gap the rounded tip is for the air gap and the pointy one is for a direct contact measurements, but yeah, we can actually design and build a like a compliant bench at least for like a pre-compliance purposes. Anyway, leave it in the comments down below if you want to see that and to actually measure the output

**Dave Jones:** from this thing actually get a proper waveform and actually check the compliance of this thing, you need what's called a Pellegrini target and it's basically a 2 ohm proper coaxial to a high frequency coaxial 2 ohm test target and it's also defined in the 61,000 -4-2 standard as well. So, yeah, you know, it's like if you want to do all this ESD stuff properly, there's a lot of stuff involved. You have to get really serious, but anyway, that let's just try the trolley. Let's just get

**Dave Jones:** something out of this thing. So, let's turn it up to L3 8 kilovolts here. We've got air discharge. We've got a single here. Of course, we can set you know, repetitive stuff, but anyway, let's just go for an 8 kilovolt. Okay, let's see if we can zap these capacitors here, shall we? We might get some noise into the microphone cable, but we'll give it a go. Geez, it's hard to reach over THE CAMERA WITH THE MACRO LENS, but uh give it a go.

**Dave Jones:** Zappity do da. Shoo, cool, huh? So, there you have it. There's a repaired Haffely Trench PESD 1600 gun and this is a real proper industry standard bit of kit for our compliance testing. So, that was absolutely fantastic. All it cost me was basically just the rotary encoder here, and bit of frustration taking it apart and putting it back together, but no, that's a Bobby Dazzler, and I have no doubt that it that actually meets its would continue to meet its spec. But, as I said, to get a proper

**Dave Jones:** waveform measurement out of this have to have a proper high-frequency 2-ohm load, which is called a Pellegrini target, and you've got to set it up specifically. And even even this cable, like you can't just leave it flapping around in the breeze. You've actually got to you know, pull it back, stretch it back so it forms like the largest loop possible. And like it's really serious stuff cuz these impulses are really high-frequency stuff. So, you know, the actual targets you use and the probing and everything else has to be really

**Dave Jones:** top-notch stuff. But, yeah, I I trust that this thing would still deliver its proper designed pulse response shape, which would be, you know, match the industry standard shape. But, there's many different aspects to ESD testing, which is part of EM It's just one part of EMC compliance, the ESD testing. But, it's all in the standard, and it's very involved and quite complicated. But, give this video up and leave a comment down below if you want me to design and build a proper ESD testing bench. I'd have to do it down in

**Dave Jones:** the dungeon. I've got room in the lab for a small bench, but you know, it's better off building it down there. And yeah, set it up properly, and maybe even I get in some waveform proper trying to get some proper waveform measurements out of this thing anyway. But, as always, give Give a thumbs up, discuss down below, and also on the EEVblog forum. And I do release all these videos on Twitter/X now as well, so you can follow me over there. And EEVblog.com for the merch.

**Dave Jones:** Catch you next time. I can make these capacitors sing. Listen to this.
