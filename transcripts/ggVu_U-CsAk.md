---
video_id: ggVu_U-CsAk
title: EEVblog #952 - Nixie Tube Display Project - Part 3
url: https://www.youtube.com/watch?v=ggVu_U-CsAk
source: youtube-asr
---

**Dave Jones:** Hi, it's time for part three in the Nixie tube display driver project and we're on to the schematic now. But just a before we get into the schematic, we'll just go back and look at the drivers that we were going to use. Now,

**Dave Jones:** I was going to actually go with a ULN2003 Darlington transistor driver with the Zener diode clamp as I mentioned in the previous video and then maybe some 74HC595s uh shift registers common as mud to drive those instead of the microchip solution

**Dave Jones:** like single chip type solution. And interestingly, I was actually partway through laying out that schematic when I went to the forum and somebody mentioned a chip that I'd actually done that back in the first video and I actually shot a clip of it, but I didn't

**Dave Jones:** and and ultimately I didn't include it in the edit because it was it was already too long and everything, but I had looked at this chip cuz I thought it was quite interesting, but it didn't have the required voltage or so I

**Dave Jones:** thought, but somebody pointed out that this chip actually has internal clamping and it's suitable. So I took another look at this thing and sure enough. So we're going to have a look at the 6C595 uh series and these are 8-bit shift

**Dave Jones:** registers and having 595 on the end, hey, you might recognize that, right? The 74HC595 the common as mud very useful jelly bean latched shift register which everyone seems to use and everyone I've been using them for decades and I was going

**Dave Jones:** to you probably use it for this project as well. I don't know if it's coincidence that they named it 595, but it works very similar. The front end in terms of the shift register and the latched part of it is very similar to

**Dave Jones:** the 74HC595. Anyway, as it turns out, um this is a fairly jelly bean part as well. And that's what I liked about it last time is that it's available from TI, ST, and NXP um in various flavors and things like

**Dave Jones:** that, various packages. But the standard one, SO16 one, which we'll take a look at here. Now, uh it's the TI one is called the TPIC 6C595 and the uh NXP one is called the N N PIC 6C595, but

**Dave Jones:** they're pin compatible. Basically, uh compatible logic between the two. It's got an eight-stage uh shift register and an eight-bit storage register as well and a serial out, um which so we can cascade the things and it's got eight

**Dave Jones:** open drain outputs as well. Uh it's a quite a nice little part. It's uh rated for uh and it's got the avalanche energy rated and everything. RDS on 7 ohms typical, all that sort of stuff. 250 milliamp current capability, ESD

**Dave Jones:** protection, blah blah blah blah blah. One thing I didn't notice in my first video, otherwise I would have chosen this chip straight away, is that it has actually output clamps on it at 33 volts. And let's go down and take a look

**Dave Jones:** at this. And all I saw when I first briefly looked at this thing was the uh maximum output voltage 33 volts. But as I said, it's actually uh a clamp It's got a Zener diode clamps. And we can

**Dave Jones:** actually go down here and have a look. Now, it's logic level uh supply voltage uh standard 5-volt uh logic. Um now, it's high-level input voltage, we'll come back to this. That's going to be a bit troublesome, 0.8 * VCC or 5 volts.

**Dave Jones:** So, that's going to cause us a bit of an issue, but we can solve that. So, we'll come back to that. Now, if we have a look inside the thing, you'll notice this is a uh typical of all the drain

**Dave Jones:** outputs. And you can see that it's got a um N-channel MOSFET in there. Of course, this diode is going to be the body diode inside that MOSFET, but it's got Zener diode clamping as well. So, look at that. Absolutely brilliant. So, we don't

**Dave Jones:** need external clamping devices, and we've got everything all in the one chip. So, we can replace a 74HC595 plus a ULN2003 into this one chip, and it Look, it costs as little as 31 cents in 2,500 volume. Okay, you go down to one volume

**Dave Jones:** of one from Digikey here, 73 cents. But, you know, hey, that's pretty decent. And, they're available in quantity from three different manufacturers. This is a part that you want to keep in your um parts box to use. This should be like a

**Dave Jones:** standard jelly bean part for any sort of like high voltage interfacing stuff like that. Very, very useful part. And, uh the NXP version exactly um it's basically exactly the uh same, although it's output it's clamping is a little

**Dave Jones:** bit different. It doesn't have that extra Zener uh from the gate down there. Anyway, it's slightly different part, but anyway, but I'm slightly leading you up a bit of a garden path here because this output clamping voltage 33 volts uh

**Dave Jones:** is not really going to do the business um because unfortunately, if we take our 170-volt uh supply voltage, and we subtract 33, that's going to give us 137 volts. And, if you remember the data sheet for the uh IN-12B

**Dave Jones:** Nixie tube that we did in the part one of this video, then it's got an operational range of like 120 volts upwards. So, in theory, um it's you know, you might get some glow from the digits. So, we need a higher clamping

**Dave Jones:** voltage to this, probably closer to the 50 volts, which I've uh mentioned before, because if you do 170 minus uh 50, it gives us that 120-volt data sheet value. But, hey, in engineering, that's too close. We like to like keep some

**Dave Jones:** sort of margin in there. So, if the data sheet says 120 volts minimum that this thing that the Nixie tube will sustain a glow at, if we're clamping at 50 volts with a 170 volt supply, in theory, the often digits that

**Dave Jones:** are supposed to be off could have a faint glow to them. So, hey, if we add some margin, assuming we can find a 50 volt clamping device, we could drop our power supply voltage. Doesn't have to be 170. We can drop it to 160, for example,

**Dave Jones:** with and with a 50 volt clamping voltage, we would get down to 110 volts. That should give us a 10 volt margin. That should be nice. So, where can we find this same chip with a 50 volt clamping voltage? Well, I'm glad you

**Dave Jones:** asked. As it turns out, these TPIC and PIC devices come in different series. We looked at the C series before. Well, you can actually get the B series. You can take a look here. It's the B the TPIC B2595.

**Dave Jones:** As it turns out, a little bit more expensive, No, that's US prices. $1.48, so it's a bit more expensive.

**Dave Jones:** And it's a 20 pin SOIC package, so a bit bigger than the 595 package. And if we go in here and have a look, it's actually an identical device pretty much. It but it has an output clamp voltage of 50

**Dave Jones:** volts. It's 150 milliamps instead of 250 milliamps or whatever. But it's got lower RDS on, but you know, it's practically an identical part in every way, shape, and form. It's just a little bit bigger, little bit more expensive, but that

**Dave Jones:** doesn't matter. A 50 volt clamping voltage. So, we will use that one in our solution. But hey, I think we need to do just one more bench test to see if these digits glow or not With a 160-V supply

**Dave Jones:** and uh 50-V uh Zener diode clamping. A very quick test here. I've got eight uh 50-V Zener diodes. Actually got uh 30-V and 20-V in series here, but it'll give a total uh 50-V drop across here. I've got those

**Dave Jones:** hooked up to the uh cathodes here and 170-V supply. Let's switch it on. 22-K uh source resistor and switch it on. No worries. There's no current draw whatsoever. These aren't It's not switching on. Whatever. Go up to 180 and bingo, we can see

**Dave Jones:** that they're just biased on 0.44 uh milliamps there total for all eight of those uh segments. So, you know, it just switches on. If we turn it back to 70, it just just still on. So, there's a very faint

**Dave Jones:** glow there, but it certainly can't start up at that. If we turn it to 160, uh of course, it's not going to uh either remain on or uh switch on at 160 V with 50-V uh clamping on there. So, a

**Dave Jones:** 50-V clamping device, 160 V, looks, you know, pretty confident. Gives some margin. We're outside of the data sheet value for the minimum operating voltage of the the well, this particular display anyway. So, but your mileage may vary with different types of Nixies. And just

**Dave Jones:** to prove that we can actually switch that on, I've just got a shorting link here and I'll just switch on an individual segment. There we go. Switch on number seven. Zero, eight. And by the way, if we do

**Dave Jones:** turn it back up to say 180 V there and we get that faint biased glow there and we actually switch a segment on, you can still see probably that we still have that glow inside these things. So, but we can switch them

**Dave Jones:** off and on. And if you switch it to 160 V, there we go. So, it proves that we can switch these segments off and on with 50 V clamping, and there's no residual glow in there. So, that looks like it'll work

**Dave Jones:** a treat. All right. So, we've chosen our driver, and I know a lot of people will say, "Oh, why didn't you use the Microchip one?" Or, "Why didn't you use the discrete transistor solution one?" Look, it doesn't matter. Do whatever you

**Dave Jones:** want. They're all going to work the same. I just wanted to try out these nice little TPE devices. Anyway, we've got the TPE B 595. And let's have a look at the schematic here, and this is basically pretty much it. Um so, let's

**Dave Jones:** check it out. Yes, I'm using Altium Designer here. Now, of course, I had to create a Nixie tube symbol here, and it's very quick. It only takes like a minute or two to create your own symbols. No worries. A nice little touch

**Dave Jones:** is that um it's to embed an image like that just to show that it's an actual Nixie. So, I just stole that image from the web, so credit to whoever who took that. But, you know, just a nice little touch like that to

**Dave Jones:** make it look nice. Just embed the graphic in there. And in Altium, that graphic file is not linked. I mean, there's an option to actually embed that in the component itself, so you don't ever lose the file or anything like

**Dave Jones:** that. So, that's a nice touch. Yes, I've rotated it there. And if we have a look at the total schematic here, zoom out, I've got this on an A3 sheet here. And you'll notice that uh we use precisely

**Dave Jones:** 11 of these chips here. So, we haven't wasted a single output. I love that. Now, of course, um to drive the Nixie tube display, it can it can drive it directly. We've got our 22 dropper like we've done in the previous

**Dave Jones:** video, and we just did the test then. That's just fine. But, of course, the decimal point, that has a 0.3 mA uh limit on it. So, because it's a physically smaller uh uh surface area on the um digit decimal point itself. So, it can

**Dave Jones:** only handle a smaller maximum current. So, I've whacked another resistor in series with that. I haven't actually measured that. Um so, I've just whacked in a value of 100k. I'll tweak that later. It doesn't matter. We're going to

**Dave Jones:** put a resistor in there, and we've got um 11 of these chips total, and we didn't waste a single output. Beautiful. Now, as for doing our schematics, I also had to create my own uh symbol for the TPIC

**Dave Jones:** um 6C595. Now, I actually did a symbol for the C version, as well. And if you follow me on EE Blog 2, my second channel, I've already updated a quick video showing creating the symbol for this uh C

**Dave Jones:** version of this uh TPIC here. And there's a reason why I've done the pinout exactly like this. So, I actually recorded this clip uh I uploaded it like uh quite a few days ago, and people have already seen that. If you haven't

**Dave Jones:** subscribed to EE Blog 2, so I'll include that now. And it just explains why I've laid out some of the pins, and it doesn't match the data sheet. So, roll the tape. Just one thing with uh making component symbols like this, because I

**Dave Jones:** had to do this, I couldn't find it in the Altium uh vault library. They've got everything but the one you want. Murphy's law, of course. But, it's trivial to create your own uh circuit symbol like this. It takes, you know, a

**Dave Jones:** minute or two. It's, you know, not hard at all. Um but, just one thing, when you're laying out the pins, let's have a look at the data sheet here. Don't necessarily just follow this uh pinout in the data sheet, because then it

**Dave Jones:** doesn't uh make for a nice flowing circuit diagram. So, you notice how on the data sheet here, uh like, you know, half of the drains are pins 3 to 6 on one side, half are on the other. And if

**Dave Jones:** you're trying to draw a nice neat schematic and you know, that is just a pain in the butt. You've got your Nixie tube on one side or your display or whatever. You're driving it. So it makes sense to have all of the

**Dave Jones:** outputs on one side. Here you'll notice that I've gone to the effort to put in the open collector output symbol here to show that they're well, in this case they're open drain. But you know, same thing you convey the

**Dave Jones:** information. And then here of course VCC. You want VCC up here so that you can put your symbol just there. You want your ground down the bottom so you can put that there. Now the chip enable usually you're going to just you know,

**Dave Jones:** for simple applications you're just going to tie it to ground. So why put it you know, somewhere else like pin seven down here and if your ground's over there then you put put another ground symbol. If you put it right next to your

**Dave Jones:** ground pin pin 16 here then you can just tie it like that. Bingo, real easy. And then VCC up the top of course then you can just put your VCC symbol there. And of course your clear pin often for simple applications again you

**Dave Jones:** will just have that permanently tied high cuz it's an active low cuz I've put the not symbol. That's what that circuit is. It shows that it's an active low input. So you put it right next to the VCC pin

**Dave Jones:** that you most usually going to tie it to. So you don't have to have all your you know, wires in your schematic running everywhere and data in data clock and then data out. And that just makes a nice compact

**Dave Jones:** symbol like this that's going to flow really well cuz then I can put my Nixie tube right here next to it and all the wires will just pop straight out and it'll be ground VCC. They won't get in

**Dave Jones:** the way and then you can have your wires coming in and out for your clock lines and everything else. So it will just makes for a nice flowing schematic. So put a little bit of thought into your circuit symbol there

**Dave Jones:** and really you'll make a make your life much easier and a much more presentable schematic. So, that equally applies to this B version as well. I've got all the outputs on one side here, including the not connect the two not connect pins.

**Dave Jones:** You could have just left those out, but I like to include the not connect pins here and everything on the other side, the input and output pins, the ground and VCC. And you can see the advantage of having the clear pin, which in most

**Dave Jones:** applications would like, you know, majority would likely be tied to VCC. So, having it there like that right next to it just makes it neat and tidy. Likewise for the three grounds and the enable, which in my majority of cases

**Dave Jones:** might be tied directly to the ground like this. So, it it just works out nice and neat because if you laid out this chip as per the actual data sheet, you would have had half the lines coming out

**Dave Jones:** here, half the lines coming out the bottom here, and then going back around. It would have been a mess. You wouldn't have been able to lay out your schematic a nice like eight digits like that and taking up a small amount of compact

**Dave Jones:** space on your schematic. This whole A3 page probably would have been filled just with the lines going everywhere, higgledy-piggledy, all over the shop. So, it's just much nicer. And then we've got just got this bus running along here driving the data

**Dave Jones:** clock input. You can see there. Yeah, the data clock and the register clock all common between all the chips. And then, of course, we just daisy chain them together. We've got our data out going here to the data out of the next

**Dave Jones:** one. So, this is our first chip here. We've got this from our microcontroller solution, and then we and then we just daisy chain them. Boom, like that, chip to chip chip and chip to chip until we get right to the end. And we're not

**Dave Jones:** actually reading any data back, we're just shifting the data out. Now, I mentioned before driving voltages, and this is can be a real trap for young players. So, let's take a look at this. We'll take a look at our microcontroller

**Dave Jones:** solution in a minute, but I mentioned before that we could come a cropper on the input threshold voltage. So, let's go have a look at it here. Here's our 6B595 high-level input voltage. Here it is and it's 0.85 volts. No, sorry, 0.85 * VCC,

**Dave Jones:** which is VCC in this case a 4.5 minimum, nominally 5. So, * 0.85 that's 4.25 volts minimum. So, your input digital signal has to be at least 4.25 volts for you to register a logic one on the input

**Dave Jones:** pin of that chip. And of course, that input pin includes the not only the data in pin here, but the D clock, data clock, and the register clock as well. So, all those three pins must be must be 5-volt uh not only just

**Dave Jones:** 5-volt compatible logic, but they don't have a standard like, you know, TTL input threshold. 4.25 volts input is a relatively high input voltage. So, you really have to drive them hard with like a 5-volt signal. You can't drive them

**Dave Jones:** with 3.3 volt logic. So, we're actually driving this thing with a WeMos D1 Mini. I'll talk about more this more in a minute. It's an ESP8266EX Wi-Fi module chipset because this design is going to be a Wi-Fi internet enabled

**Dave Jones:** eight-digit display and you'll find out why in a future video. But anyway, it's 5-volt powered the module, but its inputs and outputs, its IO pins on here are only 3.3 volts. It's actually got a regulator built in and this 3.3 volts is

**Dave Jones:** actually an output. I don't think we're using that for anything else on here. No, we're not. So, I didn't actually have to connect that at all. But 3.3 volt output. So, it's not enough to drive directly our 6C595 chips. We need

**Dave Jones:** a need a logic level translator in there. Now, you can get a whole bunch of dedicated solutions for logic level translation. TI and other manufacturers make a whole slew of uh logic level translator products. But, our requirement's very simple here. We

**Dave Jones:** only have to drive data, i.e., convert a 3.3 V signal from our module here to drive 5 V output. So, we don't need bidirectional, don't have to get data back, don't have to do anything fancy like that. So, I I

**Dave Jones:** just a simple jelly bean 74HCT04 will do the job. But, there is a trap there, of course. So, let's take a look at the data sheet for the HC and the HCT version. You noticed I used specifically the HCT, and there's a reason for that.

**Dave Jones:** So, if we go down here and have a look, let's go down. Static high-level input voltage. This is for the HC version, not the TTL compatible version. Now, let's take a look here. So, the minimum high-level input voltage here at a VCC,

**Dave Jones:** I find it rather annoying that they don't put like a standard 5 V in there. It It's always just pretty annoying that they do that. Anyway, so you've got to sort of, you know, guess in between. But, at 4.5 V

**Dave Jones:** supply voltage, um at 25° uh typical, the minimum is 3. 15 V. So, you know, like it's not And then at 6 V it's 4.2. So, really, we're inputting a 3.3 V signal, and that's it's cutting it real fine. It may work,

**Dave Jones:** it may not, the HC04 version. So, yeah, that's not the best. So, let's go to the HCT04 down here, and you'll notice the high-level input voltage. Look at this. It's a much better minimum 2 V for a VCC,

**Dave Jones:** um and in in it doesn't give individual voltages. It just gives a range, 4.5 to 5.5 and minimum of 2 volts. Bingo. So, we can easily drive the input to this uh inverter with our 3.3 volt logic. Guaranteed, huge margin, no problems

**Dave Jones:** whatsoever. So, you want this specific TTL compatible HCT04. So, you could have come a cropper there if you used a 74 HCT04 in your design. So, you might have built this thing up, prototype, no worries, whacked in a

**Dave Jones:** HCT04 and found it's not quite working or it might have worked some of the time or it'd be dependent varying with temperature or something like that and it'd be intermittent and you're not quite sure what's going on. You really

**Dave Jones:** could have come a cropper there and troubleshooting that might have been a real pain in the butt. So, without thinking of that up front and choosing the correct HCT driver chip, yeah, we avoided a possible issue there. So, just something to watch

**Dave Jones:** out for. So, our HCT04 will easily take our 3.3 volt input and of course being a HC CMOS technology driver chip, it'll output the 5 volts cuz we're powering it from the 5 volt VCC here. Just tie the

**Dave Jones:** unused inputs here. That's just nice practice, just tie them high or low or whatever, doesn't really matter. And Bob's your uncle, that's pretty much our entire design. We've got our Wi-Fi module here so which we'll program in a

**Dave Jones:** different video. I've As for the power supply, I've just got a DC jack here on the thing, which is a 12 volt input because of course we actually need 12 volts to power our pile of poo. Don't blame me for the

**Dave Jones:** name, that's the name of the website where that high voltage module we saw in the previous one comes from. And we use a 1.1 K resistor here to actually set our output voltage as we said to 160 volts instead of 170 cuz we want that

**Dave Jones:** extra margin on the Nixie tube bias. And then I've just got a triple 1 7 could have used a 7805 whatever here to give us our 5-volt output. No worries power dissipation. Of course these are CMOS chips take bugger

**Dave Jones:** all power. So the only major power on the 5-volt rail is the Wi-Fi module here and I've had a look at the specs for that and it's not a huge deal. So we should only need you know a piddling

**Dave Jones:** kind of heat sink on this thing should do the business. So just a PCB heat sink will do the job. So as I said, I want this to be an internet enabled internet of things device shock horror internet enabled

**Dave Jones:** counter module so that we can display a counter from a any sort of website. So there's many many solutions here and sorry if I haven't used your favorite little internet of things Wi-Fi enabled widget. I'm using the WeMos D1 mini here from

**Dave Jones:** wemos.cc. Nice little module. I can buy this in stock in Australia on eBay for 10 bucks delivered. You know, it's like Anyway, it's fantastic. It uses the ESP8266E chipset. There's bugger all on it really. So it's got a little USB thing,

**Dave Jones:** little 0.1 inch header with 0.9 inch spacing here. So yes, I had to do my own layout for that because of course we didn't have ones. There we go. Just did my own symbol there. It took like a

**Dave Jones:** minute. It's like bugger all. I sort of you know got almost close to the right dimensions. I sort of guestimated a couple of things cuz it didn't have a dimension from here to here. I don't physically have one in hand, but it's

**Dave Jones:** going to be good enough from photos and other info I got that it was 0.9 inches across here 900 thou and you know, that's going to be good enough. No worries whatsoever. So we've got our PCB footprint for that. Um and once

**Dave Jones:** again, creating this sort of stuff is is not a problem. Like a schematic symbol takes a minute or two. PCB symbol takes a minute or two. I didn't do anything fancy with importing the 3D, you know, some sort of 3D uh step model and stuff

**Dave Jones:** like that, which you can do. If I was doing a serious board for production and for or for a client or, you know, a company I work for, a professional sort of board, then you go to a lot more uh

**Dave Jones:** trouble that and make sure it's exactly right and include the models. But this is just a one-off uh thing. I don't plan to take this thing into production at all. So, you know, you just slap it down and Bob's your uncle. So, you might be

**Dave Jones:** wondering, why did I choose this WeMos uh D1 Mini? I could have used any other solution out there, sort of Arduino solutions or um and by the way, this WeMos uh D1 Mini actually uh is compatible with the Arduino environment

**Dave Jones:** uh now. They've got like a some sort of wrapper layer that allows you to do it with the Arduino. I could have used absolutely anything on the market. A, it's cheap, readily available, but mainly because um somebody has already produced a library

**Dave Jones:** and everything for a pretty much uh what I want to um you know, a very similar application to what I want to do. So, I I don't want to reinvent the code wheel here um and A, I suck at sort of web

**Dave Jones:** programming. I'm I'm I'm I'm fine in like in just regular embedded C programming. That's no problem for me. But all this web-enabled crap, you know, I'm not I just want the thing to work. I don't want to spend any

**Dave Jones:** more time and reinvent the wheel. So, it turns out that 16-year-old um Joey Babcock here has on his website has uh created has put all this information here step-by-step of how to use the WeMos D1 Mini to um do very similar to

**Dave Jones:** what I want. So, brilliant. I'll just use that code. So, that's one of the reasons I chose the uh WeMos uh the um D1 Mini uh chipset. Why not? Um you know, so search for your If you've got

**Dave Jones:** an application like this and you want to spend the least and you want to get it up and running as quickly as possible, of course you're going to use a solution that already had that's already out there for you that's close to your

**Dave Jones:** application. So, I just need to download that code. Don't need to know any of the nuts and bolts about uh all the web programming and the APIs and all that sort of stuff. I just copy the code in

**Dave Jones:** and then start modifying it and that's by far the easiest way to get up and running. I should be up and running in, you know, tens of minutes with this thing, hopefully. So, that's the plan. So, that's why I chose the WeMos D1

**Dave Jones:** Mini. We'll see if it works. Now, you might think that we're actually done here and we are, but there's one more step which is called an electrical rules check and I actually uh was going to put that in this video, but I decided uh

**Dave Jones:** people might want to know about this separately. So, I've just uh branched that out into a separate video which should be uploaded at the same time as this one. So, check that out if you want to know about electrical rules checking

**Dave Jones:** in schematics. Basically, we're past a DRC as I said like the hidden pin thing before. You'll notice that there's no ground or VCC inside these things, but I could like go in here and then just uh show what uh show all pins even if hidden and

**Dave Jones:** you'll notice that there are actually some hidden pins in there. So, that's it. That's our schematic and uh hopefully that works and hopefully you you found that interesting. I know what has this been like half an hour of

**Dave Jones:** waffle or something like that, but uh you know, we've covered like uh done ERC and component layout and nice schematic design and you know, stuff like that and it looks like, you know, a nice layout. I haven't done anything fancy on here

**Dave Jones:** like, you know, engineering notes and stuff like that. I'm a big fan of adding like notes like of how to drive. I might, you know, add notes down here, maybe some, you know, info for driving pins or, you know, something like that,

**Dave Jones:** whatever, but this one doesn't really uh warrant that sort of thing. I'll show you a good one that I've done in the previous video. An example of that I've done in a previous video is my micro supply old micro supply project, for

**Dave Jones:** example. Look, I categorize things in nice neat groups and then I add little engineering calculations and notes all in there and little formulas and things like that for calculating resistor values and stuff like that. So, I could have done that here, for example, I

**Dave Jones:** could have added a little engineering note saying, "Hey, how did I calculate that 1K1 resistor there?" And well, without knowing, you you have no clue why I picked that. Is it important? If you're just looking at the schematic, I

**Dave Jones:** don't know. Can I whack a 1K in there? Well, no, you can't. You'd have to go look at the data sheet for the high voltage supply, the pile of poo supply, and it's actually quite a little complex formula in there to calculate

**Dave Jones:** the 1.1K to give you your 160 volts. It's a fairly critical value. It's not quite precise, but it's uh you know, near enough. So, something like that might warrant an engineering note, but yeah, you know. This is just a one-off, not too fast.

**Dave Jones:** So, we're ready to go. So, I'm sure in a follow-up video, I'll be doing the PCB for this thing and then we'll order it, then we'll assemble it, and then we'll program it, and we'll see the final application. So,

**Dave Jones:** I hope you enjoyed that and you found it interesting. If you did, please give it a big thumbs up and or as always, discuss in the comments or links to the EVblog forum or blog. Follow me on Twitter and I don't know,

**Dave Jones:** all that sort of stuff and hello to all my Patreon. Thank you to all my Patreon supporters as well. Catch you next time.
