---
video_id: lf_HBWfFdNY
title: EEVblog 1729 - AC Basics Tutorial Part 7: AC Ohms Law
url: https://www.youtube.com/watch?v=lf_HBWfFdNY
source: youtube-asr
---

**Dave Jones:** Hi, welcome to part seven in the AC basics tutorial series. This one we're going to look at Ohm's law for AC and other things, not just Ohm's law. And the great thing about this video is you already know it. You've already learned

**Dave Jones:** this in the DC fundamentals series. I'll put the playlist for the DC fundamental series down below. We learned Ohm's law, Kirchhoff's law, node and mesh analysis, superposition theorem, and all that good stuff that we used for DC. It actually

**Dave Jones:** is identical for AC except we're actually using complex math instead of real math like we did in DC because there's in DC there is no AC component. There's no difference between the no phase difference between cuz there is no

**Dave Jones:** phase there is no phase difference between the voltage and the current. Whereas in AC there is and I'm not kidding when I say it's exactly the same as DC. Let's take a look. Let's take a look at AC Ohm's law. Here's the Ohm's

**Dave Jones:** law triangle. You're in no doubt familiar with. V on top and then I and instead of R for resistance we've got Z for impedance which we learned about in part six. Now, these are actually should be italicized. There should be like a an

**Dave Jones:** angle on the V and the I to indicate that these are actually AC and they have a real and an imaginary component and that's what we learned about in part six when we learned about impedance. We learned that an impedance Z is which is

**Dave Jones:** designated by Z. In this case we've just got a two not resistor series a two impedance two impedances in series here. Impedance which is measured in ohms just like resistance is is made up of a real component and an imaginary component

**Dave Jones:** which has a phase basically has a voltage and current relationship with phase angle and this is in the rectangular form. You you also have it in the polar forms and the same thing for the voltage over here. Voltages are

**Dave Jones:** going to have a real component and an angular component or an imaginary component. I've put this in the polar form, so that's why it's got the angle with theta and we've just nominated 0° here, but it can be any other angle. And

**Dave Jones:** likewise, the current is going to be a complex component. It's going to have a real and an imaginary part to it. So, let's look at this simple series two impedance circuit here and calculate the current I using Ohm's law. Now, when

**Dave Jones:** we're talking about voltage and currents here, we're talking in this particular case sinusoidal waveforms and the RMS value of the waveform. So, 100 V here, this 100 V source is 100 V RMS and if the current was 1 A, then that'd be 1 A

**Dave Jones:** RMS. And the phase angle, typically when you've got like a source like this, that'll be your reference. So, you put that 0° there as the reference angle, but let's calculate I. So, to calculate I, of course, in a

**Dave Jones:** standard resistance circuit, you just add up the two resistors to get the total resistance and to find current using the Ohm's law triangle, you just cover up the unit you want, in this particular case I, and it's V on Z. So,

**Dave Jones:** but we've got two impedances. It's hard to remember they're impedances and not resistors. I get tripped up all the time. I'll probably make a mistake in this video. Leave [laughter] it in the comments down below. Anyway, so we need the total

**Dave Jones:** impedance here. And of course, two impedances or two resistances in series, you just add them up. And that's why we've got them in rectangular form like this because when we did our complex number maths video, complex numbers are

**Dave Jones:** not complex, they're really easy. You need to know that video before watching this. If you're going to add up two complex numbers, you want them in rectangular form like this. It's just way easier than polar form like this

**Dave Jones:** over here. So, let's work this out. Zt here, the total, is Z1 + Z2. I know that looks like a two. Often, I put like a little thing through the Z to indicate that it's actually a Z, not

**Dave Jones:** that American Z rubbish. So, sometimes I do that, like it's just a habit. So, to add these two rectangular complex numbers, really easy. You just add the real parts here. 15 + 25, that is going to be 40. And then, we don't Notice how

**Dave Jones:** we've got a negative here? So, this impedance is going to be primarily capacitive. That's why we've got a negative in there. And this impedance Z2 is going to be primarily inductive because it's a positive value. So, we just add up the complex part or

**Dave Jones:** the imaginary part, the J component of this rectangular form. -20 plus plus 50 is plus J Wait, we have to keep including the J in there. Plus 30. It's simply -20 + 50 is + 30. So, that is our

**Dave Jones:** total impedance of the circuit in complex form in rectangular notation. So, we know our voltage now, and we know our total impedance here. We want to calculate the current I is V on Z. V on impedance, but V on Z total. So,

**Dave Jones:** impedance total here. Now, because we're doing a division, if you're doing a division or multiplication, you want numbers in polar form. It's just going to be easier to do it than in rectangular notation like this. So, voltage we've already got in our polar

**Dave Jones:** form. If we didn't, we would have had to convert it over, but it's 100 V angle 0°. But, our impedance is in rectangular form, so we have to do rectangular to polar conversion, and you whack that in the in your confuser here and it's uh 50

**Dave Jones:** angle 36.87 positive angle 36.87. And then to divide two complex numbers in polar notation, you should easily know how to do that. You just uh the real component here, you just divide them. 100 / 50 is two. That's our uh

**Dave Jones:** current there in amps. And then our phase angle theta here, when you divide, you subtract the angles. So, it's 0°. So, -36.87° That gives you Oh. Oh, I got it wrong. Minus minus 36.87° in there. So, that's uh that's easy

**Dave Jones:** peasy lemon squeezy. Now, I'll go and show you how to do rectangular to polar conversion on your confuser here. Good thing about any good scientific calculator is it's going to have a polar to rectangular and rectangular to polar

**Dave Jones:** function. And on Casio, you'll typically find that down here on the positive and negative keys. That's what this R to P and P to R thing is on your calculator there. If you've ever seen that and wondered what the heck is that, that's

**Dave Jones:** exactly what it's used for and it makes it really easy to convert between polar and rectangular and vice versa. Now, the first thing you've got to absolutely make sure about is that your calculator is in degrees mode. We can switch modes

**Dave Jones:** like that and if we're in radians mode or we're in gradients mode there, it's the numbers just aren't going to work because our complex notation is in degrees here. So, we have to be in degrees mode on your calculator. So, we

**Dave Jones:** want the R to P or rectangular to polar button here. It's a shift function. So, what we do is we first take our real component. So, we go 40 and then we go shift R to P, rectangular to polar. It

**Dave Jones:** knows it's in that mode. Now, it's waiting for the complex part, which in this case is plus 30. So, we just put in 30. If it was minus 30, we would use the if it was minus J up here, for example,

**Dave Jones:** we'd put minus in, but it's not. It's plus 30 like that. And we simply press enter, and that takes a software might take a second cuz it's doing a fair bit of math there, and then it gives us our answer. At first, it

**Dave Jones:** gives us our real component, 50, like that, and the imaginary component, or the angular component in polar form, is in the Y register. So, we go shift XY like that. Bingo, 36.87 degrees. And that's how you convert rectangular to polar. Easy peasy lemon

**Dave Jones:** squeezy. And if you want to convert polar form to rectangular form, you do exactly the same thing. You put in the real component first, 50, we do shift polar to rectangular P to R mode next, and then we put in our angular

**Dave Jones:** component, 36.87, and we press enter, and bingo, there we go. It's rounded a little bit because we rounded the number there, but it's 40, and then the Y register will contain our imaginary part there. It's 30. Simple, huh? So, you see how easy that

**Dave Jones:** was? It is no different to DC Ohm's law at all, except you've got a complex number instead of just a real number. An impedance is a complex uh number that is made up of the real component and the imaginary component. I

**Dave Jones:** with imaginary meaning the basically the phase difference between the voltage and the current inside uh the and across that uh impedance there. So, up there it's simple. It's that easy. It's exactly the same, and that goes for all

**Dave Jones:** of the laws that you learned about in the DC fundamental series. Kirchhoff's laws, nodal analysis, mesh analysis, Thevenin equivalent circuits, Norton equivalent circuits, superposition theorem, all of that is works exactly the same in AC except you're using the

**Dave Jones:** impedance Z. Lost a calculator. I've got plenty more. Where was I? They're all going to work exactly the same in AC as they did for DC just using complex numbers. So, all of the same maths, all the same working

**Dave Jones:** out, all the same things you did in the DC fundamentals uh stuff, it's exactly the same here except resistors and volts. There's another calculator. I do actually have plenty of them. Turns out, I think it's the angle of the

**Dave Jones:** calculator. Angle, get it? Ha, near a week. So, solving AC circuits is a complete nothing burger if you've already done DC. If you already know how all your DC uh stuff works and all your different techniques uh for solving

**Dave Jones:** things and basic Ohm's law, it's no difference whatsoever. You just got to remember that now you have a voltage and phase relationship for your voltage, your current, and your impedance down here and hence why they all have a real

**Dave Jones:** and an imaginary part, be it in rectangular form or polar form like this. So, there's really no value in me going through any of these and doing uh the working out and explanations for them because it's exactly the same

**Dave Jones:** methodology as before. It's just that you got complex numbers which aren't complex at all. So, if you enjoyed that, please give it a big thumbs up. As always, discuss it down below and check out the entire playlist series for both

**Dave Jones:** the DC and AC fundamental series. Catch you next time. >> [music]
