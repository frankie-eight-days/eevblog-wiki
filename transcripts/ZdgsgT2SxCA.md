---
video_id: ZdgsgT2SxCA
title: EEVblog #1008 - Mystery Teardown
url: https://www.youtube.com/watch?v=ZdgsgT2SxCA
source: youtube-asr
---

**Dave Jones:** Hi, and welcome to a mystery teardown. Thank you very much for Eli Kaminsky for sending this one in. He's from Washington in the USA, and what it is is a defibrillator analyzer for analyzing defibrillators. Go figure. Specialized bit of kit where like you've seen these

**Dave Jones:** defibrillators. I've done a teardown, I believe. I'll link it in down below. Where you have the test pads like the chest pads where you put them on the sternum and the apex. Don't worry. I can put my hands over here cuz it's not

**Dave Jones:** going to generate a high voltage on this thing. It's designed as a load based tester device. Look, check it out. It's got a scope output on it. It's got RS232 serial output. It's powered from a 9-V battery. So, I'm not going to do any damage to

**Dave Jones:** myself, and it's done for by Dynatech Nevada and made in the USA, USA, and has pretty recent calibration, too. Let's check it out. Awesome. Cuz it's an analyzer, it doesn't need to actually generate the the pulses or anything like

**Dave Jones:** that. It just analyzes them coming from the actual defibrillator itself. So, it's got a real-time scope output, which will no doubt scope. Get it? So, this thing probably costs real serious money cuz it's a specialized bit of kit. Anyway, let's do

**Dave Jones:** a quick teardown. Like it'll just have some like sense amplifiers and stuff like that, I suspect. I don't suspect a huge amount of magic in it, but you never know. Let's go. There we go. Tada! We're in like Flynn. Oh, no,

**Dave Jones:** there's fair amount of magic. Oh, no. Oh, the big, of course. You need the big dummy resistors. WOW! The Dale dummy resistors. Check them out. Of course, you need those. Oh, what monsters. I've never seen one so big. That is ridiculous. Are these

**Dave Jones:** like a custom thing? 25 ohms, 1% made in Mexico. Hello to all my Mexican viewers. Oh, this is fantastic. And looks like it's an old design cuz we got old school dip roms by the looks of it. Let's go

**Dave Jones:** further. Oh, this is actually a really nice physical design. Look how the apex and the sternum uh mounts are just uh like have those uh PCB threaded inserts in there and then they're just uh screwed into the front like that.

**Dave Jones:** Absolutely brilliant. And of course, these uh binding posts up here as well go directly into the PCB. Really nice design. And as I said, like it's just going to be a uh sense amplifier here. Looks like we got a couple of uh sense

**Dave Jones:** op amps over here. Of course, I completely forgot about you need uh the big dummy resistors to dump all of the uh power into this thing. Now, we've actually got two in series across the apex and the sternum. So, we've got this

**Dave Jones:** one and then this one in series here. I can't remember the output voltage of a uh typical deep simulator, but wow, I mean, these are absolute monsters. Look at them. And then of course, you've got some uh secondary stuff here. It looks

**Dave Jones:** like these are all in a string configuration. Again, if you have a look here, um high voltage. So, it's basically just a high voltage differential amp. So, it's basically just one huge load across here, which is uh 50 ohms load right across there. Why

**Dave Jones:** 50 ohms? I don't know. Is that some industry test uh standard? Cuz it's not for RF reasons, that's for sure. Um you know, transmission line matching or anything like that. And then it looks like uh it just simply comes out here.

**Dave Jones:** And all these you can probably might be able to see the traces under there, but these are basically all in series. I'm not sure why they're alternating between these two different types of resistors here. Um, that's interesting, but

**Dave Jones:** they're obviously trying to get a high voltage uh resistor here, which then just drops it straight into there. So, like that's it. And then we've just got a differential amplifier and Bob's your uncle. Aha, upon closer inspection, these aren't in series. It doesn't like

**Dave Jones:** alternate like this one in series with that one in series with that one. It's uh these are regular axial ones in series uh together and look these ones I can't see cuz the PCB traces are on the bottom. So, maybe it's like got some

**Dave Jones:** intermixed um dual sense line or something like that. But yeah, it's just uh these ones here in series by looks of things on the top here. And as for the circuitry, all we've got here is an LF uh 442. That's a dual JFET op amp. We've

**Dave Jones:** got a couple of uh ICL uh just the CMOS op amps over here. We've got a 7660 uh voltage inverter cuz we've only got a single 9-V rail, so they're obviously generating the uh negative rail with that puppy. And that's basically all she

**Dave Jones:** wrote. And that's pretty much all I expected. There's something I didn't notice before. Look, a Fluke calibration seal. It must have been calibrated at uh Fluke's cal lab. Uh presumably, it's not like a Fluke uh product. So, yeah, but

**Dave Jones:** maybe they have the test facilities to do it. Uh that's probably like your regular cal house probably isn't going to do this. Oh, they might if you give them the procedure and everything else. I don't know, they might be able to do

**Dave Jones:** it as a custom job, but yeah, maybe Fluke just they have a house that just uh you know, know how to test these things. And I'm impressed by the uh shielding on the test board here. Look, they've got it both sides and

**Dave Jones:** what is that? It's like an insulating uh sheet, but I just haven't seen this like wood grain finish. So, it's really interesting material, but it's not uh elephant hide um or not elephant hide, elephant hide. Um it's not that, it's

**Dave Jones:** like some sort of like uh Formica like you'd get like on a benchtop. Interesting. They're obviously using it for you know, superb electrical uh you know, high voltage insulation. Um and it'd be chosen for a reason. Let's take

**Dave Jones:** a look at it. Wait, there we go. Everything's socketed on this thing. So, they thought about uh you know, repair of this thing cuz they probably make like dozens of these or hundreds tops or something like that. It's

**Dave Jones:** would not be a high volume product, but yeah, this is really old-school. Is there a date code? Yeah, date code of 1990. So, this thing is uh 27 years old. Wow. And it's your classic microprocessor architecture, RAM, your

**Dave Jones:** two ROMs. Uh so, it must be 16-bit. That'd be 8-bit each and our processor. What have we got? And the Hitachi fanboys go wild. HD630803 or whack in the data sheet. And we've just got a bunch of uh analog stuff here

**Dave Jones:** and looks like of course we need an ADC. What is it? Old-school stuff. National Semiconductor ADC1205 classic uh 12-bit ADC that'd be used on a microprocessor-based system because it's designed to hook into a uh microprocessor data bus. And curiously

**Dave Jones:** next to that, we've got an old-school DAC0830. Um 8-bit and DAC in this thing. So, I thought this would just sense uh the signals, but it's obviously using that to generate unless it's using it to generate some offset level or uh

**Dave Jones:** something like that. I don't know, but it might make sense that it's got some built-in uh self-test or something like that perhaps. Actually, I just found the uh user manual for this thing on the Fluke website. So, um I don't know.

**Dave Jones:** Maybe Fluke did offer it or something like that. Certainly not Fluke branded though in the manual or anything or on the device itself, but hi, check this out. I found this on the Fluke Biomedical Division page. It's a paper

**Dave Jones:** on human impedance variability and defibrillator test protocol. Why 50 ohm loads are not enough to test modern defibrillators. Remember the model what that we're looking at is 27 years old. So, you know, it's really ancient. But yet the Fluke Biomedical

**Dave Jones:** Division. There you go, that's why it had the Fluke thing on there. Would have been tested by the Fluke Biomedical Decalibrated by the Fluke Biomedical Division. And let's just go through it cuz this is fascinating stuff. I'll link it in down

**Dave Jones:** below of course. You can read it for yourself. Um But yeah, blah blah blah, why we have to do it. Um current not energy defibrillates. Uh successful defibrillation requires enough current to be delivered to the heart muscle during the shock. Must transit through

**Dave Jones:** the chest thorax and the impedance that represents. Uh body mass, skin resistance, tissue type and amount all play a part in the chest thorax impedance presented to the charge delivered by the defibrillator. Uh transthoracic, word of the day. Transthoracic,

**Dave Jones:** if I'm pronouncing it correctly, impedance equals the body's resistance to current flow. Typically the definition of impedance. Uh human impedance variability has been shown from vary from 25 ohms to 180 ohms. Reference down below. Um awesome. Uh energy in respect to impedance is a

**Dave Jones:** determining factor to successful defibrillation. So, that's why they you know, like 50 ohms just doesn't static 50 ohm load doesn't cut the mustard anymore. Um And age, disease, well, I'm getting older. My is my resistance going up? Probably.

**Dave Jones:** My resistance to is going up, that's for sure. Uh successful defibrillation requires sufficient current to the heart muscle, blah blah blah, trans thoracic impedance, and schematic and formula. Brilliant. Look at this. Um And there you go. There's a 300 joule at

**Dave Jones:** 50 ohm millisecond pulse typically like it does it over 8 milliseconds as I think we've shown in a previous video. That's a monophasic waveform the typical two electrode approach that you get on most defibrillators. Like if they have

**Dave Jones:** you up in a hospital or something they might have you know more but you know you see it in the movies the paddles. You know. Um you never see them put them in the right locations. It's like just across

**Dave Jones:** the it's Hollywood anyway. Uh how defibrillators account for human impedance variability. Uh yes cuz they they now do the biphasic waveform and supposed to account for all that sort of stuff. And I've looked at these in the previous and then you can get the pulsed

**Dave Jones:** biphasic which is the Schiller. Good on you Schiller obviously named after the person who founded that one. Uh the pulsed biphasic waveform low impedance delivers more current than required exposing patient to potentially harmful high peak currents. Average impedance depends on the

**Dave Jones:** on the person. So they've got to knock it back. Anyway. There you go. 50 ohm test loads enough to ensure output conditions in modern day defibrillators. Do all of hospital patients have THE SAME IMPEDANCE? NO. TESTING BEYOND the 50 ohm load is

**Dave Jones:** necessary to ensure defibrillator. There you go. No doubt they have recommended test devices. These days Oh there you go. There is an IEC standard. There you go. Refer it to be tested at different resistances. Ta-da. 25 through to 175

**Dave Jones:** ohms is the modern standard. So this one is no good even though it was what last calibrated very recently. 2013 was it? Anyway, it might have been good enough for you know some old gear or something. Brilliant. Selectable load accessory of

**Dave Jones:** course. Fluke sells a selectable load accessory the Impulse 7010. There you go. Um so, I maybe Fluke Biomedical bought out this company um cuz they're using the Impulse name. So, uh there you go. So, interesting. That's the modern

**Dave Jones:** one. There's all the references for those playing along at home. Beautiful. Anyway, um let's power it up because the DAC inside this thing does generate some uh cardiac test waveforms, which presumably will come on the scope output. So, let's give it a whirl. So,

**Dave Jones:** we switch it on here and whoop, firmware? Yeah, I don't know if we've got the latest firmware. We'd have to get out the old EPROM programmer and the UV eraser. Um somewhat curiously, we go into uh perf for performance. So, it

**Dave Jones:** generates performance waves uh performance waveforms, and we can do an auto sequence, or we can go into manual here, and well, we don't want a zero output, do we? No, bugger that. Um there we go, 240 beats per minute ECG. There

**Dave Jones:** you go, a 2-Hz triangle, 1-kHz sine, just various test signals from that 8-bit ADC. 4-second pulse, 2-second square zero out. There we go. Let's do a 240 beats per minute wave. So, I can measure like energy, peak energy of the pulses

**Dave Jones:** and things like that, and you can test it's set up for 100.5 J, which might be a standard uh defibrillator output. And it can do auto sequence testing on uh various pre-programmed uh products and things like that. So, presumably, you can you

**Dave Jones:** know, there's a blank one in there as you saw. You could do that, but you know, like a whole bunch of stuff specifically related to um vent like ventric- like cardiac terminology. I don't know. You'd have to you know, normal sinus uh waves.

**Dave Jones:** You'd have to go through like uh the manual, which I'll link in down below, and just to see what this thing's capable of and how you use the external uh terminals and stuff like that. We're not too interested in the operation of

**Dave Jones:** this thing. Just let's just say it's a comprehensive bit of kit for doing pretty much any testing on a defibrillator. We'll have to open up the damn thing again to get into it to probe it because I didn't have the

**Dave Jones:** like a phone um output to scope like I just like well, I could probably cobble one together somehow, but it is easier just to open it again. But, I don't seem to be getting an output though. Unfortunately, so this thing might depends maybe why it

**Dave Jones:** was tossed or whatever. Um it may be cactus like the output amp I think here that little metal can package down in there I think it's the output amp. Um so yeah, it's just supposed to be outputting a waveform and it's not.

**Dave Jones:** Well, I had to go all the way back to the DAC over here and I found a DAC test point that I could use and tada, there it is 240 beats per minute. But, look at this. Isn't this a crusty

**Dave Jones:** waveform? You can see the You can see the 8-bitness of it. Let me zoom into that. Look at that. Oh, that's terrible, Muriel. I mean, that's not even 8-bit resolution. That's just generating like I like how many bits is that?

**Dave Jones:** Like five? Ridiculous. But, hey it's going to be good enough for a test waveform. This test waveform's designed to test like a monitor outputs and stuff like that. So, like you know, cardiac waveform monitors and things like that. So, we can

**Dave Jones:** change that, too. And there's our sine wave. That's not terrific. And even down at 30 beats per minute, we don't get anything better than that. So, like that could be like a function of like how fast the processor is

**Dave Jones:** operating. You know, they went we only need something near enough and it's not going quick enough and they just want to output the bit I They at least got an 8-bit DAC and they couldn't use it. It's just hilarious.

**Dave Jones:** They'd all have to be tested out the factory. They'd have to be field tested if you're doing these things properly. Some people just buy them and when the day that they put in there in situ wherever it is in the public space or

**Dave Jones:** whatever or the office and then once they expire they might they toss them out or they might get them refurbished and they might use this bit of kit to refurbish them, put a new battery on it, retest them, stuff like that. So,

**Dave Jones:** obviously 50 ohm dummy load is a standard that's 95 W. So, that's almost like 190 W dummy load there and they just got some high voltage sense lines going off to a differential amp and that's that's pretty much it and then they're

**Dave Jones:** just analyzing it with a 12-bit ADC because cardiac waveforms aren't anything you know particularly high frequency so you can just use a you know an old school 12-bit microprocessor ADC in there operated at bugger all. I don't know what you'd probably only need like

**Dave Jones:** a kilohertz sampling rate or something like that. Nothing terribly high at all. So, that's a real interesting specialized bit of kit and probably cost and you know pretty penny no doubt. So, thank you very much Eli Kaminsky for sending that

**Dave Jones:** one in. It's really interesting. It still works. It probably you know it's got fairly recent calibration on it and what good is it? I it's a dummy load for testing the ECG for testing defibrillators. So, if I ever do another

**Dave Jones:** teardown of a defibrillator and I have a working one then I can might be able to dump it into a load here and see what happens. But yeah, anyway it's not like this is only designed for pulse load. Of

**Dave Jones:** course it's not you know not dissipating 90 190 W continuous. It's just designed for pulse load applications but it's really nicely designed. I like that. So, if you like the video please give it a big thumbs up. And if you like mystery

**Dave Jones:** teardowns, give it a big thumbs up, too. Catch you next time.
