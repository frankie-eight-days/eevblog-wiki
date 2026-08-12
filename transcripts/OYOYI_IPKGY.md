---
video_id: OYOYI_IPKGY
title: EEVblog #579 - Precision Low Current Source
url: https://www.youtube.com/watch?v=OYOYI_IPKGY
source: youtube-asr
---

**Dave Jones:** Hi. Yes, it's yet another video on a precision current source. I've done a previous video on this, a two-part one, where I designed a precision 1 amp current source. Well, as it so happens, I also need a precision 1 milliamp

**Dave Jones:** current source, and also a precision 1 microamp current source. And the LTC6655 we used in the previous videos, which I have If you haven't seen them, you should. They'll be linked in down below here. And that chip, you know, we had a

**Dave Jones:** few issues with the stability of that thing. Gave me the heebie-jeebies. So, I wanted to try another circuit which has been around for a long time, and it's been touted for that time as one of the world's best precision current sources.

**Dave Jones:** And it uses the REF102 voltage reference from Burr-Brown, the old Burr-Brown, which are now owned by TI, of course. And there's a whole application note, which once again, I'll link in down below. Check it out. It's how to use

**Dave Jones:** this REF102 10-volt voltage reference, pretty good voltage reference, which has been around for donkey's years. And you can hook an op-amp onto it, and a precision resistor, bingo, you've got yourself a low current, i.e. sub 10 milliamp, precision current source. Great. So,

**Dave Jones:** where we only want 1 milliamp here, and also 1 microamp. So, not a problem. I thought I'd give this a whirl with the REF102 and the recommended OPA 227 op-amp here. And you've got your load, standard configuration we which we

**Dave Jones:** looked at in a previous video. So, I've built it up here on a breadboard, and we'll see how it performs. You'll notice no bypass caps at all here, no load capacitors at all, not really required. They do recommend an input bypass cap,

**Dave Jones:** but not, you know, really required. The ultimate application here is going to be powered from a couple of 9 volt batteries and of course the aim of this circuit is instead of you know the ground pin here being grounded and you

**Dave Jones:** get your precision 10 volts out of your voltage reference here. What it does is it lifts that ground pin there with the op amp here and it it's still this op amp does whatever well this op amp does whatever is required to

**Dave Jones:** the ground pin here to keep the voltage reference across here 10 volts and of course it's wired as a voltage buffer so the voltage here equals the voltage here minus the offset voltage which will talk about shortly. Then you get

**Dave Jones:** that precision 10 volt voltage reference across your resistor here which can be a nice precision resistor which we're going to use here today and using Ohm's law you can calculate your load current going down to ground here. So that's all

**Dave Jones:** it is neat little trick raising the ground pin of your voltage reference. Let's see if it works. Hey we had issues last time with a application note data sheet. Let's see if this one does the business. I think it will because

**Dave Jones:** they've done a whole separate application note on it. Has been around for a long time. Fairly confident this thing's going to work at the low currents and once again thanks to Yuval at the Vishay Precision Group who supplied me samples of these very nice

**Dave Jones:** in this case VHP 100 reference resistors here 10K at .01% this series VPH 100 actually capable of better than that. I'll link in the data sheet down below. Awesome little resistors and here they are in a very nice hermetically welded sealed can like

**Dave Jones:** this. They're a bulk metal foil resistor nears almost zero temperature coefficient. You don't really have to worry about it. These are .01% but they are available in .005% values to order. So these are nice resistors. Basically no with the Z foil

**Dave Jones:** technology, basically no inductance and no capacitance rise time like 1 nanosecond. Brilliant devices for you know, high performance pulse applications, things like that. So, but fantastic for use as a precision reference resistor like we're going to use here. Oops, did I mention that these

**Dave Jones:** were Z foil technology? No, they're not. That was the resistors in the previous video. These ones are the bulk metal foil technology. They have various technologies available to give different precision and tempco's and performance and all sorts of stuff. So, these are

**Dave Jones:** slightly different to the ones we saw previously. And the good thing is you can order them in any value you want, any resistance value. Just specify it, doesn't cost any more. Awesome. And here's our little circuit, the REF102

**Dave Jones:** over here and the OPA227 which of course you need an op-amp because this is a 10 V voltage reference. We power it from like something greater than 12 V or there about. So, you need a high voltage op-amp to go along with that and the

**Dave Jones:** OPA227 does that. Only a 20 microvolt or 10 microvolt offset voltage or something. It's incredibly small. So, there you go. Don't need any bypass caps on this. I think we'll get away without it and basically we've got our input over here.

**Dave Jones:** This is our voltage input. Here's our ground and here's our output here. So, I've got the load connected directly across the output to ground. And in this case, the load is my Agilent current meter up here. So, we'll just

**Dave Jones:** you know, so basically the load is just the current shunt resistor inside here. You know, for all practical purposes, it's basically a short circuit. Power the thing down here. Set a current limit, you know, 20 milliamps, something like that just so

**Dave Jones:** nothing blows up. And uh 13 volts, I don't know. 13 sounds like a lucky number to me. So, we'll use 13 volts. We just have to be above uh 10 volts. I'm not sure what the exact value is. I

**Dave Jones:** think it's a volt or two above that we need to operate. 13's a treat. Now, it's pop quiz time, just like in the previous video. I'm actually pretty confident this circuit, as I've built and hooked up, is not going to work. It's not going

**Dave Jones:** to give our precise you know, that 10 volts across 10K resistors, not going to give our cells a precise 1 milliamp through our load here to the multimeter. And you know, if you want to try and figure it out on your own, stop the video now.

**Dave Jones:** I have actually mentioned the reason for it in a previous video. Just think about the circuit and how having a very low value load on here could affect its performance. So, there you go. If you want to go figure it out, please do.

**Dave Jones:** Otherwise, let's power it on and uh see what we get. Here we go. Channel two. On and bingo. Look at that. There you go. It is not It's not It's not It's fairly close, you know. 1.03 milliamps, but hey, we expect much,

**Dave Jones:** much better than that. So, what's going on? Hmm. Now, if we actually measure the voltage directly across the resistor there, we expect 10 volts out of our Oh, I've got the leads backwards. Will the electrons all fall out? No, that's all

**Dave Jones:** right. But look, there it is, at 10.357. Basically corresponds with the meter up there. So, it's not precisely 10 volts. So, why aren't we getting our precise uh you know, 10 volts out of our voltage reference? Hmm. Oh, by the way, uh for

**Dave Jones:** this video, I couldn't get the super-duper accurate uh C version of the REF102 voltage reference. It comes in different grades, as most voltage references do. If you check out the data sheet, if you're going to order a voltage reference, be very careful which

**Dave Jones:** one you actually order. In this case, I've got the A version, which is only a 0.1% nominal accuracy. So, you know, it's not as good as it can be. The C version is 0.025%, but in this case, our error is a

**Dave Jones:** whopping 3.5%. So, it's certainly not the REF102 that I'm using here. It's certainly not going to be our precision Vishay resistor here. Not a chance. It's not going to be our op-amp down there. Well, is it? Mhm. And if you did stop the

**Dave Jones:** video and try and uh figure it out, and I hope you did. Now, I'm The reason is very simple. This OPA277 uh op-amp, because of the very low load on here, effectively a short circuit, shorting it down to ground here, it's

**Dave Jones:** not able to There's going to be a minimum output voltage it can actually drive on there. So, we're going to actually get an error on there due to the op-amp, because it's trying to operate down near its negative rail down

**Dave Jones:** here. And even if, as mentioned in the previous video, you use a uh precision rail-to-rail op-amp, they aren't really rail-to-rail when you really get down into the, you know, 0.1% or better uh margin that we're talking at, you know,

**Dave Jones:** the really low voltages down here. Rail-to-rail might mean, you know, a 10 mV output voltage or something. Well, you know, that might be okay for a normal circuit, not for a precision current source. It's going to blow our

**Dave Jones:** error uh budget right out the window. So, what we need to do is put a, as we did last time, put a diode in series with this load to lift this voltage uh on the non-inverting input on pin three here up by about 0.6

**Dave Jones:** V or so. If we have a look at the data sheet for the OPA277 here, you'll notice our voltage output here, this is not a rail-to-rail chip, by the way, but even if it was, as I said, it still wouldn't

**Dave Jones:** be good enough. So, our minimum output voltage here is going to be our negative rail, which is ground, plus half a volt. So, you know, it's hopeless. We can't, obviously, so we need to boost the output voltage above that 0.5 V. So, one, you know,

**Dave Jones:** basic silicon diode drop of about 0.6 V should do the business, but let's actually measure it and see what value we get. So, I'll measure from the ground pin here to the output voltage, because effectively we're shorting the output

**Dave Jones:** here. So, it's, you know, driving this thing down to a minimum voltage that it can. So, let's have a look. Okay, between pin four and six, there we go, 0.46 V, close enough to that data sheet minimum value of 0.5 V. So, a one

**Dave Jones:** silicon diode drop should do the business, and once we put that in, assuming that, you know, it doesn't affect the stability of it. I don't think it will in this particular case, we should get our precise 1 V 1 mA out

**Dave Jones:** of there and our precise 10 V across our precision reference resistor. So, here we go, let's take our load here, and I've got a little 1N 4148 or something like that. So, let's put that in series with our ground, and

**Dave Jones:** ta-da! Look at that, I think we're within our standard error margin, and if we measure, of course, our voltage across our precision 10K resistor, what do we get? Ta-da! There's our precision 10 V. Awesome. So, how close are we

**Dave Jones:** there? Well, let's get our trusty calculator here. 1 0.99999 2 1, I think we're going to be really close here, folks. Times 100 to give us a percentage and we're looking at tada point double O eight percent. Beautiful. Well within

**Dave Jones:** our error budget. So speaking of our error budget, let's take a look at where some of our errors accumulate and these aren't even all of them really, you know. So you're I don't think I've actually covered them all which is

**Dave Jones:** unbelievable. Anyway, when you're doing these sorts of precision circuits, all this sort of stuff matters. It really does and you can do worst case scenarios and all sorts of things and you know, you know, worst case error budget. And

**Dave Jones:** in this case it should have been actually pretty high cuz we if we take a look at our ref 102 voltage reference, it the dominant figure here I've put them all in parts per million by the way ppm but you can easily convert between

**Dave Jones:** ppm and percentage. And if you want to do that one ppm equals point triple O one percent basically. That's pretty much what we're looking at here but anyway, the paper the dominant figure as you can see here like some of them are going to

**Dave Jones:** like be drifts with temperature and time and stuff like that. But you know, if you just start with your ball park, you know, basic you know, top level banner spec of the ref 102 for the basic initial accuracy, we're we're looking at

**Dave Jones:** you know, 250 parts per million or point O 25 percent for that C grade chip. But we don't even have the C grade chip. We've got the A crappy A grade chip that only cost a bloody dollar or something

**Dave Jones:** like that. And uh that is a thousand ppm. So that's going to dominate here a thousand ppm. So what we actually measured there just before was a value of 80 ppm. You know, different from our normal expected value assuming of course that

**Dave Jones:** our Agilent meter is absolutely precise and bang on. But yeah, so that's point double O eight percent is what we actually measured. You know, so it's well within. So, the REF102 we're actually using is 1,000 ppm adjust there

**Dave Jones:** on its data sheet accuracy. So, we're already balls in the in right there. Then, you've got other stuff like the drift with temperature is maximum worst case of 2.5 ppm per degree Celsius. So, you got to take that

**Dave Jones:** into account over temperature range. And then, you've got load regulation or the the change in the normal output value over the current. So, it's a 10 another 10 ppm per milliamp error right there. And these sort of errors can accumulate

**Dave Jones:** and interact in various different ways, which we won't go into, but REF10 So, then then we've got our line regulation, i.e., our input voltage here. How does our 10-V precision 10-V reference here change with our line or input voltage? Well, 1 ppm per volt. So,

**Dave Jones:** if we change that from 13 V that we powered it to 14 V, we'd expect a 1 ppm change. Hey, let's try that. Here we go. Here's our value. I'm on 13 V. I'm going to up it to 14 V.

**Dave Jones:** There we go. Not changing anything measurable there. No. No, it's pretty good. Anyway, that is your worst case value there. So, you could, you know, if you're really doing this for serious business, then well, you got to take that into account. It's

**Dave Jones:** all part of your error budget. Then, we've got our aging of our reference as well. Well, there's another 20 ppm per 1,000 hours of operation right there. Then, we have a look at our our op amp really isn't contributing much here at

**Dave Jones:** all. The OPA227 really the only thing we're going to worry about is the offset voltage. And the offset voltage of this, I think worst case is only 10 microvolts, which is equivalent to 1 ppm over our 10-V voltage reference. If, you know, we were

**Dave Jones:** only using a 1-V voltage reference, it'd be 10 ppm. It'd be a larger percentage of that. But, of course, if you want to eliminate that, you could use a chopper amplifier in there, of course, instead of one of these

**Dave Jones:** low offset precision references. You can even get much lower than that. If you really want to, you know, gild the lily, you can get rid of it. And then we've got our Vishay resistor here. Well, its basic accuracy is a 100 ppm or 0.01

**Dave Jones:** 0.01% there. And then you've got the stability of that over temperature and time of and stuff over 2 ppm. And then you've got other stuff like overload as well, if there's any self-heating. But, in this case, you know,

**Dave Jones:** we're not driving any significant current through this and there's no any significant power dissipation in the thing. So, really we don't care about that. But, as you can see, you know, all these things, even like a 1,000 ppm and

**Dave Jones:** all the other stuff that we could potentially add in here, we're ballsing it in. We're way better. We measured about 80 ppm. Brilliant. But, hey, maybe we're just lucky. You can't expect this to happen all the time. Okay, so we've got ourselves a

**Dave Jones:** fantastic precision 1-mA current source. But, I mentioned I also want a 1-µA one. Well, can we just up this resistor here to 10 meg? 10 V across 10 meg going to give us our 1 µA. Well, in theory, yes.

**Dave Jones:** But, in practice, no. And if you want to stop the video again, here's another pop quiz. So, you might have precisely 10 V across your precise 10-meg resistor here, giving you your precise 1 µA through that resistor, but that doesn't

**Dave Jones:** mean one microamp is going to flow down here into your load like this. Why? Because inputs of two op amps have input bias currents. So, there's going to be some of it, tiny little smidgen, you know, a couple of bee sticks is

**Dave Jones:** going to fly into the non-inverting input of that op amp. Let's go to the data sheet and find out how much. Well, here's our data sheet again, and this is what we need to know, the input bias current here for our OPA2277.

**Dave Jones:** And by the way, just be careful. This is the column for the 277. You can also get dual and quad versions of this. The different packages, typically, the especially the quad versions can have bigger input bias currents than the

**Dave Jones:** single or the dual versions. That's why they have different columns here. So, just be careful with that. So, let's go back down here. Where is it? Input bias current. Here we go. IB. Look at this. Plus minus 0.5. What?

**Dave Jones:** Nanoamps. Point So, let's take that as a nominal, you know, worst case, one one nanoamp there. And a nanoamp doesn't sound like much, but when you're around with precision current sources like this, well, get your calculator out, figure

**Dave Jones:** what 0.5 nanoamps is as an error on one on a one microamp load current there. Answer? 0.05%. So, worst case, it could be like 0.1%. So, you know, we like my goal for this thing is to be much

**Dave Jones:** better than 0.05% there. So, really, I have absolutely no confidence in this in using the OPA 277 op amp, as good as it was for 1 milliamp, no confidence, really, well, not much, at getting this thing to work at 1

**Dave Jones:** microamp. But let's try it. But unfortunately, I don't have a precision uh 10 meg resistor yet. Uh still on order. So, I've just got a crappy one, but I have actually measured its value, and it's 9.912 meg or thereabouts. So, you know, if it

**Dave Jones:** was precise, we'd expect about uh 991 nanoamps out of this thing or 0.991 microamps. There we go. Oh, getting confused with all these decimal points. And what do we get? Aha, look at that. 1.027 or so microamps. But that's rather

**Dave Jones:** curious because we actually expect it. So, that's above our nominal figure. But if you have a look at the um circuit down here, we actually expect it to be less because the it's going to suck away some of the current into here.

**Dave Jones:** So, we actually expect our current into low, which we're measuring, to be under spec, not over spec. So, we'll go back to our voltage reference here and measure it, and ta-da, we're looking at uh 10.14 V there. Aha. So, that's exactly the

**Dave Jones:** same issue we were getting last time without the diode. So, now our our circuit parameters have changed, and it looks like we're our voltage reference isn't working as well. So, we're going to put two diodes in series now. And

**Dave Jones:** what do we get? Ta-da, well, it's, you know, it's a bit lower than what it was before, but if we actually measure the reference voltage now, I think we'll find bingo. But of course, that's not precisely 10 V we're reading 9.99

**Dave Jones:** uh 8 or something before. So, I've added in a third diode in series now, and bingo. Hey, I think we've solved it. Now, the reason for that, of course, is because your voltage drop on a diode is not uh constant. It's going to vary with

**Dave Jones:** the characteristic curve of the diode, of course. Look up any data sheet for the diode, and it depends on the current flowing through the diode. That's why we need at least three in series. Once we're down at 1 microamp, there's, you

**Dave Jones:** know, bugger all voltage drop across each of those diodes now. In fact, we can measure that standard 1N4148 diode, of course. You know, any any beginner would expect 0.6 V voltage drop across that. What do you get at 1 microamp?

**Dave Jones:** Let's measure it. 0.26. There you go. You'd think it was some kick-ass Schottky, but it's not. It's just a Jove logs 1N4148 silicon diode, but hey, it's right down on the lower part of that characteristic curve for the diode, so the voltage drop

**Dave Jones:** is quite small. But, we were reading slightly under on our voltage reference here, 9.998, if you remember precisely. Put those into the calculator, and tada, 1.008 microamps. That was pretty darn close to what we were measuring before, as you'd

**Dave Jones:** expect, because this is just Ohm's law. It's got to work, as long as you take into account your op-amp, as long as you're ensuring that that op-amp has enough output margin there on on the low side output drive to drive

**Dave Jones:** your voltage reference. Oh, and for those curious about the noise, no on the 1 milliamp one, no, there's bugger all noise. That's just the noise of the test setup, pretty much. The good thing about this voltage reference, it does actually

**Dave Jones:** have a noise reduction pin as well, so you can put a bypass cap on there if you really want to get the noise down. And if we have a look at the 1 microamp current source output, check this out.

**Dave Jones:** Look, 50 mV per division. That is awful. We've got some real nasty crap going on in there, but is it the actual reference itself being unstable or is it external noise? Well, it's almost I think almost certainly external noise because we're

**Dave Jones:** talking about a 1 microamp current source here and of course we've got these huge uh you know, antenna leads just you know, hanging off here going into our current uh shunt over there. So, uh yeah, I expect that and we can

**Dave Jones:** probably verify that. Let's actually have a look. Here, let's uh cut and let's try and couple in some noise into this and hey, look at that. We coupling in tada, 50 hertz. So, it looks like we're just picking up

**Dave Jones:** all sorts of crap with that big antenna uh wire coming off the uh load there to our shunt. And basically, look at this. Aha, you don't normally see big spikes like that and aha, let's freeze that and let's have a look at the frequency

**Dave Jones:** there. We could see it before, but we're talking 1 2 3 4 5 divisions between those big spikes there at 2 milliseconds per division. Bingo, 10 milliseconds. What's that? 100 hertz full wave rectified mains. Hmm, coincidence? I think not. No, so what we're doing here

**Dave Jones:** is we're getting crap picked up from external in the room and watch this, right? I don't have my LED lights on, my big LED studio lights on. Let me switch them on. Tada, look at that there. Some higher frequency, I think if I

**Dave Jones:** memory serves me correctly, it was like 64 kilohertz switching or something like that, but more crap just picked up there. So, really what we're talking about here is just external noise picked up from the environment here with these

**Dave Jones:** big antenna leads. So, if we actually disconnect this antenna here, this horrible looking antenna, and we connect our lead over there, so our load is basically shorted out, but it's kept on the breadboard now. Bingo, look at that.

**Dave Jones:** No more noise. I mean, our 1 microamp is still there. If we go down to 5 mV per division, there we go. We're getting exactly the same noise we were were before. And like, that's just basically the inherent system noise. That's not

**Dave Jones:** the voltage reference itself. And we're getting some 50 Hz on there as well. So, there's absolutely nothing wrong with that circuit with that 1 microamp current generator at all. It is just the noise to do with the system around it.

**Dave Jones:** And well, that's perfectly normal, and we won't go into Jeez, I could do a whole hour's video on how, you know, best to uh lower the noise and, you know, eliminate it from your system and while you're testing and all sorts of

**Dave Jones:** stuff like that. So, yeah, I won't go into it. So, there's effectively no problem with this uh current source down at 1 microamp either, except for the op-amp input uh bias error. So, I'm probably going to have to choose another

**Dave Jones:** op-amp from the OPA uh 277 because I think we're just going to get a bit too much uh input uh bias current there, which introduces an error in the load there. But of course of course, you could uh you know, tweak the the output

**Dave Jones:** voltage of this thing to compensate for that input bias current if you really wanted to, but you know, I'll just probably pick another uh op-amp for that. But the OPA 277 is one specifically uh chosen for this task.

**Dave Jones:** Apparently, it is a, you know, a a pretty ultra-stable sort of op-amp. So, suits this sort of application for raising the ground up quite well. So, there you go. I hope you enjoyed that one. Yeah, this will probably be my

**Dave Jones:** my last video on these uh precision current sources unless uh something uh you know, interesting that comes up. But anyway, I hope you enjoyed that short little mini-series on these precision current sources and there's a lot more as I've

**Dave Jones:** explained and shown a lot more that I can go into this with actually measuring it and characterizing its performance and in the case of the one micro amp one actually getting you know, a noise free test environment and stuff like that.

**Dave Jones:** Anyway, might be for another day. If you like the video, please give it a big thumbs up and if you want to discuss it, jump on over to the EEVblog forum. The link is down below. Catch you next time.
