---
video_id: NvIv-0-R6qQ
title: Guest Video: TannerTech Designing a Frequency Counter
url: https://www.youtube.com/watch?v=NvIv-0-R6qQ
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 15, "2": 33, "3": 53, "4": 65, "5": 83, "6": 99, "7": 123, "8": 148, "9": 168, "10": 189, "11": 210, "12": 227, "13": 245, "14": 262, "15": 279, "16": 296, "17": 316, "18": 333, "19": 347, "20": 366, "21": 382, "22": 395, "23": 412, "24": 433, "25": 462, "26": 474, "27": 492, "28": 508, "29": 527, "30": 545, "31": 566, "32": 583, "33": 602, "34": 621, "35": 641, "36": 655, "37": 671, "38": 690, "39": 706, "40": 725, "41": 744, "42": 762, "43": 784, "44": 799, "45": 815, "46": 829, "47": 847, "48": 861, "49": 879, "50": 893, "51": 910, "52": 930, "53": 950, "54": 972, "55": 990, "56": 1008, "57": 1027, "58": 1050, "59": 1068, "60": 1088, "61": 1105, "62": 1121, "63": 1133, "64": 1153, "65": 1172, "66": 1192, "67": 1210, "68": 1228}
---

**Dave Jones:** Hello, my name is Tanner and I am in charge of the Tanner Tech YouTube channel. On my channel, I make all kinds of videos covering a wide variety of different topics. I'm currently making a video right now about how to make this custom PCB

**Dave Jones:** and this PCB will actually be driving my MIDI Christmas lights this year. I've also made videos about how to make induction heaters, vacuum tube amplifiers and one of my personal favorites, the stepper motor keytar. Now, you may be wondering why I am here on EEVblog today.

**Dave Jones:** That is because Dave Jones graciously invited Smaller Electronics Channels to be on his channel while he is gone. So, I thank him very much. Enjoy my video. Frequency counters are really cool. Now, in order to understand what a frequency counter can do, we need to understand what frequency is in Hertz.

**Dave Jones:** So, imagine you had a light and it blinked on for half a second and then it blinked off for half a second and it kept repeating. So, the total time it was on combined with the total time it was off is one second.

**Dave Jones:** And so, since it had one cycle in one second, that means it was blinking at a frequency of one Hertz. Now, this is just a very, very low frequency. Some things go up to extremely high frequencies. For example, the video transmitter in my FPV drone goes up to 5.8 GHz.

**Dave Jones:** Now, that's a very high frequency. Now, a lot of frequency counters, such as this signal generator and frequency counter, are pretty expensive. For example, this one was like $58. Now, in this video, we're going to be trying to build our own frequency counter

**Dave Jones:** that's relatively simple. It's a very rudimentary frequency counter. And to build it, we're going to be using these CD4026 decade counter chips. And I'll explain how these work in just a second. But this frequency counter, well, it'll be pretty cool. It won't be very accurate and it won't be really nice to look at, but it'll work.

**Dave Jones:** So, let's get started. So, this is the CD4026B microchip and it's a typical 16-pin chip. And it's compatible with these common cathode 7-segment display chips right here. So, these are the two chips we're basically going to be using inside this video. Alright, so pretty much what this chip has is it has a bunch of different connections

**Dave Jones:** to connect to the different pins of the 7-segment display. So, you see we have pins A, B, C, D, E, F, G. Now, all those pins connect to the corresponding A, B, C, D, E, F, G pins on the 7-segment display chip. Of course, you've got 0 volts or ground and VCC.

**Dave Jones:** VCC for the CD4026 can be anywhere between 5 and 15 volts. So, it'll probably work at 12 volts for this project. Now, the CD4026 has some interesting pins. Clock is one of the most important pins on this chip. So, pretty much what happens is whenever you give a pulse to clock,

**Dave Jones:** just a singular pulse, it will increment the display by one digit. So, for example, when this starts, it'll have a digit of 0, which means these four segments or six segments will all be lit up. Now, as soon as you give it one pulse, then it's going to increment to the next digit

**Dave Jones:** on the 7-segment display, which will be a 1, and so on until you reach 9, after which it'll reset back to 0. So, that's pretty much what the clock does. Now, the disable clock pin pretty much disables the clock. Whenever you have a high signal to disable clock,

**Dave Jones:** it'll pretty much disable whatever you're doing here on clock, and it'll freeze the display. Now, disable clock, those will all be together in parallel again with all the three other CD4026 chips. Display enable, you really want to bring that high all the time

**Dave Jones:** because this will allow all these digits to be turned on. Enable out is pretty much this pin, but it could go out to the other chips, and so you can daisy chain that enable out to enable in on all the other chips. That'll be helpful.

**Dave Jones:** Now, decade out, that's another important pin. Decade out will give one pulse every time this goes back to 0. It'll pulse once, it'll go from 0 to 1, it'll keep pulsing on, and then as soon as this pulse hits 0, after it hits its 10th pulse,

**Dave Jones:** then this decade out will give one pulse, and this allows you to have multiple displays daisy chained together in multiple CD4026 chips. That way you can display larger numbers that go beyond one digit. Let's say, for example, you had a few of these chips right here.

**Dave Jones:** This chip right here would be tied to the first CD4026 chip, and it would start counting from 0 to 9. As soon as this hits 9, and then it goes back to 0, this one will go to 1, which will make 10. This one will keep going from 0 to 9 again,

**Dave Jones:** so that will be 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, and then it'll reset back to 0, and it'll give another count up to this one, which will bring the total display up to 20. Now you can put as many of these as you want together

**Dave Jones:** to get as high of a number as you want. You just need to daisy chain more CD4026 chips. So in this video, we're probably going to have three of these daisy chained together, so that way we can get a number up to 999.

**Dave Jones:** And that just means we'll have to have three separate CD4026 chips all together. Now when you're looking at all these numbers, you may be thinking that the first CD4026 chip with the clock in needs to be this one, but it's actually not. The first clock in CD4026 chip

**Dave Jones:** needs to be the farthest one to the right. This is because the decade out will need to go to the next chip to the left This one goes every 10 times. So now we get to a really important pin, and that is the reset pin.

**Dave Jones:** Now the reason the reset pin is so important is because as soon as you pulse the reset pin, it'll set whatever number is on your chip back to 0. Alright, so now that we have most of the basics regarding the CD4026 chip out of the way,

**Dave Jones:** let's take a look at the 7-segment display chip. Now this is relatively straightforward. In a 7-segment LED display chip, you just have a lot of LEDs. You have 1, 2, 3, 4, 5, 6, 7, 8 LEDs inside there, and each one can be turned on by a different pin,

**Dave Jones:** and they all have the same common cathode. Alright, so let's build a simple circuit on a breadboard that consists of these three 7-segment display LCD chips and three of these decade counters together. This may take a little bit, but once it's done, we should be able to put a clock signal on here

**Dave Jones:** and see that this thing counts all the way up and then goes back to 0 once it hits 999. Alright, so as you can see right now, I have this thing working pretty good. I have all the decade counters wired up in this huge rat nest of wire,

**Dave Jones:** and as you can see, it's counting up right now. I have this whole setup hooked up to my frequency generator, and as you can see, it's putting out a square wave right now of 110 hertz. Now if we look at the square wave,

**Dave Jones:** you can see that it's running at a duty cycle of 20%, which means it's on 20% of the time and off the other 80% of the time. So if we look at the frequency, we can actually mess around with this and we can change the speed at which the numbers count up.

**Dave Jones:** So right now it's set up so it's incrementing 10 times per second, and that's true because you can see that this one counts about 1 every second. Now if I increase the frequency to 100 hertz, you can see that this one is now

**Dave Jones:** the number increasing every 1 second. Now if I move it all the way down to 1 hertz, then you can see that this number increases every second. So as you can see, this really works very well at counting how many pulses of the square wave

**Dave Jones:** come every second. Now we can actually play with the reset button. So this wire right here goes to reset, and so any time I can reset it back to 0. And now we can also play with another pin called the clock pin right here.

**Dave Jones:** And so at any time when it's running, let's put it up to a very high frequency of let's say 60 hertz. We can actually stop this at any time and see exactly how much time has passed since it was last frozen. Alright, so now that we have this

**Dave Jones:** decade counter timer circuit all built, let's scoot it aside and go in some theory about how we can actually make a frequency counter. And so let's draw a block diagram right here. So we have the decade counter circuit, and that is just represented by this box.

**Dave Jones:** And that goes to our three displays right here. Now we also have an input signal that is a clock signal, and it will increment this counter by 1 every time a clock signal is sent to it. Now in addition to this clock pin,

**Dave Jones:** we also have a reset pin, which will reset all of these counters back to 0 whenever one pulse is applied to the reset pin. Then we have one more pin right here, and this pin is going to be the freeze pin. This is clock disable.

**Dave Jones:** And what happens is if a pulse is sent on here or this pin is brought high, then it will freeze whatever number is on this screen right now. And so with all these three inputs, we can have a very reliable frequency counter. And so let's take a look at how this would work.

**Dave Jones:** So let's say that we have a 10 Hz signal in on the clock pin. That means that this pin is going to increment once every 10 seconds, and then this one will increment once every 1 second. Now we want to freeze this every second

**Dave Jones:** to get our frequency in Hz. So what we would have to do is we would have to have a clock disable pin, so that way we can read the frequency at that moment. The clock disable pin would need to run maybe one second, maybe a half a second.

**Dave Jones:** And then immediately following this clock disable pin, we'd have to have a quick burst of the reset pin. Now between this reset time and the next clock disable time, we'd have to have that at a frequency of 1 Hz if we want to display the number on the screen in Hz.

**Dave Jones:** So in this case, this is what the waveforms would look like for the clock, the reset, and the clock disable pins. So of course we'd have the clock, and the clock would just be the input frequency from whatever we're getting it from. Now on a separate timeline,

**Dave Jones:** we can look at the reset and clock disable pins. So we'd start with a clock disable pulse on this line, and the clock disable pulse would last about 0.5 seconds, and then it would just go on. And then we'd have the reset pulse.

**Dave Jones:** Now the reset pulse would immediately follow the clock pulse right here. After this reset pulse, there's going to be a length of time between our next pair of reset and clock pulses, the first one being the clock disable pulse. This length of time right here

**Dave Jones:** in between the reset pulse and the next clock disable pulse is going to be the multiplier that we will multiply by the frequency right here to get what the actual frequency is on the clock pin. So for example, if we have, let's say, a frequency...

**Dave Jones:** Let's say we have a time right here of 1 second between each clock disable and reset pulse, and that 1 second time period will give us approximately a 1 hertz thing on here. And so that means that this number that is going to be read out on the 7-segment display

**Dave Jones:** would be the number of hertz that is being put in on the clock pin. Now if we shorten this time right here to, let's say, 0.1 seconds, then we'd have to add an extra 0 right here in order to get the right pulse.

**Dave Jones:** We'd have to multiply our signal on the 7-segment display by 10 to get the right number right here. And then let's say we divided that by a smaller number. We divide this again by 10. We'd have to add another 0 right here to get the right frequency.

**Dave Jones:** And by doing this, we could get almost any frequency on this frequency counter, but it wouldn't be accurate because we'd be adding more 0s. So we'd have to add more 7-segment displays. So this is most accurate up to 1 kilohertz, but if we added more displays,

**Dave Jones:** we could get it more accurate. And so these waveforms are the waveforms that we will need right now in order to adequately read our frequency counter. This is the basics of making this frequency counter work. Now, if we want to make this look a little bit better,

**Dave Jones:** we can turn off the display during the time when it's going to be counting because the time in between here and here, the display is going to be counting up really fast, and you might not want to see that. And so what we can do is we can add another pulse

**Dave Jones:** that starts as soon as this pulse ends, and it will end as soon as this pulse starts again. It'll be this specific time in between, whatever time period we were talking about before. And pretty much this will be another pin, which is the display enable pin.

**Dave Jones:** All right, so I didn't talk about this when I was first drawing the block diagram. The display enable pin pretty much turns on and off the display. And so if it's high, then the numbers will be on, and if it's low, the numbers will be off.

**Dave Jones:** So in that case, I will actually need to invert this frequency right here, so that way it starts high, and during this time, it goes low, shutting off the display for that annoying counting sequence before turning it on again to actually read the numbers.

**Dave Jones:** So we have these three different waveforms, and we're going to generate to put into the CD4026 chip in order to get a really good frequency reading. Now, if I had multiple different 555 timers or a signal generator, then I could easily generate these three waveforms.

**Dave Jones:** But my frequency generator only has two channels, and so that makes it a little bit difficult. And also, I really don't want to go through the pain of getting out a bunch of 555 timers and wiring up a bunch of different oscillators. So in this case, we're just going to try and generate

**Dave Jones:** these waveforms on an Arduino Nano. All right, so I've made an Arduino code, and its main purpose is to generate those three different waveforms on three different pins of the Arduino. Those pins are pins 12, 11, and 10, respectively. I've uploaded this to an Arduino Nano.

**Dave Jones:** Let's test it out. Okay, so I am stoked right now because this thing works perfectly. So first off, let me bring you down all the way to zero. So right now, this thing is operating at zero hertz. Now let's turn it up to 10 hertz.

**Dave Jones:** As you can see, we're registering a one on the display screen. And if we add another zero right here after the one, or we multiply this display by 10, we get 10 hertz. Now if I move this up to 100 hertz, you can see that we have 10 on here.

**Dave Jones:** And so if we multiply that by 10, then we get 100 hertz. Now let's move this out and bring it up a lot higher to 1,500 hertz, or 1.5 kilohertz. As you can see, the screen reads it perfectly at 15. If I crank this up a little more,

**Dave Jones:** all the way to, let's say, 50, 5 kilohertz, we're registering 499, and that is pretty close. So let's see what happens if we crank this all the way up to almost its max value, which is 10 kilohertz. As you can see, it's perfect.

**Dave Jones:** It doesn't reset back to zero accidentally. It goes up to 999. And if I crank it up all the way, it kind of messes up because it's not meant to go that high. But up until 10 kilohertz, it functions almost exactly as planned.

**Dave Jones:** Now if I did this same thing, and I added more decade counters, I could get a very, very accurate frequency counter. So now to recap. So inside the CD4026 chip, we have a bunch of different pins, including the clock pin, which is directly inputted from the signal generator.

**Dave Jones:** Now every time the clock pin is high, then it increments this display by 1. And we have a series of pulses being fed by the Arduino into the clock disable, reset, and display enable pins. When the clock disable is high, that disables the clock and freezes the display

**Dave Jones:** at whatever was last set on there. The display enable is high, which means it makes it come on. And we also have this little part right here when it resets it. And that is just a quick reset pulse. And the display is still high.

**Dave Jones:** And then it brings the display low for just a little bit of time when it lets it count up to whatever frequency is on there. After it brings it up to the right frequency, then it freezes the display at whatever frequency is on there.

**Dave Jones:** So right now, you can see that the frequency is 539, which means it's 5.39 kilohertz. That is really accurate to my function generator, which is at 539 kilohertz too. All right, so for the future, I may actually make this display a lot better.

**Dave Jones:** I may use Nixie tubes. I may even just replace this Arduino with a completely analog signal generation source where I can just control the control voltage pin of the 555 timer so we can trigger each pulse at the right time. Now also, this only works with square waves for the time being.

**Dave Jones:** But in the future, I could actually make this work with sine waves. All right, so in a sine wave, whenever it goes high, we can use a comparator. And that comparator will read whenever it goes high for each time. And every time it goes high, it'll just give one pulse like this.

**Dave Jones:** Now that will give us an adequate reading if we use a sine wave. So in the future, I'll make this frequency counter a lot more accurate and more usable for other applications by replacing the Arduino with some analog circuitry. I will also use some comparators

**Dave Jones:** to make this thing able to read sine waves. And I'll add a lot more digits to make it more accurate. But there you go. That's all. It's pretty cool. So that's it. Thanks for watching. I hope you guys learned something really cool about how to utilize a CD4026 chip

**Dave Jones:** and how you can actually use it to make a quite accurate frequency counter. As always, thanks for watching and stay tuned for next time.
