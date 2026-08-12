---
video_id: YCvDl0oXOSY
title: EEVblog 1703 - µTimer Project Part 2: An E-Paper Like LCD
url: https://www.youtube.com/watch?v=YCvDl0oXOSY
source: youtube-asr
timestamps: {"0": 0, "1": 14, "2": 31, "3": 40, "4": 56, "5": 76, "6": 90, "7": 104, "8": 118, "9": 134, "10": 148, "11": 159, "12": 170, "13": 185, "14": 207, "15": 219, "16": 230, "17": 242, "18": 251, "19": 262, "20": 285, "21": 297, "22": 311, "23": 327, "24": 337, "25": 348, "26": 362, "27": 371, "28": 383, "29": 389, "30": 410, "31": 418, "32": 427, "33": 436, "34": 449, "35": 457, "36": 469, "37": 488, "38": 498, "39": 516, "40": 533, "41": 542, "42": 554, "43": 563, "44": 581, "45": 592, "46": 603, "47": 616, "48": 625, "49": 649, "50": 660, "51": 670, "52": 685, "53": 698, "54": 709, "55": 719, "56": 731, "57": 743, "58": 753, "59": 767, "60": 779, "61": 789, "62": 803, "63": 816, "64": 830, "65": 850, "66": 863, "67": 882, "68": 896, "69": 916, "70": 935, "71": 946, "72": 957, "73": 979, "74": 992, "75": 1011, "76": 1021, "77": 1032, "78": 1046, "79": 1055, "80": 1070, "81": 1086, "82": 1094, "83": 1107, "84": 1117, "85": 1134, "86": 1152, "87": 1164, "88": 1172, "89": 1194, "90": 1209, "91": 1219, "92": 1231, "93": 1245, "94": 1257, "95": 1267, "96": 1287, "97": 1295, "98": 1306, "99": 1315, "100": 1326, "101": 1336, "102": 1347, "103": 1356, "104": 1372, "105": 1393, "106": 1407, "107": 1419}
---

**Dave Jones:** Hi, this is part two to the micro timer project. I'll link in part one if you haven't seen it where we looked at several LCD displays from bydisplay.com because this project is all centered around the LCD.

**Dave Jones:** So, it's important as a first step to pick you know a suitable LCD and then you like design the product envelope around that so to speak and possibly some of the other features and the battery and all sorts of things that we'll look at in future videos, hopefully.

**Dave Jones:** And in this video, we're going to be looking at another LCD that I just got delivered today. Haven't tried it yet, so we're going to try it out. It's from a different manufacturer.

**Dave Jones:** It's a completely different type, smaller, cheaper, and maybe looks better. But fingers crossed, let's try it out. Anyway, thank you for everyone who commented on my previous video. One of the most popular comments I got is Dave, just use e-paper e-ink display.

**Dave Jones:** They're fantastic. They're cheap as chips. They look like a million bucks and they're reflective, exactly what you're looking for for this product. Unfortunately, that's not the case. Whilst yes, they look absolutely fantastic and they're cheap and blah blah blah and readily available in the form factors required and all sorts of things.

**Dave Jones:** Unfortunately, they're not suitable. Let me show you why. This is the manufacturer of the display we're going to look at today and they primarily manufacture e-ink e-paper displays. They're called You might think it's good display, but it's actually good display.

**Dave Jones:** So, gooddisplay.com is the LCD we're going to look at today. LCD, not e-paper, but basically they make e-paper displays and they've got usage guidelines down here. We can go down and read them and here's the trap for young players.

**Dave Jones:** E-paper displays are suitable for update cycles ranging from tens of seconds to minutes. Well, we're after like a timer, a stopwatch, like once a second, tenth of a second, hundredth of a second, something like that.

**Dave Jones:** We need a high update rate and continuously updating display. And unfortunately, um e-paper {slash} e-ink displays are not designed for this. They're designed for your Kindle or whatever it is or your price tags at your supermarket that might change once a once a day or once a week.

**Dave Jones:** Current inflation, yeah, every hour. So, most black and white e-paper screens have a fast refresh rate of 1.5 to 2.5 seconds refresh. It can get faster than this, but they're not a fast updating uh display.

**Dave Jones:** Ideal for applications where static image is maintained without constant electricity, which is one of the great things about them. You remove the power, they're super low power. You remove the power, and well, the static image remains there.

**Dave Jones:** You basically don't need any power at all to keep the image on the display. And while that's very cool, they do actually take significant current to when you do actually switch the display.

**Dave Jones:** It's like tens of milliamps, even hundreds of milliamps to switch the display over. But not necessarily a problem, but when you've got a timer continuously ticking over like 10th of a second or even seconds, you're constantly refreshing that display, so they're not actually going to be that low power.

**Dave Jones:** They can't work at sub-zero temperatures, etc., etc. But basically, yeah, they've actually got a display usage guideline here. And there's other gotchas in their guideline here. Although the refresh rate of monochrome LCD e-paper is faster than that of color, we're still recommending at least a 180-second interval after completing a set of display updates.

**Dave Jones:** Frequent updates can negatively impact the lifespan of the e-paper, and it's not just this manufacturer, it's all e-ink {slash} e-paper. In fact, let's go to eink.com. They're, you know, the preeminent, are they?

**Dave Jones:** Preeminent manufacturer of e-ink {slash} displays. Technically, e-ink uses a different technology to e-paper, but they've got a similar limitation in terms of um, I've been, know, refreshing and update.

**Dave Jones:** So, let's have a look at their um, e-ink Carta 1200. It's one of their, you know, uh, premier uh, displays here. And module environment, here it is. Service life.

**Dave Jones:** They have a service life, 10 million switches or 5 years. So, this is one of the better ones on the market. The uh, good display ones I think are about a million or something like that.

**Dave Jones:** And typically, you, you know, as an industry rule of thumb, you would take it that an e-ink e-paper display sort of like has a maximum usable uh, you know, refresh uh, lifetime of about a million.

**Dave Jones:** You know, 100,000 to be safe, something like that. So, unfortunately, they are not the display solution for a permanent timer like this that's sitting there just doing a clock thing or you know, when you're not using it and then ticking over really fast when you're doing like a a timer thing, constant refresh, 24 hours a day, 7 days a week, battery-powered for, you know, for 10 years.

**Dave Jones:** It's just, no. It's, sorry, uh, for all you e-ink e-paper fanboys, but it's not the solution. Anyway, um, they do manufacture, uh, good display do manufacture a TFT display.

**Dave Jones:** And thank you for Silicon Wizard on the EE blog forum for pointing this one out cuz I never would have found it otherwise. Um, it's a 2.9 inch, which is smaller than we've had before, but it's higher resolution, 384 by 168 resolution reflective.

**Dave Jones:** And it's a reflective display, which is what I was after. I wasn't really wanting a transflective display. Um, I think somebody in the comments reckoned, "Oh, I could use the backlight for like a visual alert indicator that the time is finished or something like that." And yeah, that would have been useful.

**Dave Jones:** I would have hooked it up um, for that sort of uh, purpose. But ultimately, I am after a reflective display is more betterer. So, um, yeah, this is a reflective display um, LCD.

**Dave Jones:** And it uses that uh, ST uh, chipset. So, this is the ST7305. So, slightly different to the one we used in the uh, previous video. It's got a wide operating temperature range.

**Dave Jones:** Um it's got that high resolution. It's got an SPI interface and it has paper-like displaying. So, hopefully it'll be, you know, like similar to e-ink e-paper. That's what they're claiming anyway, but it's an actual TFT display.

**Dave Jones:** So, we'll find out about that and it's low-powered, Jobi. Um so, yeah, it all sounds very good and it's cheaper than the buy display ones we looked at in the uh previous video.

**Dave Jones:** So, uh but it is physically smaller, but anyway, we'll compare the size in a minute, but it's cheaper. Hopefully it looks better, but I do have to order a 1,000 minimum order quantity.

**Dave Jones:** The company would send me a couple of samples, but it's not like I can go out and order 100 off them or something like that. You got to order 1,000 minimum, which is fine.

**Dave Jones:** It's got on-chip display RAM, etc. It's got on-chip boosters and stuff, so less circuitry you need on your board. Fantastic. Now, this company's really good in terms of demo boards, way better than that, you know, dodgy 8051 ancient 8051 matrix handmade matrix thing that they had um in the uh and we looked at in the previous video.

**Dave Jones:** They've got a whole bunch of these. If you go into their uh driver boards, look at this. They've got ESP32, which is the one uh that they've actually sent in uh here.

**Dave Jones:** I didn't know which one they were going to send. They they just said The interesting thing about this company is I emailed them say, "Hey, do you have samples available?" Yeah, we got samples.

**Dave Jones:** "And do you have a demo board?" And they said, "Oh, we don't have a demo board for that specific one, but we can probably make one for you." You want to go, "Oh, yeah, okay, that'd be great.

**Dave Jones:** How much?" And they went, "25 dollars." Beauty. So, it looks like I don't know, like it it's this board here. So, they already had the board, um but uh maybe they custom programmed it for me or something to work with display.

**Dave Jones:** It's supposed to work out of the box. Haven't tried it yet. Let's give it a whirl. Um see if it works. So, anyway, so this has got an Arduino form factor.

**Dave Jones:** They've got Raspberry Pi form factor ones down here. Um and they've got looks like other sort of customy ones down here. So, there's a whole selection of different demo There's more pages.

**Dave Jones:** Hang on. Uh, yes, they did include one of these adapter boards somewhere. And yes, they included this adapter board over here as well. So, presumably, it's got the same pin out as their e-paper ones because these boards don't look hacked in any way.

**Dave Jones:** What's a resi option? FPC of e-paper, but this is the board they've given me. So, presumably, it works and you can download specification just for the interface board and the schematic as well.

**Dave Jones:** Look at that. There it is. Looks like they're using an Altium there. And yeah, so there's there's a schematic of the interface board. Nice. And for this display we're going to look at we can download not only the specification, but we can download the data sheet for the ST7305 and STM32 sample codes.

**Dave Jones:** Aha, so are we going to end up using an STM32 for this project? It was one of the considerations. Haven't chosen the microcontroller yet, but if we've got the sample code for it, well, why not run with that as like a first choice processor for this thing perhaps?

**Dave Jones:** They're very popular, so all the STM32 fanboys go wild. So, we had a 4-in display before. We've only got 2.9 in now, but it's not about the length, it's the width.

**Dave Jones:** That's what she said. Dalian Good Display Co. Limited. There you go. It's been approved, checked, and design stamped. Beauty. Rev 3, so they have several shots at this. It should work well.

**Dave Jones:** Here we go. We've got the physical dimensions. We've got our pin description. Here you go. So, yeah, I assume it's the exact same pin out as their e-ink e-paper displays.

**Dave Jones:** They probably did that deliberately for compatibility. So, if you did if you wanted the advantage of e-ink e-paper, but if you wanted the TFT technology with an infinite number of rights like we do here, then um yeah, it looks like they've provided this uh display as an option.

**Dave Jones:** I think it's pretty much the only one that they have. Um and it's happens to be in the form factor that we want. So, yeah, pretty groovy. Okay, so it looks like we just need some external caps on there just like the uh previous displays.

**Dave Jones:** It's got the internal boost converters and everything uh inside. It just needs some uh caps there for all the voltage uh doubling stuff. So, um basic power consumption. Now, the interesting thing about this is it's super low power.

**Dave Jones:** Order of magnitude lower than what we looked at in the previous video. Um operating current um 14 microamps here. So, the power consumption without any uh display on the screen.

**Dave Jones:** That's why it says without screen here. Um as you can see, 1.9 microamps. Sniff of of an oily rag stuff. They have goofed in the data sheet. It's 1.9 milliamps here.

**Dave Jones:** That should be microamps. So, oops, they've goofed there. So, 1.9 um microamps quiescent uh current when testing. And they've provided another graph where they continually update the screen with well, I assume maybe it's just like refreshing the same data on the uh screen, but it's not I don't know if that's actually changing it, but it shouldn't make much difference, right?

**Dave Jones:** 27.6 microamps there. And yet, 27.6 average. Where do we're talking order of magnitude lower than what we looked at in the previous video. So, yeah, this thing's pretty schmick.

**Dave Jones:** It's higher resolution. So, anyway, let's go see what we've got and see if this demo board works out of the box. Fingers crossed. Um I'm hoping it does, but you never know.

**Dave Jones:** And just a quick peep at the um STM code that we got. Looks like uh Keil. It uses the Keil uh compiler and uh firmware lib. We've got core stuff, hard uh startups, core CM3, hardware, LCD.

**Dave Jones:** There you go. We've got all our LCD stuff. Beautiful. All the commands, everything else. Yeah, it's all there. No worries, we can get started with that. Looks pretty even so simple even I can do it.

**Dave Jones:** And we got fonts. This is what we want. Wow, 24. 17 pixels wide, 24, but even like we're going to have to do a custom Oh, nice. Look, they've put even ASCII next to it.

**Dave Jones:** Is this like a um like a ST thing? Or is this their specific font? Anyway, I like how they put the actual character next to it. That's pretty good.

**Dave Jones:** Anyway, for this project we'll probably want like a custom uh you know, large because this is a high resolution display, right? This is actually even though this is a large font on this high resolution display, it's not going to look that big.

**Dave Jones:** So, we're probably going to have to do some massive um font or anything, but this gets us running. This is great. So, here's our display. It's incredibly thin. It's um yeah, basically just the uh thickness of the glass.

**Dave Jones:** We can see our interfaces at a 0.5 mm pin pitch just like we had before. It's got the protective film on it. Hang on. Here you go for you film aficionados.

**Dave Jones:** Wow, look at that. Beautiful. It's got a black surround on it, which I like. Um I presume that the display image goes right to the edge Oh, no, not maybe not.

**Dave Jones:** Maybe not. Anyway, we'll find out hopefully when we power it on. This thing is thin as. Look at that. It's absolutely There's nothing in it at all. Um yeah, so I'm super thin.

**Dave Jones:** As opposed to Here's the one that we got in the previous one. This is a 4-in jobby. So, we've got 2.9 in diagonal. Let's measure it. Are we getting the inches that we paid for?

**Dave Jones:** Oh, yeah, that's about 2.9. There you go. And this one we had was What was it? 4.1 or something. Yeah, 4.1. So, it's a bit of a monster that we had before and really, you know, thick, but it's got the backlight on there and everything.

**Dave Jones:** And this was only a 192 by 64 display. This thing is a 300 whatever by 160. Um so yeah, massive resolution difference between these and this one's are cheaper as well.

**Dave Jones:** Well, you'd expect it cuz like there's less physical physically bigger and better it's more materials to make it. I don't know. So as I said this is a fully reflective display hence well they've got the mirror on the back.

**Dave Jones:** Hi. Hi. I'm behind the camera here. And yeah, so it's a reflective back in which means you can't use a backlight. If you want to use a backlight through it you need that transflective display which this one is which combines sort of like half reflective but it also lets the light from the backlight come through as well.

**Dave Jones:** So in theory this being fully reflective it should look more betterer than this one. And it does have a more like a white mirrored finish whereas this has a like more traditional LCD greenish tinge to it.

**Dave Jones:** So yeah, I'm pretty hopeful. Should look pretty good. Anyway, here's the demo board that they presumably custom program for me but it looks absolutely the same as and it's got the same part number as that one that they supply for their e-paper displays and it's got an ESP 32 expressive ESP 32 in there.

**Dave Jones:** As you can see it's an Arduino form factor cuz they do have Arduino shields that plug on here that you can plug like various different types of e-ink displays into but they've also got this dedicated display out here.

**Dave Jones:** So I don't think this is an Arduino. Can you get an expressive Arduino? I don't know. But it but they're using the Arduino form factor I guess. Yeah, so we've got this little interface board here and it's exactly for the e-ink e-paper display USB-C on off.

**Dave Jones:** So okay, let's let's plug it in. So there's only one thing to do and let's try it out and see if they That's all the way in and see if they have programmed it for me cuz they said, "Yeah, they didn't actually have a demo board for this actual display." So, yeah, but they said they'd make it for 25 bucks.

**Dave Jones:** So, they basically did the programming for free. They just like this so cheap, 25 bucks. Anyway, let's power it on. I've got no idea what application they got programmed in there.

**Dave Jones:** I've got a little power meter here. So, well, we can't measure the in like the actual display, but we can measure the whole thing. I don't know why but why you'd want that, but anyway, let's plug it in and yeah, there we go.

**Dave Jones:** And 0.03 0.02 Oh, yeah. No? No, it's on. There we go. So, it's on. Whoa, I can see some light I can see some horizontal lines over there. I'm not sure if you're seeing that on camera, but I can see some horizontal lines.

**Dave Jones:** Uh, let's press the press the reset button. Presumably that's a reset Oh, hello. Whoa, there you go. Boom. Look at that. It's It's inverse display with Oh, a clock.

**Dave Jones:** Hello. Winner, winner, chicken dinner. Look at that. Wow, doesn't that look groovy? That is Look at that. Wow, so that's straight on. That's straight on, but we're getting some reflections off the overhead lights, which is what you're seeing there.

**Dave Jones:** Look at Look at that. Isn't that beautiful? That is very e-paper like, isn't it? And you've got to remember this is LCD. So, this is not e-ink or e-paper.

**Dave Jones:** This is LCD. Wow, that looks great. And this is higher resolution that we've got on the other one. That's a winner, winner, chicken dinner, isn't it? Wow, I'm liking that.

**Dave Jones:** Thank Thank much. Good display for programming that for me out of the box. I don't know if it does anything else. Uh what does this switch here do? Does this switch do anything?

**Dave Jones:** Uh I don't know. Maybe it does I don't know. I'd have to look at the uh uh documenta- Whoa, there you go. So, I just reset. That is a reset.

**Dave Jones:** It's not a mode thing. No, yep. Okay. So, there are Wow, oh. You see that refresh thing that came across? That was interesting. Watch this again. It starts from over here and it sweeps across.

**Dave Jones:** See it? Boom. Boom. Boom. But, you can write to the display memory in this thing. So, you can write presumably pixel by pixel or you can write into the display memory and then probably do like a page switch or something like the you know page switch maybe.

**Dave Jones:** I don't know. Haven't fully read the uh data sheet for that uh 7203 chipset or whatever it is. But, there you go. Wow. And leave me a comment down below.

**Dave Jones:** What do you think about that? Right, I'm going to power up the other display and do a direct comparison. And from the previous video, we'll just run this and there's the video Raspberry Pi and uh there's our previous display.

**Dave Jones:** I'm not going to get the other one uh because then I have to rip out all the wiring harness and everything else. So, let me see if I can get these two of these side by side.

**Dave Jones:** There we go. That's at a lower angle uh like this. Wow, there's no It even looks I'm I'm not sure unless I when I edit the video, but trust me this looks way better in person than it does on uh the screen here.

**Dave Jones:** But, anyway, so if we bring the bring it up to a higher angle, there's just It's way Look at that. It's way betterer. Just imagine that with a big font um and it looks like we do go reasonably close to the edge of the display there.

**Dave Jones:** Won't know until we uh get a full map. And you'll notice that our 4.1 in we're lying a bit there. You can see the outline of the actual visible display area there, but yeah, I'm really liking that.

**Dave Jones:** What do you think? Leave it in the comments down below. It's like chalk and cheese almost, isn't it? So yeah, this is very e-paper like, but it's not it's not e-ink or e-paper technology.

**Dave Jones:** It is an LCD. Very And like looks like based on there power graphs an order of magnitude lower power than this thing. So granted, it's smaller, but wow. Yeah, um thoughts in the comments, please, but I think we might have a winner winner chicken dinner here.

**Dave Jones:** And it's cheaper and higher res. Cool. Now, the only issue really is well, is it big enough? Like I was actually going overkill here cuz we've looked at this cuz I do want a similar form factor to these benchtop timers like this Brennan one here.

**Dave Jones:** And of course this 4.1 in over here was just like way bigger. So you know, we're adding the case and everything. That actually gets to quite a large product.

**Dave Jones:** Like with enclosure, we're talking at least like 120 mm by you know. So it's getting actually quite large. That's the same size as this one down here by the way.

**Dave Jones:** But this one here is actually the same width as the LCD in here except it looks like it actually is a bit wider cuz if you include the visible display area There you go.

**Dave Jones:** It is wider there. So yeah, that is definitely wider. And of course it's taller. So we we could have like you know, quite a large we could have a larger font than this one on there.

**Dave Jones:** And I think that it'd look pretty reasonable. And battery solution wise, you know, I'm thinking about an 18 rechargeable 18650. So this is actually uh the same width as an 18650 cell.

**Dave Jones:** So, we'll talk about that in a future video, but damn. Um yeah, I think we're just we're just going to run with that. Um it's not This is not available in They don't make it in a bigger version uh at all in the TFT uh type, but yeah, um I'm just I'm just going to run with that.

**Dave Jones:** This is where you're you can change your design based on the LCD. Like, yeah, I wanted a bigger display, but it wasn't a showstopper if I didn't get it.

**Dave Jones:** And once I found a good display, this thing's cheaper, higher resolution, order of magnitude lower power, it's just as big and slightly bigger than this. And there's nothing wrong with this.

**Dave Jones:** This is perfectly fine. I just, you know, would like significantly bigger would have been nice, but we're going to go for a little bit bigger, and it'll have uh it's like double the height there.

**Dave Jones:** So, we're going to have like two rows or three or four rows of, you know, how many timers you want and and other features and stuff like that. And that can often be the uh thing with uh designs like this.

**Dave Jones:** If you uh like write the requirements specifications down rigidly first, and then you only design your product around that, that works in a lot of cases. Fantastic. Nothing wrong with that.

**Dave Jones:** But often, um you know, you want to be a bit loosey-goosey. So, when something nice like this comes along, you go, "Ooh, yeah, that's just really sweet. I'll, you know, I'll modify my design a bit.

**Dave Jones:** I don't care if it's as big as I wanted it to be or whatever." Just to have the flexibility to be able to go, "Yeah, I'll run with that.

**Dave Jones:** Thank you very much." And then design your envelope around uh in this particular case an LCD uh for example, rather than, you know, using off-the-shelf case and have some rigid requirement for your uh displays and your interface and your user interface and things like that.

**Dave Jones:** So, if you keep things a bit loosey-goosey, um then it can be advantageous. Not always the case in uh design. Don't want you to get the wrong idea that uh you know rigid uh requirements specifications are a bad way to design, but uh especially for like you know a project where you're the one-man band doing this, then yeah, this can be a good thing.

**Dave Jones:** That is a winner-winner chicken dinner. That is the gooddisplay.com. The unfortunate uh D hidden inside the other D there, but it's yeah, gooddisplay.com. Um and we've got the STM code for it.

**Dave Jones:** Looks fantastic, so I think we've found our solution for the micro timer. What do you reckon? Thoughts and comments down below, please. And if you like a design series like this, please give it a big thumbs up.

**Dave Jones:** Um and also discuss on the EVblog forum and check out EVblog.store for all my merch. Keeps me in business. Catch you next time.
