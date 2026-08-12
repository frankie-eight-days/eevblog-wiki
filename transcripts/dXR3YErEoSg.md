---
video_id: dXR3YErEoSg
title: EEVblog #9 - Maxim/Dallas ThermoChron iButton
url: https://www.youtube.com/watch?v=dXR3YErEoSg
source: youtube-asr
timestamps: {"0": 0, "1": 16, "2": 36, "3": 48, "4": 66, "5": 81, "6": 97, "7": 121, "8": 132, "9": 149, "10": 166, "11": 176, "12": 189, "13": 200, "14": 224, "15": 237, "16": 251, "17": 260, "18": 278, "19": 290, "20": 304, "21": 322, "22": 337, "23": 361, "24": 372, "25": 382, "26": 397, "27": 409, "28": 419, "29": 439, "30": 463, "31": 471, "32": 484, "33": 499, "34": 510, "35": 521, "36": 538, "37": 551, "38": 569, "39": 582, "40": 592}
---

**Dave Jones:** Welcome to the AAV blog. I'm your host, Dave Jones, and this is episode number nine. First up, some industry news. Uh Texas Instruments actually just bought Luminary Micro for an undisclosed sum.

**Dave Jones:** Now, if you haven't heard of Luminary Micro, uh they make they're they're fairly new. Um they were sort of a startup from some venture capital, and um they uh do a range of 32-bit microcontrollers uh based on the ARM Cortex-M3 architecture.

**Dave Jones:** And Luminary Micro have uh been receiving secret funding from uh the ARM mob um among quite a few other players as well. And um yeah, they've been finally bought out by TI.

**Dave Jones:** And it seems like a neat fit. Really, because uh TI have um a bit of a gap in their MCU market. They do do uh ARM micros. TI do do ARM, but uh they're mainly for the automotive market.

**Dave Jones:** So, they don't have that general-purpose industrial um ARM line of micros. And of course, ARM are all the rage at the moment. And um and ARM is set to become um you know, the number one player in uh embedded industrial micros.

**Dave Jones:** And TI want a part of that. So, well, I think it was a pretty smart move buying Luminary Micro. It's a nice fit. Industry has predicted that uh the MCU market will be worth uh in the order of like $12 billion in the next year or two.

**Dave Jones:** And that's a that's a huge slice of pie. And um really, TI um have a very now have a very broad offering um in the uh embedded low-power embedded industrial micros all the way from their um famous MSP430 line, the ultra-low-power devices, uh right up to now these 32-bit arms and of course their original DSP lines and things like that.

**Dave Jones:** So, um they're a really huge player now, one of the majors. Now, I'm going to tell you about uh some really cool or a really cool range of devices.

**Dave Jones:** And they're the these little things. They're the uh they're called the Thermochron iButton and they're from Dallas/Maxim. Uh Maxim actually bought out Dallas quite a few years ago, but I still call them Dallas um cuz I really liked the gear from Dallas.

**Dave Jones:** I don't necessarily like Maxim as much, so Dallas it is. Anyway, the Thermochron iButton, these things are really cool. I use them a lot. They're a little um it's called an F5 uh microcan or something like that.

**Dave Jones:** That's the actual package. And it's little more than a couple of 10-cent pieces stacked. And inside here is a 10-year lithium battery. It goes for about 10 years. It's sealed.

**Dave Jones:** And um it has a a uh temperature thermometer um hooked onto the case. So, the case is actually the um the actual sensor pad. And it is um a complete data logger.

**Dave Jones:** You can set these things and forget them and you can log um temperature from once per minute up to once per year. And they've got 2K of sample memory in there.

**Dave Jones:** There's other devices with more, uh but these are This is the 2K version. This is the DS uh 1921 uh device, which is their standard thing. And it's a it's a temperature logger that um goes from, you know, minus 40 up to plus 85, um sort of, you know, the in industrial type temperature range.

**Dave Jones:** And I use them for all sorts of things. Now, I really think these things are the duck's guts. They really are. They're superb. Because they're only about, you know, $20 each or something, and you can use them for a whole range of things.

**Dave Jones:** Um, one of the more bizarre uses I use them for, because they're completely waterproof, uh, waterproof, shockproof. I actually, um, this plastic thing is actually a holder. Um, it does actually, uh, it just holds the device.

**Dave Jones:** So, there's the actual package itself. Um, and it just, uh, slips into one of these holders here. And, um, you can get all sorts of different holders for them, I think.

**Dave Jones:** But, this is the carabiner attachment one. So, what I do is I hook it onto a carabiner, and when I'm going out canyoning, um, which is one of my, uh, pastimes in, uh, summertime here in, um, Sydney, Australia, I go out canyoning, which is absolutely waterfalls and, uh, going through the spectacular slot canyons.

**Dave Jones:** And I actually clip this thing via a carabiner either onto my harness, my actual climbing harness, or, um, even onto my shoe. I attach it to my shoelaces. And it measures the water temperature.

**Dave Jones:** It logs the water temperature once per minute throughout the entire day, and the air temperature as well. And it's it's really handy. I come home, I upload the data into an Excel spreadsheet, and I can look at, uh, the temperature for my entire trip.

**Dave Jones:** It's great. But, they also have some excellent, um, engineering uses. Now, I've used them for all sorts of things. I've actually, uh, taped them onto, um, surface mount power devices, and I've logged, uh, the temperature of power devices straight on PCBs.

**Dave Jones:** Now, another thing I've used them for is I've used multiple devices, and you can put them throughout, say, a rack cabinet if you're designing, you know, if you've got a big bit of gear you're designing, and it's in a rack, you can put these all throughout the rack in different places.

**Dave Jones:** You can hang them via a string or tape them on the side, or you can put them inside equipment and that's, uh, fan cooled, and you can actually get a 3D thermal profile of your of your device of your rack or your system and you can actually see how effective fans are and all sorts of things and they're really great for that sort of purpose.

**Dave Jones:** This is one of the serial upload cables for them. This is an old one that plugs into the serial port and it's called a blue dot receptor but they've got ones that plug into USB these days.

**Dave Jones:** I've had this one for a long time and the device just snaps in there and bingo you can upload it using the free software they've got on the website.

**Dave Jones:** It's actually a Java application these days but there's older versions with an you know an XE and you can actually upload the data. It's very easy single button you upload it and you can export it straight into Excel and plot graphs.

**Dave Jones:** Fantastic. The Thermochron iButton. I highly recommend you check them out and you have some of these sitting around in your desk drawer for when you need them. They're great.

**Dave Jones:** Now I've got another product I'm not actually going to do a full review of it but I'm going to mention it and it's the Microchip PICkit 2 in-circuit serial programmer.

**Dave Jones:** Here it is. It's great. It costs about $35. It's you know they're practically giving the things away and it really is one of the hidden gems of you know actually using Microchip PIC parts is is this thing.

**Dave Jones:** It's such an easy-to-use tool. It's so cheap and it does it does heaps of stuff. Not only does it do in-circuit serial programming but it does in-circuit debugging full in-circuit debugging on most parts anyway um but it also has a built-in power supply and um you can use it to actually power your board.

**Dave Jones:** I think it's up to several hundred milliamps or something like that. You can actually uh power your board. It's powered straight from the USB. It doesn't need a separate supply.

**Dave Jones:** And you basically any product you design, you put the um microchip in-circuit serial header straight on your board, and then you just plug this thing straight in. There's some other really cool things it does, too.

**Dave Jones:** You can actually use it as a four-channel logic analyzer. There's software that comes with it. And I think you might be able to sample up to a megahertz or something like that, but it it can be used as a fairly rudimentary four-channel logic analyzer, which is pretty handy.

**Dave Jones:** And the other neat feature is this uh push button here. You can actually uh this is for field upgrading. So, you can actually um program your firmware into this device.

**Dave Jones:** It's got its own building flash. And you can go out and go out to the field, plug it into your hardware, push the button, and bingo, it'll automatically program your PIC in the field.

**Dave Jones:** This is fantastic. And uh I don't know too many other manufacturers of micros who who have uh such a cheap and simple and easy to use and um uh really handy and versatile programmer like this one.

**Dave Jones:** And it's a real gem, and it makes working with PIC microcontrollers a real joy. And it's better than the um I've I actually went and sold my um ICD 2 in-circuit programmer cuz this thing for $35.

**Dave Jones:** And and it does almost everything. It supports all their devices from their tiny eight-pin PICs right up to the uh 32-pin uh the PIC32 micros. It's great. This is one huge reason to choose PIC over anyone else.

**Dave Jones:** Now, they've just released the PICkit 3. Um it just came out the other month, and um there's a lot of talk about I haven't tried it myself, um, but I've heard that it's not quite as good as the pickit 2.

**Dave Jones:** It's got some advantages but some disadvantages as well. So, it's not a complete upgrade, but, uh, the pickit 2 you can buy them from anywhere. They're available off the shelf.

**Dave Jones:** 35 bucks. I highly recommend you pick one up.
