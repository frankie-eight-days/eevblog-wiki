---
video_id: sR92IOU7XJM
title: EEVblog #439 - Atten PPS3205T-3S Triple Output Power Supply Review
url: https://www.youtube.com/watch?v=sR92IOU7XJM
source: youtube-asr
---

**Dave Jones:** Hi, it's power supply review time again and we've got a pretty high-end bit of kit today. Not a big name brand, one of the cheapies, but that's the key. It is a precision triple output power supply. It's the 810, let me get this right, PPS

**Dave Jones:** 3205T-3S. And three independent uh uh isolated variable outputs. Um 0 to 32 volts at 5 amps on two of the channels and 0 to 6 volts at 3 amps on the third channel down here. Completely um There it is. Uh PC interface, there's a

**Dave Jones:** USB and serial interface and it's a precision supply. Forgive me. I won't. Yeah, I'll hold it up. Come on. I'm strong enough. Geez. It's only weighs 10 kilos. Um linear power supply, of course, uh precision output 0.05% so they claim. Plus minus, you know, 10

**Dave Jones:** millivolts or something like that. So, real precision bit of kit and a big graphic display on the thing as we'll see. So, the key to this is that it is half the price of probably the next one on the

**Dave Jones:** market that's equivalent kind of, you know, triple output um high power linear precision one would be the Rigol uh unit. And it's half the price. I got this for about 450 Australian dollars. So, yeah, pretty darn cheap for this

**Dave Jones:** class of instrument. Is it any good? Smells a bit cheap, but uh could be good value for money. Let's check it out. And here it is. And one of the first things you notice is that it is actually

**Dave Jones:** a quite compact unit. I mean, for the power we're talking about here. I mean, we're talking about 160 watts um for per channel. Much less on the third channel, but you know, really quite a high-powered linear supply. As I said,

**Dave Jones:** it does weigh about 10 kilos, but really it's only 200 mm wide here, so it doesn't take up much space on your bench, really. And you know, you compare it with a multimeter, it's only like two multimeters width,

**Dave Jones:** something like that. It's It is a quite small. It's about 350 mm deep, but yeah, not too bad at all. Now, yeah, it's got a carry handle on top. It's I will have to take and crack the thing open to see if it's

**Dave Jones:** actually sturdy or not. It's built like a cheapish power supply, not as bad, doesn't feel as bad as many of the cheapies, but it's certainly not like an Agilent or something like that. So, you know, really you get what you pay for. And on the

**Dave Jones:** back here, nothing much happening, standard IEC mains input, 5 amp fused, a fan, which is really annoying, we'll get into that. It is quite loud, it rattles, I don't like it at all. And USB and RS232 interfaces for the PC control. And I

**Dave Jones:** believe they would be presumably isolated as well. We'll check on that. And on the bottom of the unit, four big sturdy rubber feet on the thing, and looks like big mounts for the huge monster transformer in there, as we'll

**Dave Jones:** no doubt see when we take this thing apart. I assume that they've got shake-proof What They don't have shake-proof washers on the bottom, but they might have them on the top side inside. So, build quality is certainly adequate for the price, that's for sure.

**Dave Jones:** All right, let's power this thing up, and clunk, A10 rev 1.0 software. Be afraid, be very afraid, but there it is. It's got a triple output display here, channel one, channel two, channel three. One of the things I don't like is

**Dave Jones:** that like channel one, channel two, channel three are identical. It doesn't tell you what the you know, like it doesn't say this one's zero to 32 volts. This is zero to 32 and this is zero to six. Why doesn't it tell you that? I

**Dave Jones:** mean, you've got to you've got to know. If you just walked up to this, you wouldn't know that this one only goes up to six volts. You would have to know when you actually go in and try and

**Dave Jones:** type in a a value in there to go up to 30 volts and channel three can't do it. So, you know, labeling. I mean, jeez, it's not rocket science. Now, as for the display itself, it's not bad. Nice bright nice bright backlight

**Dave Jones:** if you're looking directly straight on the thing. If you turn it to the side, it does sort of, you know, it does wash out almost completely if you move it out like that or if you go up, then it

**Dave Jones:** washes out, of course, and it does pretty good from below like that. So, if you've got it up high on your bench, you can actually read it reasonably well. So, you know, it's it could be better. It's not the

**Dave Jones:** best display. And you know what I'm going to do is peel off this protective coating here. Does make it look a bit a bit daggy.

**Dave Jones:** There we go. Much better. Check out the quality control on this one, folks. Look, it looks like someone's like eyelash or something has been embedded behind the display in there. Someone at the Chinese factory. Hi, how you doing? If you're

**Dave Jones:** watching. Now, you can probably hear that. One of the first things you notice is that it the sound of the fan is incredibly annoying. Yes, it does have a variable speed fan, which is great, but it Listen to it. Clunk clunk clunk. Not

**Dave Jones:** sure if you can hear that, but it it really is not that great. Listen.

**Dave Jones:** There you go. It just sounds awful. It sounds sick. Like there's something wrong with the thing. Like just the bearings are [ __ ] They use some cheap ass fan in it. Anyway, we'll be able to fix that up

**Dave Jones:** later, no doubt, with a fan retrofit. Um but you know, it it's not too bad. They could have done more with the graphic display. Like, for example, if you only have one channel turned on, why not, you know, have an option for a say a larger

**Dave Jones:** single display or something like that. But now it's fixed. There's no power display. It's great that it shows the voltage to 10 mV resolution, current to an excellent 1 mA resolution, which is great. But they don't display the power

**Dave Jones:** per channel. That would have been kind of nice. I you know, it's not the best laid out um screen at all. So, I don't know. You know, personal opinion. Big output button here. I like it. If you notice, whoa, overvoltage. What?

**Dave Jones:** Overvoltage protection fail. What's going on here, folks? Haven't seen this before. Overvoltage protection in the chat in the channel two. Please push shift OV uh OV preset key to clear the OVP status and reset. Oh, well, there you go. I

**Dave Jones:** have never seen that before. Uh shift OVP preset. There we go. I get uh 34. There we go. 30 because channel two I don't know why it's set to 34 V. Maybe I was uh playing around with it. But why set it to 34 V if it's not

**Dave Jones:** actually capable of doing that? Crazy. So, feature-wise on the unit here, we've got it's actually quite, you know, quite well equipped. It's got overcurrent protection, of course, we'll take a look at uh the OVP reset there is to reset the overvoltage protection if

**Dave Jones:** it trips. The overvoltage protection is down here, so you can set all each maximum output voltage for each independent channel or switch it off if it goes over. You know, like if the power supply fails, fantastic um you

**Dave Jones:** know, protection stuff you don't normally get on uh low-end supplies. We've got independent parallel and serial mode here. Auto is it doesn't make sense, right? What's auto on a power supply? It's actually um automatic uh sequence. So, you can set up a

**Dave Jones:** sequence of events in this thing and then you can run it by pressing the auto button. You can get into the comms. It's got uh recall and uh preset um stuff. So, various uh front panel settings, you can recall and preset those. This

**Dave Jones:** mysterious button called FC down here actually sets the uh digit um un- believe it or not sets the digit that you're using when you adjust uh the voltages here with the knob and stuff like that. Step is just it actually just

**Dave Jones:** displays what uh you're um stepping at. You can't actually set it. So, you know, I don't know why they dedicated a key to that. It's bloody ridiculous. Um you've got your output on off button, which is combined as we'll take a look at. Um you

**Dave Jones:** can actually switch the uh beep off if you find that uh beep really annoying, you can go boom like that and it shouldn't, hopefully, beep at you anymore. It doesn't. Silent. Ah, there you go. And uh W um resets uh factory

**Dave Jones:** defaults. You can adjust the contrast and you've got some cursor keys to do stuff here. A lot of functionality in this thing, but convoluted layout. Now, when I first got this thing, it took me ages because I course I didn't

**Dave Jones:** read the manual. Of course, you know, it it's a power supply. You should just be able to walk up and use the damn thing. And it took me ages to figure out how to adjust voltages with the knob and set

**Dave Jones:** the on off the outputs on and off and independent like that. And well, let me show you so you don't have to go through the same grief. You can read the manual. The manual's okay-ish, but you know, uh well, it could be a lot

**Dave Jones:** better, that's for sure. And the user interface could be a hell of a lot better, that's for sure. Now, if you want to adjust the voltage, at the moment, all none of the channels are selected. So, if we press V set over here, it you

**Dave Jones:** know, we can't set the voltage, we can't set the current, we can't type in values, we can't use the knob. So, it's almost like an automatic key lock kind of thing, which is actually quite a good feature. You can't just accidentally

**Dave Jones:** bump it and you know, adjust your outputs accidentally and blow up your circuit. So, that's pretty good. So, let's say you want to adjust the voltage and current on channel one. You've actually got to press shift channel one here and channel one is now

**Dave Jones:** selected. So, now, no, you can't just go in and use your knob like that. You've actually got to go V set and you still can't use your knob like that, folks. Hate not being able to use your knob.

**Dave Jones:** It's ridiculous. Took me ages to figure out you've got to actually press it and then you're in knob mode like that. And yes, the output does change live even though you just you press enter to sort of, you know,

**Dave Jones:** lock it in and go out of that mode, but it does actually change live and I'll show you that. So, V set, there it is, jump in and you can adjust the least significant digit. As I said, this FC

**Dave Jones:** button here allows you to jump over a digit like that and like that. You can't jump to the 10 volt digit though, it doesn't let you do that presumably cuz it's too big a step and you might blow up your circuit

**Dave Jones:** cuz you don't know what you're doing. Dummy mode. Anyway, you know, as long as you once you know, it's not too bad. You know, you can get used to that. Now, as I said, you can't just push the buttons like this, it beeps at

**Dave Jones:** you. You if you want to type in a voltage, you've got to set enter and it jumps to 10.12. Not a problem.

**Dave Jones:** And it's the same deal with the current as well. You go into current like that, you press that and you can adjust your knob and then you can go up in your settings like that. So, it's not too bad

**Dave Jones:** or you can just type in the value and by the way, really annoying. Like you can't just go point two three, right? It automatically jumps to two like that. So, you've actually got to go it's same with the voltage. You've got to go not

**Dave Jones:** point two three. Geez, thank you very much. Okay. Hopefully, you think it would just assume the zero. This is little firmware annoying issues like that which just ruin the experience on this thing. And look what happens if we actually go

**Dave Jones:** into V here and we go into knob mode. Now, it didn't recognize that press and we're going jumping around like that and we just start typing in a value. Look, it's just putting 50 over there. Like, you know, 5.00.

**Dave Jones:** So, you can type on top, yet it's left all the garbage underneath. I mean, it's just Look, and it didn't even recognize that. It didn't even recognize that at all. I mean, it's just Like, why let you even

**Dave Jones:** do that? It's just It's just madness. It's pure madness. You know, 10.1 2. Look, enter. Like, oh, and then now it'll accept it. What? Oh, man. And yes, I'll state what everyone's thinking. It's typical of these cheap Chinese designed units. Nothing against

**Dave Jones:** China. It's just you know, they can produce good products if they really want to. But these companies, they you know, just get it working and they don't put any thought into the user interface at all and they build them down to a price.

**Dave Jones:** They you know, functionality wise, spec wise, it's probably quite good value for money and it's probably reasonably designed and built inside, but they always lack the user interface. They're just awful. So, really, you know, they could have dumped the recall key, the independent

**Dave Jones:** key, the auto key, the overcurrent protection key, the overvoltage protection set, this FC button, and you know, put those as shift functions somewhere else and had more usable dedicated keys on the thing. And I show you that this knob does

**Dave Jones:** actually adjust the output live because you may not believe it unless you actually try it. It's you know, it doesn't like tell you stuff like that, you know, in the manual. You've just got to sort of try it for yourself. So, with

**Dave Jones:** channel one selected, let's go in uh voltage select, boom, and we can see it. There we go. We can see it jump up there on the meter. And of course, it's bang on as we'll check. But yeah, there you go. It does

**Dave Jones:** update live and the enter is just to get you out of that mode and effectively go back into sort of key lock mode. And let's just try the parallel and serial mode. I've got it set to ohms here. As

**Dave Jones:** you can see, totally isolated between all the channels, you know, not a problem at all. So, if we go into uh I It's not too bad that you got just that dedicated independent key just to go back, you know, just uh just give me all

**Dave Jones:** independent channels, but uh on its own, you know, it's it's a waste of key. They could have used it for something else. But anyway, let's go into uh independent mode here. And you think you'd be able to use the buttons, right? You think

**Dave Jones:** you'd be able to use these cursor keys here. No, you can't, right? Like stupid. It's just like crazy. And you got to And the knob only goes one way, right? It just goes, you know, I uh it's I

**Dave Jones:** I give up. This thing's hopeless. Anyway, um enter. Let's go parallel, okay? So, these two parallel by parallel and mode, it's uh parallel and serial mode only operate on channel one and channel two. And it doesn't tell you that.

**Dave Jones:** So, if we switch our parallel mode here, it should parallel these two channels up. This one is always going to be an independent this 0 to 6 V at 3 amp always going to be an independent of these two. So, it only operates on

**Dave Jones:** channel one, channel two. Would have been nice to tell you, but anyway, parallel we should see them parallel up. And they haven't. Why haven't they parallel up? We're in auto mode. No, hang on.

**Dave Jones:** Parallel out. Set. What the hell? Uh, there you go. You've got to actually go out of bloody auto mode here, and you've got to go into independent mode, and then let's try that one more time for the dummies. Parallel, boom, there

**Dave Jones:** it is. It's switched the two outputs in parallel. And if we try the series mode, we'll find that it actually shorts the positive and negative here as you traditionally would do so that it can give you a positive and negative common

**Dave Jones:** ground output supply for op-amps and stuff like that, really handy. So, we'll go down here. We'll go series, and bingo, there it goes. It just shorted those two pins. So, that's our parallel serial mode makes up for the fact that

**Dave Jones:** you don't actually get one of those traditional shorting bars and the fact that the positive and negative terminals aren't next to each other like that, cuz that's how you traditionally do it before you slide a shorting bar across

**Dave Jones:** and you can short out the two. This one does it with relays inside, nice and handy. I like it. And they've got two earth terminals which is marked ground. Yeah, whatever you want to call it. So, you know, it's handy to have two. I

**Dave Jones:** mean, obviously you can just strap say, you know, that one if you had them in series mode, then you could strap the two like that, or you could strap them side by side. They don't give you a shorting bar to actually do that, but

**Dave Jones:** most of the time you go into use these things as independent floating outputs. And yes, they are standard 19 mm spacing. Not that handy on a power supply, but they've done that, and they've even done that for the ground as well. They've

**Dave Jones:** just standardized right across the front of that on the spacing. Now, as for the binding post input, you saw that they do have a standard banana plug inputs. And at first glance, they do look like reasonable quality binding posts, if a

**Dave Jones:** little small, of course, but you get that with a standard 19 mm spacing. But if you open them up, yeah, they do come all the way off. Great, so you can put you know, ring lugs over them and stuff

**Dave Jones:** like that. But and they do have a hole in there, as you can see, to put your wire through like that. But one thing I don't like is that they don't have the full metal base on them or on the back

**Dave Jones:** of the binding post like this. It's just a little small thing, but yeah, they're not that they're not the highest quality binding posts I've seen, but they're reasonable for the price. It could have been worse. At least they do have the

**Dave Jones:** hole that you can put your wire through anyway. Now, of course, what you pay the big money for on this thing is not only the PC programmability, but the precision of the thing. As I said, the specs in this thing are very impressive.

**Dave Jones:** Let me uh point them out. You can have a look at the data sheet for yourself, but the voltage set accuracy specified at 25° is less than or equal to 0.05% plus 10 mV or plus 20 mV when the rated

**Dave Jones:** output voltage is greater than 36 V. Huh? Doesn't sound right. It can't go to 36 V anyway. Crazy. Oh, these Jinglish specs, I don't know. But anyway, the current is also less than or equal to 0.1% plus 5

**Dave Jones:** mA or plus 10 mA when the rated current's greater than 3 A. And of course, ripple's pretty good. It's less than 1 mV RMS over the 20 MHz range for voltage and less than 3 mA RMS over that same 20 MHz range for the

**Dave Jones:** current, as well. Uh temperature coefficient, 100 ppm plus 3 mV. Here we go. I may as well show you here on the sheet. Read back resolution 10 millivolts as you saw resolution on display and 1 milliamp current resolution there. 2

**Dave Jones:** milliamps if the rated current is greater than 3, so maybe it switches range there or switches current measurement range or something there. The response time from 10 to 90% less than 100 milliseconds for rise and fall is less than 10 milliseconds if it's

**Dave Jones:** greater than 10% rated load and temperature read back coefficient less than 100 ppm. So, you know, you're talking about a serious bit of kit when it's 0.05% and that's what you're paying for. You're paying for the ability when

**Dave Jones:** you set this thing to 10.00 volts, that's what you damn well want and that's what you expect. So, let's check it out. The Fluke multimeters are similar order, of course, I could get out my higher precision bench meter, but

**Dave Jones:** let's not gild the lily here, shall we? So, channel one, let's switch it on. In fact, let's Oh, I switched all of them on. There we go. Look, you can accidentally do that sort of thing with this if you're not careful. I just

**Dave Jones:** switched all three channels on at once because I didn't deselect it. And by the way, you want to deselect, it's not obvious. We're selected. No. There we go. We selected channel one there. So, now we're only operate on

**Dave Jones:** channel No. Look. Look, it just switched them all off. What the freak? Are you kidding me? It just switched I had channel one selected. You saw it there and the output should just work on channel one. But no, look, it switched

**Dave Jones:** them all on. What the hell is going on here? Do you what? Because it's in series mode? Maybe? Sorry, let's just hit that magic independent button there. Let's try it again. There we go. Now it seems to be working.

**Dave Jones:** Let's try that series parallel mode again. This That's a bad bug if that's the case cuz it switched on channel three. I can understand switching on one and two at the same time. It has to, but to switch

**Dave Jones:** on three, that's got to be a bug. So, let's choose Okay, series mode. Okay, so we're in series mode now, and let's turn on channel one. I'll put on off. There we go. It's a bug. So, when you're in series mode, and

**Dave Jones:** presumably it'll do that in parallel mode as well, it switches on channel three. That is ridiculous, folks. So, let's select channel three. No. Unbelievable. And that's the thing. Like, ever since I started using this thing, I'm always finding something new and stupid and

**Dave Jones:** something wrong with the firmware that doesn't operate the way you expect, or it's buggy, or it just, you know, beeps at you and does nothing cuz you're in the wrong stupid mode or something like that. It's just really incredibly annoying. Ah, God.

**Dave Jones:** Anyway, let's switch them all on. And, of course, here you go. There we go. We're basically bang-on uh 10 V there. So, the good thing is its spec is actually better than the least significant digit there. So, when you

**Dave Jones:** see 10.00 there, you can be pretty darn sure you're going to get 10.00 out of this thing. So, let's go into uh channel one and set the voltage 1 V. Look, not Look, it didn't even do that. Unbel-

**Dave Jones:** Look, 1 V. Thank you. Look, it assumes that it's 10 V. It's stupid. Why do I have to go 1. Look, what? 1.000 V. Look, it's not You've got to be [ __ ] me. No, it's not letting me set change this voltage

**Dave Jones:** on channel one when we're in series mode. It's not letting me. I should be able to change channel one or channel two, and they should it should they should track. They should just track each other, and it it does it's not

**Dave Jones:** letting me change this. Why? Unbelievable. Let's go to channel two, right? I'm selecting channel two now, and let's go. Voltage set, 1 V. It's not letting me set it. Are you kidding me? Channel three. Can I change the voltage on channel on channel three?

**Dave Jones:** Yeah, I can change the voltage on channel three, but I can't change it on channel one or two because they're in series mode. How the hell do you change the voltage? I haven't done this before. Bloody hell. Now, if you read the bloody

**Dave Jones:** manual, it says that channel two is the master. There we go. In series and parallel mode, channel two is the master, channel one output automatically follows channel two output. Fine. Let's go to channel two. Channel two, there we go. We should be able to V set.

**Dave Jones:** Push that. There we go. We can now adjust it. But you saw it before, it didn't bloody well do it. And look, it's not automatically changing the digits on channel one there. So, even though it knows it's in series mode, it's not

**Dave Jones:** going to change that. I mean, is that a feature or a bug? You decide, right? 10.25 enter. Look, right? It hasn't changed it. In series mode, it's not a live output like it was. Is it? Yeah, look. Folks, we're in independent

**Dave Jones:** mode uh sorry, series mode. Okay? These are supposed to be tracking. It is not live tracking. Okay? Look, it's live tracking on channel two, which is the master, but it doesn't automatically live track channel one. That is ridiculous. Look,

**Dave Jones:** if we switch it over, if we press enter, I bet you it tracks it. No? No, it didn't track it. It's supposed to be series mode. Are you [ __ ] me? And I just used the keypad to do it, and it switched. Watch

**Dave Jones:** this, right? I'm on channel two. Okay, so channel two is selected. I voltage set 10 V. Not a problem. It changes and it tracks, right? But if you use the knob, it doesn't let you do it. It allows you It sets them independently.

**Dave Jones:** And but that's got to be a bug because it's not a feature cuz you can't change channel one unless you go back into independent mode, change it first, go back in, and learn the It It's just It's stupid. It's

**Dave Jones:** [ __ ] All right, let's try the same thing in parallel mode. And of course, there we go. We're bang on 10 volts there. All right, on both because they're actually tied together. They're shorted by the relays in parallel. So, and they

**Dave Jones:** would load share as well. I'm sure, you know, there's internal load balancing resistor in there and it balances out, not a problem. So, let's go to channel two, which is our master channel. Nice if you You know, actually You know, look, you wouldn't be

**Dave Jones:** able to just walk up to this thing on the bench and start using it if you haven't seen it before. It You just You just toss it in the bin because it's just You wouldn't be able to figure out

**Dave Jones:** how to use it. It'd take you half an hour to figure out how to get the damn thing working if you didn't have the manual. Unbelievable. So, So, anyway, let's get in there, set up What do we want? V set. Right.

**Dave Jones:** Let's go 20 volts. There we go. Of course, it's not a problem at all. It's working fine there because it's parallel mode. So, that independent mode, let's try Hang on. No, that's the keypad, sorry. Let's do this. There we go. It's following. Okay. It's

**Dave Jones:** live following now. But it's just reading back. So, well, of course, it's going to be accurate when it reads back. There's a bit of lag there on the uh on that channel. 20.59, but okay, seems to be working.

**Dave Jones:** So, let's check out the accuracy difference in parallel mode as opposed to independent mode. I've set it for 1 volt there and we're 0.9963. I mean, we're getting more down into the 0.05% plus 10 millivolts down in there,

**Dave Jones:** but let's now switch that to independent. Annoying. Channel 1, voltage set 1 enter. 1 volt 0.9964. Okay, so it's the same. Channel 3 is within spec. There we go, 0.88. It's just within the spec there. Channel 2 absolutely absolutely

**Dave Jones:** tracks our channel 1. We're in independent mode here, too, by the way. And yes, I have double-checked this with a second meter and it's a spot-on, of course. I do keep my meters within cal here. And up at 30 volts there, yes, we

**Dave Jones:** are within spec. Not a problem. Now, one thing that does work well on this is that the fact that it when you're actually have the outputs on, it displays the the actual output current. But of course, when you switch all those

**Dave Jones:** outputs if you well, if you switch the one output or all of them off, any combination, then it displays the set current, 1.5 amps. So, let's check the accuracy of this. So, let's connect it and you should to the current mode short

**Dave Jones:** out the output and you should hear the fan whoop, go up. You heard the relay switching there. There we go, 0.993. It's displaying 1.001 and it's set to 1.000. So, that is within the current spec of uh 0.1%

**Dave Jones:** plus 5 milliamps. Not a problem. And the second channel there, yep, not a drama. And let's try the third channel. There we go. Yep, all within spec. And we can get it to spark here, folks, cuz we are up at 30 volts, so

**Dave Jones:** Yeah, now we're talking. Let's just abuse the hell out of this sucker and see if it survives. Woohoo!

**Dave Jones:** Not a problem. And there we are. We're bang on, well, on the meter and a little bit off on the displayed current there, but certainly well within published specs at 5 amp current there. I've switched it down to 1 volt so we're not

**Dave Jones:** getting a huge massive spark when we do that. There we go, 5 amps and channel 3 should be 3 amps. Maximum 2.999, 3.016. All well within spec. Nice. And if we try it right down at 10 milliamps current, there it is. It's drawing 10

**Dave Jones:** milliamps there. I've got it set to constant current and of course, you know, it's going to be near enough. There we go. That's a certainly well within spec right down at that and the display is spot on. Two least significant digits. This one's

**Dave Jones:** four least significant digits out, but there you go. It's drawing close enough to 10 milliamps so and that's not too bad. I mean, you're right down in the noise and right down in the resolution and the noise of the specs, so to speak,

**Dave Jones:** right down at that bottom end of the range, but certainly not a problem. Now, what I'm going to do here is I'm going to measure the noise performance of this thing and I've got my Agilent scope here, bandwidth limited by the way to 20

**Dave Jones:** megahertz cuz that's a spec. It's very important. The spec says less than 1 millivolt RMS over the range. There it is, 20 hertz to 20 megahertz, okay? So it's important that you put that bandwidth limit in. If you

**Dave Jones:** don't, you'll see the noise increase there, the peak to peak noise. So you've got to have that bandwidth limit on. 20 megahertz, the arm we're looking for less than 1 millivolt RMS and RMS is the key. The spec is not peak to peak noise,

**Dave Jones:** it's RMS noise and there it is, it's less than 1 millivolt. So it's doing in but look at this horrible output here. Look at this switching. We're at 5 microseconds per division, three divisions there. And we're looking at

**Dave Jones:** you know around about 66 kHz switching frequency there. What is the issue here? Well, I'm not actually going to tell you. I'm going to leave that for a quick little separate video coming up. Okay, so that'll be a

**Dave Jones:** little aside video. I won't explain it here. But this noise is not coming from this power supply. And here we go. If we have a look at our noise performance here, we'll use our Rigol. We're on 1 mV

**Dave Jones:** per division there. And you know, RMS like the RMS figure is the one we're actually looking at there 700 microvolts or thereabouts. This is only for an 8 MHz bandwidth. The probe is on times one. Let's try and on times 10.

**Dave Jones:** And there we go. We can only go down to 5 mV per division on the times 10, but you know, we're down in the millivolt region. I mean, you know, I'm not going to muck around any further. It's good enough. That's at no load by

**Dave Jones:** the way. That's on the channel three output at 6 V. And it's about the same there on channel one on the 30 V range. And just for kicks, we'll try this on the Agilent as well. There are the RMS

**Dave Jones:** noise figures there for times one probe there with an 8 MHz bandwidth. So, not too bad. And here it is with the 30 V 1 amp load. It's not switched on yet. So, that's no load and now load. There we go. Not a problem. So, we

**Dave Jones:** are drawing 1 amp down there. 30 V. Yeah, it is basically bang on to our power supply there. And our noise doesn't really change. Let's bump it all the way up. And our noise doesn't increase at all at 30 V at 4 amps, but I

**Dave Jones:** set that for 5 amps. Why is it four? Yeah, it's going on here, folks. Um we have been diddled. I've I've got this uh set the current limit is set to uh 5 amps on this channel here. And you can see

**Dave Jones:** it. If I switch it off, there it is, 5 amps, but uh it just ain't Well, now it's delivering 5 amps, but it's going in constant current uh mode. So, maybe we're switching over. Let's tweak that down. There, there we

**Dave Jones:** go. We're going up. And now it's delivering It's trying to deliver 5 volts at 4 amps uh 5 amps. Sorry, 30 volts at 5 amps, but it's just uh it's there's something happening there. So, anyway, I'm not sure what's

**Dave Jones:** going on there, but let's just check the 5-amp ripple, and there we go. It's uh bugger all, really. So, um not a problem in constant current mode, but this thing's going in a constant current. So, it can't deliver.

**Dave Jones:** I don't I can't see how it can deliver. It's rated 30 volts, 5 amps, and that's only with one channel connected. Let's try channel two. Uh we seem to be getting the same performance. Uh there we go, 4.9. No,

**Dave Jones:** it's See, it just dropped down to four. What the hell is going on here? I'm setting this to 5-amp constant current, and it does not like that at all. And there we go. I just switched it down to 20 volts, and I heard the relay

**Dave Jones:** inside click. So, it obviously went to another transformer tap, and not a problem. It's able to deliver the uh 5 amps, not a problem at 20 volts, but it certainly can't do it at 30. So, there's a limitation. There's

**Dave Jones:** performance limitations here which they're not telling you in the specs. I mean, there's no, you know, uh power uh load curves on this thing or anything. No uh power performance curves, really. So, yeah, um don't take it at face value.

**Dave Jones:** And I got channel three hooked up, and I'm trying to deliver 6 volts at uh 3 amps, but it's not it's not having a bar of that. There it is, 6 volts 3 amps, but it can't do that. Let's see if it

**Dave Jones:** can do it at 5 volts. Nope. If we have a look at our uh waveform over here, that's at uh three That's at 3 amps um constant current mode, and that's 50 millivolts per division. So, yeah, that's at uh 3 amps. Let's try

**Dave Jones:** 2.9 amps. There we go. Not a problem, so it really craps out if you try and get right near the limits. Right, so I've got my uh current up here set to say 2.9 amps, okay? So, it's trying to

**Dave Jones:** draw it is drawing 2.9 amps, and uh it is doing it at 6 volts. So, it is able to do that, and my current set down here, oops, 3 amps current limit down there. So, yeah, it's able to do very close to its

**Dave Jones:** limit there. And of course, there appears to be a bit of discrepancy here, 5.91 volts. I mean, this is a precision uh load, this BK Precision um 8500. It's a 0.05% class as well, but it's dropped. That's just the leads I've got here. The um

**Dave Jones:** display itself is actually measuring right on the terminals, and if we we can confirm that with the meter over here. There it is, 5.997, so that's just the drop on the leads, no worries. All right. Now, let's test its uh

**Dave Jones:** switch-on performance. Uh going on channel three, 6 volts 3 amps. See if it overshoots at all. I've got the uh scope set up to single-shot capture, so we switch it on. Boom. Look at that transition. Ramps perfect linear ramp, no overshoot at

**Dave Jones:** all. Very clean. Nice. And that's with a full load, too, by the way. So, let's uh try it again with no load. So, we'll switch our load off here. And let's reset this. Change our Switch our output off. Switch our output on. And boom.

**Dave Jones:** Look at that. There we go. With no load, yeah, it's much uh quicker. Of course, I didn't uh change the time base there at all. And uh ramps up. There's no overshoot in there. What's Oh, look, there's a little There

**Dave Jones:** you go. You didn't see that when you're uh There you go. You zoom in. There's a bit of funny business happening there. That's uh with no load. So, you know, that might cause an issue with your uh system if uh

**Dave Jones:** that was a problem. So, there you go. That's noteworthy. Definitely. So, let's uh try, say, uh an amp. So, we'll set this to 1 amp. And is it No. Uh I set 1 amp. Boom. Okay. Now, we're set for an

**Dave Jones:** amp. Let's try that again. Output. The output is on. All right. And there you go. That's for a 1-amp constant current load, by the way, which isn't the best. We'll do it again with a um uh We'll do it again with a resistive uh

**Dave Jones:** pure resistive load to see if that makes a difference. But of course, the uh no load had that uh funny business. So, even with the constant current load, it's um you know, it's pretty perfect. Okay, let's try that again. I've got a

**Dave Jones:** pure resistive uh loaded here. It's not a wire wire-wound resistor. It's a 10-ohm uh load. So, at 6 volts here, we're only going to get 0.6 amps. But uh let's give that a shot, shall we? And see what we get. There we go. We're

**Dave Jones:** getting that same getting that same business there happening at 0.6 amps with at uh 6 volts. But of course, the most important thing is there is no overshoot, virtually no overshoot there. I mean, you know, there's a little bit

**Dave Jones:** little half a bee stick of overshoot there with a little bit of recovery, but yeah, that's Yep, that passes. All right, let's try the same thing again. Got our 10 amp resistive load 20 volts output on channel 1 5 amp current limit.

**Dave Jones:** So, it's only going to draw 40 volts. It'll only give us 2 amps on the output, but let's uh ramp that up and well, we'll have to change that to uh uh 5 volts per division. Okay, we'll give it a go. Single shot mode, output

**Dave Jones:** off, and output on. Bingo. Look at that. Nice and clean. I like that. Not a problem. That's a um switch on for a 40 watt uh load. That's at uh 2 milliseconds per division. So, that's taking uh 1 millisecond. So, that's

**Dave Jones:** taking about 2 milliseconds to uh switch on there for uh 5 10 15 20 volts, of course, for 40 watts at 2 amps output. Nice. Okay, let's try the switch off, shall we? Let's give it a go. Output,

**Dave Jones:** let's move our trigger up a bit. There we go. No output. Hey, there we go. Let's try that one more time for the dummies. We're on. And there we go. Clean switch off. Not a problem whatsoever. Now, I know what

**Dave Jones:** you're thinking. This BK Precision uh electronic load has a bit of a reputation as a power supply killer. So, let's muck around with the uh uh constant power and constant resistance modes. Here we go. I've got constant uh

**Dave Jones:** power mode set to uh 90 watts there. I've got 20 volts output. So, um it should give us just under the uh 5 amp uh current limit. So, let's switch that on. No worries. 4.5 amps, not a problem. Let's uh see what

**Dave Jones:** the uh switch on performance is. And there we go. That's our load switch on. We're 10 mV per division there. Um 40 Sorry, 90 W constant power mode. It only dropped about you know, 15 mV or thereabouts and recovered pretty

**Dave Jones:** quickly. Nice. And let's do that again, but switch off. Boom. There we go. Not bad at all. And let's do the same thing again, 20 V but with my 10 amp resistive load and bang, put it in there. Yeah,

**Dave Jones:** we've got some bounce there. That's my contact bounce, but not a problem. And I've got constant resistance mode set to 4.1 ohms and it's you know, it's handling the switch on of that no problems whatsoever. If I capture that

**Dave Jones:** on the scope, there it is. Not a problem. Let's go really nasty and constant resistance mode, 1 ohm. So it's definitely you know, it's not going to try and draw What? It's going to try and draw 20 amps, but it's going to be limited to

**Dave Jones:** current limited to the 5 amps there. So Woah. Look at that. It's oscillating. Woah. Will it kill it? Will it kill it? I love it. Listen to that.

**Dave Jones:** How long should we leave that going for? And of course it won't do that if you simply short the output. It'll just go into 5 amp current limit. So that's a unique quirk of the constant resistance mode when the thing's trying to hunt to do

**Dave Jones:** the constant resistance. That load is quickly cycling and the power supply going, "Ooh, I don't know what to do. Don't know what to do. Quick, switch relay. Switch relay. It's panic. Panic." But there you go. To its credit, it's

**Dave Jones:** survived that and it's surviving just shorts on the output as well. 5 amps constant current. So it lives to power another day. Not a problem. It's not like that Korad rubbish. There you go. I've got it on constant resistance mode

**Dave Jones:** again at 1 ohm on the uh three this time. 6 volts, there's no relays clicking, it's not uh changing um transformer taps. So, it's uh there we go. It's just jumping in and out of that 3 amp, doesn't know what to

**Dave Jones:** do. 6 volts 0.1 watt. And you can hear the fan just revving up and revving down each time it does it. All right. Now, what I want to do is capture it jumping a transformer tap. So, I've got it on 5 volts at the

**Dave Jones:** moment. And so, there it is, 5 volts per division. And we'll jump up to say 20 volts. And uh we'll try and capture that. So, trigger point is just above 5 volts. So, we'll go voltage set, and we'll go 20, and see what happens when

**Dave Jones:** it jumps. There we go. Nice linear ramp up there, constant uh current mode, and no overshoot, nothing when it changes taps. Very nice. And we'll capture that again with a uh 10 ohm resistive load. So, we'll go from 5 up to 20.

**Dave Jones:** Beautiful. Look at that. A little bit of a little bit of funny business happening there, but um yeah, it doesn't overshoot. That's the main thing. Let's try that again, just up to 30 volts. See what happens. Woohoo! Look at that.

**Dave Jones:** But it does actually recover. There we go. Two-step process as it goes through. Maybe a couple of uh taps there uh through two taps and then up to the final 30 volt. So, that was with a 10 ohm load. So, at 30 volts, that's

**Dave Jones:** jumping up to a 90 watt load. So, let's try that again, but uh with no load, shall we? So, we'll go back down to 5 volts, and we'll jump up to 30 volts. Bang! Look at that. Not a problem whatsoever. And what

**Dave Jones:** happens when we go back to 20 volts under load? Well, let's uh set our falling edge uh trigger there and we're at 20 volts and we've got our 10 ohm resistive load on there drawing 2 amps and let's go down to our 5 volts

**Dave Jones:** and see what happens. There we go. Nice ramp down. Beautiful. Think I'm getting the hang of using this thing. There we go. Look at that. All right, let's see what happens when we go from no load into constant current mode. So, let's

**Dave Jones:** capture that. Whoa, look at that. There we go. Let's try that again. Boom, look at that. So, we had some bounce there. So, let's look at that. Yeah, that's probably some bounce from our contacts there. It's jumped down. That's 2 volts

**Dave Jones:** per division. So, it's jumped down in voltage of course and then ramped back up. Let's try that again but in DC coupled mode, 1 volt per division so we can actually see the real drop in voltage and here we go.

**Dave Jones:** Boom, look at that. Nice and clean. And let's see how accurate the constant current mode is. Let's our constant current is set for 3 amps. Okay, we're currently drawing 2.995, 2.996 and of course the voltage hasn't dropped. And let's see if we get very

**Dave Jones:** close to that 3 amps. It should switch into constant current mode. Yeah, hang on. Yeah, there we go. Bang. Right on target. Now, I've had this thing going on a decent load for about 30 odd minutes now. I've got 40 watts

**Dave Jones:** load on channel one. I've got 120 watts load on channel two and I've got a 18 watt load on channel three here and I've got my temperature probe and the temperature around back it's not coming out of the fan. I mean,

**Dave Jones:** in fan's going full ball, and we're only getting, you know, 37 38° or thereabouts out of the fan. So, the thing really isn't getting that hot at all. Now, what we're going to do is try and find where

**Dave Jones:** the tap voltage on for the 30 V is. So, I'm ramping down 30 V. Once again, I got that full load happening on there. So, let's wait for the relay click. And up, there we go. So, about 23 V. Let's go up.

**Dave Jones:** Yep, 23.2 V is where that uh tap kicks in. And we should see that temperature go up, and we do because it's now dissipating more being a linear regulator. Um at 24.4 V, of course, it's dissipating more power in the heat sinks. There we go,

**Dave Jones:** we're over 40 now, and I've just had it running for a minute. So, that's going to uh climb up. So, it um the temperature of the heat sinks and its final and its final capacity before any sort of thermal cutoff uh comes in if it

**Dave Jones:** does actually have that. Then, uh we should uh get that. Um you you would have to stress it at the uh lowest point of each uh tap range. So, it's dissipating the uh most amount of voltage drop where it's got the biggest

**Dave Jones:** voltage drop across the uh pass transistor. So, there you go, but it did actually go up in temperature as expected. And the next tap here seems to be about just under 15. Yeah, 14.8 V there, and jumps back up at 15.2. And the bottom

**Dave Jones:** tap about 7.6 V. And by the way, there's one other thing that's uh noteworthy is that after all these uh load tests, um it's still within spec on uh its uh output voltage and output current. So, yeah, drift doesn't seem to be a problem. Now,

**Dave Jones:** yet another confusing thing on this is the store recall mode. Now, you might think that that stores and recalls voltage and current settings for the three channels, but it's not necessarily the case. It has to do with this auto

**Dave Jones:** programming mode and it's and the manual really doesn't explain it. It's ridiculous. Now, what it actually is, if you go into store mode here, then it gives you these various channels. Oh, we can't use the cursor keys there. We're just going to scroll

**Dave Jones:** through, okay? And it has to do with channel 1, channel 2, and channel 3. So, the different settings. So, let's go say we want the auto sequence set up the auto sequence for channel 1 output. Let's go into that, channel 1, and then

**Dave Jones:** it has these various storage options. And whoa, we can finally use our cursor keys. Look at this, folks. We can scroll around and yes, it's got up to I think 15. No, what is it? No, heaps. 30. 30 uh uh

**Dave Jones:** program steps effectively per channel. So, we go up here and this is the voltage and the current and then the delay time in seconds. So, we can set our voltage, you know, we can I've already set it there 1 and then we can set it to uh 1

**Dave Jones:** amp there for 1 second. So, we want that to stay in that mode for 1 second and then sequence through to the next one. And then if you scroll through the list here and you go and highlight say the

**Dave Jones:** third one and you press auto, then that puts that little uh cursor down there and I'm presuming it'll stop when it gets to that point um in the program sequence. So, it'll go through those two steps, but it doesn't tell you. I'm

**Dave Jones:** going to set This is channel 1 only. So, we're going to cycle through 1 V um at uh 1 amp, not that the current limit matters. We won't be using it, but you can set it up anyway. For 1 second.

**Dave Jones:** So, then it'll jump to 2 volts for 1 second and 3 volts for 1 second and should stop when it gets to the end of that point. So, it should cycle through all three of those. Let's see if we can

**Dave Jones:** capture it. All right, so we stored our program. There it is. It's in there. Let's get out of that. And no, you can't recall it. Okay, what you got to do is you just all you do is you run it, okay? So, you put

**Dave Jones:** it in auto mode like this. There we go. I've got auto mode and then you press the output button and all three channels will turn on. You don't have to individually turn them on, stuff like that. So, you press it and we'll now

**Dave Jones:** find that channel one is cycling 1 2 3 volts. You can't see the set current because the set This is the displayed current, but bingo, there you go. And if you capture that on the scope, ta-da, folks. There it is. That's what

**Dave Jones:** we have. There we go. That's 1 volt per division, so it goes 1 volt for a second. Let's horizontal position that. There we go. It's reasonably accurate. So, it jumps up to one 1 volt, 2 volts, 3 volts and

**Dave Jones:** then that ramp down is because we've got no load on there, so it doesn't ramp down very quick at all. That's the output storage cap. But there you go. It is cycling through and it's continuously cycling through. And that's a good use

**Dave Jones:** for having this oscilloscope on roll mode. There you go. You can actually see it. That's 1 second per division now and you can see it cycling through and it's actually doing that in real time. So, it works. Huh. There you go. That could

**Dave Jones:** actually be quite useful. And there we go. I've actually plugged on a 10 ohm load onto that, so it's drawing 100 milliamps, 200 milliamps, 300 milliamps. And as you can see now, when it falls back down, it falls back down very

**Dave Jones:** quickly. There we go, and boom. And now I set up a sequence on all three channels. Woohoo! I'm an advanced programmer. Channel one is counting up 1 2 3 volts, channel two is counting up 4 5 6 volts

**Dave Jones:** um all with uh 1 second intervals, but you can change the uh intervals to anything you like with 1 second resolution. So, um channel three, we've got that uh cycling 3 2 1. So, that one's cycling downwards. So, there you go. That's

**Dave Jones:** actually a pretty useful feature, and you can program it, be it a bit archaically, through the um front panel user interface. So, once you know, not bad at all, but try and figure it out on your own. Uh

**Dave Jones:** and for the life of me, I cannot find a use for the actual recall button. Yeah, shift store, not a problem, but the actual recall button, whether it's in auto mode doing something, whether it's in uh out of auto mode, do it like it's

**Dave Jones:** just I don't know. I I give up, and the manual doesn't help at all. And uh it really is a shame that doesn't let you store and recall uh popular settings for the front panel. I mean, for the um

**Dave Jones:** channels, you know? Yeah, this auto sequence mode is great, but jeez, where's some just basic functionality to uh you know, presets and voltages? Now, one of the good features is overvoltage uh protection set. So, you press that, and you can set

**Dave Jones:** up the max or absolute maximum voltage for any one of your channels. So, let's say you had a real critical device under test, a real critical board on here. It's you know, 3.3 V rail, and if you went over that, you're going to blow the

**Dave Jones:** ass out of your you know, your $10,000 prototype board or something. You don't want that to happen. Could ruin your $10 million project schedule for your $10 million project. Uh right, and you'd probably be get the boot straight out the door. So,

**Dave Jones:** you don't want that to happen. So, you can go in here and you can set, you know, I don't want that thing to be over 3.4 volts and that is a separate protection circuitry which ensures that there's no way that that

**Dave Jones:** output can go over 3.4 volts or presumably there's extra circuitry in there that allows that if the power supply fails it's supposed to be an independent the whole idea is it's an independent thing that which kicks in, but may or may not be, you know,

**Dave Jones:** probably just done in software really, but still it doesn't mean it means that you can't do anything stupid to the front panel. Let's say we don't want that channel two to go over 3 volts. I've already got that for that auto

**Dave Jones:** sequence programming. Let's see if there's a bug in there. Right? So, over voltage protection on channel two. Yeah, there we go. Notice over voltage protection on channel two. Please push shift over voltage over voltage protection reset key to clear over

**Dave Jones:** voltage protection status and reset. So, there you go. We have to clear that. Up. There we go. We've cleared it and channel two it's got 6 volts there, but let's see if we can switch on the output and

**Dave Jones:** actually get 6 volts. All right, let's press the output on and Nope, it protects it. Not a problem and I'm checking on the scope over here and no it limited it and it didn't jump up at all to 6 volts. Brilliant. One really

**Dave Jones:** annoying feature is you can't just turn on channel one like that and have over voltage protection set on another channel cuz it just won't let you turn on any of the channels. It's stupid. Protect that channel. Great, but let me

**Dave Jones:** do whatever I want with the other channels, please. Now, what OCP does or overcurrent protection here does is that instead of going into current limiting mode, if you hit the current limit, it'll just switch off the output. So,

**Dave Jones:** let's give that a go, right? It's OCP is off at the moment, right? So, it I've got channel one set to 3 volts at half an amp. It'll actually attempt to draw more than that. So, let's uh go output like that. There we go. It's

**Dave Jones:** dropped It's gone into current limiting mode, okay? So, it's current limited to 500 milliamps, but it's just continuously, like a normal power supply, is continuously current limiting. But, if you don't want that, if you if it exceed if you want it uh to

**Dave Jones:** shut off when it exceeds that current limit, easy. Turn on OCP, and bingo, it just turned channel one off because we were overcurrent there. So, if we switch all of the channels, see? And if I try to switch it on,

**Dave Jones:** I briefly try to switch it on, it goes overcurrent, and just switches the channel off. That can be very useful, depending on your circumstances. And I tried to get the uh USB serial interface working on this thing. Um yes, it is just a USB uh serial

**Dave Jones:** converter, and um it rec- I insta- you know, I it recognized it when I plugged it in and installed the uh FTDI uh driver and stuff like that, but the software, well, let's just say it's as [ __ ] as the user interface on this

**Dave Jones:** thing. Couldn't get it to work, couldn't figure out how to set the parameters to wouldn't connect to it. Complete fail. Um not going to waste any more time on it. And it does actually come with a uh document which lists all of the serial

**Dave Jones:** um serial protocols to uh talk to this thing and control it. So, I guess the idea, write your own software if you want to do that. I'm not spending another second on it. So, the verdict on the Atama PPS 3205T

**Dave Jones:** three-channel precision power supply, well, it's probably a thumbs sideways. Not a thumbs down because, well, you know, I couldn't kill it. Um it does represent a good value for money, I think. And well, it ultimately does work even though it's

**Dave Jones:** a pain in the ass to drive the thing. So, because of that, the user interface stuff cannot give it a thumbs up at all, but it does represent reasonable value for a you know, a precision 0.05% that met its uh specs. Didn't quite uh meet

**Dave Jones:** the performance, um the power performance on uh the highest uh tap on the transformer, but you know, hey. Eh, it still works. It works reasonably well. It's quirky. I would actually buy some of these for the lab as a joke,

**Dave Jones:** right? Stick them in the lab and everyone will come up to it. All the engineers come up, "Oh, look at this new funky triple output power supply." And just sit back and giggle as you watch them trying to use the thing and just

**Dave Jones:** give up and toss it across the room in frustration because it really is frustrating to use, but once you get the hang of it, I guess it's going to be okay. I'm going to keep it here in the lab, use it. It'll

**Dave Jones:** probably become my main uh lab supply cuz it is so versatile. Um you know, dual 30 V output, separate uh 6 V precision. I love the precision in it. It's programmable. And that's uh sequence mode, pretty handy. Might come in useful for

**Dave Jones:** sequencing some things. So, without the need to actually um you know, hook it up to a uh a PC and actually control the thing. So, not bad at all. Yeah, thumbs sideways. I don't know. Cheap Chinese user interface.

**Dave Jones:** Bloody hell. Anyway, if you want to discuss it, jump on over to the EVBlog forum. If you like these reviews, please give them a big thumbs up. Catch you next time.
