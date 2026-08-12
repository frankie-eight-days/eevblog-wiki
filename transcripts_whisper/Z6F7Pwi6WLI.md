---
video_id: Z6F7Pwi6WLI
title: EEVblog #1174 - Rohde & Schwarz PSU Teardowns
url: https://www.youtube.com/watch?v=Z6F7Pwi6WLI
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 30, "2": 52, "3": 77, "4": 95, "5": 114, "6": 133, "7": 145, "8": 161, "9": 184, "10": 199, "11": 211, "12": 226, "13": 239, "14": 259, "15": 275, "16": 291, "17": 308, "18": 326, "19": 346, "20": 364, "21": 381, "22": 401, "23": 417, "24": 437, "25": 463, "26": 477, "27": 494, "28": 509, "29": 529, "30": 545, "31": 562, "32": 579, "33": 596, "34": 615, "35": 634, "36": 652, "37": 669, "38": 686, "39": 702, "40": 721, "41": 739, "42": 759, "43": 774, "44": 794, "45": 810, "46": 827, "47": 849, "48": 881, "49": 901, "50": 926, "51": 948, "52": 971, "53": 984, "54": 1005, "55": 1021, "56": 1037, "57": 1051, "58": 1069, "59": 1082, "60": 1093, "61": 1108, "62": 1123, "63": 1141, "64": 1158, "65": 1177, "66": 1201, "67": 1216, "68": 1234, "69": 1250, "70": 1263, "71": 1285, "72": 1301, "73": 1315, "74": 1331, "75": 1346, "76": 1366, "77": 1382, "78": 1398, "79": 1418, "80": 1438, "81": 1459, "82": 1473, "83": 1490, "84": 1508, "85": 1526, "86": 1541, "87": 1560, "88": 1575, "89": 1591, "90": 1605, "91": 1622, "92": 1638, "93": 1660, "94": 1683, "95": 1704, "96": 1722, "97": 1739}
---

**Dave Jones:** And there's the little Ethernet slash USB board. Isn't that nice? I like the quality of the PCB material there. It looks really schmick. Nice gold-plated card edge connector. And we've got an ST-ARM micro for those playing along at home. And a Mikrel jobby there, is it?

**Dave Jones:** And what else? An Altera. Something or other? That's a little FPGA or CPLD, is it? These are bloody self-tappers. Look at this. Unbelievable. Ha! Got it for Nix anyway. Yep, so we had to get that off to take the whole back panel off here.

**Dave Jones:** So self-tappers into there. That's a bit how you do it. And then just two oddball self-tappers on the bottom. And... It looks like... Well, it was starting to slide. There we go. Oh, we're in like Flynn. Wow, look at that. Open chassis. Look.

**Dave Jones:** Look at the big-ass toroidal transformer. Oh, beautiful. Thing of beauty is a joy forever. Of course, they haven't made the mistake of, you know, shorting out that nut to the top. Yeah, it's, uh, yeah, it's not touching the, uh, top case because then you get a shorter turn and that could ruin your day.

**Dave Jones:** Assuming that it's connected down to the bottom. Yeah, look at that. Oh, wow. Look how they've done that. Thoroughly interesting construction. Look, they've got this open frame. They've got this big-ass heatsink. You can see the fins right in here, which goes from one side to the other.

**Dave Jones:** So one side has the fan on it. You can see the fan down there. And they're just, like, extracting it like that. That is fascinating. You've got to ask, though, why make it this length, okay? You've got to make it this big. You've got this big-ass toroidal transformer here, which is beautiful.

**Dave Jones:** This is a three-channel unit, okay? So you've got the optional third channel up here. You can see all the mounting holes for that. Like, could you have shrunk the board a little bit more and got rid of it and made it this long?

**Dave Jones:** Like, maybe this long instead of that long? I don't know. Maybe they had... Maybe they had some requirement to make it that length. That's just my feeling, though, is that it could have been made a bit shorter. There's our relays, of course, for our tracking switching.

**Dave Jones:** You can see those down there. That's very nice. These boards are completely galvanically isolated from each other. But isn't that... That's just gorgeous design and construction. I really love that. And they've actually put... A metal on top here so that it didn't interrupt the airflow going through here.

**Dave Jones:** Because you see how we had all those vent holes over here like this, which helps with the radiated heat. But, of course, you don't want your airflow to be interrupted. You want it to all come from your fan here and all go right over the fins of the heatsink.

**Dave Jones:** You don't want it buggering out in or out of these holes here. So, yeah, you want to put that top cover on there. That's nice. But there's a big relay. There's a big relay over on the mains section here. Oh, and look at the...

**Dave Jones:** Oh, hang on. Look at the real clunk and power switch with the rod going through. Oh, beautiful. Brings a tear to the eye. Check out the mains input board here. Look at that big EPCOS choke there. That would have cost a fortune, wouldn't it?

**Dave Jones:** That's just... That is beautiful. Look at the little ferrite ring they've got around those. They've cable tied those together. And, of course, your earth is... It's going from... Yeah, the main board down there. It's all crimp. Properly and going over to the case.

**Dave Jones:** Oh, it's beautiful. Nice, neatly wired. Ah, it's just gorgeous. Genuine Omeron relay for all you Omeron fanboys. There's a lot of them out there. And why they've got that on the mains board? What are they doing? And they've got two wires going over to the power supply section.

**Dave Jones:** I'm not sure what it's doing there. I mean, you know, we've got the big mechanical clunk and mechanical power switch here. So, it's not like a soft... Power switch. Nice attention to detail on the interface board, too. Look at that. They've got the ribbon cable.

**Dave Jones:** Got a little ferrite around that. And that's going over to your front panel. Isn't that neat? Oh, a bit of flat flex. And it's really interesting how they've done this. I mean, check out how much room they've got in here. You could swing a Schrodinger's cat in here.

**Dave Jones:** It's unbelievable. Like, here's your front panel board over here. Okay, there's your... They've got ceramic. They've got ceramic output caps. That's interesting. I would have... I'm sure they're like, you know, the proper Termination ones. So, they're not going to catch fire. I've done a whole video on that.

**Dave Jones:** Here's your wiring coming over from the front. They've even matched the blue. Look at that. Isn't that gorgeous? And then here's your wiring buggering off right to your back terminal. You've got your power wires plus your sense lines as well. Looks like we've got an Atmel microcontroller down there.

**Dave Jones:** Handling all that. Business. What's that micro? I can't read that on the screen. Controlling all the business on there. Got some local regulation here. And another OMRIN relay to do the switching. And you'll notice that this channel, 5 amp rated, this beast over here is just flapping around in the breeze.

**Dave Jones:** But this one up here has an angled heatsink. Going back over to our main heatsink, they've got a seal pad on there to isolate that. So, this is the 10 amp channel. That's not going to be... the output transistor. Maybe that's the over-voltage clamp, perhaps.

**Dave Jones:** Because it's right near the output like that. Oh, actually, that's a single jobby. You can see there's some extra holes there. And this one, dual. There you go for the 10 amp one. So, we've got them back to back there. I've got to read a part number off that.

**Dave Jones:** Aha, that's actually the output current sense resistor. That's a PBHR. That's R100. So, R100 means 0.1 R or 0.1 ohms. So, that's 100 milliohm shunt output shunt resistor. Here's the data sheet for that. And, of course, they needed two of those. They're probably, I don't know,

**Dave Jones:** whacking those in parallel for the 10 amp job. So, that makes sense. It's a 3 watt precision power resistor. Not necessarily a fan of these big tall caps here just flapping around in the breeze. I would have, like, gunked those together. I would have liked to have...

**Dave Jones:** Oh, I've seen that. Anyway, got some extra little power trannies down in there by the looks of it. Maybe they're, like, a part of a Darlington pair for the main power transistor. I don't know. I'm just guessing there. But, hmm. Oh, what's that linear tech jobby?

**Dave Jones:** What is that? And Nichicon, of course. Spared no expense. Spectacular. Spared no expense. Once again, the 10 amp module is actually significantly different. Look at this big choke here and compared to this one over here on the 5 amp. They look like a very, like, you know, very similar configuration.

**Dave Jones:** They've both got these three caps here, these two caps in here, but very different little choke up here. Well, little. Huge. Look at them. But they've got two main filter caps are the same on both. And as for the bottom of the board,

**Dave Jones:** there's your big-ass bridge rectifier. Some smaller little bridge rectifiers in there by the looks of it. So they're just tapping off some multiple stuff. Oh, it looks like we've got some surface mount fuses in there. Oh, look at that MELF resistor. They had to have one MELF resistor on the whole thing, didn't they?

**Dave Jones:** Yes, thank you very much. You know I love my MELF resistors. There are our output power transistors. Like, it just seems out of whack. There's our output power transistors and there's our big-ass bridge rectifier. Oh, look at that little bridge rectifier on the input.

**Dave Jones:** Unbelievable. Anyway, that's a big-ass surface mount inductor. And looks like we've got a couple of little optocouplers there on the output. And that's about all she wrote. There's our reverse diode protection on the output. And not much else doing on the bottom. Oh, they're actually not the same.

**Dave Jones:** I thought they'd be identical. And there's your high-voltage noise suppression cap going to mains earth. Because this screw, goes like this little isolated bit of copper here, which isn't connected to anything else, but it's connected to that screw, which is connected through to the heat sink,

**Dave Jones:** which is, of course, connected through to your chassis and hence your mains earth. But, of course, these are galvanically isolated outputs. So, this is your actual output ground, part of your circuit from your bridge rectifier going through to your output. But this one's interesting

**Dave Jones:** because they've got three parallel pads here that populated one. And, of course, you wouldn't really need to populate more than one, but why you'd have three pads as part of your layout, I don't know. That position's not really going to matter. Hmm. Bueller.

**Dave Jones:** Bueller. So, that looks like a real robust and professional design as you'd expect. And, of course, like on a real high-cost professional supply like this, you know, you're going to get, like, your noise performance, your common mode chokes and, you know, everything to prevent, like,

**Dave Jones:** mains noise and stuff getting through, you know, the big EPCOS filter up here is just, you know, like really spared no expense in getting that down. And that's what you're paying for in, you know, a real top brand professional power supply as opposed to some one-hung low eBay cheapy

**Dave Jones:** or some, you know, built down to a price kind of power supply. So, I'm just thoroughly impressed by that. That is just some nice, brilliant design and construction. Oh, sorry. I thought these were the output caps, but they're not. They're also going down to noise suppression,

**Dave Jones:** down to mains earth down there. That is your tiny amount of output capacitance. One little ceramic jobby. Yes, I do hope that is a, you know, one with flex terminations on the end. But, of course, this board's not going to flex. But still, you know, I probably would have put two in series maybe

**Dave Jones:** just to gild the lily. But, anyway, you don't want to... You don't want a large amount of output capacitance because, in constant current mode, if you have two larger output capacitance, it can effectively override your constant current mode and then dump the energy in the capacitor

**Dave Jones:** into your poor little device under test and, well, your current limit didn't do its job because there was all that reservoir capacitance on the output. So, you really want a minimum amount of output capacitance just enough to keep your control loop stable and that's it, no more.

**Dave Jones:** The cheapest power supplies might have, you know, a large amount of output capacitance just to make the control loop more stable. They just, you know, whack it in until it's stable and Bob's your uncle. Oh, but, of course, your earth filtering caps in here,

**Dave Jones:** they're also going to be basically two capacitors in series between your output there, except that the center tap is going to earth. But it is effectively output capacitance too. And there's our front panel micro so that it'd be running all the, effectively, the OS for this thing

**Dave Jones:** and, of course, we saw the individual microcontroller on the individual output boards, but this would be running, like, the display, the interface, the ethernet and all the, you know, the USB control and all that sort of jazz. So, there's not much else on that front panel board.

**Dave Jones:** The paranoia in me, though, can't help but think, that screw's a little bit high. Phew, look at that. It is below the surface of that, but there's nothing inside the case. Like, there's no insulating sheet inside the case to prevent. And there is a bit of bow when you put this case on.

**Dave Jones:** You can actually press it down a little bit. And in theory, you could actually press it down onto that bolt and you'd have your shorted turn from the top to the bottom. So, should I give it a go? Should I poke the top of this?

**Dave Jones:** Three amps, look at that. 3.6 amps. Don't want to short your turn out. Dope. All right, check this out. I'll put the case back on. Hopefully, you'll be able to hear this when I press on it. See? It bottoms out. So, if you actually had, if you set something on the top,

**Dave Jones:** that would, you know, like, I don't know, another instrument or something, I don't know, your coffee mug wouldn't do it. But, you know, if you put something, it requires a fair bit of force. But there's like, you know, in maybe three or four millimeters of travel,

**Dave Jones:** but it does actually hit the bottom of that. So, in theory, but it's probably protected by the coating on this. It's not bare metal on the back, so they've got coating. So, it wouldn't short out. But, like, if you had a sharp bolt on there that could pierce through,

**Dave Jones:** that's possible. Hmm. And I'm nitpicking, but I just noticed that. Now for the NGE-100. Oh, it's the 103, I think. Warranty expires if broken. Well, bugger that. It's not even a, it's not even a screw under it. So, that's the back cover. How does that come off?

**Dave Jones:** Ah. I got two of the screws out. What's going on? Okay, that was... Oh. Yep, it's upside down. Whoa, there we go. Well, that... They're in like flint. There's the bottom part. Oh, that's... Like, why? Why? Why do you have a very neatly laid and gunked down wire?

**Dave Jones:** That is a beautiful mod. Um, but I can't help but think that's intentional. I mean, why? From... I, I don't know. And they've done this, um, well, this one is the, uh, looks like that. That's going to, uh, your mains. That's going to your chassis, mains earth.

**Dave Jones:** And that's going, buggering off under there. That's your USB port. Wow. Are they serious about a low impedance earth path to the USB port? Very uninteresting on the top. So, we're gonna have to get in there and have a squiz. But once again, a really big ass toroidal transformer in there somewhere.

**Dave Jones:** And, well, somebody had fun with their, um, wiring sleeves here. Wow. Okay. They really didn't maybe want any sharp burrs or anything to cut through the wires. And it looks like they're all cable tied through there. Wow. Okay, so what we have here, three screws on either side.

**Dave Jones:** It looks like it's gonna let you pop out this module. Presumably with all the... I actually think it's gotta tilt out this way. So, maybe I need to put it like that. 'Cause you've got the heavy toroidal transformer at the front here. Wow, this is really comp-- some compact system engineering.

**Dave Jones:** Oh, I'll get back to you. I feel like I've gotta be a contortionist to get this out. Maybe I can get down there and pull the... No, they're all-- all the connectors in there are solastic. You can't see that, but you will in a minute.

**Dave Jones:** I'm gonna assume that... This sort of swings out like this. But I can't... Hang on. Oh! I think I got it. Something went crack. And... I... Oh! Yeah. Yeah, nah. I gotta get these cables out here first before that'll flip out. Ha! I have conquered it.

**Dave Jones:** Um, yeah. Look. We... We had to, like, take out the fan. Like, had to systematically take out this cable over here. Then... Then the fan. Then this one as you opened it up. But... Look at that. Isn't that just... Like... That is just fantastic.

**Dave Jones:** Um... System design. How... The compact nature of how they're... You know, they leave all this space in here for this big-ass toroidal transformer. Once again, I don't think we have an issue there. That... Bolt's not gonna be a problem. But, uh... Soon on, uh...

**Dave Jones:** Fan. For those playing along at home, you'd like to see their fan brands. Oh! Sorry. I think I shot all that with manual focus on. D'oh! Sorry if that was all out of focus. We're back in focus now. And, uh... Beautiful! And we can see...

**Dave Jones:** Our separate channels on the PCB. It's one big-ass PCB. But you can physically see the galvanic isolation on... Between all the channels. And, of course, they're all gonna be identical. 'Cause the, uh, power and performance on this model, I believe, is all identical.

**Dave Jones:** Got the big-ass cats. We'll have a look at those in a minute. Surface mount, uh... Heatsink on there. So... Not much doing. And wiring... Is just, uh... Looks like it's just soldered... Uh... Flat onto the PCB. That's interesting. Yeah, that's a really interesting...

**Dave Jones:** Arrangement. Look at that. And, of course, they've got a sense line coming back. Which is... You know, nice. You'd expect this in a professional, uh... Supply. So it's reading the voltage directly at the output terminal. Of course, this is... Doesn't have any... External sense terminal.

**Dave Jones:** Either on the front or the, uh... Uh... Uh... On the back. So... Uh... You know... Uh... It's not reading back on the front or the, uh... Rear. But they're actually making sure that they read back, uh... The exact value... From that. But look, they just, uh...

**Dave Jones:** Um... Just, uh... Tin those leads... And tap 'em down to the pads. I... That's... That's... Fine. I mean, it's just... It's neat and tidy. It's... Simple. Um... I just sort of like expected connectors, but... There's no reason you can't do it like that.

**Dave Jones:** It's perfectly fine. Once again... We've got our, uh... Mains, uh... Our output... Uh... To ground. Mains. We've got the compression cap there. We've got that... On each channel. And... Looks like there's no additional output capacitance on the... Output terminals. All of your output capacitance is contained...

**Dave Jones:** Here. And they've got different values in parallel. Look. Itty bitty teeny weeny. And... A 0805. And then a 1206. And then a couple more. Like that. Wow! They're... Like... Really serious about their different types of... Output caps. That would be our... Uh... Mains.

**Dave Jones:** Uh... Uh... Output caps. That would be our rever... Oop. That would be our reverse diode protection there. They're our current sense... Output resistors. They'd be... Uh... Tapping... They'd be doing your, uh... Kelvin connection to that. Tapping that off. Oh! More current sense... Resistors over there.

**Dave Jones:** And... As I said... The, uh... Output... Hang on. This has to be... A switching supply. Because... That... Heatsink. That little... Piddly, uh... Surface mount heatsink. I like that. Um... That is not enough. For a, uh... Linear... Supply. So... And... Neither is... That. Um...

**Dave Jones:** Heh. They're a fan of... They're a fan of their, uh... Gold dots, aren't they? Love it. Once again, we've got Nichicon main caps in here. There's our bridge rectifiers on the input. Yeah, so I think what we've got here is... This is actually...

**Dave Jones:** This is most likely the output, uh... Linear... Regulator. But it's got a, uh... Tracking... Switching... Pre-regulator here. These are, uh... 80 volt... Uh... Jobs. And... The... Full wave bridge rectifier from the... Uh... Mains creates a DC. And we've just got a DC to DC converter.

**Dave Jones:** Which then, um... Is... Tracks. You know... Only like a volt above. Or, you know... Half a volt above. So that... Um... Regardless of your, uh... Output... Voltage... Um... This is gonna be super efficient. So you only need a tiny heatsink... On your, uh...

**Dave Jones:** Secondary output, uh... Linear regulator. But of course... Using the output linear regulator... You get, uh... Much lower noise than a... Just a direct switching output power supply. And sure enough... If you have a look down in there... That's a... NCP... 1034... Which is a synchronous...

**Dave Jones:** Buck... Converter. There you go. So... Yep. They're just buckin' that down to... As I said... Probably... About... 50 volt... Per... Per... Per... As I said... Probably like... You know... A volt at most... Above the, uh... Output... Pre-regulator. And it's always tracking that. Um...

**Dave Jones:** So... Of course... This is... Getting rid of, uh... Most of your noise... They'd specially design... Usually like a lot of, uh... Secondary... Uh... You know... Linear regulators... Aren't very good. I've done a video on this somewhere. Um... Of like noise just... You know...

**Dave Jones:** Pass... A lot of the noise passes through. So they'd be, uh... Really looking for the, uh... Design... Of the secondary... Uh... Output regulator there. So this is interesting. Here's our mains... Uh... Power switch here on the front. It is a proper clunkin' power switch.

**Dave Jones:** Um... That comes from... Uh... The IEC connector at the back. No worries. Got a nice looking input... Uh... Common mode choke... And all the requisite, uh... Protections. Then we've got some sort of little, uh... Isolated, uh... Secondary... Power supply here. You can see it's a...

**Dave Jones:** The AC tap from the transformer... Bridge rectifier... And a... And that looks like... Maybe a little, uh... Switching... Converter or something there. Little fuse jobby down in there. This is actually the fan controller here. And then this... Is all your primary taps for your transformer...

**Dave Jones:** Which is connected... Over... Here... At the back... Of your, uh... Voltage selection... Switch over here. So how does the mains get from here... Bypassing all this... Over to here? You... You might think it's on the bottom... And... You'd be right... But... That's what...

**Dave Jones:** This bypass wire here does. It takes that mains... Over... There... To... Over to your... Primary... Transformer. So... What? They run out of routing room? To snake it over? Hmm... Because you can see the other trace here... Going... Actually on the bottom of that...

**Dave Jones:** Around like that... Just avoiding these two sections here. So... PCB designer went... Oh... Geez... What are you doing to me? Maybe it was like a... Uh... Uh... Uh... Uh... Later edition or something... Maybe they just got to the end of the layout... You know...

**Dave Jones:** And went... Oh... Yeah... Forgot all about these... Uh... We'll shove them in here... But... Oh... We don't have the electrical clearance... Um... No... Like slots routed or anything like that... Um... Which is fine... You know... If you've got the... Uh... Creepage... Uh... Distance across here...

**Dave Jones:** Creepage is across board... And... Uh... Clearance is across an air gap... So... You know... There's no... Uh... There's no... Uh... Uh... Creepage in there... But they obviously decided... Oops... Let's just... Run an extra... Wire... Okay... There's nothing wrong with that... It's done neat and tidy anyway...

**Dave Jones:** Hmm... Nice big board... And these are all your... Uh... Secondary outputs of the... Uh... Transformer... Going into bridge... Smaller bridge rectifiers... They've got multiple... Well... Two per channel... There's another bigger one... I'm sure... Three separate... Uh... Uh... Rectifiers there... Supplying... Various whatnots... And as I said...

**Dave Jones:** Electrically isolated... On each channel... You can physically see... The light shining through there... Let me get my torch... There you go... Look at that... Beautiful... Galvanically isolated... Between each channel... You might notice though... This ground up here... Once again... These are these AC...

**Dave Jones:** Caps... A lot of via stitching in there... And... They've joined these together... All three... Here... And... Here... All three... Snake up there... That's where it... Uh... Goes back to your chassis... There's our front panel board down there... There's our Wi-Fi-y thing... And... Uh...

**Dave Jones:** Looks like we've got a big ass Atmel... Processor down in there... That's running... Everything... You can possibly imagine... And... There's some memory... And... DRAM... And flash... And all that... So yeah... It's probably running some... Linux-y... Thing... I'm sure... Ooh... Look at the shield in...

**Dave Jones:** On the ribbon cable... Going over... There... Look at the... Scal... Uh... Celastic... Gunk... Somebody had fun... And you might be asking... Or you should be asking... Dave... If they're all galvanically isolated... Like this... How do they actually control... Each channel... Going over... Well...

**Dave Jones:** I'm glad you asked... Um... So all the control signals come over here... For all the three different channels... But you'll notice... Down in here... Boom... Boom... And... Boom... Down in there... That is your, uh... Serial... Like maybe a... Is it one of those...

**Dave Jones:** Uh... Analog devices... ATEM... Chips... Or something like that... Anyway... Just like... You know... Serial... They... They don't need anything... Like high-speed... Really going over... To each channel... But that's, uh... How they electrically isolate... The data... Going over to each channel... So once again...

**Dave Jones:** I'm thoroughly impressed by the, uh... Design, construction, and the engineering... Ooh... Just wanted to show you... There's those cable ties... And look... Oh... Look at all the... Wire... It's just... Beautiful... So that it... You know... It goes over the edge... And doesn't nick it...

**Dave Jones:** Fantastic... Um... Because like... 'Cause you gotta assemble... This like this... And the wires can rub over the... You know... Potential... They aren't sharp... But they could... You know... They could potentially be a burr there or... Something like that... Anyway... Beautiful like... Fit to envelope, uh...

**Dave Jones:** Design... They tried to keep this as compact as possible... Unlike the, uh... Uh... Previous ones we saw that were... Um... With that... But this is obviously for a different market... It's designed for a more compact... Uh... Benchtop... Unit... And... A very impressive design and construction...

**Dave Jones:** So this is the difference... And like... If you look at this... Like... Which is a thousand dollar... Uh... Class... Power supply... Compared to... Like the Rigol... Which is what... Four hundred dollars or something... You know... Like half that... Four... Five hundred dollar... Uh...

**Dave Jones:** Supply... Yeah... This one's... You know... A lot of work has gone into that... So... Hats off to the designers at Roden Schwartz... Roden Schwartz don't make crap... Uh... Stuff... They... You know... You pay your money... And you get... Your top quality... It's just beautiful...

**Dave Jones:** Ooh... This one isn't self-tappers... Heh... And the bigger one... We'll have a quick look inside... But I expect it to be... Uh... Very... Very similar to... The other one... Except... It's a... Uh... Uh... Uh... Uh... Uh... The other one... Except... Well... Ah... Ah...

**Dave Jones:** Ah... Ah... That's not a transformer... That's a transformer... Ugh... I do believe you'll find that this is near identical... To the other one... Except... You know... We've got the big... Uh... Uh... Dual... Uh... Current sense resistor here... Going back... It's like virtually an identical...

**Dave Jones:** Layout... 10 amp... Output... So... Yeah... Really identical across the series... The input... Uh... Switching reg... The input switching pre-regulator... Looks exactly the same... Um... So... Yeah... Nothing... Much to see... Except... Look at the badass transformer... Oh... I just can't get over that... And...

**Dave Jones:** Oh... Didn't the other one have a flat? And... Uh... This one just... Mounted vertically... Like that... And... The rod going through... It's just... Fantastic... Look at it... Bigger... And... Beefier... And of course... Those front panel boards down in there... They're gonna be slightly different...

**Dave Jones:** 'Cause the configurations are different... In terms of the... Uh... Sense wires... They're just like... Grouped in... Uh... Four... Two above the other... Instead of... Uh... Horizontal... Like we got... On the 2020 there... Don't know how to convey the size of that... Uh... Transformer...

**Dave Jones:** But like... There's my hand... Look at the size of that... It's... It's... Like... It's way more... Just that transformer alone... Than the entire NGE-100... Uh... Supply here... That's just... It's nuts... Thank you.
