---
video_id: yEG6pKUdIlg
title: EEVblog 1469 - AC Basics Tutorial Part 2 - Phasors
url: https://www.youtube.com/watch?v=yEG6pKUdIlg
source: youtube-asr
---

**Dave Jones:** Hi, this is part two in the AC fundamentals tutorial series. In part one, we took a look at what an AC waveform is, how it's generated, the pros and cons, and we looked at RMS and peak and average and all that sort of

**Dave Jones:** fun stuff. But now, in part two, we're going to take a look at phases and complex numbers. Now, you might have heard of complex numbers before, but trust me, they're not that complex. They're mathematically not complicated at all. And we're going to find out why

**Dave Jones:** every calculator, even a very basic one, has this R to P and P to R button on it. Stay tuned. Right, so you're familiar with our AC waveform. This is voltage here, 0 V here, and it goes for or it

**Dave Jones:** could be current as well. Voltage or current, doesn't matter, interchangeable really. And it follows a sinusoidal shape like this. And it actually goes negative voltage positive and then negative voltage like this or positive and negative current. And in the

**Dave Jones:** previous video, we saw how this was generated from a moving coil inside a magnetic field. We've got north and south magnets here. And as the rotor turns in there, um there's a phase angle theta in there. And it actually um draw

**Dave Jones:** it starts at zero here and it draws as it sweeps through like that, it actually ends up drawing that waveform. As it goes up there would be the peak waveform. And then down here, it'd be back to zero. And down here, it'd be

**Dave Jones:** over here. And so on. And that's how you get your sinusoidal shape. It's a natural consequence of a rotating coil in a magnetic field. And in the previous video, we took a look at the other button on your calculator here, degrees,

**Dave Jones:** radians, and gradients button. And we'll forget about gradients, cuz that's a weird thing that like civil engineers and people use. Anyway, degrees and radians are the two big things in electronics here when you're analyzing AC and other uh waveforms like this. And

**Dave Jones:** uh radians, of course, is uh 2 pi and or you can go from 0 to 360 in degrees. So, you know, choose your poison. Of course, we looked at theta, the phase angle here is omega t cuz this is time axis like

**Dave Jones:** this. Um as this thing moves around, it increases in time and uh theta, the phase angle, is equal to omega t. And that is not a w, that's actually omega, which is actually uh the lower case version of also omega, which is the ohms

**Dave Jones:** symbol. That's just the upper case version. So, if you want to look at the equation for AC voltage, it actually looks uh like this and it's the same for current as well. You just change uh v in here for i. It makes uh no difference.

**Dave Jones:** And uh vt here uh because it's got a time component um is equal to vp or v peak uh the peak voltage times um sine, which is the signet because it's a sinusoidal uh wave shape. Um and omega t

**Dave Jones:** plus a phi in here. Phi is different to theta. I've got that here. Theta is they're different Greek symbols and they actually mean different things. And it's rather subtle. In this particular case, when we're looking at and analyzing just

**Dave Jones:** the one waveform here, then we use uh theta um which is the phase angle. But when we start talking about, as we're doing a minute, looking at uh two waveforms, then uh we have to start using phi, which is the phase difference

**Dave Jones:** between two waveforms or between a waveform and a reference. So, equations like this they start getting a bit ugly when you get all this trig stuff in here like this. It's gives you the heebie-jeebies. So, engineers, what we've done is we've uh

**Dave Jones:** we use phases instead of um these sorts of equations. So, we're going to have a quick talk about and look at phases first. Now, Ohm's law, of course, V = I * R, okay? We did that in the DC

**Dave Jones:** fundamentals series. Well, the AC version of this is actually V with a little arrow on top, which means a vector like this, and then you've got I, which is a vector, multiplied by uh we should have a little dot in there to

**Dave Jones:** signify multiply, and instead of R, because we're talking about AC, it's not resistance anymore, it's impedance. And impedance is designated by Z, and Z has a vector component as well, cuz we when we start talking and analyzing AC

**Dave Jones:** waveforms, we have vectors. And you can see in here this is a vector. It's an arrow, like that. They're called vectors. And this is where the word phasor actually comes from. It's a combination of vector at the end and

**Dave Jones:** phase angle. So, we're using a vector, and we're rotating it and getting a phase angle, hence the name phasor. So, we work with phasors. And when we've got our phasors, which is a vector like this, a vector a vector it has a

**Dave Jones:** magnitude like this and a phase angle. So, now we'll get rid of our magnet thing, cuz we don't want to deal with like we don't care how this sinusoidal wave shape is generated now. All we care about is how we look at and analyze AC

**Dave Jones:** circuits using phasors. Now, we have to introduce a second sinusoidal waveform, because this is where all the advantage of complex numbers and phasors and everything comes in. So, let's just draw another AC waveform in there. Now, you can see

**Dave Jones:** that it's lower amplitude like this, its peak voltage is not as much, but it crosses the zero point at exactly the same time and it reaches the same peak at exactly the same time. I didn't have time to build it to scale or to paint

**Dave Jones:** it, but you get the idea, right? It's exactly the same waveform except it's a different amplitude. Now, when you have two waveforms like this that cross at exactly the same point and also uh reach their minimum and maximum um at the same

**Dave Jones:** time, these are called in-phase signals. And if you wanted to represent this as a phaser like this in our diagram over here, okay? We can do that. This one here is that length there, okay? That's showing because the length of the vector in here

**Dave Jones:** represents the amplitude there. And you So, during time when this vector goes around like that, that will equal the amplitude over here. So, the length of the vector equals the peak amplitude. But, the red waveform, because there's no phase difference between these, that

**Dave Jones:** phase angle we had before, theta, that's actually zero or phi actually because we're talking about two waveforms now, okay? It's exactly the same, but it's this amplitude here. And we can draw another circle in there. And if we dot that across, we'll find

**Dave Jones:** that these amplitudes are exactly the same. We've got two different phases here with two different amplitudes, but they're represented pointing in the same direction because there's zero phase difference between them. They're in phase. Now, if your other waveform, the red one here is the

**Dave Jones:** exact opposite of blue, blue is going to be our reference waveform here. You always when we're talking about all this sort of stuff, you always have a reference waveform, and that's where you get the uh phi from. You have to have a

**Dave Jones:** reference in order to figure out whether you're leading or lagging or we'll go into that in a a But, anyway, um so, you've got a another waveform here that crosses at exactly the same points here, but it goes in the opposite direction.

**Dave Jones:** It reaches a peak that's opposite, like this. This is called anti-phase or 180° often 180° out of phase or simply out of phase. So, the common terminology there is in phase if they cross at the same point and also reach peaks at uh

**Dave Jones:** on with the same uh polarity, then they're in phase. If they cross at the same time, but they reach opposite uh peaks at the same time, then they're called anti-phase or out of phase. And the phaser over here, you guessed it,

**Dave Jones:** it's 180° like that because the amplitude's a little bit smaller. It's and you can draw your circle in there and dot that across and it gives you a good physical representation. So, these phasers are actually useful for uh

**Dave Jones:** graphically understanding and illustrating and as we'll see in a second, actually, um, adding up these waveforms as well. You can actually do maths using uh phasers like this. You can do uh all your arithmetic graphically. Now, let's draw another sine wave in here at a

**Dave Jones:** different phase angle like this or it has a phase shift and we have to start talking in terms of phi here because the difference in the phase angle between where they cross like this. You can take any point. You can take a peak or any

**Dave Jones:** other point. It's just convenient to do it at the zero uh crossing point. This difference in phase angle between here and here, that is our phi. That is the phase difference between the two waveforms. As I said, uh the blue one is

**Dave Jones:** going to be our reference. You have to pick a reference. Technically, it might not matter which one um it is. You pick a reference. That's the whole idea of this is you have a reference waveform and then phi is the phase difference

**Dave Jones:** between uh the second waveform from the first one. How many degrees or radians, depending on which uh system you're using, how many degrees or radians difference. Now, an interesting thing to note, when you have two sine waves, it

**Dave Jones:** doesn't matter what their amplitudes are, it doesn't matter what their phase angle or phase difference is, makes no difference whatsoever. When you add the two of these up or you subtract them, you end up with a sine wave. You always

**Dave Jones:** end up with a sine wave of some amplitude and some phase. So, on our phasor drawing over here, how can we draw in the red uh waveform? Well, we've drawn in the blue waveform, our reference waveform here at time zero,

**Dave Jones:** we're drawing it at time zero, and then it rotates, it has an angular momentum or an angular frequency as time goes on. So, that that would be your angular frequency over here. In fact, that's what theta is. Um omega t is your

**Dave Jones:** angular frequency over there. I forgot to put in. Remember that omega is actually 2 pi f. There's a frequency component in there. So, we have to take that zero reference, and what what is our value at zero here? Well, we can dot

**Dave Jones:** that across like that, and at that point there, where it crosses our uh our amplitude reference circle, like that, I'll call it. I don't think that's I don't think it hasn't Does it have a name? Yeah, amplitude reference circle,

**Dave Jones:** that'll do. Anyway, um we draw that over, and then at that point, that's the point at time zero. So, you draw a vector in that, and you've got the exact magnitude. This is if you actually did this on graph paper, right? Or in a CAD

**Dave Jones:** package or whatever, um you would this would these would all perfectly line up. It's a bit how you do it here on the whiteboard, but if you draw it up, this is exactly, you know, you can actually take measurements off this and as we'll

**Dave Jones:** see in a minute, you can actually add these waveforms up. So, that phase angle in there or phase difference, that's going to be phi like that. Okay, so let's actually drop this down onto what's called an Argand diagram and this

**Dave Jones:** is what you analyze and you know, sort of like visually represent complex numbers in and we're eventually getting to complex numbers. We're still, you know, looking at how we're going to add phases. Anyway, we can add these two

**Dave Jones:** waveforms together cuz this is a standard operation in electronics you want to do is you want to you've got two AC waveforms and you want to add them. Well, we draw them in as our the blue's not very good, is it? Anyway, now on our

**Dave Jones:** Argand diagram, this one going right like this on the x-axis, this is actually what's called our reference plane or our you know, it's equivalent to our reference waveform down here and that's why we draw our reference waveform actually on there because

**Dave Jones:** there's no phase difference between the reference waveform and the reference. The reference waveform is the reference. So, that's why it gets put down here as V1, voltage one. And then we've got voltage two, which is a vector that has

**Dave Jones:** a phase angle. So, we can actually add graphically these two waveforms because as I said, you remember the length of these vectors is actually represents the actual real magnitude, the peak voltage of the waveform. So, what we can do, we can add

**Dave Jones:** these graphically. So, what we do is we get our ruler here, recommend a micro ruler and you actually get the exact length of it like that and you keep the angle, so hold my tongue at the right angle

**Dave Jones:** and I'll move this across like this and I will draw da a vector in like that. And of course, you'll also find that that length there, if you move that up like that, should be the exact length over there like that.

**Dave Jones:** And this gives us a new point over here. And what we can do is we can draw in a line like that. Bingo. You guessed it. The amplitude of this line, the length of Oh, look, it's almost the length Oh, it's pretty much

**Dave Jones:** precisely the length of my ruler, which is 1/10 of a smoot, by the way. This is the only ruler in existence that's actually has a smoot scale. This is 1/10 of a smoot. So, our vector here is 1/10

**Dave Jones:** of a smoot. So, the amplitude will actually be up here somewhere. Whoa, it's gone off into the title. I didn't plan this very well. So, this is a graphical technique you can use to add two waveforms together and get an actual

**Dave Jones:** proper magnitude result out of it instead of using your confuser over here. Now, you start at time zero like this, okay? So, we've got our two waveforms, our blue and our red like this. And basically, we start at time

**Dave Jones:** zero here, and then we rotate around and we add them at every So, as we rotate this like this, we're going along the time axis and we add them up. So, the blue waveform is zero at this point. The

**Dave Jones:** red waveform's up here. So, our green waveform, we'll call that our sum waveform, is the green one. It's the addition of the two of them. Obviously, it starts out at this point, and then it's going to be a bit how you doing

**Dave Jones:** here on the whiteboard. So, it's not exactly correct, okay? But, if you did this, as I said, on proper graph paper, and you actually did it properly, you would get a real proper magnitude response. And so, you add them together.

**Dave Jones:** So, at this point here, for example, where they cross, obviously, they're the same value, so it's going to be double the height up there. And, you know, so you do this at every point along here, and you eventually plot out this green

**Dave Jones:** sum response like this. And as I said, any two sinusoidal waveforms you add together or uh subtract, you will always end up with a sinusoidal result. So, it'll be some sinusoidal result. It'll be a larger amplitude because you can

**Dave Jones:** see them actually add uh like this. So, we get our resultant summed waveform using uh phasor addition, it's called. It's a graphical technique. You can do this, but pretty much nobody really does this anymore because that's what complex numbers are for.

**Dave Jones:** When you start dealing when you start talking mathematically about analyzing AC waveforms, you're not doing it graphically with vectors. But, you can, and that's where it started. And I'm sure we talked in the previous video about leading and lagging waveforms. If

**Dave Jones:** they're not in phase, then uh your V2 here because you're always talking in terms of the reference, V1. So, our voltage waveform V2 here, the red one, is either leading or lagging uh depending on the phase difference between from the reference here. In this

**Dave Jones:** particular case, it's uh leading because um just just take the zero crossing point as the reference. You can take any point, but it's easier, as I said, to take the zero crossing reference. It actually crosses the zero point and goes

**Dave Jones:** negative before the blue waveform does. So, it's leading this waveform. It it does the business first. Um so, that's called a leading waveform. But, if the red waveform was like this and it actually uh crossed the zero point and

**Dave Jones:** went negative after our blue reference waveform, then it would be lagging. I'm sure in the previous video, I've mentioned uh the convenient um acronym CIVIL here. Gradients, anyone? Um anyway, for capacitors and inductors, uh in this particular case, okay, V is the

**Dave Jones:** voltage, I is the current, and for a capacitor like this, so C is the capacitor, the current I leads the voltage. So, the current leads the voltage and for an inductor, the current lags the voltage cuz it's after. So, you

**Dave Jones:** you know, anyway, you get the point. And that's why this is not just about generating like voltages with motors and and stuff like that. In circuits, you have capacitors and inductors and capacitors and inductors create a phase difference between waveforms, voltage

**Dave Jones:** and current waveforms. So, hence you know, it's important to know this and for a capacitor, the current leads the voltage. And when you add reactive components like this as they've called and we might see why in a minute,

**Dave Jones:** reactive components change the phase angle of the voltage and or current in your circuit. And this is why we get into complex numbers cuz it does like it gets a bit more complex to analyze it. That's not why it's called complex.

**Dave Jones:** Anyway, it's called the complex plane here. So, that's phases. So, this is graphical addition using phases and it's important to learn the concept of where this all comes from because nobody really like uses these graphical methods to actually

**Dave Jones:** do calculations anymore. That's what complex numbers are for. So, complex numbers is not that complex but because we're spending a significant amount of time on the background of phases here, we'll leave complex numbers for the next video. I'll link that up here and down

**Dave Jones:** below. Anyway, hope you found phases interesting. Come check out complex numbers in the next video. Catch you next time.
