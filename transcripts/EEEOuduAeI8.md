---
video_id: EEEOuduAeI8
title: EEVblog #1272 - Mailbag
url: https://www.youtube.com/watch?v=EEEOuduAeI8
source: youtube-asr
---

**Dave Jones:** Hi, welcome to everyone's favorite segment, mailbag. Let's get straight into it. Thank you very much. Uh E Richie, they've put a sticker on top. That's E Rich, I think. Anyway, from Mount Vernon in Ohio, I think it is in the United States

**Dave Jones:** of America. It's a real old-fashioned letter. So, let's have a squeeze. What do we got? Oh, we got It's a tech scope for all you tech scope fanboys. It's like a premium HP premium plus paper. Does this come from like an

**Dave Jones:** oscilloscope camera or something? I don't know. Let's read the note. Hi Dave, my name is Ethan. Good day Ethan from Ohio. I'm 16, young whippersnapper, trying to be an an electronics enthusiast such as yourself. You already are. About a year ago, I purchased a

**Dave Jones:** tech 2213A scope on eBay, as you do when you're strapped for cash. It was listed in as working in condition. Upon receiving the unit, it was functional, but the trace was so out of focus, even with the knobs at full focus, it's

**Dave Jones:** practically unusable for anything except DC voltage measurement. Do you have any thoughts as what might be the cause of this? And if so, what the fix would be? He's basically only got a multimeter and some basic soldering and hand tools and

**Dave Jones:** stuff. Thank you very much, Ethan. Well, unfortunately, I am no tech repair guru. The best place is the I can't remember the exact name. I'll link it in down below. The Tektronix Yahoo Oh, no, Yahoo groups have shut down now, haven't they?

**Dave Jones:** Damn. They just I I don't know what Anyway, there was I I don't know where they've gone to. I'll try and find out and include it down below. But, there was a very well-respected Tektronix group. I'm sure they probably might be on Facebook or

**Dave Jones:** somewhere now, anyway. That specialized in old tech scopes, and they will surely be able to answer your question. Absolutely no no doubt about it. Either that or on the EEVblog forum. Beauty. Hi to all my German viewers and the

**Dave Jones:** anonymous person who sent this one in via Deutsche Post. So, here we go. Let's have a squeeze. I'm going to get tongue at the right angle. It's important. What do we got? We got my era Every era has its

**Dave Jones:** innovations. We show you the best of them. AI and robotics It's a pamphlet. The world's biggest Oh, a world's biggest computer museum. Didn't somebody Was it the same one the Heinz Nixdorf? Somebody sent that last time, didn't they?

**Dave Jones:** Ah, yes. As I mentioned the Heinz Nixdorf Museum one of your latest videos. We thought you might be interested in our English brochure. Have a look. Our website is available. Oh, it's the actual museum themselves. I guess they got some traffic from the EV

**Dave Jones:** blog. Anyway, awesome. The Heinz Nixdorf Museum team. Thank you very much. So, if I'm in Germany again or you're in Germany, check it out. Well worth. That looks great and it's got all sorts of activities for the kiddies.

**Dave Jones:** That's fantastic. That looks great. Love it. Thanks, guys. No mail bag's complete without a like probably $1 delivered eBay item from from you guessed it China. No, Vietnam Post. Wow. Maybe maybe it is actually from I presume Vietnam instead of China. Huh,

**Dave Jones:** the exodus is happening already. What do we got? It's it's in a Oh, it's a little board. Oh, it's a right little plug-in thing ID. Oh, it's a little It's a little touch sensor. Okay, quick squeeze, but there's not much to it. There's a going

**Dave Jones:** to be a touch sensor chip on there. It's a little six-pin SOT23 jobbie. And yeah, that'll be all she wrote. It'll be like I squared C interface. No worries. Well, it turns out this is actually rather interesting. This little six-pin

**Dave Jones:** SOT23 touch sensor here, it is from a company called uh TonTec, and this is their Ton Touch uh technology. So, I've never heard of this uh company before. It's just a Chinese company specializing in ICs, and you can

**Dave Jones:** actually buy this uh chip for about uh 8 US cents from um LCSC in quantity. Um I believe this one This is the TTP223B, and I think uh well, the 223, and I believe this one is actually discontinued, but there's the like the A

**Dave Jones:** variant of it or whatever. And I thought it would be an I²C interface, but it's not. It's just got the one IO here. So, VCC can be up to uh 5.5 V, and it's designed to just simulate a

**Dave Jones:** mechanical switch, and it'll give you a nice debounced uh thing as well. So, you obviously just uh touch the thing. The actual touch sensor is on the bottom here. The actual uh pad is not on the top. And it's uh designed for up to 50

**Dave Jones:** uh picofarads of capacitance. It's got auto-calibration, um and it recalibrates like every 4 seconds or something like that. And I believe it's got like auto shutoff. So, if you touch it when you power up, I think I have to look at the details

**Dave Jones:** more, but I think it might disable that switch if it's touched when it's powered up. But anyway, yeah, it's The good thing about this, you don't have to dick around with any uh SPI or I²C bus rubbish. It just gives you a direct

**Dave Jones:** digital output that you can uh just replace any mechanical switch with a touch sensor switch for 8 cents. So, that's terrific. Let's just hook this up quickly and uh give it a bell. But yeah, we'll just lightly touch here, and we'll

**Dave Jones:** just get an active uh high or active low depending on how you uh strap one of the pins here. All right, I set up a trigger point here with 200 ms per division. If I touch that, bingo. This one's uh set

**Dave Jones:** up for a edge trigger. You can see very nice. Uh there's no switch bounce there or anything like that because there's no mechanical contact. Don't worry about the overshoot there, that's just the uh probing here. It's a bit how you doing.

**Dave Jones:** All right, let's set it to 500 ms uh per division, and let me put my finger on here, and boom, and it releases. So, yep. So, it uh stays high as long as you got your finger on there. So, we'll try

**Dave Jones:** that again. Just do a brief Whoop. Hello. Didn't work. Just do a brief one like that, and we zoom in, and of course, it's clean as a whistle. Beautiful. And uh you can invert uh the polarity of this as well, I believe. It's got a low

**Dave Jones:** power mode as well, which is quite fancy pantsy. And it draws at 1.3 microamps. So, uh you know, for 8 US cents, that's pretty nifty. If you want to just add a simple uh touch uh system, you know, a

**Dave Jones:** touch button, power button, or whatever it is, or multiple uh ones, then it get a bit expensive if you use one of these for each uh switch. There's better ways to do it. A lot of tons of micros now

**Dave Jones:** have uh touch support built in. So, you know, if you're designing a microcontroller design, and you wanted a whole bunch of touch buttons, you'd just get a micro with uh touch built in. But, yeah, if you just want like one or two

**Dave Jones:** buttons, and you don't want to dick around with any software, any micros, any buses, or anything like that, and you just want to use a direct digital input on your microcontroller, then that's a neat little um chip. I like

**Dave Jones:** that. So, it's well worth a look. I'll link it in down below. That's a winner winner chicken dinner. And of course, there's a a bit of art in designing sensor pads and things like that. The greater the size it is, the greater the

**Dave Jones:** sensitivity, but there's trade-offs and things like that. So, yeah, and there's different uh pad geometries you can do and things like that. And that might have to be a an entirely separate video because uh a lot of your more advanced

**Dave Jones:** uh touch controllers can, you know, like interference uh discrimination water discrimination if you get moisture on there, for example, that can cause a problem. Uh things like that. In fact, let me try that. Let me just put a drop of water on that. I

**Dave Jones:** don't actually have a dropper, so I'll just have to whoop. Oh, there there we go. Yeah, triggered. Triggered. I didn't put my any my finger anywhere near that, and it's still triggering. So, if I blow that away, that changed the slope of my

**Dave Jones:** trigger. Blow it away. Did it Did it go off? No, it's still there, is it? Uh is it buggered? Oh, it might have been the auto the recalibration. Might have automatically done that. If I wait long enough, maybe I can get

**Dave Jones:** it to Oh, yeah. Oh, there we go. It was doing that, so I Let me do one more little drop. No, that was That was next to it. Oh, come on. Come on, Dave. There we go. Yeah, triggered it.

**Dave Jones:** That's common. And there's some uh specific touch sensors where you can get uh discrimination against stuff like that, but that's, you know, there's pretty advanced algorithms that go into these sort of things. And the internal diet block diagram shows that, you know,

**Dave Jones:** this is not particularly a trivial sort of uh thing to do. And you know, touch sensors, when I was a boy, that was like advanced black magic stuff. Now, it's like, yeah, you can get two dozen inputs on your, you know, 50-cent micro. Give

**Dave Jones:** me a break. I don't know all my new subscribers. Uh and in particular, Scott the Duff Palm. You should know the Duff Palm. He's a fellow uh YouTuber. I'll link in his channel down below, but thank you very

**Dave Jones:** much, Scott, for sending in this. Let's have a squeeze. It says cut open here, so I am cutting open here. And the content sounds rather boring, I must say. Um so, I opened something interesting. I'm I'm it is. Let's have a squeeze.

**Dave Jones:** Happy Christmas New Year you too. Uh uh Popping the four Oh, okay, it's a cable assembly. Yes. For the calculator, the FX um 730P calculator. Let me go grab it. So for those who remember, there it is. Uh the

**Dave Jones:** FX 730P. When Scott dropped by the lab, we did a like a little mini like impromptu teardown of this and he does great repair videos on his channel. So if you want to repair stuff, um definitely check over the

**Dave Jones:** check out the Defpom and is this by doesn't It looks by No, it's only one way. Okay, see it's got a little key. Does it go over the other way? There we That doesn't That doesn't latch in at all.

**Dave Jones:** Maybe that end is going to be Jeez, no that just sits in there loosey-goosey flapping around in the breeze. I don't know. Maybe it lost some sort of a tension mechanism or it never had it. I don't know.

**Dave Jones:** And more additional detail, Defpom has set up a new website completely free by the way, mypartsbin.com which is a parts inventory site. We'll have to check it out. Cool. Also released an open source version which is free to download beauty and use

**Dave Jones:** on a local web server as well so you don't have to you know you can run it locally on your own server. None of this you know connected to the web rubbish cloud rubbish. And he'll be close to

**Dave Jones:** 10,000 subs by the time I get this. Awesome. Well, subscribe. He's also on library.io as well or library.tv or just library LBRY. I I just passed a thousand subs on LBRY. So definitely subscribe. I link I link it in every video now my LBRY channel

**Dave Jones:** down below. I'm trying to beat Barnacules. He's got like 1500 subscribers and I reckon I can beat him within the next 6 months. Cool. So, I'll link in Defpom's channels down below, defpom.com and my partsbin.com. Thanks for the extra cable. I don't have a

**Dave Jones:** printer, but if I ever get a printer, I'll be able to print if the cable ever stays in. Oh. And stupid me shouldn't press stop on my camcorder and then open another package cuz I just got through talking about

**Dave Jones:** this letter from I'm going to try and pronounce it again. Conshohocken. Conshohocken. It's probably a silent H or something in there somewhere in Pennsylvania. And so, I've got to go through the whole description again. Anyway, if you don't know, I sell my

**Dave Jones:** meters on amazon.com in the US and Canada. Don't sell it in the EU anymore cuz they're ridiculous red tape. Anyway, if you don't know, when products get returned to Amazon, they they actually get returned to Amazon, not to me. And

**Dave Jones:** then, if Amazon deem that product to be, you know, no good for putting back on the shelves because, I don't know, somebody's marked the no [ __ ] packaging box or whatever or somebody didn't like the blue holster,

**Dave Jones:** so they returned it. Apparently, Amazon's got some good return policy or whatever. And so, all these returned meters, as a merchant, I can actually log in and see this dead inventory in the bins. And I can I saw one day that there were three

**Dave Jones:** meters sitting there in there, BM235s. And you can actually get them sent back to you, but only if you have a US address. So, man. So, I put a note on the forum saying, "Hey, does anyone want free multimeters?" If you're a hacker

**Dave Jones:** space or a school or or something like that. And somebody actually Well, somebody did apply for them and then they never followed through. Anyway, the next lucky recipient is from the Aim Academy. And this is just a thank you note. They got the meters. So,

**Dave Jones:** presumably, they worked. I pretty much knew they would, but there was no guarantee. And I sent them the uh meters, there was three of them when I looked and posted that message, but then when I went to actually send them, there

**Dave Jones:** was only two. So, I I I don't know. Did somebody nick one at Amazon or did Did they deem that one went back on the shelves? I don't know what happened. So, they got two free uh BM235 multimeters,

**Dave Jones:** and that's just their thank you note. So, there's the Isn't that awesome? Aim Academy. So, it's good to see that they went to um good use. They're designing their little robot. Awesome. It's not little. Looks pretty big, actually.

**Dave Jones:** Jeez, it's a decent arm on that sucker. Anyway, awesome, guys. Thank you very much. Glad it went to a good cause. Hello to all my Greek viewers. Uh this one's from Kostas Glasd- opoulos. Sorry, I did the writing's a

**Dave Jones:** bit uh hard to read. Anyway, um it's from Greece. Thank you very much. I rattles a bit. Anyway, um it's a JLCPCB box. So, obviously they've been making some boards or whatever. I don't know. It's just It's dead. It's a wrapped in sticky

**Dave Jones:** tape. I think we can get in there somehow. Jeez, this ain't pretty. What have we got? Well, it's a kit. It's kit. Loosey-goosey parts. All through hole. None of that surface mount rubbish. Got a BIG 40-PIN DIP.

**Dave Jones:** WHOA! WHAT IS THIS? It's a Oh, it's a SCART 18 mega It's a SCART It's got SCART Oh, it's a um Yes, it's a mini PC. I think it's a mini PC thingamajigger. Um uh please visit for building

**Dave Jones:** instructions. Well, that's an A for keeping it brief. Let's go check it out. I think this will be another Sagan assembly video that'll have to be demonetized, of course, because uh you know, to to for kids. No. And if if people don't know, no, just

**Dave Jones:** having a kid in your video does not make it child directed, okay? So, technically, um you know, if I drop a few F-bombs at the start of the video, um and even if it has Sagan in it, um it is

**Dave Jones:** not a Oh god, it's not a kid-directed video. Yeah, so that through-hole jobby, um unfortunately, like I don't have any SCART cables or whatever. So, I'll have to bodge something together, but um yeah, I'm not sure if it's uh what um

**Dave Jones:** uh yeah, the PC it's emulating or whatever. I don't know. I'm pretty sure it's some sort of PC thing. Now, ordinarily, I would just uh spend like, you know, what, 5 or 10 minutes just assembling this, um but uh this

**Dave Jones:** would be, I think, a great one for um Sagan to do. So, I'm going to uh leave that, and uh hopefully, over the cuz it's school holidays now, uh we can get Sagan in, and uh he can do some more

**Dave Jones:** soldering practice, cuz he likes building little kits like this, and uh yeah, through-hole ones, perfect. So, I'll just provide a link down below, and it looks like it, you know, a kind of neat solution. It's just got uh it's all

**Dave Jones:** in an AT uh mega, and of course, the SCART is like a RGB output, and SCART's got a uh No, yeah, it'll only do RGB, will it? Well, the RGB resistor's there somewhere, but yeah, anyway, um it does

**Dave Jones:** uh like PS2 uh keyboard and RS232 as well. Oh, fancy pantsy. Anyway, runs a little uh micro uh basic, and um emulates various other things. So, that's really quite neat. But yeah, SCART's like this European thing, where you can plug

**Dave Jones:** straight into your SCART TV. Don't have many of those here. Thanks, mate. That was just the DHL guy. And my friendly Nixon, his name is. Beauty. Anyway, um very friendly guy. Uh to What What have we got here? Oh, okay,

**Dave Jones:** Wait. Okay, our favorite thing. Thank you very much, Andre L Becanin in Richmond Hill in the United States of America. Been released from biosecurity control. We're pretty serious about our biosecurity here in Australia. All right. Open for inspection. There it is.

**Dave Jones:** Australian government. Good on you. Is that border force? Australian government. No, I don't know. It's the part department of been inspected by the department of agriculture. No, that border force rubbish. You know, if you come to Australia now, you're met by

**Dave Jones:** border force. Jeez. Anyway, yeah, well, they didn't take offense to the mouse pad. Um Anyway, what do we got? We have our favorite thing on the EV blog, a multimeter. It's a true RMS multimeter apps designed for It's a It's a Bluetooth hobby. IDM M

**Dave Jones:** wireless app 50,000 count. Jeez, that's pretty good. So, it's got to be a $100 plus meter. We'll check it out. Can't do a full review on the mailbag, of course, but it even states on the website not compatible with iPhones. Love it. So,

**Dave Jones:** thank you, Andre, for sending in this meter. It's around about 150 Yankee bucks. And I do actually recall this now. Some people on the EV blog forum, that's where you go to talk about test instruments, the best place on the

**Dave Jones:** interwebs. So, this is PDI branded, but it is just a Kyoritsu Kyoritsu manufacture meters for Extech and all sorts of companies. So, it's got IDM M wireless app, wireless data logging, Bluetooth. It's got true RMS, frequency, peak capture mode, double molded case,

**Dave Jones:** 50,000 count. So, it's high resolution, which is quite nice, waterproof and dustproof, which is quite jazzy, and 2-year warranty from PDI. So, you know, a little It's quite small. Let's crack it open. So, it comes with a little

**Dave Jones:** pouch. Oh, PDI have got their own pouch. Thank you very much. And comes with the leads, comes with the croc clips, comes with the magnetic hanger attachment. That's quite nice. And the K-type thermocouple lead. And looks like, you

**Dave Jones:** know, bog standard Chinesium probes. And it's just the plastic plugs to make it waterproof, of course, when you got the probes in there. And the two extra plugs, it, you know, it's supposed to be waterproofy. Ah, doesn't instill a lot of confidence,

**Dave Jones:** does it, with the ah the Chinese QC pass sticker. Ah, no, that just It looks That's all Let me put a bit of bit of spit on that. It's got all the genuine China dust on it. So, yeah.

**Dave Jones:** Terrific. Comes with a battery. Ah, it's on. Now, the specs aren't going to set the world on fire. Let's have a look. Do you know I'm not going to test any of the wireless stuff here today, so, yeah,

**Dave Jones:** don't ask me. Whilst it has the kind of spec you'd expect 0.06%. Usually, you know, they aim for 0.05 plus nine digits. You know, it's a bit high, but that's on 50 mV. So, 50 mV range. Wow, 50 mV range with

**Dave Jones:** 50,000 count. That's very nice. Thank you very much. That's plus four digits, so, you know, the DC spec is quite nice. But, of course, AC RMS 1%. That's what you'd expect. But, the DC current, unfortunately, no, it's not up there. 1%. So, that's,

**Dave Jones:** you know, that's really down at your, you know, your base level three and a half digit meter kind of spec and AC current. And your resistance, you wouldn't buy this for the accuracy. You're buying this for the resolutions.

**Dave Jones:** And the rest of them, for those playing along at home, not that fast. Oh, it's a What? 40,000 count. 40,000? I thought it was 50,000 count. Where did I read? Yeah, 50,000 count. 40,000 count. Make up your mind.

**Dave Jones:** Cat 3,000 V, Cat 4 600 V. Ah, yeah, okay, but it doesn't have any UL, you know, independent or ETL independent testing. So, you know, I'm not going to be If you really need a Cat 4, you know, 600 V

**Dave Jones:** rated meter, get a proper one, not a, you know, a proper, rated one, not a Chem one. Anyway, IP67 waterproof and I assume it's fused. Yeah, 500 milliamps and 10 amps. Thank you very much. And I don't actually mind

**Dave Jones:** the meters with a center off like this. It's a bit unusual, but the good thing about it is that if you turn it this way, it's all current. If you turn it this way, it's all your, you know, your

**Dave Jones:** voltage, so you can't blow it. So, in any of these positions, you shouldn't be able to blow the thing up by connecting to any voltage source. So, you know, it it has its pros and cons, but I don't mind that at all. And

**Dave Jones:** there's our display. It's quite a a decent Don't mind the look of those digits. Sorry about the glare and stuff like that, but, you know, that's all right. And if you compare that to a BM235, it's not fair, of course. And this has

**Dave Jones:** practically some of the biggest digits in the business, but, you know, that's that's quite a readable display. No worries. These probes, I swear I've seen them on dozens of other meters. They just come out of the same random Chinese

**Dave Jones:** factory and they're, you know, they are what they are. So, I wouldn't write home to my mom about them. Anyway, let's have a look. I think they had No, it didn't have input jack alert. Nope, no input jack alert, no

**Dave Jones:** beeping. Anyway, that looks like really fast updating there in AC mode. Wow, that's pretty jazzy. No worries in that. Yeah, that's DC mode. And range, oh, now we'll have to switch over to millivolts. Supposedly has a 50 millivolt range.

**Dave Jones:** There it is. Look at that. Woah. Hop, it shows precisely zero. That's a bit Well, no, it goes overload as you'd expect. Um and then it showed precisely zero. It's wide open down. But why it showed precisely Yeah, like it locks in at zero

**Dave Jones:** there. So, not sure what the deal is there. That's a bit strange. And then it jumps to overload again. Hm. Anyway, it is stupidly quick updating for a 50,000 count meter. Anyway, the the beeping sounds a bit sad.

**Dave Jones:** It's like it's like it's about to die or something. Anyway, let's check the continuity. No. Oh, that's terrible, Muriel. And it is latched, but no. Let's try that with gold probes, which is going to be better for the purposes of this sort

**Dave Jones:** of testing. Oh, yeah. Actually, yeah, it's not as bad. Yeah, that's that's pretty good. I can occasionally make it skip. That's okay. I'd say that's okay continuity test. And capacitance, almost bang on. That's resistance there. That's good enough for

**Dave Jones:** Australia. And 10k. Now, let's count down a bit. And put the Yep, good enough for Australia. And auto range speed, let's go. Well, that was really quick, wasn't it? Hang on. Wow. Oh, that was That's instant. That instantly goes to zero. I don't think

**Dave Jones:** I've seen a faster Hang on, let me get the other probes. Let's try this again. I don't think I've seen a faster auto ranging meter. Ready, set. Wow, that's straight in there. I didn't even see that range. That's nuts. It it ranges slowly back.

**Dave Jones:** It takes its time going back, but wow, that's really impressive. I wonder what chipset they use. That's that's ridiculously good. Wow. Is that like the best on the market? Anyway, I couldn't be bothered warming up my other gear to, you know, test the accuracy

**Dave Jones:** specs and things like that. Um if you want to see a full review, we'll see it, but I'll just crack this open now. There was no captive uh screws on the back. One just flew across the room, so let's

**Dave Jones:** try and How do you bloody well get this Uh that's annoying. Anyway, golden power golden shower battery um long life green energy. Yeah, right. Toxic waste in there, no doubt. Um 9-V battery, a lot of people don't like 9-V batteries in their multimeters,

**Dave Jones:** but nah, you know. Seriously, you get RSI in your hands just trying to get these screws out because they're going to be O-ring sealed and all that sort of jazz and they're super duper long because this thing's waterproof and

**Dave Jones:** uh jeez. All right. So, crack this turd open. And we're in like Flynn. What on earth is that? What Oh, that's a Oh, that's a That's a big uh resistor array. Wow, that's not like your traditional ceramic uh you know, former one. That

**Dave Jones:** Wow, that is that is remarkable. Um I don't think I've ever seen anything like that. Anyway, they have tried to shield that. Have they tied it down? Yeah, look, they've soldered that down. They soldered that down to the top of the

**Dave Jones:** crystal. And then is the crystal can connected down? Is I'm going to I might have to measure that cuz if it's not, well, that's a bit how you're doing. Um anyway, I do like Look at the cutouts in there. That's

**Dave Jones:** very nice. That's really neat. Um liking the surface mount diodes there. That's quite nice. Anyway, got a ceramic fuses. Um your typical uh 500 uh milliamp and your big uh Seba brand one. No wackers. So, that's pretty good. I do

**Dave Jones:** like the battery uh contacts there, but anyway, that That's a That's another big ass diode. What the And that's a through Is that a through hole? Surface mounted. That's a through hole that's been bodged to a surface mount.

**Dave Jones:** Okay, you know, fair enough. Anyway, there's our 10 amp current shunt. That's bent right over on the side. That's a bit how you doing. Um look at all the solder in there, but you know, look hey, it's got no shortage of

**Dave Jones:** protection. Um don't worry about that. Look at this. Three MOVs, three PTCs, and a plus your uh diode bridge and this other diode over here, whatever that's doing, but it's big and beefy. Um so, yeah, no wackers. So, it might actually

**Dave Jones:** do okay on that front, but uh as I said, whether or not it meets the standard hasn't been independently tested, and K and M aren't really known for um you know, their um highly rated uh meters, you know, so anyway, there's

**Dave Jones:** our Bluetooth module for those playing along at home, and let's go down in. That would be a That would be a just a nice squared C memory, I'm guessing. Let's have a look at the chipset. Well, that's a HY3131.

**Dave Jones:** That's interesting cuz that's the same chipset that's used in the 121 GWEV blog meter and also the Keysight uh U1282A as well. And that's um And both of those meters are sort of, you know, kind of little bit notoriously slow on their uh

**Dave Jones:** auto on their ohms auto ranging. Um so, how they've been able to implement this, I think I might know. I think they might be using the because it does have a 50,000 count mode and a 5,000 count mode

**Dave Jones:** and they might be switching to the 5,000 count mode for the initial thing. Anyway, which gives you the faster auto ranging. So, but it doesn't display 5,000 counts. It gives you the 50,000. So, they're their their software engineers, I think, have been quite

**Dave Jones:** clever to implement that ridiculously fast, practically instant ohms auto ranging. So, I'd love to see their software and know how they do that and I reckon we've just got an arm jobbie in there, do we? I'm not going to It's an

**Dave Jones:** atmel ATmega. It's not an arm. It's an ATmega processor. That's interesting. Anyway, so that's a rather interesting looking side. I'm not going to go further. If you want a full review of this, please let me know down below. But

**Dave Jones:** for 150 US bucks, it's an interesting price category. And I mentioned this on the forum, actually, I am looking at having another meter that's coming out very shortly that will be in the $150 US, of course. We're always talking US dollars, Yankee

**Dave Jones:** bucks. Price category. In fact, I could potentially sell it under 150 US bucks and it's 60,000 count and it's it's going to be sort of, you know, it's half feature set sort of halfway between the BM235 and the 121GW.

**Dave Jones:** So, please let me know in the comments if you're interested in that sort of price category. Think of it as a as a sort of like a beefed-up BM235. It's physically larger. It's got the electric field detection. But it is the higher

**Dave Jones:** count and it's got much better accuracy. We're talking like 0.05% DC and also 0.075% DC current and uh less than sub 0.1% ohms as well. So, yeah, it's not bad. So, it's an interesting sort of price category. You know, you jump up to your

**Dave Jones:** 200 buck price category and yeah, you've got the 121 GW, you've got the among others. So, anyway, it it won't have Bluetooth, of course. This one's got Bluetooth. So, anyway, it's it's an interesting meter. So, yeah, might warrant a full review perhaps. I mean,

**Dave Jones:** it's it it construction quality is kind of what I expect in a cam meter. It's okay, you know, and but it's nothing to write home to your mom about and it's kind of fast. So, yeah, let me know if you want a full review.

**Dave Jones:** Anyway, I'll link it in down below. Jeez, this one's pretty heavy. Comes from Australia. No name. Thank you, No Name. Call you Deep Throat. For those young whippersnappers won't know what I'm talking about. What have we got? Been cleaning out some boxes ex-work

**Dave Jones:** ex-work junk from the roof space. Used from Telecom Australia special service network. Thank you very much, Mark. Mark Wright. Oh, look at that. It's a what's a tele-meter? It's got some great counter modules in there. They they'll likely be stand-alone counter modules.

**Dave Jones:** They're great. Always good to have them in the jumping there. They're actually very useful. And we've got a whole bunch of boards and stuff. So, we'll have a quick squeeze of these up close. I just got the block diagram on the back. Wow,

**Dave Jones:** 2 watt HF hybrid amplifier. Check out this Bobby Dazzler. Look at the cream case on this Telecom Australia, none of this Telstra rubbish. Telephone meter type three date '87. Wow, made in Japan. All the best stuff's made in Japan.

**Dave Jones:** Ah, just isn't that beautiful? Did that reset that? I wasn't watching. I think it might reset that one and that's the total. So, woah, it's another button. No? What's that? I don't know. Looks maybe that was another button,

**Dave Jones:** perhaps. That is a gorgeous feeling button. Oh, I wish this was feel-a-vision. Anyway, this comes from the Telecom Australia special service network and let's crack it open. Have a look at the gorgeous little counter modules in there. Old school screw

**Dave Jones:** terminals, brilliant. And it all just sprung open. Wow, look at this. This is great. Oh, that just all it all just sits in there. Look at that. Giant solenoid, absolutely enormous. Oh, there we go. Oh, that's that's how it ticks over. There you go.

**Dave Jones:** So, just apply one pulse to the coil and it's just going to count up like that and you can reset this one down here. Ah, beautiful. That's a Nichicon cap. Thank you very much. There's not a lot in there, is

**Dave Jones:** there? Just a some sort of NEC What is that? I don't know. An op amp job. What's up the top? A UC177, once again, NEC. And got a sort of a spark gap there. A little [ __ ]

**Dave Jones:** down the bottom. There's not a huge amount in that at all. It's just counting um, you know, telephone line pulses or whatever. It's a some sort of like call counter, maybe. Now, unfortunately, the problem with scrapping this particular one is that

**Dave Jones:** this is not really a usable module. I thought they might have like your your traditional modules like this are just like a black module like that that you can embed into any project and things like that and you just apply a pulse in

**Dave Jones:** and it just mechanically counts like that. And well, this one's not really a usable module, is it? It's really a custom-designed bit of kit. So, fortunately, um that's not something you could really put in your junk bin. And if you feed a 12-V uh

**Dave Jones:** pulse into it, uh you can feed a square wave, but I'm feeding in a 100-ms pulse every second. If you go down to 10 ms, it it doesn't work. In fact, let me ramp down the pulse width time here down at

**Dave Jones:** 50 ms now. Still ticking over. Let's try 25. Oh, you can see it. Little tiny flicker there. Not enough. So, 25-ms uh 12-V pulse is not enough. Uh 30 it just starts to kick in. So, there you go. So, there's a 5-Hz pulse. There you

**Dave Jones:** go. Five times a second. I love it. Can't really do a huge amount more than, you know, five or 10 times a second. It's just not going to do it. And that's 10 Hz. I can play with this all day. I can just

**Dave Jones:** let this sucker running. Uh 555. And this is a Tel Spec 2-W hybrid amplifier. I like a little handle on here, so you can pull it out of the uh rack like that. And I love the uh multi-ganged

**Dave Jones:** um DIP switches here. They're They're really quite cool. If you haven't seen those before, they're like, you know, this could be triple width. Is it? Four switches wide there. So, you can actually switch four at once. Absolutely brilliant. Um

**Dave Jones:** and that would be a two-way one. And these are your traditional single-way ones. So, I got no idea what this does. Um Tel Spec Proprietary Limited are the ones who uh designed this sucker. And there is a block diagram on the back.

**Dave Jones:** So, I don't know. Test access 600 ohms. I don't know. It's a telecom-y thing. Um it needs 2 W cuz it's I don't know. It's got to do a lot of driving. Is that like the line load resistor or something like

**Dave Jones:** that? I don't know. I'm talking out my ass. I don't know Telecoms, but yeah, 3 kHz, 800 Hz are your typical Telecoms frequencies and little plug-in boards. I was going to say that we're still in the age of little color dipped ceramic caps,

**Dave Jones:** but that says ah, so that's probably some little thermistor-y thing, I would assume. These little sockets here are interesting. They come with these little little plugs and they can't like you have to they can't go in that orientation because the pins are

**Dave Jones:** rotated. So, you've got to rotate the whole thing around and plug it in. That's fascinating. Why would they go to that effort? Is there I assume that's just a shorting link. I'll measure that. Yep, shorting link. We've got a baseband

**Dave Jones:** data amplifier. So, I'm sure all the Telecom wizards out there are going to all the Telecom greybeards are going to tell us what this is. AWA, look at the old logo there. Ah, it just brings back memories. Those

**Dave Jones:** were the days when Australia actually had an electronics industry. Yeah. Anyway, nothing doing there. The only interesting thing here is SOT, SOT. That's not as in like SOT 23. That would be almost certainly select on test. So, yeah, they're not populated, but I'm

**Dave Jones:** pretty sure that's what the SOT there would stand for. Little 10 turn trimmers in there. We'll just run through all these quickly. A 2 W voice switched amplifier. So, wow, look at that. Beautiful. Custom transformer jobby. Once again, Tel spec. Are they still

**Dave Jones:** going? Doubt it. Like the fuses over here. Nice. Signaling loop extender. Longitudinal noise rejection and ring boost enable. Earth recall sense circuit. Wow, you know, all this telecoms infrastructure is quite complex. When you can like all these modules and designs are going to

**Dave Jones:** rack and make up a voice telecoms system, I guess. Now it's like it's all done on one DSP, isn't it? Baseband data amplifier. Oh, IT'S A SURFACE MOUNT. OH, NO, THAT THROUGH HOLE RUBBISH. WOW, that's advanced. We've got a date code on there.

**Dave Jones:** They just TL074s, though. Nothing special, but wow, they went with went with surface mount. Couldn't Maybe they couldn't get surface mount bridge rectifiers there, so they use the old through hole bridge rectifiers, but yeah, and a couple of big beefy diodes

**Dave Jones:** up there for protection, whatever that is, and some multi-gang switches yet again, but see the advancement in technology. Installation instructions for an AF FHA mark two, June 2001. So, you'd expect it to be fancy pantsy, and it is. Oh, look at that. Looks like

**Dave Jones:** we've even got a programmable device up here. Oh, we've progressed to surface mount tants there. Oh, look at the big Look at Wow, that's interesting. Those big uh hybrid resistors there. Wow, and a big jumper wire in them.

**Dave Jones:** That's interesting. Anyway, are they like 600 ohm you know, line terminators or something like that? Anyway, look at the big mob protection. They're beasts. That's not surprising, you know, it's got to survive lightning strikes and stuff like that, so you got

**Dave Jones:** to absorb all the jewels, and uh fair income relay in there, and the caps would be top quality. Yeah, Nippon Chemi-Con, no wackers. Oh, it's an Atmel. The Atmel fanboys they go wild. They go wild. 2001. And it's the old 89 LS series.

**Dave Jones:** Brilliant. Yep. None of this AT mega rubbish. So, yeah, you can see how by the 2000s they've they've really progressed. Of course, they you know, they keep all the same form factor and everything, but you got to plug into the

**Dave Jones:** existing racks, but yeah, they do modernize this. I'm not sure what the not sure what the micro would be doing there exactly. Not sure what this card actually does. Made in Australia. Made in strayan. No wuckers. And from the

**Dave Jones:** modern to what looks like the ancient. This is an attenuator. Look at the big ass power resistor there. Wow. It's an absolute whopper. And some big jobbies over here with their little uh little they're ceramic ceramic standoffs. Oh,

**Dave Jones:** I'm getting a bit of a woody. And some sort of resistory hybrid action going on in there. And a couple of [ __ ] Um [ __ ] one. Yeah, see the date code though. That looks like 84 by the looks of it. And

**Dave Jones:** this jobbie no idea what that's doing. Doesn't tell you. That's an 83 job. Just a bunch of [ __ ] And a bunch of well, [ __ ] again. Transformers and transistories. And that's a plezzy. That's a plezzy job. Wow. Wow,

**Dave Jones:** seriously, the print on this label is so small I cannot read that. That is ridiculous. God, I'd need a magnifying glass. So, thank you very much whoever sent this one in. It's a rather interesting size. It's a like a torque is it a torque

**Dave Jones:** wrench? LOOKS LIKE A SPECIALIZED OH, NO. OH, IT'S A SENSOR INPUT. OKAY. SO, it's a sensor um like wrench to sense how much force you're putting on things. Very important in you know, military and other you know, and NASA would probably use these for

**Dave Jones:** you know, space probe. Every nut's got to be you know, talked up by X amount in your rocket or whatever. Um and the Church of Tesla, realize your potential. The Church of Tesla. Yeah, there's a lot of Tesla fanboys out there. Oh wow,

**Dave Jones:** another one. And that that's a smaller one. Cool. Not sure how tear downable they're going to be, but um yes, these are a thing. Wow, that's enormous. Wow, that's huge. Yeah, and they've all got like little uh you know, Lemo

**Dave Jones:** connectors in the end and they and they'll be like a like a strain gauge output. And I've got a Church of Tesla button. I hope it's not like over unity crap. Because unfortunately, when you're a Tesla fanboy, it kind of like the

**Dave Jones:** connotations are that it's like yeah, free energy over unity, all that sort of jazz. So, I mean you know, you can be a fan of Tesla uh for his work, but yeah, they're the connotations these days. Look at the

**Dave Jones:** knurling. That's got purple knurling on it. Ah. Beautiful. Bobby Dezler. So yeah, it's a talky type wrench. Um although it's like it actually measures it doesn't looks like yeah, I did like it doesn't actually have like work like a real uh torque

**Dave Jones:** wrench. It's actually uh just a data output one. And for those playing along at home, RS Technologies. Uh no, that would not be um RS components. Anyway, individually serial numbered at 100 lb per inch, I guess, is the metric for that. And it's

**Dave Jones:** got a data interface. Um I don't like our chances of getting this apart, though. And that is all we can get out of the end there. That's interesting, isn't it? That's got something in there. That looks kind of weird. I'm going to

**Dave Jones:** cut that open. I'm going to tell you what, that looks for all the world like a strain gauge, but what is a strain gauge doing in in line in a cable in a heat shrink? Like, what? I don't get it. Aha, although this is

**Dave Jones:** designed by and manufactured by RS Technologies, these are actually well, one of the resellers is a PCB Piezotronics and they essentially rebadge these and PCB Piezotronics I'm intimately familiar with because that was one of my jobs was doing lots

**Dave Jones:** of acceleration and drop testing and stuff like that. So, this this is a PCB Piezotronics accelerometer, a tiny little accelerometer that you put onto your object that you're trying to measure the vibration or shock response of and you can play around with those. I

**Dave Jones:** might do a video on that one day actually building a little amplifier for it and stuff like that. Anyway, yeah, basically this is going to have a Wheatstone bridge in it and I've got the data sheet here for it and we

**Dave Jones:** can have a look at the specs. So, it's basically a bridge a Wheatstone bridge in there which then we need a proper amplifier. I've designed those back in the day. I don't think I have one here. So, you know,

**Dave Jones:** we're not going to get, you know, really good results from trying to power this thing up here on the Mayo bag anyway, but yeah, these are like real expensive bits of kit and you can get like these little handheld

**Dave Jones:** amplifiers and display readouts for them so you could do like, you know, field testing. You get under your your Boeing aircraft or whatever and you check the torque on each one of the bolts and things like that and you mark

**Dave Jones:** it down and or you can automatically record it and things like that. So, yeah, these are these are very valuable bits of kit. These are sensing torque wrenches, although they're basically a transducer torque wrench. They don't actually do the talking

**Dave Jones:** themselves. You've got to either for like a post torque inspection kind of thing or you do it by hand until until you get that exact reading you want on the display. So that's very cool. Thanks for sending those in. The

**Dave Jones:** others will be identical and I can't see any way I think it can actually screw the inner part of that out or something, but I haven't really had any luck with getting this apart. Anyway, they'll just be a Wheatstone bridge strain gauge

**Dave Jones:** in there and there's no internal circuitry at all. Be taking it straight out. But I still don't know what the heck's going on there though. Although on second thought, is that some sort of like little temperature sensor and it's

**Dave Jones:** doing some sort of temperature compensation? Perhaps? Hmm. I think we've got a second suck of the sav. This is from Keva guy. I remember the pronunciation which I goofed in the wrong one in the previous video. That that was like was

**Dave Jones:** that literally the last mail bag? Anyway, thanks Kev. But you know, you got to be careful sucks of the sav. Can't have too many.

**Dave Jones:** Is it actually something from a Digikey? Oh, it is. I think it is. Although I rather like the look of it. It is a very nice wire wound resistor. She's hollow. It's on a ceramic former and why have I got a WIRE WOUND

**Dave Jones:** RESISTOR? OH, YES, OF COURSE BECAUSE IT this is just a Digikey receipt because I didn't have a powerful enough uh well, not power Yeah, I did I didn't have a high wattage one. This is a high This is a 100 W 1K resistor suitable for

**Dave Jones:** testing Kev's um Nixie tube high voltage 180 V uh load thing. So, he sent me the matching resistor. Nice. Thanks, Kev. Actually, more to the point, this is an adjustable resistor. See this lug in the middle? You literally screw that in to the point

**Dave Jones:** along there you want, and that will give you your resistance value anywhere from 1K. Thank you very much, Rob K. Um this is like eight, yeah, Chinese e-packet um thing. It says Oh, I won't spoil it. Let's open it up. I don't know exactly

**Dave Jones:** Doesn't really spoil it for me, either. I don't I know what class of item I'm getting, but I don't know exactly what or what type of item I'm getting, but uh what it is. So, what we got? User manual. Oh, no, it's

**Dave Jones:** not Sorry, I thought it was something else. I thought it was a display for that um CRT uh scope that I'm I'm still have to upgrade. Anyway, we've got a a cheapo DSO oscilloscope. This is like one of

**Dave Jones:** these, you know, I don't know, 30 buck DSO oscilloscopes, something like that. So, yep. Ooh, check it out. I'm going to do a quick power up. It's not going to be a full review, of course, but we'll have a

**Dave Jones:** play. Now, this is a little open-source uh do-it-yourself kit oscilloscope. This one comes a fully assembled. It's probably the cheapest uh oscilloscope, in quote marks, you can actually get. Um I can get this on eBay for 23 Australian

**Dave Jones:** dollars assembled, delivered. So, it's Anyway, I believe this is a clone one, in quote marks, um because it's I believe the original, please correct me if I'm wrong, is done by uh JYE Tech, but this one doesn't have like the same logo as the original,

**Dave Jones:** I guess. Um but, it is open source, so anyone's allowed to uh actually produce this, really. Um so, yeah, it's just a little Well, let's have a look. So, as I said, it's actually a kit, and this one

**Dave Jones:** actually the instructions are really quite nice. Look at this. I I really like this. So, as like a beginner kit, um you know, it's cheap enough to uh get for this. And there's a troubleshooting flowchart as well. So, huge thumbs up to

**Dave Jones:** the uh documentation for this thing. Absolutely brilliant. Whether or not JYE Tech did that or the company that sold this one did that, I don't exactly uh know, but there's no JYE Tech uh branding on this. And there's the uh

**Dave Jones:** schematic. For those playing along at home, it's basically just an um micro and a little bit of an op-ampy uh front end. And the specs aren't anything to write home to your mom about. Let's have a look. One meg sample per second. Uh

**Dave Jones:** 200k analog bandwidth. 10 millivolts per division to 5 volts per division. 50 volts peak. It's got a standard 1 megohm input. Um and it does have a BNC. So, you could presumably use standard probes with it. Um it is 12-bit resolution,

**Dave Jones:** though. Um 1k of sample memory, but, you know, like yeah, it's uh this would have been kind of novel like 25 years ago. Like it would have been useful, but I think you know, you can argue it's still

**Dave Jones:** useful these days. Okay, for the you know, what else can you get for you know, 25 uh bucks and delivered or possibly even less from that. I haven't even looked on AliExpress yet. So, anyway, um yeah, the form factor there

**Dave Jones:** are I think the JYE Tech one comes with like Perspex uh cover on it or something like that, and it's a bit more expensive. It's in the 30s of uh dollars range, but uh and Yankee bucks at that.

**Dave Jones:** So, anyway, there's a USB. That's for power, is it? I don't think it actually does. Can you get data out of it? Well, it turns out you can't power it from the USB. That's pretty disappointing. You got to power it from

**Dave Jones:** a 9-V DC up here. It doesn't have to be 9-V DC. It's just got a 78 L05 and series diode protection there, and that's about all she wrote. So, just 5-V rail. That's dropping down to 3.3, but yeah, the USB has just got a test point

**Dave Jones:** on there. Can't power it from that. All right. So, I've got a 12-V input, even though it says 9 V. The cap's 16 V, so I think she'll be right. And yep, by JYE Tech. There you go. So,

**Dave Jones:** it does actually has the firmware for it. Attention, you can verify kit authenticity. There you go. By sending Let's Let's Let's have another look at that. There you go. So, but it is open source, I believe. Do not help fake.

**Dave Jones:** Please report fake kicks and kit seller. This saying is legal to run this firmware from SainSmart. Oh, there you go. So, yeah, I guess JYE Tech aren't happy that uh people have been cloning this sucker. Anyway, that's a nice update uh

**Dave Jones:** speed on there. Don't mind that. Let's plug some signals in. And there you go. There's a 1-kHz 4-V peak-to-peak sine wave, and not sure what that little kink is in there. That That's not my function gen. So, something's a bit how you doing there.

**Dave Jones:** And it's like you can really see that. It is quite quite sharp. So, yeah. Okay, it doesn't go crazy when you change the gain there. And there we go. Looks a bit better there. Oh, there we go. That's nicer.

**Dave Jones:** That's nicer. So, looks like I'm 0.1. Looks Yeah, see? That gives you some sort of weird thing happening there on times five, I I sensitivity times five gain. So, Oh, it is times five? You'd think that'd be greater, but it

**Dave Jones:** gives you less. Okay, it's back to front. Well, it's back to front what I think it should be anyway. So, yeah, it's very simplistic, but hey, you know, it works. But, yeah, like there's no real controls. Okay, plus,

**Dave Jones:** minus. Okay, that's our time, but like it would have been better if they were labeled a bit better. We'll start to see some aliasing, will we? Way! Oh, yeah. Look at that. Terrific. That's really aliasing. Look at the low frequency signal, that's

**Dave Jones:** aliasing, too. Wow. Wow, that is a sine wave. It's going to do that as a sine wave. Oh, sorry, glare on the screen. It's going to do that. Yeah, that's that's terrific.

**Dave Jones:** So, select, we've got auto. Haven't Haven't read the manual at all. Positive, negative trigger. Don't know how do you change that. There we go, positive or negative trigger. No wuckers. You know, it's like it's really basic. We've got some trimmer compensation caps

**Dave Jones:** up here and stuff like that. Like, you know, it's great for a beginner. Hey, you know, for your 20 bucks or whatever, you can get this like sub 20 bucks to build this up as a kit. Like, yeah, it's

**Dave Jones:** going to be a nice little kit to build. Combination of surface mount and through hole stuff and things like that. Let's actually take the Can we Is that Is that soldered in? No. So, yeah, if you get that as a kit, um

**Dave Jones:** or is all the surface mount stuff done and you only do the through hole? Yeah, I think it's only the through hole stuff on there. I think it might come Yeah, pre-surface mounted and then you've just got to

**Dave Jones:** um yeah, assemble the rest of it. So, you know, it It'd be nice if it actually came with uh you Maybe some people out there do sell a kit where uh you know, it has surface mount and through hole.

**Dave Jones:** So, you know, that'll be quite a a challenging little kit for a uh a beginner, especially with uh the relatively fine pitch uh quad flat pack in there. You know, the SO is a fairly easy, but uh yeah, that'll be

**Dave Jones:** that'll be a nice little uh do-it-yourself kit. Look, it's you know, I'm not even going to bother to like check the specs and things on this. It's just you know, it it's a 20-buck little kit oscilloscope. What do you want? And

**Dave Jones:** you know, it it does all right, I think. Anyway, good on JYE Tech. And uh they're obviously not happy about people cloning it, but uh I mention I saw mention of open source somewhere, but maybe it's not uh maybe people have just

**Dave Jones:** cloned it. And uh yeah, but you know, nice sharp trace in there. And 100 kHz bandwidth. There's our 100 kHz. Oh, it's not triggering too well, is it? I didn't change anything. I just uh It's 100 kHz. Oh, it doesn't like that.

**Dave Jones:** Let's go to 50K. Oh, it still doesn't like that. I assume that's the trigger point over there. So, it's got hold mode, running mode. Yeah, really doesn't like to trigger on the even 50 kHz. Let's go down to 10 kHz.

**Dave Jones:** And oh yeah, we're triggering at 10 now. So, yeah, the user interface is clunky and its bandwidth is, you know, audio bandwidth basically. And but hey, neat little kit. I'll link it in down below if you want one. I'll try and link

**Dave Jones:** it to the uh genuine um store. So, yeah, you know, that's that's really neat for the price, really. Yeah, especially like these things are insanely cheap these days. I mean, to get Imagine like 25, 30 years ago to get something like this.

**Dave Jones:** This would have been magical. So, thanks for joining me for another mailbag, probably the last one for the year, almost certainly. Um and yeah, I will be taking some time off in January, so I don't know what's going to happen there,

**Dave Jones:** but anyway, if you like the video, please give it a big thumbs up. And as I've been saying lately, please subscribe to me down below on uh library.tv, l b r y.tv. I'll put the link to my channel down below. I've

**Dave Jones:** cracked a thousand subs and I'm trying to beat Barnacules and uh he's got like 1,500 subs or something like that. So, yeah, I I will do a video on uh library.tv um relatively soon promoting that. So, yeah, I think it's a really you know,

**Dave Jones:** it's coming along as a really good decentralized uh content alternative to YouTube. So, yeah, it's really coming along. Check it out. Catch you next time.
