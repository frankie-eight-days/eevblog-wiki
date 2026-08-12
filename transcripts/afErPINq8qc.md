---
video_id: afErPINq8qc
title: Mini Arcade Game Console Repair OOPSIE!
url: https://www.youtube.com/watch?v=afErPINq8qc
source: youtube-asr
timestamps: {"0": 1, "1": 16, "2": 39, "3": 55, "4": 70, "5": 83, "6": 99, "7": 113, "8": 127, "9": 142, "10": 156, "11": 169, "12": 180, "13": 195, "14": 210, "15": 223, "16": 239, "17": 265, "18": 286, "19": 307, "20": 323, "21": 345, "22": 361, "23": 380, "24": 395, "25": 408, "26": 427, "27": 442, "28": 457, "29": 476, "30": 494, "31": 519, "32": 541, "33": 554, "34": 573, "35": 592, "36": 611, "37": 625}
---

**Dave Jones:** Hi, it's time for our pair video. I've got a little one of Sagan's little toys here. It's one of these little mini arcades and mini arcade cabinet. Not like my real one I've got here, but yeah, it's like got 50 games in one or

**Dave Jones:** something like that and the screen has gone skew on it. Screen's a bit knackered. Let's turn it on. We've got lines across here. Still seems to work. I can still select stuff and plays. That flickering is not just the camera.

**Dave Jones:** That's happening in real life. Oh, yeah. Oh, yeah, I can see things just. Yeah, it's one sick puppy. So, I would take it apart, have a squeeze. It's probably just a single chip solution in it. I'm sure wouldn't

**Dave Jones:** would it be an ASIC? I mean, you know, they've got to get the price down on these things. They They They practically give these things away. They're really dirt cheap. So, yeah, I don't know or is it just a an arm processor and LCD and

**Dave Jones:** maybe an external ROM or something for the games. Perhaps, I don't know. Let's take a look. Well, it looks like to open it up I've got to slice right through the decal like that. No worries. Here comes the

**Dave Jones:** knife. All right, so that was easy and there you go. A single sided board. I don't want to waste your money on a double sided jobby. So, is it looks like we are just going to uh Okay, so we've got a um

**Dave Jones:** interface board for all the for the little joystick and the buttons and a single sided. I reckon we're just going to get a uh single ASIC blob on there. So, yep, I reckon they've gone to the trouble of that. Not much else in it, is

**Dave Jones:** there? Wow. Like they've gone to the effort to put the speaker on the back, you know, I Instead, got to wire that over. And of course, you don't want any of that screw rubbish. You just uh get the soldering

**Dave Jones:** iron down there and uh just melt those heat stakes to uh keep the switch in place. Same thing for the speaker as well. No wackers. And there you have it. We've got one of those dodgy uh tab connections again. So,

**Dave Jones:** yeah, that's probably it. And of course, uh to get you a single-sided board, they couldn't get it all on a single-sided layout, so they've used some carbon jumpers on there. So, that uh extra process layer to put the carbon traces

**Dave Jones:** on there is going to be cheaper than doing a double-sided board with uh plate through. And that's, you know, that's probably the case when you're talking about these things. They're probably manufactured hundreds of thousands of these or a million of these things. So,

**Dave Jones:** yes, it was a uh is a black blob. And uh so, that's uh chip on board. That's a They just uh glue that straight on there, and then they start bond wires going over to the pad. Then they just

**Dave Jones:** gunk the whole lot. Got a uh SO8 package happening there. Have to look at the part number there, but we've got a regulator. And uh well, yeah, not much else is there. But, that's all you need. So, yeah, they developed custom ASIC for

**Dave Jones:** that Well, I presume it could be uh like a uh pre-programmed uh micro uh microcontroller. Like, it could just be like a a big memory, big flash memory arm uh processor or something like that. May not be one of the mainstreams ones.

**Dave Jones:** Maybe one of those uh uh obscure uh Chinese brands or something. And then they just get it in die form and blob the whole lot. So, not necessarily an ASIC under there. You can't make that call unless you actually know what's

**Dave Jones:** going on. But, anyway, uh I think the fault's almost certainly in our tab connection there. Groan. Seen that in many videos before. All right, let's see what happens to that screen if I push down on the connections. Just use my thumb at this stage.

**Dave Jones:** Nothing. That's interesting. Hmm, got to get my poker. Wow, no, it ain't that. It ain't a bad connection cuz that that's actually soldered. Yeah, that's actually soldered. That's actually not a conductive adhesive. So, it it ain't that. Is it inside the screen?

**Dave Jones:** Is it a bad die bond in there? What's going on? And you can actually see the COG chip on glass up there. That's our driver chip. That's actually embedded on the glass. And like if I put physical pressure

**Dave Jones:** on there, so it's not the this would be conductive adhesive. But it ain't that. It ain't that cuz they've gunked the whole lot of that. So, um yeah, it's something else. Aha, Winbond. Um not necessarily an obscure brand. Yeah,

**Dave Jones:** so that's an external flash memory by the looks of it. 25064 or is that Q64? All right, I'm going to see if it's a thermal thing with the die bond under there. Going to get my freezer spray, uh air duster

**Dave Jones:** turned upside down. Instant freezer spray. Nope. What? Chilly finger, chilly finger. It ain't that. No, it wasn't that. Let's try the LCD connection.

**Dave Jones:** Nope. It's nothing thermal. Well, thermal doesn't fix it anyway like a bad connection or something like that causes it to get worse or get better. So, hmm. All right, so the next thing I'm going to suspect is the solder connections on

**Dave Jones:** there. So, they look a little bit how you doing, don't they? Hard to tell. Really got to get them under the microscope. You could have a micro crack in any one of those. Of course, you can uh can check those manually. You can just

**Dave Jones:** buzz out each side of that fairly conveniently. And that's a pretty quick, easy test. So, I'd probably do that as a matter of course or you could just simply Oh, it just stopped playing. Oh, auto turn off perhaps? Yeah, so or

**Dave Jones:** you could just go reheat them all, but I might just buzz them all out first. And not sure if you can see that on camera, but I tried to probe this and you can't really cuz you can see that hopefully

**Dave Jones:** that there's a whole bunch of uh uh gunk covering that. So, you can like Yeah, you really need sharp probes to uh pierce through. It's uh It's really annoying. They've put like a a It's almost like a glue type stuff on top.

**Dave Jones:** Hmm. Well, this is getting nasty. I just resoldered all the connections on there. And we've got the exact same problem. I I I went through and reheated them all. I just What you do is just get in there with your iron and you just

**Dave Jones:** drag them like that back and forth. And it exactly the same problem. And I did it twice. So, you'd think that the odds are that if there was a bad joint on there, it would have either got worse

**Dave Jones:** or gotten better. But no, it's exactly the same. Hmm. Is there a uh little micro crack in the ribbon, perhaps? Wouldn't be the first time I've encountered that, but I've been wiggle, wiggle, wiggle year in, and I I just

**Dave Jones:** can't Oh. Can't get anything to anything to happen. So, it's not like it's a bad contact or intermittent contact somewhere. Oh. I just threatened to get the oscilloscope out, and uh it I turned it on, and it just went

**Dave Jones:** It didn't It didn't play. Oh. I swear. Whoa. Something's going on. Whoa. Yeah, something's happening. Give the board a flex. Yeah. Something's dodgy. Let's try flexing that board, cuz that'll affect the that black gunk isn't perfect. There'll be some flexion in there,

**Dave Jones:** and the bonds might not If they're intermittent, they could come a gutter. But no. No, that's okay. Whoa. But that screen is doing that, and it's resetting, and it's flickering. So, hmm. Something very wrong with this LCD. I'm

**Dave Jones:** playing a game at the moment, and I can't see a thing. So, it's not like the it's the just the stripes. And if you have a look on the edge like that, when you put it on the side, you can actually see it.

**Dave Jones:** Can I select that? Continue. Start. There you go. So, you can like straight on, can't see a thing. It practically vanishes. And on the side, you can. It seems to be You know, it's it's kind of mostly working. There's some ghosting

**Dave Jones:** stuff happening there, but there you go. So, that's really interesting. What's going on? And what do you know? What what what what? I dropped it, didn't I? I wasn't moving stuff on the soldering bench, and it dropped off onto the floor, and

**Dave Jones:** that's the result. So, yep, cracked the LCD. There's just no point fixing it now, so I'm going to leave that. I couldn't be bothered, and yeah, goneski. I'm afraid. And yeah, I'll just dump this on the second channel. So,

**Dave Jones:** ah, well, that sort of stuff happens. Anyway, if you got any idea about the about the lines on there and why it's faded like that, let us know. We could have got into like the drive voltages and all that sort of jazz in

**Dave Jones:** there, but yeah, I no no. Not going to waste any more time on it. Catch you next time.
