---
video_id: 7ocancoZ02Q
title: EEVblog #804 - HP1740A Oscilloscope Repair - Part 2
url: https://www.youtube.com/watch?v=7ocancoZ02Q
source: youtube-asr
---

**Dave Jones:** Hi, just a follow-up video to this HP 1740A 100 MHz dual channel analog oscilloscope and the repair of this thing. And where we got to last time was that we found that once we took the case off this thing, it basically would not

**Dave Jones:** fail except for one very small capture that I got by coincidence as I was tweeting a photo where all of the power rails, five different power rails on the output of the secondary linear transformer. This is in a switch

**Dave Jones:** mode converter supply. So, five different linear rails all dropped at once. And well, I left the thing for like at least 4 hours. It might have been closer to 5 hours or something like that. Still would not fail. So, it's

**Dave Jones:** either a a thermal problem where the unit where because the the case is now off this thing, the heat can escape. It can't build up inside and the thing is not is upside down now. So, if it is something

**Dave Jones:** to do with the power supply for example or something on the bottom like this board here, then you know, the heat doesn't sort of build up inside that case. But, it may not be a thermal problem. It may actually be

**Dave Jones:** a mechanical issue. So, let me actually explain on the schematic here what I'm talking about. But, before we do that, if you're trying to capture intermittent faults, which I wasn't here by the way cuz I you know, I thought it

**Dave Jones:** just sit there for an hour and then just fail. I wanted to see what the rails did. But, I didn't know it would have that like intermittent you know, a dropout like I captured by accident. So, if you want to do that

**Dave Jones:** with your meters, you hook them up and you use your min-max mode. So, that's what I've done on these four meters here and I've left the the once again for another like hour or so and I haven't been able to capture everything anything

**Dave Jones:** at all. Before this thing was easily failing within the hour and it was fairly repeatable at that but I haven't put the case back on and everything. Anyway, I've set them to min max mode so it'll capture any transients which go low. So I've got

**Dave Jones:** it displaying the minimum at the moment but it's always it's in min max record mode all of these meters even this old Fluke 27 has it and I'm actually displaying the minimum. So maybe I can actually I don't know simulate a mains brownout

**Dave Jones:** or something just by wiggling the power cord or something like that perhaps. Here we go. I'll give it a go and they'll all jump down. Just a trap for young players if you've got a negative rail like this you don't want to set it

**Dave Jones:** to minimum like I've set this one. If you're looking to get brownouts and drops in the voltage you've got to set this one to maximum because it's a negative voltage so it'll go up towards zero effectively. So you know so it's

**Dave Jones:** actually maximum. So I don't know let me see if I can wiggle this mains lead on the input. I can switch it off and on but that's a you know I want to get like a wait there we go. There we go. It did

**Dave Jones:** something. There we go. Drop down. There we go. So that was just by wiggling the mains lead on the input. So we're able to capture that. Now as I said in the previous video looking at the schematic for the main power supply

**Dave Jones:** board you can see it's a it's basically a standard linear transformer. It's got multiple isolated taps two four six different taps here all going to standard bridge rectifier full wave bridge rectifiers and then the big filter caps the big old ones from

**Dave Jones:** Sprague and Mallory I think they are. Anyway, but yeah we've got a linear regulator chip you know pass transistor mounted on the back all kind of you know standard stuff but basically I'm measuring the output of most of

**Dave Jones:** these. I'm measuring five Um, we've got six taps here. Anyway, I'm measuring five main rails here and they all dropped according to that photo, even though I have not been able to reproduce it yet. But, we did actually capture

**Dave Jones:** that drop. So, you've got to assume what can drag all five rails after the linear regulators down. As I said, they've each one's got individual current limit in here in here a current limit output resistor and it's got current limit in

**Dave Jones:** inside the chip, whatever uh chip that is, I'm not sure, but it doesn't matter. Um, how would you drag all the output of all those linear regulators low? Well, the most obvious uh thing like because if you just shorted out one here, for

**Dave Jones:** example, even if this say this diode bridge rectifier shorted out or did something weird so you know, you loaded it down, didn't have any protection, etc. I don't know, the cap was doing something weird. You know, it's unlikely

**Dave Jones:** to drag down any of the others because of the low impedance source through the transformer. It's just not going to affect it. Um, these other channels. So, odds on, it's got to be something on the primary side which is causing a dropout

**Dave Jones:** because then anything that happens on the primary side if it can't deliver enough power, uh then the outputs here because these are all drawing I don't know how much power this scope draws, you know, I don't know, 10, 20 watts or something,

**Dave Jones:** right? You know, it's a reasonable amount of power, okay? So, if this this primary side for some reason cannot deliver that power, all of these outputs are likely to drop. Well, the outputs of the outputs of the linear regulator

**Dave Jones:** here, but I you know, obviously the outputs of the uh transformer will drop and then bingo, it'll go through to the linear outputs. So, the first thing I would suspect is something on the primary side of this transformer and

**Dave Jones:** just forget what's going on down here with these couple of transistors. This is just uh some interface uh stuff for the two BNCs, the gating outputs, um the maiden delay gating outputs on the rear panel. They just happened to use those

**Dave Jones:** as a convenient uh jumping from one board to the other cuz the board happened to be there. So, they mounted on there and doesn't matter. So, that's got nothing to do with this main side and the main side is incredibly simple.

**Dave Jones:** We've got a an IEC mains input connector here, 1 amp fuse on the input, and then we've got our switch. Okay, that's our front panel line switch on the front panel, and then we've got a the voltage selection

**Dave Jones:** switches which is on the base of the unit down in here. And And then then you've got some socket wiring contacts. You've got your PCB connector going off to here. So, I'm suspecting possible My first point of call would

**Dave Jones:** either be the front panel main switch or the main selection switch here because these are You got to remember, these are like what? 30 This is 1980. Okay, so this is a 35-year-old scopes. So, these are 35-year-old switches, 35-year-old

**Dave Jones:** contacts on there. And contacts can pit and corrode over time with use for example. So, if the contacts are pitted and they can And because they got power reasonable you know, not super high power flowing through it, right? We're

**Dave Jones:** only talking 10 or 20 watts or whatever this scope takes, but it's enough current to cause a potential issue. So, if if the contacts either in here or maybe the front panel main switch are pitted, then it could potentially have a

**Dave Jones:** change while like under time. Maybe it heats up a little bit. Maybe it's got a little bit of higher resistance and then slowly heats up inside until some you know, something happens on the surface contact of the switches in here

**Dave Jones:** which then it causes not to be able to deliver enough power to the transformer. So, all the outputs are going to drop. That's the first thing I want to check. So, yeah, you could go, you know, right down the rabbit hole trying to look at

**Dave Jones:** all the other boards in the thing and whatever's hooked onto the output of all of these channels here. See if one of them's loading down and you can chase that rabbit hole, but I think that's pretty foolish because they all seem to

**Dave Jones:** drop. So, this, I think, definitely worth looking at. So, I think if you didn't have a look around here first, you would, you know, going for a wander down the garden path. Now, the problem with this is is I cannot reproduce the

**Dave Jones:** fault. So, what I'll I'll probably have to do first, maybe off camera, is to disconnect all the multimeters, put the covers back on, run the thing for an hour, and see if I can actually reproduce the problem. But, anyway,

**Dave Jones:** there is our mains input voltage selection. So, there's some like PCB contact switches under there. It looks like we might be able to take that off and inspect it, but they're probably like, you know, PCB solder connectors on

**Dave Jones:** there. And yeah, I can go and it's probably almost impossible to expect inspect cuz they're probably sealed switches in there. We'll have a look in a second, but yeah, I can go and spray some, you know, contact cleaner in them in in those, but

**Dave Jones:** the problem is if I can't reproduce the fault, how do I know that I fixed it? So, yeah, we have to try and reproduce the fault first before we go spray the contacts. It's all It's great to have

**Dave Jones:** this theory that it's probably something to do with the contacts somewhere. It's not likely to be the board-to-board, but you might take those out, have a look at the contacts on there just as a matter of course, though.

**Dave Jones:** We got one! I got lucky! I just switched the I just disconnected the mains power cord out the back and then reconnected it and bingo! Look, I on the screen down here. Oh, it's hard to I won't bother setting

**Dave Jones:** up another camera shot, but have a look. It's uh like Yeah, like there is nothing I can't adjust that. We're getting, you know, just that fixed line and all of the rails. All the rails are low. Look at that. Why? Hmm. Okay, so these aren't

**Dave Jones:** in min max anymore. Okay, so I'm going to wiggle that mains cord and see what the problem is. Not. So, I'm wiggling the mains input connector. Okay, so it's not that. Let me show you that. I'll show you my wiggling. Let's wiggle

**Dave Jones:** the front panel line switch. Give that a little bit of a Can you see that? I'm giving that a bit of a bit of a jiggle. There we go. Nothing doing down in there. I'll get my isolated uh prodder.

**Dave Jones:** Um well, these are all secondary. So, no drama there. Give those a bit of a bit of a wiggle. These are the main mains connectors. Give those a wiggle. And mains switches. Those voltage selection switches, although I'm only hitting the top. Maybe

**Dave Jones:** I can HIT THE BOARD. HMM. NOPE, NOTHING. It's permanently low. So, here we go. I will uh repower. Let me repower with the back here. There's all the rails dropping.

**Dave Jones:** Oh, hey, look. Has it permanently failed now? Excellent. Ah, that's what we want. That's what we want. Permanent failure. You bloody ripper. Now we're getting somewhere. Murphy's on his uh lunch break, I think. All right, so let's test our primary

**Dave Jones:** side theory here. The way we can do that is take, for example, just one of the rails. We'll do them one at a time, otherwise I'll need like 10 multimeters. Let's take the 5-V output here. Okay, so the 5-V output goes through this pass

**Dave Jones:** transistor, and it goes on to this side to plus 9.5 V there to this C11, this 5,300 microfarad cap on the output of this full-wave bridge rectifier. So, if this doesn't measure 9 V, well, it actually says 9 V here and then 9.5 V

**Dave Jones:** there. Little discrepancy. Anyway, if it doesn't measure around about 9 V, or, you know, significantly higher than the 5 V, cuz the dropout voltage of the pass transistor here, so let's assume and say it's a 2-V maximum dropout

**Dave Jones:** voltage. It's going to need at least 7 V to regulate this thing. So, if it's not at least, you know, around It should be around about that 9-V figure. If it's not, then we know, bingo, the primary side

**Dave Jones:** is not being able to supply enough power on that particular winding, and most likely on all the other windings as well. So, here we go. I've got another meter here set up across that 5,300 microfarad cap down in there. It's still

**Dave Jones:** got some charge on it. Hasn't been able to bleed it off cuz they haven't got a bleeder resistor on there, so the all that, you know, the regulator IC is the pass transistor is just switched off, and there's still some charge there.

**Dave Jones:** Anyway, so let's power it on. Hopefully, it still fails. Um so, let's power it still. Oh, oh, it's working. 9 V. You bastard. Oh, no, no. Hang on. No, 7 V. You saw it. Here we go. There we go. It's

**Dave Jones:** dropping. So, there's our 5-V rail. There's our 5-V rail. 4.2 V. No wonder, you know, it's it Well, actually, 0.2 V regulation is pretty good, actually. So, yeah. But, look. So, it's dropped, and all the other rails have dropped as

**Dave Jones:** well, but you can see that the output of the full wave bridge rectifier and it's failed of course. And so the output of the full wave bridge rectifier is it cannot you know is is dropped. So that means our pri it's most likely our

**Dave Jones:** primary side of the transformer cannot supply enough power. Let me check one of the other rails. Okay, I've now hooked it up to our 6,000 microfarad cap. That's where our plus 15 volt regulated output put uh output of the bridge rectifier on that

**Dave Jones:** cap as we should read on here. It should be about 21 volts or thereabouts. So it's powered on. Yep, it's failed again. This is repeatable. Hey, no we're still getting look at that. That's interesting. There you go. I lost that bit.

**Dave Jones:** That's enough. That is more than enough to give our regulated 15 volts output. But we're not getting our regulated 15 volts output. So that's really interesting. Hmm. And there we go. That's interesting. This is the negative rail. It shows positive there. I've

**Dave Jones:** hooked it up back to front. Murphy got me. Anyway, that's the negative rail. So we're looking at negative 22 volts. So that's correct as well. Wow, I really lost that bit. So but our negative rail is minus 12.

**Dave Jones:** But it's got more than enough voltage to regulate. It's got the regular output voltage expected from that full wave bridge rectifier. And let's try the 42 volt rail as well. I've got it across the 500 mic 75 volt cap. Should be about

**Dave Jones:** 55 volts according to the rail. And yep, but we're all good again. Bloody hell. Come on. Fail. Fail. Come on. You can do it. You can fail. Come on. And there we go. It's failed, but it's at 60 volts. So it's actually jumped up,

**Dave Jones:** which seems to in you know, like there's less load on there. So, yeah, that's interesting, but we lose regulation. So, maybe there's something that's tying maybe an overload on the 5-V rail perhaps into uh that causes uh drop out of regulation

**Dave Jones:** of the other channels. Hmm, but the bridge rectifier outputs the all the other ones are fine. It's only the 5-V rail. I can actually whack that one back. What was it? This big one here? There we go. No, hang on. No, it was this one here,

**Dave Jones:** was it? I can never remember. Yeah, there we go. 4 volts. No good whatsoever. And I'm just having a look at the uh ripple on the 5-V rail here and uh we're on uh 2 volts per division. And as you

**Dave Jones:** can see, it's just over that uh yeah, that 4 volts uh that we can see over there. I haven't got the multimeter on the uh rail, but yeah, it's a you know, that 4.2 volts or whatever we were

**Dave Jones:** seeing before, and the ripple is um basically bugger all. Look at that. The main output voltage has dropped. And by the way, if you're going to uh scope probe these things, I've done a whole video on uh mains ground earth referencing, and

**Dave Jones:** you're probably better off for using an isolation uh transformer when you're testing something like this, um or just make sure your ground reference point for your probe is actually chassis uh ground. Otherwise, you can blow the ass out of your um scope and or your

**Dave Jones:** product. Okay, I'm trying to make it come good now, um but it's No, it's not going to come good. Um but you know, it's not like the capacitor has failed, and then otherwise we'd see huge amount of ripple on here,

**Dave Jones:** cuz it should be what normally uh 9 volts or whatever. So, you know, 2 4 6 8, you know, it should be like up here and you know, if the cap was uh troublesome, we'd see, you know, a large

**Dave Jones:** amount of ripple, but we're seeing hardly any ripple on there at all. So, it's it must be drawing excess current and it's it's just dragging that down. The output winding can't provide enough power. So, what we need to do now is go back to our

**Dave Jones:** schematic and have a closer look at what's happening here. Um, because what we've been doing up until now, we didn't like sit down there and analyze all how the power supply worked and made a few assumptions and it

**Dave Jones:** was actually quite reasonable to suspect the primary side because all of our outputs dropped. And so, we did the right thing. We said we came up with a quite plausible theory about the primary side here. We went about testing it by and we

**Dave Jones:** actually found that our 5-V, the output of our bridge rectifier here on our 5-V rail, this 9-V actually dropped right down. Okay, so that seemed to confirm that theory, but then when I went to double-check, always double-check this,

**Dave Jones:** okay? Don't assume anything. So, I I went and measured the other rails here and these other rails weren't being dragged down. So, that fact basically ruled out our primary side theory, high impedance primary side dragging everything down on these secondaries.

**Dave Jones:** So, we have to go check the rest of the circuit and see what's what. Okay, so what we've got here is our three Let's just look at this like ignore all these complicated looking ones with the transistors up top. Let's just like

**Dave Jones:** concentrate on what's happening to the 5-V and the plus minus 15-V rails here. Now, so we've got three regulator ICs here, okay? And but when you actually look closer at these, okay? This one here is the one for the plus 5-V rail.

**Dave Jones:** Sorry, plus 15-V rail, okay? So, we've got our plus 22-V coming in here, and we measured that that it was still 22-V yet our output was actually being dragged down. Now, this looks fairly typical. Look, here's our output here, our plus

**Dave Jones:** 15-V. Oh, there we go. Sorry, you can't see that, but here There it is, our plus 15-V output here, and we've got our our Look, we've got a voltage adjustment pot here for the 15-V. So, we've got our

**Dave Jones:** typical output voltage divider feeding back and actually into our regulator here using this external pass transistor, and that is a very very typical you know, voltage regulator. But, we we know we're measuring 22-V here, but we're not getting 15-V out of here. Why?

**Dave Jones:** But, more interestingly, let's take a look at another one down here. Okay? This is the negative 15-V one. Where is Where are the feedback resistors from this from this negative output rail? Look, aha, here's our feedback resistors. Look, it's referenced to the 15-V rail,

**Dave Jones:** the plus 15-V rail here. So, this is not independent. It actually relies on the fact that this 15-V rail is set correctly. And then if you go look at the 5-V voltage regulator, right, here's our output here, here's

**Dave Jones:** our output current sense resistor, here's our series pass transistor. Where is the voltage reference coming from? Bingo, the plus 15-V rail again. So, if that plus 15-V rail drags down, of course it'll drag down the 5-V rail. Of

**Dave Jones:** course it'll drag down the negative 15-V rail. So, it looks like the all the rails there are referenced to that plus 15-V output. And of course, wouldn't you know it, if you actually go and read the theory of operation of this thing, it

**Dave Jones:** tells you exactly that. Look at this. All voltages plus 5 43 120 plus minus 15 what we've been measuring and the high voltage are referenced to the plus 15 volt supply. Duh. So, of course it So, it must be

**Dave Jones:** made operational first. The supplies are current limiting type as as we've seen. They've got those current limit resistors. So, any excessive loading on the vertical, horizontal, etc. will cause the supply to read 20 to 30% low and that's what we've been seeing. So,

**Dave Jones:** of course they're going to it's going to drag down all of the rails. Okay, so what it actually tells you to do in the troubleshooting procedure and what's obvious is to actually remove this board here which connects the output of the

**Dave Jones:** power supply here to all the other boards here, the horizontal and the vertical boards. And well, that's a really that's really is very nice. It just slips out like that cuz we've got cartridge connectors on here. They are

**Dave Jones:** looking great condition. There's no no corrosion at all on the everything's beautifully gold plated. Be very thick gold plated too. Top notch. No worries whatsoever. And I'm looking at the rails and of course they're all bang on. I

**Dave Jones:** might just leave it for a while and see if it fails but I suspect no. There's something that's dragging down one of those rails. And of course with no horizontal and no vertical, what do we get? We get a dot straight in the middle

**Dave Jones:** cuz it ain't driving it left, right, up, down, or wherever. And you can actually see the high voltage output here still connected to the board down here. So, we still drive all our high voltage stuff. We're still driving our CRT and

**Dave Jones:** everything else. It's just that we're not connected through to our horizontal and our vertical boards here. So, what we're doing now is just checking to see if it's the horizontal or the vertical boards at fault here. See if our problem

**Dave Jones:** returns. But as we've we've been seeing here, these intermittent faults are a pain in the ass because you don't know whether or not you're just getting lucky and the fault's not showing up. It could be in the high voltage section, which is still

**Dave Jones:** being powered from here. As I said, it could still be in there, but you know, there could be some reason why it's not showing. You know, Murphy will get you every time. So, you know, just because we could leave it

**Dave Jones:** here for an hour and it might still be good. But that doesn't actually prove anything as such. This is why intermittent fires are such a pain in the ass and you can waste a lot of time. You can go down a lot of

**Dave Jones:** uh you know, chasing a lot of red herrings down the rabbit hole and well, yeah. So, but it's not failing so far. So, I don't know. You You name the odds of the high voltage power supply section being at

**Dave Jones:** fault. I I suspect it's not. I suspect it's on the vertical or the horizontal sections. And that suspicion is backed up by Remember our plus 5-V rail is the one that actually went down here and the output of this bridge rectifier was

**Dave Jones:** really loaded down. And by the way, it was that pass transistor that was getting hot and this voltage regulator here U2. I've actually checked the position on that on the component overlay and it was that one that was

**Dave Jones:** getting hot for that 5-V rail. So, our 5-V rail over here, we've got assembly A14 and it looks like a 5-V rail doesn't go anywhere else. So, I'm suspecting A14 over here. I don't know what that is. We'll have to have a

**Dave Jones:** look. Well, there you go. That doesn't help. Here's our power supply up here. This is the interconnecting board, the A14 interconnect we just physically removed and that plus 5-V comes out of the power supply and goes off to both

**Dave Jones:** the horizontal sweep assembly and also to the vertical preamp assembly. So, it could be either one of those, horizontal or vertical. Well, thanks for that. And if we have a look at this rather complex-looking interconnection diagram, our low-voltage power supply

**Dave Jones:** here, our plus 5-V output here as we saw, it goes off to the horizontal assembly down here, and it also goes off to the vertical assembly in here. But then the plus 5 V from the vertical assembly also goes over

**Dave Jones:** here as well. There's I you know, the horizontal's pretty boring. There's not much doing in the horizontal. So, I more just for a sheer odds point of view, I think there's more likely to be stuff happening in the

**Dave Jones:** vertical channel. So, I'm more suspecting the the vertical side of thing, the vertical board, than the horizontal board, but I mean, you know, it's just guessing, really. Okay, so what I'm going to do now is just have a quick check of the

**Dave Jones:** 5-V rail output current. And we don't have to get in and break the circuit with our multimeter to measure the current at all because we've got ourselves a current-limiting resistor here, this 1-ohm resistor R30 here. We can just measure the voltage across

**Dave Jones:** that. And hopefully the voltage across it when it's not failed and then wait until it fails and then see if the voltage increases, i.e., the current increases. So, let's give that a whirl. There we go. That's our 1-ohm current

**Dave Jones:** shunt resistor. I'm using these parrot clips in there. I love through-hole parts like this, troubleshooting through-hole parts, cuz you can get in there with your little easy hooks or your parrot clips or whatever, or your even your alligator clips, and actually

**Dave Jones:** clip on to the components. You don't have to solder on. You don't have to do anything. It's really easy. So, we'll power it on. Yeah, we're working, and we're getting 0.25 V there. So, we're looking at uh you

**Dave Jones:** know, 250 milliamps on the 5-volt rail. I'll just sit here uh wait for it to fail. Hopefully, it was failing before within a few minutes. So, hopefully, fingers crossed. Oh, there we go. There we go. 4 volts It's dropping. Our current's actually

**Dave Jones:** going down. Yes, I've got it hooked up uh backwards. So, I didn't know which way it went. So, it's Yeah. But, no, our current hasn't increased. But, look. Our current hasn't increased, but the voltage, that's 2 volts per division.

**Dave Jones:** So, our AC output our rectified output tap has certainly dropped. Look at that. There we go. I've powered it back up. I've put the probes around the right way. So, 250 milliamps and there's our normal There's our normal uh ripple um after

**Dave Jones:** our full-wave bridge rectifier. So, 2 4 6 Look, look, slowly Oh, You see it drop? Did that drop or was that just my imagination? Anyway, 2 4 6 Oh, did we get a glitch there? 2 4 6 And then,

**Dave Jones:** whoa, 8 No, that's that's one sick puppy. Look at that. But, our current you'll notice our current did not increase. So, it's not like it's being overloaded. Bingo. And just as a matter of course, I'm going to check the

**Dave Jones:** connections on the uh transformer input there. They look They look pretty darn good. No corrosion or anything on those. So, based on Kirchhoff's current law, what can be can be happening here? Where can, if it is uh excess current, where can it be

**Dave Jones:** going? So, say for example, there's excess uh current on the output of this bridge rectifier and it and it is actually dragging this rail down and this diode bridge and this uh tap here can't uh can't supply uh the power required, where's it going?

**Dave Jones:** Well, it's not going through here. It's not going out of here because here's our current sense resistor. It can There's only two places it can be going. One is somehow through the base of this transistor into our I think believe it's an LM 723

**Dave Jones:** voltage regulator here or it's going around here once again into a current limit pin. It doesn't seem likely at all. We've measured the voltage across here. There is no excess current flowing out there. So, it can only flow there or

**Dave Jones:** there. So, it can't go anywhere else. So, what's happening here? Well, as I said, if that capacitor if that was a bad capacitor this 5300 microfarad cap, if that was, you know, bad as well, it's, you know, 35 years 30 years old or

**Dave Jones:** whatever it is. 35, is it? Yeah, you'd certainly suspect that, but you'd see a lot a huge amount of excess ripple. That's what I would have expected. So, I'm starting to suspect either this transformer tap, which is highly

**Dave Jones:** unlikely, the interconnects in here, which is uh plausible just like we had on the primary side. We thought maybe there's a, you know, some sort of interconnect issue or the diode bridge. And the capacitor one we can prove. I'm

**Dave Jones:** just whacking a 20 ti- I think it's a 2200 microfarad 60 odd volt across the rail there and well, let's have a look at our ripple as well. And watch it. Okay, everything's working hunky-dory at the moment, but I suspect

**Dave Jones:** this puppy is going to fail. And yeah, the scope scope still works. So, everything's fine. I think we'll sta- Well, wait. Did Did that just drop or was that in my No, look, it's jumping around. It's jumping around. And

**Dave Jones:** remember this is the voltage across to that full wave rectified capacitor there. So, I think if we wait, I reckon it's going to drop and do exactly the same thing as before. I Yep, there we go. It's dropped. Bam.

**Dave Jones:** Voltage across there, 4.4 V. Our voltage over our 5-V rail, the output of the voltage regulator, 4.1. Bingo. Even with the extra cap on there, so it ain't the cap. Now, you wouldn't know what's really handy about having these

**Dave Jones:** transistors on the back and these connectors going straight onto the pins? Because these are identical uh series pass transistors, we can swap them. This is uh this one here is the one for our uh 5-V channel that we're looking at

**Dave Jones:** here, but we can just swap it with this one here. So, that's what I've done. Bought the the wires are just long enough on an angle to get over there and plug in. So, we can see if the fault

**Dave Jones:** stays with the transistors swapped over, we know there's not a problem with the in some weird way, shape, or form. Okay, it's still working. And uh oops. Sorry. Forgot to turn that back on. It's just discharging that cap. And our

**Dave Jones:** ripple iron just is jumping around here. I reckon she'll uh Yep, there we go. Failed again. Not the transistor. Not that I expected it to, but hey, because we can swap it. Very quick, easy test to do. Okay, now what I've got is I'm just

**Dave Jones:** measuring the uh transformer output tap there. We can in Can you see that? 9 V AC there. And uh let's wait until see if we get a fire. I'll switch this back. Sorry. I uh I moved that a little bit.

**Dave Jones:** Come on. There we go. All right, there we go. Bingo. We're still getting Look, it's gone back up. So, that means we're still getting the AC out of that uh transformer. No problems whatsoever. And because there's looks like there's less

**Dave Jones:** load on it, look. So, what's left? Diode bridge. That diode bridge down there is our culprit, because I was measuring on uh pin seven and eight here. Pin one starts over here. Go straight into that diode bridge. So, I'm suspecting that

**Dave Jones:** puppy, but I do stand corrected. It could potentially still be like the solder joint on those pins, or maybe the connection inside there, but I can't really see any problem in there. It looks really good. Uh it could be, you

**Dave Jones:** know, it could be a dry joint on the bottom of this connector, or the uh diode bridge itself. It may not be the diode bridge. Could certainly be an old-fashioned dry joint. Now, I was about to say this is actually uh really

**Dave Jones:** quite easy to uh get out because of the uh the wire into the uh past transistors on the back. Just pull those off, couple of these, disconnect the uh mains here, disconnect the secondary, uh take off the plate there. There's a couple of

**Dave Jones:** wires in there for our mains input. Um but there's our mains uh voltage selection switches for those uh fanboys, but there is two screws going to the that there. That uh there's a bottom mount. Uh that's the mains power switch

**Dave Jones:** all right there, which is no surprise, cuz here's the mains input. Um and there's a shaft which comes all the way on the bottom of the board and connects to there. So, oh, and I've got to disconnect, carefully disconnect uh this

**Dave Jones:** connector here through to the bottom board. I've done that, and um I think it sort of Yeah, I don't know how that attaches under there, cuz there's the whole high voltage um supply on the back of that. So,

**Dave Jones:** jeez, I don't know. Well, I figured it out. Uh I sort of moved this slight I've disconnected this main connector down here. I can move it just like half like half a centimeter towards the front panel here, and then once I've got it on

**Dave Jones:** the front panel, tada, there's the line switch and the line switch is actually square but it's protruding enough that it now lets me unscrew it. Tada, look at that. So I can unscrew the shaft from the main switch on the back. This

**Dave Jones:** is all very, very clever. And by the way, yes I did eventually figure out that this is actually explained in the manual, doll. So bingo, this now with perhaps some difficulty, hmm, should actually come out somehow. Yeah. Well, looky what we have here.

**Dave Jones:** Look at those pins. Can I wiggle those from the bottom? Uh, not a huge amount. Look at those dry joints. Dry as a dead dingo's donga. But the funny thing is that's not the one that I'm suspecting. Okay, this is

**Dave Jones:** actually CR3, I think it is, which is the flood gun, the high voltage flood gun tap, which I wasn't looking at. This is the one that I'm interested in. That's the that's that tap for the 5 volt rail,

**Dave Jones:** but that looks that looks okay. So yeah, I don't know. Anyway, so I'm not sure if I caused that problem by uh wiggling the connector out. I I don't know. But geez, I'm certainly going to fix it up. No dry This here is the diode No,

**Dave Jones:** sorry, this one is the diode bridge we're interested in. So yeah, I'm going to replace that diode bridge as a matter of course. That's for the 5 volt rail. And also these ones on the other end, too. They might show up

**Dave Jones:** really well on the camera here, but to the naked eye they look like good joints. I had to look at those under the Mantis microscope. The others look good. These ones also, these two here, I'm not sure if this will show up on camera.

**Dave Jones:** It's hard to see on the camcorder LCD here, but these ones will these ones also have cracks in them, but the one we're interested in, this one here, looks to be good, but I'm going to resolder this whole damn connector just

**Dave Jones:** as a matter of course. I desoldered that suspect diode bridge, and it's interesting to note no solder has flowed through to the top side of the component there like they have for the other components. Look, all the other components solder has fed through

**Dave Jones:** no problems at all, but on that diode bridge, it's suspiciously hasn't. I think I'm going to go through and resolder all the diode bridges. It might not be anything wrong with the diode bridge, but I will replace it with a new one or a new old

**Dave Jones:** stock as a matter of course. And that diode bridge wasn't lone either. It looks like practically all of them are going to have that same issue. None of the solder has flown through. And granted that shouldn't be a problem,

**Dave Jones:** but you're relying on the through hole plating of the PCB itself, and you'll notice that, you know, most of them have all the traces on the top half. If I flip it over, you'll see that very very little is

**Dave Jones:** actually on the bottom there. So, you've got to rely on all that top half connection right through the vias there. That's asking for it, especially after 35 years. So, that might not be a dodgy diode bridge at all. By the way, the pad

**Dave Jones:** fell off in the repair there. I was using a reasonable temperature, but it just came off. So, you know, 35-year-old PCB, meh. But all of the Most of the connections look all for that diode bridge, three for that one,

**Dave Jones:** three for that one, three for the 5-V one under interest, two. And all of the connections for that that we saw some really dodgy dry joints on. I mean, you know, completely cracked, right? Dry as a dead dingo's donger.

**Dave Jones:** Every single one of those connects to the positive side. So, if we had no solder flow through on these diode bridges, you got to assume that we had no solder flow through on those. I didn't actually physically remove it and

**Dave Jones:** check it, but I sucked them all out. It wouldn't sort of budge. There was some, you know, it's quite hard to get these sort of things out sometimes depending on the hole size, but I resoldered them as a matter of course. And all of the

**Dave Jones:** diode bridges, so yes, I did replace the one diode bridge on the top side there. There it is. I replaced that puppy there, but I probably didn't have to. I suspect there was Now, looking at those joints, I don't think

**Dave Jones:** there was much wrong with those diode in that diode bridge at all. I suspect it's just 35-year-old solder joint problems. And um this problem has probably been sitting in there waiting to happen for 35 years. Not adequate solder flow

**Dave Jones:** through like they got on these parts here. Look all the other parts, no problems at all. But maybe these higher thermal mass ones, or maybe they were soldered separate, or I don't know what the deal is. They had no flow through

**Dave Jones:** whatsoever, and maybe the connector, too. So, anyway, resolder it all. Let's whack it back in. Okay, let's power it on and see what we get. I've only hooked up the 15-V rail, but Oh, helps if I plug it in. Plugged in, we're getting 4

**Dave Jones:** 5 V, and we're getting our 9.8. Everything's hunky-dory. Now, all we've got to do is wait, but I suspect we've fixed it. And I'll tell you what, it seems to be the diode bridge, actually. I've had this thing jumping

**Dave Jones:** around. I've just got it tested here. I'm supposed to be drawing like a half amp load from this puppy, and and it's it was like 5 volts before, and it's not it's just dropped it's just dropped and it was actually jump back.

**Dave Jones:** I'm probably Murphy means I'm probably not going to be able to get it to jump back. Come on, damn you. Come on. Anyway, I reckon there's something thermally wrong with the with the you know, the diodes inside this thing, and

**Dave Jones:** that's probably a first. I don't think I've ever like I've seen diode bridges blow, but not ones that sort of you know, intermittent thermally fail like that. So, yeah, I'll see if I can nab it though. There we go. I got it. This is what it's

**Dave Jones:** normally like. Okay? And hopefully, we'll just see it suddenly jump. Bingo! Hey, just saw it. Got you. There you go. It just jumped down. And if we let it cool down, it actually recovers and it's repeatable. The bloody diode

**Dave Jones:** bridge. Unbelievable. So, there you have it. The EV blog curse has been lifted. Where I either when I get repair stuff like this, it's either so incredibly simple to fix or it's BER, beyond economical repair. And you know,

**Dave Jones:** too complicated and expensive to fix, but this one fantastic. I hope you enjoyed a look at how I traced down to the bloody diode bridge. Do you believe it? And potentially uh, solder joint, um, issues as well. Unbelievable. I don't think

**Dave Jones:** I've ever seen a diode bridge fail intermittently like that. Usually these, you know, diode bridges, yeah, they fail, but they fail usually fail open like that. And, well, these ones, this was failing, uh, not so much like open. If it failed open, then it would

**Dave Jones:** have been fairly easy to, uh, find that we weren't getting any voltage out and stuff like that. But, because this, uh, thing had a quite unusual, uh, power supply arrangement in that all the voltage rail references were actually

**Dave Jones:** tied to the 15 V reference, then if the 5 V one went down, and there's all the other circuitry, it, uh, by some mechanism I haven't gone in and, you know, investigated the whole thing, maybe through another board or something

**Dave Jones:** like that, can actually drag, um, the other, the 15 V rail down, and then the 15 V rail drags down all the other rails as well. And you would have actually noticed that all of them are dropped by

**Dave Jones:** exactly the same, uh, same percentage as well. So, that sort of, you know, clued in that they're all tied into the single 15 V rail, but that was a fascinating troubleshooting look. It's, like, a power supply fault, right? Really,

**Dave Jones:** really simple. But, because it failed in a very subtle and intermittent way, you saw how I actually got a little bit lucky here in terms of that, uh, it did actually play ball in the end and actually failed pretty much on cue when

**Dave Jones:** I could power it up, wait a minute, it would fail. But, it didn't do that uh, the first time I played with it in my first video. It was, you know, sitting there for 4-5 hours and wasn't doing a

**Dave Jones:** thing. So, if it doesn't fail, and, well, we came up with a, you know, a couple of theories. The primary side seemed like a, a reasonable, uh, theory to check. And I, um, it was lucky that I went in and double-checked that, of

**Dave Jones:** course, to make sure, uh, that the other voltage taps had actually, uh, dropped as well as the 5 volt one I saw because if I did that I might have gone off and you know try to look for some short and

**Dave Jones:** by the way if I followed the troubleshooting procedure in this thing I might have to take a capture of it and show you it basically implies I think I read it out there I did show it before it says that the horizontal if they all

**Dave Jones:** drop by 20% or whatever exactly what we saw here right all the rails drop then you know they said oh the horizontal the vertical you know it's likely to be in a fault like that so if you were strictly

**Dave Jones:** following the troubleshooting guide you may have gone down that rabbit hole thinking oh there's some sort of overload on the horizontal or the vertical boards and it's lucky that I actually well it's not lucky I deliberately went in there and went no

**Dave Jones:** before I do that I'll go in and check that check the current it's worth checking the current double checking checking things before you go down that rabbit hole chasing all those red herrings where you think it might be you know you might have fixed

**Dave Jones:** 10 of these before and go oh yeah it's been the vertical board or whatever actually had a few people email me since the first video on they said oh yeah I've seen this it's you know the vertical board or it's this or it's that

**Dave Jones:** and stuff like that and nobody nobody picked a diode bridge and potentially some dodgy try solder joints try as a dead dingos donger those things were amazing and typically you'd start out with troubleshooting something like this with a visual inspection but you can't

**Dave Jones:** visually inspect those joints that we saw in there until you take out the whole board so we only had the measurement you know just take some measurements to sort of see where we led so I hope you like that troubleshooting I

**Dave Jones:** could have made this video shorter sorry it's been like 45 minutes or something in this second one. Uh because it's been going for like an hour. I just edited the uh footage and it was like 40 minutes worth. So, I've

**Dave Jones:** been yapping off for another five. Sorry, at least. Maybe 10. But, we really got lucky with this puppy that it was such an obscure fault that, you know, you're not very likely to see something like this. Yeah, intermittent

**Dave Jones:** faults are, you know, happen all the time. But, usually something, you know, like that uh dry cracked joint, it'd be, you know, either a physical flex thing you might be able to, you know, flex the board just might have so I was poking

**Dave Jones:** around off the poker. It it didn't actually come and go then, which indicates that's probably wasn't the problem. And ended up being an obscure thermal issue that didn't just o- you know, fail open. It failed sort of high

**Dave Jones:** impedance, which was a different thing, which made it look like and it, you know, it could have led you down the garden path. You could have I could have easily wasted a lot of hours on this uh scope before eventually finding

**Dave Jones:** something like this. And that's the problem with bloody intermittent failures. Anyway, I hope you enjoyed that. And there's probably people who are saying, "Oh, jeez, Dave, that was that was pretty easy. It was just a bloody power supply. Why didn't you find

**Dave Jones:** that in 5 minutes?" Well, I basically it did not take as long as what you're seeing here. I was waffling on and, you know, going through what was talking through what was in my head and stuff like that. It might have been like

**Dave Jones:** an hours worth of troubleshooting video, but in reality, if I didn't have the camera on and I was just working on this, it it was probably 10 15 minutes worth of work. So, it's, you know, it's probably not it it took me longer than I

**Dave Jones:** think to get the board out and then repair it, clean it up, and put it back in than it did to actually find the fault in the end. So, it was a pretty quick repair in the scheme of things.

**Dave Jones:** So, what are some quick lessons from this one? Well, always measure your voltages. Thou shalt measure voltages, golden rule of troubleshooting. Don't assume something's overloaded. Actually measure the thing. Double check. If we didn't double check, we may have gone

**Dave Jones:** down, you know, a route. Don't necessarily believe any instructions you have. Yes, they can be handy, but they might also lead you down the garden path as well. Got to have your thinking cap on. And with these intermittent faults,

**Dave Jones:** don't just go around with, you know, a theory in your head, oh yeah, it's the primary side contacts and start cleaning all the contacts and going, oh yeah, I fixed it because Murphy'll bloody well get you. I guarantee it. That it'll, you

**Dave Jones:** know, it'll look fixed, it'll work for a week or whatever, and then the thing will come back. But we got reasonably lucky on this one that it decided to sort of play ball, but it may not have. This one could have been really ugly. So

**Dave Jones:** we made a couple of assumptions in here, came up with a couple of theories, but we tried to verify them. And then, hey, I was wrong, you know, it wasn't the primary side. Hey, but it was worth a

**Dave Jones:** quick, you know, a 30-second look just to measure it and make sure, but hey, we found it. It pointed somewhere else, and then that pointed to another thing, and bingo, we found it. Beauty. Never assume. And also, this is not a bad

**Dave Jones:** example of where having multiple multimeters comes in handy, and potentially, even though we didn't get that far, having a multi-channel scope. A lot of people ask, well, what use is a four-channel scope? Well, you can measure four power supplies at the same

**Dave Jones:** time and see what they're doing, and capture transients. If we had some weird, you know, fire mode, we may have gone down into that detail, and maybe even because these are ground reference, maybe you might have needed We didn't get this far ever, but you

**Dave Jones:** might have needed a nice multi-channel isolated scope like this one. Two channels. Hopefully do a repair and tear down on this one, too, soon. Two isolated channels so that we can get in there and probe different points at the same time,

**Dave Jones:** fully isolated from any uh between uh scopes. So, yeah, it's handy to have more than one meter. I keep saying it. Good example. Hope you enjoyed that. That was a bloody ripper. I love a good adventure hunt like that. So, I hope you

**Dave Jones:** did, too. If you want to discuss it, jump on over to the EEVblog forum. Links down below. All that sort of stuff. I've got the warranty void if not removed t-shirt. I'll probably link in that down below if I remember. Usually don't.

**Dave Jones:** Anyway, leave YouTube comments, blog comments, all that sort of jazz. Catch you next time.
