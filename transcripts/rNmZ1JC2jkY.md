---
video_id: rNmZ1JC2jkY
title: EEVblog #81 - Smart Tweezers LCR Meter Review And Teardown
url: https://www.youtube.com/watch?v=rNmZ1JC2jkY
source: youtube-asr
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. Hi, it's product review time. And this week, we've got the Smart Tweezers from Advanced Devices. Let's check it out.

**Dave Jones:** So, what is the Smart Tweezers? Well, as you can see, it's a pair of tweezers with a meter attached to it. In this case, an LCR meter, a completely automatic LCR meter. And it has other features, too. It does diode testing,

**Dave Jones:** uh continuity, and it even has a little oscilloscope display, as well. So, it's a pretty useful device. And as you can probably tell by the tweezers, it's designed for today's SMD surface mount components. You You know, you put the

**Dave Jones:** components between there, and it'll automatically measure the component on the display. Pretty darn handy. It comes from a company called Advanced Devices in Canada. And this is their only product, and you probably haven't heard of them before, but this is a real nifty

**Dave Jones:** device, and it's getting quite popular. I've had quite a few people ask me to do a review on this. Not only are they a Canadian company, check it out, made in Canada. Can you believe it? Made in Canada. I don't think I've ever had a

**Dave Jones:** piece of electronic gear made in Canada before. It's incredibly novel. Gets a huge thumbs up just for that. I love the Canadians. Now, of course, there are other LCR meters on the market, like multimeter style, or little pocket ones with, you

**Dave Jones:** know, test leads, and you try and probe your components like that. But that's really annoying. And so, what they've come up with with those devices is you can actually buy a similar sort of tweezer attachment for those. But

**Dave Jones:** they're still, you know, they're messy. You've You cables all over your bench and stuff. And if you're like me, if you're assembling a board or something like that and you've got hundreds of little surface mount components already on your bench there ready to be mounted

**Dave Jones:** on your board, then you know, if you drag your test leads across your bench, bingo, you can wipe out all your components and ah, it's a pain in the ass, really. So, these smart tweezers are completely self-contained, no test

**Dave Jones:** leads, just these little gold-plated tweezers and they're very nice. Check them out. They're This is the straight version. They also um Well, my one came with a curved version as well. I'm not sure if the standard one comes with curved and they've also

**Dave Jones:** got what's called a precision type one as well, which I think has a more refined head on it. And it looks like really thick, solid gold plating. It You know, I've I've been using it for a couple of weeks and and there's no

**Dave Jones:** noticeable wear on it. Um but you know, that's that's hardly a big test for it, but the probes are really, really nicely well designed. It's probably the best aspect of the product and so it should be because that's its primary use as a

**Dave Jones:** probable tweezer device. But hey, who cares about all that? Let's get to the fun part. So, don't turn it on, let's take it apart. Okay, taking apart is real easy, just three screws on the top here, self-tapping screws and bingo, there it

**Dave Jones:** is. Check it out. As you can As you'd expect, a big LCD like that. Now, that's the first thing I really notice about this. There's no window, there's no protective window on there, so you're really reliant upon the glass surface of

**Dave Jones:** the LCD to actually protect it. So, you know, it's it's probably in that respect, it's not as rugged as it could be. Okay, so let's check it out. As you can see, you got your three button cells here. Now, um that's not the world's

**Dave Jones:** best uh battery holder. It's just got the two metal tabs coming straight out just squeezing the batteries together, but you know, it works. You can actually get a battery upgrade for it. You can get a rechargeable battery and induction

**Dave Jones:** rechargeable battery. Now, as you can see, there's the piezo There's the piezo transducer in there if you can see that. Yep, there it is. Little tiny piezo transducer, so it does beep and buzz and do all sorts of

**Dave Jones:** things. Now, as you can see, the LCD is just stuck down with some tape. Pretty with some just some double-sided sponge tape. That's pretty standard practice. Now, um what they've got here is they've got a mechanism looks like a mechanism holding

**Dave Jones:** the probes in place. So, let's check that out. Now, if you try and get the rest of the board out, you don't undo this screw here. You undo another self-tapper on the bottom here, and the board should just the whole mechanism should just

**Dave Jones:** lift out like that. And bingo, here it is. As you can see, they've got a really some sort of big custom mechanism here with some There's the actual contact going across for the for one probe and the same thing on the

**Dave Jones:** other side for the other probes. That's really quite neat. They've come up with their own little sort of you know, custom enclosure for the custom mount for these probes, and it's really is quite nice. Now, as you can see here with the circuitry,

**Dave Jones:** nothing unusual there at all. It's It's basically exactly what I expected. There's an MSP430 processor here. There's some just some just some basic analog stuff around here, and there's a slide switch over here which actually selects the which actually selects the voltage mode,

**Dave Jones:** and I'll talk about that later cuz that's one of the really annoying aspects of the product which I don't don't particularly like. And in dumb jog shuttle down here which allows which which you can push in like that to

**Dave Jones:** switch it on and off and then you can rotate side to side to go through the menus and then push again to select things and there that's a standard interface they use on all sorts of products MP3 players and

**Dave Jones:** mobile phones and and I I actually recognize that one I've used it before it in my own design so you know it's it's all pretty standard stuff there's not much in it uh but the actual quality of construction

**Dave Jones:** is is really it's you know it's it's reasonably nice I like it they really haven't cut corners in too many places now I'm not sure who actually makes the LCD but as you can see it's quite a high

**Dave Jones:** contrast one and and you can read it from you know quite it probably doesn't show up in the camera but you can read it from different angles and it really is quite a very nice dot matrix display I

**Dave Jones:** like it now as you can see here the spring contacts do actually have quite a bit of spring to them they are bent in quite far so they do apply a fair bit of force onto these batteries which isn't too bad

**Dave Jones:** at all okay now let's check out the operation of this device everything's controlled by this little jog shuttle here which can move left and right like that which calls up a menu system now um it allows you to scroll through the

**Dave Jones:** menus like this and as you can see it's got a whole bunch of menu options which we'll go into but when you first turn the unit on I was actually quite confused it comes up with this advanced devices thing and it shows no

**Dave Jones:** measurement at all and I thought oh Jesus taking a long time to boot but no it's just automatically it'll automatically put up the reading once you actually um once you actually probe something which I guess is kind of neat but I'd I'd

**Dave Jones:** rather it have zero on the display anyway that's just personal preference so you push the jog shuttle in here and you come up with the menus. Now, um as you can see it's got um auto set is like the big mode where it just

**Dave Jones:** automatically chooses whether it's capacitance in in this case capacitance when I touch it with my fingers and you short it out and it measures resistance. And that's that's probably the mode you most want to use it in cuz it works

**Dave Jones:** really well the auto set mode. But uh let's have a look at some of the other modes, okay? What? Let's go into the menu, press it and you go into measure and uh you can go into mode here and you can

**Dave Jones:** choose all the different things. Auto mode, you can force it into different modes. Resistance, inductance, capacitance, diode, voltage and the uh trace mode. So, you know, if you want to put it in the diode mode, there it is.

**Dave Jones:** It comes up with the diode symbol. It's got a diode symbol on the display and what's really good about it is that if you um short the probes together like I am now, it tells you that it shorts out.

**Dave Jones:** Now, let's actually take a board here and let's probe a diode in circuit, okay? Now, look. As you can see it's it's come up with the diode symbol on the display and the whoop. It's Sorry, it's hard to keep the probes

**Dave Jones:** on. As you can see the diode symbol on the display, it tells you which way around the diode goes. Let's put it around the other way and there it is there. It See, it goes in the other direction. So, it tells you

**Dave Jones:** which uh pin correspond It shows you which um whether the anode or cathode corresponds to which probe. It's really quite nice. But unfortunately, it's got a real big problem. It can't measure LEDs um at all because it's got

**Dave Jones:** such a low voltage There you have switched off again. Such a low voltage threshold that if we try and measure an LED here in circuit, well, it it makes trust me, it makes no difference if whether it's in circuit or not. Um it

**Dave Jones:** just can't measure and that's a standard green LED at like 1.8 volts. It just can't measure it, let alone measure white LEDs and things like that. So, I think that's a huge limitation really uh because when you've got a whole bunch of

**Dave Jones:** diodes on your um you know, laid out on your bench here ready to be soldered, you want to know uh which way around they go and this is real handy for diodes but not for LEDs. Now, let's check out the system menu. Let's go in

**Dave Jones:** and go down to system here and you can see that uh you can turn the sound off and on. You can actually swap the actual display uh left and right. So, if you're left-handed, you can actually go left

**Dave Jones:** like that and it's swapped it around. Isn't that neat? Now, other things in the system menu, um you've got timeout. You can change the timeout um uh from when it takes no reading at all to when it switches the thing off. In this case,

**Dave Jones:** it's 60 seconds. I believe that's the default uh setting. Um service is like uh you can get the uh you can measure the battery voltage. You can actually um adjust the offset so you can actually trim the offset like that. Uh the

**Dave Jones:** battery voltage, you can measure 4.4 volts which is rather neat. Now, there's also a whole bunch of measurement options as well. As you can see, I'm just um probing my fingers here which measures the capacitance. It thinks it's

**Dave Jones:** primarily a capacitance and it's giving this it's this giving us the series resistance as well and then it's showing the measurement frequency is 10 kHz. Now, you can change that measurement frequency and the secondary display as well. If you go into uh measure and you

**Dave Jones:** go into settings, you can um change the test frequency. So, let's say we want to change that to 1 kHz. Now, unfortunately, it doesn't have 100 kHz which I think's a big limitation as well, but I'll talk about that later.

**Dave Jones:** Now, um See, it's changed the test frequency. Now, let's go into Sometimes it doesn't respond to the button press, which I find rather uh curious. It seems to be like a timeout period there where it where it doesn't seem to respond um

**Dave Jones:** properly. Maybe it's doing something in the background. Anyway, um you can change the uh whether or not it measures um uh the actual Q or the dissipation factor. So, let's go into QD, and as you can see, the secondary display is now

**Dave Jones:** showing the dissipation factor of the capacitance. That's really quite neat. I like it. You've got If you go down in the settings, you've got the test frequency, you've got the period, which allows you to change the measurement period, 2 seconds, a second, or half a

**Dave Jones:** second. That's um it defaults to 1 second, I believe. So, it's it's nice to be able to change the measurement period. I guess you get increased accuracy or uh increased stability with uh longer measurement period, but I haven't uh particularly tried that in

**Dave Jones:** depth. And it's got a hold mode as well. Now, if you do hold, let's try that. Put it on 34. And And it holds the display like that. That's really It's It's really quite uh It's really quite neat. And as you can

**Dave Jones:** see, 1.8 Now, it's held it at 0.9. So, it's, you know, I guess there are quirks to that mode. Um it doesn't necessarily hold the last one. Yeah, it did that time. So, I guess it's But generally, that's a pretty

**Dave Jones:** handy mode. It's like a It's like a touch hold mode on a auto touch hold on a multimeter. Terrific. The other interesting feature of the display is it actually has a bar graph as well, which is which is really quite

**Dave Jones:** uh neat. I guess you can see changes, but really the primary display is nice and big and clear. As you can see, it's just, you know, it's it really is a beautiful display. A lot of effort's been put into how this, you know, to the

**Dave Jones:** fonts and things like that of how this displays. I really like it. You can buy additional probes, as I've mentioned before, and they're really quite sharp. I'm, you know, it's it's probably going to be hard to see on there, but trust me, they

**Dave Jones:** are really good quality probes, and they should last quite some time. Now, the curved ones are quite good, cuz when you use it like this, often you if you're probing stuff on the bench, you want them to curve out like that, so

**Dave Jones:** that it it's just nicer, the components don't flip around as much and stuff like that. So, I guess that's a personal preference thing, but I really like the probes. Thumbs up. Okay, now let's check the accuracy of this. Now, I'm actually

**Dave Jones:** using my micro current and measuring a component in circuit that I know is 10k, .1%, and as you can see, it's uh basically spot on. Now, if I change the range here on my micro current, it switches in a 10 ohm, .1% resistor, and

**Dave Jones:** as you can see, it's pretty damn good. Um and and I find that's pretty much over the range. It's much more accurate than its quoted specifications. It's really quite nice. I like it. Now, as for measuring components in circuit,

**Dave Jones:** it's just like any other in circuit component tester. Sometimes it works, sometimes it doesn't, depending on what components are in parallel. Let's measure this tantalum here, which is supposed to be 47 microfarads, and well, it basically is, with the series

**Dave Jones:** resistance of 7 ohms. So, and once again, it works in both should work in both directions. There you go. So, that's that is an example of one where it where it does actually work. Now, here's another example where

**Dave Jones:** I think it's probably going to work. That should be a 100 100n cap in there, and you know, sure enough, it it kind of is, you know, and it it does work um for some components in parallel, but not all

**Dave Jones:** of them. Here's an example of it measuring an inductor in circuit, and it's not too far off the mark in this case. So, you know, there are a lot of instances where it works, but I found a lot of instances where it just simply

**Dave Jones:** will not work cuz there's too many components in parallel. Now, let's try and measure the inductor in this small DC to DC converter circuit here and see what we get. It should be 10 microhenries, and it jumps around a bit, you see? It It

**Dave Jones:** doesn't automatically lock in. So, that shows that it's you know, it can't measure everything. There was eight microhenries there. There we go. No, see? It jumps around. It jumps around. It often gets very very confused with some in-circuit components. So, it

**Dave Jones:** doesn't always work. Now, that will that will change with the frequency as well. Um but, you know, it's you can't rely on it as as a 100% foolproof in-circuit tester. Let's turn it around the other way and measure it in the other

**Dave Jones:** direction. There you go. Bingo. 9.1 microhenries. So, you know, you've just got to be careful when probing stuff in circuit. This thing is not infallible, and it's not unique to this. Any in-circuit component analyzer will be just the same. Now, let's switch it back

**Dave Jones:** again. And hey, there you go. It's finally locked in. Maybe it had some residual charge in there somewhere, and it's just it's fairly happy about it now. But, yeah, just be careful. Now, an important thing to actually measure is the in-circuit test voltage

**Dave Jones:** because this can have an effect. If it's too high, it can switch on PN junctions in the circuit when you actually measure stuff in circuit. Now, the unit claims to be around um 320 millivolts, uh RMS or or 400 millivolts

**Dave Jones:** uh drive voltage. It's um it's not entirely clear. Now, I've got it on 10 kHz test mode here. I've captured the signal, and it's about 266 millivolts RMS or almost 800 millivolts uh peak-to-peak, which is larger Well, it's, you know, it meets its spec, but I

**Dave Jones:** think it's larger than it it probably should be, but the device seems to work reasonably well in circuit, so, you know, I'm going to I'm going to give it that. It does actually seem to work. Now, an interesting thing is when you uh

**Dave Jones:** is during This is just in auto test mode, so obviously it's going through some auto mode, and as you can switch see it's switching between some high frequency and some low frequency uh thing there as well as switching off in

**Dave Jones:** between. So, it's doing some sort of compensation or some other I don't know measurement that it needs to do to get the display. And that's not just in auto mode, either. I've just got it set to to the

**Dave Jones:** straight capacitance mode, and it's doing the same thing. There's one other thing to consider with stuff like this, and it goes for SMD tweezers as well, is is the material a non-magnetic type? Because if it's magnetic, you can actually um it can

**Dave Jones:** pick up it can actually attract components and pick them up, and that could be really annoying. So, I've got my little uh magnetizer demagnetizer thing here, and I've tried to magnetize it, and I can't really. So, I think it's

**Dave Jones:** like a some sort of uh you know, not easily magnetized material, which is great. There's one other thing it actually comes with, and that's a a uh calibration certificate, which is, you know, which is really amazing for a

**Dave Jones:** device like this. It's got the serial number on it where it was tested, but it's not it's not trace I don't think it's traceably um you know, calibrated, so it may not um it may not be valid for a lot of

**Dave Jones:** companies who take that sort of thing seriously, but still it's pretty good. And it but it doesn't give you the exact measurement readings. Just says better than 3%, you know, better than 1%, you know, better than 5%, so

**Dave Jones:** you know, it's it's not great, but hey, at least you get one. Now, one of the problems I have with this device is that it's low in It's not really capable of measuring low value inductors. Now, here's a 2.2 micro Henry inductor, okay?

**Dave Jones:** And it measures that fine, but here's a 1 micro Henry inductor. There we go. That's 1 micro Henry. There you go. It's, you know, it just doesn't know. It's an inductor. It just can't measure that low. And I think that's a that's a

**Dave Jones:** reasonably, um, you know, problematic limitation. Um, now, I've got no problems with the low capacitance mode. As you can see, you know, 1 pF is, you know, a few pF is nothing for it. It can measure that easily. But inductors, its range

**Dave Jones:** probably isn't as big as I'd like. Okay, let's just do a quick comparison, uh, with an in-circuit ESR against the Bob Parker ESR meter I've got here. Now, as you can see, this, um, the Smart Tweezers is measuring at 10

**Dave Jones:** kHz, and as you can see, it's 1.1 ohms ESR, basically. And the Bob Parker ESR meter, let's take a look. Very quickly, it's 1.1 ohms. So, it matches fairly well. But of course, one of the big drawbacks with the Smart Tweezers is that its

**Dave Jones:** maximum frequency is only 10 kHz, whereas the ESR of capacitors is measured at an industry standard rate of 100 kHz. So, really, it's just not capable of that. One weird thing it comes with is this little pocket clip like this. Now,

**Dave Jones:** you're supposed to like, I assume, you're supposed to just hang the probe in there, and it's supposed to like, you know, hang on your pocket like that. But, I you know, it's just it's just going to fall out. I

**Dave Jones:** don't know why they bothered. Now, actually on paper it's specs aren't aren't that terrific, you know, we're we're talking 3% 5% like from 10 10 puff up to 100 microfarad is you know, less than 3%. Um I found it's actually better

**Dave Jones:** than that, but hey, they're the actual um specs or 0.5 picofarads up to 5,000 microfarads is five less than 5%. This The specs aren't aren't going to set world on fire, but it seems to be much better than its

**Dave Jones:** specification, which is really quite good. The unit, of course, can also be used as a little mini oscilloscope in trace mode. So, to do that, you actually go down to measure and you go down to mode and you go down to trace mode like

**Dave Jones:** that. Now, it'll actually say slide switch cuz what you got to do is you got to slide this tiny little switch in there and you can't do it you there's no way you can possibly get your fingernail or anything like that in there. So, you

**Dave Jones:** got to hunt around for like a little screwdriver and then you got to flick it across like that and bingo, it goes into trace mode with a fixed plus minus um 5 V um scale. I think Yeah, I don't think

**Dave Jones:** you can change the scale, but you can change the time base by just um pushing the jog shuttle. Let's see if we can speed it up. Yep, there are it's actually you can actually might not show up on camera too well, but it is

**Dave Jones:** actually flying through at a fast reasonably fast time base and then you can slow it down. And that's rather neat, but I think that really lets it down. That slide switch is a terrible design aspect, the only really bad

**Dave Jones:** design aspect of this product, I think. I don't like it at all. Now, for those who are going to get excited about the oscilloscope capability of this thing, well, don't because I it's pretty much down in the gimmick category. Okay, here

**Dave Jones:** it is measuring a 10 Hz sine wave and as you can see it's it's it's hard to read and yeah, it's displaying it, and yes, you can change the time base setting, but as soon as you do that, you know, it

**Dave Jones:** just it just disappears. It's It's really uh I wouldn't say hopeless, but it it really is down in the toy category. Really going up in the high bandwidth stuff, 100 Hz. As you can see, it hasn't triggered properly or it's aliasing.

**Dave Jones:** That's obviously aliasing. Okay? Just based on the sample rate. Now, I turn the sample rate up. Trust me, that's not a thing with the camera. I can't even see that display. It has disappeared. It is just, you know, it's

**Dave Jones:** it's no good at all. You know, that's a sine wave, but that, you know, trust me, that is not that is not the real deal. Okay? It's just it's really no good at all. It's except if you want to see very

**Dave Jones:** slow changing fluctuations down in the, you know, couple of hertz cat sub 10 hertz category. That's it. And I wouldn't get excited about the voltage ranges because if it's fixed on this plus minus scale here, in fact, I think

**Dave Jones:** it's actually plus minus seven or something like that. But as you can see, if we turn it if we turn it down, it doesn't you know, it it doesn't auto scale or anything like that. So, you're really stuck with that one range. Now, in

**Dave Jones:** addition to the oscilloscope display I showed, which is a bit of a toy, it also measures voltage as well. And you've got to switch it to that mode, too. And the manufacturer warns that you shouldn't on regular LCR meter mode, don't put

**Dave Jones:** anything greater than I think 1.6 volts on the probes, otherwise you'll damage it. So, you know, I think that's a pretty simple rule. Just don't use it for any voltage or oscilloscope type measurements. That's what your meter's for. Just, you know, stick to the LCR

**Dave Jones:** meter functionality, I think. Now, Advanced Devices who make this, they're really trying to pitch it as sort of a semi-professional to professional level tool because the support you get with it is quite good and all the accessories you can get you can get you know

**Dave Jones:** different types of probe attachments and you can get rechargeable solutions for it recharge auto induction docking stations and things like that for people who who have high volume use you're using it you know 100 times a day to measure you know

**Dave Jones:** components in production and stuff like that and really I think that's that's its main market they should stick to that because that's why you pay a high price for it really but you know as a as a cheap hobbyist

**Dave Jones:** tool well it's you know it's not it's clearly not marketed as a really cheap device. So let's sum up the smart tweezers. First of all who's it for? Well it's not really for your average hobbyist I don't think it's a pretty

**Dave Jones:** specialized bit of kit because it's it's really designed for people who have a ton of components spread over your bench when you're assembling or you're doing batch matching or you know component matching or stuff like that this comes

**Dave Jones:** in real handy because you don't have to worry about probes dangling all over your bench and it's really and the probe form factor is really very nice it's very nice to use. So in that respect it's it's unbeatable

**Dave Jones:** if you need the tweezer type functionality I think it's fantastic but as a general purpose LCR meter I'd probably prefer one with the you know a standard multimeter looking one with probes I think they're you know they're just a bit more

**Dave Jones:** versatile I think but and you can get probe attachments for those multi for standard LCR meter multimeter you can get tweezer attachments sorry so you know but it's pretty good. Now the problem is I think one of the major

**Dave Jones:** problems is the price it's pretty high so that rules out you know a lot of hobbyists and things like that it's $320 street price so I don't think you can really get it under that. That's US dollars. So, it's pretty high. You're

**Dave Jones:** paying a premium price for, you know, I mean, granted, it's a very, very good unit. Um but, you know, it's might be pricing itself out of some markets. But, for businesses and for well-heeled uh hobbyists and things like

**Dave Jones:** that, it's really good. And I'd recommend it. I I thought it was a bit of a gimmick at first, you know, when I first saw it and I thought, "Oh, it's like those probe-type multimeters." You know, I just hate them. They're just

**Dave Jones:** They're They're a gimmick. But, this one's not. It actually works really well, apart from a few limitations which I've mentioned. And I find I'm actually reaching for it very often. It's a very useful bit of kit to have

**Dave Jones:** you know, to actually have on your bench if you can afford it. And it actually comes with a rather nice uh display, you know, a padded padded carry case, so you can sit that on the bench and it doesn't

**Dave Jones:** get damaged. So, I think it's quite a useful tool overall. It's You know, it generally meets its meets or exceeds its performance specification. And I give it a thumbs up. But, price, So, just how does these smart tweezers

**Dave Jones:** actually work? How does a typical LCR meter work? Now, I've covered this in another blog. I think it was blog number way back at 32 or something like that. But, I'll go over it again. Now, the basic circuit, the basic functionality

**Dave Jones:** of an LCR meter, including the smart tweezers, is to have a function generator like this with different test frequencies and a an output series resistor here, RF, and that goes into the device terminals, the device under test, the DUT. That's written there.

**Dave Jones:** They're actual tweezer terminals. And it taps off uh the voltage from that, amplifies it, and feeds that into your analog to digital circuit analog to digital converter and your microcontroller. Now, it also feeds that signal into a standard feedback a low power

**Dave Jones:** feedback current amplifier and that actually gives you an it allows you to measure the output or this the current going through the device under test. Now, because the micro is generating this waveform it knows what phase the test signal is and so therefore it

**Dave Jones:** measures the voltage and the inductance and also the phase that's the key thing of the voltage and inductance as well and from those things as as I've explained in a previous blog you can determine everything capacitance inductance series resistance parallel

**Dave Jones:** resistance quality factor dissipation factor a whole slew of things you can actually measure from just the voltage and the current. Okay, now that's terrific, right? You can measure all these things from just the voltage and the current but how does

**Dave Jones:** the device know that whether it's or not whether it's inductive or whether it's capacitive? Well, I'm glad you asked that too. Let's take a look at it how it works in auto mode. Okay? Now, this is a standard

**Dave Jones:** polar waveform. Okay? Based on the phase of the current through the thing. Now, if the if the current is leading if it's positive in relation to the test signal then it's going to be an inductive component. Now, if it's lagging the test

**Dave Jones:** signal current's lagging the test signal in any way then it's going to be predominantly capacitive in nature. Now, of course if the device under test is a pure resistance okay then it's going to have no phase angle difference at all.

**Dave Jones:** So, the phase angle is zero like this and that represents a pure resistance. Now, if it's positive okay basically it depends on the quality factor. Now, if the quality factor is greater than one in this direction like this, then it's

**Dave Jones:** the component is predominantly inductive with a small amount of series resistance. But, if the quality factor is less than one, but the phase angle is still positive, it's predominantly resistive with a little bit of inductance. So, it knows what the

**Dave Jones:** primary component is, whether or not to display it as a primary on the primary display or the secondary display. Now, um the same thing with the capacitance. If the quality factor is greater than one, the component is predominantly capacitive with a small

**Dave Jones:** amount of, in this case, parallel resistance. Now, um if it's less the quality factor is less than one, likewise, it's predominantly a resistive component with a small amount of parallel capacitance. And there's a series ESR in there as well, but that's

**Dave Jones:** essentially how it works. And for those playing along at home, here's a little bit more detail. When you actually measure or when you calculate the the phase the voltage and current phases and you measure them, what you come out with is an equivalent

**Dave Jones:** circuit of two series components, RS and XS. Now, um if XS is greater than zero, it's an inductive component. If XS is less than zero, it's a capacitive component. But, from those two figures, as I said, you can calculate everything,

**Dave Jones:** all sorts of things. This is um only a small section of what you can actually calculate. Quality factor is the absolute value of XS on RS. Dissipation factor is one on quality factor, the impedance of the component, RS squared

**Dave Jones:** plus X sorry, XS. Got that wrong. XS squared and square root the series capacitance is 1 over 2 pi F absolute value of XS, the parallel inductance is XS on 2 pi F, and the parallel resistance 1 +

**Dave Jones:** and so on and so on. You can calculate a whole bunch of stuff just based on fundamental voltage and current phases. It's a really neat technique. And this is how the smart tweezers works. Probably not as in-depth as this, but some even the

**Dave Jones:** top end, the you know, the 10,000 20,000 bench LCR meters, they're going to use this technique to calculate everything.
