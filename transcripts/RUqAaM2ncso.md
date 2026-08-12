---
video_id: RUqAaM2ncso
title: EEVblog #298 - Dave's Decade Digit Display - USB Supply Part 3
url: https://www.youtube.com/watch?v=RUqAaM2ncso
source: youtube-asr
---

**Dave Jones:** Hi, it's USB lab power supply time again and I promised that I would talk about the display solution used on here because I said I wanted to go away from the LED display used on my previous prototypes and

**Dave Jones:** possibly use something else because you know I've been talking about this you saw in the previous video the housing display I'm going to use like a clear thing on the top possibly so I'll be able to see whatever display solution is

**Dave Jones:** through the clear Perspex or polycarbonate cover on the front so there's no need to worry about things like cutouts because when you do when you use displays like these seven segment displays or LCDs or something like that you'll notice that you have to add

**Dave Jones:** cutouts to you know to see the display through on a typical front panel and they're a pain in the ass to get those aligned it's extra cost in manufacture and things like that so with a clear you know display window on the front of

**Dave Jones:** this thing we can use pretty much anything we want LCD LED whatever and you'll be able to see it straight through so why am I going away from these seven segment LED displays well it's pretty obvious they draw a fair bit of current

**Dave Jones:** now you can get really efficient LCD LED displays these ones are LTC7424 they're a very nice little display and they're reasonable cost I will have a look at the cost in in a minute cuz that's what it's going to come down to

**Dave Jones:** really for the display choice this time around so these aren't bad displays but they're going to take at least a couple of milliamps per segment to get them at a you know a usable brightness in you know a typical environment you

**Dave Jones:** know like a lab or an office or a room or whatever. So, let alone outside. Let's say you got, you know, a good grunty 5 milliamps per segment. That should give you a fairly decent brightness. Well, you could have,

**Dave Jones:** if you're displaying an eight with a decimal point, you could have eight of those on for each one of those digits. So, that's 40 milliamps. That's 8 * 5 milliamps, 40 milliamps right there for one digit. And of course, you wouldn't

**Dave Jones:** with these sort of solutions, you multiplex them. Um so, you know, you can get a maximum ever Well, a maximum value of 40 milliamps for the entire display. That you know, in a normal project, it's probably not a lot. In a regular bench

**Dave Jones:** power supply, not a huge amount. But, this thing, we've only got 500 milliamps uh total. What we're ignoring power here. We're just, you know, 500 milliamps at 5 volts. But, then you got the loss of the converter, the the

**Dave Jones:** isolated DC to DC converter. And to draw 40 milliamps at say 3.3 volts, that's a fair whack of your power budget. So, really bad idea to do the LED display. But, as you might see, going to end up using

**Dave Jones:** LED. But, you'll see something a little bit different. Come to that. Now, the obvious solution everyone says use LCD. Great. Okay, I like LCD displays as much as the next person. But, we'll take a look at it there. And a similar cost

**Dave Jones:** solution, probably even a little bit more than these seven-segment LED displays. So, really I'm trying to keep cost as absolute low as possible on this project. So, LCD, well, it's a, you know, a nice solution. A, it's expen- It's, you know, it's not

**Dave Jones:** cheap um unless you go for 100 low, get them from Alibaba in China. And uh it's just it's really horrid. It's not something you want to do for a project like this. I want to stick to like a name brand LCD,

**Dave Jones:** something that, you know, is going to be available in 5 years time or something like that, not just some one-batch wonder from OneHungLow on Alibaba. So, the LCD solution, uh it's not bad, similar cost, but then you've got to find an LCD

**Dave Jones:** uh a microcontroller with an LCD driver to drive the thing. I'm going to come up with a really low-cost display solution. It's not nearly as good in terms of uh you know, direct reading and things like that, as you'll see, but I think

**Dave Jones:** it's reasonably clever if you want a really ultra-low-cost solution. Let's go to the web. All right, let's jump straight on to Digikey, shall we? And we'll search for our LTC70 uh 4724, which is what I've used in my

**Dave Jones:** previous one, and here it is. And uh let's scroll across and take a look at it. It's from uh Lite-On, and they're a really nice little compact display. I really like them. They're really small, but uh they're $2.92 in one-off

**Dave Jones:** quantity. Well, let's uh go in and look at the price breakdown for those. Even if I'm making a thousand of these things, buck 30 each, right? So, that's $2.60, bam, right there in your cost. So, remember that. Well, even if we had like

**Dave Jones:** one of them, for example, okay, we're still talking a dollar 30 in a thousand of quantity. Not that, you know, when you're trying to shave cents off your production cost and things like that, trying to keep this thing ultra-low

**Dave Jones:** cost, um that would make this, by far, the most expensive component on the entire board. Well, it'd be the most expensive uh apart from the DC-to-DC converter, but that's always going to be the most expensive component in a little USB

**Dave Jones:** power supply like this. And by the way, folks, for all those who are complaining or asking, "Why don't I make this thing, you know, capable of 2 amp, you know, to utilize the USB ports with 2 amps or 3

**Dave Jones:** amps or whatever the latest charging standard is in USB 3.0?" It is because the DC-to-DC converters are very expensive and they don't linearly increase in cost. Usually, to go from, say, a 2-W converter, which is what we need for a 500-mA solution, up to, you

**Dave Jones:** know, a you know, a 5- or 6-W version or even higher, that we'll need for a higher power solution. It's just they you can double, triple, quadruple your bomb cost right on your isolated DC-to-DC converter like that. And, of

**Dave Jones:** course, I want this project to be isolated, so that isolated converter is an absolute essential. So, if you're if you complained about that and wondering why I don't use it, well, go and check the costings for these DC-to-DC

**Dave Jones:** converters and you'll find out for yourself. And if you're wondering if there are cheaper LED seven-segment solutions out there, not really. Here I am, I've sorted all of the LED displays on Digikey seven-segment ones by three- and four-digit ones and let's sort by unit

**Dave Jones:** price of, say, 1,000. And let's have a look at it. Well, we've got something here. We've got a three-digit display, which is 86 cents. That's a bit cheaper, but they don't have any in stock. Look, what's the point? We get

**Dave Jones:** down to the display we're using down here, which is a similar cost. We're talking a dollar 30. So, you know, if you're talking Digikey here, which is what you really want to base a project like this on, unless you want to go for

**Dave Jones:** Ali Baba or something like that in China, the prices are pretty much set at say a dollar 30 per thousand of quantity. You might be able to get the price down a bit, but it's not that great. But, as I

**Dave Jones:** said, the current consumption of a seven segment display is fairly prohibitive. Okay, I've used my parametric search here to search for LCD displays. I've limited here to three through to four digit ones cuz that's really all we need. We can get away with three, three

**Dave Jones:** and a half one will be okay, and four digit one will be okay, too. So, I've applied the filter to that, and let's go over and let's search for our thousand of quantity again. Nice good ballpark figure when you're working on

**Dave Jones:** a design like this cuz I think it, you know, it'll sell in the thousand or two. So, that's the price target I'm going to shoot for, and let's have a look. We've got some nice looking Lumex ones here,

**Dave Jones:** and I've seen these before, and we're talking, you know, they're cheaper than the seven segment LED display solution. Okay, we're talking 95 cents here. They're available in, you know, there's a decent quantity available in Digi-Key, not a huge amount, but they're there,

**Dave Jones:** and they're 95 cents a pop. Well, that's cheaper than our seven segment LED display solution, lower power, so it's not a bad choice, I guess. You can certainly go for that. So, that looks like pretty much the best

**Dave Jones:** solution there. And yeah, they jump up in price pretty quick. Look at that, you know, $2.50, bam. And trust me, I've searched Mouser and things like that, and it doesn't really get much better. So, from the reputable suppliers, you're

**Dave Jones:** talking 95 cents or almost a dollar for a three digit, in in this case, this is a three digit display solution, and we can actually take a look at the data sheet like that if we want, and we will, because that comes

**Dave Jones:** into uh how many uh well well what sort of microcontroller we need with built-in LCD capability to drive this thing. Now, for some reason I'm really getting déjà vu on this. I think I've gone through all this before

**Dave Jones:** in my um battery-powered power supply thing. So, I Please uh forgive me if I have gone through this before, but we'll do it again. This uh to drive this uh seven-segment display here, this 95 cent display, just one of them uh by the way,

**Dave Jones:** we need a microcontroller that has one common pin, and we have uh well, basically uh 23 uh different segments. So, we need a microcontroller that has only that has support for one common pin. All of them will have that, but uh some will have,

**Dave Jones:** you know, two, three, or four common pins. Um but we need one common pin with 23 segments. So, we need to find a microcontroller that is uh capable of driving this LCD display. Now, what microcontroller I'm actually targeting uh for this is an

**Dave Jones:** ATtiny48-AU, and it's um it's one of the um you know, it's one of the tiny range of microcontrollers. Unfortunately, they only have 100 quantity uh price breaks here, but that's 86 cents. So, um as you can see, that's cheaper than uh than any

**Dave Jones:** solution itself. So, if you take out the display and you take out the DC-to-DC converter, then the microcontroller becomes the most expensive component on your entire board at 86 cents. But, of course, this one can't drive a microcontroller. So, let's find the next

**Dave Jones:** simplest one that can drive this LCD. Okay, what I've done here, I've decided, "No, I'll search for every brand microcontroller on the market available from Digikey according to their parametric search that has an LCD display. So, I've gone through the table

**Dave Jones:** here and I've searched out all the ones that have LCDs and I've sorted by thousand off price and right up the top here or at the bottom of the price scale, we have a Freescale RS 08. Doesn't look like a 28-pin

**Dave Jones:** SOIC. Doesn't look like it's going to have enough pins. We're talking 68 cents in thousand off quantity and then it jumps up to the next one jumps up to some PIC 16LF 1900 series micros. I've actually used those before. They're not

**Dave Jones:** bad and they're like, you know, jump up to 99 cents, a dollar, something like that. So, we've automatically jumped up like an extra 20 cents in our price, but these are only like the 28-pin ones cuz we've got 24 pins already just for the

**Dave Jones:** LCD including the common and we need the power and ground. So, there's 26 and that only leaves two pins available, which is useless. So, we really need to search for ones that have greater than 28 pins. So, let's try that. All right.

**Dave Jones:** So, what I'm going to do here is just limit these to 44 pins through to 48 cuz I don't want some monster device and I want something that's got an adequate number of pins and I know a 44-pin device will be able to do what we

**Dave Jones:** want. So, bingo, I've searched again and as it turns out, the PIC 16LF 1934, it still kept our thousand off quantity here and sorted by by price. Bingo, we've automatically jumped up to a dollar 68. That is almost double what

**Dave Jones:** our previous ATtiny 48 device is and there you go and I'm still searching every one of these manufacturers. As you can see, right? To go for this LCD solution, we've saved a little bit of cost going from our LED over to our

**Dave Jones:** LCD, but then we've doubled the cost of our chip. Crazy. So, just there you started to see the trade-offs between cost of your display, your functionality required in your microcontroller to drive it, and things like that. So, I got to thinking, well,

**Dave Jones:** how can I lower the cost of this display solution? Cuz I think the LCD is still, you know, I think I can get a lower cost than that at you know, what was it? 96 cents or just under a dollar or

**Dave Jones:** something like that. I can get cheaper again. Probably not as good in the seven-segment display department, but we'll see. Now, one obvious way to do this is to use a LED seven-segment display, but instead of using an expensive actual seven-segment display

**Dave Jones:** like used on this one, you can actually replace these individual segments with individual LEDs because LEDs are really cheap. When you buy them on a reel of like 3,000, they're like a cent each or something like that. They're incredibly

**Dave Jones:** cheap. So, you can actually manufacture you could put like two LEDs there for each segment, and you could even get reverse mount ones, but they're a bit more expensive. But, like I use on my micro controller, reverse mount ones

**Dave Jones:** mount on the back of the board, shine through the board a little, and then you could uh drill a little slot in your board on your PCB file, and you can actually make your own seven-segment displays out of individual LEDs, and it

**Dave Jones:** can actually work out cheaper. Individual LEDs for all these segments for the whole three or four digits later whatever than it is to buy the completed LED assembly. But, that's not my solution because that will save you cost. So, if you're just after cost,

**Dave Jones:** that could be a way to do it, but I want cost and reduced current consumption, too. So, what have I got up my sleeve? Let's take a look at it. It does involve LEDs. Some people aren't going to like

**Dave Jones:** this, but I want to hear your feedback whether or not you think it's a good concept. Let's go to the CAD tool. And I was going to show you this concept on the breadboard, but it's easier just to

**Dave Jones:** show it in the CAD tool in the 3D view, and this is what I have in mind. Here it is. Here. Tada! It uses individual It's a decade-based individual LED display like this. So, we've got a total of 32 LEDs here, and

**Dave Jones:** allows us to display voltage and current in these vertical segments up and down here like this. Now, these are like a standard 0603 surface-mount LEDs, and like I said, they're like a cent each. They're incredibly cheap. So, this entire

**Dave Jones:** display solution costs 32 cents, and it works as a Well, it can work as a dual display. You toggle between voltage and current down here. So, what we have is a vertical bar graph effectively of 10 LEDs for

**Dave Jones:** each digit like this. The Because we don't actually need all 10 for the for the most significant digit over here for voltage and current, because our voltage is only going to go up to In this case, it's XX.XX volts, so it's 10 mV

**Dave Jones:** resolution on this thing, but we don't need to go up to 99.99 volts, right? We only want to go up to like one or zero Sorry, one or two. Say, 20 volts, for example. This could actually go up to 29.

**Dave Jones:** 99 volts. So, I can go practically to 30 volts with these only two LEDs. And there's no need to have the most significant zero on there either because our decimal point is not here, it's here and here for milliamps. So, um the good

**Dave Jones:** I what I like about this, it's a bit harder to read of course than a seven segment uh LED display or a seven segment LCD display, but it's a really cheap. It's like 32 cents or less. There's no hand soldering involved like

**Dave Jones:** there are with um this uh LCD and this uh seven segment LED display solution. So, it's all done by the pick and place machine which helps reduce your assembly cost again cuz you're not paying for that hand assembly labor. So,

**Dave Jones:** uh the other good thing of course is that this is a lower power solution. And you would multiplex this of course. You've got a You would multiplex the individual rows like this and you'll be able to see this on my um

**Dave Jones:** You'll be able to see this on the uh if I go into the 2D mode here, they're you know, uh column base like that and on the bottom row they would go across like that. So, you multiplex them

**Dave Jones:** all like that. Okay? And it's um and so you've only got one LED on at any one time. So, your entire display solution is safe if you want 5 milliamps per LED, it's only going to be 5 milliamps cuz

**Dave Jones:** you would scan because you're only going to have one LED in each of these columns on a any one time. Let's say you've got uh 12.34 volts. Well, this LED here will be on to represent the tens digit. This

**Dave Jones:** LED here will be on to represent um so, that's 12 1 2 and then this LED here will be on with three and then .4 there. So, it's 12.34 volts. And as you like uh press the buttons on this thing, I can think it

**Dave Jones:** it'd be quite neat cuz you'll see the LEDs sort of, you know, scanning up the bar graph like this, and then it'll count up, and then well, I think it would actually be quite neat to actually watch it as you, uh, you know, turn the

**Dave Jones:** knob, or in this case, uh, press the buttons, cuz I'm not going with knobs, but I think this will work out quite well. Let me know what you think. I know it not everyone is going to, uh, like

**Dave Jones:** this, but it is cheap, and it's reasonably low power. Sure, not as low power as a segment seven segment display, but we but it means that we can use our, you know, 80 cent microcontroller instead of our dollar 60

**Dave Jones:** microcontroller, for example. Uh, and we can, um, so we've, you know, halved the cost of our microcontroller there, and it doesn't and we've got a wider choice of microcontrollers, cuz it doesn't have to have a built-in LCD controller.

**Dave Jones:** There you go. I think it's rather a neat solution. Let me know what you think, if you like it, if you don't like it, but please just bear in mind that it is super duper cheap, and it's easy to get.

**Dave Jones:** There's no, you know, it just uses standard off-the-shelf surface mount LEDs. I'm going to call it Dave's decade digit display. I don't know. Is it catchy? But there you go. It's not, you know, it's not new. Projects have done this,

**Dave Jones:** uh, before, but hardly anyone ever does it, but I think there's still possibly a reason to use it here, eh? It's a bit novel, but it saves, uh, cost, and, uh, and, uh, you know, machine assembly and things like that, and easy to get parts.

**Dave Jones:** It's not too bad on the, uh, power front, as well. So, there you go. Anyway, let me know your thoughts. I think I'm probably going to go with this, unless somebody can, uh, convince me otherwise to go with an LCD, um,

**Dave Jones:** solution, cuz it comes down to basically this or a, uh, seven segment LCD. Let me know what you think and uh as always jump on over to the EEVblog forum to discuss it and uh uh please if you like this video, if you

**Dave Jones:** like this uh USB power supply series, please give it a big thumbs up. Catch you next time.
