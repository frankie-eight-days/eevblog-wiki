---
video_id: Iq4QlfH-oqk
title: EEVblog #926 - Introduction To The Oscilloscope
url: https://www.youtube.com/watch?v=Iq4QlfH-oqk
source: youtube-asr
---

**Dave Jones:** Hi, let's check out this cool looking device, the humble oscilloscope, the most essential tool in all of electronics. What is it? Why do you need one and how does it work? Let's go. But before we take a look at the

**Dave Jones:** oscilloscope, both the modern digital type and the old school analog type, we have to take a look at the multimeter. You're familiar with the multimeter and how it measures voltage among other things, hence the name multi, measures multiple things. Now we can put it on DC

**Dave Jones:** volts here and we can measure our battery, which is a DC source. There it is, 9.23 volts. No worries, right? But what happens if this voltage changes? Hmm. Now just imagine that you start to graph this voltage that you measure on your

**Dave Jones:** multimeter. It on the Y axis here we've got voltage and on the X axis here we've got time. So let's take this one sample point here at uh let's say at the one second mark, we measure that on the

**Dave Jones:** multimeter and we get our 1.5 volts or whatever it is. Now what happens if we keep actually taking a reading on our multimeter every second or 1/10 of a second or 1/5 of a second, whatever the multimeter updates at. You

**Dave Jones:** might end up with something that looks like this. And you might have noticed it looks something like this sine wave we're getting on our oscilloscope here and that's all an oscilloscope does is it measures voltage on the Y axis here

**Dave Jones:** versus time. And if we hook our multimeter up to our adjustable lab power supply here, we can adjust that voltage and we can see that voltage change with time. It's not just one fixed value. But if I turn this knob

**Dave Jones:** really quick, the multimeter really has a hard time keeping up with that. And that's a huge limitation of the multimeter is that it does not allow us to view these changing voltages or signals as we call them. And why is that

**Dave Jones:** a big deal? Well, because practically all modern electronics works on high-speed signals that you cannot display on a multimeter. You just can't see it changing with time. So, our oscilloscope is a window of voltage versus time here, and we can slow it

**Dave Jones:** down with what's called the time base, and we can display these signals. Now, DC is not interesting. It's just a fixed line because it's at a fixed voltage. But, if we adjust that power supply, ooh, look at that. It's

**Dave Jones:** jumping all over the place, but that's relatively slow. Good thing about this oscilloscope is it allows you to view a really fast-changing waveforms. So, if we use what's called the horizontal time base here, it goes from anywhere from

**Dave Jones:** seconds to milliseconds to microseconds around to nanoseconds like this, and it'll just allow The slower the time base, the slower the dot moves across there. So, the way we measure things on an oscilloscope is by this grid here or

**Dave Jones:** what's called a graticule. And you'll notice that it's volts per division. One division is one of these little squares either horizontally or vertically. That's why what's called the vertical amplifier here is in volts per division. So, if we're actually currently right

**Dave Jones:** here on one, it's 1 V per division. So, each time that line goes up by one division, bingo, that's 1 V. And likewise over here on our horizontal time base, it's in seconds per division or 0.5 seconds per division, and there

**Dave Jones:** you go, count it. Each time it goes across, it takes half a second to get to each division. This case is 0.1 seconds, so it takes 1 second to sweep 10 divisions across the screen there. And you'll notice that the dot goes across

**Dave Jones:** the screen or sweeps across the screen as it's called, and then it retraces back to the start. That's because we don't have an infinitely long screen, but we want to be able to view waveforms. So, it goes across and then

**Dave Jones:** jumps all the way back and starts displaying again and again and again on the same screen. So, if we disconnect that and feed in no voltage at all, and look where that line is, okay? It's the second division from there. We can

**Dave Jones:** actually adjust that to any position that we like, and I won't explain why. It's just handy to be able to do this at the moment. That's all you need to know. Then, okay, that is our reference point. That is our ground point or zero volts

**Dave Jones:** point. Now, if we plug in our signal, it's going up one, two divisions, and we're at one volt per division, so it's one volts, two volts, and what do you know? We're feeding in two volts. So, if we've got a circuit that we're

**Dave Jones:** analyzing, then we can just take our oscilloscope probe, which hooks up, we connect this onto the ground point of the circuit, and then we can start probing around and having a look at some of the signals that are in our circuit.

**Dave Jones:** Now, we never would have been able to see these with just a multimeter. It's a window into another world. So, this signal that we just saw here, look, it's got ground, and then it jumps up where it one volt per division here, so one,

**Dave Jones:** two, three, four, like four and a half volts. So, we've got ourselves a digital signal that we're looking at. We can change our time base like this, 0.1 microseconds per division on our horizontal scale over here. So, we can see the time difference

**Dave Jones:** between these two points. It's about one, two, three, four, five divisions there, or 0.5 microseconds between these little pulses. And we can zoom in using our horizontal time base. You might have noticed that this just looks like one

**Dave Jones:** thing, but we zoom into it. Look, there's more, even higher speed signals buried within there. Magic. And the oscilloscope is the only tool that allows you to view this voltage versus time, and to actually see all of the

**Dave Jones:** signals that are actually going on within your circuit. It is the essential tool for electronics design, troubleshooting, and just understanding what's going on in your circuit. You can't do without this oscilloscope. And really, that is all you need to know. An oscilloscope

**Dave Jones:** measures voltage versus time. Simple. That's it, really. Now, I'm feeding the same signal into an analog and digital oscilloscope here, and the digital oscilloscope works exactly the same, voltage versus time. Except it's got a lot more measurement functionality and

**Dave Jones:** things like that, but there's one crucial difference between the digital and the analog oscilloscope. The digital one allows you to store the waveform and analyze it. So, it allows you to freeze it and then work on the signal later and

**Dave Jones:** debug it and analyze it, but it also allows you to capture single-shot events, i.e., events that only happen once, whereas an analog oscilloscope won't be able to capture that. So, if you have a look at a very slow 1-Hz

**Dave Jones:** signal on an analog oscilloscope, you can see that you can just maybe see a trail going behind it there. That's because of the phosphor on the screen that's actually lighting up, but this is not a storage oscilloscope. So, all you

**Dave Jones:** get is the current present value as it sweeps across. But if you view the exact same 1-Hz signal on digital oscilloscope, look, the waveform stays there. You might be able to see it. Oh, there it goes. So, it stays on the

**Dave Jones:** screen at all times, and of course, you can press the stop button to freeze it at any time. And if I have an event that only happens once for a brief period, we can't see it. But a digital oscilloscope, we can

**Dave Jones:** put it in what's called single-shot mode by pressing the single button here, and it'll sit here armed waiting for that event to happen, as long as you set up the trigger right, and that's for another video, until our event happens,

**Dave Jones:** and bingo, there's our event. And we can zoom in and actually see exactly what happened there. In this particular case, I found some very interesting behavior here of when I actually switch on my Siglent function generator here using the output. So,

**Dave Jones:** it's got a relay based output there, and it's just doing something rather unusual. I didn't know that. Bingo! Couldn't see that with an analog oscilloscope. And if we hook our oscilloscope back up to our power supply and put it in what's called a roll mode

**Dave Jones:** here, then and I just the power supply, you'll be able to see I am wiggling that, and you can actually see it moving in real time cuz it acts like a chart recorder, those old-fashioned, you know, seismographs and things that

**Dave Jones:** you've seen. It's basically, you can see how it's changing with time, and I'm twiddling the pot on my power supply, and it's following that. So, that's kind of like different to what we saw on the analog oscilloscope. So, that's just

**Dave Jones:** another way of representing a voltage versus time, but the window just slides across. It just keeps sliding, going in that direction instead of capturing, but that is the subject of another video, I'm sure. So, if I disconnect that, our signal's gone. We can't do

**Dave Jones:** anything with it. But this, we can with the digital scope, we can just press stop, and bingo! We can go in there, and we can analyze that signal. Even though we've stopped it and we've disconnected it from the

**Dave Jones:** input, we can go in there, zoom in and out, and play around with it, and analyze that signal to our heart's content. So, that is an incredibly valuable insight, and the reason why you should have a digital oscilloscope over an analog one. And the

**Dave Jones:** modern digital oscilloscope allows us to measure all sorts of things automatically, like the voltage from the peak, the negative to the positive peak here, and allows us to get the average value, the frequency, and a whole bunch of other measurement stuff, the rise and

**Dave Jones:** fall time, which you may not be uh familiar with, but all these insights into your waveform, a modern digital scope can actually measure, and you can turn on uh cursors, for example, and then you can go in there, and it can

**Dave Jones:** automatically measure the exact time for you between that cursor and that cursor of the waveform, so you don't have to go in there and count them manually, and then squint and hold your tongue at the right angle, and go, "Oh, I think it's

**Dave Jones:** near enough to that." A modern digital scope can measure everything precisely. Now, of course, our humble multimeter isn't completely useless. It can, of course, measure AC alternating current. This is where the waveform goes positive and negative voltages like that. So, if

**Dave Jones:** we disconnect it, but if we connect it up, we'll notice that we've got a 1 kHz sine wave here. And, of course, this can measure it. It can measure the true RMS value of that changing signal, and it's

**Dave Jones:** accurate up to a certain frequency. Read the data sheet for your multimeter. 1.74 V. There we go. RMS voltage, because the digital oscilloscope can actually measure and calculate this mathematically. 1.79 V. It's There's a little bit of error there, but it's

**Dave Jones:** basically measuring the exact same thing. So, yeah, this can do it, but that's about all the multimeter can do. If you want to actually see your waveform, you've got to have an oscilloscope, and seeing is believing, cuz this is just a

**Dave Jones:** number. This actually tells you what's really going on. So, there you go. I hope you learned something about this oscilloscope here. And, yes, they're complicated-looking things, but they're so cool. They give you an insight into what's happening in your circuit. And,

**Dave Jones:** if you're getting into electronics, you want to figure it out, you want to play around with stuff, it is the essential tool, and you can buy them for a couple of hundred bucks. So, don't be afraid of the oscilloscope. They look complicated,

**Dave Jones:** but really, it's just measuring voltage versus time. All the extra stuff is just a bonus and they're really not that hard to use when you get into it. And if you do and if you are a beginner and you do

**Dave Jones:** get into trouble and things like that, you're mucking around and you're doing all sorts of things and you're not sure what's going on and everything's not quite working for you and it's where's my waveform? You can actually just hit

**Dave Jones:** the auto button and it will hopefully show you at least I get you a basic waveform on the screen. There it is, right there. And then you can start playing around with it. Although, I do of course recommend that you learn how

**Dave Jones:** exactly how an oscilloscope works and get to know it intimately so that you can use it. Incredibly valuable tool, the tool for electronics troubleshooting. And I've got other videos here which I will link in and at the end of this as well, including one

**Dave Jones:** where I show you how not to blow up your oscilloscope with your ground clip lead here. Very important you understand the grounding when it comes to oscilloscopes and things like that. So, I'll link that in down below. Hope you enjoyed it.

**Dave Jones:** Catch you next time.
