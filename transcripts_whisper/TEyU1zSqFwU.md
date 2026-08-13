---
video_id: TEyU1zSqFwU
title: EEVblog #883 - Orange Pi One vs Raspberry Pi 2
url: https://www.youtube.com/watch?v=TEyU1zSqFwU
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 20, "2": 40, "3": 55, "4": 79, "5": 93, "6": 107, "7": 128, "8": 146, "9": 169, "10": 186, "11": 205, "12": 221, "13": 236, "14": 253, "15": 271, "16": 288, "17": 308, "18": 325, "19": 341, "20": 359, "21": 373, "22": 392, "23": 407, "24": 424, "25": 441, "26": 458, "27": 475, "28": 494, "29": 509, "30": 525, "31": 546, "32": 566, "33": 582, "34": 595, "35": 610, "36": 623, "37": 637, "38": 657, "39": 672, "40": 692, "41": 711, "42": 729, "43": 745, "44": 759, "45": 779, "46": 802, "47": 827, "48": 847, "49": 866, "50": 883, "51": 902, "52": 923, "53": 941, "54": 962, "55": 978, "56": 996, "57": 1010, "58": 1024, "59": 1039, "60": 1054, "61": 1073, "62": 1088, "63": 1101}
---

**Dave Jones:** Hi! I thought we'd check out the new Orange Pi 1. What is it? Well, it's a $10 Raspberry Pi equivalent board. Yes, $10. Unbelievable. Now, I know you can get the Raspberry Pi 0 for $5, half the cost of this new Orange Pi 1.

**Dave Jones:** But the remarkable thing about this Orange Pi 1 is that not only is it $10, but it basically is more powerful than the Raspberry Pi 2. Now, if you actually compare this to the Raspberry Pi 0, there's basically no contest. The Raspberry Pi 0 is a single-core ARM Cortex-A7 running at 1 gig.

**Dave Jones:** But this thing uses the all-winner H3 chipset, which we'll take a look at. The ARM Cortex-A7 has got four cores in there, running at 1.2 gig. Now, a fairer comparison here would actually be between the Orange Pi PC, it's called, not the Orange Pi 1 we're looking at here.

**Dave Jones:** It's a $15 board instead of a $10 board, and it's more compatible with the Raspberry Pi 2 in terms of form factor and feature set. But in this case, as you can see, the Orange Pi PC has a four-core ARM Cortex-A7, but it runs at 1.6 gig instead of the 900 megahertz that the Raspberry Pi 2 works at.

**Dave Jones:** So, much more powerful. And the Orange Pi PC has a couple of little extras, like an IR receiver there, and it's got a microphone built in, but unfortunately, just like the Orange Pi 1, one of the big downsides, you can't actually power it from a USB connector.

**Dave Jones:** You've got to power it from the DC power jack, and it's got one less USB 2 connector. Raspberry Pi has four, the Orange Pi PC has three. But, you know, both got 100 meg ethernet, they've both got 1 gig of RAM on them,

**Dave Jones:** so, you know, and a camera interface. But in terms of bang-per-puck, it's no contest, really. The Orange Pi wins hands down. $15 versus $35. No worries. And it's not quite as small as the Raspberry Pi 0, but it's pretty close. And if you actually compare it with the Raspberry Pi 2, then take a look at how small this thing is.

**Dave Jones:** It's absolutely incredible what you can get for $10, and this thing is chock-a-block. As I said, the all-winner H3 ARM Cortex-A7 processor, and it's got a GPU in there that it's capable of playing H.265 4K video at 30 frames per second. Absolutely incredible.

**Dave Jones:** It's got 512 meg of DDR3 RAM in there, which is half that on the Raspberry Pi 2, but the Orange Pi PC actually has 1 gig on there. We've got our regular microSD card, we've got our regular HDMI output, we've got USB on the go, we've got a little UART pin header here.

**Dave Jones:** But unfortunately, you cannot power this board through the USB connector. Unfortunately, you've got to power it through this little mini DC jack here, and that's really annoying, it's not your more standard 2.5mm size one. Unfortunately, a little reset switch on the side here,

**Dave Jones:** and we've got ourselves the camera connector on the bottom here. But apart from that, it's basically a Raspberry Pi 2, shrunk down into a smaller form factor with a more powerful processor, more powerful GPU. And it's got a 100 meg Ethernet port, which is reasonable, but a huge downside,

**Dave Jones:** only one USB 2.0 port, but hey, given the size of it, eh. Now one major thing to be aware of here, the 40-pin HAT connector, pin-compatible of course, but what they've done on the Orange Pi 1 is they've actually rotated it 180 degrees.

**Dave Jones:** So pin 1 is actually here, as opposed to the Raspberry Pi, whereas pin 1 is over here. And that's obvious, because if you've got a board, if you've got a HAT board that plugs in there, it's not being found by these connectors, but this one, of course the USB and the Ethernet are there,

**Dave Jones:** so you can't just plug the board directly on. So they've rotated it around like that, so you'd actually have, or your plug-in HATs would actually go in that direction like that. Just be aware of that. But that 180 degrees modification does not exist on the Orange Pi PC.

**Dave Jones:** Orange Pi PC is exactly the same as the Raspberry Pi 2. Now these Orange Pis come from a Chinese company called the Shenzhen Zunlong Software Company, and you can only buy them on AliExpress at the moment anyway. And here's the one we're looking at, the Orange Pi 1, and it's only $10,

**Dave Jones:** and as I said, the Orange Pi PC, that's $15. And these are the different models that they have on the website here, and they actually sell one that is not listed here, because it's very new. It's actually called the Orange Pi Lite, and you might have seen that on the box that we had there.

**Dave Jones:** It was the same. Now, the Orange Pi Lite is the same as the Orange Pi 1, except it has a Wi-Fi chipset instead of the Ethernet. So you can see the antenna connector there, and that one's only $12. Complete with Wi-Fi, and it's got two USB connectors on it, but it's got HDMI.

**Dave Jones:** The whole works. It's got the 4-core 1.2-gig processor. The whole works. Unbelievable! $12! But just bear in mind, you buy the board for $10. It does not come with the microSD card or the power supply, so you've got to supply those to get it up and running.

**Dave Jones:** Now one big differentiator with the Orange Pi is that it is actually open source, whereas the Raspberry Pi, closed source, uses the Broadcom processor. And of course, the Broadcom processor used on the Raspberry Pi 2, famously, can't get the datasheet for it. You've got to sign an NDA and all that sort of crap.

**Dave Jones:** But with the Allwinner H3 chipset here, they're both ARM Cortex-A7, by the way, so the same ARM Cortex, except the Allwinner A3 is actually a faster processor. But you can get, like, the full, like, 500-something, 600-page datasheet or something. Crazy. I'll link it in down below.

**Dave Jones:** Now if you take a look at the Orange Pi website, very briefly, it looks kind of impressive at the top surface, but that's pretty much where it stops. I've found a lot of issues with this thing, trying to set it up, and the support and things like that.

**Dave Jones:** There's just information missing and all sorts of stuff. The Raspberry Pi is just a much better platform. If you're a beginner looking to set these things up, no contest whatsoever. Raspberry Pi is the winner. But if you're after a low-cost board, then definitely the Orange Pi offers the best bang-per-buck.

**Dave Jones:** Now, if we have a look at the builds here, these are the different types. You can see that the Orange Pi 1 board here only has an Android build. That's it. It does not have a Linux build available for it, but I'll show you an alternative to that later.

**Dave Jones:** Whereas the Orange Pi Plus 2 and the Orange Pi Plus, which are different older versions, it's got a version of Raspbian here, but it's old. Look, from the 6th of June 2015. So it's like, you know, almost a year old. And that's the other thing.

**Dave Jones:** They actually claim that this is compatible and can run the Raspberry Pi image. But that's complete BS. It does not. You can't just get the Raspbian image and put on the... or swap SD cards between the Raspberry Pi and the Orange Pi 1.

**Dave Jones:** The chipsets are different, and even though they use the same ARM Cortex-A7 processor, they're different, they're not compatible, you need a different build. So that's just... that's just BS. And all sorts of stuff is missing and, like, out of date or whatever, not up to date on their website, so just be careful of that.

**Dave Jones:** You might actually struggle, especially with the newer Orange Pi 1 that we're actually playing with here. And if we go into the resources, and we go into the download, and we actually go and download the Android OS for this thing, you'll know that here's the actual thing where we're downloading Sun 8 IW or whatever,

**Dave Jones:** and the Google Drive link does not work, and if you go into the HTML source for this page, it actually... you can find a link to it, and it's the wrong version. It's a BananaPi build, it's crazy. And then if you hit this Baidu cloud, it takes you to some weird-ass Chinese website,

**Dave Jones:** which is auto-translated by Google, which then gets flagged by Google as, like, a security threat, and things like that. And you've got to override the security settings in Chrome, for example, before you can download it. And I couldn't download it with the other browsers.

**Dave Jones:** Complete pain in the butt. But I don't recommend you run that Android OS, because there's famously a very big security flaw in this thing, which made all the news recently, I'm not sure if they've actually fixed it yet, but the Android build of this thing from Allwinner CPU,

**Dave Jones:** they actually tell you this down here. Look, it's the OrangePi and the BananaPi boards as well that use these Allwinner chipsets. That massive security threat. There's a backdoor you can get in, and it's a root thing. I don't know the technical details. So I don't recommend you use that, but what I'm going to use today is Armbian,

**Dave Jones:** which is an Arm build, an Arm Debian build for the OrangePi 1. So they've gone to the trouble to actually specifically do the desktop and the server version of the Jessie Debian build. Fantastic. And I'm pretty sure that this Armbian build does not have that security threat in it.

**Dave Jones:** But I stand to be corrected, but I'm pretty sure it doesn't. They've fixed it. So what I'm going to do today is install the Armbian build, the Jessie desktop version here. So you just download. It's a .raw file. You can use the Win32 disk imager or an equivalent on Linux or whatever machine you use

**Dave Jones:** to actually write your image to the SD card, and then it should just boot. So ironically, I had to go to a third-party build here to actually get this thing working because the OrangePi builds and website just don't cut it. The support's not there.

**Dave Jones:** There is a forum, but it's not hugely active yet because these are relatively new boards, but you can get help there. But yeah, they need to do a lot of refinement to their website and just having the builds available that actually work. It's just crazy.

**Dave Jones:** Okay, so I've copied that image over, and then you boot it up, and it's going to take quite a few minutes to get to this stage, but this is only on the first time. And then you've got a login prompt here, and you actually have to log in as root,

**Dave Jones:** and then your password is 1234 for the build. So yeah, we're in like Flynn. We're required to change it. So I don't know what all these errors mean, but it works in the end, and it's got to initialize this thing. It only needs to do this once.

**Dave Jones:** Once you do that, then the build will automatically go straight into the desktop. So it'll ask you to reset your password. Once you've done that, it'll go in and set up all the GUI for you. So it says OrangePi 2 Mini, but this is actually a specific build for the OrangePi 1.

**Dave Jones:** I'm not sure how different they are. They could even be identical, but the name of this PC will actually be OrangePi 1, so they must have tweaked it in some way. And then we choose a username, so EEVBlog, and then it asks you some other rubbish.

**Dave Jones:** Yeah, whatever. And we're in like Flynn. Check it out. Here we go. Here's our application. We've got our web browser. Everything's hunky-dory. All of our tools are in there. It's installed LibreOffice and all the regular stuff, so terrific. And it works a treat.

**Dave Jones:** What a bobby dazzler. Ooh, zero YouTube subscribers. Yeah, bug there. I've got to fix that. And yes, it runs Boink, exactly like the Raspberry Pi 2. No different whatsoever. It just works an absolute treat. I've done a separate video on this if you want to know how to get it up and running,

**Dave Jones:** and I'm doing SETI at home processing on this thing, and that's why I want this cheap Orange Pi 1, because I'm going to build a supercomputer cluster with them to do this. So, beauty. And we can actually install some benchmarking software here, so I'll just use the command here inside the root terminal.

**Dave Jones:** So we'll install the Sysbench software, and then bingo, we're in like Flynn, and then we can actually run some benchmarking. So we can actually run different types of tests. You can see that we've got CPU, memory, threads, and other stuff, so we can actually run the CPU test.

**Dave Jones:** And I won't bore you with all the details, but we can set the number of threads here, and we can, oops, we've got to put run on the end of that. So I've also installed Sysbench here on the Raspberry Pi, and we'll run that, and we'll get some benchmark figures between the two.

**Dave Jones:** And it takes about two watts there, just sitting idle, doing absolutely nothing on the Arbian desktop. And as a comparison, the Raspberry Pi 2, just sitting there running Raspbian, doing nothing on the desktop. About 1.8 watts. This is running all four cores on the SETI processor at 100%.

**Dave Jones:** Around about, oh, let's call it 3.7 watts or thereabouts. Ooh, smoking. So this poor little A-winner processor's going to get pretty hot. How hot? Well, let's check it out. Here we go. We're looking at, it can get up to 85, 90, 91! Wow!

**Dave Jones:** It can get up to 90 degrees. That really risks shutting this processor down. Wow, that is crazy hot. Definitely need a heatsink with this. And running full tilt, boink, with all four cores at 100%, the Raspberry Pi 2, about 2.5, 2.6 watts. And if we have a look at the benchmark figures for all four cores there,

**Dave Jones:** the orange one is obviously the Orange Pi 1, and you can see it's significantly faster there on either 1, 2, 3, or 4 cores. On 2, 3, and 4 cores, it's about 1.85 times faster. Whoa! But if the Raspberry Pi 2, which draws 2.5 watts full tilt,

**Dave Jones:** actually got the same performance as the Orange Pi, then it would need 4.5 watts. But the Orange Pi 1 only takes 3.5 watts with all four cores pumping. So it's actually about 28, maybe 30% better in terms of MIPS per watt. So if you're looking to run a supercomputer cluster of these things,

**Dave Jones:** then obviously the Orange Pi 1 wins hands down all the orange, whatever flavor of Orange Pi. The all-winner processor, far superior, and this could even be better with the all-winner PC, which is 1.6 gig core as opposed to 1.2 gig core we're looking at here

**Dave Jones:** with the Orange Pi 1. So not only is it better bang-per-buck, but it's more efficient too. Winner. All-winner. And the memory on the Orange Pi 1, 58% faster than the Raspberry Pi 2. It does do the memory benchmark on 10 gig worth of 1K blocks,

**Dave Jones:** 7.1 seconds as opposed to 17.2 seconds on the Raspberry Pi 2. Beauty. So there you have it. That's a quick look at the Orange Pi 1, and it's much better bang-per-buck performance per watt than the Raspberry Pi 2. And for $10, it's absolutely amazing the value you get with this,

**Dave Jones:** but it has its downsides. The software builds are terrible, and the website's almost terrible, but hey, it's open source versus non-open source. It's cheap. It's only $10. If you're a beginner and you want the best experience possible, just stick with the Raspberry Pi.

**Dave Jones:** But if you're doing something like I'm going to do, which is build a supercomputer cluster with these things, and price and performance per watt matters, then definitely the Orange Pi with the all-winner H3 processor is an all-winner. I love it. It's just a shame it's not nearly as polished as the Raspberry Pi,

**Dave Jones:** but hey, for the price, it's hard to beat. But yeah, only if you know what you're doing. And you can run pretty much anything on this thing. You can run Android, of course, but as I said, there's a security exploit in that, so be very careful.

**Dave Jones:** But you can run. You can probably run Raspbian build if you want to run Ubuntu or whatever, but I ran Debian or Armbian, no problems whatsoever. They've already compiled this. The Jessie desktop works. You can get a light server version, and it works just great.

**Dave Jones:** So yes, it has its good points and its bad points, so weigh those up if you're looking to buy this sort of thing. If you're looking to run video, I didn't run any video tests here, but I've heard that it runs 4K video 30 frames per second seamlessly.

**Dave Jones:** You can't do that on the Raspberry Pi, so if you're looking to use it as a media center or something like that, playing back video, then it's a much better solution. But make sure you put a heatsink on the thing, because this thing, I've also read that it can actually shut down.

**Dave Jones:** The processor can shut itself down or maybe even destroy itself if you tax it like that. So definitely get a stick on heatsink. I don't know how well they're going to perform. I haven't actually measured that yet, but definitely do that if you're going to play around with this thing.

**Dave Jones:** So there you go. Oh, by the way, AliExpress, buying this thing only on AliExpress was a pain in the butt. I had to try four times, and my credit card was rejected like three times. On the fourth attempt, I finally was able to order these things

**Dave Jones:** through Alipay, and it's a pain in the butt. Anyway, that's the only way you can get it, but for $10 and $3.60 postage to Australia, it's a winner. It really is amazing what you can get these days. Unbelievable. Anyway, if you want to discuss it, links down below,

**Dave Jones:** all that sort of stuff. I hope you enjoyed it. Catch you next time. Hi. How many of you have one of these lying around? A Raspberry Pi, be it an original Raspberry Pi, Raspberry Pi 2 like I've got here, or whatever the latest flavor is.

**Dave Jones:** I bet there's a lot of people out there who bought one of these things because, hey, it's a cool little Linux computer, you know, and it's super duper cheap. Hmm, I've got a couple of these lying around the lab. What can I do with them?

**Dave Jones:** Can I do anything useful? You know, let's look for aliens. Why? Because aliens.
