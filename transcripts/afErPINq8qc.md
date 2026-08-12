---
video_id: afErPINq8qc
title: Mini Arcade Game Console Repair OOPSIE!
url: https://www.youtube.com/watch?v=afErPINq8qc
source: youtube-asr
timestamps: {"0": 1, "1": 19, "2": 39, "3": 52, "4": 61, "5": 72, "6": 87, "7": 103, "8": 113, "9": 125, "10": 134, "11": 151, "12": 164, "13": 172, "14": 184, "15": 201, "16": 213, "17": 223, "18": 237, "19": 254, "20": 270, "21": 293, "22": 309, "23": 323, "24": 352, "25": 371, "26": 384, "27": 392, "28": 411, "29": 427, "30": 438, "31": 451, "32": 462, "33": 478, "34": 495, "35": 516, "36": 536, "37": 546, "38": 559, "39": 571, "40": 584, "41": 598, "42": 620, "43": 630}
---

**Dave Jones:** Hi, it's time for our pair video. I've got a little one of Sagan's little toys here. It's one of these little mini arcades and mini arcade cabinet. Not like my real one I've got here, but yeah, it's like got 50 games in one or something like that and the screen has gone skew on it.

**Dave Jones:** Screen's a bit knackered. Let's turn it on. We've got lines across here. Still seems to work. I can still select stuff and plays. That flickering is not just the camera.

**Dave Jones:** That's happening in real life. Oh, yeah. Oh, yeah, I can see things just. Yeah, it's one sick puppy. So, I would take it apart, have a squeeze. It's probably just a single chip solution in it.

**Dave Jones:** I'm sure wouldn't would it be an ASIC? I mean, you know, they've got to get the price down on these things. They They They practically give these things away.

**Dave Jones:** They're really dirt cheap. So, yeah, I don't know or is it just a an arm processor and LCD and maybe an external ROM or something for the games. Perhaps, I don't know.

**Dave Jones:** Let's take a look. Well, it looks like to open it up I've got to slice right through the decal like that. No worries. Here comes the knife. All right, so that was easy and there you go.

**Dave Jones:** A single sided board. I don't want to waste your money on a double sided jobby. So, is it looks like we are just going to uh Okay, so we've got a um interface board for all the for the little joystick and the buttons and a single sided.

**Dave Jones:** I reckon we're just going to get a uh single ASIC blob on there. So, yep, I reckon they've gone to the trouble of that. Not much else in it, is there?

**Dave Jones:** Wow. Like they've gone to the effort to put the speaker on the back, you know, I Instead, got to wire that over. And of course, you don't want any of that screw rubbish.

**Dave Jones:** You just uh get the soldering iron down there and uh just melt those heat stakes to uh keep the switch in place. Same thing for the speaker as well.

**Dave Jones:** No wackers. And there you have it. We've got one of those dodgy uh tab connections again. So, yeah, that's probably it. And of course, uh to get you a single-sided board, they couldn't get it all on a single-sided layout, so they've used some carbon jumpers on there.

**Dave Jones:** So, that uh extra process layer to put the carbon traces on there is going to be cheaper than doing a double-sided board with uh plate through. And that's, you know, that's probably the case when you're talking about these things.

**Dave Jones:** They're probably manufactured hundreds of thousands of these or a million of these things. So, yes, it was a uh is a black blob. And uh so, that's uh chip on board.

**Dave Jones:** That's a They just uh glue that straight on there, and then they start bond wires going over to the pad. Then they just gunk the whole lot. Got a uh SO8 package happening there.

**Dave Jones:** Have to look at the part number there, but we've got a regulator. And uh well, yeah, not much else is there. But, that's all you need. So, yeah, they developed custom ASIC for that Well, I presume it could be uh like a uh pre-programmed uh micro uh microcontroller.

**Dave Jones:** Like, it could just be like a a big memory, big flash memory arm uh processor or something like that. May not be one of the mainstreams ones. Maybe one of those uh uh obscure uh Chinese brands or something.

**Dave Jones:** And then they just get it in die form and blob the whole lot. So, not necessarily an ASIC under there. You can't make that call unless you actually know what's going on.

**Dave Jones:** But, anyway, uh I think the fault's almost certainly in our tab connection there. Groan. Seen that in many videos before. All right, let's see what happens to that screen if I push down on the connections.

**Dave Jones:** Just use my thumb at this stage. Nothing. That's interesting. Hmm, got to get my poker. Wow, no, it ain't that. It ain't a bad connection cuz that that's actually soldered.

**Dave Jones:** Yeah, that's actually soldered. That's actually not a conductive adhesive. So, it it ain't that. Is it inside the screen? Is it a bad die bond in there? What's going on?

**Dave Jones:** And you can actually see the COG chip on glass up there. That's our driver chip. That's actually embedded on the glass. And like if I put physical pressure on there, so it's not the this would be conductive adhesive.

**Dave Jones:** But it ain't that. It ain't that cuz they've gunked the whole lot of that. So, um yeah, it's something else. Aha, Winbond. Um not necessarily an obscure brand. Yeah, so that's an external flash memory by the looks of it.

**Dave Jones:** 25064 or is that Q64? All right, I'm going to see if it's a thermal thing with the die bond under there. Going to get my freezer spray, uh air duster turned upside down.

**Dave Jones:** Instant freezer spray. Nope. What? Chilly finger, chilly finger. It ain't that. No, it wasn't that. Let's try the LCD connection. Nope. It's nothing thermal. Well, thermal doesn't fix it anyway like a bad connection or something like that causes it to get worse or get better.

**Dave Jones:** So, hmm. All right, so the next thing I'm going to suspect is the solder connections on there. So, they look a little bit how you doing, don't they? Hard to tell.

**Dave Jones:** Really got to get them under the microscope. You could have a micro crack in any one of those. Of course, you can uh can check those manually. You can just buzz out each side of that fairly conveniently.

**Dave Jones:** And that's a pretty quick, easy test. So, I'd probably do that as a matter of course or you could just simply Oh, it just stopped playing. Oh, auto turn off perhaps?

**Dave Jones:** Yeah, so or you could just go reheat them all, but I might just buzz them all out first. And not sure if you can see that on camera, but I tried to probe this and you can't really cuz you can see that hopefully that there's a whole bunch of uh uh gunk covering that.

**Dave Jones:** So, you can like Yeah, you really need sharp probes to uh pierce through. It's uh It's really annoying. They've put like a a It's almost like a glue type stuff on top.

**Dave Jones:** Hmm. Well, this is getting nasty. I just resoldered all the connections on there. And we've got the exact same problem. I I I went through and reheated them all.

**Dave Jones:** I just What you do is just get in there with your iron and you just drag them like that back and forth. And it exactly the same problem. And I did it twice.

**Dave Jones:** So, you'd think that the odds are that if there was a bad joint on there, it would have either got worse or gotten better. But no, it's exactly the same.

**Dave Jones:** Hmm. Is there a uh little micro crack in the ribbon, perhaps? Wouldn't be the first time I've encountered that, but I've been wiggle, wiggle, wiggle year in, and I I just can't Oh.

**Dave Jones:** Can't get anything to anything to happen. So, it's not like it's a bad contact or intermittent contact somewhere. Oh. I just threatened to get the oscilloscope out, and uh it I turned it on, and it just went It didn't It didn't play.

**Dave Jones:** Oh. I swear. Whoa. Something's going on. Whoa. Yeah, something's happening. Give the board a flex. Yeah. Something's dodgy. Let's try flexing that board, cuz that'll affect the that black gunk isn't perfect.

**Dave Jones:** There'll be some flexion in there, and the bonds might not If they're intermittent, they could come a gutter. But no. No, that's okay. Whoa. But that screen is doing that, and it's resetting, and it's flickering.

**Dave Jones:** So, hmm. Something very wrong with this LCD. I'm playing a game at the moment, and I can't see a thing. So, it's not like the it's the just the stripes.

**Dave Jones:** And if you have a look on the edge like that, when you put it on the side, you can actually see it. Can I select that? Continue. Start. There you go.

**Dave Jones:** So, you can like straight on, can't see a thing. It practically vanishes. And on the side, you can. It seems to be You know, it's it's kind of mostly working.

**Dave Jones:** There's some ghosting stuff happening there, but there you go. So, that's really interesting. What's going on? And what do you know? What what what what? I dropped it, didn't I?

**Dave Jones:** I wasn't moving stuff on the soldering bench, and it dropped off onto the floor, and that's the result. So, yep, cracked the LCD. There's just no point fixing it now, so I'm going to leave that.

**Dave Jones:** I couldn't be bothered, and yeah, goneski. I'm afraid. And yeah, I'll just dump this on the second channel. So, ah, well, that sort of stuff happens. Anyway, if you got any idea about the about the lines on there and why it's faded like that, let us know.

**Dave Jones:** We could have got into like the drive voltages and all that sort of jazz in there, but yeah, I no no. Not going to waste any more time on it.

**Dave Jones:** Catch you next time.
