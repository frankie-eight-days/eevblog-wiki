---
video_id: CKdeqqo2diI
title: EEVblog 1564 - Agilent/Keysight U1273AX Multimeter Repair
url: https://www.youtube.com/watch?v=CKdeqqo2diI
source: youtube-asr
---

**Dave Jones:** Hi, just a follow-up to the mixed box of multimeters and I mentioned that this U1273AX OLED Agilent multimeter none of that Keysight rubbish was a faulty. Now this is basically I've never used it. It was brand new in the

**Dave Jones:** box. I do believe like it it worked at one point then went back in the box and it just next time I took it out it just it was dead. So I'm going to actually I've put new batteries in this thing and

**Dave Jones:** we can like turn it on. It it it powers on but we've got absolutely nothing on the screen at all. So the screen is dead. So clearly the processor is working cuz it's going through some 1980s boot up cycle which is absolutely

**Dave Jones:** ridiculous. Like whoever approved that who it bloody Agilent approved that. Come on seriously. So let's get this bad boy apart. There's a serial number for those playing along at home. As I said yeah this just like it was just sitting

**Dave Jones:** in the box. So I got no idea why this would have would have died. I don't think it's ever been used in anger. Why is this only got three screws? That's weird. Three and then hooks up the top. Is that it? Really? No

**Dave Jones:** there's another one under there. Oh by the way this has had this could have something to do with it. But it's a long way from the screen. This one did have there was battery leakage in it and attempt to stop the

**Dave Jones:** rot in there. Like it's not horrid right but obviously something's gone wrong with this one here and that could have leaked in through there and gone onto the board. So first thing we're going to look for is for you know it's it's not a

**Dave Jones:** huge amount of damage, but it's actually corroded this screw here. So, the way No, that screw doesn't want to come out. Okay. Yeah, this has got hooks on the top. So, that's budge your thing. Get the old Whoa. Yeah, okay. What?

**Dave Jones:** Here we go. And Whoa. Yeah. See that screw? Oh, that screw Oh, that's just cracked. That's just completely cracked. No, it obviously Whoa, it Yeah, it does not like that at all. Wow. So, that's crusty as, right? That's crusty burger. Check that out.

**Dave Jones:** Wow. But, that's nowhere near the LCD, right? So, or maybe there's some Oh, yeah, it's it's all Okay. Well, that's all the crap that came out of it. All right. You know, maybe, right? If you've had battery leakage and you've got a faulty

**Dave Jones:** product, then well, you know, obviously, you suspect the battery leakage, but that really doesn't look that horrific, does it? I mean, I'm not seeing a major issue with the board there. I mean, that's your That's your battery contact. So, you know, clean up those.

**Dave Jones:** Stuff like the other pads fine, but Yeah, so there's some spillage on there, but not a not a huge deal. So, max 4611 there, and there's not many traces going to it. Analog switch, okay. It just has nothing

**Dave Jones:** going to it. So, um Well, there's not much there anyway. No worries. Um let's keep looking. First thing, just a visual. So, well, it doesn't mean there's nothing like on the other side of that board, but I don't know. Could be.

**Dave Jones:** Unlikely, though. All looks pretty clean, and as I said, the uh processor is clearly working because it's doing the boo boo start up sound. Almost certainly sending um stuff over to the LCD. AD637, there you go. That's the I know that one.

**Dave Jones:** That's the true RMS uh converter chip. Before start probing around in here, maybe it's worth start maybe it's worth just flipping the board and stuff and having a look on the other side. I think that's worth it. Really? Was that only a single screw? Or

**Dave Jones:** is it No, it's just a nice just a plastic clip. There you go. Okay. Well, that was easy. Geez. No lockers. All right. It's the bottom of the What? Bottom of that down there. Once again, whoop. Yeah, the post is uh

**Dave Jones:** post is just completely gone. Really didn't like that. So, it looks like the battery stuff just ate away the plastic um as well. And uh like it's not going to be anything wrong with the contacts cuz cuz the contacts work and that's not

**Dave Jones:** going to be an issue driving the LCD or whatnot. Why is that? Why do we have that serial number stuck there? I'm not sure what's doing there. Haven't I don't think I've torn down this meter before. It's not a problem. I'll check out the

**Dave Jones:** switch better. It's It's hard to get it like under the microscope here. It's better if you just do it visually or under my uh mantis or something like that. It's all about lighting. You got to get all the

**Dave Jones:** lighting at the right angle and whatnot. But um no, nothing's nothing's happened. You know, like No, there's there's there's no way. I don't think that battery stuff could have caused that. I think that's just a coincy-dink. There's our

**Dave Jones:** OLED module. It's just a pin interface there. I wouldn't rule out just the OLED failing. So, if the actual display itself is gonsky, then nothing under the rubber baby rubber baby buggy bumpers there either. See, so you know, that's

**Dave Jones:** clean as a whistle, right? The contaminant didn't get down further. Now, of course, the problem with OLEDs is that uh they they chew a lot of power. Um but they they look gorgeous, of course, but they chew a lot of power. Do they

**Dave Jones:** last as long as LCDs? I don't think so. Well, there you go. It's metal threaded inserts on there. Yeah, they're soldered in. Everyone wants to see the processor. Show me the processor, Dave. 78F0547.

**Dave Jones:** So, that's a uh Renesas jobby. 595 so the win. Thank you very much for expansion, some serial parallel expansion there. Obviously boots and does its thing, and it's the OLED that's dead. So, here it is. And flippity do dah, voltage on here.

**Dave Jones:** Unfortunately, all the circuitry's under the bottom, and um it's hard to probe while the damn thing's powered up. Unfortunately, bloody Murphy, a 33063. There you go, 1.5 amp peak boost buck uh inverting switching regulator. So, fortunately, I can't measure that. But,

**Dave Jones:** down here we also have the uh chip on flex down here. This is the driver. So, this is the actual driver chip. So, it's just coming straight over here onto the driver chip. Uh that all looks good. That's not any of that hot

**Dave Jones:** bar rubbish. That's just proper solder. So, that's Yeah, they aren't uh that's not the your adhesive uh conductive glue um down there. So, that's all soldered in. So, that's all rock solid. I'd be measuring that power first. Unfortunately, to do that, I really have

**Dave Jones:** to solder on some like wires and get it out. Unless there's a pin coming back. Once again, like I don't have a schematic. We we have a part number on there. We might be able to get something on that to see what voltages and stuff

**Dave Jones:** it requires. So, I'll That's worth a shot. Well, what do you know? It's an 108 US dollars. Oh boy, it's it's just a chipset, basically. It's a Farnell data sheet. Oh, oh, oh, I saw a Keysight multimeter there.

**Dave Jones:** 2.4 inch mono mono color mono color OLED. Yeah, that's just the driver. Yeah, the driver IC is that. Okay, so that's the common driver IC. That's not the actual unit itself. There you go, you can buy the OLED. Oh, right. Yes.

**Dave Jones:** Yeah, the Okay, so it's the same model that's used in the U1253, which I've done a video on like way back, like in the first, you know, 30 videos of mine or something like that. FOB price, 60 bucks a piece.

**Dave Jones:** You But that's Yankee bucks, too. You'd have to be a bit desperate. And you've got them order minimum five pieces for the OLED. Just for the OLED. Oh, wow. If I can get the multimeter for 60 bucks, I'd be buying five of those. You

**Dave Jones:** can bet your bottom dollar I'd be reselling those on eBay for a huge profit. So, okay, so that's the driver chip. Okay, so Vbat, it needs 3.3 volts and it needs 2.7 volts for the digital. 190 microamps operating current, 550 microamps. That's

**Dave Jones:** pretty low. Oh no, here we go. Okay, normal mode current, 138 milliamps. You pay a hefty toll a fee for your fancy whiz-bang OLED display there. Anyway, I'm just going to uh clean up that board a little bit.

**Dave Jones:** Make sure that's all hunky-dory, and then I'm just going to re-power this thing uh back up, cuz you never know, you know, could just be like a bad contact on the OLED um on that uh board-to-board interconnect or something like that, but

**Dave Jones:** Nope, still deadski. Okay. So, unfortunately, it's just really annoying to troubleshoot this because as I said, I'm going to have to solder some wires on there to actually measure it. And that other chip there is a C2P A51.

**Dave Jones:** It's obviously a linear reg there. So that's maybe for the local digital. Bloody black solder mask makes it hard to see. With the inter- we'd be using the internal switch as pin two. Oh, pin two is not connected to the inductor

**Dave Jones:** there which is rather interesting. And pins one and eight aren't connected either. So it's not in the usual buck configuration. So yeah, the most annoying thing about troubleshooting this is that you have to put it back in the case in order to get the switch on

**Dave Jones:** there to get the power into the circuit and get it, you know, fired up and doing the right thing. And then you've got to put the top on unless you solder like power wires onto there to power the

**Dave Jones:** thing and simulate the battery. It's really annoying. And hopefully like these and these wires then have to go out through the blast wall over here which has deep penetrators in it. So like I get trying to get these contacts onto here without

**Dave Jones:** damaging these what like oh Yeah, that just wasn't going to work putting the case on. So I just soldered external power supply in here. 6 volts 1 amp. 1925 milliamps 20 milliamps. So we got the Right, so it's doing its thing. Um by

**Dave Jones:** the way, little pro tip you can't see it here but the cables that I've got running in here like this. Um you can't just have them dangling off the edge of the bench cuz then like the weight of the cables will actually pull

**Dave Jones:** these wires like straight off. Like So yeah, so I've got a little weight here on the cables just or you can stick them down to the bench just to make sure that these don't, you know, the weight of

**Dave Jones:** these leads just don't fly off the bench if you've got them like hanging off the bench or whatever. So anyway, so I've got a ground here and so this is the switching converter. Okay, so we've got 7.7 volts on that cap. So that's higher

**Dave Jones:** than the battery voltage. So that's a boost input. I think this is the input. Okay, 5.2. That sounds like an input voltage. Then this should be the output voltage of that regulator. You'd expect 3.3, 3.5. Okay, that's seems to be precisely 3.5.

**Dave Jones:** So okay, that seems fine. So I'm going to rule out that linear voltage regulator there. There's no way it's going to fail. Like if it's a meant to be a 3.3, it's not going to fail to like precisely 3.5. Obviously, you know, it's

**Dave Jones:** 99.9% sure it's set precisely to 3.5 volts. So it's a 3.5 linear reg. So 7.7 volts on that OLED on that boost converter there, that sounds reasonable. So if we go over to the data sheet for the SSD

**Dave Jones:** 3303, once again, this is just the driver chip, not the whole board. The whole board is a Agilent Keysight designed board. But there you go. High supply voltage VCC 7 to 16 volts. So 7.7 should be working. Like I don't know if

**Dave Jones:** that's what it was intended to be. Maybe it was intended to be higher and then maybe it's dropped a bit and it's a bit it should it's within the operational range, right? And that logic supply voltage there can be as high as 3.5

**Dave Jones:** volts. That's its operational range. So they've set it to 3.5. Okay, no worries. They're within the voltage range. And the connections as you saw to the OLED display looked fine because they're not like an adhesive bond. They're properly

**Dave Jones:** soldered down. So it seems like it's an OLED failure. Let me go check if there's any history of this. Sure enough, EEVblog forums got everything right. OLED slowly going bad and there's replacement videos. And Ian Scott Johnson has got a video down here

**Dave Jones:** coincidentally um this afternoon or this evening I'm actually doing an amp hour with Ian Scott Johnson. He's going to be on the amp hour so check that out. I'm actually recording that tonight. So what a coincidence. So yeah, he's done a

**Dave Jones:** video here. I haven't haven't watched it but yeah, it's I think he's had the OLED fire. There's there's the that's a different one. That's a okay so the I cuz this is the 1253. Okay, so they've updated it

**Dave Jones:** slightly but physically it looks physically it looks the same but it looks like he's got a replacement one or he's yeah, he's physically replacing the OLED strip and there's another video over here Stuart Rogers. It looks like another repair. Yeah, that's that's the

**Dave Jones:** board. There you go. So this is a thing removing that so yeah, it looks like you can buy the oh, it's stuck down too. That's annoying. You got to heat it up to get it off. Anyway, it's damaged

**Dave Jones:** damaged anyway. So that's what it looks like the problem is. I'm not even going to bother looking any further. In fact, I probably didn't even have to measure these voltages. It was fun anyway. So yeah, I'm I'm just going to leave it

**Dave Jones:** now. I'm going to go order a new OLED screen see if I can get this back working. It looks like yeah, it's a thing. These things fail. Let us know in the comments down below if you've had one of these Keysight Agilent OLED

**Dave Jones:** multimeter fires. It looks like a lot of people have and they've done repair videos on them. So there you go. I could have found that out. I probably didn't even have to test it. I could have just went

**Dave Jones:** dead OLED. You know, 90% chance of it actually being the OLED screen. I could have just ordered one without even opening this puppy up if I actually did some research beforehand. And I'm back. I've got a screen. Got it delivered. Hopefully it's

**Dave Jones:** the right one U1273. So um if it's not the right one, then apparently we will get a bit shifted, like an an inverse image, because the bit is bits are shifted or something like that. So, you have to get the

**Dave Jones:** correct one, but tada, there it is. And here's the original. It's not a copy of it. It's a complete uh like reverse-engineered job. So, here's the original and here's the new one here. Look, oh, we've got a got the

**Dave Jones:** programming header here. Yeah, it's got a micro in there. Have a look, but he uses a totally different look. This has got the chip on board over here. They've got a micro here, which is programmed to like actually decode whatever, you know,

**Dave Jones:** bit stream that this requires for this to drive a a completely different OLED screen. So, let's go down in there and have a look. And there we go, STM32. There you go. So, all the STM somebody I mean, this is such an issue,

**Dave Jones:** right? This There's so many meters that have failed that somebody um has gone to the effort, presumably in China, to actually reverse engineer this screen here, like to reverse engineer the protocol and everything and the chip set or whatever, and drive,

**Dave Jones:** well, the protocol um used to, you know, map the stuff onto the uh screen, and program a custom micro to drive whatever screen that is. So, there's the uh there's the code for the new screen. There it is there, for those playing

**Dave Jones:** along at home. Um so, I don't know, I might overlay some data here for that one, but I won't check that now, but yeah, it's compatible and they've put in the programming header. Nice. And they've got, of course, the

**Dave Jones:** relevant uh voltage drive. So, um fingers crossed. Let's actually plug it in and see if it works. Cuz apparently, um Ian Scott Johnson got his one um he had one that was back to front, apparently. So, yeah, there we go. And since I've done

**Dave Jones:** the teardown, I've actually lost one of the screw lost one of the screws. Oops. Oh, wait. I've I've taken the wires off. Everything's gone. I'm sure there's a plastic cover on there. Let me scrape that off. That would have been

**Dave Jones:** embarrassing if I left that cover on and uh Come on. You can do it. There we go. Beautiful. Like a bought one. Three screws will be enough um cuz yeah, I don't I don't know. It's got to be on the

**Dave Jones:** bench here somewhere. Or it might have fallen on the floor. It's probably on the carpet. Can't forget our speaker. So, let's put that back on. No, that's not going to pinch. No, I ain't where We're going to be good to go. Will it

**Dave Jones:** work? Will it work? Uh Huh? Uh I have not got all the batteries in. Is it not making Oh. Whoa. Oh. Something's not making Oh. It's not It works. It work It works. LOOK AT THAT. OH, IT'S LIKE A BOUGHT ONE. Um yeah,

**Dave Jones:** I've got to screw the case back together. All right. So, it is back together and look at that. Uh thing of beauty, joy forever. We're getting some flicker on the screen here, but that's only on the screen. I don't see that in real

**Dave Jones:** life. That's just the camera frame rate there. Oh, look at that. No worries. So, that is one gorgeous looking screen. If it's a bit of a power hog, but there you go. And I'm sure this thing works absolutely fine cuz there's

**Dave Jones:** nothing There was nothing wrong with it. It was brand new. Basically brand new in the box. Never really used it, but the screen just died as most of them in this in in the both the U1250 series and the 1270 series

**Dave Jones:** with the OLED screens, they all just die. So much so that there's a whole third-party market of compatible screens. It's unbelievable. Now, this wasn't cheap. This cost me like 80 US dollars to get this replacement screen module. You might be able to get a bit

**Dave Jones:** cheaper if you just get the the actual you can if you're lucky you can find one of the original OLEDs and replace it but then you might end up with the same problem because the fire is inside the OLED whether or not it's

**Dave Jones:** inside the cable whether or not it's a physical manufacturing thing inside you know all the magic smoke escapes from the OLED in there and it it completely comes the outside so yeah I wouldn't recommend that I'd recommend the third party board which

**Dave Jones:** presumably uses a completely different OLED which is not well it's probably hopefully not susceptible to fire but there you go that is that is beautiful. You can of course get the LCD version the U1272A and these are these are

**Dave Jones:** excellent meters I you know they're really good. I'm surprised they're not more popular actually they're really incredibly feature packed. They don't you know bang per buck whatever but you know it's it's a pretty decent they're really good meters

**Dave Jones:** they're super fast they're super accurate. Well I thought this video was done and dusted. Unfortunately I discovered two problems with this one's minor one's pretty major. The first one is you know how I mentioned the reverse back to front display well watch this

**Dave Jones:** works a treat turn it off turn it back on boom it's back to front. If you turn it off too quickly it actually it looks like it doesn't reset properly. Now I can leave it off for a few seconds

**Dave Jones:** there there you go. Yeah yeah we're good and if you go into the setup and the setup's just fine right it's got a comprehensive setup you exit the setup it resets itself it's come again. So there's obviously something to do with the reverse

**Dave Jones:** engineering of this particular new display in here that it's I it's some power on resets not working properly. That the meter is back to front. Come on. It's hilarious. Anyway, yeah, it doesn't actually reverse itself. You just got to

**Dave Jones:** leave it off and then turn it on. So, yeah, oopsie, but minor, I guess you could live with that. Now, I only realized this after I actually uh shot and edited and almost ready to release this video. I was bragging about how I

**Dave Jones:** was going to sell this um on eBay starting at 99 cents. I was going to auction it off. But, anyway, I was bragging that this thing was obviously going to be within spec because it was brand new in the box and the only thing

**Dave Jones:** wrong with it was the LCD and the uh contaminant battery contaminant hadn't gotten anywhere on there. So, you know, of course this thing's going to be bang on. This is like a high spec meter, right? I can put up the specs here. But,

**Dave Jones:** look. Look, it's 1.1% out on DC volts. Are you kidding me? What the Now, it turns out if you're on the low end of that um like the same range, okay, the same like a 3-V range cuz this is a

**Dave Jones:** 30,000 count full scale, then like it's pretty close. And if you go to millivolts, it's actually, you know, that's within spec. Okay. But, why on volts, if I change that to 1 V, look, it's like come on. No. And at full scale there, look at

**Dave Jones:** 3.04. You got to be kidding me. This is totally out. So, it looks like on both the 3-V range and the 30-V range, it is out. But, it's not out on the millivolt range. So, now I've got a

**Dave Jones:** bloody calibration check this whole stupid meter. Unbelievable. Bloody Murphy. And on my precision AC calibration standard, I've got it set to 1 V here and 1. 01. So, what what 1. nominal 1.8% out. And just to show you

**Dave Jones:** that that is bang on. This is a really schmick um you know a transfer standard AC volt standard. And you can see I got a 1272A here. It's bang on. So this one is out. Now whether or not that

**Dave Jones:** considering that it's both out by a similar amount on AC and DC volts shows that possibly the input voltage divider has drifted there. Now of course you don't need that divider when you're on the millivolt range. So the millivolt range is going

**Dave Jones:** to be bang on. So I reckon if I go to millivolt range here if I change that to 100 millivolts it does take time to settle but they are like well what like well within spec 99.94 right? No worries

**Dave Jones:** and this one here let's go to millivolts and yep there you go. That's within spec so that's fine. So it shows that possibly something's up with the voltage divider in this thing. Now of course we could go through the calibration procedure. I

**Dave Jones:** have checked you can actually get the service manual for this thing. But I I don't know. Like is it going to like drift like with time? Who knows? And once again on 10 volts that is out by 0.2. I'll go up to the

**Dave Jones:** 100 volt range and we'll try that cuz this thing can go up to 1000 volts so it's pretty 1100 volts actually. Yep it's so all of those voltage ranges are out. So that indicates yeah it's a like divider thing. I can't believe like

**Dave Jones:** there's a calibration adjustment problem in this meter. So we're back inside again having another squeeze and this is where you know your visuals didn't really pick it up last time. But you remember how obviously the only leakage was around this part here and

**Dave Jones:** then but now with hindsight right this is this is the input AC coupling cap. So let's not worry about that. But this pin here this is the top side of the resistive divider, right? This is the resistive divider here. Here's the the

**Dave Jones:** ceramic and you can see it's it's shielded here. So the ceramic, it's there, right? So we've got, you know, just like a shielding pad here, which you can see that with hindsight there has actually been a bit of

**Dave Jones:** corrosion on there, right? Check it out. You can see that there. But that doesn't explain why we're out. The only reason we'd be out is if like there's extra load across this divider. There's some contamination under that marks. Perhaps that's causing some sort

**Dave Jones:** of issue. So cuz this is how you get the different ranges. You get the different ranges from this resistive divider and they put them on the ceramic. I've done a video on that showing the like they laser trim cuz they're really

**Dave Jones:** stable and you can match them and then they thermally they've got really great thermal properties and matching. So all of your ranges match. So your good quality high precision meters are going to have a a hybrid ceramic resistor divider in

**Dave Jones:** them and this one does. So obviously I reckon something has gone wrong. Like there's no other reason for this meter to drift like that. And did contamination get onto the onto the ceramic divider itself? I don't know. I'm going to have to desolder the

**Dave Jones:** shield to get in there and have a look. Ta-da! There we go. We've got that out. There you go. It's a top quality Caddock. No worries there, but like you can't get in there. It's like sealed. Like it doesn't have a

**Dave Jones:** surface on it. Like some of them have an external surface. This one doesn't. In quite a lot of them you can actually see the like the actual resistive elements actually patterned onto the carbon and then little laser trim marks and

**Dave Jones:** everything on there. But no, this is a fully sealed thing. So, I don't see a problem. I I I can't imagine a problem within there. I'm guessing contamination somewhere else that's loading down the resisted divider. And if you don't fix

**Dave Jones:** that sort of problem, then yeah, I can recalibrate this and I'm sure it'll work fine for now, and then it could drift further. Yeah, I was looking to get in an ultrasonic bath. I'm like, "You got to throw it in an ultrasonic bath. It'll

**Dave Jones:** clean it." Yeah, I don't have one yet. So, well, I'm going to give it a thorough shellacking with some ultrasolve uh cleaning solvent um which, you know, a bit better than uh isopropyl. I don't know. Um you know, can it penetrate

**Dave Jones:** under the chips and everything? Don't want to go like removing all the chips and everything else. So, after a thorough spanking, nope, it's still out. So, I've come back the next day, left it overnight, and look, it's it's a bit

**Dave Jones:** closer. So, I think we're getting there. I think maybe we can might have to uh take a few things off the board or something. Hm. Right. So, back to here again. Now, you got to remember that uh the impedances are around here. Your

**Dave Jones:** standard meter is like 10 megaohms input impedance. So, all the impedances around the uh top side of the voltage divider here, they're very high. So, it doesn't take much leakage at all on the top side of a resisted divider, leakage due to

**Dave Jones:** contamination under a chip, you know, PCB uh creepage and stuff to be an issue. So, they've removed the solder mask around here for a reason, right? Because this is a high impedance uh part of uh the top side of the uh resisted

**Dave Jones:** divider here. Now, we've got this big ass series cap here, and that is the top part of your resistor divider here. So, um I'm inclined to take that cap off because that's, you know, like smack on where the uh contamination actually came

**Dave Jones:** through. So, yeah, I'm going to take that cap out. It'll function fine without that cap. It's just like a you know, an AC bypass type thing. So, as far as DC's concerned, we can take that off and we should be if the leakage goes

**Dave Jones:** away, then we know, "Aha, we've got it." Right? And then we can measure that cap out of circuit. So, even though this is in circuit, we should measure in the order of 10 meg there. And sure enough, there it is, right? 9.9

**Dave Jones:** That might eventually go up to 10. So, we might have another meg here and it might be like a total of 11 meg input impedance there. But yeah, so that's across that cap. So, it doesn't take much leakage at all for that to

**Dave Jones:** become a problem. And of course, on the 200 mV range, it doesn't use a divider or 300 mV range, it doesn't use a divider. It doesn't use that divider. It basically bypasses it. So, any contamination causing extra parallel

**Dave Jones:** impedance there isn't going to cause a problem, at least in terms of accuracy. It's just going to slightly change your input impedance and who cares?

**Dave Jones:** There we go. Now, of course, it's hard to tell, but you know, there could be it could be something there. Like, you know, you can see some paths there and the bottom side of that cap is well, it's

**Dave Jones:** not terrific, is it? Look at that. I think I think we might have a bit of a culprit here. Yeah, like you can see like there could be like a leakage path there. It's obviously had something Well, we know what. It's the alkaline

**Dave Jones:** from the battery is is been trapped under there. Yeah, you can just see it there, right? It's There's definitely leakage under that. So, I'm going to I'm going to give that clean again and then we'll just run the

**Dave Jones:** meter. Cuz as I said, in DC volts, that cap's not going to matter. Now, as far as that cap's concerned, we can attempt to measure that, but we're not going to have any success, I suspect, because any contamination like it was just

**Dave Jones:** dried out by the hot air that I removed this thing with. Can't remember the range of my national insurance meter here. Is it 100 meg? So, I'm going to clean up that cap and um we can just actually put that back in. So, I don't

**Dave Jones:** think it's damaged the actual ceramic of the cap cuz you got to remember the capacitance elements are inside there. So, you know, we should just be able to clean the outside and yeah, it should be good to put back in. Aha, we haven't

**Dave Jones:** come back within spec yet, but well, it's on its way up. Yep. Yep, I think we cracked it. Yeah, we've had contamination there like I haven't dried out the board properly yet, but yeah, that has solved it. You

**Dave Jones:** can see how that's clearly moved. We were, you know, 1% over 3 volts before and the theory pans out that, you know, that high impedance side of the input voltage divider, yeah, I think this thing is going to be absolutely

**Dave Jones:** fine once this thing just dries out and we've cleared all the contamination. Cuz once the contamination is cleared, then we're back to where the original factory calibration would have been. So, yeah, that's just slowly going to eat up.

**Dave Jones:** Yeah, we've just just needs to dry out. That's all, but we've confirmed it. Soldered our freshly cleaned capacitor back on there and I do believe we can declare that a winner winner chicken dinner. That is within spec. Once again, like it might dry out

**Dave Jones:** a little tad more, but yeah, anyway, shields back in place, the capacitors back in place, that series resistor there in series with the cap. That was just a bead like in just an RF bead there. And look, absolutely fantastic. So, yeah, no

**Dave Jones:** worries. I'm sure the AC will be spot on as well. And of Of it is. There you have it. So, yeah, it's basically bang on to its original factory calibration. No issues whatsoever. So, I'm going to give that a

**Dave Jones:** thumbs up. And if you like that repair video, please give it a thumbs up as well. I don't even have to check the other ranges. It's just like okay. And there you go, bang on at 100 volts as

**Dave Jones:** well because well, engineering works, right? It's you're talking about resistor high impedance resistor divider ladders here. And if one was out, then it's obviously that the other ranges that use that resistor divider would be out as well. And I've checked some resistors as well,

**Dave Jones:** spot check. It's absolutely fine. So, it was just that high end leakage on the high end of the resistor divider ladder there that did it. And whether or not say an ultrasonic clean would have got that out from under that cap, I don't

**Dave Jones:** know. But anyway, yeah, we just took it out, give it a bit of a clean, back it back. No worries. Bob's your uncle. That is a repair video. So, if you like that, please give it a big thumbs up. And as

**Dave Jones:** always, discuss down below. And I will actually put this on eBay starting at a 99 cent auction on the eBay blog store. So, go for it. Catch you next time.
