---
video_id: ZP0KxZl5N2o
title: EEVblog #1045 - How To Drive an LCD
url: https://www.youtube.com/watch?v=ZP0KxZl5N2o
source: youtube-asr
---

**Dave Jones:** Hi, this is a second video on a series on LCDs and how to drive them. I'll link in the first video down below which talks about LCD technology and how they work and things like that. This one we're going to look at driving a static

**Dave Jones:** LCD, i.e. a non-multiplexed LCD. Let's get to it. So we saw in the previous video that an LCD is just constructed with what's called a common which is actually more technically called the backplane electrode in there and then just basically the segment

**Dave Jones:** pins, however many segments you've got. And this is your typical static LCD will only have one common on here. So your LCD display is a glass sandwich with some liquid crystals in there and it'll have at least one common pin or common

**Dave Jones:** pin which is actually more technically referred to as the backplane electrode and then you've got all your other pins which drive your individual segments. In this case we've got a classic seven-segment display with one common and that's what we use in the

**Dave Jones:** practical example coming up. So, how do we drive this thing? How easy is it? Well, it could in theory be as easy as this. We'll take a look at two different ways to drive it. One of them's correct

**Dave Jones:** and one of them's incorrect, but still kind of sort of works, but you don't want to do it. So, trap for young players coming up. How do we drive it? Well, if we hook our common pin up just to our zero volt our ground

**Dave Jones:** pin and we can simply drive, put five volts on any one of the other pins. A typical LCD driving voltage might be three volts to five volts, something like that and we can actually turn these segments off and on just with a digital

**Dave Jones:** signal. You can drive it with any sort of digital logic, microcontroller or anything like that and it will technically work as I'll demonstrate shortly. But this is actually an incorrect way to do it. You do not want to drive this. Why? Because it Well,

**Dave Jones:** let's assume that you have one second on, one second off, a 50% duty cycle, it's going to give you an DC average voltage of, in this particular case with a 5 V drive signal, 2.5 V if it went up like that, for example, and

**Dave Jones:** it was 50% duty cycle. And DC offsets on an LCD will eventually kill them. You do not want to use this method to drive your LCD, but it does technically work. Now, some people will try and get around

**Dave Jones:** this by driving it with a burst. In this case, you know, you could have, say, 100 Hz or something like that to try and get your DC average value lower, but yeah, it's going to lower it, but you're still

**Dave Jones:** going to end up with some DC level on there, and it's not going to really eliminate the problem. Now, you can actually kind of use this method to actually drive it correctly, but you've actually got a take this negative for an

**Dave Jones:** equal amount like this, and in this case, you do it as a burst like that. So, you've got, say, you know, that can be your 100 Hz burst, for example. Uh just, you know, a low frequency, and then on and off, and

**Dave Jones:** then your DC level, instead of being 2.5 V, your DC your DC level, average DC level, becomes 0 V. So, this will be the correct way to drive your LCD using this. But the problem is, you've got to have a

**Dave Jones:** negative 5 V rail down here, and that's going to ruin your day if you've just got your digital logic, your 3.3 V digital logic, 5 V. You've got an Arduino to drive it, some other microcontroller to and you just want to

**Dave Jones:** drive your LCD. Getting that minus 5 V is a pain in the butt. Anyway, let's go have a little play around with this on the bench, and then we'll come back and show you a more elegant solution to

**Dave Jones:** solve this problem that doesn't use a negative rail. Not as clumsy or random as a blaster. An elegant weapon for a more civilized age.

**Dave Jones:** So, let's use the example of this same seven-segment LCD that we used in the previous video. I'll link in the data sheet down below. It's a nominal 5-V drive static display, which means it only has the one common pin, which is

**Dave Jones:** down in the bottom left corner there, and we're just driving one of the segments here. 2 V per division with a 5-V TTL signal there. 1 Hz on off on off on off, simple like that, and our ground reference point is there.

**Dave Jones:** And as you can see, that works just beautifully. That segment's turning off and on. The contrast is beautiful. Couldn't ask for anything better. You might So, you might hook this up to your microcontroller and think, "Hey, I can

**Dave Jones:** just drive this with my 5-V TTL signal or my 3-V TTL signal." This one will also work down to 3.3 V in this particular case. And you might think everything's hunky-dory. You might design your product around this. And it

**Dave Jones:** might work for 6 months, but look at the average DC value, of course, because our ground reference is here. The average value is up here like this at 2.5 V. I mean, I could just leave this at 5 V.

**Dave Jones:** Hook up the pin just permanently at 5 V. Yeah, the segment will come on, but then your average DC value relative to your common pin is 5 V, and that's going to eventually kill your LCD. So, while this

**Dave Jones:** might work, in {quote} marks, do not drive your LCDs like this. You want and need a 0-V average value for your drive signal. 100-Hz continuous 100-Hz square wave. And as you can see, the segment is on, but the contrast isn't that great."

**Dave Jones:** Now, let's have a look what happens if we actually adjust the DC offset of the signal. So, let's actually shift this down like this, and you can see that if we actually take that to zero DC offset, so

**Dave Jones:** we've got plus minus 2 and 1/2 V still 5 V peak to peak, you'll see that it's actually vanished like that. So, the nominal 5 V drive for this particular LCD isn't good enough. Now, if we actually continue to take that down

**Dave Jones:** to negative, you'll actually see that come good again. So, that's just the difference that the DC offset can make to the contrast on an LCD. Now, you can see that our signal drive level is still exactly the same peak to peak, but it's

**Dave Jones:** just not good enough. And it doesn't really matter what you do here. When you've got a ground reference here, and you're just driving your LCD positive, in this case, I've got a 0.5 second period, so it's flashing at a 2 Hz rate

**Dave Jones:** every 0.5 seconds, and I've got burst of a 100 Hz frequency in there. You're still going to end up with an average value, which is Well, it's not going to be in the middle anymore, but it's still going to be somewhere above zero. And

**Dave Jones:** that's eventually going to damage your LCD. So, there's just no way to drive this with your 3.3 V or 5 V LCD signal directly as you know it, like your regular 0 to 3 or 0 to 5 V.

**Dave Jones:** So, let me take it up to 8 V here, for example. The like it's coming on nice and dark, but you'll see it never switches off. Why? Because look, our DC our minimum level here is at minus uh 4 V there. It should be at zero. We

**Dave Jones:** need to drive it both positive and negative with the average value of zero because the average value at the moment, look, is minus two volts. It's not actually zero. So, if we actually shift our DC level to ground here, and this is

**Dave Jones:** the correct way to drive it as solid off and on, which we could achieve by other methods, but this way there's no DC offset on the LCD, we can't damage it. So, we've got to go both positive and

**Dave Jones:** negative, but that is a real pain when you're using digital logic to drive this LCD. So, while she can get away with using this method number one here to drive your LCD, it requires that negative supply and to get your DC average at

**Dave Jones:** zero. So, it's not very practical way to do it, especially with digital logic. So, we're going to have a look at another method. We'll just call it driving the common pin. Driving the common pin. And this is basically the

**Dave Jones:** industry, the more industry standard way to do it, and it's how most of your LCD driving chipsets, be they static ones or your multiplexed ones, which we'll have to do another video on cuz it's more complex, actually work. So, instead of

**Dave Jones:** actually hooking our common pin up to ground here, we're going to actually drive the common pin with a digital signal like this. And this is just your regular digital signal. Let's say zero volts and five volts like this. We're driving that

**Dave Jones:** backplane electrode in there. And you might think, why? Well, stick with me. It gives you a nice little trick you can do to avoid this negative five volt rail up here. Now, you might get a little bit confused by the terminology that

**Dave Jones:** industry terminology of common. Common, you might think common's always ground. Well, it doesn't have to be. The LCD is just its own independent floating thing. It's LCD here doesn't care what this pin is hooked up to. It can be put and

**Dave Jones:** hooked up to your circuit common, your five volt rail, 1,000-V rail, negative 1,000-V, it doesn't matter. It's only the relative difference between the common pin and the segment pins up here that actually matters to the LCD. So, we

**Dave Jones:** can drive that common pin with, let's say, 100 Hz might be a typical way of driving frequency. It's high enough frequency to avoid any visual flicker, but it's low enough not to chew a large amount of power due to driving the

**Dave Jones:** capacitance. The higher frequency you drive your LCD, the more you've got to drive the capacitance, the more reactive current that you're actually going to get through the capacitance of the LCD, and the higher the power consumption. That's why your LCD watch

**Dave Jones:** can last for years, assuming you don't have one of these new thing called stupid idiot smartwatches, can last for years or 10 years, or the shelf life of the battery. It's cuz the LCDs take practically nothing cuz they're only

**Dave Jones:** switching at, you know, 100 Hz or something like that. So, if we're driving the common pin with the 100 Hz, what does that achieve? Well, it achieves a neat trick in being able to avoid the 5-V rail. Let me show you how.

**Dave Jones:** Um, how do we turn the segments off and on? Well, you could leave the segments off just by having these pins floating, of course. A tri-state output on your driver, for example, then in theory, your segments would stay off because there's no

**Dave Jones:** voltage difference between those. The pins are just floating. But, because as you saw in the previous video, how just the electric field picked up by my body, I could touch the pins and cause those segments to turn on and stay on due to

**Dave Jones:** the capacitive charge and things like that, you don't just want to leave these pins open because they could eventually build up charge on them and then turn on, actually drift on. But, you always want to drive them. So, in this case, if

**Dave Jones:** you wanted them off, you could simply just tie them all like that. No problems whatsoever. If they're all at the same level, there's no difference between the common pin and the segment pins and the segments will stay off. No worries. But,

**Dave Jones:** let's say you wanted to drive segment A here, how do you do it? Well, it's easy. You use an invert You'll notice that we don't have an inverter down here. It's just a driving gate, but if we hook an

**Dave Jones:** inverter up there and the same 100 Hz signal here, but we invert the phase Ah. Let's take a look at the resultant waveform. So, if we draw two separate waveforms of the waveform on the segment pin here in blue and the waveform on the

**Dave Jones:** common pin here relative to our circuit ground 0 V here. This is important. You'll see that they're out of phase because one's the inverse of the other, but they're still 0 to 5 V TTL CMOS type levels. There's no negative thing

**Dave Jones:** involved. But, if you look at it from the perspective of the LCD here, if you actually take the difference between these two out of phase signals relative to not circuit ground anymore cuz circuit ground doesn't matter. Remember, the LCD only cares about the difference

**Dave Jones:** between the common pin and the segment pin. So, if you take the common pin as a reference, bingo, it's actually going positive and negative according to the LCD. As far as it sees it, it's flipping polarity relative to the common pin. So,

**Dave Jones:** the average value as far as the LCD's concerned is zero relative to the common. There is zero DC offset. So, you're uh aren't violating the issue with driving your LCD by having a DC offset on the common pin and we're driving this effectively

**Dave Jones:** with a single 5 V 3.3 V TTL CMOS digital uh source. Winner, winner, chicken dinner. But I hear you saying, "Dave, how do we actually drive this with a real microcontroller or a digital logic or whatnot?" Well, yeah, you just hardwire

**Dave Jones:** this in. Well, we don't have to hardwire these things in. Of course, you could. And if you just If you didn't want your display to change, you've always wanted to display the one thing, you could actually hardwire it like that. Let's

**Dave Jones:** get rid of our inverter here like this. And if you remember our digital logic fundamentals, which I'll have to link in at the end of this and down below, how can we actually What sort of gate can we use to control this

**Dave Jones:** sort of thing? Aha! That gives us a controlled inversion, your good old XOR, exclusive OR gate. So, this is your segment in and this hooks up to here like this. So, if you feed a logic zero here, zero volts into your

**Dave Jones:** XOR gate like this, it's going to work just like a buffer here. It's not going to invert this at all. So, your signal here is going to equal your signal here like this. So, the segment will be off

**Dave Jones:** because there's no difference between the segment and the comp pins. They're not out of phase They're We're not driving them out of phase, we're driving them in phase. They're effectively like shorting that pin to that pin. It's exactly the same. But, if you put a

**Dave Jones:** logic one here, bingo! The XOR becomes an inverter and it creates your out-of-phase signal. Tada! We've got now got logic control of driving the comp pin like this from a single logic rail circuit. Be it a microcontroller, 74 series, 4000 series

**Dave Jones:** logic, and Arduino or micro, whatever it is, you can drive it with a single logic just by doing out of phase waveforms. Awesome. And of course, you would do that for as many segments as you have in there. You just need those controlled

**Dave Jones:** XOR gates in there. Or if you're driving this from a microcontroller, for example, an intelligent logic device, you would just hook these straight up to the pins and then you can generate the required in phase and out of phase

**Dave Jones:** signals directly on your microcontroller pins. You just have to be careful. If you had a lot of segments here and they were hooked up to different ports on your microcontroller, for example, there might be a small delay time if you

**Dave Jones:** change one port and then change the other. But micros are so fast relative to the the quite low, you know, 100 hertz update rate that it really is not going to affect the DC offset thing at all, really. So, it's just of academic

**Dave Jones:** interest. So, there you have it. It's that easy. Just drive them out of phase. I know this might be a bit like it might sound a bit hard. Let's go to the bench. Demonstrate the thing. All right. Let's give this a

**Dave Jones:** burl. I've got a 74HC86 classic exclusive OR gate here and you can follow the wiring plan along at home if you want. But what I've got here is this powered from 5 volts and the gate on pins 1, 2, and 3 here is just a

**Dave Jones:** driver for the common pin. I've got the second pin there just strapped over to ground there. So, it's just acting as a buffer and I'm also feeding that same 100 hertz signal on pin number one there over to the second exclusive OR gate on

**Dave Jones:** pins 4, 5, and 6 there. And the output of that actually driving a segment on the LCD. And I've got it powered up. We've got 5 volts. We're feeding in our 100 hertz square wave. There it is and

**Dave Jones:** you'll see that the signal on both pins there are in phase. So, the top one is the uh common one, the yellow, and the green one down there is the segment. And check out the weird effect when I put my

**Dave Jones:** hand I'm just capacitively coupling my hand. We're just picking up all sorts of common mode noise and crap. Anyway, if you hook it up to a one there, it inverts the phase, segment turns on. You connect it to ground,

**Dave Jones:** there's no inversion in the phase. It's the same signal. The pins are effectively tied together. Segment turns off. That's it. That's how you properly drive a static LCD with a TTL signal. The difference signal that we actually saw on the uh whiteboard there, we can

**Dave Jones:** actually subtract channel one from channel two. We've got the operator as negative, so we're getting the difference between one and two here, and we're at a 5-V uh per division scale. There is no segment turned on because the waveforms are in phase, so there's

**Dave Jones:** no difference. Signal is 0-V difference, 0-V offset or difference between those the segment and the common. But, if we strap that pin over to positive there, bingo. The zero signal, the ground, effectively as far as the LCD's concerned, is smack in the

**Dave Jones:** middle there. And it actually goes up by 5 V and down by 5 V. So, it's actually 10 V total. So, you actually get a greater voltage to drive it. So, if you've got an LCD that needs a you know

**Dave Jones:** a higher voltage than uh other ones to drive signal, this is a neat way to get both of that 10 V peak-to-peak from a 5-V logic level. So, if you used a 3.3-V uh logic circuit, you would actually get

**Dave Jones:** a 6.6-V peak-to-peak signal, which will drive practically any LCD at a very large uh contrast. No worries whatsoever. And if you're wondering how to do this with a microcontroller, or in this case an Arduino, um I've got a Arduino Uno

**Dave Jones:** tied onto the back of this thing. We're counting from zero to 10. That's it. And you'll notice that there's no driving circuitry whatsoever. We've just hooked the LCD directly onto the pins of the micro here. So, the common goes to a pin.

**Dave Jones:** They're all on the same port, which means you can just switch them all at once. It's easy. And but you don't have to do that. And you can do this with as many pins as you want wanted with a

**Dave Jones:** static LCD. Um, and that's all there is to it. And we just drive the pins in phase or out of phase like we did before. And for those playing along at home, here's the firmware. David wrote it while I edited the video. I was going

**Dave Jones:** to do it, but I just got him to hack it together in a couple of minutes and there it is. And there's the bitwise uh, exclusive or operator. There it is. By port val, it basically just inverts it or not. It's controlled inversion for

**Dave Jones:** each particular segment. That's all. That's all there is to it. Easy peasy lemon squeezy. So, there you go. Don't be afraid to either design your own LCD as we're going to see in future videos in this series or use an off-the-shelf one

**Dave Jones:** and drive it with your either digital logic microcontroller or whatever. They're pretty easy to do. At least the static drive version. The multiplex one will have to require a separate video. Once you go to multiplex, it you can do it with a

**Dave Jones:** microcontroller and discrete logic, but it just gets a bit harder cuz you have different bias levels and things like that. And in that case, for multiplex ones, I'd recommend going to a proper LCD driver chip or a microcontroller

**Dave Jones:** that has a proper LCD driver built in. So, anyway, if you like that video, please give it a big thumbs up. And as always, discuss down below and there's end card video thingies at the end where you can watch more videos or highly

**Dave Jones:** recommend you do. So, yeah, stay stick around. There will be future episodes in this series where we design a custom LCD. Anyway, I hope you liked it. Catch you next time.
