---
video_id: 4-PhbPS5LQU
title: EEVblog #689 - Back To The Future Time Circuits Troubleshooting
url: https://www.youtube.com/watch?v=4-PhbPS5LQU
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 27, "3": 40, "4": 52, "5": 68, "6": 78, "7": 94, "8": 108, "9": 123, "10": 137, "11": 153, "12": 166, "13": 178, "14": 191, "15": 205, "16": 219, "17": 235, "18": 251, "19": 265, "20": 277, "21": 291, "22": 302, "23": 322, "24": 340, "25": 352, "26": 364, "27": 377, "28": 389, "29": 405, "30": 418, "31": 436, "32": 451, "33": 464, "34": 479, "35": 494, "36": 510, "37": 527, "38": 541, "39": 554, "40": 568, "41": 582, "42": 594, "43": 609, "44": 621, "45": 634, "46": 648, "47": 661, "48": 674, "49": 685, "50": 696, "51": 707, "52": 723, "53": 737, "54": 747, "55": 764, "56": 780, "57": 794, "58": 808, "59": 819, "60": 834, "61": 847, "62": 860, "63": 875, "64": 891, "65": 903, "66": 919, "67": 936, "68": 948, "69": 959, "70": 972, "71": 987, "72": 1002, "73": 1016, "74": 1029, "75": 1043, "76": 1054, "77": 1066, "78": 1077, "79": 1089, "80": 1106, "81": 1120, "82": 1139, "83": 1152, "84": 1166, "85": 1178, "86": 1195, "87": 1207, "88": 1225, "89": 1240, "90": 1254, "91": 1266, "92": 1281, "93": 1296, "94": 1310, "95": 1324, "96": 1338, "97": 1351, "98": 1368, "99": 1384, "100": 1397, "101": 1410, "102": 1424, "103": 1434, "104": 1451, "105": 1465, "106": 1482, "107": 1496, "108": 1508, "109": 1522, "110": 1533, "111": 1552, "112": 1569, "113": 1585, "114": 1601, "115": 1617, "116": 1632, "117": 1646, "118": 1658, "119": 1674, "120": 1687, "121": 1700, "122": 1715, "123": 1729, "124": 1740, "125": 1748, "126": 1759, "127": 1770, "128": 1784, "129": 1796, "130": 1810, "131": 1826, "132": 1840, "133": 1856, "134": 1867, "135": 1882, "136": 1895, "137": 1910, "138": 1925, "139": 1941, "140": 1953, "141": 1967, "142": 1981, "143": 1997, "144": 2009, "145": 2025, "146": 2047, "147": 2070, "148": 2085, "149": 2106, "150": 2121, "151": 2132, "152": 2149, "153": 2172, "154": 2185, "155": 2200, "156": 2214, "157": 2229, "158": 2245, "159": 2255, "160": 2268, "161": 2279, "162": 2293, "163": 2305, "164": 2319, "165": 2333, "166": 2348, "167": 2361, "168": 2369, "169": 2383, "170": 2395, "171": 2410, "172": 2421, "173": 2436, "174": 2452, "175": 2461, "176": 2474, "177": 2487, "178": 2497, "179": 2507, "180": 2520, "181": 2535, "182": 2546, "183": 2556, "184": 2566, "185": 2592}
---

**Dave Jones:** Hi, in a previous video, we looked at repairing this Back to the Future time circuit display from the the guys at uh Shack Space in Germany. They sent me this as part of my mailbag. So, click here somewhere if you haven't seen that

**Dave Jones:** video to watch uh repairing this. But, unfortunately, after the repair, yeah, we got back it powered up. We fixed our blown chip and everything, but we're still not getting any update on the display. So, we're going to crack out

**Dave Jones:** the scope, crack open the schematics, and uh take a look, see what's wrong with this thing. Let's go. Now, I have confirmed with uh Joki, he's one of the designers of this thing, and he said, "Yeah, this isn't normal. Something is

**Dave Jones:** wrong with it. I've programmed the code into here exactly the same as what uh he's got. He's uh double-checked that. It's okay. And I can talk to it via the serial port. I can update the real-time clock and everything. So, it should

**Dave Jones:** automatically um update the RTC on the display here. It shouldn't be like this." So, there's um this appears to be something wrong with the hardware. And if I power it up, you might see it change. The top one stays pretty consistent, but

**Dave Jones:** this Yeah, that second one there, you saw it. Even the green is a bit dim. Sorry about that. It's uh it's got more loss in the uh green uh diffuser there. It needs to be turned up a bit. So,

**Dave Jones:** there are slight differences there in the display every time you power it up. It's like a bunch of segments uh missing. But, more to the point, it's not updating anything on the display. It's just static, basically displaying all digits. So, yeah, something's wrong.

**Dave Jones:** So, we're going to get in there and probe the chip. The uh real-time uh this um shield on here, this is only a real-time clock. Uh basically, there's no extra circuitry on there. The uh uh multiplex and drive circuitry is on the

**Dave Jones:** back of the panel here. So, this is the chip we fixed uh in the last video, and uh it's identical. So, we can actually plug this cable into all three displays. We'll try that first. Now, what I've done is only plug the cable into the top

**Dave Jones:** display here. So, I've disconnected the other two boards, so they're not cascaded after that. So, we power it up and of course we get that display, but look what happens if I touch the back of that driver chip at

**Dave Jones:** the back here. Watch this. Ooh, look at that. All I did is put a little bit of force on that driver chip. And you might think, "Okay, maybe there's something wrong with my soldering or something like that perhaps." And that

**Dave Jones:** would be an obvious thing except for the fact that every time I re-power it, it goes back there. And if I touch the chip again, boom, I can make all the segments come on. So, when I physically touch the

**Dave Jones:** chip, so you might think, "Okay, that's a solder joint." But it's not because it resets itself every time. It's an electronic fault. It's not a mechanical fault in the solder joint of that chip. So, there's obviously some sort of

**Dave Jones:** capacitive coupling thing from my finger even though I was careful not to touch any of the pins, but as I approach, I'm sort of like putting in 50 h or the mains frequency here in the lab is being

**Dave Jones:** picked up by my body and then that is even though I'm not physically touching the circuits on the back, just the act of capacitively coupling, that I'll see if I can tilt that. That is enough. Ready? Here we go.

**Dave Jones:** Here we go. Oh, you can't see it. Sorry, but yeah, there we go. So, I didn't actually touch anything electrically, but I got very close physically to that multiplexer chip. And I got the cable now plugged into the green board here and now we're

**Dave Jones:** getting exactly the same thing, just all digits lit up. And if this thing worked, if there was something wrong with the display that with the chip that I resoldered, then we would see these other boards work. And once

**Dave Jones:** again, if I plug in the third board there, there we go. No, we're just getting all digits. So, the data is not getting there and updating that display. So, by seeing changes on this when I just lightly touch the top of that chip, getting

**Dave Jones:** close to capacitive coupling something in, that tells me that there's possibly some sort of floating line, broken connection perhaps, that you know, we're getting 50 hertz into a line, something like that, and the multiplexer chip is just going

**Dave Jones:** and it's getting noise into it and doing whatever. So, potentially there's something along that those lines. I don't know yet. We're going to have to get the schematic out and have a look, but anyway, that's a reasonable first

**Dave Jones:** assumption that maybe there's a broken line somewhere, and that would explain the lack of data getting from here over the ribbon cable into the boards, but hey, we won't know until we start probing. Okay, so let's take a look at

**Dave Jones:** the schematic here, which I'll link in down below. It's one of these modular type one, so it doesn't flow very well. It doesn't show you the system flow. We've got our input connector over here. We've got our output connector here.

**Dave Jones:** We've got our seven segments displays just with that net names. We've got the 74HC164 down here, and we've got the TLC Texas Instruments 59282 driver chip over here. So, it's a bit And and also we've got the high side driver MOSFETs as well for

**Dave Jones:** increased current handling capacity because you can't just sync all the current for all the displays through the HC164 multiplexer here. You can't do it. So, if we go over to the uh TLC 59282 driver chip, very nice little

**Dave Jones:** driver chip. It does all the multiplexing and everything else and the latching of the data and uh stuff like that, and also current control as well. Anyway, we'll see how this has been implemented here. Uh we've basically got

**Dave Jones:** our input connector over here, which is equivalent to this one over here. And we've got our lines coming in. You'll see our data coming in, our blanking line, our latch line, our S clock line. And these are the ones that are coming

**Dave Jones:** in here. Now, they're showing that with uh little joiner dots on there. It's not that. It's actually three. You can see that symbol. So, those uh lines, there's three lines, clock, latch, and blank are all just running in parallel over to its

**Dave Jones:** all subsequent chips here. And then all they do is daisy chain the data. So, data in here goes into uh data in of the first chip, and then out goes to the next chip, and so forth. But, we've only

**Dave Jones:** got one chip uh per board here, one of these chips. So, if we go back to the main schematic here, we can see that the data comes in on the input connector here, goes into the uh multiplexing chip here, the uh TLC chip,

**Dave Jones:** and then it goes data out. Here it goes, S data out, and that goes off to the next uh line display over here, to the second board, and the third board. Now, as you saw, all of our displays are

**Dave Jones:** actually uh showing all of the digits. So, they're all stuck on. So, that indicates that the multiplexing system is actually working. The data uh latch and things like that. Because it's uh it's most likely reading out the contents of the data from this, which is

**Dave Jones:** just It hasn't been set up. We haven't set up the data registers in there to display anything else. So, by default, power on, it's just displaying all segments. So, the multiplexer, 74HC164, is uh no doubt uh cycling through. Now, if we

**Dave Jones:** have a look at the system that's been implemented here, the main TLC uh driver chip is capable of uh 16 segment outputs, or 16 LEDs. We're you We're driving seven segment well, not seven segment display, we're driving these

**Dave Jones:** starburst displays. So, up to these starburst displays, they're using um all of the outputs from that chip. But, when you go over to say the seven segment displays over here, which a few of them are, they're only they're not using all

**Dave Jones:** of the output pins. Anyway, we need all those output pins. So, one of these um segments uh can take all of the data output. And then, we've got our common anode pin here, which of course, if we have a look, goes down to A1. And that's

**Dave Jones:** driven via our high side MOSFET drivers here, because uh you need those to get the uh high current requirements when all of the LEDs uh driven. And then, the gate of each of these driver transistors, of course, GA1 there, that

**Dave Jones:** is driven by uh effectively what is a multiplexer here, but they're actually using a 74HC164, which is a a um 8-bit serial shift register. So, overall, it's uh quite arrangement. We've got our data coming our serial data coming in, which is the

**Dave Jones:** actual segment data that we want displayed on the uh starburst or seven segment display. And then, that data is uh shifted into here based on the S clock. And then, once the data all 16 bits are in, bang, it hits the latch

**Dave Jones:** line like this. And then, that switches on and latches the data in uh straight to the outputs like this. But, at the same time, we've actually got a bit which then comes through on here. And effectively, we're shifting an

**Dave Jones:** individual bit along like this based on that uh latch line as well to turn on each FET in turn like that. So, you'll never have two of these on at once. You're only going to have uh one. So,

**Dave Jones:** it'll it'll switch on like a zero zero. And then, a zero will shift its way through turning on each FET in turn. And then, of course, when each FET turns on, that means each display turns on and reads the data out from here. So, it'll

**Dave Jones:** just shift across in this fashion displaying the data for each one of those in turn. And we can might be able to see that actually if I set the frame rate of the camera to the right setting. Let's see if we can do that. Well, what

**Dave Jones:** do you know? I can't make that top display come and go anymore by touching it. So, yeah, I don't know what's don't know what's changed. That's weird. Oh, there we go. No, hey, something changed. There we go. Anyway, if I put

**Dave Jones:** the camera in the shutter priority mode, I've currently got a setting of 1/25th of a second. And as you can see, you shouldn't you might be able to see a little bit of flicker on the display. Anyway, let me increase and that value

**Dave Jones:** or decrease it to get a shorter shutter time. Okay, so that's 1/250th of a second shutter speed. And you can really start to see the flicker on the display now. And there we go. That's the fastest shutter speed I can get,

**Dave Jones:** 1/2000th of a second. And you can really start to see the digits actually scanning across like that. You can really see it. And because it's a very fast shutter speed, you can probably see the noise in the image.

**Dave Jones:** It's darker and a lot noisier. There's just not as much light getting to the sensor. Now, there's a lot of people that might automatically say, "Aha, this is a digital thing timing. I need a logic analyzer." Well, no. I for

**Dave Jones:** something like this, because I know it's a proven system or it should be and the software should be working. We're actually debugging a hardware fault here. And this is where you need your scope and not the analyzer cuz we could

**Dave Jones:** have a broken line, a shorted line, floating, all that sort of jazz. You don't want to be mucking around with a logic analyzer like that. Only when you're dealing with protocols and things like that would you want a logic

**Dave Jones:** analyzer. So, we're just going to use a regular scope and take a probe around. See what we can find. And also, even though I've got a four-channel scope here, I wouldn't jump straight into actually hooking up all four probes and

**Dave Jones:** hooking them up to all the lines. It's just, you know, it it's just a waste of effort, really. Just a simple probe route with one probe first just to see if signals are getting there is more than enough. And when you're probing a

**Dave Jones:** ground point like this, um to use one of these uh alligator crocodile clips and try and clip it into uh one of these uh pin headers here, no, it's going to fail. You're just going to short them out, no good. So, make sure you just get

**Dave Jones:** one of these uh headers like that and uh Bob's your uncle, no problems whatsoever. Or, in this case, I would probably go to the effort to uh solder on a little uh pin which jumps up from the uh ground plane here. And yeah,

**Dave Jones:** we're not too concerned about signal integrity at the moment, so the length of this ground lead uh doesn't matter much at this stage. We're just looking for signal, is it there or not? Now, if we had to get in there and actually

**Dave Jones:** probe this little 0.6 uh 35-mm pin pitch SSOP package, that would be a pain in the ass, but thankfully this system allows us to break almost everything out onto uh these header pins here except the serial data in here, but we can

**Dave Jones:** check the clock and the latch and everything else. Okay, so let's start out with pin one here, which is the uh call O line. I assume it's uh column. And bingo, we're getting we're getting some data there, so that's

**Dave Jones:** fine. It's not uh shorted, and of course all these little uh uh transitions in here, they're coming from the clock line. So, if we actually uh had the clock line in parallel with this, you would see that the clock would

**Dave Jones:** be transitioning every period like that, and that's why we're getting those uh glitches caused by um coupling, ground bounce, all the other all the usual uh signal integrity crap because we're not probing that well, so but that's all we

**Dave Jones:** want to see is that there's a signal there and it is the correct signal level. It's 1 V per division. We're getting our 5 V logic, no problems at all coming from the Arduino board. So, that's all right. So,

**Dave Jones:** let's go into pin two, which is the Sorry, pin three, which is the latch line. And well, the latch line is short. It's a much shorter pulse, but there it is. So, our latch line is there. No dramas.

**Dave Jones:** So, it's not shorted. It's getting onto the board. In fact, it's not only getting onto the board, but it's going to the output connector. So, not a problem. Okay, now our blanking line. Yep, we're getting ourselves a blanking

**Dave Jones:** pulse as well. No problems at all. Looking good so far. Okay, the next pin, pin seven, is the serial data out. So, let's have a look at that. And that the serial data coming out of that chip will

**Dave Jones:** tell us whether or not we're getting data in. And nope, even last time base setting we're getting no data coming out. So, that poss- That's just the contact bounce on the pin there with my probe. So, that tells us that we're getting no

**Dave Jones:** data. Um possibly no data into the uh chip in into the Texas Instruments TLC display driver chip cuz there's nothing coming out. Now, that could be because the Arduino is not sending any information. It could be a software

**Dave Jones:** issue. We don't 100% haven't ruled that out yet, but we're not getting any data out. So, there you go, and it's supposed to be I have supposedly programmed the board to output the real-time clock information. So, we're getting nothing

**Dave Jones:** there. Okay, that would explain why we're getting all the digits turned on. Okay, now for the clock line, which I'm pretty darn sure we're getting based on the other uh stuff we were Yeah, there we go. There's our clock line, and we could see the We

**Dave Jones:** knew that clock line was there because we were getting the transitions in coupled over to our other signals. So, there you go. It's all there. Looks like we have a data issue. Now, we could actually probe the serial data

**Dave Jones:** input pin here, but as I said, you risk shorting out those pins and you could actually ruin your Arduino, ruin your board, or anything like that. But, as it turns out, well, we could like put an extender on here as well. You can

**Dave Jones:** actually solder up a little female to male adapter so you can get in there and like extend that out. And so you can get in there and probe each pin. But, as it turns out, our the other end of the

**Dave Jones:** cable already has another connector on here. So, we can just whack some pins in there and then just probe them. Easy. Signal integrity is going to be pretty awful, as I said, but hey, we're just looking for signal. All

**Dave Jones:** right, so here we go. I'm going to probe these again. This is coming directly out of the Arduino board, and there's the first line, which is the colo line, and then we've got our latch signal, and then we've got our blanking signal. We

**Dave Jones:** know all those are correct. Now, here it is. Here's the data. Aha! Look at that. And we have got very significantly changing data there. And if we, you know, if we got in there and actually had a good look, but we are

**Dave Jones:** getting data coming out of the Arduino board. So, bingo. But, there's nothing coming out of our second chip. So, effectively, what we've got here is all of our signals are coming in fine. We've measured all of those, and our data is

**Dave Jones:** at least coming from the controller here. We haven't actually probed at the first chip itself, and it's almost as if, well, it's not getting to that chip. So, because otherwise, all the signals should be there. Should be working. So,

**Dave Jones:** unless I've actually missed a solder joint on there or something that's not making correct contact, could be. Could be a hardware fault, but the Arduino is certainly outputting some data, which we should see on the display. So, yeah, now

**Dave Jones:** we have to try and get close to this chip, see if it's coming out, because we measured this We we had a second connector over here. It wasn't a second chip. Well, there was on the second board. So, we had a

**Dave Jones:** connector in here, and we saw that there was no data coming out from this serial output here. So, it's either not getting to this chip, or the chip is not outputting it for some reason. And I don't see why the chip wouldn't output

**Dave Jones:** it if it's getting in and it's getting all the clock and the latch and everything else. It should work. Okay, I'm going to probe the pin. Now, I've got to be very careful and watch the chip here instead of watching the

**Dave Jones:** display. So, I know you can't see me do this, but I'm probing pin two, which is the data pin. Yep, it's there.

**Dave Jones:** It's there. All right, so we're getting data going into that TLC chip, but nothing coming out. Okay, I'm going to probe the output pin directly, which is pin 22. So, I'm going to concentrate.

**Dave Jones:** No. Nothing. Just high, as we saw on that uh pin header. Now, I'm going back to the data line for a second there, and uh we're back on the uh ribbon cable itself. And if we just single shot

**Dave Jones:** capture that, um we can see that the data is really changing all the time, as you'd expect um when this thing is updating the uh the clock. So, um yeah, I I don't know. Data's getting into the chip.

**Dave Jones:** Our clock pulse is getting in. We're Well, we're fairly sure. I haven't checked all the pins directly on the chip. So, that's probably the next uh bit. Are Is all that data getting to that chip? But, that's the thing. If it was a

**Dave Jones:** problem with my rework chip here, then I've already tried, as I showed before, plugging this cable directly in to these other two boards, which are known working boards, or they were um when they were given to me. And I don't think

**Dave Jones:** I've blown them cuz they all seem to work um identically. The multiplexer chip works. We wouldn't get all that stuff on the display if we didn't. Um yeah, even though it's just all uh basically all segments turn on. So,

**Dave Jones:** really, you know, that data he's getting across, it's getting there. I'm absolutely confident the data is getting to that chip. But, uh I'll check it anyway. And now we'll just have a squeeze at the uh 74HC164. As I said, see if we've got a zero on

**Dave Jones:** the gate of these uh high-side MOSFETs here actually traveling across like this. We won't be able to see it uh traveling across each one cuz we've got no timing correlation. We've only got a single uh probe and a single trigger

**Dave Jones:** point. But, anyway, let's have a look. Pin three is one of them. And yep, bingo, we've got a zero in there. And if we go to the next one, yeah, we see exactly the same. But, if we actually probed Yep. If we

**Dave Jones:** actually probed all of those, we would uh like at once and uh triggered off one of them, then we would actually see a uh staggered We would actually see each one staggered in time like that. So, that's just multiplexing each

**Dave Jones:** particular digit. But, of course, I totally expected all of that to work because if it didn't, well, we wouldn't get anything on the display. We'd get one stuck digit or something like that. So, really, it all comes down to um

**Dave Jones:** this driver chip. We know we've got data probe coming in. I've probed that. I have probed the other pins directly on the chip, and we're getting the data going in. Our I reference pin is all fine, and we're getting um it seem Well,

**Dave Jones:** we're getting no serial data out of the thing and it seems like uh we're just getting basically all highs on the output here. So, it's not latching any data, yet we know different data is being shifted into this thing.

**Dave Jones:** So, unless we get deep into the protocol, it's Jeez, it it looks fine on the hardware side, exactly what we expect. Well, I was just about to get all medieval on its ass. Hooked up the logic analyzer, got out the

**Dave Jones:** 3000 series scope, got printed out my timing diagrams and everything, but I thought, "No, look, there's all that data seem to be getting to the chip." And I've I've I've hooked it up and I verified, well, the data's

**Dave Jones:** coming out of the Arduino here, no problems whatsoever. So, I thought, "Why isn't it doing anything?" I'm assuming that the software is correct, which Jockey has assured me that it is. It works on his and this unit was tested before we sent

**Dave Jones:** it out. I thought I would have another probe again to see if the chip signals are making the chip. And I said before that I had actually checked that and it was the case, but Aha! It just didn't

**Dave Jones:** make sense if we were getting all of these clocks and data and everything else coming in here and getting no serial data out of here. It just didn't make sense. So, it's almost as if the clock pin wasn't actually getting right

**Dave Jones:** to the chip itself. And I thought I had tested that, but I double-checked it and sure enough what? File. It's a soldering issue on my chip. I looked really closely under my Mantis 3D microscope at a really deep angle. Sorry, I'm not

**Dave Jones:** going to be able to get a good shot at it and it turns out that the um clock pin, pin three on the chip that I reworked, just wasn't quite making it and I was actually probing the the pin. I was actually the pad. I was

**Dave Jones:** probing the pad and there there was a minute little gap between the pad and the pin itself. So, the signal is there if you probe the pad, but it's not there if you actually probe the very top of

**Dave Jones:** the pin. Now, I'm not sure if you'll be able to see this precisely, but pin three there is the clock pin. And this is my scope probe and when I was probing the bottom of that like that, you know, of course, if you're

**Dave Jones:** probing that pad, there's some pad extending out there for the pin, no problems whatsoever. And if you of course and if you're probing down on the pin like that, then that's enough to put force on it and make contact, but as you

**Dave Jones:** can see there's just not enough solder under there. I just missed it. And if you probe up here like this and lightly touch it and not put any extra force on it, then I'm not getting the signal. So,

**Dave Jones:** the clock signal is making its way through to the pad and but it's not actually getting into the chip. Bingo. So, what? That's a fail on my part. I was a bit hasty in my visual inspection of that thing and yep, that's a PEBCAK.

**Dave Jones:** But the interesting part of this that led me up the garden path to think that that chip was fine, there's nothing wrong with it, is that I disconnected this ribbon cable over here and plugged the cable directly into these other two

**Dave Jones:** boards, which I was pretty sure were not uh blowing. They didn't uh get hot. I thought it was only this top board here. So, I've totally disconnected my rework board and if I power that up if I power that up, of course

**Dave Jones:** power that up, of course, um you know, we just get the same results. So, that data's not going through. So, that's what led me into a a false sense of security that that chip I had soldered was just fine and because I briefly

**Dave Jones:** probed the pin and I saw a signal, yeah, everything's hunky-dory, it's getting the clock and everything. But when I went back to just think about it for a second, I thought, this got like it almost has to be that clock. And sure

**Dave Jones:** enough, I went back and looked at it, and yep, we've got a dodgy joint on this. I'm just going to reflow that, but it doesn't explain why these other two boards aren't working either. Um so, what are these ones blowing too? And uh

**Dave Jones:** the chip There's a different failure mode in these chips, and I have to replace those, too. Could very well be. All right, so I've resoldered that pin. It should be good now. Haven't actually checked the signal on there, but it

**Dave Jones:** really looks good under the uh Mantis microscope. I've disconnected the second board, so the second and third boards aren't connected. So, we will flip this up, and let's power up this puppy and see if it does anything. Woohoo! Winner, winner, chicken dinner.

**Dave Jones:** Look at that. We have two other failed boards with failed chips. They just Ah, man, unbelievable. Classic case of being led up the garden path by multiple things. And there's probably people at home just, you know, screaming at me

**Dave Jones:** that this was just bleedingly obvious, right? And um yeah, I'm just an idiot for not um not finding it sooner. But there's That's the thing. When you're involved in this sort of thing, you see these um you know, these things you just miss

**Dave Jones:** these things, and you get led up the garden path by various clues, and uh red herrings at every corner, and there you go. That's what it was. Looks like we are most likely have two other failed uh TLC chips on these two as

**Dave Jones:** well, but those ones didn't get uh red hot and and blow the smoke out like the first one. So, I just assumed that they survived. And because this one was giving out the same uh display as the other two, it was

**Dave Jones:** unbelievable. There you go. Oh. So, yeah, with hindsight, that was bloody obvious. And it did finally twig to me that, you know, it like a brand new chip I sold it on, the data was getting in there, but nothing was coming

**Dave Jones:** out. It's got to be the clock. And sure enough, it damn well was. So, I can't imagine how much time I would have wasted when I started diving into the protocol here. I would have found that, of course, it was perfectly fine. And I

**Dave Jones:** was, you know, I I was trusting Jockey, and it sure enough, he was right. There's nothing wrong with the software at all. It was working fine. So, it had to be a hardware fault like that. So, there you go. But, I thought, you know,

**Dave Jones:** oh, maybe it's a signal integrity problem cuz he talked about he put some termination resistors on the board, for example, and but didn't populate them on these ones. And well, you know, that could potentially be like a signal

**Dave Jones:** integrity issue and stuff like that. So, imagine if I went through and started looking at all the timing diagrams here and all the protocol and everything else, and then finding no problem there, and then going on, you know, thinking

**Dave Jones:** confidently that I've already probed the chip in there, and everything and the hardware must be right. That and, you know, then I go, well, it's a signal integrity issue then. Imagine the hours I would have wasted trying to actually

**Dave Jones:** probe properly cuz if you want proper signal integrity, you can't just use an antenna earthly like this. You've got to go in there and set up these things properly. And well, yeah. Man, could have wasted forever. It's lucky I just, you know,

**Dave Jones:** stepped back and went, "I'm going to double-triple check that clock pin." And sure enough, bloody well was. So, I'm going to replace these two puppies here on these other channels. And yes, I did order enough because well, they cost what? 50 cents or a

**Dave Jones:** dollar each or something. And if you're going to order these parts, you know, I got these from Digikey in the US cuz they're not available locally. I think I got them from there. Or no, Mouser, I think. Anyway, so like it's

**Dave Jones:** not like I just ordered them. So I'm, you know, want to make it worth my postage and all that sort of stuff. So you, you know, you throw on like five of them or something. If you don't use them

**Dave Jones:** all, well, whack them in your parts bin. No worries whatsoever. So I'm going to replace those and a few people commented on the previous video and I meant to mention this another technique for getting these chips out. And I'm sure

**Dave Jones:** I've mentioned it in a video before is you can on like these SO type chips, you can actually get in there and cut out the individual pins and then lift it off and then get your solder wick and your

**Dave Jones:** soldering iron and just, you know, easily remove the pins that are remaining. Or you can get an X-ACTO knife and go in there and carefully cut down the pins like that. But I don't It's It's okay, but it's a bit

**Dave Jones:** medieval. I mean, you can really if you put the wrong pressure on it, you can end the wrong angle or whatever, then you can easily rip the pads and do other stuff. So it's, you know, it works, but

**Dave Jones:** you just got to be careful. And somebody noted this on the comments and I thought I got an inkling this was the case too, but I thought oh, I was just going wonky. Look at the pin pitch of this footprint is slightly out. Look,

**Dave Jones:** this pin is like smack in the center there and when you look, it looks like the errors accumulate as you go further down. So this is a 0.6 mm pin pitch. So it looks like the pin pitch of the footprint used in this

**Dave Jones:** thing is just slightly out of kilter. And if you had a really big chip, it would really add up and cause a problem. So there's something wrong with that footprint there. That's hilarious. So forgive me for recording this through my

**Dave Jones:** uh LCD screen here, but uh it's just easier. Now, the interesting thing to note is that nobody in the comments picked up or not that I've read anyway, picked up that I had a dodgy solder joint. They didn't pick it up

**Dave Jones:** at all. It just goes to show the benefit of a uh you know, like I can tilt it like that and maybe it'll Yeah, it'll refocus things like that. You can get at an angle down in there. It's going to be

**Dave Jones:** nice if I you inspect this uh you've uh cleaned it up, of course, but uh yeah, nobody uh nobody spotted that. Now, I didn't spot it on my first go under either the Takagi microscope while I was doing it or the uh Mantis, but yeah, I

**Dave Jones:** should have looked better. I was pretty hasty. I was shooting a video, just trying to get the thing done and yeah, it comes back to bite you. So, quite a lot of people do ask which is better, a 3D microscope, a stereo or you

**Dave Jones:** know, a stereoscopic uh microscope, doesn't have to be a Mantis, or whether or not uh a one of these like, you know, either it's a cheap USB webcam, you know, USB microscope or whatever, is uh better or even a high-end one like this Takagi.

**Dave Jones:** Well, you simply cannot beat a proper stereo microscope. Cannot be beat. But, these ones are obviously useful. You can get them like on a big huge screen here and you know, you don't have to be sort of, you know, hunched

**Dave Jones:** over the uh microscope to see it, but uh yeah, for real proper inspection, you can't beat one of those puppies. Just absolutely, you know, I The only issue with these is that uh you know, you have to get

**Dave Jones:** your eyes There's only a small little window where you have to get your eyes so that you can actually see it. Otherwise, it totally shifts out of um you know, out of field. You can't actually see it, but yeah, these things

**Dave Jones:** because you can actually move your head just side to side a little bit and the angle sort of tilts. It's a bit 3D. Um that's the advantage of this um high-end expensive Mantis one, as opposed to one of the, you know, the regular uh stereo

**Dave Jones:** ones, which I've shown in previous videos. And you can get really quite tired, actually, uh soldering through these things. I mean, this Mantis, I've um soldered on this like, you know, 10 12 hours straight, and you don't get

**Dave Jones:** tired. And the reason for that is because your distant, your uh your lenticular distance, I believe it's called, is the same when you look through here down. So, it's the same uh visual path length as when you focus

**Dave Jones:** down. So, if you look through here and then gaze down here, your eyes don't have to refocus. They don't have to continually refocus between here and here. And so, that's why you can work under these Mantis ones all day long.

**Dave Jones:** But, of course, you know, the uh USB um uh ones or ones like this uh Takane here, they're, you know, great. I mean, I've got that on a huge, you know, um 22-in monitor there, and it's, you know, it's just fantastic. But, you

**Dave Jones:** know, not as good as a proper stereo microscope for actual inspection. So, I'll just finish this off. I've put my flux pen on there, and uh we're almost ready to go with our three our three chips. Yeah, that's the only disadvantage with

**Dave Jones:** this Takane, cuz it's a long arm. If I don't If you don't have a really steady bench, then uh yeah, it's not that great. Can bounce The image can bounce around, so there you go. That's good enough. Well, really, I should uh power this

**Dave Jones:** thing up uh one board at a time, but I'm going to go for broke. Here we go. Woohoo! Uh bottom one. What's wrong with the bottom one? The green one's just on. You probably can't see that. It's very dim, but it's

**Dave Jones:** there. And the bottom one's doing something weird. Hmm. Oh, no, it's there. Sorry, it's just uh very dim that you can't actually see it. So, oops. Okay, let's try that again. And uh Hack Space. Look at that. Nice.

**Dave Jones:** Well, why would you uh Shack Space? There you go. They've got their address in there. Well, why would Shack Space? Yep. Nice on the third display. Very nice. And there you go. Um I've got them almost turned up to maximum there. So,

**Dave Jones:** the green one is quite dim, and the uh yellow one down here was just fine. It's just that it was so dim that it just looked like they were sort of like all on. So, yep. Winner, winner, chicken

**Dave Jones:** dinner. Fixed. Now, the only issue with running these at uh maximum brightness is these suckers get hot. How hot? Well, let's find out. Look at that. They get very, very hot. 70 up into the 80s. Look at that.

**Dave Jones:** So, yeah, 85 I saw there. So, 88. So, yeah, that's um for the green. So, Now, sorry about the glare of the lights there, but yeah, 85. Certainly worth uh putting on a uh little heat sink onto those suckers. Getting one of those uh

**Dave Jones:** stick-on, glue-on uh heat sinks with some uh thermal adhesive on there. Well worth the effort. There's a and kind of enough room on there. Just be careful you don't short out to the pins next to it. Well worth it if uh well, I I plan

**Dave Jones:** to run this thing uh 24/7 um in front of my live uh webcam here in the lab. If you haven't seen it, eevblog.com/live. Yes, you can watch me work or not work. Um pretty much mostly not work um here

**Dave Jones:** in the lab live 24/7. Fantastic. So, uh yeah, I'm going to put that up there so, I don't know, people have something to watch. There you go. But, that's fixed. So, what did we end up actually learning from this uh video? Yes, I left

**Dave Jones:** everything in warts I didn't uh leave anything out. Well, uh what did we have? We had uh the fact that I only had one visual indication um like when I blew this thing up, the smoke and everything else uh from this

**Dave Jones:** one channel here um that didn't work. So, I thought I okay, I've only blown the one channel. And so, we went in there, we fixed it, we repaired it, and then all the displays we're getting exactly the same thing. So, I thought if

**Dave Jones:** they're all getting exactly the same thing, foolish me, I should have thought about it a bit more. I could have twigged to the fault uh then and there, but I thought, "Hey, if they're all getting the same thing, I don't know.

**Dave Jones:** It's more likely to be like a firmware uh you know, issue or you know, there's some sort you know, I'm not programming the Arduino right, something simple like that cuz it was probably more more likely than not that I only blew say one

**Dave Jones:** channel or something like that. And I couldn't remember even if I had all three plugged in at the same time when I blew it. I don't know. I can't recall, but anyway, so that was the first thing, there was only one visual indication of

**Dave Jones:** a blown fault. So, that was um issue number one. Then of course, we replaced the damn chip in this channel, and we didn't inspect it correctly. It looked good under the 2D microscope, and a brief look under the 3D microscope it

**Dave Jones:** looked good, but I didn't give it as good a visual inspection as I should have. So, it was slightly lifted off the pad, and it was looking like it was looking like it was connected, but it wasn't. So, when I probed it, the extra

**Dave Jones:** force of the probe coming down on that pin made me think that there was a signal there. And hey, you've checked all of the signals going to the pins, and then you get led up the garden path. That was a complete red herring there

**Dave Jones:** that you know, led me to think that it was more of a firmware issue. And then I plugged it into the same board, I was getting same information. And so, we went down the path of actually checking, systematically checking all the pins and

**Dave Jones:** everything else. And it was looking like I was about to launch into this protocol decoding thing when I took a step back and went, "Hey, you know, I I sort of trusted the original designer of this thing and really, you know,

**Dave Jones:** it seemed to be something else. It was still niggling at me, and I didn't go off willy-nilly. I could have spent all day, you know, mucking around checking these protocols and timing everything. That was going to be the intention of this video. I came

**Dave Jones:** back today and I went, "Well, okay, you know, look, I'll I'll hook it up." And I went to the trouble to get my scope out. I hooked up my probes and everything down here, and I was ready to go into

**Dave Jones:** that and maybe some signal integrity stuff if I got that far. Oh, what's it saying there? There you go, Shack Space. Mate, I I might leave that in there. Got to advertise the guys. So, all those different things add up to lead you down

**Dave Jones:** the garden path to think that you've A, checked it, and B, it can't possibly be that. But hey, you know, when you always go back to the fundamentals, if all the signals were getting into that chip, we should have been getting something

**Dave Jones:** different out of these displays. At random, garbage, whatever, we should have been getting something. We knew we were getting we measured like you know, information going into these with the display information. The data was going in there, changing data was happening. And

**Dave Jones:** if it was getting the clock, it should have been outputting something. We checked the multiplexer uh down in here with the shift register that was driving all that. That was all working. We were shifting through our displays, otherwise

**Dave Jones:** we would would have got all this. And well, in the end, it was pretty obvious it had to be that that thing wasn't getting a clock. And sure enough, it bloody well was. Unbelievable. Murphy'll get you every time. So, lessons learned there. Pays to

**Dave Jones:** double-check, even triple-check things to make sure they're right. And then not just go jumping into measuring stuff willy-nilly without um you know, thinking what could actually be what must be causing this problem. Once I thought about it, you know, it must be

**Dave Jones:** the clock. And I I got lucky. It might not have been. It might have been something other weird of screw-up. Could have still been the protocol or the signal integrity or something like that. Would have been much harder to find

**Dave Jones:** that. And that's what I thought this video would end up being. It's already been going like 40 minutes or something in this video. Crikey. Sorry about that. But anyway, this is my basically real-time investigation. You followed me through of me debugging this thing. And

**Dave Jones:** yeah, it has taken me this amount of time to get this far. So, that's just the real world. That's how long these things take. And somebody else doing this or me on a different day with more luck might have, you know, it just

**Dave Jones:** lucked upon this thing first go. Or maybe if I had my thinking cap on a bit better or more systematically analyze it. Too busy, you know, shooting a video, trying to get the thing up and running, and stuff like that. So, you

**Dave Jones:** know, often it's it's just a matter of luck of what you probably if I maybe put if I didn't put enough pressure on that probe to begin with, I would have found it yesterday, and I would have went,

**Dave Jones:** "Aha!" Or the other day would have went, "Aha! That's, you know, that's obvious. There's no clock getting to that pin." And well, no, I applied a bit extra pressure, and sure enough, bang, it made contact. So, I ignored that, went on to

**Dave Jones:** something else, tick, verified, and Bob's your uncle. So, there you go. I hope you enjoyed that lengthy little real-time troubleshooting getting this thing working. And it was a complete PEBCAK on my part. Sorry about that, but I hope you actually learn something.

**Dave Jones:** These things are always interesting when you go through them and troubleshoot, and very satisfying when you finally fix the bastard. There you go. Look at that. It's a bobby-dazzler. It works. Now, I've got to program it and have some

**Dave Jones:** fun. So, if you want to discuss it, jump on over to the EEVblog forum. Links are down below. And as always, if you like it, give it a big thumbs up on YouTube. Sorry, you can't really give it a thumbs

**Dave Jones:** up anywhere else. It's got to actually be on YouTube. So, if you're watching through somewhere else, you can't do the thumbs up thing. Some people have actually asked, "Where do I do the thumbs up thing?" And anyway, if you want to check out

**Dave Jones:** this, go on to hackspace.de, I believe it is. Also, linked down below. Catch you next time. Great Scott! Whoa, this is heavy.

**Dave Jones:** Ah! What did I tell you? 88 miles per hour!
