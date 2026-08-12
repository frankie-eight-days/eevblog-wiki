---
video_id: C7nBF9bkG5Q
title: EEVblog #781 - Samsung LCD TV Part 2
url: https://www.youtube.com/watch?v=C7nBF9bkG5Q
source: youtube-asr
---

**Dave Jones:** All right, we're back on this Samsung dumpster dive 46-in LCD TV and it might look a bit funny because here's the frame. It looks like it's the front, but you can see the circuitry because we've actually taken off

**Dave Jones:** the front bezel here um with all the associated I'll flip it around with all the associated uh front panel uh stuff on it. It's got the uh the LED down here. It's got the speakers over here and here like the bottom

**Dave Jones:** speakers. There's speakers on the back. Uh of course they're like the uh subwoofers on the thing for the uh low frequency performance, but it's got four speakers here and it's got um the uh sensor board in here as well. So, that's

**Dave Jones:** all capacitive uh touch sensing under there. So, that just came out easily with uh four screws. Unfortunately, one of the uh mounts for that actually broke off. So, um yeah. Oops. So, I'm not sure if that's indicative of uh the issue

**Dave Jones:** we're having, but what I believe the issue is, I'll link in the previous video if you haven't uh seen this thing. Uh we couldn't really fault the power supply. All the uh measured values on the uh T-con, the timing control board

**Dave Jones:** here, all looks fine. Voltages over on the main processor board look fine. So, it all points towards the panel itself. Now, I've actually um well, what happens here Okay, you got your main processor board. Signal comes across this flat flex here.

**Dave Jones:** I've played around with these connectors. Nothing doing there at all. And then you've got the timing control board, which actually uh outputs all the timing and video uh signals for all of the LCD information. Now, because this is a full HD panel, there's a um 1920 by

**Dave Jones:** 1080. So, it's got 1920 columns. So, if you actually uh count the number of conductors in there between these two cables going to the panel, there's of course not going to be uh 1920 uh columns on there for the damn thing,

**Dave Jones:** right? Let alone the horizontal stuff. So, um, yeah. So, these actually go to little boards. You might be able to Here we go. I'll see if I can, uh, get the camera over. You might be able to see that little board in there.

**Dave Jones:** You see that board? There's a board which will runs all the way along here. Goes all the way right out to either side. So, there's two boards that, uh, go in different directions like this and they would have all the column drivers

**Dave Jones:** on them that actually, uh, go down. So, it's most likely that they're, uh, the way this thing is constructed is that this connects up into here and then you've got this, uh, I don't know, we'll call it like the driver board or

**Dave Jones:** something that is tucked away inside here and then there'll be multiple flat flexes again with like a hot bar, uh, solder attachment probably direct to the flat flex bonded flat flex bonded directly onto the, uh, PCB itself using,

**Dave Jones:** uh, hot bar technique it's usually called. That's most likely. I don't know. I haven't opened up this one, a particular one before, but there's probably a few of them along there and then these and there'll be circuitry to

**Dave Jones:** actually demultiplex, uh, that stuff into the panel. Or the panel actually, uh, could have, uh, the circuitry on the flat flex, uh, itself. That would be like, uh, chip on flex technology or something like that. So, I think there's most likely to be an

**Dave Jones:** issue right up here. Yes, I have actually, uh, you know, fiddled fiddled around with these and reset them and everything while the, uh, TV's going and couldn't see any difference whatsoever. So, it's not that. So, I think it's

**Dave Jones:** further on inside the panel. So, what we're going to try and do now is, uh, somehow, get access to that so we can actually see and, uh, play around with those potentially. And there's the whole front panel. It actually looks rather

**Dave Jones:** jazzy on its own. I I really like it. It's sort of like a shame to put the, uh, glass around on thing. Actually, looks kind of like, I know, industrial. David, too, what do you reckon? Way better. Way better. He thinks it's way better

**Dave Jones:** than having the wanky glass around the outside. Yep. Yep, absolutely. All right, so this has screws in here, and uh if we take those out, maybe this top this whole top bezel will uh lift off, and then we'll uh

**Dave Jones:** should be able to see the uh flat flex connections. Let's give it a go. Yeah, yeah, there we go, we got it. Oh, we're in like Flynn, and it's exactly as I said, there's a few more than what I

**Dave Jones:** thought, but I'll show you that in a sec. All right, here we go. Exactly as I suspected, there's actually um 16 of these uh flat flexes. Yep, they are hot bar attachment, just as I suspected. I'll show you a close-up in a sec, and

**Dave Jones:** they've got the chip on board decoder as well. So, 1,000 uh so, if these are all column uh drivers, then it's a full HD is um 1920 uh columns, 1920 pixels across like this. So, um divide that by 16, that's 120.

**Dave Jones:** So, there must be a driver chip in there embedded on the flex, which drives 120 columns like that. So, here it is. Here's the flat flex coming over from the T-con board. You can see that that's hot bar soldered directly down to there.

**Dave Jones:** The reason that they Well, it's actually like, yeah, reflow {slash} hot bar. The reason that they call it hot bar is because uh during at the uh PCB assembly house, they like literally have a bar a metal bar that comes across, and it's

**Dave Jones:** hot, and it you know, they have a jig which comes in, and then just presses, you know, down onto there like that. They sort of, you know, have little jigs to align it all up, and then the hot bar

**Dave Jones:** just comes down and boop, and then just solders everything in one operation. So, they've done that, and there uh for the um that's for the T-con connection, and then these all split out to these, uh, 16 different flat flexes here. Once

**Dave Jones:** again, hot hot bar attachment, don't trust that any further than I can throw it. This one looks solid. Look, you can see the solder fillets in there, kind of. I might get the macro lens out in a second, but these ones These ones are

**Dave Jones:** definitely hot bar attached, and they just don't look as solid as these ones down here, but and much higher density, of course. So, you know, there could be something wrong in here, or I can show you, well, because it's on the top, I

**Dave Jones:** can show you the underside of the chip up here up there. That's a chip, actually, driver chip embedded onto the flat flex. So, there we go. That's a closer up shot of that, and you can really see the difference in the

**Dave Jones:** pin pitches on those, too. So, the one the bottom one's the one coming from the T-con board, and I've got high confidence in that. As I said, like I've wiggled that around and everything, but yeah, as far as the column issues we're

**Dave Jones:** seeing, um, there could be a tab connection issue along here, or it could be the, uh, chip on top and the bonding and all that sort of jazz. You'll have to excuse the video here. I've got to look through

**Dave Jones:** this mylar flat flex, or whatever it is, and you can actually see the connections. You can actually see some test pads in there that they've got. So, this is the underside, and that chip is actually a physical, like a large chip like that.

**Dave Jones:** It's actually physical the die is physically long and, uh, thin like that. So, that that's just the way it's organized logistically to get all the traces out the other side. So, these So, you'd have it See, you've got a

**Dave Jones:** relatively small number of traces coming in here, okay, like serial input or whatever it is, and then huge then you'd have like the 120 traces coming out the other side, which you can't see at this uh, angle. So, that's why they've

**Dave Jones:** actually manufactured the die like that. Now, the interesting thing about all this is you're probably wondering where are the horizontal drivers? Well, the I'm I think this is the vertical driver chip on here and the horizontal might actually be coming

**Dave Jones:** perhaps directly from the T-con. You can actually maybe if you look closely, you can actually see some traces then bypassing the chip and going out into here. And then we've got another connection there. You can see that on the They're all

**Dave Jones:** little traces running through. There I showed this up in minute detail in previous videos, but yeah, there's got to be some traces snaking around the side of this whole thing for the horizontal the horizontal lines as well because you

**Dave Jones:** can't just have column drivers. You've got to have intersecting horizontal ones as well. Now, you can actually this is the corner of the glass LCD. You see some traces snaking their way around here. Here you can probably see like the individual

**Dave Jones:** pixels in there now. If we uh maybe if we Yeah, yeah, you should be able to see that. There we go. All the individual pixels. Hard to tell on my LCD screen here. Yeah, there we go. You can

**Dave Jones:** see these traces actually snaking around the side like this and going all the way down to the horizontal down here. So, I'm not sure if there's any chip on glass drivers under here for the horizontal. So, I'm not actually sure

**Dave Jones:** sure of the exact mechanism they're using there to get all of the 1080 traces that they need to. They might be doing half on one side, half on the other maybe. I'm not sure of the mechanism. Can't really get the entire

**Dave Jones:** glass panel out to take a look. Now, if we actually zoom in on the side here, you can actually Look. Look at that. You can almost see You see something in there. Something very strange and staggered. Three It's almost like there's wires

**Dave Jones:** jumping over. It almost looks like they're jumping over like that and making connections. So, yeah, I'd love to see more detail, but it's actually really difficult to manipulate this thing under the uh microscope. And you know, at at this

**Dave Jones:** angle, you might actually even be able to might come out better, but uh That is That is fascinating. Look at that. It's a staggered arrangement of three. And somehow, they're getting all of the horizontal drive out of that. All right,

**Dave Jones:** here we go. We've actually powered the thing up without its front panel bezel, so it doesn't have like the front panel power capacitive touch switch. Doesn't have the front, you know, all the touch switchy stuff. So, it obviously didn't

**Dave Jones:** need that to power up. Now, you can see the clear vertical stripes here. So, now it's time to poke it. So, let's give it a burl. Let's uh touch our our flat flex up there. Put some pressure on that hot bar.

**Dave Jones:** Uh uh Nothing. Nothing. Okay, let's go to these ones over here. Well, I'm starting to think it may not be the I'm starting to think it may not be these, either. I would have expected Yeah, if you push these down, maybe.

**Dave Jones:** Yeah, no. I But but but but but but Yeah, these are separate boards. Yep. They are two separate boards. And those are two separate ribbons. Yep. So, you'd need It looks like two separate failures. Okay. We might be wrong. It may not be

**Dave Jones:** these connections. So, They They're They're are solid. They're pretty solid. I'd expect to see something something change in there. But, uh not a sausage. No, that is rock solid. So, is it is it the T-con? Is there something wrong with the T-con

**Dave Jones:** board? Cuz it doesn't look like there's anything wrong with these flat flexes. As you saw in the previous video, we actually uh got out the thermal spray the uh freezer spray and we uh and we froze those big

**Dave Jones:** uh ASIC chips on there and it didn't do anything. So, there was any sort of uh you know, dry joint BGA uh issue, then that it doesn't always show up with the uh freezer spray, but you know, odds are

**Dave Jones:** that it uh should have shown something and it didn't. So, I don't know. There you go. So much for the uh flat flex uh theory. Hmm, bummer. Love the relays clicking. Yeah. I don't think I trust a product that

**Dave Jones:** doesn't have relays. Just instills confidence in you when you power something and relays go click click click. What are they using them for? Uh main input mains. See that? See Yeah, see it's not there. Look, and then it started.

**Dave Jones:** Then there's some couple of little red dots there. Uh and then then it started There it is. It's coming in. Is there a video like filter? Is there something like Yeah, no, because this doesn't pass through any analog pass. It's It's

**Dave Jones:** entirely It's entirely digital and this and it remains regardless of where the of what uh you know, we do the test signal and it's still there as well. So, Look, yeah, that's so that that is very very strange.

**Dave Jones:** It gets way worse. Does get worse with time. So, that's not indicative of a flat flex issue. So, there you go. We'll have to choose a different path. Choose your own adventure. Right, we've got a theory because those horizontal lines went They

**Dave Jones:** were common all the way through and we've got two separate boards like this. It's effectively split it. Um so, it seems to be happening further back in the chain somewhere. So, what we've done is we've disconnected this side

**Dave Jones:** of the panel and we'll see what happens. Apply power. Physically disconnected this side. So, here we go. Can you Yeah, I can see Yeah, there we go. So, we're still getting the lines. We're getting half those lines. Yep.

**Dave Jones:** Now, we go. But, all the horizontal lines are still there and the vertical lines are all still there. And we'll do the other one. So, it's Yep, we'll just uh swap that over. And of course, I think we'll see exactly

**Dave Jones:** the same thing, but this half will work. So, that in that will indicate Yeah, you can see it coming. That Look, see how it fades in, though? Seems worse. That greeniness. Yeah, that's Yeah, it does kind of seem

**Dave Jones:** worse. And also, we noticed before that a couple of these little pixels up the top here for this red bar, they were like start like it would like vanish off and on. So, That's worse. It was weird. It's worse?

**Dave Jones:** We're not getting a menu. And we're not We're We're not getting the menu signal, right? No. I don't know. Where's the should be half a menu there. We're not getting a menu. All right, so we've got it back.

**Dave Jones:** Yes, bare feet. And yeah, Dave wears socks. He's complete weirdo. I David, sorry, doesn't like being and Dave.

**Dave Jones:** Now, here it comes. Here it comes. Wait for it, folks. Wait for it. Fading in. Fading in. That is not indicative of a uh panel fault. That is not indicative at all, I don't think. And look at that. The bars are back.

**Dave Jones:** Yep. Yep. It's different. It was Yeah, it was more solid before and we got no menu. Why weren't we getting the menu? I mean, plugging this side. So, I'm not sure the exact, you know, mechanism between horizontal drive. Maybe there was no

**Dave Jones:** Yeah, I think what was happening maybe that side is controlling more of like the the horizontal or more of the horizontal or something like that. I don't know. I haven't thought about the architecture of the driving mechanism behind it yet, but

**Dave Jones:** I I've got high confidence in the panel. I I I'm not suspecting any of these uh flat flexes at all or the um chip-on-flex drivers or the hot bar attachments. I'm not suspecting those cuz we have fiddled and diddled with them and nothing.

**Dave Jones:** So, we're sitting here thinking I think we both agree it's got to be the T-con board. Because if it's a processor board, um yeah, I like you wouldn't be getting the menus. It's probably in serial. They're probably be like eight I I

**Dave Jones:** reckon there's like you know, a bunch like eight or 16 or something differential pairs over that sexy ribbon cable that we showed in the back that connects the processor board to the T-con board. And if it was serial problem, you'd

**Dave Jones:** expect a really widespread errors. carnage, right? There'd be carnage. You wouldn't get the menu with you know, doing all its funkiness. Although, if you remember in the first video, which David too has not seen, um the we were getting the ghosting, a

**Dave Jones:** weird ghosting on the menus. So, That's gone. And that's gone. I only saw that once. So, but I did capture it on film. Mhm. Celluloid. You know, we shoot this in like 70 mm. And we're using the eight-track sound system, you know, so

**Dave Jones:** This this camera takes up half the lab. It's crazy. Yeah. So So, if you want the original source footage for the videos, just send me a self-addressed uh stamped envelope and I'll send you the original eight-track tapes and tapes and uh

**Dave Jones:** Do that again. Ghosting's back. Ghosting's I What did you do? I I I DON'T KNOW. I DA- DAVID was tapping something. I was tapping was tapping something. I remember I was like tapping the ground or something. I was tapping something.

**Dave Jones:** What were you doing? God. Any changes? No, no. It was It was like plastic tapping, like that original one. Like do do do that first tap you did. I I can't remember I don't remember. I wasn't I wasn't taking it seriously.

**Dave Jones:** What was I doing? Dave was zoned out tapping the back of the TV. He found whatever the hell it was. Oh, we do know that I don't know if you can see me. I'm boo. Um we do know that the Yeah, the main

**Dave Jones:** ASIC on the processor board is driving a whole bunch of differential pairs, as you'd expect, over that main cable, that black cable we saw inside, over to the T-con board. Um it's being driven directly. That sounds like the tapping that you

**Dave Jones:** were doing. Yeah, okay. That sounds the same. Okay. Well, that's the main ASIC on the processor board. Although, I was shortly before that spraying some of the memory, some of the um ASIC memory that's surrounding it. So, Yeah, it only takes one bit to get every

**Dave Jones:** second. to get issues. Yeah, every second row or some row missing. Yeah, that's right. Yeah. So, I don't know. Is our money now on the processor board? You were definitely tapping the processor board, right? I was. Yeah, I haven't been tapping the

**Dave Jones:** T-con. Well, we've got to choose something, either the T-con board or the processor board, and of course we're going to choose wrong. Murphy will ensure that happens. So, we're going to um like usually like T-con boards are more

**Dave Jones:** popular uh failure modes, in fact by by far the most popular, but we do suspect something on the processor board cuz we were tapping around here and we made a difference and we were freezing around here, made a difference. So, we don't

**Dave Jones:** like the look of the So, we think it's either the ASIC or it's the memory. And little pain in the ass BGA memory chips in there. Uh they're actually easy to reflow. We don't have to take the board

**Dave Jones:** out or anything like that um cuz they're a low uh thermal mass, everything else, you know, we don't need a preheater underneath or whatever. Or we'll just preheat on the top a little bit, then we'll go in for the kill doing those.

**Dave Jones:** And um yeah, so that's really quick and simple just to rule out those memory chips there. So, we'll just give it a go. Um you know, I don't like our chances, but uh Are you feeling lucky? Plug. No.

**Dave Jones:** Go for it. Plug it in. Is that a camera between your legs or are you just pleased to see me?

**Dave Jones:** All right. We have um what we've done is we've uh reflowed, reheated the um the DRAMs. The uh surrounding the Is our yep, our friend the red. Yep, no. It's exactly the same. All right, so we reflowed those uh

**Dave Jones:** memory chips and nothing. What? Thanks for playing. And the other thing we're perplexed about is why it only seems to be get Well, vertical issues here only seem to be on things which line up with ASCII characters. You see we've got our

**Dave Jones:** characters here, and the vertical lines like are each um a line with each ASCII character. The PC over here is like orange, but we're getting like red or it's what's What is it? Yellow? Um but we're getting the red

**Dave Jones:** stripes lining up with the ASCII characters. And this one's interesting. Lines up with our um uh colon there, but we don't have um Oh, no, no, there is a faint one. Extremely faint. Yeah, there is a faint one trailing

**Dave Jones:** the outer pixels of those two characters. So, maybe it's like it's almost as if like the density of the character is causing a uh you know, a vertical stripe issue. It's just bizarre. See, but we don't get anything

**Dave Jones:** on these vertical lines here. Which is solid bars. Which is Yeah, yeah, big solid bars. So, it's like graphical. It only happens on the text insertion side of things almost. Like, you know, plus we're we've still got the

**Dave Jones:** issue with the horizontal lines, right? But that may be may or may not be related. They could be two separate faults. Who knows? But one of them seems to be definitely related to ASCII characters. It's weird. You can see we've got a

**Dave Jones:** different menu up now. We've put the bezel back on so that we can access the menu. And see, it follows the uh It follows the text and menus and things like that. So, it's really it's really rather bizarre. And it stays

**Dave Jones:** there for a bit. And then we can eventually get it to do other stuff. It's just uh there's something sticking to all the menus. Something like that, anyway. All right, I'm starting to strongly suspect this uh T-con board now. I I it

**Dave Jones:** might be a red herring with the uh tapping on the processor Um board making it go completely away. Although we did see it go completely away. So anyway, T-con board could be a bad BGA joint under either the memory or these two A6 here. It's

**Dave Jones:** you know, unlikely to be these flat packs and things like that. These BGAs are classic culprits for that. I've already actually reflowed the two memory chips here and it didn't do anything. So the next step is to get medieval on its

**Dave Jones:** ass and whack it in the reflow oven. I'll put it through a standard temperature profile. I can't remember what temperature profile I've got set up for this beta layout one as you've seen in a in a previous video. But yeah, it's like a pretty

**Dave Jones:** stock standard temperature profile. So it should work the business for this. I'll just whack that in there and it'll take you know, 5 minutes or something. Hopefully heat everything up, reflow all the joints and if there's any problem in

**Dave Jones:** the joints at all, hopefully it would fix it. Fingers crossed but I don't know. I don't think the chances are too high. I'm not sure what the actual fire modes are with this particular T-con board in particular anyway, but yeah, I mean T-con board

**Dave Jones:** classic culprit in this scenario for the LCD. But yeah, I've like you know, I've tried the flat flex ribbon. I've been I've gone to town on this flat flex and I can't find any issues barring going in there and actually measuring the receipt

**Dave Jones:** getting differential probe and measuring the receiver points and everything to make sure everything's okay. Easier just to reflow the thing. So we'll give that a whirl. And yes, this is actually a double-sided load. So you know, ideally you want glue

**Dave Jones:** on the second side components. Can't actually see any glue on these puppies. But anyway, we'll give it a go. Most likely there is cuz they might have tiny little dabs of glue on them. Hopefully, anyway, the surface tension of the solder should

**Dave Jones:** keep the components there on the bottom. They're only very low mass components. So, yeah, fingers crossed yet again. And if you haven't seen my little Beetle Layout Reflow Controller before, it is quite nice. So, you can buy it from

**Dave Jones:** Beetle Layout and it's got a learn mode as well where you can actually set up the thermal profile for your particular oven, which is excellent. And I just whacked the I've already like pre-programmed this for a solder profile

**Dave Jones:** for this oven. So, at the moment it's in a preheat mode and it'll go into soak, then this is where the reflow happens. It gives like a little peak to the temperature profile, then dwells for a while, and it's all finished. So, well,

**Dave Jones:** it'll take a while. There we go. It just finished its reflow process and little bit more left. As you can see, it's up nearing up around 230° C in there, give or take. And the only real problem with these toaster ovens is that

**Dave Jones:** they don't cool down very quick. So, the way you fix that, we're finished now and we can just woo open the door. All right, here we go. We've reflowed that T-con board. So, if there were any bad solder joints on

**Dave Jones:** there, hopefully, you know, it might have done something, reflowed them, as the name suggests. So, let's give it a whirl.

**Dave Jones:** I don't think we'll get that lucky. Um but you never know. Never know. No. No. No, I can still see some horizontal stuff happening. No. I think we'll see our red stripes come back. Yep. Yep. Yep, yep, start.

**Dave Jones:** No, there you go. Reflowing the T-con board. Didn't do a thing. Well, the good news is didn't damage it. Hmm. I just wanted to point this out. Look at the beautiful length matching on these uh LVDS differential pair traces here.

**Dave Jones:** Check this out. You'll see because of the shape of the thing, okay, the shape of the thing the um the pair on the inside here is going to be a little bit shorter than the pair on the outside.

**Dave Jones:** The pair on the inside here will need a lot more wiggles in it to actually get a longer length to match the outer one. So, if we actually zoom right in here, you can see that these outer ones, see

**Dave Jones:** they have little wiggles in there to match the length, and the outer ones actually stop there and there, and it gets progressively shorter. They stop at different lengths until So, this pair in here is the exact same length as this pair out here so

**Dave Jones:** that the timing between all the data is exactly the same. Very nice. Well, there you go. I think I've had about enough again for today. Haven't spent all day on it, you know, spent like half an hour on the damn thing, but anyway, um yeah,

**Dave Jones:** I don't know if anyone else has got any good ideas about this, let us know. We might have to start cracking out the scope or something like that. Geez, that's a bit rough, but yeah, reflowed that board. Could reflow the processor

**Dave Jones:** board as well. I don't want to do that right now. So, anyway, I'll just leave that video here. I don't know. That was just like half an hour of us just bumming around with this monitor TV. Sorry. Anyway, if you liked it, give

**Dave Jones:** it a big thumbs up and all that sort of stuff. Catch you next time.
