---
video_id: hMBbnWjbUAU
title: EEVblog #1054 - How an Analog PC Joystick Works
url: https://www.youtube.com/watch?v=hMBbnWjbUAU
source: youtube-asr
---

**Dave Jones:** Hi, in the previous video, we took a look at the classic IBM PC Junior computer and how it was a big flop back in the 80s and I'll link it in down below and at the end of this video if

**Dave Jones:** you haven't seen it. And one of the things I briefly mentioned in the teardown of this is how the game port joystick controller circuitry actually worked. When I was tearing down the PCB, we saw a 558 timer in there.

**Dave Jones:** And I explained that this was quite common back in the day, but I thought we'd take a deeper look at that cuz it's rather interesting how this works, I think. It's rather clever. So, let's take a look at the classic analog

**Dave Jones:** joystick. This is the original IBM joystick from back in the day. IBM didn't actually I don't think they actually made this cuz the original IBM PC actually didn't come with a joystick or a game controller port as it was

**Dave Jones:** called back in the day, but you could actually buy a plug-in card which actually was just the game controller PC card and that became the de facto industry standard joystick interface for the PC from then until the end of time

**Dave Jones:** until like USB joysticks took over. So, they lasted a long time this game controller joystick interface and it started out just as that single plug-in peripheral card which could control two different joysticks through a D15 connector and a Y splitter cable. But of

**Dave Jones:** course, that took up an entire slot in your PC and well, dedicating a whole slot to a game controller kind of sucked. So, eventually these multi-combo IO cards took over where you could actually they would integrate a serial

**Dave Jones:** port, parallel port, joystick controller ports, real-time clock and all this sort of stuff into the one expansion card to try and save slots, but the circuitry remained exactly the same for like a long time and there's probably other

**Dave Jones:** brand personal computers back in the day that used a similar type of analog joystick interface. And that's exactly what this is. It's actually an analog joystick. It It wasn't just buttons. You could actually get real feedback and real fine control. If you moved it just

**Dave Jones:** a little bit, then your you know, your spaceship it just move a little bit or whatnot. The PC could actually read the position of the joystick on here. And the standard IBM ones had two buttons like this. It was exactly the same on

**Dave Jones:** the Tandy 1000, which is a basically a clone of the IBM PC Junior and was massively more popular than the PC Junior. And I've done a video, once again, linked in at the end of this where I design a turbo board for the

**Dave Jones:** Tandy 1000. That's a real old video, but it's interesting. So, stick around and check that one out. But exactly how did these analog joystick controllers work and what circuitry was required to actually read them? Well, let's do the first thing, tear this one

**Dave Jones:** apart. I can just move this and you can see that these two rotating arms on here would actually just connect up to just a regular carbon pot in there, a potentiometer, a variable resistor. And it they'd connect directly onto the shaft in there and

**Dave Jones:** simply turn that pot. So, the resistance value you can see that they're only using the two wire one here, so they're not center tapping that, but it's fine. You can do it either way. And that's how they do it. So, they need to read

**Dave Jones:** the resistance value on this pot. This joystick's actually quite interesting in that it has a a free mode. You see how it actually springs back in both directions? Well, you could actually move it to the corner and then you could go free like that.

**Dave Jones:** And then it would be free to sort of stay it didn't spring back in that direction, but it was still spring back in that direction and you could do that for both of those either or axes like that. So that was actually a really neat

**Dave Jones:** thing on the analog PC joystick. Like a 100k like that and I'm pretty sure that was just like an industry standard value and you'll notice that they've got a little bit of a bulge in here. They've got some caps as that go into the shield

**Dave Jones:** of the cable or perhaps just some noise suppression there. I don't remember my Tandy 1000 joystick ever having that. So how do we read the value from this pot? Well, that's where it gets a bit interesting. Now of course you might be

**Dave Jones:** thinking that the obvious solution you've got your potentiometer here just hook it up to your 5 volt rail and your ground and then you just you'll get 0 to 5 volts depending on the location of the joystick there and then you'd simply

**Dave Jones:** feed it into an analog to digital converter and you get your 8-bit or whatever value out and bob's your uncle, right? Well, you've got to remember that this was like the late 1970s early 1980s and ADCs these were actually quite

**Dave Jones:** expensive back then and you'd need four of them. You'd need at least a four channel one to read a dual joysticks in the PC. Two pots per thing and of course there was no such thing as microcontrollers back then

**Dave Jones:** essentially what we take for granted these days is about pick our AVRs our arm microcontrollers and they've got built in ADCs up to 12 bits and like all these peripherals built in basically microcontrollers didn't exist back then. We had microprocessors which

**Dave Jones:** is what all these PCs ran on and if you wanted ADCs you had to buy a separate ADC chip and they were quite expensive cuz you got to remember something like say the first sort of reprogrammable microcontroller pick

**Dave Jones:** 16c84 which used E squared prom. None of this flash rubbish. That didn't came come out until 1993. And that didn't even have a built-in ADC. So, you know, you take these things for granted these days, but you haven't

**Dave Jones:** always had these micros with all these peripherals and ADCs built in, especially back then. So, the clever designers went, "Well, we've got to cut cost." Doesn't get much cheaper than a 555 timer. Let's take a look. So, you should be

**Dave Jones:** familiar with the classic 555 timer and the various building block circuits that come along with that. And it's been popular for what? Four decades or something? And they still mass produce this thing. Found a 555 timer doing little one-shot and other timing type

**Dave Jones:** applications in a lot of the old vintage PCs from the '70s and '80s. In this case, the classic one-shot monostable circuit. And you're no doubt familiar with this classic building block circuit. We've got our resistor up here. You connect the

**Dave Jones:** discharge and the threshold pins. I won't go through how the 555 timer works. 555 timer T-shirt, my hand-drawn T-shirt, linked in down below, by the way, if you want to check it out. I'd recommend you do. And then a cap going

**Dave Jones:** to ground. And basically, we have a negative going trigger pulse coming in. So, when your trigger pulse goes low like that, it starts the timer, which will produce a single pulse, the pulse width of which, the time of the pulse

**Dave Jones:** width, is determined via the RC time constant here. And of course, if you replace the resistor here with the pot used inside the joystick here, bingo. You've got yourself a proportional time pulse, variable time pulse, that will vary based on the

**Dave Jones:** position of the joystick. And because you've got a PC, which has various timers and things built in, we can actually time in software how long that pulse takes. It's neat. So, there's no need to convert an analog value into a

**Dave Jones:** digital value using an ADC. You can simply do it using a timer-based approach, and PCs are really good at doing timing. But, of course, you need four of these 555 timers. Uh well, you didn't want to use four separate chips.

**Dave Jones:** Bugger that. But, of course, the 555 timer is available in both the single one, which is the 555, also the 556, which is the dual 555, and tada, the 558 quad 555 timer, not very often used these days. And this is what you saw in

**Dave Jones:** the teardown of the IBM PC Junior, which has the original IBM game card, or whoever made the design the IBM game card, it used a 558 timer, which is four 555 timers in the one chip, and it was super cheap,

**Dave Jones:** and there's basically not much more you had to add to it. So, it had the four channels. We could hook up the four joystick pots here. Uh four capacitors going to ground, they'd all be the same value, might be

**Dave Jones:** typically 10 nF or something like that. Depends on the the speed of the PC and the timing and the 100k used up here and stuff like that. And bingo, you would actually tie all the triggers together like this, cuz

**Dave Jones:** they were independent timers in here. But, if you tied them all together, then they then they all start at once, as we'll see in a minute why. And then, you would get the different pulse lengths out depending upon the position

**Dave Jones:** of each one of the joysticks, the X and Y on joystick one, and the X and Y on joystick two. Beautiful. And all the PC has to do is read the time period from there to there, there to there, there to

**Dave Jones:** there, and there to there. Easy peasy, lemon squeezy. But, of course, the PC being the PC, it uses a data bus. In the case of the IBM PC, of course, cuz it used the 8088 processor, it had an 8-bit

**Dave Jones:** uh data bus instead of the 8086 processor, which had a full 16-bit data bus. We have to somehow get this hooked up to the data bus so that we can uh use the timers in the PC to actually time

**Dave Jones:** it. So, how do we do that? Easy. We just uh hooked it up to a latch here, or a buffer/ uh latch, and then we would of course do the address decoding. I won't go into architectures of uh PCs and

**Dave Jones:** stuff like that, but basically every every peripheral, everything, every IO port or memory port on the PC needed a particular address. So, it would have an address decoder here, uh typically using discrete uh and, you know, NAND gates

**Dave Jones:** and all whatnot, stuff like that. So, they'd decode the uh address, and which is specific to the joystick, it would enable the chip, and you could read back the values on all the on all four of these um timer

**Dave Jones:** um outputs here. But, of course, the joystick also had two buttons on, so you could use the other four inputs here for the two buttons, and of course you'd have an 8-bit uh data latch, which then would go off to the PC bus. But, how do

**Dave Jones:** you trigger it? Well, you use the address same address decode, but instead of reading back the data, you would actually write it. So, the PC write pin would actually go to the trigger. So, you just write something to that

**Dave Jones:** address. You It doesn't matter what data you wrote, cuz the data was uh useless. All you wanted to do is trigger these timers. So, you'd write to the particular joystick address, and then you'd uh continually read back and until

**Dave Jones:** the end of the time period. But, the problem with this approach, of course, is that it requires software timing loops, and that imposed a real problem to PCs as they got faster and everything else. So, there were very I believe

**Dave Jones:** there were various uh schemes eventually to compensate for that sort of thing, and ultimately um all of this uh stuff would be built into the motherboards instead of add-on cards. It'd be built into the motherboard chipsets and things like

**Dave Jones:** that. But of course you still used the classic 558 on the output, but you know, all this stuff typically started to get integrated into the chipsets as time went on. So there you go. I think that's a rather cheap and clever way to do it.

**Dave Jones:** All you needed was a 55 a couple of ICs, hook it up to your D15 connector for your joystick and your buttons over here, and Bob's your uncle. You could just have a little address to code and read it back. Very simple. And

**Dave Jones:** of course if you wanted a greater precision in reading the position of the pot, you had to do finer and finer reads on your port so that you could read the pulse width there with greater precision. And we can actually see the

**Dave Jones:** value change here if we move the joystick, but of course you could trim it. You had these uh little uh trimmers on the front that you can move back and forth to uh center that. And you can see

**Dave Jones:** the physically the joystick actually um sorry, the pot actually moving back and forth as I tweak that uh trimmer on the top. So you know, you might want to trim it to the center or something like that. And if I move the joystick, you can see

**Dave Jones:** that it uh went all the way with LBJ up to 120k. These pots weren't very uh precise back in the day, and then it'd go down to zero like that. So you'd get the full um mostly the full range of the pot there.

**Dave Jones:** And if we actually have a look at the IBM PC Junior motherboard, we can actually see the triple 5 timer up in there as we saw in our previous teardown. And there it is, a classic National Semiconductor genuine, none of

**Dave Jones:** that rip-off rubbish, uh 558 quad triple 5 timer. You'll notice some uh some of the timing caps there because of course you didn't want your PC shorting out and having no resistance at all in series with your cap. So they'd put some

**Dave Jones:** resistors in series for that just to give you and like a restricted end stop type value on your joystick when your joystick shorted out and went to zero. And of course due to the proximity to the 558 there, that's

**Dave Jones:** almost certainly the buffer used to go on to the PC bus. Your absolute classic 74LS 244. And they'd have probably some of your decoding stuff up here as well. And of course I'd love to show you the timing on this. Unfortunately, if we

**Dave Jones:** have a look at the outputs here of course, then it actually does nothing. It's actually not triggering the output. It's not giving any pulses whatsoever on there because the timers wouldn't actually turn on or trigger unless the software was actually

**Dave Jones:** writing to that address. So you're running a game or something that was continually polling the joystick. So in this case, this PC Junior doesn't work. Aw. Now the Tandy 1000 is interesting in that it actually uses a slightly

**Dave Jones:** different hardware implementation. It doesn't use the triple five timer. So let's actually take a look at how it actually does it. Here's the block diagram here. It's essentially doing exactly the same thing as what we were doing with the triple five timer. It's

**Dave Jones:** producing a proportional pulse width timer output based on a trigger signal, but it's doing it using an integral here and that's what that little fancy symbol is. Integral of IDT there. What that means is that it's just producing a ramp

**Dave Jones:** which starts at zero when you trigger it. And that voltage ramps up. And if we have a look at the schematic here, you can see that that little ramp generator there with the JFET there, it just generates a ramp voltage which then goes

**Dave Jones:** into comparators there. Which then the joystick the voltage from the joystick just goes into these four comparators, and then of course, once the ramp voltage gets up and reaches each individual joystick position, the comparators flip over and produce a zero

**Dave Jones:** instead of a one or vice versa, and then the PC can actually read that as a time period. Exactly the same as the triple five timer, except the hardware implementation is a little bit different, but it works exactly the

**Dave Jones:** same, and you can see the 74LS244 buffer on there, and the right and the address decoder and the right signal and the read signals as well. As well, it works exactly the same as the original IBM PC game adapter. In fact, the

**Dave Jones:** software, as long as you kept the read and write address the same, the software wouldn't even know the difference. Wouldn't know whether you're using the integrator there, like the ramp generator and the comparator, or whether or not you're using the triple five

**Dave Jones:** timer. Still going to work exactly the same. Software wouldn't notice a difference except if there's some variations in there in the actual timing itself, but apart from that, no, you'd get the same thing. And I'd love to show

**Dave Jones:** you the Tandy 1000 working as well. This is the IBM PC Junior. The 1000's down in my storage bunker, but I can't find my five and a quarter inch boot floppies, so I just can't get the thing going. And

**Dave Jones:** without that software, there's nothing to trigger the polling or whatnot without even being able to boot up DOS to then you know, be able to write to the joystick address to trigger the damn thing so that we can see the timing and

**Dave Jones:** stuff like that, but I hope that gave you a good idea of how the IBM PC joystick game adapter actually works. It's not the greatest solution cuz it is you know, software timing dependent. You've got to be able to accurately

**Dave Jones:** measure the time periods and do it fast enough to respond to all the joystick controls, and of course, PCs back then, they had to share all the same bus, and they were all doing, you know, they had to do everything at once, but you know,

**Dave Jones:** it it actually worked back in the day, and that was a fairly cheap and simple solution to bring the component cost down instead of using an ADC or something like that. So, anyway, I hope you enjoyed that and found it useful. If

**Dave Jones:** you did, please give it a big thumbs up. As always, discuss it down below in the YouTube comments or on the EVblog forum, and there's a couple of videos here at the end you should check out. And thanks

**Dave Jones:** to all my patrons and supporters who uh help keep this channel going. You can probably find a link here at the end somewhere, too, if you want to join. Anyway, catch you next time.
