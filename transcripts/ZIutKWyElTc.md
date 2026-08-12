---
video_id: ZIutKWyElTc
title: EEVblog 1515 - Dumpster Tektronix TDS540D 500MHz Oscilloscope LCD Upgrade
url: https://www.youtube.com/watch?v=ZIutKWyElTc
source: youtube-asr
---

**Dave Jones:** Hi, you might remember this dumpster find from a video quite it was probably a few years ago now. Anyway, I'll link it up here and down below if you haven't seen it. It's a Tektronix TDS 540D and it's a four-channel 500 megahertz

**Dave Jones:** jobby and it actually works but the CRT in it didn't work but the I was able to get it working from the VGA output on the back and it seemed to work just fine. It's missing a couple of knobs but

**Dave Jones:** these TDS series scopes they do have a reputation for having problems over the years but they're still incredibly powerful scopes. It doesn't have a huge amount of memory I think it's only like 32K or something. Four-channel 500 megahertz I think two gig sample per

**Dave Jones:** second. You know, it's a pretty still a pretty beastly scope. So I thought that instead of repairing the CRT that I'd do an LCD replacement for it and this is actually quite a common thing a lot of people do

**Dave Jones:** a CRT replacement for this thing. So that's what I've got now but I'm having a bit of issue with it. Show you what's actually going on here and see if we can solve it. Anyway, during my live show the other week I did

**Dave Jones:** actually get this out of the bunker. It's been there in parts and I reassembled it and when I first turned it on I encountered a bizarre fault. It didn't work and I'll insert the clip here and it was just amazing what the

**Dave Jones:** culprit actually was. Flowchart. Diagnostic flowchart primary troubleshooting procedure. Press on the principal power switch. Can you hear the fan whirring? No, cuz I've disconnected it. 622 refers to the flashing code eight in the right center of the flowchart. Oh, thank you.

**Dave Jones:** Primary troubleshooting procedure. Really don't miss it. Does DS1 first flash dot eight then display a sequence of hex numbers? No. Does DS1 flash eight then display the sequence of hex numbers pausing to the flash.c. No, no. Replace the A11D RAM processor display module.

**Dave Jones:** Obviously, displaying the eight is the first thing it does and then it just resets and keeps flashing eight. Eight. So, it's clearly not being allowed to go through its sequence. It's like change the entire processor board because you

**Dave Jones:** get a flashy eight. No. No, no, no. I'll I'll plug the fan in just for that authentic fan noise. I don't think it's detecting the fan. It's only a two-wire jobby, but you could detect that. Who knows? That'd be

**Dave Jones:** embarrassing if it was. Hey, no. It's now working. It was the fan. Really? Wow. Yeah, it's flashing. It went through a cycle. All all the leads are on. It's now flashing top, bottom, top, bottom, top, bottom segment. It boots.

**Dave Jones:** May I don't know. Is the Dallas SRAM in this thing going? Let's try and prove that. I'm going to disconnect the fan. The only thing I'm going to do is disconnect the fan. I'm going to turn it back on. I think it'll work. I reckon

**Dave Jones:** there's something else afoot. No, it detects the fan. There you go. It detects the fan. Wow, I would not have guessed that. It is It must have some circuitry to detect that the fan is connected cuz it's not like a

**Dave Jones:** it the fan's only a two-wire jobby. That That made a fool out of me. I would not have guessed that. Who else would have guessed? Be honest. That it was detecting the fan and that was causing it to cycle boot. Although, the fan does

**Dave Jones:** plug into the processor board. There's a bit of a bit of a bit of a giveaway. It plugs in the processor board, not in the power supply board. So, there you have it. It was the fan on this thing, which

**Dave Jones:** is this giant jobby over here. And as you can see, like it's it's only a two-pin physical connection on there. So, they must be doing some sort of like load detection to, you know, determine that there there's a load on the fan.

**Dave Jones:** So, if I boot it up without the fan here, and you can see it just flashes the eight and the front panel just flashes off and on. It's like it's like it the power supply's hiccuping. It's doing something like that.

**Dave Jones:** So, yeah, it's really weird. And I don't think this is actually covered in the manual at all. Actually, I haven't tried this. Can I just plug the fan in? Will it Yeah, look. It just As soon as I plug

**Dave Jones:** the fan in, it goes. Don't know if the four is correct. It hasn't fully booted yet. Like that when it's good. Nah, I'll just turn it off. So, we'll just boot that up. There we go. It's gone through

**Dave Jones:** its power on. Yep. And then it'll eventually reach a point where it will shoot just toggle Yeah, toggle up and down like that and it's working. Now, of course, this uses some Dallas non-volatile memory. And what's the date code on

**Dave Jones:** those? '99. So, they're 22 years old. So, yeah, that's a bit of a problem. But anyway, it still seems to work. I'm not sure if they hold calibration data or whatnot. You can see there's some missing memory here. This is actually

**Dave Jones:** for the color option. I did actually buy some memory. This is way back when I was in the old that big rented lab that I had and I was looking at doing this. I did actually buy the memory and I've got

**Dave Jones:** it somewhere, but it's you know, hidden away in a box somewhere in the bunker. So, yeah, I'm not going to bother with the color upgrade until I find that. I just want to get the LCD working. So, what

**Dave Jones:** I've got is this LCD here. I'll put up the data. Here it is. A generic type, but apparently this is the one that fits the TDS or at least that's the info I found on the web interwebs somewhere and yeah, it just

**Dave Jones:** came with one of these boards which has a VGA interface. You buy the LCD on its own, but or you can buy it with a board. And unfortunately, I'm getting a bit of problem. So, let me power it up. So,

**Dave Jones:** check it out. Don't know if you're seeing that, but I've only got one waveform there, but there's more than one because it's got multiple colors. Have a look at the font down here. If you can see that it's got the different

**Dave Jones:** colors there and they're on like alternate lines or something. There's some sort of like interlacing type problem or something like that. There's something going on there, but it does work. Interestingly, if I turn on the menu system, it does it with the menu as

**Dave Jones:** well. Auto config, that's not going to fix it. So, oh, there we go. Now, it just moved it up to the top there. The text is fine, but it's I'm doing some sort of weird decoding of that. And now, given that

**Dave Jones:** it's got different colors and this is only a mono output, uh first of all, and then I will uh disconnect, I think, um two of the color lines and see like if we just get the one color and it's

**Dave Jones:** it's fine. I don't know. I've got a slightly more modern scope. My MDO 3000 has a VGA output and that looks fantastic. There it is. So, it's something particular with this uh TDS 540. Yes, if you're wondering what that

**Dave Jones:** uh display is there, that's a uh safe operating area uh display. I've been playing around with that. I might maybe want to see a video on safe operating area, anyone? Viewer? And I've got another LCD here, but it's the wrong

**Dave Jones:** form factor. I'm not sure where this one actually uh came from. It works just fine and dandy. So, there's something with this board that's um in particular with the signal from this uh TDS 540, and but this board um

**Dave Jones:** I don't know, JST pin or something um works just fine. So, yeah, look, it's beautiful. But, it's the wrong form factor and no, the um LCD cables aren't compatible, I don't think. What we want to do is disconnect combination of the

**Dave Jones:** colors. So, if I've only got one color, so like it'll just not get the other colors because it's we're seeing multiple color lines here. So, if you just get rid of one, I don't care if I have a green screen. In fact, that'll be

**Dave Jones:** quite retro. If we go down here, we should be able to see some RGB inputs and and bingo! There you go. 75 75 75 should be three of those. Yep. Okay, so that'll be red, green, blue input there. And I'm sure if

**Dave Jones:** we buzzed out that point there, that point, and that point, that would go over to the RGB. So, which one's which? They do actually have a VGA connector under there, by the looks of it. Nice. Okay, yeah, so you could have put it like a

**Dave Jones:** VGA directly on there. Red, green, blue. There you go. So, you've got I squared C, and you've got grounds, and you've got your vertical sync, your horizontal sync. Let's leave the middle one intact. Let's leave the green one intact, shall we? Or

**Dave Jones:** is the input coming here and going through this zero ohm resistor? I'll I'll just buzz it out. 75 ohms to ground. That's shorted to the fourth pin down there. Yeah, the bottom side of each of those 75 ohm resistors is

**Dave Jones:** grounded. So, the zero ohm resistor could be the input. Let me try and find it. Geez, the buzzer's loud on this stuff. 786 when you've got a dead silent lab here. Zero. There you go. Fifth pin. 1 2

**Dave Jones:** 3 4 5. So, if we take out the zero ohm resistors, Bob's your uncle. Top zero ohm resistor and the bottom one, and that should just leave us with green. Sorry, you can't see this. I want to get it vertical. Got

**Dave Jones:** him. Okay, let's give that a whirl. And we can't see that, of course. So, as I've shown in the video, just get a light. Got a little my little light here, and look at that. Magic. Check it out. Like, it's just just absolute

**Dave Jones:** magic. You don't need a polarizing filter or any of that rubbish. So, uh SSD 102 star. Oh, look at that. It certainly is green, but um no, it's not It's It's solving our problem. That was kind of obvious, wasn't it? But I I do

**Dave Jones:** like the green. I like that retro look. I think I might keep it if I can fix this damn thing. Wait. Hold on to your hat. I think I might have fixed it. Look, if we go through the menu here,

**Dave Jones:** in here there actually there's this thing called clock. I I had it on D. It looks like it has A B C D. On D, we actually got something. Look, but it's not very bright. Uh yeah, it doesn't show up on

**Dave Jones:** camera that well, but that looks good. I think I just need to maybe play around with that clock and then adjust the brightness. Yep. We're good. So, there's something with that clock setting. Let me play Oh, look, there's a

**Dave Jones:** few lines over here, but that is actually usable in its own right. It's just not very bright. Um maybe I could put the other two colors back and it might be good, but uh yeah, I'm going to play around with this clock setting now.

**Dave Jones:** Dull. There you go, I set it to clock A and that looks absolutely fantastic, except the brightness is still quite high. Look at that. There you go. Oh, I like the green. I'm liking that. Tell me I'm wrong. That looks old

**Dave Jones:** school. I love it. I'm not going to put that back. So, that that's fixed. That's all it was. Dull, obviously. Um there you go. So, there it is. So, I don't know what that clock setting does. It shifts the clock and it's I don't

**Dave Jones:** Yeah, don't know. If you know, leave it in the comments. Couldn't be bothered investigating that, but that works hunky-dory. Look at that. So, I'm now going to try and hopefully retrofit this in here. It's supposed to be the model that actually fits, but uh

**Dave Jones:** we'll find out. Anyway, you get the uh both of the top boards out. You've seen this in the uh previous videos, and that's where all the uh LCD um CRT stuff used to go. Um and the VGA cable, of course, we'll disconnect that

**Dave Jones:** from the back, and we can just plug the cable in, and I can just have a short cable. I don't know about the cable solution yet, but somehow it has to mount in here, and this pulls off, and

**Dave Jones:** this has got a little ribbon, which goes over. That's for the buttons on the front. And there you go. So, we have to somehow mount this screen in there. I I just love the magnesium alloy body on these things. It's absolutely beautiful.

**Dave Jones:** So, all that has to shove in there, and up, that's upside down. All the electronics are going to fall out. So, this has to somehow get in there like that, and mount on the back of here. So, oh, that's a pretty

**Dave Jones:** good fit. That's not bad. Although, you can see it. Um you could just put some black tape on there, I guess, just to cover up the metal. But oh, well, I don't I don't know. Why won't you put the front cover? I

**Dave Jones:** actually the front cover, yeah, once you put the front cover on there, I don't you'll notice that. Yep. Just center that in there, and just tape that. Tape that in place, I think, and Bob's your uncle. Um yep, you just need to line it up.

**Dave Jones:** Potentially minor problem here. Um our board requires 12 V DC input, and by the looks of this sticker here, all of our supply here is it doesn't There's plus five, and there's plus 15, and you know, minus five and stuff, but no 12 V

**Dave Jones:** to tap off. Um there could be like a 12 V on a board somewhere, like the plus 15 might go to the board, and there might be a 12 V reg on one of the boards. Maybe we can

**Dave Jones:** tap, but it's just annoying. All right, so this is my plan. I've stuck my PCB on the back of the LCD in here. So, the LCD is stuck in there. So, that's hunky-dory. I've actually added the control board up here. So, I've stuck

**Dave Jones:** that down, so that it should be able to access, cuz the PCBs just in here. I think this is just vacant space and the power cable because we've got the floppy drive here, which I haven't got actually connected.

**Dave Jones:** The connector for that is over here on the edge. I think there should be 12 volts on that, shouldn't there? And then my VGA cable, I'm just going to have that curled up. I'll stop it flapping around in the

**Dave Jones:** breeze in there. And then the VGA cable here, that will come up there and go in there. I'm just putting some tape on there for the sharp edge and that should just sit in there. It should just connect up there like that and

**Dave Jones:** Bob's your uncle. Um that's the plan. We'll give it a burl. Yeah, it really needed some sort of black mask around the screen there. So, I haven't figured that out yet, but I don't know. Yeah, I might replace that

**Dave Jones:** later. It turns out I had to move the control board because this metal actually is a fit under there like that. So, the power cable and and that, I don't know. That might have to sit on the fan or flap around in the breeze.

**Dave Jones:** I'll figure out some way to do that. I just wanted to have it outside so I could actually play around with it after the fact. Right, so I screwed this plate back in place and I I've mentioned this

**Dave Jones:** before. I do like how these supports. This is the hard drive board. I don't believe it runs the OS. I think it's just storage. Isn't it? Yeah, that'll just sit in there and then it just slots, it pushes

**Dave Jones:** back in place and locks. It's really It's really very nice. Now, we'll put our processor board in place and I'm sure I can get 12 volts from somewhere on here. There's our VGA connector. Plug that in. No wackers. Then we put our little

**Dave Jones:** interconnect board in here. There is a third board that goes on top. You can see there's another slot there. I don't know what the third optional third board is. It's rather tricky to get in. But, it's in nonetheless.

**Dave Jones:** Side ribbon cables, which I really like. And then, we've got this side interface board over here.

**Dave Jones:** Beautiful. Look at that. So, that'll take the just higher frequency signals over, does it? So, rather than just the IDC ribbon. So, that And we're going to plug the fan in, otherwise it's not going to boot. And the VGA is plugged

**Dave Jones:** in. And then, this is the printer output, I think, isn't it? Ooh, is that why the fan it knows it's not there. It's a smart fan. Control temp. So, yeah, that's just not I don't think that's an ordinary fan. Or is that a

**Dave Jones:** pot? No, I don't know. It's a temp temp sensor. Yeah, it looks like a control temp. Looks like yeah, 45°. Looks like yeah, something smart about it. But anyway, we do have our control board now, so we can

**Dave Jones:** just start stick that down to the fan. No worries. And uh all we've got to do is get 12 volts into this sucker. So, I got might Well, I can just measure things or I can just check the manual.

**Dave Jones:** See if we can get the pin out for that. Oh, no. I found it. It's got some yeah, convoluted ribbon which goes over. So, I have to take that shield off and try and get it back in. All right, let's just

**Dave Jones:** turn it on temporarily. So, I've got the plug pack actually connected. Let's see if I've got it all connected in place. No sync. It should take a bit. Yeah, it looks quite It is a bit offset. That's not

**Dave Jones:** just the camera angle. Well, partially the camera angle. There you go. Tektronix TDS runtime environment. It's not hugely bright, but I can increase the brightness on that and contrast. No workers. So, that works. Yes, I did change it

**Dave Jones:** back to white. Sorry. Yeah, I did like just in case you want to do the color upgrade option or there's some sort of, you know, shading or something like that for the instant, you know, the DPO mode or

**Dave Jones:** something like that. Hey! That is not fish flashing anymore. Ah, can't catch a break. Bloody Murphy. Although I didn't see a light come on, I didn't hear a click clunk or anything. It's just a ribbon, so it looks like

**Dave Jones:** it's custom thing. It's going to work. Nope, it stopped again. What? Seriously? I haven't done anything. Oh, jeez. Well, I've done a few repairs and it works, but no, that's not my tripod on the wrong angle. Yeah, don't use gaffer tape to hold in

**Dave Jones:** your screen. Looks like I'm going to have to do something better than that. Oh, it's probably going to take it off anyway to do the black surround but it now works. So, yeah, it's not very bright so I can call that up but yeah, I

**Dave Jones:** don't know like like four five times in a row it didn't work but now it's working. So I I don't know. Like is that non-volatile Dallas SRAM going? Like I I don't know is the hard drive going that requires cuz I can hear the hard

**Dave Jones:** drive spinning up when it boots and you know, it's trying to access something and I I yeah, I don't know. All I've got to do now is well, fix that and find a 12 volt point. Now, the way you way I

**Dave Jones:** would find a 12 volt point, I've got the manual, I've got the service manual, maybe it's got some voltage test points or something like that. But I'd be looking around at caps, things like these tans down here. You can see these

**Dave Jones:** tantalums, right? Which will get Oops, kicked up my focus there, had on manual. Look at caps like this and ones that are like high voltage rated could be it. Like you could get like a 16 volt or a

**Dave Jones:** 25 volt you know take tan or an electrolytic or something like that. These are all take tans on here. There's no electrolys at all on here actually but there's a few take tans. So I might just go around and

**Dave Jones:** actually measure those and we might get lucky. We might actually get 12 volts. I mean down here is near the floppy drive which I've still got disconnected. No, that wasn't it by the way. So yeah, maybe there's 12

**Dave Jones:** volts around there. So I might check out that see if I get lucky. All right, do I feel lucky? Let's have a squeeze. 5 volts. Nope. 5 volts. Nope. 3.3. No, these are right in the middle of board. These are all going to be 5 volt.

**Dave Jones:** No. There's one right near card edge over here. No, not a sausage. Anyway, pretty confident I'll find 12 volts on the hard drive board here. So and then it's easy just to bring the wire under the other board and

**Dave Jones:** just solder it on. No wackers. Unfortunately, you turn it on with this board and all you get is hiccuping rails. It's all you get. So yeah, that's that's no good at all. It's almost as if it doesn't you know,

**Dave Jones:** it needs the logic board to switch it on. So we like to switch the to keep the power supply switched on it. You know, switches it on the logic board supposed to I don't know send back power good

**Dave Jones:** signal or something and then switches off and hiccup hiccup hiccup. Well, it turns out that the optimal position for the LCD actually fits within side the existing rubber. Here, you can kind of sort of like push the rubber to the side

**Dave Jones:** a bit and it kind of sort of fits in there which is pretty much the ideal angle like actual placement within there. So yeah, it's not too bad. And it looks like the LCD is like practically the exact height of

**Dave Jones:** the existing plastic in here. So, you could actually like you know, get a custom fitted you know, plastic backing on it or something like that if you're really you know, if you're really keen. Now, at this stage I

**Dave Jones:** thought it might be easy just to power this board from uh 5 volts, but um unfortunately well, the the outputs here are 1.2 volts and 3.3 as you'd expect for a a you know, custom ASIC like that and the input is actually sure enough 5

**Dave Jones:** volts. Okay, so we don't need our 12 volts in, but then our LCD over here that's actually 9.8 volts. So, yeah, and that's probably coming in from that'll be derived from the uh 12 volt input. So, we can't just bypass that and put

**Dave Jones:** the 5 volts directly in. I don't think that's going to work. And I just checked the uh service manual. I found a service manual that was searchable for the uh D model here and I searched for 12 volts

**Dave Jones:** and nothing comes up at all. So, I don't think there's a single 12 volt rail in this entire product. Wouldn't you know it? Bloody Murphy. All right, so what I'm going to do is I'm going to use uh

**Dave Jones:** one of these little TI uh converter modules. These are little uh 12 watt uh jobbies. Uh more than enough and uh you can it's 5 volt input to adjustable output depending on what a set resistor um is and I could just got these in the

**Dave Jones:** junk bin uh in my parts cabinet and we yeah, I'm going to just use one of those. So, a single resistor on there, 5 volts in, that'll give me 12 volts out and then I can just solder it to any

**Dave Jones:** point on that uh main processor board, really. Bugger, it looks like the uh shot I just took uh over on the other bench actually powering up the uh little uh brick DC-to-DC uh converter. Um it just 5 volts in, 12 volts out. It was

**Dave Jones:** hunky-dory, but I don't know, the camera lost that clip. It was corrupted or some rubbish. I don't know. Um I think the battery died or something. Anyway, I've got the wires coming out here, heat shrunk, and then I've just got them

**Dave Jones:** going into two uh header pins here, and I actually found ground and 5 volts on uh pins like like three and five there or something like that. Um so yeah, so I found my 5 volts. So that goes into the

**Dave Jones:** DC-to-DC converter. That's all hidden behind there. And uh let's try and power it up, shall we? Right, so I think I've got that around the right way. Otherwise, the magic smoke's going to escape. Uh I got my 12-volt uh

**Dave Jones:** uh DC-to-5-to-12-volt DC-to-DC converter in there. And um it should power up. So let's go. Wait. Gone up to seven on there. Yep. Obviously getting power. And will it show that problem that we were having before? We got flash flash

**Dave Jones:** flash flash up on the LED display up there. It's going through its boot cycle, though it froze after this, didn't it? Can't remember exactly. And that has booted. Uh yeah, I need to short my obviously not low conductive enough

**Dave Jones:** to uh clean that but and get that menu off. But that that's a winner winner chicken dinner. Whack that front panel back on. Going to operate the buttons. We've got the floppy back connected, although I don't think I ever tested the floppy. No

**Dave Jones:** idea if it works. There are modern uh replacements you can get. Solid state replacements for the floppy, I believe. Yep, there we go. That's got to click into place. Really bit difficult to get these front panels off. There's a bit of

**Dave Jones:** a knack to it. There you go. Like a bought one. And here it is, cover back on. Does actually power up, and it seems to work. So I have to run like, you know, feed in signals, but I fed in signals before and

**Dave Jones:** I think all four channels worked. Um, so, yeah, it's all hunky-dory. The screen isn't as bright. I like if you turn the brightness up, it just appears like like the backlight and it fades out and stuff. So, you know, it's okay, but

**Dave Jones:** it's you know, it's nothing to write home about. Anyway, the good part about it is is that it is functional. There's channel one. There's a significant offset, actually. Channel two, significant offset. So, I might have to run through the Three's

**Dave Jones:** got an offset as well. And four, might have to do there's a couple of more traces in there. I got some math waveform on or something. Let's turn DPO mode on. Uh, which works better in color, of course, but then it it drastically drops

**Dave Jones:** the memory. Uh, yep, that just turns it back off. And we can put it in dot mode. Yay! Cal down here, signal path initialized. Can we hit that? Compensation corrects for DC inaccuracies. That's what we want cuz by

**Dave Jones:** temperature variations, long-term drift. Yep, can run anytime after the oscilloscope has warmed up. Okay, so I'll leave it warming up for I think it's 30 minutes. And then they claim rerun it. Um, if the ambient temp has changed by more than 5 C or once a week

**Dave Jones:** in vertical settings of 5 mV per division or less. I don't I don't know what the front end's like on these really drift. Yeah, I don't I don't recall um, them being that bad. Don't recall ever being an issue um, for the

**Dave Jones:** older ones I've used. Oh, yeah. Yep, there it goes. I'll I'll just run it just to see if the uh, DC offset goes away. Who cares if it drifts again, you can just rerun it as many times as you

**Dave Jones:** want. Well, that's finished and yep, that fixed the uh, DC offset issue as you'd expect. So, yeah, no worries. Can we change the vertical on that? Looks good. We can go right down to 1 mV per division. Not a problem. So, there you

**Dave Jones:** go. That was an interesting upgrade of a uh, Tektronix TDS 540D and as I said, uh, there is a color upgrade available as well. You have to uh, solder in the extra RAM chips and do some other um,

**Dave Jones:** mods to it. I can't remember what they were, but unfortunately I can't find those chips. I've got them in a little baggie somewhere down in the bunker, but you know, it's in the last lab move they've come a gutser. And yeah,

**Dave Jones:** you know, be nice to get some new knobs for these things, but anyway, I got plenty of scopes here in the lab. I have no use for this one, so I'll probably just I don't know, sell this auction it off

**Dave Jones:** or something. And no, please please do not leave comments down below. Oh, I'd love to have it. I'll pay for postage. Trust me, I'll pay for postage. No, you don't want to pay for postage for this thing and no, I don't want to

**Dave Jones:** ship it overseas. Sorry, that's just the way it is, okay? Shipping these things is a pain in the ass, so I'm just going to do it I'll just probably just, you know, sell it locally. Start at a 99

**Dave Jones:** cent auction or something, maybe. After all, it was found in the dumpster. But yeah, four channel 500 meg bandwidth. I'll double check that two gigs samples per second. I think that it halves, doesn't it? Anyway, I'm going to put like the minimum of effort

**Dave Jones:** required into this to just to tell people what it is and I'll probably just auction this thing off or something. I don't know. But anyway, if you found that video interesting, give it a big thumbs up. As always, discuss down

**Dave Jones:** below. Catch you next time.
