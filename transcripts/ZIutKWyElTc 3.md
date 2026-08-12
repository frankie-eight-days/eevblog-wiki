---
video_id: ZIutKWyElTc
title: EEVblog 1515 - Dumpster Tektronix TDS540D 500MHz Oscilloscope LCD Upgrade
url: https://www.youtube.com/watch?v=ZIutKWyElTc
source: youtube-asr
timestamps: {"0": 0, "1": 7, "2": 28, "3": 42, "4": 59, "5": 74, "6": 87, "7": 102, "8": 117, "9": 133, "10": 144, "11": 158, "12": 168, "13": 175, "14": 195, "15": 206, "16": 216, "17": 226, "18": 239, "19": 250, "20": 260, "21": 268, "22": 280, "23": 292, "24": 304, "25": 313, "26": 333, "27": 340, "28": 347, "29": 358, "30": 371, "31": 378, "32": 394, "33": 409, "34": 420, "35": 445, "36": 458, "37": 467, "38": 480, "39": 490, "40": 497, "41": 507, "42": 518, "43": 528, "44": 538, "45": 548, "46": 557, "47": 564, "48": 576, "49": 587, "50": 594, "51": 605, "52": 623, "53": 633, "54": 645, "55": 653, "56": 665, "57": 677, "58": 686, "59": 703, "60": 713, "61": 730, "62": 743, "63": 750, "64": 762, "65": 782, "66": 788, "67": 799, "68": 807, "69": 822, "70": 831, "71": 843, "72": 854, "73": 871, "74": 877, "75": 887, "76": 900, "77": 915, "78": 924, "79": 944, "80": 955, "81": 967, "82": 978, "83": 990, "84": 999, "85": 1008, "86": 1020, "87": 1034, "88": 1051, "89": 1065, "90": 1084, "91": 1096, "92": 1106, "93": 1123, "94": 1138, "95": 1150, "96": 1162, "97": 1171, "98": 1181, "99": 1193, "100": 1205, "101": 1220, "102": 1232, "103": 1248, "104": 1264, "105": 1286, "106": 1307, "107": 1325, "108": 1339, "109": 1354, "110": 1370, "111": 1378, "112": 1389, "113": 1409, "114": 1419, "115": 1430, "116": 1445, "117": 1456, "118": 1466, "119": 1474, "120": 1484, "121": 1493, "122": 1500, "123": 1511, "124": 1526, "125": 1538, "126": 1552, "127": 1560, "128": 1568, "129": 1578, "130": 1587, "131": 1598, "132": 1607, "133": 1615, "134": 1628, "135": 1639, "136": 1649, "137": 1658, "138": 1670, "139": 1678}
---

**Dave Jones:** Hi, you might remember this dumpster find from a video quite it was probably a few years ago now. Anyway, I'll link it up here and down below if you haven't seen it.

**Dave Jones:** It's a Tektronix TDS 540D and it's a four-channel 500 megahertz jobby and it actually works but the CRT in it didn't work but the I was able to get it working from the VGA output on the back and it seemed to work just fine.

**Dave Jones:** It's missing a couple of knobs but these TDS series scopes they do have a reputation for having problems over the years but they're still incredibly powerful scopes. It doesn't have a huge amount of memory I think it's only like 32K or something.

**Dave Jones:** Four-channel 500 megahertz I think two gig sample per second. You know, it's a pretty still a pretty beastly scope. So I thought that instead of repairing the CRT that I'd do an LCD replacement for it and this is actually quite a common thing a lot of people do a CRT replacement for this thing.

**Dave Jones:** So that's what I've got now but I'm having a bit of issue with it. Show you what's actually going on here and see if we can solve it. Anyway, during my live show the other week I did actually get this out of the bunker.

**Dave Jones:** It's been there in parts and I reassembled it and when I first turned it on I encountered a bizarre fault. It didn't work and I'll insert the clip here and it was just amazing what the culprit actually was.

**Dave Jones:** Flowchart. Diagnostic flowchart primary troubleshooting procedure. Press on the principal power switch. Can you hear the fan whirring? No, cuz I've disconnected it. 622 refers to the flashing code eight in the right center of the flowchart.

**Dave Jones:** Oh, thank you. Primary troubleshooting procedure. Really don't miss it. Does DS1 first flash dot eight then display a sequence of hex numbers? No. Does DS1 flash eight then display the sequence of hex numbers pausing to the flash.c.

**Dave Jones:** No, no. Replace the A11D RAM processor display module. Obviously, displaying the eight is the first thing it does and then it just resets and keeps flashing eight. Eight. So, it's clearly not being allowed to go through its sequence.

**Dave Jones:** It's like change the entire processor board because you get a flashy eight. No. No, no, no. I'll I'll plug the fan in just for that authentic fan noise. I don't think it's detecting the fan.

**Dave Jones:** It's only a two-wire jobby, but you could detect that. Who knows? That'd be embarrassing if it was. Hey, no. It's now working. It was the fan. Really? Wow. Yeah, it's flashing.

**Dave Jones:** It went through a cycle. All all the leads are on. It's now flashing top, bottom, top, bottom, top, bottom segment. It boots. May I don't know. Is the Dallas SRAM in this thing going?

**Dave Jones:** Let's try and prove that. I'm going to disconnect the fan. The only thing I'm going to do is disconnect the fan. I'm going to turn it back on. I think it'll work.

**Dave Jones:** I reckon there's something else afoot. No, it detects the fan. There you go. It detects the fan. Wow, I would not have guessed that. It is It must have some circuitry to detect that the fan is connected cuz it's not like a it the fan's only a two-wire jobby.

**Dave Jones:** That That made a fool out of me. I would not have guessed that. Who else would have guessed? Be honest. That it was detecting the fan and that was causing it to cycle boot.

**Dave Jones:** Although, the fan does plug into the processor board. There's a bit of a bit of a bit of a giveaway. It plugs in the processor board, not in the power supply board.

**Dave Jones:** So, there you have it. It was the fan on this thing, which is this giant jobby over here. And as you can see, like it's it's only a two-pin physical connection on there.

**Dave Jones:** So, they must be doing some sort of like load detection to, you know, determine that there there's a load on the fan. So, if I boot it up without the fan here, and you can see it just flashes the eight and the front panel just flashes off and on.

**Dave Jones:** It's like it's like it the power supply's hiccuping. It's doing something like that. So, yeah, it's really weird. And I don't think this is actually covered in the manual at all.

**Dave Jones:** Actually, I haven't tried this. Can I just plug the fan in? Will it Yeah, look. It just As soon as I plug the fan in, it goes. Don't know if the four is correct.

**Dave Jones:** It hasn't fully booted yet. Like that when it's good. Nah, I'll just turn it off. So, we'll just boot that up. There we go. It's gone through its power on.

**Dave Jones:** Yep. And then it'll eventually reach a point where it will shoot just toggle Yeah, toggle up and down like that and it's working. Now, of course, this uses some Dallas non-volatile memory.

**Dave Jones:** And what's the date code on those? '99. So, they're 22 years old. So, yeah, that's a bit of a problem. But anyway, it still seems to work. I'm not sure if they hold calibration data or whatnot.

**Dave Jones:** You can see there's some missing memory here. This is actually for the color option. I did actually buy some memory. This is way back when I was in the old that big rented lab that I had and I was looking at doing this.

**Dave Jones:** I did actually buy the memory and I've got it somewhere, but it's you know, hidden away in a box somewhere in the bunker. So, yeah, I'm not going to bother with the color upgrade until I find that.

**Dave Jones:** I just want to get the LCD working. So, what I've got is this LCD here. I'll put up the data. Here it is. A generic type, but apparently this is the one that fits the TDS or at least that's the info I found on the web interwebs somewhere and yeah, it just came with one of these boards which has a VGA interface.

**Dave Jones:** You buy the LCD on its own, but or you can buy it with a board. And unfortunately, I'm getting a bit of problem. So, let me power it up.

**Dave Jones:** So, check it out. Don't know if you're seeing that, but I've only got one waveform there, but there's more than one because it's got multiple colors. Have a look at the font down here.

**Dave Jones:** If you can see that it's got the different colors there and they're on like alternate lines or something. There's some sort of like interlacing type problem or something like that.

**Dave Jones:** There's something going on there, but it does work. Interestingly, if I turn on the menu system, it does it with the menu as well. Auto config, that's not going to fix it.

**Dave Jones:** So, oh, there we go. Now, it just moved it up to the top there. The text is fine, but it's I'm doing some sort of weird decoding of that.

**Dave Jones:** And now, given that it's got different colors and this is only a mono output, uh first of all, and then I will uh disconnect, I think, um two of the color lines and see like if we just get the one color and it's it's fine.

**Dave Jones:** I don't know. I've got a slightly more modern scope. My MDO 3000 has a VGA output and that looks fantastic. There it is. So, it's something particular with this uh TDS 540.

**Dave Jones:** Yes, if you're wondering what that uh display is there, that's a uh safe operating area uh display. I've been playing around with that. I might maybe want to see a video on safe operating area, anyone?

**Dave Jones:** Viewer? And I've got another LCD here, but it's the wrong form factor. I'm not sure where this one actually uh came from. It works just fine and dandy. So, there's something with this board that's um in particular with the signal from this uh TDS 540, and but this board um I don't know, JST pin or something um works just fine.

**Dave Jones:** So, yeah, look, it's beautiful. But, it's the wrong form factor and no, the um LCD cables aren't compatible, I don't think. What we want to do is disconnect combination of the colors.

**Dave Jones:** So, if I've only got one color, so like it'll just not get the other colors because it's we're seeing multiple color lines here. So, if you just get rid of one, I don't care if I have a green screen.

**Dave Jones:** In fact, that'll be quite retro. If we go down here, we should be able to see some RGB inputs and and bingo! There you go. 75 75 75 should be three of those.

**Dave Jones:** Yep. Okay, so that'll be red, green, blue input there. And I'm sure if we buzzed out that point there, that point, and that point, that would go over to the RGB.

**Dave Jones:** So, which one's which? They do actually have a VGA connector under there, by the looks of it. Nice. Okay, yeah, so you could have put it like a VGA directly on there.

**Dave Jones:** Red, green, blue. There you go. So, you've got I squared C, and you've got grounds, and you've got your vertical sync, your horizontal sync. Let's leave the middle one intact.

**Dave Jones:** Let's leave the green one intact, shall we? Or is the input coming here and going through this zero ohm resistor? I'll I'll just buzz it out. 75 ohms to ground.

**Dave Jones:** That's shorted to the fourth pin down there. Yeah, the bottom side of each of those 75 ohm resistors is grounded. So, the zero ohm resistor could be the input.

**Dave Jones:** Let me try and find it. Geez, the buzzer's loud on this stuff. 786 when you've got a dead silent lab here. Zero. There you go. Fifth pin. 1 2 3 4 5.

**Dave Jones:** So, if we take out the zero ohm resistors, Bob's your uncle. Top zero ohm resistor and the bottom one, and that should just leave us with green. Sorry, you can't see this.

**Dave Jones:** I want to get it vertical. Got him. Okay, let's give that a whirl. And we can't see that, of course. So, as I've shown in the video, just get a light.

**Dave Jones:** Got a little my little light here, and look at that. Magic. Check it out. Like, it's just just absolute magic. You don't need a polarizing filter or any of that rubbish.

**Dave Jones:** So, uh SSD 102 star. Oh, look at that. It certainly is green, but um no, it's not It's It's solving our problem. That was kind of obvious, wasn't it?

**Dave Jones:** But I I do like the green. I like that retro look. I think I might keep it if I can fix this damn thing. Wait. Hold on to your hat.

**Dave Jones:** I think I might have fixed it. Look, if we go through the menu here, in here there actually there's this thing called clock. I I had it on D.

**Dave Jones:** It looks like it has A B C D. On D, we actually got something. Look, but it's not very bright. Uh yeah, it doesn't show up on camera that well, but that looks good.

**Dave Jones:** I think I just need to maybe play around with that clock and then adjust the brightness. Yep. We're good. So, there's something with that clock setting. Let me play Oh, look, there's a few lines over here, but that is actually usable in its own right.

**Dave Jones:** It's just not very bright. Um maybe I could put the other two colors back and it might be good, but uh yeah, I'm going to play around with this clock setting now.

**Dave Jones:** Dull. There you go, I set it to clock A and that looks absolutely fantastic, except the brightness is still quite high. Look at that. There you go. Oh, I like the green.

**Dave Jones:** I'm liking that. Tell me I'm wrong. That looks old school. I love it. I'm not going to put that back. So, that that's fixed. That's all it was. Dull, obviously.

**Dave Jones:** Um there you go. So, there it is. So, I don't know what that clock setting does. It shifts the clock and it's I don't Yeah, don't know. If you know, leave it in the comments.

**Dave Jones:** Couldn't be bothered investigating that, but that works hunky-dory. Look at that. So, I'm now going to try and hopefully retrofit this in here. It's supposed to be the model that actually fits, but uh we'll find out.

**Dave Jones:** Anyway, you get the uh both of the top boards out. You've seen this in the uh previous videos, and that's where all the uh LCD um CRT stuff used to go.

**Dave Jones:** Um and the VGA cable, of course, we'll disconnect that from the back, and we can just plug the cable in, and I can just have a short cable. I don't know about the cable solution yet, but somehow it has to mount in here, and this pulls off, and this has got a little ribbon, which goes over.

**Dave Jones:** That's for the buttons on the front. And there you go. So, we have to somehow mount this screen in there. I I just love the magnesium alloy body on these things.

**Dave Jones:** It's absolutely beautiful. So, all that has to shove in there, and up, that's upside down. All the electronics are going to fall out. So, this has to somehow get in there like that, and mount on the back of here.

**Dave Jones:** So, oh, that's a pretty good fit. That's not bad. Although, you can see it. Um you could just put some black tape on there, I guess, just to cover up the metal.

**Dave Jones:** But oh, well, I don't I don't know. Why won't you put the front cover? I actually the front cover, yeah, once you put the front cover on there, I don't you'll notice that.

**Dave Jones:** Yep. Just center that in there, and just tape that. Tape that in place, I think, and Bob's your uncle. Um yep, you just need to line it up. Potentially minor problem here.

**Dave Jones:** Um our board requires 12 V DC input, and by the looks of this sticker here, all of our supply here is it doesn't There's plus five, and there's plus 15, and you know, minus five and stuff, but no 12 V to tap off.

**Dave Jones:** Um there could be like a 12 V on a board somewhere, like the plus 15 might go to the board, and there might be a 12 V reg on one of the boards.

**Dave Jones:** Maybe we can tap, but it's just annoying. All right, so this is my plan. I've stuck my PCB on the back of the LCD in here. So, the LCD is stuck in there.

**Dave Jones:** So, that's hunky-dory. I've actually added the control board up here. So, I've stuck that down, so that it should be able to access, cuz the PCBs just in here.

**Dave Jones:** I think this is just vacant space and the power cable because we've got the floppy drive here, which I haven't got actually connected. The connector for that is over here on the edge.

**Dave Jones:** I think there should be 12 volts on that, shouldn't there? And then my VGA cable, I'm just going to have that curled up. I'll stop it flapping around in the breeze in there.

**Dave Jones:** And then the VGA cable here, that will come up there and go in there. I'm just putting some tape on there for the sharp edge and that should just sit in there.

**Dave Jones:** It should just connect up there like that and Bob's your uncle. Um that's the plan. We'll give it a burl. Yeah, it really needed some sort of black mask around the screen there.

**Dave Jones:** So, I haven't figured that out yet, but I don't know. Yeah, I might replace that later. It turns out I had to move the control board because this metal actually is a fit under there like that.

**Dave Jones:** So, the power cable and and that, I don't know. That might have to sit on the fan or flap around in the breeze. I'll figure out some way to do that.

**Dave Jones:** I just wanted to have it outside so I could actually play around with it after the fact. Right, so I screwed this plate back in place and I I've mentioned this before.

**Dave Jones:** I do like how these supports. This is the hard drive board. I don't believe it runs the OS. I think it's just storage. Isn't it? Yeah, that'll just sit in there and then it just slots, it pushes back in place and locks.

**Dave Jones:** It's really It's really very nice. Now, we'll put our processor board in place and I'm sure I can get 12 volts from somewhere on here. There's our VGA connector.

**Dave Jones:** Plug that in. No wackers. Then we put our little interconnect board in here. There is a third board that goes on top. You can see there's another slot there.

**Dave Jones:** I don't know what the third optional third board is. It's rather tricky to get in. But, it's in nonetheless. Side ribbon cables, which I really like. And then, we've got this side interface board over here.

**Dave Jones:** Beautiful. Look at that. So, that'll take the just higher frequency signals over, does it? So, rather than just the IDC ribbon. So, that And we're going to plug the fan in, otherwise it's not going to boot.

**Dave Jones:** And the VGA is plugged in. And then, this is the printer output, I think, isn't it? Ooh, is that why the fan it knows it's not there. It's a smart fan.

**Dave Jones:** Control temp. So, yeah, that's just not I don't think that's an ordinary fan. Or is that a pot? No, I don't know. It's a temp temp sensor. Yeah, it looks like a control temp.

**Dave Jones:** Looks like yeah, 45°. Looks like yeah, something smart about it. But anyway, we do have our control board now, so we can just start stick that down to the fan.

**Dave Jones:** No worries. And uh all we've got to do is get 12 volts into this sucker. So, I got might Well, I can just measure things or I can just check the manual.

**Dave Jones:** See if we can get the pin out for that. Oh, no. I found it. It's got some yeah, convoluted ribbon which goes over. So, I have to take that shield off and try and get it back in.

**Dave Jones:** All right, let's just turn it on temporarily. So, I've got the plug pack actually connected. Let's see if I've got it all connected in place. No sync. It should take a bit.

**Dave Jones:** Yeah, it looks quite It is a bit offset. That's not just the camera angle. Well, partially the camera angle. There you go. Tektronix TDS runtime environment. It's not hugely bright, but I can increase the brightness on that and contrast.

**Dave Jones:** No workers. So, that works. Yes, I did change it back to white. Sorry. Yeah, I did like just in case you want to do the color upgrade option or there's some sort of, you know, shading or something like that for the instant, you know, the DPO mode or something like that.

**Dave Jones:** Hey! That is not fish flashing anymore. Ah, can't catch a break. Bloody Murphy. Although I didn't see a light come on, I didn't hear a click clunk or anything.

**Dave Jones:** It's just a ribbon, so it looks like it's custom thing. It's going to work. Nope, it stopped again. What? Seriously? I haven't done anything. Oh, jeez. Well, I've done a few repairs and it works, but no, that's not my tripod on the wrong angle.

**Dave Jones:** Yeah, don't use gaffer tape to hold in your screen. Looks like I'm going to have to do something better than that. Oh, it's probably going to take it off anyway to do the black surround but it now works.

**Dave Jones:** So, yeah, it's not very bright so I can call that up but yeah, I don't know like like four five times in a row it didn't work but now it's working.

**Dave Jones:** So I I don't know. Like is that non-volatile Dallas SRAM going? Like I I don't know is the hard drive going that requires cuz I can hear the hard drive spinning up when it boots and you know, it's trying to access something and I I yeah, I don't know.

**Dave Jones:** All I've got to do now is well, fix that and find a 12 volt point. Now, the way you way I would find a 12 volt point, I've got the manual, I've got the service manual, maybe it's got some voltage test points or something like that.

**Dave Jones:** But I'd be looking around at caps, things like these tans down here. You can see these tantalums, right? Which will get Oops, kicked up my focus there, had on manual.

**Dave Jones:** Look at caps like this and ones that are like high voltage rated could be it. Like you could get like a 16 volt or a 25 volt you know take tan or an electrolytic or something like that.

**Dave Jones:** These are all take tans on here. There's no electrolys at all on here actually but there's a few take tans. So I might just go around and actually measure those and we might get lucky.

**Dave Jones:** We might actually get 12 volts. I mean down here is near the floppy drive which I've still got disconnected. No, that wasn't it by the way. So yeah, maybe there's 12 volts around there.

**Dave Jones:** So I might check out that see if I get lucky. All right, do I feel lucky? Let's have a squeeze. 5 volts. Nope. 5 volts. Nope. 3.3. No, these are right in the middle of board.

**Dave Jones:** These are all going to be 5 volt. No. There's one right near card edge over here. No, not a sausage. Anyway, pretty confident I'll find 12 volts on the hard drive board here.

**Dave Jones:** So and then it's easy just to bring the wire under the other board and just solder it on. No wackers. Unfortunately, you turn it on with this board and all you get is hiccuping rails.

**Dave Jones:** It's all you get. So yeah, that's that's no good at all. It's almost as if it doesn't you know, it needs the logic board to switch it on. So we like to switch the to keep the power supply switched on it.

**Dave Jones:** You know, switches it on the logic board supposed to I don't know send back power good signal or something and then switches off and hiccup hiccup hiccup. Well, it turns out that the optimal position for the LCD actually fits within side the existing rubber.

**Dave Jones:** Here, you can kind of sort of like push the rubber to the side a bit and it kind of sort of fits in there which is pretty much the ideal angle like actual placement within there.

**Dave Jones:** So yeah, it's not too bad. And it looks like the LCD is like practically the exact height of the existing plastic in here. So, you could actually like you know, get a custom fitted you know, plastic backing on it or something like that if you're really you know, if you're really keen.

**Dave Jones:** Now, at this stage I thought it might be easy just to power this board from uh 5 volts, but um unfortunately well, the the outputs here are 1.2 volts and 3.3 as you'd expect for a a you know, custom ASIC like that and the input is actually sure enough 5 volts.

**Dave Jones:** Okay, so we don't need our 12 volts in, but then our LCD over here that's actually 9.8 volts. So, yeah, and that's probably coming in from that'll be derived from the uh 12 volt input.

**Dave Jones:** So, we can't just bypass that and put the 5 volts directly in. I don't think that's going to work. And I just checked the uh service manual. I found a service manual that was searchable for the uh D model here and I searched for 12 volts and nothing comes up at all.

**Dave Jones:** So, I don't think there's a single 12 volt rail in this entire product. Wouldn't you know it? Bloody Murphy. All right, so what I'm going to do is I'm going to use uh one of these little TI uh converter modules.

**Dave Jones:** These are little uh 12 watt uh jobbies. Uh more than enough and uh you can it's 5 volt input to adjustable output depending on what a set resistor um is and I could just got these in the junk bin uh in my parts cabinet and we yeah, I'm going to just use one of those.

**Dave Jones:** So, a single resistor on there, 5 volts in, that'll give me 12 volts out and then I can just solder it to any point on that uh main processor board, really.

**Dave Jones:** Bugger, it looks like the uh shot I just took uh over on the other bench actually powering up the uh little uh brick DC-to-DC uh converter. Um it just 5 volts in, 12 volts out.

**Dave Jones:** It was hunky-dory, but I don't know, the camera lost that clip. It was corrupted or some rubbish. I don't know. Um I think the battery died or something. Anyway, I've got the wires coming out here, heat shrunk, and then I've just got them going into two uh header pins here, and I actually found ground and 5 volts on uh pins like like three and five there or something like that.

**Dave Jones:** Um so yeah, so I found my 5 volts. So that goes into the DC-to-DC converter. That's all hidden behind there. And uh let's try and power it up, shall we?

**Dave Jones:** Right, so I think I've got that around the right way. Otherwise, the magic smoke's going to escape. Uh I got my 12-volt uh uh DC-to-5-to-12-volt DC-to-DC converter in there.

**Dave Jones:** And um it should power up. So let's go. Wait. Gone up to seven on there. Yep. Obviously getting power. And will it show that problem that we were having before?

**Dave Jones:** We got flash flash flash flash up on the LED display up there. It's going through its boot cycle, though it froze after this, didn't it? Can't remember exactly. And that has booted.

**Dave Jones:** Uh yeah, I need to short my obviously not low conductive enough to uh clean that but and get that menu off. But that that's a winner winner chicken dinner.

**Dave Jones:** Whack that front panel back on. Going to operate the buttons. We've got the floppy back connected, although I don't think I ever tested the floppy. No idea if it works.

**Dave Jones:** There are modern uh replacements you can get. Solid state replacements for the floppy, I believe. Yep, there we go. That's got to click into place. Really bit difficult to get these front panels off.

**Dave Jones:** There's a bit of a knack to it. There you go. Like a bought one. And here it is, cover back on. Does actually power up, and it seems to work.

**Dave Jones:** So I have to run like, you know, feed in signals, but I fed in signals before and I think all four channels worked. Um, so, yeah, it's all hunky-dory.

**Dave Jones:** The screen isn't as bright. I like if you turn the brightness up, it just appears like like the backlight and it fades out and stuff. So, you know, it's okay, but it's you know, it's nothing to write home about.

**Dave Jones:** Anyway, the good part about it is is that it is functional. There's channel one. There's a significant offset, actually. Channel two, significant offset. So, I might have to run through the Three's got an offset as well.

**Dave Jones:** And four, might have to do there's a couple of more traces in there. I got some math waveform on or something. Let's turn DPO mode on. Uh, which works better in color, of course, but then it it drastically drops the memory.

**Dave Jones:** Uh, yep, that just turns it back off. And we can put it in dot mode. Yay! Cal down here, signal path initialized. Can we hit that? Compensation corrects for DC inaccuracies.

**Dave Jones:** That's what we want cuz by temperature variations, long-term drift. Yep, can run anytime after the oscilloscope has warmed up. Okay, so I'll leave it warming up for I think it's 30 minutes.

**Dave Jones:** And then they claim rerun it. Um, if the ambient temp has changed by more than 5 C or once a week in vertical settings of 5 mV per division or less.

**Dave Jones:** I don't I don't know what the front end's like on these really drift. Yeah, I don't I don't recall um, them being that bad. Don't recall ever being an issue um, for the older ones I've used.

**Dave Jones:** Oh, yeah. Yep, there it goes. I'll I'll just run it just to see if the uh, DC offset goes away. Who cares if it drifts again, you can just rerun it as many times as you want.

**Dave Jones:** Well, that's finished and yep, that fixed the uh, DC offset issue as you'd expect. So, yeah, no worries. Can we change the vertical on that? Looks good. We can go right down to 1 mV per division.

**Dave Jones:** Not a problem. So, there you go. That was an interesting upgrade of a uh, Tektronix TDS 540D and as I said, uh, there is a color upgrade available as well.

**Dave Jones:** You have to uh, solder in the extra RAM chips and do some other um, mods to it. I can't remember what they were, but unfortunately I can't find those chips.

**Dave Jones:** I've got them in a little baggie somewhere down in the bunker, but you know, it's in the last lab move they've come a gutser. And yeah, you know, be nice to get some new knobs for these things, but anyway, I got plenty of scopes here in the lab.

**Dave Jones:** I have no use for this one, so I'll probably just I don't know, sell this auction it off or something. And no, please please do not leave comments down below.

**Dave Jones:** Oh, I'd love to have it. I'll pay for postage. Trust me, I'll pay for postage. No, you don't want to pay for postage for this thing and no, I don't want to ship it overseas.

**Dave Jones:** Sorry, that's just the way it is, okay? Shipping these things is a pain in the ass, so I'm just going to do it I'll just probably just, you know, sell it locally.

**Dave Jones:** Start at a 99 cent auction or something, maybe. After all, it was found in the dumpster. But yeah, four channel 500 meg bandwidth. I'll double check that two gigs samples per second.

**Dave Jones:** I think that it halves, doesn't it? Anyway, I'm going to put like the minimum of effort required into this to just to tell people what it is and I'll probably just auction this thing off or something.

**Dave Jones:** I don't know. But anyway, if you found that video interesting, give it a big thumbs up. As always, discuss down below. Catch you next time.
