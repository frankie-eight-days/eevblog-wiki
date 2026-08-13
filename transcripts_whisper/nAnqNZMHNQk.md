---
video_id: nAnqNZMHNQk
title: Electronex Expo 2011 - EEVblog #207 (1 of 3)
url: https://www.youtube.com/watch?v=nAnqNZMHNQk
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 35, "3": 49, "4": 59, "5": 76, "6": 176, "7": 191, "8": 209, "9": 228, "10": 246, "11": 268, "12": 287, "13": 303, "14": 327, "15": 341, "16": 365, "17": 386, "18": 404, "19": 423, "20": 457, "21": 481, "22": 497, "23": 515, "24": 527, "25": 545, "26": 561, "27": 580, "28": 593, "29": 612, "30": 626, "31": 645, "32": 664, "33": 684, "34": 704, "35": 719, "36": 740, "37": 777, "38": 795, "39": 815, "40": 841, "41": 867, "42": 890, "43": 904, "44": 921, "45": 940, "46": 958, "47": 977, "48": 994, "49": 1012, "50": 1029, "51": 1056, "52": 1080, "53": 1103, "54": 1117, "55": 1134, "56": 1151, "57": 1169, "58": 1186, "59": 1202, "60": 1221, "61": 1242, "62": 1280, "63": 1312, "64": 1338, "65": 1356, "66": 1370, "67": 1387, "68": 1408, "69": 1468, "70": 1499, "71": 1522, "72": 1542, "73": 1572}
---

**Dave Jones:** Hi, welcome to the EEVblog, an electronics engineering video blog of interest to anyone involved in electronics design. I'm your host, Dave Jones. I'm not even inside yet, I haven't even registered, and somebody already came up to me and shouted out, Great Scott, and he wins a multimeter.

**Dave Jones:** It's Phil. Hey, Phil, how are you doing? There it is, there you go. It's not brand new, unfortunately. It has been reviewed, but it should be a winner. So, you're here for the show? Here for the show, yes. Excellent. And? Representing La Trobe University.

**Dave Jones:** Oh, okay, you're from La Trobe. Excellent. Department of Physics. Excellent. And they gave you time off? Sure, yep. Okay, so you work there or are you a student? I'm a technician now. Okay, excellent. I'm a technician, so hello to all the students that are watching Dave's EEVblog.

**Dave Jones:** Excellent. Well done, mate. You shouted out, Great Scott. You weren't embarrassed? You came up and shouted out? I was embarrassed, but I shouted out anyway. Awesome, well done. Thanks. Thanks very much. See ya. Cheers. I ran into an Amp Hour listener, Travis here.

**Dave Jones:** Hey, Travis. Hey, David. How are you doing? Good, mate. And look, he was inspired by Carl Sagan, by My Little Baby Sagan, and he's got contacts. Everyone loves contacts. Beautiful. Fantastic. Thanks, Travis, for doing the show. No worries. Nice to meet you. All right, and say hi to Chris.

**Dave Jones:** Hey, Chris. How are you doing? Huge Amp Hour fan. Thank you. Great stuff. Thank you. Cheers. Cheers. And I'm here at the Emona stand with my mate, John South. Hey, Dave. How are you going? Hey, good. And what do you guys carry? GW Instec?

**Dave Jones:** Yep, we've got the Rigol range, obviously, but we've also got some new product from GW, which is the new GDS. Which we'll take a look at in a sec. The new GDS scopes. Other new product that we've got here is a little new non-invasive current probe system from TPI, which we can show.

**Dave Jones:** Some new active differential probes as well, oscilloscopes, and obviously our general purpose range. All right, let's check them out. The new range of GDS 3000 BPI oscilloscopes. Two and four channel from 150 meg to 350 meg bandwidth. It's got a very high update rate, coupled with intensely graduated display.

**Dave Jones:** This is basically a video field signal that we're seeing intensely graduated display on them. They've got a range of advanced trigger facilities, including some serial bus trigger. They've got also some power measuring capability, as well as LAN interface, USB interface standard. One of the unique features on them is they've got a split window mode,

**Dave Jones:** where they can basically display multiple signals with different triggers on them. Excellent. So I've got basically two signals on here, and we've got... So you can separately trigger both channels independently? That's correct, and have different time base. Oh, different time base on each?

**Dave Jones:** Different time base on each. Nice. And if we had a four channel model, we'd be able to do four independently triggered signals, and time base, and vertical attenuation. So I've got a, if you see here, I've got a video trigger. Yep. I'll just change that to PAL.

**Dave Jones:** Signal. Okay. So I've got this one triggering on video and PAL. This one's an edge trigger, which is basically, if I toggle down to this one, we can see we've got an independent edge trigger control. The signal we're basically displaying on the bottom one is we're displaying a new current probe system.

**Dave Jones:** Right. Which is a non-invasive current probe. It's from a company called TTI. TTI, yep, I know that. UK company. Yep. So it's brand new, whereas we can basically display current measurement on circuits using the iProber. So what's the frequency range of that? This one's five megahertz.

**Dave Jones:** Five meg, yep. Displayed down to milliamps, up to the amps range. Right. And it also comes with adapters to do basically normal current probe measurements. Yep. But the main thing that it does is a non-invasive current probe. Excellent. Non-contact current probe rather. So the update rate of this is probably somewhere between the TEC series and the Agilent.

**Dave Jones:** That's correct, yes. 2000 series. It's probably not quite the 50,000 waveform updates per second of the Agilent. Yeah, that's correct. It would be close to that, getting up there. And there it is up close. It's quite a thin unit. I rather like it.

**Dave Jones:** It doesn't weigh much. I like the huge feet on the back of it. I don't think I've ever seen feet quite that large. And on the backside here, if we can turn it around, we have all the ports as standard. We've got LAN, USB host, and video out, and all the Cal and Trigger, and the Go, No Go outputs.

**Dave Jones:** And there is also a fan in it. Is it loud? No. No, it's not loud. There you go. That's the new GW Instek. It's not TTI branded? No, it's aimed at conjunction of product combination. Right. Aimed at TTI. Okay, right. So, what, TTI own aim, or?

**Dave Jones:** I believe so, yeah. Right, okay. That's the story. All right, John, we've got some infrared. These are a thermal imaging camera from a German company called Trotec. Trotec? Yep, that's right. So, they're a German-made product. Basically, they're a high-resolution camera, so they have the ability in electronics,

**Dave Jones:** we'll be selling electronics, is the ability to resolve very small SMD components for design, manufacture, repair, rework. So, it'll do thermal, they're basically designed for thermal profiles of components, is that? They can do thermal, basically any heat of any product that they will do.

**Dave Jones:** Just let me get that set up. Okay. There we go. So, we can basically see around the LCD. Yep. Around the LCD, there'll be heat around the LCD. And if we're looking at, say, for example, the PCB over here. Yep. We can turn it upside down, and we can easily resolve what's heating up on here.

**Dave Jones:** Nice. That must be some fine temperature resolution, because there wouldn't be much temperature differential in that probe, I would assume. No. They have a very, these have a, basically a 0.01 degree temperature resolution differential. Right. The best way to show that is the old hand-mark trick.

**Dave Jones:** So, put a hand-mark on there, and we can see the hand-mark. Yes, you can. You probably can't get that on camera, but you can see the hand-mark. Fantastic. That's brilliant. How does that compare to, like, the Fluor 1s? Are they in the same market, or?

**Dave Jones:** Fluor concentrate more on either the very low end, which is like a 60x60 resolution, because all thermal imaging cameras have a certain array resolution. Yep. Trotec start with 160x120 array. These ones are 340x280. Yep. So, that's 110,000 odd temperature points. Right. So, you're able to see smaller components.

**Dave Jones:** Yep. The similar Fluke and Fluor are like about double the price of what these are currently. Right. And how much does this go for in Australian dollars, roughly? These range from roughly around the $5,000 to $9,000 mark in the product family that's in there.

**Dave Jones:** Nice. But we start out at $2,700 for a 160x120. Okay. But the more resolution, the smaller the component you're able to see and resolve. Excellent. And is that, like, drop-proof? It looks pretty rugged. They do have IP ratings. Right. Yep. Nothing's drop-proof. Right.

**Dave Jones:** Okay. Got it. But they do have certain IP ratings. And we've got the Rigol spectrum analyzers. Yep. They've got a range of spectrum analyzers from 2GIG to 3GIG. Yep. This is their top-of-the-range model. Features things like a 10-hertz resolution bandwidth, very good noise-force specifications,

**Dave Jones:** range of automated measurements. It can run off a battery pack. Oh, it can. Nice. Can be field-portable. Yep. Price-wise, these ones are around $5,000. Yep. And they also have a slightly lower-end 3GIG one for around $4,000. Right. So it's very competitive pricing for the price-performance specification.

**Dave Jones:** Excellent. Yeah. And this is the 6,000 we looked at. Last time we were here, they're still – are they selling well? Yeah, they are. Yep. They're selling well. We sell them typically in areas that would have only ever bought Agilent or Tektronix. Right.

**Dave Jones:** Government research departments, university research, places like that that need a bandwidth of 600 megahertz. Yep. Without having the budget to pay, you know, $15,000, $20,000, 600 meg or 1GIG. Right. Bandwidth. Have they dropped the prices since Agilent have come through? Well, they don't really compete with the Agilent because they're a higher bandwidth

**Dave Jones:** specification. Yeah, because they – what, they start at 1GIG or is that the – They start at 600 megahertz. Yeah, 600 meg, which is higher than the Agilent 3,000 series. Yeah, they're not really competing with the Agilent 3,000 series. Yep. But the price has come down.

**Dave Jones:** They start out now around $5,700 for a 600 megahertz 2-channel. Nice. Excellent. Thanks, John. No worries. Thanks, Dave. All right. See ya. I'm here with Kevin from Upton Australia. Thanks for joining us, Kevin. No problem, Dave. Thank you. Excellent. So this is a machine from a company that was previously known as APS Novastar.

**Dave Jones:** Right. Now known as DDM Novastar. Right. They've recently had a buyout. They're made in Philadelphia in the USA. Yep. Nice. This machine is specifically designed for people doing prototypes, small runs, low volume. So it's not really a high volume thing, just in terms of speed or –

**Dave Jones:** In terms of speed, it's in real time, 3,500 components an hour. Yep. So we'd be able to dispense solder paste down to 0603 dots. Yep. We can do micro BGAs. We can do 0201 packages. Yep. We have a vision option for the machine.

**Dave Jones:** This machine, we've just got it set up to run a fairly basic board. Yep. Just to give the people at the show an indication of what's going on. Let's run it. Let's do it. Here we go. All right. We'll just – you might see that the screen is a little bit fuzzy.

**Dave Jones:** We'll be replacing the double-sided sticky tape. Right. Rather than solder paste, which we would prefer to do. Got it. But we've got sticky tape. So there's the – yeah, you can see the sticky tape on there. Double-sided tape. Yep. It works. It works.

**Dave Jones:** Good. All right. We've just gone to a fiducial to make sure that we're located where we need to be. We go to the other one and, again, ensure that we're positioned where we need to be. So now we're picking from the feeders. Yep.

**Dave Jones:** And placing components to their designated order. Nice. It's had a misfeed there. Yep. So the reason for that is that the tape hasn't peeled back. Okay. Sufficiently to release the component. Got it. Just reset that. We have it running in a number of modes, from slow to fast.

**Dave Jones:** Yep. But mainly just to give people an indication what we can do with a low-cost pick-and-place machine from VDM Novastar. A machine like this is in the vicinity of around $25,000. About $25,000, yep. Which is not sell your house to get up and running.

**Dave Jones:** No, exactly. And how many feeders? Is that a usable machine at that sort of level? We can have up to 64 feeders on this machine. Using a bank feeder, we can increase that 50%. So close to 98mm tape feeders. Yep. We can also pick-and-place short-strip from the super-strip feeder.

**Dave Jones:** The super-strip feeder allows us to put a length of 20 discrete components. And any number of those, we can pick-and-place from matrix tray and from tubes. Excellent. Looks like a nice bit of kit. I like it. Thanks, Gary. I'm here with Mark from Techmark Australia.

**Dave Jones:** He's going to show us lots of cool Tektronix stuff. Let's go. Go, Mark. Relatively new from Tektronix is our real-time spectrum analysis tool. Slightly different to the traditional spectrum analyzer, where you have a swept analysis using a resolution bandwidth filter. What this does, it takes chunks of data, 85 meg in this case,

**Dave Jones:** or 110 meg in the other next unit up, and it does up to 50,000 discrete Fourier transforms a second, up to 60,000 waveform captures, and then overlays those in a display which we call DPX. But it's just not a pretty coloured waveform. Each colour indicates spectral intensity.

**Dave Jones:** Intensity based on all the captures. Yeah, it hits and that type of thing, yeah. So what we've got here is just a very basic frequency oscillator that's drifting, and we can see through the peak hold that it's got a centre frequency of about 2.4 gig,

**Dave Jones:** and it's shifting backwards in time and shifting up and coming back. So now that you've seen that, you can set up the appropriate frequency domain capture or time domain capture and then go in and analyse that a bit further. Ideal for pulsed radar type applications,

**Dave Jones:** just general purpose spectrum analysis type work. Yeah, so that's where the tech side have gone in with the spectrum analysis tools here. This has been out for a while. The theory has been out for about 10 plus years. It came out of the old Sony Tech Alliance,

**Dave Jones:** and then with the changes in the spectrum analysis market, Tech came out with what they wanted to do with something to differentiate themselves and came out with this real-time spectrum analyser. It started out with the 3000 series, and then we progressed to the 5000 and the 6000 up to 20 gig.

**Dave Jones:** Has all the technology been off into the new MMDO? It's funny you should say that. Yeah, it has. It's sort of leeching across, you might say. So obviously you're paying quite a few bucks for this one. That one, it's down a bit. Yeah, it's a good little analyser on the MDO.

**Dave Jones:** But yeah, this one does a little bit more applications. And what's the price you're talking about in Aussie dollars? In Aussie dollars, we're starting at around $60,000 for the basic RSA 51,000. Up to the 20 gig unit, you're probably looking at about $110,000.

**Dave Jones:** That's nothing. Every home should have two, yeah. But no, they're quite a good, very good dynamic range. Yeah, so it competes well with the Rodenschwarzes and the Agilents. And each has got their own little niche. We're not saying that this is going to beat theirs or theirs is going to beat ours.

**Dave Jones:** Just looking at different ways of, as I say, skinning the onion. Still going to get tears doing your measurement. Still going to be fun, but we just do it a different way. I'm at the Agilents stand. I'm here with CK. What's new? Well, we've got a latest launch of the 20 gig spectrum analyser.

**Dave Jones:** And that is really hot. Here we go. There it is, handheld spectrum. And what's that worth? How much is that going for? Full feature, you're looking at about $25,000. About $25,000? Yep. Bargain. Specs, come on. So it's one major 20 gig? Yep. We have other models starting from three gigs, a seven gig and a 13 gig.

**Dave Jones:** So four models and this is the highest end 20 gigs. Excellent. Very nice. Is it rugged? It looks sort of, you know, nice. Is it drop proof? We did a drop proof on the dance. It's still working. And I've heard you've got a special on at the moment.

**Dave Jones:** Yes. Look at the poster. Oh, posters. Trade in and sell it. There you go. And more scopes and you get 50% discount from there. And, unbelievable. $25,000. I get a 7,000 scopes. Infinite scopes. You get a free? 3,000 scopes. For free? For free, yes.

**Dave Jones:** You've got to be kidding me. You guys must churn these out for a couple of bucks each. Giving them away. Well, we'll want to generate more interest on the 3,000 scopes. Yes, definitely. That's the way to do it. Free 3,000 series scope. Yep.

**Dave Jones:** Awesome. Thanks, CK. Thank you. And the best thing about these trade shows is the freebies you get. Isn't that right, CK? Yes. You guys have got freebies here? Yes, we do. Awesome. What a score. See ya. Bye. On Track Technology and you have a very cool soldering machine.

**Dave Jones:** Tell us about it. Here it is. Well, this is just one of the new 3-axis soldering robots that we've invested in. How much does this baby cost? That's what everyone wants to know. I'm not too sure, but it'll probably be around $3,000 or $4,000.

**Dave Jones:** Okay. Right. This is only just a little baby model. Yep. There is larger models that we're planning to invest in in the future. Probably more in-line, automated sort of process. Yep. More of a semi-automated process. Right. We're just trialing this little baby out.

**Dave Jones:** Okay. We just want to see how much productivity we can improve just by using these sort of machines. And have you found in trials, have you found that it's actually usable? Yes, it is. Speed-wise? Yes, it is. It's pretty quick. It is a lot quicker.

**Dave Jones:** Yep. But for this show, we've actually slowed it down considerably. Yep. So you can see it. You can see it and you can see all the sort of functions that it can do. Yep. And naturally, it's limited to a size of this, size of the jig here.

**Dave Jones:** So you can get larger versions. That's the sort of versions that we're trying to evaluate to see if it's worthwhile. Like our plan is to try and get one of these on each of our hand-soldering workbenches. Yep. If we can do that, it means we can improve the productivity of our soldering

**Dave Jones:** and our final hand-soldering process. Naturally, final hand-soldering is always going to exist because it's all those components that we can't get on our pick-and-place machines or on our wave solder. Yep, exactly. They're physically difficult to access. Or if we have like very temperature-sensitive super caps, that sort of thing,

**Dave Jones:** or batteries that can't... Must be hand-soldered. It's got to be hand-soldered. Yep. With heating possibly even on them. That's right. So, yep. Ready, go for it. This way? Yep. There you go. So normally it runs ten times faster. Yeah, we'll just slow it down so it's in the process.

**Dave Jones:** Alright, okay. Normally you want to put the boards at an angle, you put it straight, so bang, bang, bang. A LeCroy A WaveRunner 640Zi. Tell us about it. This year we brought the LeCroy WaveRunner. It's a new model from LeCroy. Covers anywhere from 400MHz up to 4GHz.

**Dave Jones:** Yep. The WaveRunner used to do up to 2GB, but because frequency demands are on the rise, they thought, hey, we better address the need in the 4GB, and hence the unit. The WaveRunner also comes in 12-bit front-end resolution versions. Right. At what bandwidth?

**Dave Jones:** 400 and 600MHz. 400 and 600MHz in 12-bit. Yeah, exactly. So for those industries like medical and other industries that require less noise and a better resolution on their front-end, we're addressing that right now. Nice work. And what's with the screen here? It sort of pops out.

**Dave Jones:** Glad you asked that. Yes, let's have a look. So let me... Let's look around the side here. So the screen flips up and down. Okay, so it tilts up and down. But have a look at this. For ergonomic reasons. Have a look at this.

**Dave Jones:** Let's say you've got data lines and you've got a stack of them and you want to see them on the same time base. So what happens... Bingo. Look at that. Portrait mode. It's not exactly a... Everyone's going to slim, lightweight ones these days,

**Dave Jones:** so I guess that's the price you pay for that nice screen. Yeah, it's a bit bigger because it's catering for bigger frequencies and there's more of the acquisition boards inside and the processing is a bit more complex. So, yeah, it needs the space.

**Dave Jones:** It's got very good ventilation as well for stability. And what sort of price are we talking about for a... Well, they're very, very well priced. For 4 GHz, you'd be looking at around $4,000. So that's top of the range in this model. Off we go.

**Dave Jones:** And here we are at the after party. You probably can't hear me because it's complete nerd rabble. Everyone's turned out for the free food and the free booze, I think it is. So here we go. But it's only for people who've got a red tag on their thing.

**Dave Jones:** So, yep, I think it's only... Not Joe Public, it's only the vendors. That's pretty much it. I think it's pretty exclusive. See ya. And I've stuck around. The party's still going on. I've snuck into the exhibition hall and there's nobody here. Not a soul.

**Dave Jones:** I'm the only one. This is absolutely brilliant. I'm the only one here. I've got free reign of pretty much anything. I can play with any toys. Hmm. What can we do? Oh, we can do some... We can have some serious fun here. Let me tell ya.

**Dave Jones:** Hmm. Got any ideas? I'm thinking a few things. Play with some Agilent gear? Maybe if we swap, say, the Agilent gear for the gear on the road and Schwartz stand. What do you think? That'd be awesome. It's kind of spooky, actually. It's... There's nobody here.

**Dave Jones:** I love it. Ha, ha, ha, ha. Altium might be in for a bit of a surprise at tomorrow's show. Hmm. Ha, ha, ha, ha, ha.
