---
video_id: DX_f0Cg6pHo
title: How a 4-20mA Process Control Current Loop Rotational Sensor Works
url: https://www.youtube.com/watch?v=DX_f0Cg6pHo
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 55, "3": 89, "4": 119, "5": 145, "6": 174, "7": 202, "8": 228, "9": 257, "10": 286, "11": 317, "12": 341, "13": 371, "14": 388, "15": 413, "16": 426, "17": 447, "18": 476, "19": 493, "20": 521, "21": 555, "22": 571, "23": 596, "24": 628, "25": 656, "26": 682, "27": 700}
---

**Dave Jones:** This one comes from Australia. Thank you very much Mark Vitnell from Sinusoid Proprietary Limited. I know this is and I think we're going to have Oh, that didn't Knife totally missed that. Um, I think you'll find this quite interesting.

**Dave Jones:** Boom. All right, we have Tada! Rotary encoders. But better than that, Australian made rotary encoders. And I believe we've got one working and one that's already torn down cuz they're probably not easy to tear down. So, we're going to have a look at how rotary encoders work. Awesome. Oh, look at this Bobby dazzler made in Australia by Sinusoid here in Sydney by the way at Turramurra. Fantastic. Um, this is the RPE48 for those playing along at home and it's a rotary position encoder. But this one has an absolute analog output

**Dave Jones:** of 4 to 20 milliamps. So, it's a a classic 4 to 20 milliamp process control signal as they're called. So, what this is going to give us is a 4 to 20 milliamp process current output as it's called and it can give a 12-bit resolution for the entire 360°. So, wherever the reference is for 4 milliamps, which is like say the 0° position so to speak, as you rotate that around that'll increase up to 20 milliamps and then that will wrap back to 4 milliamps. So, you can actually get

**Dave Jones:** the absolute position of this thing with our 12-bit accuracy and this will do it very quickly as well up to 7,500 rpm. So, this is a three-wire jobby. So, you got to provide it a power source, but some 4 to 20 milliamp stuff you don't have to. In fact, there's basically three different types and I'll I'll try and put up some graphics here if I can find some of the different types of 4 to 20 milliamp uh, process current output uh, devices that you can get. One is

**Dave Jones:** that you basically put it in series and it acts as a, uh, current source and then you have a load resistor on there with, well, in series with it, uh, typically 250 ohms and then that converts it to a voltage and then you can read the, in this particular case, uh, the position of, uh, your rotary encoder, but it could be any other, um, industrial control. And this is where 4 to 20 milliamp comes in. Now, the other type is what we've got here, which is a

**Dave Jones:** three-wire type, so you basically provide a, uh, in this particular case, uh, 12 V to 30 V, uh, DC and then you get an absolute current output, which, uh, then you connect, uh, down to ground. And the other type is basically an isolated, uh, type where the actual, uh, sensor part itself is isolated from the, uh, current loop, uh, section. So, um, but this particular one, let's take a look at it here and see how this works. Now, why would you have a 4 to 20 milliamp output? Why not

**Dave Jones:** have 0 to 20 or 0 to 10 milliamps? Well, this is because, uh, you can have very long cable runs. Remember, the 4 to 20 milliamp, uh, process current loop standard is its, uh, a basic name and this is where, uh, you, you might have heard of a, in fact, I've done a video, I'll have to link it in, of a process calibrator and, like, it's effectively a multimeter that's sort of like specializes in this sort of 4 to 20 milliamp, uh, you know, generation and

**Dave Jones:** also measurement, uh, as well. But there's a couple of multimeters on the market that have it. I'll show you that in a minute. So, the reason they use 4 to 20 milliamps is, uh, so that any, uh, interference on the line, you want a, basically, a high current solution so that if you get any noise coupling into your very long cables in your factory and all your machinery and stuff, whilst it's easy to induce a voltage into a cable, it's very hard to induce a current and in this particular case,

**Dave Jones:** it's very hard to induce the milliamps of current that would actually upset uh, this sort of thing. So, that's why they use 4 to 20 milliamps. If you go right down to zero, then you're going to come a gutter with like a small little induced currents in your cable down near that zero point. So, they have 4 to 20 milliamps so that the system knows when it's reading it, if it's less than 4 milliamps, let's say typically under like 3.5 milliamps or something, then you know that's an error. Or if

**Dave Jones:** it's above 20 milliamps, say 25 milliamps, then you know that's an error as well. So, 4 to 20 milliamps has become sort of like the industry standard. In fact, I don't know, is there a standard for this or is it kind of like a de facto standard? Off the top of my head, I don't know. I have to check. And another advantage of having a 4 milliamps as your absolute minimum is that then you can steal some of that current to basically power remote sensors at the end of the line, so to

**Dave Jones:** speak, because it's a constant current loop. So, if you've got a sensor like embedded in your machine or something like that, you don't want to have to run some extra lines to it. You run a current loop to it. And basically this 4 to 20 milliamps de facto industry standard, it basically means zero to 100% of in this particular case a rotation, but it could be anything, some pneumatic actuator or absolutely any other industrial process mechanical thing or electrical thing you can think of that would give you like that you want

**Dave Jones:** to know like zero to 100% or you want to control something. Not only just reading back, but you can actually control stuff as well. So, yeah, 4 to 20 milliamp current loops are very wide massively widely used in the industry. So much so that they make dedicated test equipment like those process meters, you know, Fluke make them and many other companies have done this like a real el cheapo one before that I found for next to nothing.

**Dave Jones:** It's just a huge de facto standard that lets you run a whole bunch of stuff. Anyway, up very cool. So, there's the specs for those playing along at home. It's got ball bearings in it. No worries. No plastic rubbish. You can get up to 7,500 RPM if you remove the seal, but otherwise 3,000 RPM here. So, it's got and you can get different flange sizes and sampling rate of 10.4 K samples per second at 12 bits. And well, let's give it a go. Now, I do believe

**Dave Jones:** that this Keysight U1272A is the only meter I have here in the lab, I think, that has a specific 4 to 20 milliamp mode. Now, of course, you don't need a specific multimeter with this 4 to 20 milliamp function or a process meter to actually measure one of these things.

**Dave Jones:** You can just use a standard multimeter in current mode and you going to measure 4 to 20 milliamps. But, this is just nice in that it gives you a percentage mode like this. So, you know, we're we're just basically selecting it so we can get our current like that, 7.145 milliamps. But, when you go into the process mode like this, it'll actually convert that to a percentage and it gives you the milliamp value up there.

**Dave Jones:** Oh, I just realized that LED display is really hard to read. Can you even see that on camera? Anyway, okay. So, what we got here is three wires, your 12-V supply, your red and black, and the white one is the current output.

**Dave Jones:** So, I've got the current output going into just the current jack of the multimeter here. And you can see we're supplying 12 V here and we're getting a value about and as I turn the knob, we're going to get from 0 to 100% and if I'm very, very careful, you'll see it wrap around there.

**Dave Jones:** Very touching, it'll wrap back to zero, but basically goes from 99 back to a zero. So, we're reading the rotation of this shaft here from 0 to 100% and that gives us 4 to 20 milliamps. And you can see the current actually changing for the sensor. There's going to be some internal circuitry in here which takes some residual power, but but basically we're going to get that 4 to 20 milliamps output. Cool, huh? Because this is basically a constant current, well, an adjustable constant current generator.

**Dave Jones:** Now, because this has 12-bit precision in here, my fingers, my silly human fingers just aren't good enough to I'm putting the lightest pressure on that. It's absolutely tiny, but it's going to wrap around because it's not absolutely God, calibrate it.

**Dave Jones:** Come on, you can do it. There you go. And it jumps around to zero. My clumsy human fingers here aren't good enough to get that 12-bit resolution, but if I put like a huge massive wheel on here and then I just tight, you know, just feather touched it, then you'd be able to see the 12-bit resolution available inside this rotary encoder. So, yeah, very cool. Zero to 100% and then you can guarantee that you're almost doesn't matter where you put this in your factory. It doesn't

**Dave Jones:** matter how much crap and noise there is around it. You're really not going to upset a constant current reading like that. And that's why they use these constant current loops, these process loops as they're called. And this one is the smaller shaft diameter. Now, I thought that this might be these might be difficult to take apart, but they're not. Now, it has a very nice cable interface here. Check out the cable interface they've got here. This actually screws in like that and then it's got a like a waterproof tight seal,

**Dave Jones:** dust and waterproof seal on the end of that. Looks like we can just open that with three screws and it pops off and you'll see that these are deceptively simple. Let's just open this up here and you'll see how this works.

**Dave Jones:** Almost a meter No, no, no, screws off. There you go. Look at that. Oh, Dazzler. Wow, there we go. It fell apart. And that's all that's in this thing. Well, by saying that's all, there's actually a lot of tech that goes into it, of course. But at the end of the day, it's pretty simple. All we've got is this shaft, and then it's going to have a nice ball bearing in there. It's a real Bobby Dazzler. It feels like it.

**Dave Jones:** It's pornographic, really. It's just got a permanent magnet on the end of that, and it just It just spins. And then, and yep, you guessed it. We've just got a Hall effect uh sensor um chip in the middle of that. And of course, these are um you know, amazing tech inside these uh Hall effect uh sensor chips in there. Um I can't quite make out the number on that. I'll get that, and I'll pull up the data sheet right here. And that's an Osram AS5047 um Hall effect sensor there. And it's

**Dave Jones:** actually a 14-bit jobby. So, this one at uh 12 bits, they're uh being a bit uh conservative uh there. It is The actual chip is uh capable of more than that. But uh yeah, that basically gives you an an SPI output. It's got a lot of magic built into that puppy. And what else they've got here is a Microchip uh 12-bit DAC there. I don't know what that jobby is there. But if we flip it over, got a little programming port there.

**Dave Jones:** Just inside there, you can see that on the other side. All the ST fanboys go wild. Hopefully, I can get that. Uh that's an ST Micro by the looks of it. And uh then there's This is how they're doing the uh 4 to 20 milliamp current uh conversion here. So, that's a neat little unit. Of course, all the magic happens in the Osram uh Hall effect sensor there. It's got four uh sensors in there, and lots of ADCs, and lots of other magic. And it can sample, you

**Dave Jones:** know, up to 10,000 times a second, or whatever uh it was there. And uh yeah, the micro is just uh doing all that processing and in uh real time. And then just converting it from to that 4 milliamp standard. So, that is very interesting. Thank you very much Sonia Soyd for sending that this in.

**Dave Jones:** I'll link it in down below. Aussie made company selling these really high-quality rotary encoders. Great stuff.
