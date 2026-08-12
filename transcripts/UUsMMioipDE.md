---
video_id: UUsMMioipDE
title: EEVblog #240 - Power Supply Design Part 8
url: https://www.youtube.com/watch?v=UUsMMioipDE
source: youtube-asr
---

**Dave Jones:** Hi, just a recently quick video on the power supply design series again. I wasn't going to do this one, but I thought well, while I'm troubleshooting this thing, I might as well turn the camera on and give you a look at it.

**Dave Jones:** Now, yes, I'm up to the PCB. Here it is. I've built the thing up and if you've been following me on Twitter and the forum, you'll know I've been having a whole bunch of issues. It's taken me a

**Dave Jones:** couple of days to get this stupid thing running because of the stupid Arduino software and the Arduino interface and the AVR studio and the AVR micro. Anyway, I won't go into it. It's a whole other video. Anyway, it's been frustrating,

**Dave Jones:** but beauty, I've got it working. I've got the LCD working. I've got the pots working. I've got the switches working. Everything's sweet and looking good. But now I'm starting to talk to my DAC. And as you know, it's an SPI DAC. It's a

**Dave Jones:** It's a and it's a software interface. It doesn't use a hardware SPI interface on the AVR micro. It's a software interface. So I wrote my code based on the data sheet bit banging the serial port. Cross my fingers,

**Dave Jones:** stuck my tongue at the right angle and what do you know? It didn't work first go. Go figure. Murphy. So I thought I'd just turn on the camera while I'm troubleshooting this thing and we'll take a look at it. Let's go.

**Dave Jones:** And for those playing along at home, there was a small error in my schematic, too. This is the rev 1 schematic and of course I had it correct because I breadboarded the thing and the ADC I out is going to the non-inverting input of

**Dave Jones:** this op-amp here. So that's the output from my current sense amplifier. So it's going to pin 5 there. But what? On rev B here, I've got it going into pin 6. Fail. The reason that happened is because when

**Dave Jones:** I was re-jigging this uh you know, making it look pretty. I was moving things around, dragging, cutting and pasting, and those lines obviously got moved, and I put them back and accidentally swapped them. Oops. Trap for young players. And of course, the

**Dave Jones:** ERC checking in the these types of uh CAD programs aren't magic. They can't cater for fires up in the gray matter. Doh. All right. So, this is what we're going to take a look at in in this video. My DAC isn't working here. I've

**Dave Jones:** got my SPI bus on the input, which as I said is a software SPI bus. It doesn't use the hardware uh interface bus. So, I'm writing my own library for that because it's so incredibly simple, and I show you the code in a minute that

**Dave Jones:** actually does it, but it's not working. And it could be something incredibly simple. I probably done something dumb in software. Maybe there's a hardware fault building it. We won't know until we track it down. I think it's most

**Dave Jones:** likely to be uh you know, I've done something uh dumb in the Arduino uh driver software for this SPI interface, and it's just not uh talking, but let's just check the hardware pinouts. Analog VSS is ground as it should be. VDD, and

**Dave Jones:** I've checked these voltages. They are 3.3, ground, uh Vref on the inputs. We'll have to check those. Uh L DAC, the uh that's the load output. Now, the data sheet specifically says you can actually tie that low and then rely on the

**Dave Jones:** positive-going chip select at the end of the data sending the data to actually latch the internal data that you send from the SPI through to the analog uh output here. And that's it. It's a pretty darn easy uh chip. It's not in

**Dave Jones:** shutdown mode because that uh that shutdown pin nine there is connected high, so it's an active low shutdown. So, all right. Everything should be working. So, we've got to check our um chip select. Make sure our chip select's

**Dave Jones:** working. Might have to get the logic analyzer out for this one. We can probe it with the scope first to see if it is a protocol issue, we'll have to get down into the logic analyzer, get down and

**Dave Jones:** dirty and take a look. But basically, I'm getting zero on the output here. I'm changing my input voltage as we're seeing and getting nothing. So, let's try and debug this thing. All right. So, here's my board here and I won't go into

**Dave Jones:** details. I'm going to have a whole video on how I designed the board, how it fits into the case, and all the system engineering that goes into that. So, don't worry about that. That'll eventually come. And we're just doing

**Dave Jones:** debugging today. And here's the LCD. It's a my uh Newhaven uh display with the RGB LED backlight I haven't hooked up yet. It's a 20 by 2 instead of the more common 16 by 2, which is really good. And uh I've got it so it um has

**Dave Jones:** the set output voltage and the set output current here. And then the measured output voltage and the measured output current here. This may change on the final interface, but I reckon that's pretty good interface. And my knobs work. Check it out. There's my voltage

**Dave Jones:** control uh knob there. My rotary encoder works just fine. It's jumping up in 10 mV steps at the moment. And the current limit can also jump up in 1 mA steps like that. And uh this is all working in code so that

**Dave Jones:** this value, at the moment, what I'm trying to do is send uh this uh milliamp value directly it out to my uh DAC here. This is my DAC. And uh I'm getting no output value at all. So, I'm trying to

**Dave Jones:** that uh value's already in memory and I'm trying to shift it out through the SPI bus. And well, it's just not working. So, uh we're going to have to look into it and see what's going on. Now, now what I've got here is I've got

**Dave Jones:** an Arduino Duemilanove, if that's how you pronounce it correctly. I've actually removed the chip. And what I'm doing here is I'm just using this as an FTDI interface. If you've been following my Twitter and uh forum uh things, then

**Dave Jones:** you'll know I had to do this because I couldn't find my other interface. So, basically, I've got my reset line, my transmit and receive, and my ground uh using this as a basic um FTDI interface to the Arduino IDE environment. And it's

**Dave Jones:** working uh just fine. And with the bootloader here, I've got an ATmega328 AVR chip on here, exactly like what's on an Arduino Pro. And this serial interface is also exactly the same as the Arduino Pro. They I've got to fix

**Dave Jones:** the pin out for the reset line, but apart from that, uh it is an identical interface. So, I've programmed the bootloader firmware on my PSU board to be exactly the same firmware as what is on an Arduino Pro board. So, as far as

**Dave Jones:** the Arduino IDE is concerned, you just set it to talk to one of these uh genuine Arduino Pro boards, and it doesn't know the difference. It'll talk to my power supply board instead. Beauty. All right, one of the first

**Dave Jones:** things I want to do is uh just compare the data sheet pin out against what I've got on my schematic here, just to make sure there wasn't an issue with uh the pin out in my uh library compiler for

**Dave Jones:** that, and that looks sweet. So, I don't see any issues there at all. So, and um because I've done a DRC check between the schematic and the PCB, I know the PCB is going to match the schematic. So,

**Dave Jones:** it should be sweet. All right, the next thing I'm going to want to do is uh just uh check a few things. Uh just check pin one here. That's my VDD. That's uh 3.3 V. It's 1 V per division. Not a problem

**Dave Jones:** at all. Um I've already checked the uh VREF voltage. That's uh 2.0 V and that 2.048 V. So, that's pins 11 and 13. There it is there. And uh check pin 11 as well, cuz there's two separate voltage references for both um A and B

**Dave Jones:** voltage outputs, and they're working just fine. And the ground is connected. So, really, that leaves the um SPI interface. So, let's do pin 8, which is the low DAC. That should be low, and it is permanently low, so the

**Dave Jones:** data sheet says we can do that. The shutdown pin, pin nine, should be high because it's an active low shutdown, so the chip is not shut down. Beautiful. Right, let's take a look at the chip select pin because my software here, I

**Dave Jones:** don't have to actually do anything. It's continually updating and sending the latest current data as you saw on the LCD, sending that value through to the DAC. So, let's probe pin three here, which is the chip select, and see if we

**Dave Jones:** get anything. Bingo, there we go, we do. We're getting uh how much worth of uh 5 milliseconds per division, 5 10 15 milliseconds um sounds okay for sending all that data. It's an active low chip select, so clearly that's working

**Dave Jones:** because um that was an issue because um well, that uh may have been an issue because that was going through my I squared C IO expander. So, if my I I squared C IO expander wasn't working, then the chip select for the DAC

**Dave Jones:** wouldn't work, and so on. If you're following the schematic along at home, you'll know what I'm talking about. So, um let's check the data in, pin five. Bingo, we're getting data. Not a problem, and that data should change if

**Dave Jones:** I change the pot. Yes, it does. It's It's not uh it's not terribly uh stable there, but you can see that the uh trigger changes, but you can see that data change as I change the pot. The pot is still, and

**Dave Jones:** bingo. So, no problems at all with the data. And um you you don't really um sometimes if you don't have a scope available with you, you can use a uh just a standard logic probe, old old school logic probe to see that your

**Dave Jones:** data's actually transitioning here. Um but, it's handy with the scope. You can actually see the data. And well, it's looking like we may have to get out the logic analyzer because uh let's well, let's check. I've I've got

**Dave Jones:** one line left, which is pin four, which is the uh clock line. So, let's go to pin four here. Aha! Uh there you go. That's the culprit. Pin four's not working. There's no clock. No wonder I'm getting no data out of my DAC.

**Dave Jones:** Dull. Dead easy. All right, let's fix that. So, there's nothing getting to pin four of my DAC. Well, is it coming from the output of my uh AVR chip here? Because there could be a break in the PCB. There could have been

**Dave Jones:** an etching fault. I doubt it. It comes from my new New Zealand uh supplier. It looks first-class quality, Circuit Labs in New Zealand or um pcbzone.net. They're This board is manufactured in New Zealand. I might give you a closer

**Dave Jones:** look at that later, but let's check this pin here, which is the output of the AVR. No, it's exactly the same on the scope. So, what? Fail. So, what I want to do here is check my SPI clock here, pin 26. It

**Dave Jones:** is actually the uh ADC3 input or A3 input. So, if I go to my Arduino code, let's uh check out to see if that's actually correct. And there it is, SPI SClock A3. And the others work. I've defined that pin, and

**Dave Jones:** we can go down and check it further down, but I don't know. That should work. Hmm, now if I have a look at my DAC send routine here, I've actually defined the DAC clock toggle here. I've actually defined

**Dave Jones:** that as an operation where the SPI clock goes high, and uh I added this delay extra while I was trying to debug it without a scope before, and then uh digital write low. So, it's supposed to So, every time I call call DAC clock

**Dave Jones:** toggle, it's supposed to go high, and then delay for a millisecond, and then go low. And well, it's not doing that. So, I don't know what you know, I'm calling it a whole bunch of times throughout here that clock toggle and it

**Dave Jones:** doesn't like it at all. And here where I define my pin mode, there it is SPI clock is an output, not a problem at all, just like the SPI data. So, it should be working. I'm not sure why.

**Dave Jones:** Very puzzling. And I'll just double-check the Arduino Pro schematic. There it is, ADC3, pin 26, A3. So, that's the pin I'm using. Why doesn't it work? Well, what do you know, I found it. Look, silly naming thing which the

**Dave Jones:** Arduino environment didn't pick up because it already has names registered. I defined here SPI SCLK, but if you go down the bottom here where I define where I actually do the output here, SPI clock, not SCLK. There's no S in there.

**Dave Jones:** So, the Arduino didn't pick that up because SPI clock must be defined somewhere else, maybe in like an internal library or something like that. So, yeah, if I change that to SPI SCLK doll and have I goofed up the

**Dave Jones:** routine up here as well? SPI clock. Yeah, there we go. Let's change that to SPI SCLK, SPI SCLK and that should be sweet. We don't need that 1 ms delay in there, that debug delay in there anymore. And let's compile and

**Dave Jones:** download that and see what happens. So, it's compiling the sketch now. And I'm using 7.3 K of my 30 K already, which isn't too bad at all, I guess, because I'm using some S printf stuff, which adds about 1.7 K or

**Dave Jones:** thereabouts. And it's done uploading, and let's give this a go. And tada, there it is. There it is. Not a problem at all. Awesome. So, it should be fixed if I stick my multimeter on the output of that DAC, um assuming

**Dave Jones:** that I've got my algorithms correct um for my SPI serial interface, then I should get the exact value out I expect. All right, let's check a couple of things. Let's check our voltage reference for starters. There you go,

**Dave Jones:** 2.049 should be 2.048. Near enough. And let's uh adjust our um our current output pot here. As you can see, it's zero, so let's measure the output. Let's probe the output pin, which is pin uh 7 8 9 10,

**Dave Jones:** I believe. Currently 0 V. And What? No. Nothing. What's going on? Bummer. Yeah, and I just checked the other output, too, just in case I didn't get it wrong in software, but no. Nothing. What's going on? This is hopeless. It

**Dave Jones:** should at least be outputting We saw that data changing as we changed the pots, so there's some data going into it. So, unless I've screwed um something in the Well, I've obviously screwed something in the software. Something's going on because um all

**Dave Jones:** we're getting all the signals on the SPI bus now. So, well, I think it's time to crack out the logic analyzer. Now, what we're going to do is have some fun with our Agilent 3000 series with the building logic analyzer capability in

**Dave Jones:** here and the serial triggering because it can uh do SPI serial bus debugging. You don't have to have a fancy mixed-signal scope like this. You can do it with a cheap simple PC-based USB logic analyzer that supports these

**Dave Jones:** serial uh decodes. And we can change the number of bits here, and we can do all sorts of things and we can set up our uh trigger. I'm triggering from the SPI uh bus at the moment as you can see. We can

**Dave Jones:** trigger off all sorts of things and we can trigger off two different types of serial buses and it's really is quite neat. But we can go into trigger setup and once we get all this set up, we'll be able to trigger off this SPI bus and

**Dave Jones:** see exactly what's happening here. We don't have to do this. We can actually just single shot uh capture this thing using the regular um scope if we want. Um but it just it'll be nice because it'll give us our data uh decode here

**Dave Jones:** and we can see that the data will actually match what we're sending in our software. Now what we want to trigger off here, we want to trigger off um uh MOSI, master out slave in, because our AVR is our master and the it's

**Dave Jones:** sending data to the slave in. We're not actually using the fourth channel um MISO because we're not actually retrieving data back out of this DAC. We're only sending data to it. So we only need the three signals. So we can

**Dave Jones:** just ignore the fourth one. Now I haven't actually done um SPI debugging on this scope before and I'm not sure why it only offers um to trigger off the data. It doesn't offer you offer you to trigger off the uh clock or the chip

**Dave Jones:** select or anything. The chip select would be um a nice one to trigger off. So I'm not sure what's actually going on there. Pretty happy with that. I love that it gives you the waveforms and stuff like that here. It's really nice.

**Dave Jones:** This we don't want to trigger off the MOSI data because it it's actually a data pattern which is why it's not actually uh triggering at moment. I'm doing I'm press start single shot and it's still sitting there waiting for the

**Dave Jones:** trigger. So that's no good because we don't want to trigger off a bit of data. I want to actually trigger off the uh chip select or something like that. Instead of um the SPI is just the data. It only gives you the options for the

**Dave Jones:** data. So we don't want that. We want to actually trigger off an an edge for one of the uh source channels and here's where you should label them. So that instead of having 1 2 3 4 like that, you

**Dave Jones:** should actually go to the effort to label them but ah, I'm not going to bother today. Um and we'll trigger off the chip select. Of course, our chip select is channel four here and the threshold voltages, they're all okay. So

**Dave Jones:** let's go back into our trigger menu here and we want to trigger off channel four like that. Bang, which will be our chip select. So there we go. Captured it single shot mode. Bang and there's our data. Ah,

**Dave Jones:** beautiful. Let's single shot capture that and as you can see our chip select is the top trace up here. Uh this is our data and the yellow one down here is our clock and if we scroll along and zoom

**Dave Jones:** into that, you'll notice that the chip select is actually a long way past here because to do the chip select, we're using the I squared C bus. So our software has to actually send during this time, it has to send a command

**Dave Jones:** through to the I squared C bus to actually switch it on and that's 200 microseconds per division. So it's roughly taking, you know, 200 400 600 800. It's roughly taking 1 millisecond to actually send that command before it

**Dave Jones:** gets through to change the chip select high and um I don't know if that is actually an issue. Maybe that time there to set the chip select back high is causing the DAC. I don't know. I'd have to read the data sheet but let's go in

**Dave Jones:** and we can actually examine the data in here and as you can see, it hasn't actually decoded individual data here. It's just got B611. It hasn't actually decoded our data like I wanted there. So maybe I haven't set the thing up

**Dave Jones:** properly yet but there you go. There's our data and our chip select sorry, our our clock here. The data should be stable when it transitions. So, when it clocks high here, then uh that is going to read in a

**Dave Jones:** one from the data. When it clocks high here, it's going to read in a zero. 1 1 0 1 1 and well, this pretty much matches up with the data sheet precisely. And there's the timing diagram for our data

**Dave Jones:** sheet. So, as you can see, uh chip select, where that goes low first, which is exactly what we got on the scope screen. And then, uh the positive um edge of the uh S clock here is where is

**Dave Jones:** smack in the middle of the data byte, which is where it samples at. And it's sending out 16 bytes uh 16 bits uh total, regardless of whether or not it's a 12-bit uh DAC, the 10-bit DAC, or the 8-bit DAC.

**Dave Jones:** Um it just If you scroll down here, you'll see that the good thing is, it's totally software compatible. You just ignore on the 10-bit DAC, it ignores the last two bits over here. And you go down to the 8-bit DAC, and it simply ignores

**Dave Jones:** the last four bits. It's great. So, you can um completely software compatible. You can just plug in an 8, 10, or 12-bit DAC and just send out the data cuz it'll ignore those least significant bits. Oh, I think I figured it out. I'm only

**Dave Jones:** sending 14 bits, not the entire 16. I'm missing out on the last two bits. I wasn't sending them cuz I can be I decided to only um send 10 bits uh worth of data because it matched up with my

**Dave Jones:** output vol- output current correctly and stuff like that. So, uh oops. Duh. I got to fix that in software, send the extra two bits. And presumably, it's waiting for those. So, that's why I'm getting nothing out. So, there you go. I've added in uh two extra

**Dave Jones:** bits here. I've set them both to hardcode them both to zero because we're only sending out 10 bits worth. So, I'll upload that, click on upload, and in a few seconds, it uh should output on my little board here. So, hopefully, um

**Dave Jones:** that's all the problem is. We'll find out in a sec. Okay, I won't even bother uh re-triggering the uh data over there to see if I've got uh 16 bits. I'm pretty sure I will. And so, let's um

**Dave Jones:** increase our current here and see probe the output. Ah, bingo! Bingo! There we go. I knew it. I knew it. There we go. We're getting our output voltage. Fantastic. There you go. So, it looks like that DAC did not like um being two

**Dave Jones:** bits short. It just didn't recognize it as a valid command. Now, curiously, this is supposed to be one bit per millivolt uh output, but I'm not getting that. I'm getting I'm I'm sending 100 uh milliamps here and I'm getting 200 millivolts out.

**Dave Jones:** And that basically, if you increase that, it actually is two times. So, I wonder if I've got There is a two times amplifier in this thing. So, I wonder if the bit for that is set incorrectly. Well, what do you know? There we go. I

**Dave Jones:** didn't read the data sheet correctly. The output gain is actually always referenced to 4,000 and uh 96 or the output voltage is always referenced to 12 bits regardless of what device you use, whether it's an 8, 10, or 12-bit

**Dave Jones:** one. Although we're trying to do 10 bits in this case, it's always referenced to D on 4,096. And it And it does have two uh gains there. And I'm actually sending out a one uh for GA here. At least

**Dave Jones:** that's what my um That's what I programmed in in my Arduino software. So, we're using that formula there. So, there's two things that are wrong here. One is that I'm using the wrong gain. I'm going to need the two times. And

**Dave Jones:** I've got my bits uh shifted. I'll show you the code in a sec. I've actually got my bits all on the high side. I need to shift them towards the low side. You know how I added those two bits on the

**Dave Jones:** least significant digits. I need to add them on the most significant digits. Doh! So, what we want say if we're feeding a 100 from our you know, 100 million amps, which will be a value of 100 directly in the internal register, then

**Dave Jones:** we want to divide that 100 by 4096, okay? And then we times it by our voltage reference, which is 2.048 volts. Bingo. So, I got to give us 50 millivolts. We want that to map to 100, so we want to use the times two

**Dave Jones:** output. So, let's change that around and we'll find it'll work precisely the way we want. These sort of things always happen first go when you don't engage your mind before you write the software. I just whacked it in there and asked

**Dave Jones:** sort it out later. She'll be right. Right, so in our routine here, up here, where we've got output voltage gain select times one, we want to change that to times two. So, we want that to be a low and we want

**Dave Jones:** we have to shift all this data here so that uh we're shifting the 10 bits at the top, so we'll send Let's go home here and we'll Oh. We'll copy these two bits we've got down here. We'll copy those and

**Dave Jones:** we'll put those right at the start here. And bam, that should do it. Let's download and try it again. All right, let's probe the output here. We've got 0 milliamps there. We get zero on the output. Well, we're actually getting 1

**Dave Jones:** millivolt there, but you know, it's down in the noise, so let's shift it up by one. Wait, it doesn't go anywhere. We're down in the noise, but let's say take it to 10 and no, no, we're not quite there. We're

**Dave Jones:** 5 millivolts, so we're still down in the low range, but we should find let's go up to 100 milliamps, we should find that to be uh it's a it's a bit off, 96, but there you go. It is actually

**Dave Jones:** mapping, and we're mapping at 500 milliamps, too. It's slightly low, but if we go up to a volt, we'll find that one will map as well. And it does, but we are once again uh about uh 5 millivolts or 5 milliamps short. Now,

**Dave Jones:** the interesting thing is is that our reference voltage here is uh 2.0493 volts, and that's well within our spec. The spec of this voltage reference is 0.25% and 0.1% um of 2.048 volts is 2 millivolts. So, we're well under 0.1%

**Dave Jones:** there. So, really um that doesn't explain a 0.5% discrepancy or 5 millivolts in a thousand on our output. Strange. This meter's bloody annoying, by the way. Keeps auto switching off even though I'm using the damn thing and measuring stuff. Crazy. Now, um I'll

**Dave Jones:** just probe directly on the pins of the DAC to make sure that we're getting I've set it for 500 here, and we're getting still getting in that 5 millivolt uh differential there. Not that there was any major current flowing through

**Dave Jones:** here anyway, cuz I was probing on on the other side of the board before. You just have to be uh careful of that that you're not getting a voltage drop there, but that's directly on um the uh pins of the DAC. And the same thing

**Dave Jones:** with the uh reference voltage, I'm measuring directly on the input pins, and once again, it's still the same. There was no drop elsewhere, as you'd expect, 2.0492. Let's have a look at our raw data here. If we uh start out here, here's the bit,

**Dave Jones:** okay, at the first that first transition there. So, it's 000 111110 100. And if you convert that to decimal, that's 500. It's exactly what I'm feeding in. And if you plug the actual values into the formula in the data

**Dave Jones:** sheet, the actual voltage reference we're feeding in 500 / 4096 * the voltage reference 2.0 493. We actually should and then multiply by two for our internal gain amp, should get precisely point 5003 V out, but we don't. We actually get

**Dave Jones:** 495. Okay, now what I've done is changed the software so that it also outputs it on the other channel, too. And there's the other channel. Got to set to 500 again, and we're getting 497.3. And the original channel we had, the

**Dave Jones:** same data, uh sending to both, 495.1. Now, if we have a look at the data sheet here, this gain error is typically -0.1% of the full-scale reading, not including the offset error, which can be up to 20 mV

**Dave Jones:** at the low end, but it's a maximum of 1%. So, it's pretty horrid. And if we actually disable that * 2 gain amp, I've got a 1,000 mA, so we expect 500 on the output, and let's check it out. That's

**Dave Jones:** the uh channel That's the current channel output, 497.7. So, it's still not still not there, and 499.0, which is better, but it's still not spot-on. So much for our precision DAC. Well, I don't know. It's not that great. I

**Dave Jones:** expected a a bit better than this. So, I think what I'm going to do is try the an actual 10-bit version of this DAC and see if it's any better because it scales up for the cuz we're only using the lower 10

**Dave Jones:** bits in this 12-bit DAC. So, we'll see if it performs any better by getting the actual 10-bit version. So, stay tuned. But wait, I've got a couple of more chips. Let's try it out and see if they're any different. All right, here

**Dave Jones:** we go. I've got it once again set to a gain of one still. So, that's 500 milliamps there. We should expect 250. So, I've got a another chip in there. It's the same chip. It's still the uh MCP4922. Let's measure the

**Dave Jones:** output. Ah, look at that. 253.9 millivolts. There you go. 200 254 millivolts. And let's check the other channel, which has exactly the same number. 248. Look at the discrepancy. First channel, 246.5. The other channel, 253.0. There you go. These specs on these

**Dave Jones:** things are as loose as a goose. But hey, there you go. MCP4922 integral non-linearity error plus typically plus minus two least significant bits can be as much as plus minus 12 least significant bits, which is you know, pretty much what we're

**Dave Jones:** seeing there. So, it's certainly not meeting its typical figures. So, I guess I can't be too harsh on this thing, you know. It's It's certainly It does meet its specs. It's just you know, I was hoping for spot on.

**Dave Jones:** It's a 12-bit DAC. That's what you expect. But anyway, I might see if I can pick up some MCP4912s here and see if they perform any better cuz really probably don't need a 12-bit DAC on this thing. It's a bit overkill.

**Dave Jones:** I think I'll just go for the 10-bit DAC and I'll pick some some of those up tomorrow from Farnell's. Hopefully they've got some in stock. They may or may not. I'll have to check. Anyway, I hope you enjoyed that.

**Dave Jones:** That's a bit of DAC debugging on the new power supply. I'll catch you next time. Now, just as a little aside, I thought I'd show you this on the I2C bus that actually drives the LCD. It also drives

**Dave Jones:** those I2C decoder IO chips, but this is an actual problem with the LCD display I'm getting. I This is our SCL our clock and this is our SDA our data. Look at that little runt pulse in there. Check that out. Now, I've got my

**Dave Jones:** scope set up to trigger on the start condition. I'm using serial protocol triggering here. So, let's trigger on the start and let's capture that and bam, let's Hang on. Let's do that again. Let's There we go. That is the data

**Dave Jones:** going onto my I2C bus and this is probably the decoder over here, but this is the LCD. Trust me if I've looked at this before and it's rather interesting. Look at that. It's almost as if there's a bus Well, there is some sort of bus

**Dave Jones:** contention there that is actually causing that thing cuz it's not supposed to be a tri-level bus like that. It's only supposed to be two levels data, one and zero of course. It's digital, but we're not. So, it looks like there's actually some

**Dave Jones:** contention caused by the LCD and trust me I've isolated it down. It's not the other I2C chips. They haven't got the same address or anything like that. Trust me I've isolated it down and it is the LCD and

**Dave Jones:** it's not actually my code doing that either cuz I originally wrote my own LCD driver code from scratch and I got this result and I thought it was funny. I thought my code was doing something weird even though I copied it directly

**Dave Jones:** from the data sheet of the LCD manufacturer and I thought okay, it's the Arduino the one wire library has been giving me troubles. Maybe there's an issue there and that could still be it but I downloaded somebody else's

**Dave Jones:** code. I searched around sure enough the Arduino had a library for my exact New Haven LCD display and even using that I get the same data and but the LCD works. So I haven't really looked into that in detail but

**Dave Jones:** so I'm not sure either if it's the one wire driver doing something funny or it's the LCD actually doing something and dragging the bus down when the driver is trying to do something but clearly there's a conflict there and

**Dave Jones:** well at this stage I'm not going to look into it cuz my LCD is working. I'm happy with it. So I'll have to leave that fight for another day but that happens even on the library that's already out there for the

**Dave Jones:** New Haven display. So something going on there. Catch you next time.
