---
video_id: 6Kcf7IJjszg
title: EEVblog #386 - Glass Delay Lines Part 2
url: https://www.youtube.com/watch?v=6Kcf7IJjszg
source: youtube-asr
---

**Dave Jones:** Hi, this is just a quick follow up video on the acoustic delay line we had a quick look at inside the Sony video 8 camcorder 1985 vintage and this is a a PAL delay line, a glass delay line which we had a quick look at and a

**Dave Jones:** lot of people wanted me to expand on that and just do some measurements and actually show the delay through this thing and just generally have a play around with it. Now since that video some people have sent through various

**Dave Jones:** links and info on these glass delay lines and they really are fascinating stuff. So I'll link in an interesting paper down below but that basically explains how these things work all sorts of math behind the shear waves in these things

**Dave Jones:** and the bandwidth and all sorts of stuff. So it's rather interesting. So if you want to get more involved in the math and the technical details of how these things actually work, I suggest you have a look at that link. Now

**Dave Jones:** as we said before, if you haven't seen the previous video, there's two acoustic transducers up the top there. You can see that little bit of gold on the top there. One transmitter, one receiver but they are actually by you know, you can use one for either.

**Dave Jones:** It's so this one can be the transmitter or receiver or vice versa and we'll actually test that. We'll hook it hook it up to the scope and we'll measure a delay going through this thing. So as we said, if this one is transmitting here

**Dave Jones:** for example, then it goes then the shear wave inside this thing goes down through here, bounces off this wall here, bounces off this wall because these are oblique angles. They start off at oblique and they come in at these

**Dave Jones:** oblique angles. So they can't actually bounce off the wall. So it goes all the way through there like that. Bounce, bounce, bounce, bounce and back out. Now as it turns out this these things are typically either a quartz uh glass or a

**Dave Jones:** potassium lead silicate uh glass. The thickness of this glass will be uh and basically one wavelength. So, it uh effectively works as a wave guide. And this black stuff on the back of the glass here, I did guess correctly last

**Dave Jones:** time. It is actually an epoxy uh compound which just uh dampens the glass a bit in that particular location. It helps guide the shear waves through the glass. Now, as it turns out, these um potassium lead silicate glass delay

**Dave Jones:** lines like uh this one, I believe, they have an approximately um uh velocity wave velocity inside the medium and it does travel inside. It doesn't travel on the surface. So, that even that though that epoxy is on the

**Dave Jones:** surface, it's just used to dampen the wave inside the thing and keep it channeled within that particular wave guide uh function. So, it can, you know, because it's folded back and forth and has this convoluted path, you need those

**Dave Jones:** dampeners in there just to help concentrate those uh waves, those shear waves, inside the glass. Now, that that has it has a velocity of propagation of about 2.5 mm per microsecond or 2,500 m per second. Now, I actually got out my ruler and I

**Dave Jones:** measured all of the paths in here from center to center and I added them all up and uh it was uh 26 + 6 + 22 + 21 + 7 + 29 + 7 + 21 + 18 mm huh for a total path

**Dave Jones:** length of 157 mm or thereabouts, you know, it's with a ruler. It's not going to be horribly accurate. But, if you divide that by 2.5 mm per microsecond, what do you get? You get 62.8 microseconds and this is

**Dave Jones:** supposed to be a 64 microsecond delay line. So, it basically measures out. Now, what makes this thing actually directional and allows the wave to travel all this complex path is not only the thickness of the glass, which is nominally one wavelength, but

**Dave Jones:** the aperture as well, which is the distance of the path, the width of the path like that. And that is typically much larger, as you can see, than the thickness of the glass. So, that allows the wave to be directional. The physical

**Dave Jones:** properties of that allow the wave to be directional and hence make that entire distance without dispersing too much. And it's helped by these epoxy dampener materials, which just keep it channeled within there and stop coupling between the paths. Now, if we have a look at the

**Dave Jones:** edge of this thing, you can actually see that it's very, very smooth. And that is required in order to get the reflection off the oblique angle of 45° coming in like that. And the shear wave inside needs to bounce clearly off that edge,

**Dave Jones:** which edge with as little attenuation as possible. So, they do that by keeping that a very, very smooth edge on that thing. Whereas, the surface is going to be different. Now, the surface here you can actually see is quite opaque. It's

**Dave Jones:** not completely clear. And they've clearly treated that probably due to a through some chemical treatment process or something to roughen it up to ensure that those shear waves actually stay within stay shear waves and they stay within the body of the material like

**Dave Jones:** that so that they can actually reflect off there because this thing is effectively a high fidelity transmission line, so to speak. Because we're we're not just passing digital one and zero through this thing. We're the signal integrity of this transmission

**Dave Jones:** line matters. We're passing analog high bandwidth analog information through this stuff, color video signals. So, we need to we need for this to be as a good a transmission line as possible. And that includes reflections and bounces and stuff to do

**Dave Jones:** with regular transmission lines. Loading impedances, things like that. So, if this top surface wasn't treated in some way, we might have some surface effects happening as well as the shear wave going through the body of the material. And then that would cause different

**Dave Jones:** delays and with you know, it really wouldn't be a good transmission line at all. We get lots of different delays and phase and all sorts of things happening there. So, really for this to be a very good transmission line, they

**Dave Jones:** need to treat that surface and have a very good reflection of these edges because you're going to get a loss at each edge. And because this thing bounces what around a dozen times or something off these various oblique edges here. It comes in here,

**Dave Jones:** bounces off 45°, goes across here and up like that. And that happens you know, a dozen or so times. Jeez, you know, it's a wonder these things can get through with the fidelity that they do. But these have been

**Dave Jones:** specifically designed and engineered to be high fidelity transmission lines. Fascinating. And really you shouldn't get too many end-to-end reflections. I.E. If this is the transmitter here, you shouldn't get it going all the way through and then bouncing back off the

**Dave Jones:** end, the transducer end here because A, it's terminated properly and B, because it physically has the transducer glued or soldered onto that edge there. Then um, you know, it's it you've affected the uh properties of that edge. It's not

**Dave Jones:** going to reflect nearly as much uh magnitude as it does when you get bouncing off these nice smooth edges that you do within uh other aspects of the device. And it actually would be fascinating to uh if we actually had suitable uh

**Dave Jones:** transducers to try and attach them um to the various uh points. And if we did that at the various reflection points, if we did that, we'd actually be able to see all of the multiple delays. We'd be able to see uh you know, that'd be like

**Dave Jones:** a couple of microseconds delay, you know, 5 microseconds, you know, delay. If we put a sensor down in there, we'd measure that that and we could actually see it propagating all the way through the device. Now, as it turns out, the

**Dave Jones:** bandwidth of these things is actually can be quite uh large in like in the order of like uh 80% or more of the carrier frequency. So, uh let's draw a little graph here of a typical response characteristic of these things. And they

**Dave Jones:** are tuned to the carrier frequency, but they don't just operate at that. They will have a very wide bandwidth over that. So, if we have a little Dave CAD drawing here of uh frequency on here and uh this is

**Dave Jones:** basically uh the gain of the thing, which let's go V out on V in here. And we'll have a response looking something like this. There'll be a little ripple sort of in the pass band like that, but it will be something like that over the

**Dave Jones:** frequency. And basically, that'll be the center frequency there. And we'll have quite a large bandwidth over that. And this might be in the order of say minus 20 dB or something like that. So, um these things have to work with a

**Dave Jones:** specific load or they or they're better uh operated with a specific load and tuned to a specific frequency. So, when we hook this thing up and measure it, we probably don't expect more out than what we put in, especially if we you know, if

**Dave Jones:** we load the thing down and tune it properly. But, we'll just do some crude measurements today of you know, I'm not going to tune this thing exactly with LC circuit. So, we'll just have a bit of play around with, but we don't expect

**Dave Jones:** anything any more out than what we get. But, this will I would expect that to change uh fairly greatly between different models and different types of glass delay lines. And if we have a look at another Dave Cad drawing of basically

**Dave Jones:** how they implement these things, they're going to have a tuned uh LC filter on the input and the output here typically with a variable inductor. And they have to be loaded correctly. Now, for these glass delay lines, apparently that load is typically in the

**Dave Jones:** order of 270 to 390 ohms on the output and also the uh source impedance as well. So, apparently, you know, these things work better. They'll have a more linear uh bandwidth if you specifically tune them. But, uh today we'll just

**Dave Jones:** whack on a resistor. We won't worry about the L's and C's L's and C's. We'll just whack on some some resistor uh source impedance and load impedance. And well, see what we get. Bob's your uncle. Now, these ultrasonic uh transducers on

**Dave Jones:** the oblique edge down here, these have to be very very thin. They have to be uh at least uh in the order of like a a quarter of the half to a maybe a half to a quarter of the typical wavelength,

**Dave Jones:** which as I said will be the thickness of the glass there in order to ensure good performance. So, these things really need to be as thin as possible on that edge to maximize the performance. And the potassium lead silicate glass

**Dave Jones:** they use in this thing is also become known as isostatic glass with a T. Um, and that basically means that these are zero temp call very low. I in in practice they're going to be in the order, I believe, of a couple

**Dave Jones:** of ppm per degree C. But for all practical purposes, these are referred to as zero temperature coefficient glass. Soldered some pins in it just allows me to pull it in and out and rotate it easily on the breadboard. I've

**Dave Jones:** got a 270 ohm termination resistor on the output here, 270 ohm series input resistor here. I've got no L's and C's to actually tune this thing, but let's see what we get, shall we? Input here is connected to my Rigol DS4000

**Dave Jones:** function generator. That That will allow us to easily generate the waveforms we need. I've got channel one on the scope connected across that as well. So, we'll use that for the trigger and that will give us our reference waveform where we

**Dave Jones:** get our delay from. And on the output here, I've got channel B of the scope hooked up. So, let's hook it up, feed in some burst pulses of around about the resonant, you know, frequency of 4.43. Because as I said,

**Dave Jones:** these things do have quite a large bandwidth on them. So, we'll be able to measure that on the scope. Let's go. Now, on the function generator here, what I'm doing is I'm generating a sine wave of approximately 4.4 MHz there, 5 V

**Dave Jones:** peak-to-peak, and we're turning on burst mode as well. So, we can turn burst mode on. There it is, and it shows that we're generating a burst and then a dead period. So, basically, what we want is a is the

**Dave Jones:** period of the burst, the complete period, that green part there, to be 100 microseconds, you know, larger than larger than the delay period. Cuz our delay period of this thing, we think is going to be about 64 microseconds. So,

**Dave Jones:** we want it to be larger than that. I can set it much, much larger, but let's just go for starters, 100 microseconds. So, that gives us a burst of waveforms, then a dead time. And I can set up the number

**Dave Jones:** of cycles as well. So, if you go right, you know, let's I don't know, 100 cycles or something like that, whatever. So, we're generating a burst of 4.43 MHz and we can adjust that frequency, of course, and we will to check the

**Dave Jones:** bandwidth of this thing, even though it's not tuned. And let's see what we get on the scope. And bingo, here it is. And you'll notice that it's jumping all over the place. That's because of the trigger. So, what

**Dave Jones:** we'll do is we'll single shot capture that. There we go. And we can see our delay here. That the yellow waveform's our input. Of course, that's our burst of 4.4 MHz sine waves there. And we've got if you actually count them, you'll

**Dave Jones:** get 108 or whatever it is we set over there. And you can have like a single sine wave. It doesn't have to be this long, but whatever. Just for purposes of test. And you'll notice that look at that. If we have a look at that

**Dave Jones:** delay time there, I think you'll find that that's 64 microseconds. In fact, we can go to the delay here because our trigger point is that little triangle up there, which is right at the start there. The first pulse, but we can get more

**Dave Jones:** accurately in there, but we're getting around about that 63.8 microsecond delay. So, let's get in there with the cursors and get a little bit more accurate on that, shall we? But you'll notice that we're 1 V per division input and 50 mV per

**Dave Jones:** division output. So, our output signal really is quite low at 4.4 MHz or the, you know, the intended center frequency or I believe the intended center frequency of this thing. It could be operating higher and then they you know, they modulate the thing, but I

**Dave Jones:** don't know. At 4.43, the output voltage is quite low. And remember, we don't have the tuned LC filter on the input or output either. We've just got that resistive load. So, what I've done is I've turned on cursor mode here, and we want because

**Dave Jones:** we're using different channels for the cursors, we want the X2 cursor, well, the second cursor, to be a source a source on channel two. So, we can zoom in there and set our cursor, let's set it like right at

**Dave Jones:** the start when that waveform starts going, okay? So, there we go. And then, we want cursor X1 there to be channel one, and then we can adjust that. So, we can zoom in on that, and then take that right at that point there, and

**Dave Jones:** bingo, our delay Let's have a look at our total delay there, and there's our delta X time, 63.83 or 829 microseconds. So, very close to that predicted 64 microseconds. Although, curiously, it is a tad under it. But an interesting thing to check

**Dave Jones:** will be does that time delay actually change with frequency at all? I don't know. It might. We need to check that. So, what we should do is uh turn our frequency up here. Let I'm going over to sign. Okay, I'm going to

**Dave Jones:** go to 10 MHz. Here we go. I'm going to 10 MHz, and you'll notice that the amplitude has gone way up there. It's gone a long way up, so we'll check that. But look, we're still zoomed in We're zoomed in on that thing

**Dave Jones:** and we're still Look, we're still spot-on pretty much. So, the delay doesn't change with frequency. I mean, we've more than doubled the that frequency of this thing and basically, um that's pretty conclusive that there is no delay change with

**Dave Jones:** frequency. It's completely constant. And as I said before, this is an ISO pour stick uh glass, so it has zero temperature coefficient as well. So, the delay is not going to change with temperature, either. Doesn't change with temperature, it doesn't change with

**Dave Jones:** frequency. These things are pretty stable. And the only variable left really would be uh aging. You know, like, you know, this one is 1985 vintage, so it is very, very old, but um like, you know, because this is based on

**Dave Jones:** the physical uh distance, you know, the physical properties of the glass, that hasn't changed over the 20 uh plus years. So, really, these things are going to be incredibly stable over frequency, temperature, and time. Now, there's one thing you'll notice here is

**Dave Jones:** that we do have an additional uh waveform. It looks like we've got some reflected bounce or something happening in here, and it's not aligned with that at all, and it doesn't seem to be a multiple of that. So, um you know, it's

**Dave Jones:** not like it's a second reflection or anything like that. So, I'm not sure what that particular burst there is doing. What I'll do is I'll run it here, and you There will be some capacitive uh coupling as well.

**Dave Jones:** Now, what I'll do is I'll physically remove the delay line from the breadboard, and we expect these to vanish, but we'll probably see still some capacitive coupling in there from the breadboard at that frequency. Bingo. There you go. We've still got

**Dave Jones:** that capacitive coupling. There's no delay line in the breadboard at all. It's just it's just that coupling there. So, I'm not sure what's happening with that one cuz it's not a multiple there. So, maybe some sort of near field

**Dave Jones:** surface effect or I don't know. I'm probably talking out my ass. I have no idea. There's something physical going on there. And what I'm going to do is have a look at the output amplitude versus bandwidth here. Now, I've got it

**Dave Jones:** set to 1 MHz and if we zoom all the way in there, you can see that it's 1 MHz but uh it won't uh that counter just doesn't just doesn't kick in there. It really is uh quite annoying there. But uh yeah, it's

**Dave Jones:** picking up the repetition rate there instead of the uh burst frequency. But that is 1 MHz. So, we're going to start there and you'll see that we're getting no output and I'm right down at 50 mV per division there. We're really down in

**Dave Jones:** the noise. We are getting nothing. So, I'm going to turn this going to wind the wick up here. And uh 1.5 MHz, 2 MHz 2.7. So, you know, around about, you know, 2 and 1/2 we sort of start to see

**Dave Jones:** a bit of something. We're at 3 MHz now. And we're at let's go to the uh nominal operation frequency this 4.4 MHz and you'll see we're still at 50 mV per division but we do have a 64 microsecond

**Dave Jones:** uh time in there and I I trust me and guarantee you if we go in there that'll be 64 microseconds of course cuz we've already discovered that it doesn't change with uh frequency. And as you'll see there now I'm at 5 6 6 MHz

**Dave Jones:** now and you'll see the amplitude going up. 7 MHz. Really? Well, we're really going change that to 50 mV per division. Going up. 9 MHz, 10 MHz now. So, if we get zoom in there we go. We're 10 MHz

**Dave Jones:** there. And one thing you'll notice is that when we get to that I'm at 4 MHz now or 4. Say 4 MHz, you start to see that little uh ghost pulse there after that that little reflection pulse. It's not a

**Dave Jones:** complete multiple of the uh distance of this delay line, but you see that kick in over that 4.4 MHz mark. Now, I've gone up to 10 MHz now and let's go right up and try to find the peak value of this

**Dave Jones:** thing. I'm 12.2 MHz. There we go. So, about 13 MHz. So, we zoom in, we're at 13 MHz there. And that 13 MHz for this particular physical configuration cuz we don't have the tuned LCs in there. 13 MHz seems to be the peak

**Dave Jones:** frequency in there and you'll notice uh that's 15 MHz and we go down where it's 16, 17 MHz, 20 MHz, etc. So, 21 MHz, there we go. And you'll notice that there's uh some coupling through there as well at high frequency.

**Dave Jones:** But, yeah, basically that it does seem to have a very wide operational frequency range. So, if I set it to that is that 13 MHz which seems to be about the maximum there where it's 50 mV per division. So, we're still not

**Dave Jones:** getting if we set it to the same volts per division and they're both 1 V per division. See how small that uh output there is. Now, how high that would be with your tuned LC filter in there, I don't know. You would have to

**Dave Jones:** actually build the thing and check that out. But, you'll notice that the if you looked at these Sony schematic diagram as we saw in the previous uh teardown, we would have we noted that there was a differential amplifier in

**Dave Jones:** there, you know, amplifying the output of this thing. So, you can expect it to be reasonably low. But, as I said, uh near the start of the video, I'd expect significant differences in that depending on uh models and types of

**Dave Jones:** delay lines. And if you want to know if this thing is bidirectional or not, i.e., you can swap the input and the output, let me disconnect it from the breadboard here. You can see the coupling, high-frequency coupling as we saw before, and I'm

**Dave Jones:** turning the thing around. So, it's now backwards. And bingo, it's still exactly the same. We've still got our 64-microsecond delay in there, and everything's hunky-dory. And the other thing to note, let's have a look at our output here.

**Dave Jones:** Here's our output, and you notice that it is positive going exactly the same as the input all the way over here is positive going as well. Now, let's see what happens if we reverse the polarity on our output

**Dave Jones:** terminals and see if it goes negative. And bingo, it does. I just swapped the polarity on our output, and as you'd expect, it goes negative while the input still goes positive. And if you're wondering if we can actually do anything

**Dave Jones:** by physically touching the glass, well, the answer is uh not much at all. Let me tap it.

**Dave Jones:** I'm tapping the thing there, and well, you know, we can't really see much in there at all. Let's We we could actually trigger off the output here and get it a bit stable. There we go. That's And I'm tapping.

**Dave Jones:** You can probably hear that. I'm tapping that with my finger, and you can it can't really see anything. Yeah, there might be something in there, but that seems to sp- sporadically pop up even if I'm not touching even if I'm not tapping the

**Dave Jones:** thing. So, really, it uh they don't seem to be very vibration sensitive at all. And if I squeeze it with my finger, I'll stay away from the uh wires there, so I'm not capacitively touching anything. So, I'm squeezing the edge there, and

**Dave Jones:** you can see the amplitude certainly does drop. It dampens that a fair bit as you probably expect, just like the epoxy um stuff dampens thing and you know, it works as a dampener, so does that. And if I really

**Dave Jones:** really squeeze it There we go. But, we haven't killed it. We've just dampened the thing, and we've still got our delay time is exactly the same. Our delay's line doesn't uh change at all because um of course the

**Dave Jones:** uh shear wave, that S-wave is flowing through the body of the glass. It's not actually on the surface at all, but uh you can certainly dampen it. It's quite interesting. And if you're wondering what happens with no load on this thing, where it

**Dave Jones:** we're still at uh 12 14 MHz there, actually. 14 MHz. Now, let's remove the load resistor here. So, we'll pull that and bingo, we have actually gone up a bit, but it hasn't changed the delay time at all. Now, let's lower the frequency

**Dave Jones:** there. Oh, 4 MHz. There we go. We're still 11 MHz, 10. So, we still send a peak around that 13 MHz mark there. And if we go all the way down to 4 MHz or so again, there we go, 4.4 MHz. We're still way

**Dave Jones:** down in amplitude. So, that that load, you know, doesn't really make much of a difference in this particular build. So, let's increase our burst period here up to 1 ms and have a look at some of these reflections in there. We should be able

**Dave Jones:** to do that at 1 ms. Let's give it a go. And there we go. We now have a 1 ms period between these things, 500 microsecond per division. We've got the same number of bursts. As I said before,

**Dave Jones:** the number of bursts does not matter at all. It makes absolutely no difference. Let's turn that frequency up to where it peaks there at uh 12 MHz. 12.5 MHz. Even at lower frequencies, I can't see any notable reflections in there now. So, looks like

**Dave Jones:** this is a pretty good glass layline, but if we remove our 270 ohm source termination resistor, bingo, we get a reflection in here. And if we take out the Uh let's take out the uh load resistor. Now, we're just getting

**Dave Jones:** excess noise in there, which is of course just 50 Hz crap all the way in there, but we're not getting any additional reflection really due to the lack of a uh load termination resistor. And if I turn on high-res mode on the

**Dave Jones:** scope here, we can actually um see a couple little Yeah, one reflection there, then another one cry you know, right there. And uh I've got the uh source resistor uh source termination resistor in place here, and that's uh 3 and 1/2 MHz. Basically, go down to

**Dave Jones:** 3 MHz. So, you can see the reflections change in there a little bit, but not much. Let's go up to 4. 43, which is supposed to be its uh nominal operating point, but really, you know, that Hang on. Let's 4.43. There it

**Dave Jones:** is. And uh you know, really, we don't see a huge amount of difference there at all. So, if I go up 5 MHz, that first one disappears there, and we only get that second reflection there. So, you know, I mean,

**Dave Jones:** you can muck around with this until the cows come home with various uh source and termination uh impedances and tuned circuits and all sorts of uh stuff, but really, we're not getting uh significant reflections there at all. So, I'm up at 6 MHz at the

**Dave Jones:** moment, and we're up at 10 MHz there, and you know, really, we are We are talking very low amplitudes out still, and even much lower than that reflection there. So, if we up the frequency, 10 11 12 you know, 13 MHz, we're really you

**Dave Jones:** know, it starts to the reflections start to completely vanish there. So, really, there effectively is no uh resonant point for this thing. It doesn't, you know, there really doesn't seem to be much happening there at all. There's just a

**Dave Jones:** couple of little pulses, but um they are effectively all over the entire bandwidth of this thing. So, there's just some uh simple initial experiments on these glass delay lines, just having a bit of a muck around. Um it might be interesting to do some more

**Dave Jones:** thorough uh tests on these things to actually uh see how they perform with their real uh LC uh loads on them as well, actually tuned to the specific frequency. But, as we saw, they do seem to have a very large uh

**Dave Jones:** bandwidth and that's backed up uh by the uh uh theory as well. And these things are really uh quite uh linear and quite um remarkable uh devices in terms of the uh information that you can push, the bandwidth and information you can push

**Dave Jones:** through, you know, just uh essentially what is just a piece of glass with a couple of transducers. I mean, there's, you know, more to it than that. Just the physics alone on and just the material physics alone on these things is really

**Dave Jones:** complicated subject and you can do entire PhD thesis on just one aspect of these things. So, they really are fascinating. As I said before, I've linked below an interesting um uh paper on these things, an interesting uh section from a paper anyway, on a bit

**Dave Jones:** more of the uh theory of how these things work. So, I would suggest you take a look at that if you're interested in these things. So, I might follow this up with uh some more videos playing around with these glass delay lines cuz

**Dave Jones:** they're quite fun and fascinating devices. If you want to discuss it, jump on over to the EEVblog forum cuz that's where everyone hangs out. And don't forget, give it a big thumbs up if you like it. Catch you next time.
