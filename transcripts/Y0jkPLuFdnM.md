---
video_id: Y0jkPLuFdnM
title: EEVblog #528 - Opamp Input Noise Voltage Tutorial
url: https://www.youtube.com/watch?v=Y0jkPLuFdnM
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Fundamentals Friday. Today we're going to take a look at op-amp voltage noise. Now, this can be a real big can of worms, so I'm going to only open it just a little bit today, and we're going to take a look at one of the

**Dave Jones:** more confusing parameters on an op-amp data sheet, and that's input noise voltage density and input noise voltage. If you didn't know, well, you do now, that any op-amp is going to have inherent noise in it, just like all

**Dave Jones:** components and all wires and everything else has inherent noise within it, and the op-amp is no different, and that's what we're going to take a look at. Now, we're not going to take a look at anything around the circuit, the

**Dave Jones:** resistor noise and other components and stuff like that, just what's inherent in the op-amp. And to do that, we're going to start by taking a look at a typical data sheet. Now, let's take a look at the op07, a typical precision op-amp,

**Dave Jones:** not particularly low noise, but it is one of the jelly bean precision devices. Now, um it has a parameter here called input voltage noise, and that's the noise effectively on the input, and the units are very easy, they're microvolts

**Dave Jones:** in peak-to-peak. And it's uh called EN or VN, depending on the data sheet, could be called other things, but they're just uh typical labels for it. And, you know, that figure might be familiar to you, and it's fairly easy to

**Dave Jones:** understand. Okay, I've in the case of the op07, we've got 0.35 microvolts peak-to-peak input noise. So, if we've got a voltage follower like this, with a gain of one, we're going to get an output noise or an inherent noise in our

**Dave Jones:** op-amp uh in our complete amplifier here of that 0.35 microvolts peak-to-peak. Real easy to understand, but there's a catch. Take a look at the conditions that that value is measured over and it's actually 0.1 hertz to 10 hertz bandwidth. And you

**Dave Jones:** might be familiar with this from power supply specs, for example, they might specify the output noise of your bench lab power supply over typically a 20 megahertz bandwidth. Well, in this case, it's a very small low frequency bandwidth and we'll find out why later.

**Dave Jones:** It's 0.1 hertz to 10 hertz. This is typically how they measure it. They've got the op amp here. It may have some may or may not have some gain. The input will be grounded. It'll all be shielded, of course.

**Dave Jones:** And then we'll have a band pass filter of 0.1 hertz to 10 hertz. We'll have some more gain in there because we're talking about low signal levels. That'll go into a scope and they can measure that value. And they'll give you a peak

**Dave Jones:** to peak or a maximum peak to peak signal and they'll also give you take a look at this also in the data in most data sheets. They will also give you a typical waveform as well. Once again, that's a bandwidth limited to 0.1 to 10

**Dave Jones:** hertz. Very limited frequency range. So, that's well and good if you're operating down in that frequency range in your circuit. Fantastic. You've got this real world figure here. You understand it. It's easy. It's a peak maximum voltage and you know what your system noise is

**Dave Jones:** going to be at least just you to the op amp. Very simple. But what happens if you want to actually operate typically over a larger frequency range? Well, we get into something a bit more complicated called input noise voltage

**Dave Jones:** density. You'll notice it's exactly the same, but they've added this word density. And if we go back to the data sheet and take a look at some typical figures for the op 07, what do we get? Well, look, you can see that the

**Dave Jones:** conditions there, there's three different values, and these are called the spot frequency values. In this case, we've got 10 Hz, 100 Hz, and 1 kHz, and we've got different figures for that, 10.3, 10, and 9.6, respectively. And you'll notice how it's slightly higher

**Dave Jones:** at lower frequencies, and that's important, which we'll take a look at in a minute. But it uses these bizarre units, which confuses a lot of people, and it's nanovolts per root hertz. And here it is. Once again, it's labeled

**Dave Jones:** exactly the same, EN, VN, exactly the same, but instead of microvolts peak to peak, we've now got a value in nanovolts per root hertz. What does that mean? In a nutshell, it's spectral density, i.e., the density of the noise over a specific

**Dave Jones:** spectrum or frequency range, just like our input voltage noise was measured from 0.1 Hz to 10 Hz. It needs a these this unit here actually needs a frequency range over which it's going to be valid. Otherwise, it's a meaningless

**Dave Jones:** figure. Now, the confusing part about these units of nanovolts per root hertz is that you go, "Well, what kind of units is that?" Well, it's just voltage. It's you know, even though it's called nanovolts per root hertz, the per root hertz part just

**Dave Jones:** specifies that it's defined over a frequency range, because it's a spectral density. Now, so with basically, it is just a voltage. That's all there is to it. Now, the data sheet, for example, for this one, at a specific frequency,

**Dave Jones:** has for example, 10 nanovolts per root hertz. Now, it's very important to understand that this is not divided by root hertz. It's per root hertz, and it's actually a reference to 1 hertz. So, it's 10 nanovolts for every 1 hertz

**Dave Jones:** of bandwidth, and that's the key to understanding this thing. So, if you've only got a 1 Hz bandwidth, then your noise is going to be square root of 1 Hz, which is the same 10 nV, but you know, usually you're not going to be

**Dave Jones:** operating over a 1 Hz bandwidth. So, let's look at a 1 kHz bandwidth, and the formula then is Fmax minus Fmin. That's a little bit complicated, but it's basically the bandwidth you're operating under. So, if your operate circuit uh is

**Dave Jones:** operating from 0 Hz up to 1 kHz, then you've got a bandwidth of 1 kHz minus 0 is 1 kHz. 10 nV times the square root of 1 kHz gives you a final value of 316 nV. Easy. That's how much noise

**Dave Jones:** RMS by the way, this is all RMS noise in your op amp, inherent in your op amp, just like this value up here was microvolts, but it was specified in peak to peak. This one up here nV per root Hz

**Dave Jones:** specified in RMS. So, you can see that the higher frequency range you operate over, the more noise you're going to have, because it's multiplied by the square root of the frequency. If we operate over 10 kHz there, it's going to be bigger noise

**Dave Jones:** once again, or 100 kHz, or a megahertz. The next important thing to understand is this is what is called input referred noise, or equivalent input noise. You'll see these terms at various different types of terminology, but it means that

**Dave Jones:** this is the noise on the in the equivalent noise on the input of the op amp. So, what that means is it gets always gets multiplied by the gain of the op amp. In this case, we've just got

**Dave Jones:** a gain of one. So, in the case of this op 07, 316 nV RMS on the input, same 316 nV RMS noise on the output. Pretty low noise. But, if you suddenly whack in a gain of a thousand in there

**Dave Jones:** AV equals a thousand. Bingo, you've gone from 316 nV to 316 microvolts or 0.3 mV. Much higher noise. Now, if you remember, I said this was RMS. So, how do you convert it to possibly a more useful maximum peak-to-peak value in your

**Dave Jones:** system? Well, this one gets a bit fuzzy and you have to introduce probability. Now, what we're talking about here is white noise or you know, purely random noise, which has your typical Gaussian response like this and we won't go into

**Dave Jones:** hugely into types of noise, but it has that Gaussian response. Now, I've drawn a voltage here. I've rotated the axis like that. So, positive and negative voltage noise can always be equally positive and negative. Doesn't just go positive. And basically, the peak value,

**Dave Jones:** so this is just a typical voltage peak like this over time. So, as you can see, you know, the noise is completely random and what are these peak values here going to be? This is where you get into

**Dave Jones:** that probability term, sigma. Now, if we look at the value of plus minus three sigma there, basically, what that means is that we have a 99.9% confidence or close to it that the peak-to-peak noise is going to be within

**Dave Jones:** that specific value. So, at that three sigma value, what you to get that, that's a typical figure quoted. So, manufacturers might typically define the convert RMS to peak-to-peak by using a multiplier of times six or times 6.6. 6.6 will give

**Dave Jones:** you 99.9% probability the noise falls within a certain range, but it doesn't guarantee it. There's a 0.1% chance can be outside that. And well, it's up to you as the system to designer to determine what probability you need, but that's a good

**Dave Jones:** ballpark. So, multiply that value by about 6 or 6.6. So, in our example of a gain of 1,000 here, what's our output noise for this op07 with 10 nV per root hertz specified? Well, it's going to be the output is going to be 316 microvolts

**Dave Jones:** RMS around about 2.1 millivolts peak to peak with a good confidence level. And that is going to be your output noise just solely due to your op-amp, not taking into account any other components or any other part of your circuit. So,

**Dave Jones:** that's really quite easy to understand once you know. Just multiply that figure by the square root of your bandwidth, and you get your output noise in RMS. Very simple, but yeah, there's more to it. Let's go a little bit deeper. Open that

**Dave Jones:** can of worms just a little bit more. And yes, hold on to your hat. We're going into a graph of noise voltage versus frequency here on dual log axes. So, we've got our nanovolts per root hertz here versus frequency. And as I said,

**Dave Jones:** log axes, that's important. So, 10 hertz, 100 hertz, and it's not a linear increase. Same with frequency, 10, 100, 1K, and then it's your typical log axes you should be familiar with. So, the black line there is our noise voltage,

**Dave Jones:** and you'll find this uh typically find this curve in the data sheet as well. And it'll always be in this particular form. And here's where the trick with all this op-amp voltage noise comes in. Then we've effectively got two different

**Dave Jones:** types of noise in our op-amp, and they effectively split into different parts of the frequency spectrum. The higher frequency, say from around 10 hertz or 100 hertz up, typically is going to be your Gaussian white noise that we showed

**Dave Jones:** before. And effectively what we're using up there for our input noise voltage density. That's our white noise up there. But all op amps, regardless of the type, are going to have this characteristic response that tails up at low frequencies. And this is called 1/f

**Dave Jones:** noise. So, white noise dominates at higher frequencies, 1/f noise dominates at lower frequencies. They're usually, you know, around about 10 Hz or lower or that figure. That's why our input voltage noise here, peak to peak, was specified over that 10 Hz range because

**Dave Jones:** they're really looking at the 1/f noise there, the low frequency stuff. Whereas our voltage density is looking at the higher frequency noise up here. And yeah, they are two different things. So, when we were actually calculating this input noise

**Dave Jones:** noise density over here for a 0 to 1 kHz range, we were actually including this lower part down here. But because the frequency range we were working over, because it's a log axis, is so large, pretty much you can ignore

**Dave Jones:** this tail up end. And you know, we can stick with the ballpark figures we got over here for our noise voltage density over that entire frequency range. And we won't go into specific details of the types of noise cuz there are quite a few

**Dave Jones:** different types. But suffice it to say that the white noise, the high frequency stuff, is made up a combination of shot noise and thermal or junction or Johnson noise, as you may have heard it called. And the 1/f noise is also referred to as

**Dave Jones:** pink noise. And that's due to what's called flicker noise. But it's more typically just called 1/f noise. And that's the trap with components. You can't escape this 1/f noise. It's just inherent in nature. There's absolutely nothing you can do about it. There are

**Dave Jones:** things you can do in the process of manufacturing your devices to, you know, to reduce the flicker noise, but pretty much you're going to cop it at that low frequency range. So, you might think these op amps less noisy at DC. Well, that's not the

**Dave Jones:** case. As you can see, they get much, much noisier at DC. They're lower noise at the higher frequencies. It doesn't make sense, but hey, a lot of things in physics don't make sense. Next thing we know, we'll be talking

**Dave Jones:** about spooky action at a distance. Now, Gaussian white noise like shot and thermal noise has a uniform power density. What that means is that it's going to be the same value regardless of the frequency, and that's why we get a

**Dave Jones:** flat line in there for that. But, one on F noise is not a uniform power density, so that's why we get basically a flat line straight line like that, but it has a specific slope 3dB per octave. But,

**Dave Jones:** we won't go into the details. And this all comes back to why our input noise voltage density was specified in the data sheet at three particular frequencies, 1 kHz, 100 Hz, and 10 Hz. It's so that you can do

**Dave Jones:** comparisons with other op amps of how this noise changes and how well it performs over a frequency range like that. Because if you see a large change, for example, between 100 Hz and 10 Hz in for one op amp and hardly any difference for

**Dave Jones:** another op amp, then you know that that second op amp with the same figure right down to 10 Hz is going to be a better op amp. And that's basically a deciding factor, that corner frequency that we've got there, that effectively determines

**Dave Jones:** how good your op amp effectively is. The lower that corner frequency, the better your op amp, and that's the one you're most likely going to choose, all things being equal. And as always with data sheets, the marketers are going to fudge

**Dave Jones:** the numbers to give you the best possible banner spec. So, beware. You have to actually go in there and look at the graphs, look at the individual data, and compare op amps. And it can actually be pretty hard to compare op amps just

**Dave Jones:** from the data sheets. Not that easy. So, you've got to be careful and know how to design it into your system. And you'll also notice on the data sheet that there's an identical noise spec for current as well. So, it's input uh noise

**Dave Jones:** current density and input noise current. And we won't go into that. That's the current into the input to the op amp. So, at the moment, as I said, we're only looking at the voltage scenario. But, hey, if you've got significant input

**Dave Jones:** currents, you have to take the input current noise into account as well in those really critical low-noise circuits. But, the same sort of fundamental theory applies. And yes, it's all going to add up with the voltage noise as well. So, you just got

**Dave Jones:** to be careful. And by the time you actually practically build the circuit up, usually usually the external components are going to dominate your circuit more than the op amp itself. But, hey, that's why they spec these things cuz a lot of critical

**Dave Jones:** applications you have to get the lowest noise op amp possible. And that's what it's all about. Frequency range. Remember how much noise density within that 1-Hz window. And when you extrapolate these two lines here to get that corner

**Dave Jones:** frequency crossing point where they intersect, if you extrapolate that down, then we've got that There's 10 Hz, there's 20 Hz. So, it's somewhere in there. Let's say about 15 Hz is our corner frequency for this example we've drawn here. Then,

**Dave Jones:** that 15-Hz point is the point where the value of the white noise is equal to the value of the 1/f or noise. And of course, if you sum them together, let's say it's a 10 there as shown, then you

**Dave Jones:** don't get 10 + 10, of course, you get 10 * the square root of 2. So, you get about 14.1. So, there you go. That probably took a bit longer than I expected, and there's a lot more detail in here as well. But,

**Dave Jones:** suffice it to say, for your basic op amp like that, if you're working from DC, if it's all DC coupled in your full bandwidth is from DC to 1 kHz, for example, you effectively do have to take into account these two different types

**Dave Jones:** of noise, and you've got to sum them together. And when you add noises together, it's actually the root of the sum of the squares. So, it's the square root of uh this noise here squared plus this noise here squared, and you've got

**Dave Jones:** to add them together, and that gives you total noise. But, as we said right at the start, this is just the noise inherent in the op amp itself. Uh it doesn't include the resistors here, which of course have that uh thermal uh

**Dave Jones:** Johnson noise you might be familiar with, that classic equation, the higher the resistor value, the more thermal noise you're going to get in the resistor, and all sorts of other stuff in your circuit. So, it can get really

**Dave Jones:** complicated, but I hope you found that really It is pretty easy to understand what nanovolts per root hertz is and how to calculate your noise. Very simple. This is a bit more detailed of how it actually works, but let's go out and see

**Dave Jones:** if we can actually measure exactly this graph. To the bench. And what tool do you use to measure the input noise voltage of something like an op amp? Well, you use a dynamic signal analyzer or DSA, which we've seen in the

**Dave Jones:** previous videos. And this is my HP 35660A DSA. They go from DC to about 100 kHz, perfect for characterizing the uh and seeing the one on F noise and power spec spectral density of the noise in something like an op amp or any other

**Dave Jones:** circuit. It's the tool of choice, but unfortunately this uh 35660A isn't exactly the world's best performance. It's noise floor isn't that great in itself. So, that's what we'll do first. We'll just measure the noise floor of this unit itself with a 50-ohm

**Dave Jones:** terminator on the input of course on channel one here and we'll see what we get. But, it's not going to be that crash hot, but it should be good enough to at least allow us to see differences between uh different types of op amps.

**Dave Jones:** So, I'll just run through you briefly how to set up a dynamic signal analyzer to measure power spectral uh density on a low voltage uh signal like this. Now, when you first turn it on by default here, we've got our frequency spectrum

**Dave Jones:** like this. It's displaying our frequency spectrum from 0 Hz down here to 102.4 kHz and we're only uh looking at channel one. So, there's the span. The record length is 3.9 ms for each one of those. And on our Y axis here, we have uh dB

**Dave Jones:** volts RMS. Whoop, there we go. It's doing its auto calibration. And we've got a figure, you know, down around that 130 minus 131 dB volts RMS mark. The first thing we have to do because we're measuring low signal levels, go to

**Dave Jones:** input. So, I've selected the input button on the front and then channel one range. At the moment it's auto ranging. We really don't want that. We want it to um just be fixed. And this thing, I'm pressing the up down uh keys and as you

**Dave Jones:** can see, there you go. The channel one range up there, the uh highest gain range or the lowest voltage range it's got is minus minus 51 dB volts RMS. And that's equivalent to I think about 4 mV uh

**Dave Jones:** peak or thereabouts. Next thing we want to do is turn on some averages. so I'll press the average button on the front and then we want to turn average on like that because otherwise we'll just get, you know, we want a smoother line. See

**Dave Jones:** what happens when you turn the average on there? It's set for 10. I'm going to change that to number of averages there and I'm going to enter 100 averages. So now when you press the start button and we start our acquisition, there we go.

**Dave Jones:** It's giving us a bit of a plot already and we can already see that we're getting a result. Here it is. There's our pretty much flat line with the big one on F noise tailing up at the bottom.

**Dave Jones:** But why didn't it look like the whiteboard? Well, because we haven't plotted uh the frequency on a log plot yet. It's a linear plot. It's a linear axis, sorry. Speaking of which, we have to go uh to the input here, set it up

**Dave Jones:** and just make sure we've uh got a DC coupling here. We want to go all the way down to DC. So to change that to a log graph, we press the scale button on the front here. And here it is. X axis,

**Dave Jones:** there it is. Currently set to linear, we'll change that to log and bingo, look at that. We're starting to get exactly the response that we wanted. Now, the reason why it's um there's not many data points down here because it

**Dave Jones:** has to do with the number of lines in the FFT response of this thing. Now, we've got a full uh span here of 102.4 kHz and this particular instrument only has uh 400 lines of resolution. So if you divide um 102.4 kHz into 400, you

**Dave Jones:** will get, if we move our marker across here, you'll notice that um each step it can only measure at those frequency points there. So it's very coarse down there, of course, and you'll find that the uh lowest step down there is going

**Dave Jones:** to be 1/400 of 102.4 kHz. So 102.4 K divided by 400. There we go. Gives us 256 Hz where our marker is all the way over there. What's our marker X? There it is, 256 Hz. So, it can only jump up

**Dave Jones:** in 256 Hz steps cuz that's all the FFT resolution we've got there. And of course, that really shows up when you've got the log X axis like that. Didn't really show up on the linear one because then it'll be stepping in 400 even

**Dave Jones:** linear increments across the screen. Now, if I press the measurement data button on the front panel here, we're in what's called well, just normal frequency spectrum mode, more correctly referred to as linear spectrum mode. And that gives us a voltage response here.

**Dave Jones:** And as we saw before, DB volts RMS there, minus 123. And if we plug that into the calculator, minus 123, and then we divide cuz it's in DB. Remember, if you want to convert it to a voltage, then we divide it by 20. And

**Dave Jones:** then we take the inverse log of that, and we've got ourselves 708 nanovolts. But, what does that mean? Doesn't really mean anything because that isn't our power spectral density. So, we press the scale button on the front, and we'll

**Dave Jones:** have a look at the vertical units which we've got here, DB volts RMS at the moment. And as you can see, there is no option for that voltage per root Hz because we're in the linear spectrum mode. We're not in a

**Dave Jones:** doing We're not actually calculating the power spectrum density. But, that doesn't mean that this graph isn't correct cuz it actually is. The shape of this graph is absolutely bang on to what we would get in the spout power spectrum density, except our

**Dave Jones:** units aren't up here aren't correct. We're DB volts RMS instead of that voltage per per root hertz. So, how do we do that? Well, how do we convert it? Well, we can do it manually. We can do all the math ourselves to convert

**Dave Jones:** between the linear spectrum and the power spectrum density, but we don't need to do that. What we can do is go into the press the measurement data on the front. This thing will do it for us. That's what these dynamic signal

**Dave Jones:** analyzers are designed to do, measure this noise specifically. And there it is, PSD mode or power spectrum density. Bingo. If we go into power spectrum density, you'll notice that the graph hasn't changed at all. And uh normally when you

**Dave Jones:** change mode, it rescales things, but it hasn't. The graph has stayed exactly the same, but look what we've got now. It's got a little asterisk next to it here, and that asterisk means there it is, volts RMS per root hertz. And if we go

**Dave Jones:** back, that's exactly what we want, exactly what we saw on the whiteboard. And if we go back into the measurement uh sorry, the scale here into our vertical units, we'll see because we're now in the power spectrum density mode,

**Dave Jones:** that we've got root hertz options here. Volts RMS squared, DB volts RMS per root hertz hertz or volts per root hertz. That's what we want. Volts, well, we want nanovolts, but volts per root hertz is the same thing. It'll scale for us.

**Dave Jones:** So, bingo. Look at what we've got now. Our And that value there at uh 10 kilohertz, close to 10 kilohertz, is now switched over and it's calculated that it's 28 e to the minus nine. That's nano, of course, nanovolts per root

**Dave Jones:** hertz. Bingo. We've now got our DSA to uh check its own performance because we've uh remember we've got a 50 ohm terminator on the front, and there it is. That's what it is after 100 averages down here over that uh well, at the

**Dave Jones:** moment the full span from zero to 102 kHz. So, as you can see, this instrument um you know, is worse than a basic uh you know, op07 op-amp. 28 nV per root hertz. And as we saw in the data sheet

**Dave Jones:** before, a just a basic op07 is around, you know, at a spot frequency um in this case 10 kHz. It only goes up to 18 I think. Uh but, yeah, you know, because it's flat, it's going to be exactly the

**Dave Jones:** same. It had a figure of around 10 nV per root hertz. So, this thing isn't good enough to measure the performance of an op07. The way you normally do it, although it is, you could actually use this instrument, the way you'd normally

**Dave Jones:** do it is use an external uh extremely low noise purpose-designed amplifier to amplify the noise before it gets into this instrument. So, you use this instrument, um you've already gained it up, so you bring it way above the noise

**Dave Jones:** floor of this instrument, and then you can, you know, if it's got times 100 gain, then you can just, you know, change the units to compensate for that, and you can actually measure the performance of an op07. Now, if we take

**Dave Jones:** our cursor all the way over to uh the corner frequency down there, uh once again, we're very coarse cuz we're measuring the whole 102 kHz bandwidth. As it's telling us the corner frequency is about 1 kHz, but I know that's not

**Dave Jones:** going to be the case. What we want to do is change the span so we get more detail down on this 1 on F region instead of just three crappy three data points. And that's easy. You just press the

**Dave Jones:** frequency button on the front. You can see these DSAs are specifically designed for these types of measurements. They're optimized for it. This is what they're designed to do. Anyway, we can just go span like this, press the span button,

**Dave Jones:** and then we can uh just type in, say, well, no, let's do 1,000 hertz. We'll do a kilohertz range and then it's going to restart. You can see it's automatically restarted and it'll do the RMS averages. It takes longer, of course, cuz it's

**Dave Jones:** lower frequency, so it takes a quarter of a second per record uh length like that. But there you go. This one has actually dropped off the screen, so I think we've done something with our input scale in there. So, if we press

**Dave Jones:** our scale button there, we can just auto scale that and bang, that's going to bring it in line like that. And look at that. Look at that. We can now uh one that cursor, we can now put it at 1

**Dave Jones:** kilohertz. There you go. So, it's at 1 kilohertz there and we're getting a value of about 31 uh nanovolts per root hertz. That's the noise floor of this thing. As I said, not very spectacular. In fact, I want to investigate open this

**Dave Jones:** thing up, uh have a look at the op amps used in this and other components and see if I can actually use modern uh drop-in high-performance op amps to actually um increase the performance of this thing. So, uh I'll leave that to a

**Dave Jones:** future video. But you can see it's essentially flat and it starts to tail up a bit there. You can see it just starting to go up. So, you can see um because we're effectively measuring the uh noise of the um input noise of

**Dave Jones:** the the input section or the input op amps inside this particular instrument. So, we'll get exactly the same result if we were measuring an external op amp effectively. So, the value 1 kilohertz here is going to be slightly lower than

**Dave Jones:** the value at 100 hertz, which once again is going to be uh uh lower than the value at 10 hertz here. And that's why they have those three spot values on the data sheet. 1 kilohertz, 100 hertz, and then 10 hertz

**Dave Jones:** over here. And of course, that will be a continue basically completely flat out to that 100 kilohertz we saw uh last time. But you can see it pretty much starting to get bad at just under 200 Hz there. I've put it on 160 Hz for a

**Dave Jones:** reason because let's go to the data sheet for this HP DSA. And here it is, straight out of the user manual on the minus 51 dB volt range, i.e. the highest gain range which it we've got, source impedance of 50 ohms which we've got 16

**Dave Jones:** RMS average as well. We've done 100. You'll notice that it doesn't specify anything under 160 Hz. It's got that 160 Hz to that 1 kHz range is minus 130 dB volts per hertz. And of course, you were if you wanted to, you have to convert

**Dave Jones:** that to the power spectrum density which we can do which we've just done with the instrument itself. So, there you go. That's why they've got the figure of 160 Hz in there because it it's performance really starts under

**Dave Jones:** that 160 Hz, you know, it really starts to be a bit how you doing. And one thing I want you to take note of, near 50 Hz there, you'll notice that we're getting no 50 Hz pick up at all.

**Dave Jones:** And of course, this lab is just swimming in 50 Hz mains frequency because as we saw in the teardown of this thing, it's incredibly well shielded and we've just got a 50 ohm terminator on the front. But as we I

**Dave Jones:** think we'll see when we try and measure a practical circuit, we're going to get at least some 50 Hz pick up. It's almost unavoidable. Okay, so let's take note after 100 averages at our marker frequency of 1 kHz because that's a

**Dave Jones:** value we can get from the data sheet for some op-amps, we're getting 31.3 nanovolts per root hertz. So, that's the basic noise floor of our DSA here. And of course, to measure noise floors like this, you need a Faraday cage. You need

**Dave Jones:** a shielded box, one of these diecast alloy boxes, absolutely fantastic sort of industry standard way to measure these things. A little mini breadboard in there with a TL072 on it and I've got two 9-V batteries. Now, if you look at the data sheet, the

**Dave Jones:** voltage uh the noise for these for all these chips is usually specified at say plus minus 15 V or sort of maximum rail. It's going to be near enough plus minus nine. Now, of course, once you put the lid on

**Dave Jones:** this sucker, there's no way anything is getting in there at all. We've got our nice BNC on there. We've got a shielded coax all the way to the input. Bob's your uncle. And of course, you do want to use batteries internal to the box.

**Dave Jones:** You don't want to be using an external power supply or any type of switching power supply or anything like that. Batteries the only way to do it. And you'll notice no, I don't need any decoupling on there. It's good enough

**Dave Jones:** because we've got the low impedance battery directly and this thing ain't going to oscillate. So, we've got our box hooked up with the TL072 in it. Now, I chose the TL072 cuz it's not a particularly low noise op-amp

**Dave Jones:** about 18 nV per root Hz at that 1 kHz figure straight from the data sheet because it's not designed for noise. It only has the figure at 1 kHz. It really, you know, it's not that great. It doesn't

**Dave Jones:** really specify in depth. But here we go. So, that is the noise floor of our DSA. Let's press start and we will get using the exact same parameters we set up before. Remember 31.3 nV per root Hz. Now, of course, that is below So, the

**Dave Jones:** noise that we're trying to measure here of this TL072 is below the noise floor of this DSA. But aha, remember that they sum together. So, we should see an increase there. Let's press start and away we go. And woohoo, look at that. 1 on F noise

**Dave Jones:** has gone right off the the there and look at that bump. What frequency do you reckon that is? 50 Hz. Bang on. Where are we picking up our 50 Hz from? It ain't through the box, it's through the

**Dave Jones:** shield of the coax. That's the only place it can be getting in. I don't know, this is a you know, RG59 cable or something. I don't know, just a cheap one I had lying around. So, uh yeah, you really, even with fully

**Dave Jones:** shielded coax's and that shielded box, we're getting our 50 Hz pick up. But anyway, look, we've got almost got 100 averages. There we go. We've gone up from 31.3 nV per root Hz to 38.028 uh 38 uh nV per root Hz at 1 kHz. So, it's

**Dave Jones:** gone up by about 7 nV per root Hz. And what value should have we expected? Well, 31.3 nV per root Hz, the base noise floor we had there, we've got to square that. Remember the formula we had on the

**Dave Jones:** whiteboard before? And then we've got sum of the squares, so we've got to add in the data sheet value, typically 18 nV per root Hz at 1 kHz. So, uh yeah, let's square that. And then get the square root. We should

**Dave Jones:** get around about 36.1, and we're getting 38.1, you know, uh 38. So, you know, near enough. There you go. We were able to see a difference with that TL072. Now, let's get one that's even worse, 42 nV per root Hz. It's a TL062.

**Dave Jones:** It's an absolute shocker. I've put it in there. Let's press start. And there we go. Woah. We still get our 50 Hz, of course. Horrible 1/f noise gone off the scale here. But there we go. It's massive now. Look at that. In

**Dave Jones:** the order of you know, 75 nV per root Hz. Awful. There we go. After 100 averages, 68.1. Is that correct? I don't know. What is it? 31.3 squared, which is noise floor of our DSA, plus the nominal 42

**Dave Jones:** from the data sheet. And then we can get that and then we square root that. We expect it around about 52.3 and we're well above that. So, that one's not working out too great. Really isn't ancient chip though, trust me.

**Dave Jones:** It's like 25 years old or something. Let me check the date code. There's actually not a date code on that, but this one's actually like I had this one since I was a kid and it was actually desoldered from a board. So,

**Dave Jones:** it's ancient and shocking. But, anyway, it allows us just to show the difference there, what a crappy op-amp can make and how you can measure it. And I've now put in an analog devices AD712, the identical 18 nanovolts per root hertz of

**Dave Jones:** our TL071. So, let's give that one a whirl and see what we get. Still get our big 50 hertz, but uh there we go. We're getting Yeah, about 40 odd. Not too dissimilar to what we're getting with the TL072.

**Dave Jones:** And as I said, if we really wanted to measure the performance of these op-amps properly, I would have to use an external amplifier in here. I'd have to really design it properly and ironically, you need an incredibly, you know, low noise amplifier in there

**Dave Jones:** to measure low noise. Imagine trying to measure the state of the art op-amps. Well, you're going to be very careful in how you roll the input amplifiers and we would still be able to measure it easily once we got, you know, some gain in that

**Dave Jones:** box to I get well above the noise floor there and actually be able to measure properly the absolute performance of the op-amps. But, anyway, I hope you found that interesting. We were able to see the differences between some op-amps

**Dave Jones:** there. And if I put in a really schmick op-amp in there, we would have actually seen it drop to pretty much the same noise floor as this particular DSA. So, there you go. If you want to discuss it,

**Dave Jones:** jump on over to the EEVblog forum, and I hope you like the video, and if you did, please give it a big thumbs up. Catch you next time. Wait, hang on. I found an NE5534 op-amp. Really good use a couple of them

**Dave Jones:** in here from what I saw on the schematic. Anyway, I'm not at the front end, I don't think, but anyway, somewhere in here. And that has a noise figure of about 4 nV per root hertz. So, let's give it a whirl.

**Dave Jones:** And there we go. Yep, still picking up our 50 hertz, but once again, we haven't gone off scale here now. And there we go. We're not we're almost exactly the same noise floor as we got with the instrument itself. What was it? 31.3 nV

**Dave Jones:** per root hertz. If we wait till it goes up there, we're only a couple of nV above that. So, bingo. There you go. There's a good quality op-amp for you. There it is. 33.7 for the record. Beautiful. Catch you

**Dave Jones:** next time.
