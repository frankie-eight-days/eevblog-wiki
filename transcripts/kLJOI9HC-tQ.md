---
video_id: kLJOI9HC-tQ
title: EEVblog #3 - Static Myths, PIC Micro, Pocket Multimeter
url: https://www.youtube.com/watch?v=kLJOI9HC-tQ
source: youtube-asr
---

**Dave Jones:** Hi, I'm Dave Jones and this is the AEV blog number First up, as usual, is a book review. Now, I don't actually have a physical hard copy book this week. The reason being is that it's available online as a

**Dave Jones:** PDF book for free. Now, what I'm talking about is it's called the scientist and engineers guide to digital signal processing by Steven Smith. And it's available at the website dspguide.com. And it's available in hard copy form for those who want it.

**Dave Jones:** Regular hard copy book, about 650 odd pages or so. But, Steven's made it available on the website for free as a PDF download. You can download the individual chapters as separate PDF files or you can view them as HTML. It starts out at the

**Dave Jones:** basics, what DSP is, and goes through FFTs, discrete Fourier transforms, and and there's a whole bunch of sections on digital filtering, so all sorts of how to implement all sorts of digital filters, which is which is really handy.

**Dave Jones:** And there's lots of example code, too, and it's in regular basic. So, it just means it's easy to read and easy to translate to other languages if you need to. And it's really good. And the book's easy enough for regular

**Dave Jones:** beginners to read. It's a great introduction to DSPs. It's not really highly in-depth if you really want to know the ins and outs of DSP, but for basic applications and how to implement it, it's it's a really good read. And

**Dave Jones:** further on the book, there's all sorts of stuff on audio processing and things like that. So, there's it's it goes in really in-depth on various applications of DSPs. So, I highly recommend it. Check it out. dspguide.com.

**Dave Jones:** Now, for something that really ticks me off. Something I constantly get annoyed with and I'm constantly finding silicon bugs. These are not software bugs. These are bugs in actual silicon devices. Um a recent one I've had experience with

**Dave Jones:** is the PIC, the Microchip PIC 24F series. I use the 24 FJ64GA series device in my uh scientific calculator watch. The list of bugs in the 24F series uh device I was using is actually quite extensive and I'm going

**Dave Jones:** to have to actually read a list here. Um the brownout reset, the real-time clock, the I²C module, the UART, JTAG, uh SRAM, they got the size of the SRAM wrong. It's incredible. Uh ADC, SPI, and uh a whole bunch of core

**Dave Jones:** functions, voltage regulator stuff, and and just regular core functions. It's crazy. The list is longer than my arm. And they're up to like the fourth revision of the device or something and there's still a whole list of bugs in

**Dave Jones:** there. It's just It's just crazy. I don't know where it comes from. So, really it's worth uh checking out. Next time you go to use a new device, check out the silicon errata first. It could save you a lot of head scratching,

**Dave Jones:** really. Yes, I've changed into a anti-static lab coat. Why? Because it's myth-busting time. First myth is anti-static bags. You've seen them before, these pink things? They're designed They're supposedly anti-static. But, would you believe me if I said they're not?

**Dave Jones:** These are static dissipative. That means that they will not build up a static charge. But, they will not protect your devices at all, not one little bit, from getting zapped. If you put your devices inside one of these pink static dissipative

**Dave Jones:** bags, they're not protected at all. I can come up and zap straight through there, and your devices are goneski. Now, if you actually go to a real ESD course, um the the first thing they will actually do is actually demonstrate this

**Dave Jones:** myth to you. They will actually take an antistatic bag, and they will put a an actual receiver inside, and they will or a sensor inside, and they will zap straight through the bag, and you'll see that it does absolutely nothing. And

**Dave Jones:** then they'll do the same thing with a static shielding bag, and you'll see that it won't get through at all. And that's just a common myth, because people don't really Well, a lot of people don't really understand the basics of antistatic and

**Dave Jones:** static control. Now, what you really need is one of these static shielding bags, one of these They're actually a Mylar with a shielding impregnated thing inside a Mylar wrap. And these will actually protect your devices. If you put your device in there, you cannot

**Dave Jones:** zap through the bag, because they're static shielding, not static dissipative, static shielding. Now, that's why you'll often find uh a whole bunch of devices, they will be wrapped in an antistatic bag for basic handling on an antistatic bench, and

**Dave Jones:** then they'll go inside a static shielding bag or a static shielding box. And the same thing goes for your IC tubes as well. These are not typically static uh shielding. They are antistatic, and it says so right on the back if you can

**Dave Jones:** read it. It says antistatic, which is static dissipative. It means the same thing. Antistatic is static dissipative. It won't build up a charge. But, I can zap that chip straight through that tube, and it's totally destroyed. So, that's why

**Dave Jones:** um these tubes must come in a static shielding bag. And uh for the ultra paranoid, the static shielding bag will come inside a static shielded box as well. And really, um unless you're If you want to uh use

**Dave Jones:** ESD If you want to treat ESD seriously, um you really shouldn't be uh playing with these You shouldn't take anything out of a static shielding bag unless you're at a static approved workstation. Cuz if you do, you can zap them.

**Dave Jones:** Soon as you take them out of the bag, right through the tube. Nasty. Now, it's time for an equipment review. This seems to be everyone's favorite part of the blog. People just can't get enough of gear reviews. So,

**Dave Jones:** all that new stuff from the manufacturers that uh has been promised, it's all still in the mail. So, you know, I'm going to have to uh just review something on hand again this week. Once again, it's of interest to

**Dave Jones:** electronics engineers. This week, I've chosen the pocket multimeter. Ta-da! Now, this one is a Wavetek DM78A. Uh I've had it for I don't know, maybe 8 10 years or something like that. It's um reasonably old. I've got quite a few of

**Dave Jones:** them. Um I use them uh I've got them in tool boxes at work, in little tool pouches, things like that. They're great to put in the car glove box. Just handy to have in your desk at work. Just just for when you need it. Now,

**Dave Jones:** there's many of them on the market, but um this is this is the one I like and prefer. It's got the vinyl wallet, fold over type wallet with the fully attached test probes. And that's what really makes a good pocket multimeter.

**Dave Jones:** There's nothing worse than losing your probes. Um so really you need one with the attached probes. There are others that have the probes which actually wrap around the outside and things like that and they're not really as good. Um I

**Dave Jones:** much prefer these. They fold up in a little Velcro the probes fold up in a little Velcro attachment there. And it just folds over, you can put it in your pocket, fits in your back pocket real easy. And they're just really handy.

**Dave Jones:** They range anywhere from 2% to .5% accurate. So you can get reasonably accurate ones. Um and there's many more on the market these days. This is the this is the traditional model, but there's ones that have capacitance test and frequency test and

**Dave Jones:** they're really quite handy. I have never seen a manual ranging one. They're all auto ranging usually 3200 count or something like that. And they're just really handy. I think everyone should really have one of these pocket multimeters or two or three. And

**Dave Jones:** you can get them quite cheap. You can get them on eBay and various stores and things like that. And you get them for as little as $10 or something like that these days. But some of the really good ones you can

**Dave Jones:** pay upwards of you know 80 to $100 or something like that. So I don't think they're worth that much. But um, you should have a couple of these cheap ones around, and they're just so darn handy, and it's pretty much

**Dave Jones:** all you need for basic everyday use. Check them out, the pocket multimeter.
