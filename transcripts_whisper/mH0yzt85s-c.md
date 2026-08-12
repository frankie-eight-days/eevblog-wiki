---
video_id: mH0yzt85s-c
title: EEVblog 1624 - Electronex: Liquid Instruments Moku Oscilloscope
url: https://www.youtube.com/watch?v=mH0yzt85s-c
source: whisper-large-v3-q5_0
timestamps: {"0": 0, "1": 19, "2": 34, "3": 54, "4": 78, "5": 96, "6": 111, "7": 127, "8": 147, "9": 161, "10": 184, "11": 201, "12": 225, "13": 245, "14": 261, "15": 261, "16": 273, "17": 288, "18": 310, "19": 327, "20": 345, "21": 365, "22": 383, "23": 402, "24": 416, "25": 436, "26": 456, "27": 473, "28": 491, "29": 508, "30": 525, "31": 537, "32": 557, "33": 567, "34": 586, "35": 605, "36": 616, "37": 634, "38": 649, "39": 662, "40": 686, "41": 701, "42": 722, "43": 740, "44": 756, "45": 767, "46": 777}
---

**Dave Jones:** Hi, I'm here at Liquid Instruments, Australian company, and here's Ben Price to tell us all about this cool looking design, Australian design and made oscilloscope and everything else. How many functions? So we currently have 14 different instruments. Only 14? Only 14. Are there plans for more?

**Dave Jones:** There are plans for more to come soon. Tell us which ones you've got. So currently our main ones are like this. You've got your oscilloscope, you've got your spectrum analyser, you've got your waveform generator, you've got your frequency response analyser. All your basics, yep.

**Dave Jones:** Yeah, and then you've got like PID controllers and also like laser locking boxes and lock-in amplifiers for your photonics measurements. Wow, they're usually very expensive. Yes. Yes. And they come also with our $1,000 Australian dollar units built in. Which hopefully... Hopefully you guys might send me for a tear down, I think.

**Dave Jones:** Yes, it would be interesting. Yes. We also provide a system called multi-instrument mode, which allows you to basically stack. I'll show you how we set it up. Basically allows you to stack instruments on top of each other. So you could have a waveform generator that goes into a frequency response analyser that say I want to see its spectrum and then I want to modulate it using a PID controller.

**Dave Jones:** You can then hit go. All internally, it will connect all of its internal signals to its inputs. It's outputs. You can then link buses to each other. You can... So that's doing that via analogue switching within the unit. Internally. Right. No need to set up cables, Ethernet cables, redundancies, everything operates internally.

**Dave Jones:** Wow. And you can just switch instruments to whatever instrument you want. So say I now want that to be a lock-in and I want that to be an arbitrary. Bang, launches, don't have to change any modules, works instantly. And how many and how much of that functionality is inside the little baby here?

**Dave Jones:** So the little Moku also has the functionality, but it only comes with two channels because it's only two input, two output. So you can stack two channels on top of each other. That's the same with the lab. But the probe being a four channel in, four channel out allows you to have four channel, four instrumentation stands on top of each other.

**Dave Jones:** And what type of price range we're talking for the high end pro? So for the high end pro here, it starts at 15,000 US dollars. Yep. That comes with your standard five instruments. And then you can basically... Add on each instrument you need from ranging from about thousand to $2,000 an instrument, depending on what it is.

**Dave Jones:** Or if you want to go full all out, you can spend 25,000 US dollars and get every single instrument. And when we release new instruments every six to 12 months, depending on how complicated the instrument is to make, you'll automatically get it uploaded onto your device.

**Dave Jones:** Right. And what markets are you selling into? So we were designed for photonics stuff originally. So these photonics labs are using these instruments to do high. Accuracy, photonics measurements for photons and things like that. We also have companies that are doing high volume electrical test and development programs.

**Dave Jones:** So needing to automate test processes through needing to have an oscilloscope, then a spectrum analyzer, then a waveform generator. You're basically able to write that in our API. It automatically switches between each instrument. You can leave every single cable the same, and it will work itself all out using Python, MATLAB.

**Dave Jones:** Lab view, C, whatever your preferred language is. I noticed you got a digital logic analyzer here. So how does that work? Because you've got no digital inputs. Are they on the back? We've got the Moki Go, which is our entry level one, which also comes with a digital signal in which you can link to your pro or your lab and basically allows you to have digital triggering or digital output signals.

**Dave Jones:** You can do that over Ethernet into each other. You could do that by using an iPad for this device. A computer for this device, both on the same device, you can stack devices on top of each other so you can have one device connected to one Moki and then you can go back to the other one and just switch between them all on the same device.

**Dave Jones:** And then if you wanted to use your logic analyzer, once it launches in the product it is connected to, you've got your sweep so you can basically just create signals by going in here. And then if you wanted to use your logic analyzer, once it launches in the product it is connected to, you've got your sweep so you can basically just create signals by going in here.

**Dave Jones:** And then if you wanted to use your logic analyzer, once it launches in the product it is connected to, you've got your sweep so you can basically just create signals by going in here. And then if you wanted to use your logic analyzer, once it launches in the product it is connected to, you've got your sweep so you can basically just create signals by going in here.

**Dave Jones:** And then if you wanted to use your logic analyzer, once it launches in the product it is connected to, you've got your sweep so you can basically just create signals by going in here. And then if you wanted to use your logic analyzer, once it launches in the product it is connected to, you've got your sweep so you can basically just create signals by going in here.

**Dave Jones:** bits to basically do what you need to do. That is a nice user interface. How long have you guys been working on the design of this thing? So we've existed since 2014 and we launched our first product in 2015 the Moku Lab and then about

**Dave Jones:** three to four years ago we launched the Moku Pro and then about two to three years ago we might launch the Moku Go. All for separate markets, all for separate uses, depending if you need super high frequency, super high bitrate, 5 giga samples at 600 megahertz for the Moku Pro, all the way down to 300 megahertz

**Dave Jones:** at 225 mega samples. And there's a spec so this is the lab, this is the mid-range version? Yes that is the Moku Lab yep. Okay right and what's the price point on that one? Starts at $5,000 USD and then goes up to $10,000 USD for everything added into it.

**Dave Jones:** And Australian design and manufacture, you've got your development here? Yes. And they're manufactured here? Yes. Can you tell us more about that? So our complete development team that do all the board design, all the firmware, all the mechanical design, everything's done in our office in Canberra.

**Dave Jones:** We manufacture the Moku Pro virtually completely in Melbourne and the Moku Go is assembled completely in Melbourne. So we're trying to be basically as Australian dependent as possible, trying to advocate for Australian manufacturing, Australian design, because we are one of the best countries in the world at doing this kind of stuff, so why not?

**Dave Jones:** Fantastic. So there was no price, because this is into the higher end price market. Yes. There was no pressure to manufacture in China at all? No definitely not, because we know that we can still, we still undercut a lot of people such as someone like

**Dave Jones:** National Instruments that have those module systems which you need to buy each individual module. We can do that all for one box, don't need to buy upgrades, don't need to buy things, it's all software-based, so why not buy the better system? And a lot of people are going to compare with this with the

**Dave Jones:** Analogue Discovery, maybe not in terms of that, but in terms of functionality in software. How do you reckon yours competes with the Analogue Discovery? My personal humble opinion, I reckon our user layout and use functionality is much more intuitive. Can you show us the oscilloscope for example?

**Dave Jones:** Yes, so our oscilloscope here launches simply, so this is for the Moku Go demo, so the little unit. So you've got your simple channel A, your channel B, you've got each of your coupling, your ranges, you can do your time base, simply, trigger, simply.

**Dave Jones:** We've got quite intuitive symbols, so understandable in all languages. Our device also can be in six different languages as well. You've got your measurements that you can add, so say I want to add a frequency, all the different ones you would ever want to know, it's all there nicely laid out for

**Dave Jones:** each channels. And then we've also got a built-in multimeter which just sits there. I was going to ask about multimeter functionality, because this is a 16-bit, it's a 16-bit native 16-bit analog-to-digital. Yes. Right, got it. But I think the spec says it goes up to 18-bit?

**Dave Jones:** Yes, so our MarkQ Pro can operate 10 times 18-bit, so the 10 times is for our low-speed ADC and we've got the 18-bit for our high-speed ADC. And we also have a patented system which basically allows us to blend our low-speed and high-speed ADCs together, so instead of when you're sweeping for a full

**Dave Jones:** frequency range, instead of getting a skip, we have a basically clean frequency sweep through the entire band from 6,000 megahertz all the way down to 10 Hertz without any jumping, any weird noises and stuff like that, through our like patented blending system. Nice.

**Dave Jones:** So the low end's a thousand Aussie bucks, you said? Yes. How much in Yankee bucks? 600 bucks. About 600 US. Not bad at all. So, ooh, that's hefty. Yeah. That's hefty. It's got, it's got stuff to cool down. So this is the top of the range one, so

**Dave Jones:** this one costs about 800 USD. Oh, okay. And this has also programmed... What is the difference? What is the difference between the low-end and high-end? Low-end, so the base model doesn't come with any programmable DCs. Oh, okay. And then the high-end one comes with forced individual programmable DC outputs.

**Dave Jones:** And what sort of power level we're talking? I can't remember exactly off the top of my head, I'm sorry about that. That's alright, they'd be switching converters, obviously, and... Yeah, I think we do, I think we do, I think we do up to about 10 volts at about 0.1 amps, so for simple, like...

**Dave Jones:** Okay, right, it's just for powering basic circuits. Yeah, for simple stuff, so if you want to, like, say, you want to design a little Arduino circuit, you want to measure what your capacitor is measuring, so you can power it off your unit and also measure the signals all at the same time.

**Dave Jones:** Can you feed the function gen into the power supply and ramp the power supply? Because Analog Discovery can do that, so that's one of their little neat things that they can do. I'm gonna say that's a yes, or are you trying it for the first time?

**Dave Jones:** I think, well, so we're trying to add, what do we want to do? A function gen into the power supply, so that the power supply is mod, you know, you can ramp the power supply, for example. Function generator. So, yeah, we've got waveform generator into our...

**Dave Jones:** So, will this allow you to join things if it can't do it? Like, if it knows it can't do it? So, you can... Oh, God, it's been a while since I've used this. I'm putting you on the spot. I know. Yep, totally. Pressure.

**Dave Jones:** Oh, Fur Filter Builder. Nice. Wow. Sorry, I've just, I have, it's a humble mechanical engineer. Yes, I was gonna say, you are a mech engineer, so... Yeah, so, you're probably the wrong person to ask. I can't work it out right now, but... All right.

**Dave Jones:** That's all right. If we do send it off to you, we'll send you a basically a full instruction of how different things work, and we have all the information anyone would need on our website. It steps you through how every instrument works, how every instrument can communicate with each other,

**Dave Jones:** and what limitations you could have, and what it could work for your needs, and what you want to test. So, what have you worked on in terms of the mechanical side of things? Housings and... Yeah, so, Mocha Pro was kind of my main task things.

**Dave Jones:** So, basically, all the internal, how shielding works for all the front ends, thermals, so making sure everything's stable for calibration, noise levels, so the fans, the fan vibration doesn't couple into... Ah, yes, of course, yes. Yes, it doesn't couple into your photonics measurements or stuff

**Dave Jones:** like that. How this thing is assembled itself at the manufacturing line, so we have a consistency of quality. And when you're spending this much money on a device, you want to make sure it's pristine. Nice and schmick and polished and everything. So, there's a small fan in there,

**Dave Jones:** is that loud? Yeah. So, we've got two 52 mil fans at the back here, which are coupled into a two dozen thermal sensors across the entire thing. Two dozen? Yeah. Wow, you're serious. So, on the low power and high speed, low power and high power amplifiers, each of them have a thermocouple for each channel of

**Dave Jones:** the outputs. We've got one thermocouple for each of the boards, each of the main chips, for different parts of the FPGA, for everything. So, we basically have a proprietary algorithm that communicates with all of them and works out where the fan speed measurement should be to keep

**Dave Jones:** calibration at its optimum, so you get the best results. Okay. So, you're almost trying to temperature stabilise it, almost? Yes. Well, because for calibration, it's on like a PC, you don't want it to be as cold as possible. You want it to be that temperature.

**Dave Jones:** So, it also allows us to have a lot of headroom. For example, this can operate in 45 degree ambient. So, say you want to server mount it, which you can. It's 45 degrees in there. You don't really care if it's loud in there.

**Dave Jones:** So, the fans can ramp all the way up and it can keep itself running at the correct operating temperature. Got it. Right. So, this fits in a rack, doesn't it? Yes. The standard 19-inch rack. Yes. Standard 19-inch rack. Exactly 2.5U high. It comes with server rack ears.

**Dave Jones:** So, you just bolt them. Oh, okay. There's your bolt. Okay. Yep. Things slide through. There's your threaded holes. Yep. All goes together. Very nice. All right. Thank you very much, Ben. Excellent. That's awesome. Thank you, mate. Thanks, mate. Cheers.
