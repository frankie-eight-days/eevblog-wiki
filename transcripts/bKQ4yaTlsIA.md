---
video_id: bKQ4yaTlsIA
title: EEVblog #23 - GSM mobile phone audio design
url: https://www.youtube.com/watch?v=bKQ4yaTlsIA
source: youtube-asr
timestamps: {"0": 0, "1": 17, "2": 35, "3": 51, "4": 69, "5": 85, "6": 101, "7": 120, "8": 139, "9": 159, "10": 179, "11": 196, "12": 213, "13": 235, "14": 252, "15": 264, "16": 275, "17": 287, "18": 304, "19": 321, "20": 334, "21": 346, "22": 358, "23": 370, "24": 385, "25": 397, "26": 412, "27": 429, "28": 444, "29": 466, "30": 480, "31": 498, "32": 512, "33": 536, "34": 551, "35": 569, "36": 579}
---

**Dave Jones:** Hi, welcome to the EE blog. I'm your host, Dave Jones, and this is episode number 23. Uh just a couple of weeks back I was um working on uh the front end for for the design of a uh GSM um mobile phone. It

**Dave Jones:** was actually a GSM uh GPS uh as well and also Bluetooth. And um I've got some I've got an interesting story about the uh prototyping for that project. Uh we thought we would prototype the um audio front end because um

**Dave Jones:** the audio uh the uh headset, which you know, drives the uh audio in a phone, like this one, um can be a major design problem with uh GSM phones. And and it's it's a notorious problem. And you've almost certainly come across it

**Dave Jones:** yourself. I'll see if I can actually demonstrate it here, shall we? Let's give it a go. I'll um I've got my mobile phone. I'll um dial my home phone here. Here we go. And I'll answer it. What a GSM mobile phone does is it

**Dave Jones:** actually uh sends and receives in um uh packets at a predetermined rate. And um so what it does is it um it it generates um you know, these RF bursts and current uh draw bursts from your power supply if you're actually

**Dave Jones:** designing the chipset itself. So there's two separate uh issues here, really. One is the uh power supply current surge from the um GSM chip or the GSM module you're actually using. That's um you know, that's a problem for the actual

**Dave Jones:** GSM uh circuit designer. And um the other problem is um RF, which um which you know, the massive RF field, which can get into nearby products. Um or it can sneak back via the um uh antenna back into its own product.

**Dave Jones:** So, the RF energy from the antenna can sneak back into your actual GSM phone which you're designing. So, there's two separate issues. So, let's look at the current draw for a GSM phone looks like this. If If this is

**Dave Jones:** current, okay, this is I, okay, it'll have um the GPS module will have a level which is quiescent current and then it will actually draw bursts like it will actually draw bursts of current like this at a fixed

**Dave Jones:** predetermined rate. And this is transmitting and this is receiving. It doesn't require as much um uh current usually to actually receive. So, and this is at a repetition rate of 217 Hz. And this 217 Hz is the magic figure

**Dave Jones:** that you have to worry about for a GSM um mobile phones. We thought we'd just prototype the headphone amp to see what issues we had and and it proved quite valuable at and see what performance we could get using you know it really best

**Dave Jones:** type construction techniques, low noise construction techniques and and see what we could get. So, I built this little sucker and this could take some focusing but I built this and it looks really really ugly but it's it's it's not.

**Dave Jones:** There's There's quite This is actually quite a good and well-known technique for building you know really tightly coupled low noise circuit. You get some copper clad board Uh, like this and you put your and and your wire components on there point-to-point.

**Dave Jones:** It's called point-to-point construction technique, but it's also called a dead bug construction technique. Um, and I'll explain why. Tiny QFN package, and you actually turn it upside down on your This is your blank copper clad board, and you actually um and what you do

**Dave Jones:** beforehand is you actually cut in um little isolated pads into your copper clad board, but there's many different ways to do it, but this is how I did this particular one. Anyway, you turn your chip upside down, you apply some

**Dave Jones:** glue, and you stick it on your board. So, so it's like a bug, and it's you turn it upside down, it's a dead bug. So, the leads are sticking up. Except this one didn't actually have leads, it just had tiny little pads on the bottom,

**Dave Jones:** but it makes no difference whether it's a SO package or something like that. Direct very short wires straight to your ground plane. So, this is your ground plane right under the chip, and you can actually wire things straight on. And

**Dave Jones:** you can actually The good thing is is that you can actually turn components um on their end like this. You can actually uh turn components like this, and you know, solder directly on there, and it creates very, very tight um

**Dave Jones:** loops, you know? They're The actual um current loops in there, the actual ground power and ground loops are incredibly small, and they can be smaller than what you would get on a purpose-designed um board sometimes. So, it's it's really good. you to have a big

**Dave Jones:** ground plane right under the chip on the top and the bottom of the board because the board will be double-sided, and you can have a ground plane on the bottom side as well, and you can actually strap the top and bottom ground planes, and

**Dave Jones:** and you can do all sorts of things. And then you run little point-to-point wires everywhere, but the idea is that you can really get some low noise really good low noise construction out of these things, and I'll show a couple of um

**Dave Jones:** photos as well of the I did uh a few different prototypes. That's the technique. Now, what did we get with this little thing? You know, I was you know, I was quite proud I built this little thing and you know, I was all

**Dave Jones:** that you know, it's properly decoupled and and it's got a voltage regulator on there really tightly coupled and and all sorts of things and it's it's really designed nicely. You couldn't get much better. And we found this was it

**Dave Jones:** performed horribly. You would still get when the mobile phone came within cooee of this thing or this is the headphone socket. You plug your headphones in. If you put your phone anywhere near the headphones plugged into this, you would

**Dave Jones:** pick up that garbage that we heard before. You would pick up that 217 hertz and its harmonics and and all sorts of horrible artifacts. Now, this is a real problem because if you've got an amp like this, if you've

**Dave Jones:** got you know, your headphone driver amp and it's going out here and it's driving your you know, it's driving your set of headphones and you've got input and you've got power. Okay, and you got ground. Now, RF is a horrible thing. RF

**Dave Jones:** can sneak in anywhere. It's really horrible stuff. Now, um not only can it sneak in at the from the headphone leads here, it can sneak into the input of course and it can also sneak in via the ground system and it

**Dave Jones:** can also sneak in via the power as well. Power and ground input and output. You screwed all sorts of ways, but it can also and this is one of the things it can also sneak directly into the silicon

**Dave Jones:** die itself. It can get in there and you've got to remember that at at RF every PN junction, every diode is a potential RF detector. It's going 800 900 megahertz Um, and also um, 1800 MHz, as well. Okay, you have to try and put

**Dave Jones:** in RF traps to actually reduce this. So, we would put in our little RF traps, and we'd put in a couple of caps to ground on the And we do this not only here, um, on the output, but we do it on each

**Dave Jones:** rail, and we do it on the input, and like right at the chip, using this, you know, low noise using this very tightly coupled construction technique. We We put these recommended RF traps. It's 33 pF and 10 pF to this chip. It was an,

**Dave Jones:** um, LM, um, 4809. And, um, no matter And no matter what we did to it, we just we just could not get rid of the problem. It was always there. So, to get rid of the problem, we had to

**Dave Jones:** resort to a specially designed, um, RF-immune headphone amplifier. And it's the, uh, the Maxim 9724. And this is, um, a specially designed and laid out, um, chip that's immune to, um, RF, uh, interference. And, um, specifically for use in GSM mobile phones. It's

**Dave Jones:** purpose-designed. And we And we got this chip. We got some samples, and we tried it out, and, lo and behold, it worked perfectly with nothing more than a single bypass cap. That's all it needed. It was amazing. And no RF filtering at

**Dave Jones:** all. Uh, no low-dropout regulator on the input. And, you know, nothing. We couldn't believe it. It just worked. So, there you go. You know, next time you're doing something critical like this, remember about RF immunity, and, um, cuz it can be a real problem. And a

**Dave Jones:** great test for your product, actually, after you've designed your product, a really good test is to get your mobile phone and put it near, you know, put it make it ring, and put it all over the board and see what happens to your

**Dave Jones:** board. Is your next product capable of passing the mobile phone test? Give it a go. It's a really, you know, neat test to see how immune uh your product is to high levels of RF energy. So, give it a go next time.
