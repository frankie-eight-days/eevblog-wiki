---
video_id: JvYA4X58Xuw
title: EEVblog #401 - Lecroy 9384C Oscilloscope Repair - Part 2
url: https://www.youtube.com/watch?v=JvYA4X58Xuw
source: youtube-asr
---

**Dave Jones:** Hi. Yes, we're back on the Lecroy oscilloscope PCB short slash repair because I had so many people saying that they wanted to see the follow-up to this because I couldn't find the fault within the hour that I had last time.

**Dave Jones:** You I'll link in the previous video if you haven't seen it. It is a must-watch. You can't This probably won't make much sense to you unless you watch the previous video. So, I thought we'd start again because we

**Dave Jones:** got to the point in the previous video where we found that the we we had a you know, a 0.1 or thereabouts short across the 3.3 volt rail on here and we tried to track that down and I explained how

**Dave Jones:** the usual culprits are the either the bypass caps or you know, one of the semiconductors or something like that. But of course, I sucked off what I believe were all of the bypass capacitors on the 3.3 volt rail

**Dave Jones:** and the short was still there. And then I did some quick thermal temperature measurements of the only four devices which seem left on the 3.3 volt rail, which are these ASICs here because I don't have the memory modules plugged in

**Dave Jones:** and they were all at at the same temperature pretty much. So, one of them didn't really stand out, you know, that was hotter than the others and I couldn't find any other place on the board just you know, using my hand just a quick

**Dave Jones:** look. You know, a quick feel around on the board to see if I could find any hot spots, but there has to be one here because as I mentioned in the previous video, the 3.3 volt rail is only capable

**Dave Jones:** of 6 amps the actual power supply and we applied external 3.3 volts and we'll get in 11 amps. So, that extra power has to be going somewhere and has to be heating something up, you know? I can't do a Scottish accent, but you

**Dave Jones:** know, you can't defy the laws of physics, Captain. It's got to be there. So, there's extra power now. So, there is definitely a short on this board. Contrary to what a lot of people said, a lot of people

**Dave Jones:** mentioned that oh no, it's probably normal, you know, and that power supply is capable of more and they did all sorts of thermal, you know, back of the envelope calculations to sort of convince themselves that that was the case. No, I

**Dave Jones:** can assure you there is a short on this board somewhere and that is obvious. A typical system rail on this board, like a typical 3.3 V rail will not measure 0.1 ohms both directions on a multimeter with different multimeters showing no

**Dave Jones:** capacitive charge up at all. You know, that is just not normal. There is definitely a short on this board. And um thanks to uh Sam at uh the Lecroy um uh users group, there's a Yahoo users group specifically to these uh scopes. He

**Dave Jones:** measured uh the rail and confirmed that it was above 1 ohm. So, there is definitely a short there. So, let's find it, shall we? It can't be that hard. Now, um well, it it can't be that hard. Well, we'll find

**Dave Jones:** out, right? As I said, these heatsinks were all the same temperature. So, what I'm going to do is I'm going to use an IR thermometer and we'll go in there and we'll double-check those and we'll look around the board with one of those cheap

**Dave Jones:** IR thermometers which uh everyone probably should have in their kit and see if we can find something because there's got to be something on this board on the 3.3 V rail dissipating that extra power. Now, quite there's a few

**Dave Jones:** people who said yeah, it might be some sort of latch up to another rail cuz I'm not powering the other rails and stuff like that. Well, yeah, that could be the case, but that doesn't explain the 0.1 ohms. And when you find a gotcha like

**Dave Jones:** that, you should track it down. That's why in the previous video, that's entirely what I focused on because if you can't find that 0.1 ohm short, nothing else matters. So, everything will be a red herring in terms of

**Dave Jones:** drawing the extra power. Now, it may be the case that there is some of that extra power dissipated in the other rails cuz it's protection diodes and stuff like that cuz we haven't powered up the extra rails, etc., etc. And that

**Dave Jones:** could be the case, but there is definitely some extra power being dissipated there. So, I expect there to be something else on this board that's heating up. Now, let's just do a quick recap here. I got my external high current supply at

**Dave Jones:** 3.3 volts. Says 3.2, but it's near enough to 3.3. And it's drawing about 11 amps, which yes, if you take the 0.11 ohms short, it should be drawing a lot more than that. And people said, "Aha, there's you know, there's something

**Dave Jones:** wrong there." But no, it is a short. That is very common and expected in something like this. You would expect the resistance to heat up and have a temp co like that. It is very, very common and then the current drop. Just

**Dave Jones:** because we measure 0.11 ohms at, you know, the milliamp or to that this multimeter is going to measure that current at, doesn't mean that resistance is going to stay the same at 10 or 11 amps. It's not. So, I would expect it

**Dave Jones:** not to match up with Ohm's law in that respect because the short is going to be non-linear and in some respect and and or it's going to have temp co and it's going to heat up. So, that is

**Dave Jones:** perfectly normal. So, don't worry about that. Now, a few people wanted me to measure the voltage over here as well. I don't think we'll get too much drop in those leads, maybe a few hundred millivolts. Let's have a look. There you

**Dave Jones:** go, 3.05 volts. So, really, you know, it's not a huge it's not a huge drop. It's It's not a huge drop there at all. Now, I've only had this thing on for a minute or two, but let's have a look at

**Dave Jones:** the temperatures of these heat sinks again. I've got my little Fluke 59 mini IR thermometer here, and that will tell us the temperature on those heat sinks. Now, I think I was getting around about 70° or something before after they

**Dave Jones:** heated up for quite a few minutes. And yeah, I have no idea if this is regular operating temperature or not, whether or not the clocks are working, whether or not you need the other power rails powered up, whether or not you need the

**Dave Jones:** processor board. It doesn't matter, okay? We're looking for a temperature differential between these heat sinks. So, let's measure that. You know, it's going to peak at about 60 there. That one's very similar, around 60. This one here is Yeah, it's around 60 as

**Dave Jones:** well. If I can get it, yeah, 65. So, there's not a huge There we go, 63. You know, it's quite hard to get it with these things, but you know, I would expect one of those to stand out. So,

**Dave Jones:** really, there's no temperature differences between those. Forget it, completely rule it out. Now, let's probe around other parts of the board and see if we can find it. Let's take the bench, for example, as a reference. It's 20,

**Dave Jones:** you know, 24, 25° for example, 27. I mean, we're we're going to get some heat coming off the heat sinks and stuff like that. So, as I said before, I don't think any part of all this stuff is

**Dave Jones:** powered up at all. So, really, I wouldn't expect to find and these once I think just we're getting some residual heat from those heat sinks there, but these ASICs of course aren't powered up. Now, there's one thing I

**Dave Jones:** wanted to check because we really have to go back to the the beginning here. We have to go back and consider that it could be a physical short. Now, in the first video I ruled that out because that is

**Dave Jones:** usually the least likely scenario for a product like this that used to work just fine. It was out in the field, worked for years. You know, they they don't just magically get a short in the power plane or the or a connector or

**Dave Jones:** something like that, but I want to go back and start at the connector here and have a look. Now, these um there's no surprises for guessing that these alligator clips here get reasonably warm because there's contact resistance in

**Dave Jones:** there. So, this thing's working 11 amps. So, they get quite warm, but um maybe you know, there's a short near it or under the connector or something like that. As unlikely as it seems, um we have to consider that because this unit

**Dave Jones:** has actually um had some physical shock or something to it. If you've seen the teardown of this, you'll know that the case has got a big crack in it and uh all sorts of things. So, it's most likely been dropped or something like

**Dave Jones:** that. So, maybe we've got some stress transferred onto the connector or possibly as a couple of people mentioned, the uh mounting hole down in there. So, possibly um there could be a short in there. Look at that. We might be getting some residual heat

**Dave Jones:** from the connectors there cuz the those connectors are quite hot, right? They're like 40 plus degrees. They're they're getting quite warm cuz there's fair bit of contact resistance in there. So, it's going to heat up. So, but that board

**Dave Jones:** next to it is getting quite quite warm. Hang on. 35 degrees and climbing on that on that pad down there. Look at that. 32. Maybe there's possibly some heat spreading through that ground plane. Possibly even all the way over to here.

**Dave Jones:** Because I wouldn't expect it that to be uh warm at all over there. But this one over here is definitely hot. There's something going on there. If you design this board properly, then these uh large uh mounting holes here, you should have a

**Dave Jones:** power plane pulled back, what's called pulled back from around the hole so that when, you know, you put screws in there and you tighten them all up, then it doesn't uh crush the power planes inside there. But who knows? Um you know,

**Dave Jones:** unless you had the CAD files for this thing and you can check or you dissected it or you x-rayed it or, you know, something uh like that, uh you don't know how close those are. So, it's not out of the uh you know, the bounds of

**Dave Jones:** possibility that when this thing was dropped, there could have been pressure on a through hole uh mounting uh pad like that and it could have uh crushed the internal power planes. This is a six-layer board, so there's not going to

**Dave Jones:** be a huge physical uh difference uh you know, a physical gap between the ground plane and the power plane. So, um it depends on what layer the 3.3-V uh one's on. Usually, it's going to be uh right next to the ground plane. So, um you

**Dave Jones:** know, with a very small amount of um FR4 prepreg between the layers. So, it's not out of the bounds of possibility that you could crush that due to something like that. So, what can we do to test that theory that uh it

**Dave Jones:** could be something to do something some sort of short on the power plane in there? Well, we can freeze it. We can cool it down and see if the current changes. Heck, it might even go away if you freeze it down enough.

**Dave Jones:** You know, the the short could actually vanish. So, if we're right, we might actually see that current change. Now, I don't have any freezer spray, but I do have air duster. So, what you do with the air duster is simply turn it upside down and

**Dave Jones:** all the the cold gas actually settles at the bottom and that comes out. Instant freezer spray. Cool down that pad and see if this current changes. You ready?

**Dave Jones:** No. No, nothing. It's not changing at all. That's strange. Would have expected something. Maybe our theory is not correct. You can actually see how it's freezing down in there. It really is a That is pretty darn cold. And if I get

**Dave Jones:** the thermometer on that again, you know, 16°, 13, 8. You know, it is very very cold that pad is now very cold, but it's still showing 10 and 1/2 amps. Hmm. Now, here's that pad up close and I don't see too much uh

**Dave Jones:** well, really any major compression trauma or anything like that on the on the pad. Well, and the same goes for the bottom there. I mean, it's not like, you know, somebody's like really screwed this thing up and and compressed those. You

**Dave Jones:** know, that looks pretty darn normal wear and tear on those mounting pads to me. So, um, uh, possibly in the connector. I don't want to have to, what, desolder the connector unless I absolutely, uh, have to. Now, they look

**Dave Jones:** okay, but of course they could, um, you know, it's it's a remote possibility, but we're getting down to that point where we have to look at remote possibilities. Now, I just thought I'd, uh, check something. Uh, these mounting holes, uh, that

**Dave Jones:** we're, uh, curious about to see if they're actually, uh, grounded. So, yes, they are actually grounded. There you go. Right. So, if there's not adequate, uh, plane pull back inside those things, um, they could, uh, certainly, um, you know,

**Dave Jones:** uh, compress or short out or something like that with, uh, physical damage. Now, I think we've gotten to the point where we probably have to, uh, power up the other rails as well and just, uh, see what our current draw is on that,

**Dave Jones:** uh, 3.3 V rail. And, yes, I've measured it and this, um, 3.3 V rail does seem to be dead on this power supply. So, um, the power supply seems to have, uh, died. As I said in the, uh, first video, it,

**Dave Jones:** uh, and the teardown, of course, it was actually working and then it died. So, I suspect that the short eventually, uh, killed the thing. Now, this is my theory on this. There is definitely a short on this board, okay? 0.1 ohms is not

**Dave Jones:** correct, right? It's just not. Definitely a short there. And the thing the power supply was good enough to continue to keep the thing basically working, but we were getting corruption on that 3.3 V rail, i.e. all the capture

**Dave Jones:** memory, which is kind of what we were seeing, um, in the, uh, data. So, all of the, um, all of the capture memory which runs from the 3.3 V rail, there's probably excess ripple or whatever was going on there. It was hiccuping or

**Dave Jones:** doing whatever. I don't know, but, um, it was um, so it was able to still power through that short just like our high current supply here can. It can still supply 3.3 volts, but it was drawing too much and it eventually got to the point

**Dave Jones:** where no, I can't take this anymore. Kaput, it's dead. Okay, so what we're going to do is um but all of the I have measured all the other rails and they all still work. So, I'm going to cut into this cable here,

**Dave Jones:** the 3.3 volt one. We'll power that from the external supply and we'll power up all the other ones as well and see what we get. Right, so what I've got now is I've got it powered up and we'll check the

**Dave Jones:** voltages on here. 5 volts, there we go. And we're getting minus 5 volts. So, all the other rails are all all up. Not exactly sure what they are, plus 15. So, the other rails are up, the plus 5 and

**Dave Jones:** all that and but look, it's still drawing 9.6 amps. So, there you go. That's busted that theory that um it was, you know, it was latching, you know, the power was latching into other unpowered rails through protection diodes and, you know, all that sort of

**Dave Jones:** jazz. So, my hunch was correct that there definitely is a short there and it's not surprising because 0.1 ohms is not normal. Now, um Sam has also confirmed that yeah, the 3.3 volt rail should be drawing about 6 amps. So, it

**Dave Jones:** is and he also said, as I said before, that it's, you know, it's over an ohm and, you know, when you actually measure it with a multimeter. So, there is definitely a short on this board. No doubt about it. Don't hear anymore. And

**Dave Jones:** just to doubly sure, yes, I've plugged in the processor board here and yes, we're still drawing 10 amps on the 3.3 volt rail. I just want to try this temperature again, but I'll leave the connector in now so that we've got the

**Dave Jones:** well, the uh pins going through to the power plane there. The third one seems to go off to somewhere else. And um and also I'm using the ground point over here. So, um we should get less heating on that uh

**Dave Jones:** on that pad due to the contact resistance we had before. So, we're still 33° on that pad down in there. So, whether or not that's actually normal um due to the um the the contact resistance of the connector at

**Dave Jones:** um 11 10 or 11 uh amps and then the uh heat is spreading through the power plane. So, you can see even this pad right down here, you know, well away from the ground point over here and the contact

**Dave Jones:** resistance over here is still you know, that's still 33°. So, clearly that's just the residual heat spreading through the power plane. So, it is not obvious yet where this damn short is. Now, a few people asked why don't I use my Aim TTi uh I Prober

**Dave Jones:** 520? It's because it's not really going to work. You're going to get positional issues as I've shown in the video for this rotational positional issues on this sort of thing. So, if you put it here, let's Okay, I've got it into the multimeter

**Dave Jones:** instead of the uh uh scope cuz we're dealing with the uh DC here. It's just fine. And if I rotate that, look at just the positional different like I'm not I'm just rotating that, okay? So, just the I just the you

**Dave Jones:** know, rotating that is going to be all over the shop. There you know, you're pushing uh the brown stuff up the hill with a pointy stick trying to use this thing, I'm afraid. It's not going to work. You could do it like using an AC

**Dave Jones:** uh method on the rail or something, but uh no, ugly. So, it's just simply not going to work when you have a huge power plane like this thing. So, no, sorry. As cool as this thing is, it's not going to

**Dave Jones:** do the job in this particular instance. Now, as I mentioned before, you can do the thing with like feeding a constant current through the thing and then using this um to measure uh voltage drops, but the problem with that is when you've got

**Dave Jones:** active devices on here um drawing huge amounts of current, you're naturally going to get the drops across here anyway. So, um you know, you're going to get the drops across the plane. So, here's our input connector, and all

**Dave Jones:** these four ASIC devices here are all drawing, you know, large amounts of current. So, unless you could uh isolate those, um it's going to be incredibly difficult to find the issue. Like, let's go from this cap here, for example, to

**Dave Jones:** this one. I think I've got the right one. No, let the other pad here. Okay, so just from one ASIC to the other, we've got a 13-mV uh drop there, okay? From there from there to there across the uh

**Dave Jones:** plane there, okay? 13 mV. And then if we go a bit more, we'll find that we've got more drop. Oh, wrong pad. There we go. We've got 40-mV drop across there like that. And then if we go over

**Dave Jones:** here, we're going to get a larger drop. Uh if we can get in there. There we go. We've got 81-mV drop. So, you know, how can you really essentially narrow that down when you've got such large currents drawn across a plane like that? It's

**Dave Jones:** very difficult to do. So, I don't think that's really going to work in this particular instance. It can work in other uh instances, but this one, not so much. So, we can do the same thing again with the um

**Dave Jones:** uh instead of the uh drop on the rail uh itself, we can get the voltage drop of the rail instead of the voltage drop across the the resistance of the tracks and the plane. So, we can start out over here

**Dave Jones:** and we're getting at the connector we're getting 3.032 volts input, okay? 3.0325, for example. And then let's go to our cap over here. Bang, it's dropped a bit. You'd expect that just due to the plane resistance and we'd expect it to drop a bit more.

**Dave Jones:** There we go, 2.96. As we go to this ASIC over here, 2.93. There you go, it is dropping as you progress across the plane like that. What does that tell you? Nothing, essentially. Now, if we scan over the board with our

**Dave Jones:** IR thermometer again, we can uh have a look, you know, 61, 63. It sort of peaks at 64. 63, similar sort of peaking, 65. Peaking there. So, you know, there's not there's nothing in that really. Go to the other ASIC, 63.

**Dave Jones:** You know, that's got slightly more heat sinking on that one, I think, so you'd expect it to be a little bit lower. But uh yeah, you know, like this there's not much in that one though. There's only Oh, no, there we go. We can

**Dave Jones:** get it going up to almost 60, something like that. So, you know, very similar temperatures across the board and it drops as you go away, for example, pretty evenly. As I said, that um temperature is going to be, you know, uh

**Dave Jones:** fairly evenly spread across that plane. So, trying to detect this is uh almost a needle in a haystack. So, this thing just doesn't seem to be doing the business. I mean, it's only a single spot. What we need is more resolution.

**Dave Jones:** Unfortunately, I I want to one of those multi-thousand-dollar um thermal uh IR cameras, but I know someone who does. Let's go.

**Dave Jones:** So, thanks to my mate Charles at Trio Smart Cow, purveyors of fine test equipment pornography, I have just that. Check out these puppies. I've got three um infrared thermal imaging cameras. Fantastic. We have a Flir E60. Um this puppy goes for about

**Dave Jones:** $12,000. It's a 320 by 240. It's the pretty much the Rolls-Royce in handheld thermal imaging uh cameras. I mean, Flir are the best in the business. And uh the E60 is the uh top of the range E-series. Ah,

**Dave Jones:** beautiful bit of kit. And check out this, folks. Look at this. Made in Estonia. Woohoo! Would you believe it? Ha! There you go. And then we have a uh ULIR Vision uh brand TI 160. These are much uh cheaper.

**Dave Jones:** Doesn't have the same resolution as um you know, the uh Flir, of course, but um still this one's much cheaper. I think uh Charles said this one's about 2,800 Australian dollars or something like that. Don't uh fully quote me on that.

**Dave Jones:** And then we have the same brand again, ULIR Vision TI 395. This is um I think a couple of thousand dollars more expensive than uh this one. And it's a gun-style one. And it's almost identical uh look and feel to the

**Dave Jones:** Senso Exakty camera I used to use for the blog. Check it out. It's like, you know, it's um these gun-style ones almost identical look and feel. Ah, man, I love it. So, that's a nice little uh funky form factor. I don't really like

**Dave Jones:** this form factor on here. In fact, I'm probably after I finish doing some thermal measurements of this, I think I'm going to do a separate video just playing around with this thing these things. So, I've only got them for the

**Dave Jones:** afternoon. So, I'll have a further play around with them later, but what we want to do now, we've got the right tool for the job now, folks, because this board if you remember just a few minutes ago, was uh, you know, we couldn't find that

**Dave Jones:** any hot spot at all apart from the ASIC. We couldn't find it like around the hole down there and the wires and stuff like that. It seemed to be fairly evenly spread around the power plane in this thing. So, let's

**Dave Jones:** power it up and let's, say, start out with the Rolls-Royce. Let's use the Flir E60 and see what this puppy is capable of doing. Welcome to the world of infrared, Flir.

**Dave Jones:** Just want to hug this thing. It's pornographic. It really is. Man, what a great toy. Let's start out by taking a look at our heat sinks. Ta-da! Here we go. And uh if I this is the focus on the front

**Dave Jones:** here. So, if I adjust the uh adjust the focus, we can see the temperature and you can see the spot measurement up there. We're talking, you know, 75 degrees. Something like that. I mean, this one's only 79, but this second heat sink here

**Dave Jones:** seems to be much Well, by much hotter, I mean, you know, 3 or 4 degrees hotter than uh what we were getting than what we get on the other ones. And considering that this one here is the same heat sink, so

**Dave Jones:** it seems to be a few degrees hotter. And this FLIR camera has various different modes, of course, which uh we need to investigate and look at, but you know, so that may I don't know if that um you know, says anything about my

**Dave Jones:** original prediction in the first video that that second device there seemed to have um a slightly lower resistance than all the others. So, maybe it's no surprise that it's getting hot, but um let's check out the resolution on this

**Dave Jones:** thing. It really is very, very, and I can take a can take screen captures of that and all that sort of jazz, so Right, so we know that those heat sinks are all um you know, pretty much identical temperature except for the

**Dave Jones:** second one there. Now, if we scan around the board, we can see our connector down there. If you have a look, um I've got the I'm I'm deliberately not um putting it right on the pins there. I'm deliberately getting it away, so we can

**Dave Jones:** uh look at the current flowing through those wires with the thermal imaging camera, and also we should see, you know, a hot spot around here where it's connected. Um but let's see if we can find a hot spot on there, and in

**Dave Jones:** particular that um mounting hole down in there. So, if we take a look around, that There you go, you can see the connector. And you can see the heat spreading out from from that connector there. I mean, that

**Dave Jones:** connector is getting up to 42°. It is It is actually pretty pretty darn hot. Now, if we have a look at the connector there, we can actually see You see how the two right-hand wires there are like that one's, you know, it's like 40°

**Dave Jones:** on those wires, and the one on the right-hand side that I said had no current flowing through it very little current, you can see that there is no current flowing through that other wire. Now, it's tricky to sort of get this cuz

**Dave Jones:** we are getting heat spreading from this heat sink here. So, it is it is rather a bit tricky. It spreads across, but you can see that there's no hot spot on that hole mounting hole down there at all. There

**Dave Jones:** is no hot spot. So, there's nothing going on there. You can actually see inside the inside the actual connector as well. If you can see inside that there you go. You can actually see the connections heating up inside the

**Dave Jones:** connection, but no hot spot on that mounting hole. So, that pretty much rules that out. There you go. So, it is not the mounting hole which a lot of people thought. In fact, the short doesn't seem to be anywhere else on this

**Dave Jones:** board. I can't see it. Now, I can't see any other hot spots around the board here. On Sorry, it's hard to really get this thing on camera, but there are no other hot spots apart from those four heat sinks. And of course that second

**Dave Jones:** one, which we'll call the second one down there, does look hotter than all the others, but there are no There's like nothing. I can't I can't see anything. There's no other components that actually show any hot spots at all. So, this is not looking good,

**Dave Jones:** folks. Let me tell you it is looking like it is something to do with those ASICs. Now, if you pan around the rest of the board Now, here's an interesting thing. You might see a hot spot on these

**Dave Jones:** on these BNC connectors here. And you might think they're actually hotter than other, you know, than other parts of the board, but that's not That's just heat reflection. And you've got to be very careful with shiny objects like this.

**Dave Jones:** You will actually get um heat reflection off these components. So, if you don't use it correctly, you might think, "Aha, that B and C is getting hot." But it's not. It is just reflection. If I put my hand near that, you'll see it change,

**Dave Jones:** right? There you go. If I put my hand near that, you can see the heat reflected reflected off those shiny B and Cs, and it can also do the same thing on solder joints and things like that as well. So,

**Dave Jones:** that's a real trap for young players with using these things. You've got to know about the reflective properties you're actually viewing. Now, let's have a look at the back of the board, see if we can get it, and

**Dave Jones:** you can see the hot spots on the ASICs there, of course. Once it's about 65° on the back of there. And that Yeah, that's the first one. And the second one, 67. So, once again, it's a bit hotter. Third one, not 65,

**Dave Jones:** not quite as hot. And the fourth one down there, but there are no other hot spots. I mean, there's the connector down there. Right? It is It's showing It's showing nothing around that mounting hole. There's Let me get that in focus. That's the

**Dave Jones:** mounting hole down there, and I can't see anything any issue there whatsoever. If you go up here, you can see the connector up there. You've got the ground clip, but no nothing. And of course, no other part of

**Dave Jones:** the board is um powered. Now, here's another example of one of these traps for young players. You might think, "Aha, look, we've found right in the center there a little hot spot. It's a couple of degrees hotter and it

**Dave Jones:** certainly shows up there, but it's not." What is it? It is these shiny uh solder pads here. They're the things that are showing up on there as a different temperature because they're shiny. It's not because they're actually warmer. So, yeah, when you're using

**Dave Jones:** these things, just make sure you really know how to use them because there's quite a few traps in there, but no, sorry, folks. Um this uh $12,000 piece of magic is telling me that there is nothing wrong with this board at all in terms of

**Dave Jones:** actual shorts on the board. And if we use the ULIR Vision camera as well, um we get well, the same result. I mean, I can scan over the board again, but there's the uh there's the connector down there. If we're going to have a

**Dave Jones:** look at that, and once again, there is no hot spot on that hole at all. You can see the connector. Not sure why it freezes there. It says rectifying. There you go. You can see the two wires heating up.

**Dave Jones:** But that that works brilliantly, actually. And you can see this one um has a uh tracker well, the uh floor has it as well. Well, it has an auto hot spot uh tracker which tells you the hottest spot on the screen there, but um

**Dave Jones:** you can see see the two wires on the right-hand side have all the current flowing through it. The one on the left has bugger all. It's just getting some residual heat from the others um as we measured in the first video, and there's nothing

**Dave Jones:** on that hole at all. There's nothing there. And if I scan the rest of the board, there's nothing over the board, either. Once again, hard to capture on camera. I've done it uh off camera and thoroughly and there's

**Dave Jones:** nothing there. Zip. Now, if I switch the other power rails on here, you'll notice that it dropped from 10. 5 there to 8.6. So, it looks like there might actually be some current going through the other unpowered rails there either through

**Dave Jones:** protection diodes or whatever mechanism is in place on those rails to actually do that. So, but still, you know, that doesn't explain anything. That's a complete non sequitur. So, all that's left is to current limit this and see if we can get any temperature

**Dave Jones:** differentials, but I reckon all those are dead. Now, have a quick scan around the board again with just the 3. 3 V rail and as you can see, apart from the heat sinks and the connector, I've only just switched on everything else is uh

**Dave Jones:** everything else is dark apart from those heat sinks. So, let's um switch on all the other supplies and we should start seeing a few other things heat up as well.

**Dave Jones:** So, yeah, I can start see some uh other circuitry on the far side. Yeah, look and see all those chips on the far side there start to heat up cuz they're all the 5 V 5 V rail stuff.

**Dave Jones:** You can see they they weren't lit before. This thing has a laser on it, too, by the way. You can actually switch the laser pointer on and it does uh show up, but there's some parallax error there on this thing, so

**Dave Jones:** it's not that great, but you can see some of the other chips in there heated up. Another one over there is getting a bit warm, 47°. And uh but yeah, not that exciting. There we go, that one in there. There's another

**Dave Jones:** that one in there is getting quite warm. It's getting up to 73°. That one behind there that's really quite warm. Yo, ouchy. Now, this is interesting. Check this out. I've got a constant current uh of uh 1 amp over here. So,

**Dave Jones:** there's my uh constant current. And the voltage has dropped right down, of course. It's no longer 3.3 V. It can't provide all the uh Well, it's amp It's current limited, that's why. And if I switch on switch on all the other rails, check out

**Dave Jones:** this little chip. Gets hot really, really quickly. He gets up to 100°, but I don't think it's faulty. It's just that the fact that the voltage on that 3.3 V rail has dropped cuz that goes away if that 3.3 V

**Dave Jones:** uh rail actually goes up to normal. So, um yeah. Well, I mean, I've checked that chip's actually connected to the 5 V rail, but uh obviously there's uh something on maybe the inputs or something like that that's causing that

**Dave Jones:** sucker to uh to heat up. And if I turn on all the other rails without the 3.3, check out the hotspot inside those chips. You can actually see the die heating up through the plastic package of that. That is

**Dave Jones:** really quite That's really quite something. I like it. And once again, that uh chip over there is getting uh red hot as well. That's if you don't power the 3.3 V rail. So, those chips really do not like

**Dave Jones:** that at all. And with the power supply current limited on 1 amp, you can see the ADC heatsink uh heatsinks over there are still uh warm. And you can see once again that that second ASIC we've been looking at

**Dave Jones:** is warmer than is still warmer than all the others. So, but, you know, that really doesn't account for all of the difference in the power if these three chips were working and this one was faulty and somehow got SCR latch-up

**Dave Jones:** or some other damage internally which shorted it out across the power rail was then well, I'd expect it to be massively a massive temperature difference compared to the others, but as it stands, it's only a couple of degrees.

**Dave Jones:** So, it really there's nothing in that. Well, sorry, folks. I think that's all I'm going to do on this one today because I think I'm going to call this one and declare it unrepairable. I think something has died in this power supply

**Dave Jones:** which has killed taking out everything on the 3.3 V rail. Everything being the only four devices on the 3.3 V rail which are these four ASICs here. Unless somebody can come up with another very plausible explanation for what's wrong

**Dave Jones:** here. I mean, I cannot find a hot spot where it's you know, dissipating all that extra power. We know for a fact the rail's not supposed to be 0.1 ohms. Obviously, it's supposed to be an order of magnitude greater than that.

**Dave Jones:** We know it's not supposed to take 11 amps. We know it's only supposed to take six tops. So, all that extra power is going somewhere and we've used a $12,000 IR thermal camera going all over this thing and cannot find a hot spot at all.

**Dave Jones:** All the power is being dissipated in these four ASICs. So, I can and because they're almost essentially a uniform temperature, the only logical conclusion on this one, folks, as much as I hate to say it, I think it's unrepairable. Four

**Dave Jones:** identically dead ASICs. That one slightly more dead than the rest. I might have some more fun with it maybe. I don't know. Maybe suck out this second device and see if it makes a huge amount of difference, but

**Dave Jones:** no. Think we're going to lose it, folks. Bummer. Anyway, if you want to discuss it, jump on over to the EV blog forum. Catch you next time.
