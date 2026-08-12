---
video_id: 7iXwRlGDLmI
title: EEVblog #1190 - Mailbag Review Bonanza
url: https://www.youtube.com/watch?v=7iXwRlGDLmI
source: youtube-asr
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. Let's get into it. Thank you very much Christine Coronado from Labjack Corporation in the United States of America. I'm sure we've had Labjack before, right? Oh, well spoiler alert. There you go. I've no

**Dave Jones:** idea what it kind of is though. I'm sure we've had Labjack on here before. Anyway, they're from Lakewood, Colorado. I know all my viewers in Lakewood, Colorado. There's a few in Colorado. Had a few mailbags from Colorado. Let's have a look.

**Dave Jones:** We have a note. Labjack, "Hi Dave, big fan of your show since going to college and watching your fundamentals Fridays. I've been working as an engineer at Labjack for 10 years now." Been watching since the beginning, have you? It's almost 10 years in April. I

**Dave Jones:** think April 4th is the official EVBlog anniversary. Anyway, finally been able to convince some of my coworkers that it'd be a good idea to send you one about. I'm sure Labjack have sent something in before. I should I should have sworn. Anyway,

**Dave Jones:** got obligatory stickers and a stationary bottle opener. What is a stationary bottle opener? Oh, I get it why it's called a stationary bottle opener cuz it's come with comes with screws and you map map I standing on bubble wrap.

**Dave Jones:** And you screw it into a wall and then you Oh. Glass, very nice. Thank you very much. Tool holder. Cuz I don't I assume that looks like a beer glass, right? I don't drink beer but oh, got a t-shirt. Thank you very

**Dave Jones:** much Labjack. Check it out. By the way, medium or small, none of this large rubbish if you are going to send in a shirt, especially none of those large American large which is like It's practically a dress here in

**Dave Jones:** Australia. Anyway, um so what have we got? LabJack T7 Pro. I have no idea what a T7 Pro is. Got one of the ever useful the screwdrivery pocket things that go in your pocket. Cool. And this looks like

**Dave Jones:** some sort of That looks like a PLC kind of thing. So So, let's check it out. Oh, well. Wow, you don't see the big ass D connectors like that anymore. Old school. Oh, and they sent the correct USB. None of this Yankee rubbish. They

**Dave Jones:** sent an Aussie one. Unfortunately, it's not compliant. Check it out. It does not have the insulation on the pins. That is technical technically illegal here in Australia. I don't know how it got cut past customs. Anyway, she'll be right. So, what we've

**Dave Jones:** got here is an industrial DAC device or data acquisition device and it contains DACs and ADCs and all sorts of stuff it just like you'd get like the National Instruments cards a classic DAC cards. For example, this one is not only USB

**Dave Jones:** Ethernet but it's got Wi-Fi as well obviously. So, it's a Wi-Fi DAC thing 429 Yankee bucks which might sound expensive but for a professional data acquisition device it's peanuts really and it looks quite the part. I like it. And here's some more detail on

**Dave Jones:** that. I can leave you to read it but it's got a modbus so that can be integrated with larger SCADA systems and things like that. So, it's great for load cells RTDs thermocouples and all the business and if we have a look at

**Dave Jones:** some of the specs here, it's pretty impressive 14 analog inputs 16 to 24 bits depending on speed and device type. Excellent expand to 84 analog inputs when you actually max them all together. Uh 16-bit ADC up to 100 K samples per

**Dave Jones:** second or the pro is actually 24-bit low ADC as low as 1 microvolt noise noise free. Is there what they're talking about when they talk about noise free is the uh least significant there's no noise on the least significant bit or last couple

**Dave Jones:** of least significant bits, I guess, but jeez, that's an ask. Um software configurable resolution single-ended or differential input fantastic and sometimes you need differential analog input ranges handy plus minus 10 and 1 and 0.1 and 10 mV ranges as well. Wow,

**Dave Jones:** killer. Low latency sampling and control less than 1 ms, beautiful. It seems to have all the business 12-bit uh DACs as well. It's really quite a professional uh feature set for a DAC system. Yeah, terrific. High-speed counters and

**Dave Jones:** quadrature inputs and like PWM outputs. Wow, it's got everything. Fixed current outputs as well. 200 microamps, 10 microamps. Wow, take a squeeze inside. I'll just get the Wi-Fi antenna out of the way. And there we go. That looks pretty jazzy. There's a lot

**Dave Jones:** involved in there. PIC32 processor. Let's have a look on the bottom. Got real-time clock, of course, that hints the battery. Uh this is rev 1.35. Jeez, they've been through a few revisions, of course, which you'd expect. Looks like

**Dave Jones:** that's some sort of protection job in there perhaps right near the input. But uh yeah, yeah, on these sorts of things protection's a big uh deal as well. Looks like they're like got lots of series resistors in there. Looks like they're doing the

**Dave Jones:** business. So yeah, PIC32 processor upside down, so all the electrons are going to fall out. Then we've got our Wi-Fi module. I don't think I recognize that particular one. Anyway, that's likely our programming header for our uh PIC32 micro.

**Dave Jones:** For those who want to see exactly what model that one is. There you go. I won't go through in detail and read all the uh part numbers or whatnot. Oh, we got a Did that go to the outside? The little

**Dave Jones:** micro SD card there? Probably. Can we update the uh firmware? Does it got a remote boot loader? Anyway, it looks like there's lots of ADC and DAC stuff happening around there. I won't go into a huge amount of detail trying to

**Dave Jones:** get these parts, but you can have a look. AD7190 there. And yeah, the other ones the can't decode them properly. Bit of a pain in the butt. DG series, that'll be a uh mux switch thingamabob. Another couple of DG series muxes, stuff like

**Dave Jones:** that. Looks like you got all your requisite uh some diode protection on the input, clamping. There's our pick. More clamping, more clamping, more clamping. Ethernet chipset. Well, that's a tidy little array, isn't it? What are they doing there? And

**Dave Jones:** double-sided load cuz they really couldn't fit everything on the one side. It would have made it uh significantly larger. All sorts of fused inputs. So, I'm sure they've got all the requisite protection on this thing. No worries. Don't you hate lead-free

**Dave Jones:** solder and how they look like Frosty the Snowman there, but there's nothing wrong with those joints. It's just It's just lead-free solder. So, the hardware looks quite nice and I'm sure a lot of work and uh revision has uh refinement spit and polish has

**Dave Jones:** gone into getting that down. It's in a nice form factor, but uh it's for this sort of thing. It's all about the software. So, let's just fire it up and uh see what's what. And you get a calibration certificate. Beautiful. Like

**Dave Jones:** You've got to specify a temperature to what? Two decimal places. No worries. And uh yeah, they use some uh HP uh benchtop DMM and and a calibrator. That's like great. That it should keep the uh QA department happy. All right, so let's

**Dave Jones:** install the software for this thing, which I already actually have. I've uh just downloaded install the software downloaded that no problems. I connected it it connected up no problems whatsoever. We've got the LEDs on there and then we run this Kiplin thing. By

**Dave Jones:** the way, it uses the National Instruments uh drivers and whatnot. And then we run this Kiplin thing and there we go, scan USB, Ethernet, Wi-Fi. I'm not going to bother hooking it up to Wi-Fi at the moment. I'm sure sure it

**Dave Jones:** works, but there we go. It's found it. Just bam, straight off the bat. So, let's go run the uh application software. And there's a log and there's a stream. So, oh, here it is. Hang on. Okay, I just had to type in a file name and

**Dave Jones:** there it is and we're logging. Wow, look at that. There was an initial uh amplitude. Right, so they're right down at must be in bipolar mode cuz it uh and number of channels can we just go up? We can just increase our number of

**Dave Jones:** channels. Yep. Terrific. Why we're choosing four? There we go. I can just turn them off and on. That's great. I've got no signals fed in at the moment, so you know, I I know doubt it works. Um sampling interval.

**Dave Jones:** So, can you go down to like 1 ms or something like that? Yep, number of iterations. There it goes. Fantic graph history, change working directory, all that sort of stuff. Read you can write to file. You can just go can we just Yep, cuz I

**Dave Jones:** put in a file name before it asked you that when you load up and sure it's Is it I guess it's automatically saving that, is it? Huh. And anyway, most of those analog inputs would be on the D connectors, of

**Dave Jones:** course. I haven't looked at the pin outs or anything like that. You've got your other stuff here like your current outputs and things like that. So, anyway, can we like zoom in? How do we zoom in? We can't zoom in.

**Dave Jones:** This is very Ah, see. Yeah, this is like it's written in LabVIEW or whatever or LabWindows/CVI. I I used to write in LabWindows/CVI. I've done lots of automation. Uh lots of production test system auto automation in LabWindows/CVI. And it's

**Dave Jones:** like it's giving you the screen like like Just a big window pane. That's a bit Come on, we need to fix that. I'm sure there's a way to fix that. That's a bit amateur hour. So, yeah, this is all

**Dave Jones:** standard like LabVIEW type windows and graphs, but we can't seem to resize that, and I can't I can't zoom or pan or do Oh, here we go. Okay, right click and auto scale X, auto scale Y. It's not really auto scaling, is it? If

**Dave Jones:** it it should be like down It should be should zoom in. Oh, cuz we're not on the right range. How do we change our range? Scaling equations, you can put the equations in. That's nice. But I don't see a place to set up, not in here

**Dave Jones:** anyway, to set up your analog inputs, to change your range and stuff like that. It's purely just a login program. Okay, there's this other thing called stream, and it's going really slowly, maybe because I'm sampling over here, perhaps.

**Dave Jones:** Once a second or something like that, it'll come good. No, see? It's really jerky. I can't have both of these running at the same time. Wow, that's a bit clunky. I can't even Oh, I've got to See, can't even shut

**Dave Jones:** down the window. You've got to use the exit over here. This is like real old school LabVIEW LabVIEW stuff. And you can start stream. So, I'm not sure what the difference between log and stream is. It's popped up Yes, this program worked

**Dave Jones:** correctly, I guess. Scan log, scan reads, millisecond per loop, scan reads. So, it's streaming to a file. So, I I don't quite understand. I did I'd have to RTFM. Sorry, this is not going to be an in-depth review. I just

**Dave Jones:** want to see that it talks and and it's sampling stuff. And it's just floating, which is what you'd expect. Start stream. There we go. So, it's doing that, but it's not Oh, okay. That's why our auto scale didn't

**Dave Jones:** work before cuz we had the I still can't change manually change the the axes down here. That's a bit disappointing. And I can't like just do basic stuff like zoom in. Uh? Now, you've got to understand that these are

**Dave Jones:** just like um example apps and stuff like that. The whole point about these sort of things is that you integrate them into your own production test system. So, you write your own software. That's why you would use like the LabVIEW

**Dave Jones:** interface. I don't know if they have a Lab Lab Windows CVI. They do have a C uh interface as well. I'm Yeah, C C++ um and it's not native LabVIEW support. You've got to use their library. So, the

**Dave Jones:** LJM library there, but who cares, right? That's what you'd expect cuz it's not National Instruments uh approved hardware. Uh like you don't use the supplied software. So, it's just examples. Not sure if they supply the source code for

**Dave Jones:** the uh supplied examples or not. It's, you know, the hardware's professional and I'm sure the drivers uh work just fine. And I'm sure they'd provide professional-level support as well. If you get into trouble actually uh you know, trying to implement this in your

**Dave Jones:** own test system. I have no doubt about it. So, the dashboard. Well, let's go back to Kipling. I think that's where we set it up. Here we go. There we go. We're in like Flynn. And device info. Here we go. This is So,

**Dave Jones:** this Kipling side isn't this nice? Oh, and they've got the direct links to all the example code for LabVIEW Python DAC Factory Java.net Node.js, and more. Okay, yep, I'm I'm thoroughly impressed. Okay, that's great. Yeah, this It's a

**Dave Jones:** professional-level support for this thing. As I said, as you'd expect. SD card installs, high high-res ADC installed, real-time clock. Wow. Yeah, they Here's the This is the dashboard for it. Oh, look at that. It's got the pin outs

**Dave Jones:** and everything, and you can just select Uh very nice. Yep, that's absolutely terrific. DB-30 Like, nobody uses DB-37s anymore. That's hilarious. And DB-15s. It's great. Old-school stuff. Um And and the analog inputs, you can configure There you go.

**Dave Jones:** Here's where you can configure ranges, and I'm sure that flows through to the other uh software and stuff like that. Register matrix. Woah. Wow. Wow, this is ah Wow. Okay, this is incredibly powerful. Wow, filter by tags. Analog input. Shh.

**Dave Jones:** If you want just the UART stuff, there it is. You can define all the UART registers settings. Lua script debugger. I I'm not into Lua, but yeah, okay. Um Power up defaults, device up data, DAC outputs. We've only got the two 12-bit

**Dave Jones:** DAC. Anyway, I'm thoroughly impressed. That is Anyway, that's enough for my old bag. Uh thank you very much, Lab Jack, for sending it in. Might be able to use that on like automation test projects. Shame it doesn't have the uh like motor

**Dave Jones:** driver like a couple of motor driver channels in it. That would have been It's asking to It's a data acquisition system. It's asking too much. But like a I just need needed something like this would have been perfect for getting the

**Dave Jones:** toggle bot back up and running, cuz we've got a new version of the meter with We just want to test the switches again, the 121G meter. And uh yeah, if it had a just a couple of uh motor

**Dave Jones:** driver channels, we could have used this for the toggle what? Would have been fantastic, but yeah, I'm I'm pretty impressed by this. So far, the but the supplied applications typical they leave a bit to be desired. They're just like

**Dave Jones:** slapped together LabVIEW stuff, but in terms but as I said, you generally not going to be using those. You're going to integrate this into a production test system, and for that it looks like a winner for your 430 bucks or whatever it

**Dave Jones:** was. That's That's pretty good. Thanks, LabJack. That's awesome. Hi to all my viewers in Italy. This one comes from Belina Limited or whatever. It's got Belina Fin on there. I don't know. Let's go. Let's go.

**Dave Jones:** Got a shipping label here. Cool looking large demoway board sort of Yeah, it's a Raspberry Pi type board. We have a note. Hi Dave. Please find enclosed an early production unit of our carrier board for the Raspberry Pi compute module. We

**Dave Jones:** found a lot of people looking to deploy Raspberry Pi in commercial industrial environments at scale, and so we've worked hard to create a board which solves the issues faced cuz you might ask, why not just use a Raspberry Pi

**Dave Jones:** instead of putting a Raspberry Pi compute module onto a board which then becomes a Raspberry Pi board. This is the reason why. Wider power ranges, wider temperature ranges, more robust physical connectors, power over Ethernet, etc. etc. while still running

**Dave Jones:** all software that the Pi does. We added some stuff, too. Namely a co-processor. What sort of co-processor would they have on it? And does the Raspberry Pi ecosystem support a co-processor? Like software ecosystem support a co-processor? I've no idea. Real-time

**Dave Jones:** clock? Yeah, the Raspberry Pi doesn't have a real-time clock, does it? Um and a uh, mini PCI slot and jewel camera support. Cuz if you want to do like stereo vision stuff, the regular Raspberry Pi only supports one. So,

**Dave Jones:** cool. Let's take a look. Thank you very much, uh, Chris Crocker-White, hyphenated last name. Ooh. Go to the other bench. So, yes, just a reminder, if you are going to send stuff in, make sure you put mailbag on the

**Dave Jones:** top. Otherwise, I could accidentally open it thinking it's something I've ordered. We get the, uh, BalenaFin. That's how you pronounce it, uh, board. We'll take a close look at that. Get a funky looking case. It's all plastic. I

**Dave Jones:** like how that's got a rubber baby buggy bumper on there. That's your DC input jack. And, uh, looks like that's just, whoop, splits apart. And that's just a plastic case. Does have a vent hole there, but like there's no fan or anything like

**Dave Jones:** that to, uh, keep it going. Not sure of the power dissipation of this, um, so you can probably whack a heat sink on that, maybe. And, uh, if you, well, I don't know. Is there enough room at the bottom? Yeah, there probably

**Dave Jones:** is enough room at the bottom to actually have the heat sink on there, I suspect. And you get a plug pack with all the requisite, uh, adapters. It's just one of those things that plugs on. Let's take a close look at the board. So, it's

**Dave Jones:** got the Raspberry Pi, uh, hat on it, of course. Nicely color coded. Look at that. Not sure how they've actually, uh, done that, but that's pretty neat. I like it. Um, a surface mount fuse over here. Very nice. Got another one over

**Dave Jones:** here. Look at the DC input. You can power it from a DC jack or a Phoenix type connector, Molex type connector. And, uh, look, massive diode protection here. Surface mount fuse in a holder. Fantastic. More protection, more protection. And, that's just absolutely

**Dave Jones:** terrific. What you want for an industrial solution. Um, expansion, I'm not sure what type of expansion header that is. And it's got the requisite, uh, Ethernet to USB. Probably would have been nicer to have more USBs on there.

**Dave Jones:** Like two's, you know, a bit limiting. Um I'm not sure doesn't seem to have power over Ethernet. Um let me check that. No, sure enough. Um you've got to put on the power over Ethernet hat. So, you've got to actually um yeah, like

**Dave Jones:** waste a hat for to get power over Ethernet functionality. Oh, would have been really nice if that was built in. Um anyway, like not everyone's going to use it, so it does waste uh space and cost and all the rest

**Dave Jones:** of it, but still that would have been nice. Got ourselves our antenna down there. All the ground planes pulled back. Very nice. And there's our co-processor. It's actually a Silicon Labs uh BGM 111. As I said, I'm not sure how

**Dave Jones:** that works inside the uh ecosystem, but of course you could it's got its own uh Wi-Fi thing, so you could uh like just run your own like a little Wi-Fi apps in there. So, Wi-Fi related apps. So, that's you know,

**Dave Jones:** really what they mean uh by that co-processor, I think. It's not like a you know, you can offload uh all of your like, you know, your heavy math or anything to this sort of thing. It's like that's not what it's for. It's

**Dave Jones:** designed for like application control and stuff like that. So, you can run your own little application on there, which runs entirely separate to the Raspberry Pi. So, that's pretty neat. So, camera zero there and camera one and also uh display as well. And of course,

**Dave Jones:** as you'd expect, HDMI and a mini uh PCI Express slot. That's very nice, so you can put some uh nice storage solutions on there or whatnot. And uh that's where we plug in our Raspberry Pi. Let's whack that in there.

**Dave Jones:** Made in the old dart. Fantastic. So, we're in like Flynn. Let's power it up. So, I power it from the DC jack 6 to 30 V input. That's a nice range. I like it. We get a 12-V 1.5

**Dave Jones:** amp pack with it. Uh Houston, we have a problem. First hurdle is I got a just pulled a uh configured SD micro SD card out of another Raspberry Pi, random one I had lying around, and went to plug it in,

**Dave Jones:** and it doesn't go in cuz that's a nano SIM connector, and there is nowhere else to plug it in. Womp womp womp womp But then I realized it does have a built-in uh eMMC memory. There's the Sandisk chip down in there, but still I

**Dave Jones:** reckon that's a huge oversight not to have I'm sure I'm not sure why they deliberately decided not to have a micro SD card. That's like you can just whip it out of or compatible with any other Raspberry Pi. It just

**Dave Jones:** They've got They've added everything, including the kitchen sink, except micro SD card. Wha- Well, I'll tell you what, for the 199 Yankee bucks that this uh thing costs, and by the way, it's a complete kit. It does come with the Raspberry Pi

**Dave Jones:** Compute Module, the case, and everything else. So, um yeah, I did want to come already preconfigured and fire it up. Let's hope so. Let's plug in a monitor. Nope, turns out doesn't look like it comes preconfigured. I just get zippity doo

**Dave Jones:** dah. But the thing is the eMMC memory on here with the uh this little USB here. Apparently, if you plug in the micro USB, it automatically enters a boot programming mode where it turns it into a mass storage device. So,

**Dave Jones:** yeah, at least we can get access to it, but still I think it's just a silly decision not to have a micro SD card on there so you can just come along and just upgrade the firmware with just a

**Dave Jones:** like SD card. That's all upgrade the firmware, the OS, you know, with the It's not one of these uh newfangled embedded things. This is like a Yeah, full-on PC. Whatever. Anyway, I I think that's a big oversight. It's nice to

**Dave Jones:** have the eMMC memory on there. That's Don't get me wrong. That's nice, but yeah, microSD card, please. All right. So, I'm going to plug this up. I don't I You might be able to power it through the micro USB, but I think it's really

**Dave Jones:** just designed for especially not with all the extra stuff on there. Um you know, if you want to take any grunty stuff from it, you should power it from the DC jack. Anyway, it will have enough power to

**Dave Jones:** boot this thing up and get it running as a mass storage device. It's supposed to auto boot into a mass storage device. I'm not seeing any thing on Windows. Uh I'll get back to you. So, here's the page, by the way. Go

**Dave Jones:** in and order it now. Flexible networking, real-time low power capable, excellent embedded 32-bit arm. That's the co-processor. Allows maximum power efficiency and real-time computing. Expandable. Blah blah blah blah blah. Why? Belina Fin. There you go. You can go check it all out. And uh it is very

**Dave Jones:** feature-packed. But yeah, as I said, I've It looks pretty comprehensive. There's a big manual for it. And yes, um the schematics are available. Check them out. You can just download those from the GitHubs. Here is our data sheet, and

**Dave Jones:** we'll go in there and we'll try and figure out how to cuz this thing ain't popping up. So, got to go in there and figure out how to get this mass storage working so then I can download the uh like a Raspbian uh image and put

**Dave Jones:** it on the thing so it can boot up. It should come preconfigured for 199 buck pack, I want it out of the box. I want it to just work with, you know, Raspbian or whatever. Please. And next, open the eMMC flashing

**Dave Jones:** tool such as Etcher. What the hell is Etcher? To instruct the Fin to boot into USB mass storage mode. No. Out of the box for I don't want to jump through these stupid hoops. I don't care how easy Like everyone knows "Oh yeah, I use

**Dave Jones:** Etcher all the time." Whoop-di-do. No. This is ridiculous. It should either come pre-configured and work out of the box or have that micro SD card. Well, at least they don't buggy you off to some GitHubby stupid GitHub thing somewhere.

**Dave Jones:** They at least Yeah, select image. Yeah, download 64. All right. All right, there we go. I've got to select the image. So, I've got to go find a Raspbian image or whatever and then select it and we should be able to flash it. Oh, I just

**Dave Jones:** remembered that you need to have an imaging tool for a micro SD card for Raspberry Pi anyway. So, okay. You know, it fair enough. Still, I reckon they should have a micro SD card so that you can just mass produce these things or

**Dave Jones:** whatever, especially if you've got an array of them or something like that. You know, you just want to be able to swap it in and out. Only 12 hours left. Thankfully, the torrent's going to be a bit quicker. There you go. 9.1 megabytes

**Dave Jones:** per second. Sweet. All right, we select the full image. That was quick. That only took a couple of minutes. And select drive. No removable drive detected. What what what what? Well, sorry. I'd love to show you this working, but I can't get it to work. I

**Dave Jones:** I'm following the instructions. It's like not rocket science. It's like plug it in. It says that uh and instruct the Fin to boot into USB mass storage mode. I don't know how to do that. I just load the program and I

**Dave Jones:** run the Etcher program and it doesn't give me like any option to enable it into boot mode. I thought it like did it automatically. It's just I I'm trying different USB ports and I simply cannot get this damn thing to

**Dave Jones:** boot into a drive. So, that's actually running sweet now. And apparently there's like a balena OS is an operating system using docker containers. Yeah, I got no idea there's a command line interface or you geeks can just go

**Dave Jones:** absolutely crazy and they've got like a GitHub with all the balena fin like cloud balena cloud examples and all sorts of stuff. So looks like it's pretty comprehensive. It's not just a Raspberry Pi industrial computer. Looks like they've got all their own stuff and

**Dave Jones:** everything else that extends that and sorry this isn't going to turn into a full on review it would take me ages to you know, look at all the different stuff on this and likewise that co-processor on there for example, I'm

**Dave Jones:** not sure how you end up programming that but I'm sure it's all in here somewhere if you check it out. I'm sure. Anyway, it's very comprehensive they actually put a lot of effort into this and it seems very comprehensive. So

**Dave Jones:** it's just a bit pricey unfortunately. It's like a 100 the one we've got here is the I think it's the developer kit 199 US bucks. So it's not particularly cheap but it does seem very comprehensive. If you just want the basic board with the 8

**Dave Jones:** gig eMMC memory 129 Yankee bucks. Anyway, it does seem very cool and you can get in early one of the first order one of the first 100 developer kits now. So it seems quite comprehensive. The only thing missing I think is integrated

**Dave Jones:** power over ethernet actually embedded on the board cuz that but if you don't need it then as I said it just waste board space and everything else but with the wide range DC power input and stuff like that and I

**Dave Jones:** think it's missing micro SD card too because if it had a micro SD card I would have just avoided all that hassle I had that probably was the fault of Windows or whatever driver problems or whatever trying to

**Dave Jones:** get that eMMC thing running. Anyway, um, it looks like a very useful, uh, industrial Raspberry Pi compute module type thing to add lots more bells and whistles. Like, if you're doing dual camera support and doing all sorts of

**Dave Jones:** other things with that co-processor as well. That's really good for like low-power stuff. You can just have it like background running in the, uh, that low-power applications processor just running in the background handling like just a couple of inputs and doing stuff

**Dave Jones:** like that. And then it could maybe wake up and power up the main, uh, Raspberry Pi compute module, um, to do the more heavy-duty grunty stuff. So, could be very, very flexible this thing. It's pretty groovy. So, check it out.

**Dave Jones:** Links down below. Thank you very much, Tom Ballard, from, uh, Pittsworth in Queensland. Bloody Queenslander. They'll know what I'm talking about. Anyway, let's have a look. Oh, it's a Hi, Dave. It's a tail light. It's a tail light. Thought this might be

**Dave Jones:** interesting to some. It is a tail prime mover tail light assembly which has failed intermittent problems. White wire is earth. 9 to 32 volts. Wow, 32 volts, really? They have like I thought they had 24 volt. Didn't know they had 32

**Dave Jones:** volt. Anyway, brown is tail lights left and interesting know how and why. Seems like a hell of a replacement for three incandescent bulbs. Why would it be? Like, it's not even a LED one. Um, it Yeah, it's not even a LED one.

**Dave Jones:** It's just a bulb base one. Oh, no, it is LED base. Sorry, bulb. Oh, okay. Seems like hell of a replacement for three incandescent bulbs. Right, that's what Tom's talking about. Okay, yeah, there is Oh, actually, this looks Yeah, this

**Dave Jones:** looks more interesting than it seems. Let's take a squeeze. So, here's the tail light that Tom sent in. And as you can see, it's rather rather interesting. They've actually conformally coated, um, a good lot of it, but it's really

**Dave Jones:** uneven. Look at the patches up here where there's no conformal coat. You can tell by the shine on that. And then the tops of the components aren't uh conformally coated either. I mean, if you're going to do that they do this for

**Dave Jones:** moisture, of course. It stops that moisture like forming on the board and getting between the components and causing leakage and you know, it contaminated and then it contaminates with dirt and gunk and everything and then things start getting low impedance

**Dave Jones:** and they start effectively uh shorting out and ruining your day. But like they've effectively got a potting box here. So why I would have just like potted the whole blinking lot in one big solid potting compound or at least a

**Dave Jones:** re-enterable potting compound or something, but yeah, curious. Let me get this uh outer plastic bit off. And you can see the LEDs down there. They're interesting little uh four-terminal jobbies. Um it's curious how they've got these uh these lenses like really

**Dave Jones:** Usually you'd have them like right on top. But you can see that they're actually domed underneath to sort of focus and then sort of uh disperse that on the top or whatever, you know, the optical mechanism air. So I think we've

**Dave Jones:** got the convex on the bottom and then just flat on the top. Even though it looks concave, I don't think it actually is. So yeah, it's just interesting how far they've got those off there. But if you look down in

**Dave Jones:** there, you can see how it actually magnifies that. So it makes it look like a larger individual dot. All right, so let's hook up the red wire up and the white uh 12 volts, which is supposed to be the brake

**Dave Jones:** lights. So oh, jeez, that's pretty Whoa. Was it Hang on. Whoa. Look at that. It's climbing. And like a couple came on first. Why is it like climbing like that? Wow. That's That's weird. Like, you would think that it would just

**Dave Jones:** like come on. Yeah. I think that's one sick puppy. Oh, she's still climbing. This is nuts. Is it just going to eventually like burn out or something? Or is that normal? I don't like Does that like No, cuz brake lights aren't

**Dave Jones:** They're They're either on or off. Really? So, I'm not sure what the deal is there. That's very strange. Oh, there we go. There we go. Have we Have we stopped? No. No. No, it's climb It's decided to climb again.

**Dave Jones:** That is bizarre. No. No, we're going back down. I'm going down. Is there magic smoke escaping from something?

**Dave Jones:** Can't smell anything. And they're just going to switch off. I You watch. Will we get like those two that just had like the threshold that we saw before? This I What? Here we go. They're going dim. Dim. Yeah.

**Dave Jones:** Yeah. Some are brighter than others. Whoa. Look at that. Whoa. They're pulsing. Oh, wow.

**Dave Jones:** Yeah, that's one sick puppy. So, let's try the brown wire. That lights up the red red ones, too. At near half an amp. That seems fairly consistent. Let's try the green. Maybe that should light up. Yeah, lights up the other

**Dave Jones:** side. Got our yellow. Um and Well, okay. Try both. There we go. We've got an amp total. And there's the back. We've just got some surface mount resistors on there. They're all just wave soldered on. No worries. Let's have a closer look at

**Dave Jones:** the circuitry but there's nothing intelligent going on here. On this microcontroller rubbish. Okay, what we've got here is a 34063 absolutely classic. I've done a very early video on that. That's a just a switching controller and there's the

**Dave Jones:** coil down there for that and the driver transistor as well. So they use doing that externally and we've got the two driver [ __ ] over here. One for this side and one for the other side that are

**Dave Jones:** just be doing the constant current thing and triple five timer for the win. Thank you very much. I don't know what that's doing. Maybe some sort of blinking capability but I thought these tail lights like use external bimetallic

**Dave Jones:** blinkers. That's what I thought anyway. I don't know anything about car or truck electrics or whatever. So yeah, I I really don't know. It looks a bit how you doing. Around here is someone had a hack at this.

**Dave Jones:** I don't know. Looks pretty ugly. But yeah, there's not much to it. It's just going to have a constant couple of constant current drives there. So why it's going funny I don't know and in a mail bag I'm not going to go in and

**Dave Jones:** troubleshoot this but that's that's interesting. I like how the you know they've used the big bulbous lens on the top there which then mates up with another convex lens on the bottom of that and then a flat thing on top. I don't think the optics

**Dave Jones:** are quite fascinating on that. Anyway, not sure what these are doing. Do they like little they point inwards to some lens mechanism on the other sort of lens mechanism on the top. They just seem to light up as part of this. I think

**Dave Jones:** they're all the same array. Aren't they? So I not sure what the deal is. Anyway, that's interesting. Thanks, Tom. And Tom did question the reliability of something like this, but it seems to be quite a rugged design and

**Dave Jones:** construction. Don't mind it at all. But as I said, I would have completely potted that whole thing, not just not just pour some conformal coating over the top. That's That's pretty piss-poor effort there. The soldering leaves a bit to be desired, considering

**Dave Jones:** that this whole thing is supposed to be wave soldered. You can see all these are wave soldered over here. Yeah, someone's had Someone's had a hack. I reckon someone's had a hack at this. Don't get postcards much these days.

**Dave Jones:** Delivering memories with that circuit. What's that going to do? Anyway, it's from the Chaos Computer Camp. Chaos Post. Awesome. So, um it doesn't actually say who it's from. It just says from the Chaos Computer Camp. I'd love to go. I was invited once, but

**Dave Jones:** unfortunately it's like on just after Christmas time. And for those who don't realize, like it's like in Germany somewhere, and it takes like 24 hours just in flight time. More like by the time you get transfers, like 30 hours.

**Dave Jones:** Then by the time you get to and from the airports and to and from the destination and and your layovers and and waiting at the airport a couple hours before. It's like 60-plus hours just in travel time to get to this and back. So, yeah, 60

**Dave Jones:** hours. That's like 1 and 1/2 working weeks. Thank you very much, Matthew Liberty. No, you don't salute liberty, do you, in the in the United States of America. Thank you very much. I actually know what this one is, and it is a

**Dave Jones:** Kickstarter. And I guess kind of disclaimer, I suppose, is that I'm actually designing not an identical product, but pretty close to it. So, yeah. Um that just a disclaimer there. I don't know why, but I guess I don't

**Dave Jones:** know. Um some people might think I'm prejudiced or something because I'm going to Don't ask when mine is going to be available. Just don't, okay? It's I don't know, so don't even ask. Anyway, it's a Kickstarter. Thank you very much.

**Dave Jones:** It is the JewelScope. Yes, it's a microcurrent like thing, but a more advanced microcurrent, like a USB one, that can do I don't know that look nice. Oh, hang on. No, they don't screw No, it's just banana plugs, but it comes

**Dave Jones:** with different adapters. Anyway, JewelScope, it's a USB microcurrent type data logger type thing. It's got a from memory, it's got a couple hundred kilohertz bandwidth and yeah, it allows auto ranging and allows you to Yep, there's the different adaptery

**Dave Jones:** things and stuff like that. Anyway, yes, so I am working on a very similar thing. But anyway, let's take a look at it. It looks cool. Even got a Stanley Torx driver to go with it. Beautiful. So, we can open it up and

**Dave Jones:** replace the front panel. Cool. Is that a piece of Is that a PCB front panel? Not sure, we'll find out. So, here is the JewelScope by Jet Perch. It's the JS110 Precision DC Energy Analyzer jewelscope.com. As I said, it is a

**Dave Jones:** current Kickstarter, which has raised I think about 115,000 Australian dollars of its 98,000 Australian dollar goal, something like that. I'm just working in Aussie bucks, sorry. That's what Kickstarter tells me. And it's a basically a USB interface energy analyzer. So, it measures current

**Dave Jones:** and voltage, of course. You just feed in your power supply to your device under test, your product, and out, and it measures the voltage and current and can hence calculate power and basically samples that with up to um

**Dave Jones:** it's got a 14-bit 2 meg sample per second isolated cuz it's got to be isolated. You can't be connecting to your power into your USB ground over here. That'll ruin your day. It uses the same MAX4239 op-amp that I use in the

**Dave Jones:** micro current, of course. But yeah, it still it has that noise spike around 11 kHz. It actually varies quite a lot because it's actually a chopper amplifier, so it's got to chop at a particular frequency. Anyway, yeah, bandwidth is a couple hundred kHz, I

**Dave Jones:** believe. For the 2 meg sample sample rate, and this is a beta unit. It's currently going for 500 Yankee bucks on Kickstarter, which is quite expensive for basically an ADC in a box, but it's the ADC. It's like a 2 meg sample per

**Dave Jones:** second 14-bit converter is probably like, you know, a $30 chip on its own. You know, real expensive precision parts, no doubt, used in this. Just like even the micro current, as simple as it is, um like I've got resistors in the

**Dave Jones:** micro current that are like $2.50 US for one resistor, one shunt resistor. Like and that's in volume. So, yeah. Anyway, it's going to have a retail price of $799 Yankee bucks, which is you know, it's getting up there. But

**Dave Jones:** that's not hugely expensive for a commercial product, which this is obviously intended to be. And yeah, they started at $399, but they're actually sold out. So, it's currently $499 on Kickstarter. 7 days left if you want to get in on it. Just check it out. Now,

**Dave Jones:** the issue with trying to measure product current consumption, let's say you have your little doohickey new Internet of Things wankery gadget, and you want to measure its current consumption, well, it likely has a sleep mode, which is, you know, down

**Dave Jones:** in the microamps or even lower, and then it, you know, wakes up um periodically or as some event or whatever, or it has like and and it might not any wake up and then draw milliamps, but then it

**Dave Jones:** might have a a Wi-Fi thing, which can then draw hundreds of milliamps or even amps. Um so, it the problem with the microcurrent and any measurement device is one of uh dynamic range, which means that uh yeah, like you can't have just a

**Dave Jones:** single shunt resistor and then measure even microamps in the presence of amps and get any sort of resolution down at that microamp range. You need like a 32-bit ADC, which is just not possible. You know, it's ridiculous. So, you've

**Dave Jones:** got to have ranging. And uh this one does auto ranging, which as my new uh version of my uh eventually, my new product I'm working on is going to have uh the same auto ranging, but auto ranging is not magic

**Dave Jones:** because the if the processor is in sleep mode, for example, you're going to get resolution, let's say it, you know, draws a microamp or something. Oh, oh, we're going to open. Oh, we got Mylar on the side. We're being mooned. There we

**Dave Jones:** go. Oh, look at that. Isn't that nice? There's the um there's the isolation. That's pretty neat, isn't it? I like that. So, I'll just leave it there while I discuss this for a minute. So, if your product's consuming a microamp and you

**Dave Jones:** want to measure that, you know, reasonably accurate is accurate accura- accurately, you want to like a, you know, a day couple of decimal places on that, probably. Like, you you know, what, 3 and 1/2 digit meter resolution or whatever on that, then uh right,

**Dave Jones:** you've got to have a shunt resistor like a 1K shunt resistor, for example, 100 ohm shunt resistor, that then, when you're, you know, use some like times 10 or maybe even times 100 uh amplification, you can get decent

**Dave Jones:** resolution on that one micron. But, the problem is, let's say your shunt resistor is 1K, then when your microcontroller just suddenly wakes up from its sleep mode and wants to draw a couple of 100 milliamps, what what what

**Dave Jones:** what, 100 milliamps through a 1K resistor shunt resistor to measure the current, that's 100 volts. What what, your power supply is only 3.3 volts, it doesn't have 100 volts to drop. So, the voltage on your product drops to zero. Even if you use a 100 ohm

**Dave Jones:** resistor, not good enough. It's still going to drop 10 volts at that 100 milliamps. You know, a 1 ohm resistor is still going to drop a 100 millivolts, 0.1. That may not make your product drop out, but then you

**Dave Jones:** can't get the resolution down at the lower currents. So, you've got to use Well, well, you don't have to. Oh, there we go. Look at that. That's very neat. There we go. We've got a header on there. It's a 0.1 inch header. That

**Dave Jones:** works where uh we considered this one for the new micro supply, actually. And I'm not sure, maybe I've done a video on it, not sure. Anyway, this sort of pin solution to go to a front panel. It's exactly what we're going to do on

**Dave Jones:** the new micro supply, but we actually went away from that in the end for various reasons, but there you go. That's a neat solution. I like that. And I haven't seen these before. Look, they've got 2 mm They're 4 mm uh banana

**Dave Jones:** jacks with like a shrouded high voltage shrouded ones with a 2 mm soldered pin on the back. That's really interesting. I I don't think I've come across those. I rather like those, except that they're not binding posts, which is really

**Dave Jones:** annoying. I'd love to see binding posts on this product. And why you need the 4 mm insulated uh plugs on that, I I don't know. Much would have preferred binding posts, but hey, the good thing is is that we can change the board, and we do

**Dave Jones:** actually have different boards. Like this one, for example, we can just plug it in, and bingo, you can measure your USB power consumption. Isn't that neat? No worries. Anyway, back to the auto-ranging thing, auto-ranging is a problem because I your circuit has to

**Dave Jones:** detect that current and then switch fast enough before your product under test actually has time enough to drop out before that voltage becomes an issue and stop your product of current. And if you don't have enough bypass capacitance

**Dave Jones:** either on the output of this, which it shouldn't really have, or on your or on your product under test that you're trying to measure, then it can drop out pretty quickly. Like it can drop out in microseconds, you know, hundreds of nanoseconds,

**Dave Jones:** something like that. If you don't have enough bypass capacitance and it suddenly goes from drawing a microamp up to an amp, that can ruin your day. So, ultimately, there's no magic solution for this. You should try and switch

**Dave Jones:** auto-range your shunt resistors as fast as possible, but ultimately, there will be some products where that simply is not a solution. So, unfortunately, you've got to do like manual, you know, you really have to do it manually by setting a

**Dave Jones:** manual range and then forcing your product into one mode and forcing it into another. You can't sort of measure it dynamically. So, yeah, there's always limitations there, but apparently, this can switch in I think it's like a 2

**Dave Jones:** microsecond Yeah, under overflow 2 microseconds. There you go. Tells you when it switches ranges on overflowing under 2 microseconds to ensure the target device runs unhindered hindered. And then if it is true auto-ranging, you've got the issue of

**Dave Jones:** hysteresis and like switching back and all that sort of stuff. You don't want it to like the ranging to oscillate and and things like that if there's like little dips in the drop-out or whatever. It's it you know, it's quite a difficult

**Dave Jones:** problem to solve auto-ranging. So, yeah, I I wouldn't expect this to get it right for every product. You know, you I guarantee you there will be products where this can have the world's best auto ranging for this sort of thing and

**Dave Jones:** you're still going to find products that is going to be an issue with. Oh jeez, I really need to take a high-res photo. Maybe I'll do it as like a take a high-res photo and then we can zoom

**Dave Jones:** around this baby in in software editing. That might be easier. All right, so let's have a look at this. There's our NXP processor there. There you go, it's upside down so all the electrons are going to fall out and that's doing all

**Dave Jones:** the USB streaming and comms and everything else. Then we've got something else down here. What's this ice? What is that? Oh, that's a lattice semiconductor. That looks like a CPLD. Anyway, it looks like we have an interface here that does

**Dave Jones:** some data and stuff like that. That's on the PC side of things. Now, this is interesting. One thing which I don't know if this has, but you would probably want to add to a product like this is a

**Dave Jones:** synchronization with your product under test. So, a synchronization with a digital signal. This doesn't have any digital inputs. Now, it's got some generic ones over here, but these are on the not they're not on the product side. They're not on the isolated side.

**Dave Jones:** They're on the PC side of things. So, yeah, so you could maybe add some functionality there, but it's on the it's on the wrong side of the force, unfortunately. And it looks like we've got a trace input there programming

**Dave Jones:** debugger header and all that. That would be an NXP header. We've got another lattice part over here. Um so, is is that one of those mini FPGAs? The ICE40LP2. Yep, that's one of their ICEcube ultra low density FPGA design. You get more

**Dave Jones:** for less. Blah blah blah. All that sort of jazz. So, the neat thing about that is it's available in a you know, a reasonably usable package. None of that BGA rubbish, although you've got the you've already got the BGA over here.

**Dave Jones:** So, you know, you pay that uh assembly penalty there, you may as well pay it everywhere else. Now, what am I what I'm interested in here? So, this is obviously doing like data formatting to go across the uh isolation channel here.

**Dave Jones:** What what isolator have they got? There you go. They've got the uh Silicon Labs um 86 and that's the low-power six-channel digital isolator that does uh 150 megabits per second. So, more than good enough. Um we're only doing uh Well, no,

**Dave Jones:** we're doing two meg samples per second. It's samples per second. So, you've got to multiply that by however many bits, in this case, 14-bits conversion. So, you need a 16-bit word there. So, you've got to multiply the two meg samples by

**Dave Jones:** 16, so it's got 32 megabits per second across that little uh channel there. So, that's why they're doing some like formatting inside the FPGA there. They're just doing some fast data formatting because you probably can't I and and some buffering

**Dave Jones:** as well. They're probably doing some buffering and stuff like that. And then the micro might read that at a slower rate. I don't know. Something like that. Anyway, um we've got a um STM32 micro on the low side that it'd be doing uh I assume all

**Dave Jones:** of the auto-ranging. I have no idea if you can do this uh manual or auto range. Uh like choose manual range or not. It might just be um all automatic all the time. Have a browse around. I I like I

**Dave Jones:** prefer doing this on the PC. Now, it's just nicer than trying to do it on camera and set the angles and do everything. Take a nice high-res photo and you can just, you know, you can just pan around until the cows come home.

**Dave Jones:** Anyway, what I'm interested in is the shunt and uh switching. So, if we go over here, here's our input connector here. And these are obviously uh big-ass MOSFETs. Don't even need to look up the number. You can tell by the pinouts how

**Dave Jones:** they shorted all the pins there, shorted all the pins there, and they'll have one for the gate drive. So, that's a MOSFET. So, I can see our shunt resistors right away. Okay, so let's have a look at what's going on here. Here's our first

**Dave Jones:** shunt resistor, and this looks like I think like I thought that was 10 ohms, but I think that's actually 10 milliohms shunt resistor. And that's this MOSFET here is the one that's actually shorted Why do you need to shut

**Dave Jones:** that off? You wouldn't need Oh, sorry. No, it's going at the positive side. Okay, so that's enabled all the time. And then you've got the 100 milliohm, the 0.1 ohm shunt resistor here. That is not a four-terminal jobbie

**Dave Jones:** like I have on the micro count. Neither of these are four-terminal jobbies, and I don't see any uh Kelvin connection coming off there. Um so, they've got an unpopulated thought they needed something not at 100 milliohms. The capacitors can't do naff

**Dave Jones:** all there. That's why they left it off. But we do have here's a 1 ohm shunt resistor up here, and these would be all like 0.1% jobs, something like that. Um because there's two ways to do it. You

**Dave Jones:** can either build in the accuracy into the resistors, or you can calibrate it later. It's six one, half dozen the other. Depends where you want to spend your money. Do you want to spend your money calibrating the thing, or do you want to spend the

**Dave Jones:** money buying the good resistors so you don't have to calibrate the thing? And right, so they're tapping that off. And that's going to the MAX4239 over here, or 4238. Yeah, they've got the higher bandwidth, so the 4239 I

**Dave Jones:** think is the higher bandwidth one. And then that MOSFET there shorts out the 100 milliohm where Yeah, it gets rid of No, it gets rid of the top part, so they're shorting out the top parts of them. So, it shorts out but the top

**Dave Jones:** string, I mean. So, uh yeah, that one there cuz we're still in you know reasonably high current territory. So, we need a grunty two grunty MOSFETs there and then we start getting to more little piss ant MOSFETs here. Surprised they don't use all the

**Dave Jones:** same there actually, but they've actually used another two of one type then another two of another type and then we've got our other shunt resistors here. So, this would be one ohm, this is they're obviously going up decades. So, this would be 10 ohm,

**Dave Jones:** 100 ohms and 1k shunt resistor and then they've got another Maxim amp up here. So, it looks like yeah, they looks are they permanently measuring? Looks like they're permanently measuring across the bottom shunt resistor. Anyway, not going to

**Dave Jones:** analyze it till the cows come home. But yeah, that's exactly what I expected to see except I expected to see maybe some four terminal more expensive four terminal shunt resistors on there and I don't see it. Especially for the price.

**Dave Jones:** As I said like you know, you can pay three four dollars for a single, you know, a good shunt resistor, four terminal shunt resistor and they got lots of miscellaneous amps and stuff happening around here. So, not sure what the deal is there.

**Dave Jones:** Lots of you know, I'm not going to go in this is just a mail bag. Geez, I'm not going not going to go to town. What do we got here? And aha, these are your comparators over here because to do your

**Dave Jones:** auto ranging, you got to have the comparators to be able to set the thresholds where you want the auto ranging to happen at. So, this is actually doing auto ranging in hardware, which I'm I'm surprised it's not quicker

**Dave Jones:** than the two microseconds then in hardware, but you know, I that was one of my questions. Is it doing this in is it doing auto ranging hardware or software? It's there's I don't see any reason to have the

**Dave Jones:** comparators there if you weren't doing it in hardware. Anyway, this design looks pretty jazzy. Looks like it can do the business. So, obviously our ADC is in here somewhere. Where is it? You know, we're going to have a nice voltage

**Dave Jones:** reference, and there's going to be Where's the 14-bit ADC? Where's Wally? I reckon Wally's got to be one of these TI jobbies here. It's obviously like a serial output one. Um 2 megabits per second serial output. So, anyway, um that looks uh pretty

**Dave Jones:** good. And uh Matt's gone through lots of design iterations. It's been 2 years working on this. Lots of design iterations. Uh shows some like prototype development photos on the Kickstarter, which is really good. Uh yeah, very professional-looking board, very

**Dave Jones:** professional-looking campaign. I'm going to power it in. See if we can get something. Won't be an extensive review. I just want to power it up and see what the software's like. Well, that was easy. Check it out. No drivers to

**Dave Jones:** install. I just plugged it in. I downloaded the software, which is available for Linux and Mac as well as Windows, I think. And bingo, we've got the multimeter interface, and it works. There you go. It's updating. Of course,

**Dave Jones:** all these digits are [ __ ] Um I believe I think the specs for this 1.5 nanoamps resolution. So, the resolution So, all of this So, basically, everything every digit after the decimal point there is useless. So, five useless digits on the

**Dave Jones:** nanoamps. It's just Nah, you know, come on. Anyway, we've got current, voltage, power, and energy over time, and we can reset our energy. It's just accumulating there, as you'd expect. 56 picojoules. There you go. Um Why is it got an accumulate

**Dave Jones:** thing? It's already accumulating. Not sure there. Anyway, our device I wonder if you can have more than one. And we're multimeter uh default. So, let's go into oscilloscope default. And Woo! Woot! Look at that. Wow, that's fast update,

**Dave Jones:** isn't it? Can I Yeah, I can go full screen on that. Wow! That's pretty Hey! There we go. Yep. Yeah, that's all 50 hertz pick up and crap and it's ranged right down. So, that's why you're seeing all the noise

**Dave Jones:** and crap like that. So, let's get some piezo electric effect. Boom! Boom! Boom! You can see it on the current on the top, current on the top, voltage on the bottom. That's that that axis.

**Dave Jones:** Oh! Oh, yeah, different response there. So, that's Yeah, has it got like triggering? It doesn't seem to have triggering. Not that like I wouldn't have expected it just occurred to me because I'm doing like a still a scope functionality. I

**Dave Jones:** thought we could have like a selfie trigger and it could stop sampling. That'd be nice. Um anyway, it's not there by the looks of it and and here we go. We can actually or manual range by the looks of it. Yep, 10 amps.

**Dave Jones:** Flat line and it once again, yeah, here's where it shows you check this out. This is where it shows you let's say we went to 180 milliamps, right? Which is a reasonable range. Let's look at what the Yeah, it's auto scale Okay.

**Dave Jones:** So, it's if it went higher it did or it's just auto scaling the graph. It's auto scaling the Y axis. So, it's not like it's going to 180 milliamps. It's Look, 800 microamps. There it is. So, the noise is like we've got like 200

**Dave Jones:** microvolts of noise down there. So, imagine if your product was in sleep mode during you know, if it was drawing 200 microamps. That's a ridiculously high sleep mode. You know, it might be in the order of 20 microamps. You know,

**Dave Jones:** like you know, tens of microamps tops. You can't measure it in 180 milliamp mode, right? With a 14-bit converter. You can't do it. This is why you need um, auto ranging and or you know, to manually arrange things and then force

**Dave Jones:** your product into different ranges and stuff like that. What else have we got? Let's have a look. Uh, what is that? Automatically. Ah, right. So, I can change the auto range There we go. We can change the What?

**Dave Jones:** What have I done there? Why are they separating like that? What? Oh, that's the Oh, that's our time base. Okay, I'm using the mouse um, the scroll wheel. I'm using the scroll wheel. There you go. That's got to be, surely.

**Dave Jones:** No? What's Yeah, there we go. Oh, sorry. Yeah, the x-axis is there. It doesn't It's not labeled. I don't see the x-axis Oh, I Okay, we've got our nice cursory things. I don't see the x-axis being labeled there. It's like

**Dave Jones:** 8.4 what? Like Right. I I don't get it. What's What's going on there? 14 seconds. Yeah, that's Okay, so we're now in seconds cuz it'll take should take, you know, 14 seconds to get most of the way across the screen. 15

**Dave Jones:** seconds there. Why does it not display it? That seems silly. Anyway, we've got voltage ranges 5 volts or 15 volts. So, you know, if you're using a 3.3 volt thing, then you'd uh, use your 5-volt range just to get extra resolution, but

**Dave Jones:** voltage is not the thing here. Like it it doesn't matter. You could use an 8-bit converter for the voltage and like, meh, who cares? Or, you know, 10-bit or something like that if you want to gild the lily. There's no need

**Dave Jones:** for a like a 14-bit converter for the voltage, for example. So, because you just you don't care. Current's what the thing you want to measure over the massive dynamic range over like the eight different ranges that we have

**Dave Jones:** here. How many ranges? Two, four, six, eight, seven. Or, we can turn off the current. Sure why you'd want to turn it off, but okay. Fair enough. And it We turn it off and it's it's just giving us still our noise. So, yeah.

**Dave Jones:** 18 microamp range. Hang on, I've changed ranges. I've changed ranges and we're getting I've gone down to the 18 microamp range and we're still getting noise like that. I still don't know why that's coming together like that. What's

**Dave Jones:** What's get What's What's going on here? And of course we can just instantly stop it. Oh. No, how do we start again? Record button? No. What's What's a Joulescope data uses its own data format. Can you like export and

**Dave Jones:** stuff like that? I don't see export. I want to export my data to XLS. Geez. Device Joulescope currents raw Okay, that took time to come back. Why did that come back? After all that time. Okay, we can save it, but yeah.

**Dave Jones:** And that's what's in the Joulescope uh file format, so it's certainly not uh XLS. Doesn't look like Yeah, doesn't look like it save your data. Then if we stop it, we can't select data. Oh, yes yes yes we

**Dave Jones:** can. Can we select? Ah, that's that's zoom in. Okay, there we go. Not sure why it's having the different colors. That's as close as we can zoom. It won't let us zoom in any more than that. Okay, but we can't export

**Dave Jones:** the raw data. Hmm, that's not good. Anyway, look. Oh, look. Look, we can jump jump to voltage current multi display. That's kind of cool. Current voltage, okay. And then we can have power graphs. That's That's pretty flexible. I like that. Single value display. Okay,

**Dave Jones:** neat. Developer. Ooh, we can get all the developer stuff. I frames, M frames, example. I just noticed it took actually a long time, like tens of seconds before I pressed the play button here before it actually popped up. Anyway, um the

**Dave Jones:** developer edition actually comes with comes with these little little demo board. We've got a little processor there and a little power supply that you power from a micro USB and this allows you just to demonstrate this. So, look, we're getting 3.3 volts.

**Dave Jones:** So, obviously, um and it's drawing, you know, near on 20 microamps there. So, let's bugger off out of the multimeter and have a look at our current there. How where's our Oh, sorry. We're auto Let's auto Let's auto range

**Dave Jones:** our current, shall we? 5-volt range. See, 3.3 I don't like that. It just shows you you zooms in the noise there. It's kind of silly. Um let me see if I can get something from here cuz I'm not getting

**Dave Jones:** anything on the amps. Okay. For some reason, it's not Oh, there we go. Yeah, I think the software's a little bit a little bit buggy. There's something going on there. Anyway, yeah. Um let's Oh. Why does it Once again, it

**Dave Jones:** adds those That must be like Is that a peak function or something? What What's going on there? I don't I'll have to RTFM on that one. Wow. Okay. Yeah, the auto range is just It's all over the shop. Um it'd be nice

**Dave Jones:** to have like a trigger and then you can capture an event, but it looks like you might have to manually do it because I don't see any other ability here to do that. So, that's a bit of a shame.

**Dave Jones:** Okay. Press the Arduino reset button, apparently, and it will I'm pressing the Arduino Yeah, it's flashing. It's flashing, but I don't see any other action going on there. So, there we go. There we go. There we go. This is the This is the one used in

**Dave Jones:** their example. Yep. Okay, there we go. So, at a slow time base So, we'll just yeah. There it is. So, current milliamps. So, this is not right. So, it's auto ranging back to the microamps there. And if we push the

**Dave Jones:** Arduino reset button, it's going to take some time. So, it's flashing. It's not flashing yet. Here we go. One flash. No. No. Yeah, there it goes. There it goes. So, just you know it works. Um yeah, it it it does the

**Dave Jones:** job, but like the software I it's maybe there's a few little quirks in it. Um it's not as full featured as I like, but it's open source. It's all the software is all open source and the the hardware is not open source, but the

**Dave Jones:** software and the files for the front panels and and stuff and and things like that are though. So, yeah, it can kind of do the business. So, needs some spit and polish, but this is a complicated product. There's a lot

**Dave Jones:** to do in the software if you really want to really want to make it polished. But, there you go. That's the Jewel Scope. And it does it kind of works as advertised. Once again, this is not a large dynamic range here. This is like

**Dave Jones:** milliamps. This is like, you know, eight eight milliamps down to uh tens of micros. It's not a good example showing the massive dynamic range. This isn't a review. I will so I won't uh go and set up, you know, a a

**Dave Jones:** demo a better demo than this. And yeah, it's jump No, it's it's jumping to 600 microamps, right? So, it's jump from 600 microamps to 8 milliamps. You can just do that on one range. So, these red traces here, these are actually the min

**Dave Jones:** max and yellow is the average. I'm not even sure you can actually view the raw data. Maybe there's a Was there a raw mode option? Anyway, um it's completely buggy. I don't understand. Look, the yellow live data is down there. Okay, I've manually set

**Dave Jones:** the range to 18 milliamps and yet these the red traces are up at 60 plus minus 60 microamps. Why? This is absolutely insanity. I'm not I don't even know why you can if you can turn that off or not.

**Dave Jones:** And so I'm fixed range now. I'm fixed range and I can't I don't see how you can fix the axes either. Right? So we've captured our data, but look um the min max uh like stop stop. Like look at the look at the maximum

**Dave Jones:** there, right? I'm on the 18 milliamp range. Noise is not going to be like I I I can't see the noise actually being like that and if it is uh that much like say from you know 3.4 milli uh milliamps up to 3.8 milliamps.

**Dave Jones:** If your noise is actually that high, why can't we see it um in a live view? And I I just don't believe it because like look at all these Look at all these peaks up here like this. Like and then the it's showing the

**Dave Jones:** average. I don't Uh it's I I just don't like the way this thing operate the software operates. That's just wrong. That is wrong. So and then okay okay, there might be that much noise there, but we can't see the live data. So I'm

**Dave Jones:** not sure how that works, right? There's no option to say uh average is there? Device waveform. Grid X show me Okay, so we can disable our min max. Trace width. Okay. So we can get rid of our min max.

**Dave Jones:** That's better. Okay, that's less confusing. And is it doing like a rolling average? Um Oh, there we go. There we getting our spikes. That's better. Uh the confusing min max crap that doesn't work and you can't it looks like

**Dave Jones:** I don't think you can scale your axes. Can you like I can't there's nothing I can do to do that but yeah anyway I I don't know it's it's weird and buggy don't get it. But it kind of works there you go like

**Dave Jones:** it's it's it's doing what you kind of expect but I I don't know averaging I want the real data. And check this out there is certainly a delay in I've got the live update current here okay so it's point seven micro amps this little

**Dave Jones:** Arduino is drawing in live mode I fixed let's fix the current range to 18 milliamps. Okay actually let's go to 10 amps. Yeah there we go you can see the see the resolution change why why you get all that those digits it's just

**Dave Jones:** silly. Anyway two amps like it should yeah it gets better and better. Okay 180 milliamps there you go. And I so 18 milliamp range okay so watch the current there and then the waveform okay so it jumps up

**Dave Jones:** three milliamps but we get nothing on the display and then it comes in and then it jumps up and comes in and it so there's like yeah it's you're not getting your live data on your oscilloscope screen. I

**Dave Jones:** think that's pretty silly. This thing does actually work and it's yeah out of the box and it the hardware looks quite decent and the software needs some spit and polish but it's open source and you can do whatever.

**Dave Jones:** It's missing a few features but it's really quite expensive especially if you don't get the kick starter and it's 799 retail when it comes out so yeah. Anyway I'll link to it down below. Joulescope oh wow not sure Sure you can hear that

**Dave Jones:** but it's hailing outside. There's hail.
