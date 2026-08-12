---
video_id: RUqAaM2ncso
title: EEVblog #298 - Dave's Decade Digit Display - USB Supply Part 3
url: https://www.youtube.com/watch?v=RUqAaM2ncso
source: youtube-asr
timestamps: {"0": 2, "1": 30, "2": 54, "3": 79, "4": 107, "5": 124, "6": 135, "7": 152, "8": 162, "9": 173, "10": 189, "11": 199, "12": 216, "13": 227, "14": 245, "15": 265, "16": 276, "17": 290, "18": 302, "19": 312, "20": 340, "21": 348, "22": 373, "23": 389, "24": 405, "25": 415, "26": 432, "27": 445, "28": 469, "29": 482, "30": 494, "31": 511, "32": 524, "33": 535, "34": 550, "35": 562, "36": 589, "37": 605, "38": 619, "39": 632, "40": 654, "41": 676, "42": 699, "43": 714, "44": 725, "45": 751, "46": 762, "47": 779, "48": 792, "49": 816, "50": 834, "51": 843, "52": 871, "53": 888, "54": 906, "55": 919, "56": 928, "57": 937, "58": 946, "59": 970, "60": 986, "61": 1016, "62": 1029, "63": 1045, "64": 1058, "65": 1077, "66": 1102, "67": 1124, "68": 1142, "69": 1163, "70": 1176, "71": 1188, "72": 1202, "73": 1216, "74": 1227, "75": 1237, "76": 1251, "77": 1263, "78": 1281}
---

**Dave Jones:** Hi, it's USB lab power supply time again and I promised that I would talk about the display solution used on here because I said I wanted to go away from the LED display used on my previous prototypes and possibly use something else because you know I've been talking about this you saw in the previous video the housing display I'm going to use like a clear thing on the top possibly so I'll be

**Dave Jones:** able to see whatever display solution is through the clear Perspex or polycarbonate cover on the front so there's no need to worry about things like cutouts because when you do when you use displays like these seven segment displays or LCDs or something like that you'll notice that you have to add cutouts to you know to see the display through on a typical front panel and they're a

**Dave Jones:** pain in the ass to get those aligned it's extra cost in manufacture and things like that so with a clear you know display window on the front of this thing we can use pretty much anything we want LCD LED whatever and you'll be able to see it straight through so why am I going away from these seven segment LED displays well it's pretty obvious they draw a fair bit of current

**Dave Jones:** now you can get really efficient LCD LED displays these ones are LTC7424 they're a very nice little display and they're reasonable cost I will have a look at the cost in in a minute cuz that's what it's going to come down to really for the display choice this time around so these aren't bad displays but they're going to take at least a couple of milliamps per segment to get them at

**Dave Jones:** a you know a usable brightness in you know a typical environment you know like a lab or an office or a room or whatever. So, let alone outside. Let's say you got, you know, a good grunty 5 milliamps per segment.

**Dave Jones:** That should give you a fairly decent brightness. Well, you could have, if you're displaying an eight with a decimal point, you could have eight of those on for each one of those digits.

**Dave Jones:** So, that's 40 milliamps. That's 8 * 5 milliamps, 40 milliamps right there for one digit. And of course, you wouldn't with these sort of solutions, you multiplex them. Um so, you know, you can get a maximum ever Well, a maximum value of 40 milliamps for the entire display.

**Dave Jones:** That you know, in a normal project, it's probably not a lot. In a regular bench power supply, not a huge amount. But, this thing, we've only got 500 milliamps uh total.

**Dave Jones:** What we're ignoring power here. We're just, you know, 500 milliamps at 5 volts. But, then you got the loss of the converter, the the isolated DC to DC converter.

**Dave Jones:** And to draw 40 milliamps at say 3.3 volts, that's a fair whack of your power budget. So, really bad idea to do the LED display. But, as you might see, going to end up using LED.

**Dave Jones:** But, you'll see something a little bit different. Come to that. Now, the obvious solution everyone says use LCD. Great. Okay, I like LCD displays as much as the next person.

**Dave Jones:** But, we'll take a look at it there. And a similar cost solution, probably even a little bit more than these seven-segment LED displays. So, really I'm trying to keep cost as absolute low as possible on this project.

**Dave Jones:** So, LCD, well, it's a, you know, a nice solution. A, it's expen- It's, you know, it's not cheap um unless you go for 100 low, get them from Alibaba in China.

**Dave Jones:** And uh it's just it's really horrid. It's not something you want to do for a project like this. I want to stick to like a name brand LCD, something that, you know, is going to be available in 5 years time or something like that, not just some one-batch wonder from OneHungLow on Alibaba.

**Dave Jones:** So, the LCD solution, uh it's not bad, similar cost, but then you've got to find an LCD uh a microcontroller with an LCD driver to drive the thing. I'm going to come up with a really low-cost display solution.

**Dave Jones:** It's not nearly as good in terms of uh you know, direct reading and things like that, as you'll see, but I think it's reasonably clever if you want a really ultra-low-cost solution.

**Dave Jones:** Let's go to the web. All right, let's jump straight on to Digikey, shall we? And we'll search for our LTC70 uh 4724, which is what I've used in my previous one, and here it is.

**Dave Jones:** And uh let's scroll across and take a look at it. It's from uh Lite-On, and they're a really nice little compact display. I really like them. They're really small, but uh they're $2.92 in one-off quantity.

**Dave Jones:** Well, let's uh go in and look at the price breakdown for those. Even if I'm making a thousand of these things, buck 30 each, right? So, that's $2.60, bam, right there in your cost.

**Dave Jones:** So, remember that. Well, even if we had like one of them, for example, okay, we're still talking a dollar 30 in a thousand of quantity. Not that, you know, when you're trying to shave cents off your production cost and things like that, trying to keep this thing ultra-low cost, um that would make this, by far, the most expensive component on the entire board.

**Dave Jones:** Well, it'd be the most expensive uh apart from the DC-to-DC converter, but that's always going to be the most expensive component in a little USB power supply like this.

**Dave Jones:** And by the way, folks, for all those who are complaining or asking, "Why don't I make this thing, you know, capable of 2 amp, you know, to utilize the USB ports with 2 amps or 3 amps or whatever the latest charging standard is in USB 3.0?" It is because the DC-to-DC converters are very expensive and they don't linearly increase in cost.

**Dave Jones:** Usually, to go from, say, a 2-W converter, which is what we need for a 500-mA solution, up to, you know, a you know, a 5- or 6-W version or even higher, that we'll need for a higher power solution.

**Dave Jones:** It's just they you can double, triple, quadruple your bomb cost right on your isolated DC-to-DC converter like that. And, of course, I want this project to be isolated, so that isolated converter is an absolute essential.

**Dave Jones:** So, if you're if you complained about that and wondering why I don't use it, well, go and check the costings for these DC-to-DC converters and you'll find out for yourself.

**Dave Jones:** And if you're wondering if there are cheaper LED seven-segment solutions out there, not really. Here I am, I've sorted all of the LED displays on Digikey seven-segment ones by three- and four-digit ones and let's sort by unit price of, say, 1,000.

**Dave Jones:** And let's have a look at it. Well, we've got something here. We've got a three-digit display, which is 86 cents. That's a bit cheaper, but they don't have any in stock.

**Dave Jones:** Look, what's the point? We get down to the display we're using down here, which is a similar cost. We're talking a dollar 30. So, you know, if you're talking Digikey here, which is what you really want to base a project like this on, unless you want to go for Ali Baba or something like that in China, the prices are pretty much set at say a dollar 30 per thousand of quantity.

**Dave Jones:** You might be able to get the price down a bit, but it's not that great. But, as I said, the current consumption of a seven segment display is fairly prohibitive.

**Dave Jones:** Okay, I've used my parametric search here to search for LCD displays. I've limited here to three through to four digit ones cuz that's really all we need. We can get away with three, three and a half one will be okay, and four digit one will be okay, too.

**Dave Jones:** So, I've applied the filter to that, and let's go over and let's search for our thousand of quantity again. Nice good ballpark figure when you're working on a design like this cuz I think it, you know, it'll sell in the thousand or two.

**Dave Jones:** So, that's the price target I'm going to shoot for, and let's have a look. We've got some nice looking Lumex ones here, and I've seen these before, and we're talking, you know, they're cheaper than the seven segment LED display solution.

**Dave Jones:** Okay, we're talking 95 cents here. They're available in, you know, there's a decent quantity available in Digi-Key, not a huge amount, but they're there, and they're 95 cents a pop.

**Dave Jones:** Well, that's cheaper than our seven segment LED display solution, lower power, so it's not a bad choice, I guess. You can certainly go for that. So, that looks like pretty much the best solution there.

**Dave Jones:** And yeah, they jump up in price pretty quick. Look at that, you know, $2.50, bam. And trust me, I've searched Mouser and things like that, and it doesn't really get much better.

**Dave Jones:** So, from the reputable suppliers, you're talking 95 cents or almost a dollar for a three digit, in in this case, this is a three digit display solution, and we can actually take a look at the data sheet like that if we want, and we will, because that comes into uh how many uh well well what sort of microcontroller we need with built-in LCD capability to drive this thing.

**Dave Jones:** Now, for some reason I'm really getting déjà vu on this. I think I've gone through all this before in my um battery-powered power supply thing. So, I Please uh forgive me if I have gone through this before, but we'll do it again.

**Dave Jones:** This uh to drive this uh seven-segment display here, this 95 cent display, just one of them uh by the way, we need a microcontroller that has one common pin, and we have uh well, basically uh 23 uh different segments.

**Dave Jones:** So, we need a microcontroller that has only that has support for one common pin. All of them will have that, but uh some will have, you know, two, three, or four common pins.

**Dave Jones:** Um but we need one common pin with 23 segments. So, we need to find a microcontroller that is uh capable of driving this LCD display. Now, what microcontroller I'm actually targeting uh for this is an ATtiny48-AU, and it's um it's one of the um you know, it's one of the tiny range of microcontrollers.

**Dave Jones:** Unfortunately, they only have 100 quantity uh price breaks here, but that's 86 cents. So, um as you can see, that's cheaper than uh than any solution itself. So, if you take out the display and you take out the DC-to-DC converter, then the microcontroller becomes the most expensive component on your entire board at 86 cents.

**Dave Jones:** But, of course, this one can't drive a microcontroller. So, let's find the next simplest one that can drive this LCD. Okay, what I've done here, I've decided, "No, I'll search for every brand microcontroller on the market available from Digikey according to their parametric search that has an LCD display.

**Dave Jones:** So, I've gone through the table here and I've searched out all the ones that have LCDs and I've sorted by thousand off price and right up the top here or at the bottom of the price scale, we have a Freescale RS 08.

**Dave Jones:** Doesn't look like a 28-pin SOIC. Doesn't look like it's going to have enough pins. We're talking 68 cents in thousand off quantity and then it jumps up to the next one jumps up to some PIC 16LF 1900 series micros.

**Dave Jones:** I've actually used those before. They're not bad and they're like, you know, jump up to 99 cents, a dollar, something like that. So, we've automatically jumped up like an extra 20 cents in our price, but these are only like the 28-pin ones cuz we've got 24 pins already just for the LCD including the common and we need the power and ground.

**Dave Jones:** So, there's 26 and that only leaves two pins available, which is useless. So, we really need to search for ones that have greater than 28 pins. So, let's try that.

**Dave Jones:** All right. So, what I'm going to do here is just limit these to 44 pins through to 48 cuz I don't want some monster device and I want something that's got an adequate number of pins and I know a 44-pin device will be able to do what we want.

**Dave Jones:** So, bingo, I've searched again and as it turns out, the PIC 16LF 1934, it still kept our thousand off quantity here and sorted by by price. Bingo, we've automatically jumped up to a dollar 68.

**Dave Jones:** That is almost double what our previous ATtiny 48 device is and there you go and I'm still searching every one of these manufacturers. As you can see, right? To go for this LCD solution, we've saved a little bit of cost going from our LED over to our LCD, but then we've doubled the cost of our chip.

**Dave Jones:** Crazy. So, just there you started to see the trade-offs between cost of your display, your functionality required in your microcontroller to drive it, and things like that. So, I got to thinking, well, how can I lower the cost of this display solution?

**Dave Jones:** Cuz I think the LCD is still, you know, I think I can get a lower cost than that at you know, what was it? 96 cents or just under a dollar or something like that.

**Dave Jones:** I can get cheaper again. Probably not as good in the seven-segment display department, but we'll see. Now, one obvious way to do this is to use a LED seven-segment display, but instead of using an expensive actual seven-segment display like used on this one, you can actually replace these individual segments with individual LEDs because LEDs are really cheap.

**Dave Jones:** When you buy them on a reel of like 3,000, they're like a cent each or something like that. They're incredibly cheap. So, you can actually manufacture you could put like two LEDs there for each segment, and you could even get reverse mount ones, but they're a bit more expensive.

**Dave Jones:** But, like I use on my micro controller, reverse mount ones mount on the back of the board, shine through the board a little, and then you could uh drill a little slot in your board on your PCB file, and you can actually make your own seven-segment displays out of individual LEDs, and it can actually work out cheaper.

**Dave Jones:** Individual LEDs for all these segments for the whole three or four digits later whatever than it is to buy the completed LED assembly. But, that's not my solution because that will save you cost.

**Dave Jones:** So, if you're just after cost, that could be a way to do it, but I want cost and reduced current consumption, too. So, what have I got up my sleeve?

**Dave Jones:** Let's take a look at it. It does involve LEDs. Some people aren't going to like this, but I want to hear your feedback whether or not you think it's a good concept.

**Dave Jones:** Let's go to the CAD tool. And I was going to show you this concept on the breadboard, but it's easier just to show it in the CAD tool in the 3D view, and this is what I have in mind.

**Dave Jones:** Here it is. Here. Tada! It uses individual It's a decade-based individual LED display like this. So, we've got a total of 32 LEDs here, and allows us to display voltage and current in these vertical segments up and down here like this.

**Dave Jones:** Now, these are like a standard 0603 surface-mount LEDs, and like I said, they're like a cent each. They're incredibly cheap. So, this entire display solution costs 32 cents, and it works as a Well, it can work as a dual display.

**Dave Jones:** You toggle between voltage and current down here. So, what we have is a vertical bar graph effectively of 10 LEDs for each digit like this. The Because we don't actually need all 10 for the for the most significant digit over here for voltage and current, because our voltage is only going to go up to In this case, it's XX.XX volts, so it's 10 mV resolution on this thing, but we don't

**Dave Jones:** need to go up to 99.99 volts, right? We only want to go up to like one or zero Sorry, one or two. Say, 20 volts, for example. This could actually go up to 29.

**Dave Jones:** 99 volts. So, I can go practically to 30 volts with these only two LEDs. And there's no need to have the most significant zero on there either because our decimal point is not here, it's here and here for milliamps.

**Dave Jones:** So, um the good I what I like about this, it's a bit harder to read of course than a seven segment uh LED display or a seven segment LCD display, but it's a really cheap.

**Dave Jones:** It's like 32 cents or less. There's no hand soldering involved like there are with um this uh LCD and this uh seven segment LED display solution. So, it's all done by the pick and place machine which helps reduce your assembly cost again cuz you're not paying for that hand assembly labor.

**Dave Jones:** So, uh the other good thing of course is that this is a lower power solution. And you would multiplex this of course. You've got a You would multiplex the individual rows like this and you'll be able to see this on my um You'll be able to see this on the uh if I go into the 2D mode here, they're you know, uh column base like that and on the bottom row they would go

**Dave Jones:** across like that. So, you multiplex them all like that. Okay? And it's um and so you've only got one LED on at any one time. So, your entire display solution is safe if you want 5 milliamps per LED, it's only going to be 5 milliamps cuz you would scan because you're only going to have one LED in each of these columns on a any one time.

**Dave Jones:** Let's say you've got uh 12.34 volts. Well, this LED here will be on to represent the tens digit. This LED here will be on to represent um so, that's 12 1 2 and then this LED here will be on with three and then .4 there.

**Dave Jones:** So, it's 12.34 volts. And as you like uh press the buttons on this thing, I can think it it'd be quite neat cuz you'll see the LEDs sort of, you know, scanning up the bar graph like this, and then it'll count up, and then well, I think it would actually be quite neat to actually watch it as you, uh, you know, turn the knob, or in this case, uh, press the

**Dave Jones:** buttons, cuz I'm not going with knobs, but I think this will work out quite well. Let me know what you think. I know it not everyone is going to, uh, like this, but it is cheap, and it's reasonably low power.

**Dave Jones:** Sure, not as low power as a segment seven segment display, but we but it means that we can use our, you know, 80 cent microcontroller instead of our dollar 60 microcontroller, for example.

**Dave Jones:** Uh, and we can, um, so we've, you know, halved the cost of our microcontroller there, and it doesn't and we've got a wider choice of microcontrollers, cuz it doesn't have to have a built-in LCD controller.

**Dave Jones:** There you go. I think it's rather a neat solution. Let me know what you think, if you like it, if you don't like it, but please just bear in mind that it is super duper cheap, and it's easy to get.

**Dave Jones:** There's no, you know, it just uses standard off-the-shelf surface mount LEDs. I'm going to call it Dave's decade digit display. I don't know. Is it catchy? But there you go.

**Dave Jones:** It's not, you know, it's not new. Projects have done this, uh, before, but hardly anyone ever does it, but I think there's still possibly a reason to use it here, eh?

**Dave Jones:** It's a bit novel, but it saves, uh, cost, and, uh, and, uh, you know, machine assembly and things like that, and easy to get parts. It's not too bad on the, uh, power front, as well.

**Dave Jones:** So, there you go. Anyway, let me know your thoughts. I think I'm probably going to go with this, unless somebody can, uh, convince me otherwise to go with an LCD, um, solution, cuz it comes down to basically this or a, uh, seven segment LCD.

**Dave Jones:** Let me know what you think and uh as always jump on over to the EEVblog forum to discuss it and uh uh please if you like this video, if you like this uh USB power supply series, please give it a big thumbs up.

**Dave Jones:** Catch you next time.
