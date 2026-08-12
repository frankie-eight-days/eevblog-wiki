---
video_id: VFX47ZGOn_o
title: EEVblog #587 - Tektronix MDO3000 Mixed Domain Oscilloscope Teardown
url: https://www.youtube.com/watch?v=VFX47ZGOn_o
source: youtube-asr
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. It's not every day that Tektronix release a new oscilloscope, especially these days, but they have. It's the new MDO 3000 mixed domain oscilloscope, a sort of a lower end follow-up to their MDO 4000, which we've reviewed and

**Dave Jones:** teardown before, and I'll put the links down below if you haven't seen that one. So, I expect this one to be a similar high-quality design and construction inside. It's got the built-in RF spectrum analyzer, which is going to be

**Dave Jones:** fantastic to take a look at, and this is the 1 GHz version, so it will actually contain different hardware to the lower end 100 to 500 MHz version, at least on the front end anyway, but Oh, yeah. So, of course, we could power

**Dave Jones:** it up and review it, but hey, you know what we say here on the EEVblog, don't turn it on, take it apart. And here it is. It is small and lightweight, and pretty compact. Well, at least, you know, small and lightweight for the

**Dave Jones:** size. I mean, the screen is absolutely enormous on this thing. And well, I see a couple of screws on the back here, so let's whip it open. It looks like, you know, traditional Tektronix type type design here, just a few screws on the

**Dave Jones:** back. The whole back panel will lift off. I can see the boards, the big fan in there. I can see the boards through all the rear board through here, so it looks like it just whips straight off, and there's a metal shield on top,

**Dave Jones:** so there'll be more items in there. They looks like Yeah, this back panel will just lift off. We don't have to undo any nuts on the BNCs there, maybe on the inside, well, almost certainly on the inside before we can get that metal can off.

**Dave Jones:** And of course, this is going to be shielded really well. This spectrum analyzer built in, just like the 4000 one, will have its own metal diecast uh metal can inside there. So, there will be some RF port inside there,

**Dave Jones:** no doubt. It's a 3 GHz bandwidth. As I said, this is the 1 GHz model and it is physically different to the 100 to 500 MHz model. If you want to upgrade, if you buy the 100 MHz model and you want

**Dave Jones:** to upgrade to 500 MHz, you can with just a software license. But, if you want to go to the 1 GHz like this model is, you have to physically send it back and they swap the board. I'm fairly confident

**Dave Jones:** it'll only be the front end that actually changes, the amplifier on the front end. I don't think any of the processing or anything like that actually changes inside. So, really if we are able to see the analog front end,

**Dave Jones:** that'll be the only difference between this and the lower end model. The RS spectrum analyzer 3 GHz bandwidth one is the same on all models. Now, of course, Tektronix are famous for their hybrids. They're a huge company, of

**Dave Jones:** course, one of the big scope one of the big three scope manufacturers and they of course roll their own hybrids for all sorts of stuff, their own custom ASIC chips and things like that. So, they're notorious for you know, if they fail,

**Dave Jones:** especially like in the old Tektronix scopes, getting replacements very difficult indeed. Although, of course, these modern ones, they're so so complex that you know, you probably wouldn't repair these suckers like you know, in 20 years time, you're probably not going to be

**Dave Jones:** able to repair one of these things if it goes haywire. Let's lift it off. Because this is my own unit. Um they did donate it to the EEVblog lab here. So, it is now the highest bandwidth scope in my lab at 1 GHz. So, we're

**Dave Jones:** going to have lots of fun playing with this thing over time. And uh so, yeah, I really don't want to damage this. Uh even if it was theirs, I wouldn't uh want to damage it anyway. It did get

**Dave Jones:** stuck in customs. Sorry for the late notice on this thing. Um but it did get stuck here, and I had to pay customs fee to get it cleared and get it into the country. But, I was supposed to have this before the launch

**Dave Jones:** deadline. It launched on the 25th of February. And I'm sure and you can actually buy it right about now. Prices start from, I think, don't quote me, about 3,300 dollars for the base model unit. Looks like there is another

**Dave Jones:** second shield under there, cuz I still don't see the uh nuts for these BNC connectors. And I am taking that high-res photos of this as I go along. So, if you want to see those, jump on over to eevblog.com,

**Dave Jones:** where they will be uh linked in. The link will be down below for that. Yes, I've got my new Sony uh NEX-5T camera with my macro lens. Very nice. Ta-da! And ha! Look at that. We're in like Flynn, and the main board

**Dave Jones:** exposed. Fantastic. And the power supply up the back. Look at that. All very neat, but you'll notice, the first thing, of course, is that there's no shielding from the switch-mode power supply to the main logic down here. Go go figure. Well, not

**Dave Jones:** a huge deal in the logic, cuz this is all the digital logic stuff, uh you know, around here that's near this uh switch mode. All the RF all the stuff that matters, the RF on the uh front end, of course. Uh

**Dave Jones:** RF The RF spectrum analyzer will have its own metal can, but all the analog uh front end for the four channels will be all in its own individual individually shielded thing, but still, uh a scope of this quality, I would have expected

**Dave Jones:** shielding around the can like that, cuz that's par for the course in other scopes that are cheaper. So, yeah, not that impressed. Now, I do really like this uh rear connector board like this PCI card edge connector, which then

**Dave Jones:** flips over onto the main board. I really like that. So, we didn't have to undo any of the connectors on the back to get it open. This is a really very well-designed case. So, you can see the thought that's gone into this. Small

**Dave Jones:** touches like the fan over here. They've gone, "Oh, well, you know, ordinarily you would power that from the power supply board over here, but oh, we don't want to run a cable all the way over there. Oh, look at this. Let's make it

**Dave Jones:** nice and neat and just the right length and mount it on that rear panel connector board there." You know, absolutely brilliant. The mains wiring, very neat, very tidy down in there. Look, the cable runs have been kept to

**Dave Jones:** an absolute minimum. They're cable tied here. They've just got exactly the right length cable to go in there. Beautiful. Now, even though the power supply is unshielded, but I'm sure Tek have done their homework on that. So, I'm just

**Dave Jones:** nitpicking with the shielding. It's just not best practice, that's all. But, they're obviously getting away with it and well, okay, I trust Tek to know what they're doing. But, the actual power supply looks like very high quality. They've got an Emerson

**Dave Jones:** transformer down here. You know, top quality brand. It's all, you know, TUV compliance on it and all sorts of stuff. Looks really, really well-designed. Of course, Tektronix wouldn't have done this. They would have chopped this out. But, yeah, I, you know, look at that.

**Dave Jones:** Beautiful celastic holding everything in place. All your protections are there. Oh, you've got your boots even even over the uh earth connector there. We've got a rubber boot over that. Beautiful. We've got some input protection down in there.

**Dave Jones:** It's, you know, they're doing everything right on this power supply. High quality. But, hey, that's what you'd expect when you pay a high price for a Tektronix. And for those who love to know the capacitors, as we all do and

**Dave Jones:** you should because they should be high by in a Tektronix. Yes, it is a Rubicon brand. No problems whatsoever. And that one, by the way, was 105° C rated and this one down in here, even though you can't see it, trust me, is a

**Dave Jones:** Nippon Chemi-Con. So, once again, top quality and 105° C rated. No problems. Someone really has gone to town with the Silastic gun. Look at all this. It's all gunked down. Just you Well, you know, it's beautiful, of course. It looks like

**Dave Jones:** we might have some small PCB fuses down there, perhaps. They've got silicon in the end on the end on through hole mounting like that. Fantastic. And the pot is sealed. Nice. And the fan, once again, also good quality brand name, Sanyo Denki. No

**Dave Jones:** problems at all. So, our main processor board is significantly less complex than the MDO 4000, its big brother product. And that's what you'd expect. Why? Well, it's obvious they're trying to meet a much lower price point with this thing.

**Dave Jones:** So, they're going to sacrifice some horsepower and capability compared to the MDO 4000. And if you compare it, which I'll link in the photos and the video down below for the 4000, well, this has bugger all compared to the

**Dave Jones:** 4000. We've only got three main heat sunk devices here to share across all four channels. Now, there could be more stuff on the other side, but certainly not big heat sunk devices like this. Whereas, the MDO 4000 had, I think, a

**Dave Jones:** separate ADC per channel heat sunk and all that sort of stuff. Look, three main devices. The sample memory here, almost certainly the sample memory. Why? Well, there's four of them there and they're coupled in with presumably match length traces to get

**Dave Jones:** the timing right. We'll take a close in look at that. So, there's one device per two channels like that. So, of course, your sample rate will half half if you turn on both channels, presumably. And then they've got the uh third main

**Dave Jones:** heatsink device over here. That could be a uh you know, the main acquisition uh ASIC or you know, something like that triggering all sorts of other jazz. Um but that's tied between all four channels. So, really they have cut costs here.

**Dave Jones:** Presumably not the same um ASICs as they use in the MDO 4000. I presume that they've uh spun new ones for this MDO 3000. And here's one of the main ASICs well. A totally custom uh job presumably um you know, tech partner but you

**Dave Jones:** probably can't get any info on that uh to save your life, no doubt. And they've got some more memory coupled into that here closely. And if you follow the traces out like that, you'll notice that it is coupled into these channels over

**Dave Jones:** here. So, there we go. You can follow that bus all the way around over into this main ASIC and presumably on some of the other layers there will be another uh you know, parallel bus going from here over to that one as well. So, this is

**Dave Jones:** obviously some sort of main uh acquisition and uh processing ASIC. Probably does all the uh DPO uh way in, you know, intensity grading and things like that. Perhaps part of the display ASIC perhaps. I still don't know where the display is

**Dave Jones:** plugged into this thing. So, that's the thing. With these when you're doing teardowns like this, you can tell a lot of the functionality due to the proximity of stuff. Like if the display connector was here and then coupled in,

**Dave Jones:** well, you know that this is doing the main display processing as well. So, anyway, this thing does have a couple of hundred thousand uh waveform updates per second. So, they're obviously doing that in hardware instead of the main

**Dave Jones:** processor uh down here, which we'll take a look at that handles all the GUI and the controls and uh and the communications and all that sort of stuff. And if we have a closer look at those memories, I've checked the uh data

**Dave Jones:** sheets for these. ISSI brand, of course. These are 8 meg by 32 or a total of 256 meg synchronous DRAM. So, there you go. That's coupled There's two of those. Maybe another couple on the back side of the board. We don't know until we flip

**Dave Jones:** it over. Coupled into this main ASIC. So, presumably that would all be for the DPO uh intensity grading and display uh processing and stuff like that. That'd be my guess, anyway. Until I flip the board and find exactly where the

**Dave Jones:** processor and the display is connected into, we know won't know. But, that's a good first guess, I think. And back over here to the uh ASIC, which shares two channels. We've got ourselves uh some Micron memory here. That's the Micron

**Dave Jones:** symbol. And uh you have to decode this part number here. But, thankfully, Micron on their website have a part number decoders for these small BGAs. They can't print the full number. For those playing along at home, it is actually an MT42H64M16HR.

**Dave Jones:** And that is a 1 gigabit or 64 megabit by 16 memory. So, where is the rest of it used for? Well, clearly used for the uh logic analyzer would be uh my guess. I see an dedicated logic analyzer

**Dave Jones:** circuitry, but I don't see uh logic analyzer memory unless we flip the board out. And there's our main clock down in there. Looks like 100 MHz. Don't know the exact brand. It looks like it's got uh decoupling on like a little uh

**Dave Jones:** surface mount hybrid there. That's quite interesting. Hooked into a uh Analog Devices ADF4360. And that's a uh no surprise, a synthesizer and voltage controlled uh oscillator. So, that gives a three That chip's capable of a 350 MHz to 1.8 GHz

**Dave Jones:** output. So, clearly, that's not uh providing directly the main sample clock for the ADC. This thing uh samples at 5 gigasamples per second. So, there has to be some additional multiplication happening somewhere else. And no surprises for seeing tied into

**Dave Jones:** that is a Macrel HEP11U. Had a look at the data sheet for that one, found it. No surprises, it's a pecal buffer. So, that's actually providing the drive. Here we go, here's the input coming from the output of the

**Dave Jones:** VCO there, coming through here into the buffer and then check this out. There's the output there coming across. They're tapping clearly tapping off that signal there and there and through to the bottom layer so an internal layer through those vias. And then they've got

**Dave Jones:** this massive LC filter network. Huge number of stages here and then popping out the other end there to drive something else. Fascinating. So, you've got to wonder if that's some sort of LC delay line or something like that. Hmm. Now, this is

**Dave Jones:** rather interesting. Check out this Lattice device here. It's a LFE3 series FPGA and it's not a particularly, you know, big beast and it's not heat sunk so it's not doing any real serious work but it's only a 33,000 lookup table FPGA

**Dave Jones:** with 1 megabit of memory built in. They've got some ROMs, you know, some flash memory coupled into that so you've got to wonder in you've got to wonder what this thing is doing. Is it running in some sort of internal, well, it must be

**Dave Jones:** running some sort of internal processor if it's got some flash memory hooked up to it like that. So, maybe a soft core processor. But take a look at all of these test pads out here. This is not for an

**Dave Jones:** unpopulated connector. I believe that's a, you know, some sort of production test pad or something like that. So, maybe could this be a real expensive and dedicated way to do production testing perhaps? I don't know. Maybe it's doing

**Dave Jones:** something else. You can clearly see the traces coupled up here. Look, they're hitting all the way up there coupled in to one of the input uh ASICs over here as I'll call them and presumably there would be a similar

**Dave Jones:** Yeah, yeah. No, there could be a similar bus heading on over to the other one. You would think so anyway. So, yeah, what is that puppy doing? On second thought, it's actually very likely to be the serial decoding feature

**Dave Jones:** of this thing cuz this is like a you know, advertised six-in-one instruments and that's one of the main instruments is the serial decoding and stuff like that. So, maybe they're doing that in hardware in this dedicated FPGA. And it just looks like we have some

**Dave Jones:** power supply stuff down there presumably for that Lattice local regulation core voltages for that Lattice FPGA. And we have ourselves another oscillator. It's one of the Espresso series. Can't quite get make out the part number of that, but yeah, presumably just another

**Dave Jones:** clock multiplier. And we've got a couple of JTAG headers here and here conveniently fully populated with the proper header connector. So, go and plug straight in and hack and debug and play around to your heart's content, I guess. And I

**Dave Jones:** have absolutely no idea what's going on here. Look at this. It's almost as if it's some sort of big touch sensor. Um you know, it's some capacitive touch sensor. They've got some digital traces running underneath there. So, that's not good practice to begin

**Dave Jones:** with, but like why? Why is that? Look, you know, my finger is you know, that's sort of like the size of my finger. I wonder what it does. Be interesting to power this thing up and just touch your finger

**Dave Jones:** on there maybe. Because look, there's a couple of vias on there. So, it's not you know, so they're electrically connected in two separate halves. it's not some weird-ass spark gap uh you know input protection thing cuz there's no solder mask removed off it or

**Dave Jones:** anything like that with the sharp corners. It It It's a capacitive touch pad. It's all I can figure. And check it out. I found a little bodgy in there. Look at that. Curiously, on just one channel of this multi-channel

**Dave Jones:** uh logic analyzer input here. Here's our the logic analyzer actual connectors on the other side of the board down in there, presumably surface mount on the other side. And no surprises for guessing these are your input comparators. Yes, very fast ADCMP562s

**Dave Jones:** 1-nanosecond comparators 500-picosecond rise time differential PECL outputs. Ah, it's all happening there. And just above those is a voltage regulator, but not just any voltage regulator, a fast pulse response voltage regulator specifically for driving these uh input comparators, no doubt. Because

**Dave Jones:** that's the real disadvantage with having extremely fast well, devices of any digital nature like this, they take huge gulps of current when they're switching. So, it really you need a fast transient-response voltage regulator up there local just to power those devices.

**Dave Jones:** And that's a um LDO 7725. Nothing much happening around here. This ICL30 3221 looks important, but it's just a max uh sort of 232 equivalent part for RS232 interfacing. That brings us over to our main processor or main applications

**Dave Jones:** processor as you'd really call it because this is no surprises for finding a Freescale i.MX6 series. This is a core ARM Cortex-A9 processor 1-GHz. This uh series of chips you can actually get quad-core versions, but this is only

**Dave Jones:** this what's called the solo chip. Uh hence the S in the uh the 6S there in the part number. Um so, this only has one core in it. But, this thing is quite a beast, you know, operating at 1 GHz,

**Dave Jones:** capable of 1080p encoding and decoding. Fantastic stuff. So, as you can see, we've only coupled in one uh DDR uh two memory here. You can see there's an unpopulated footprint on the bottom. There could be another one on the bottom

**Dave Jones:** side there, of course. And of course, you notices the uh serpentine traces. That's to max uh that's to match all the length of the differential pairs going to the DDR memory there. Now, whether or not this thing is driving this display directly

**Dave Jones:** or whether uh the display is actually handled by this main Tektronix ASIC over here, because if you're getting 100, you know, a couple hundred thousand waveform updating updates per second, it's going to be hard to do that through even a

**Dave Jones:** real beefy applications processor like this. But, hey, they could be doing it. Um so, yeah, we don't know. We have to find out where the LCD is actually physically connected into this interface here. But, yeah, there you go. I mean,

**Dave Jones:** this is going to be handling all of your main, you know, your main front panel, your user interface functions, your operating system, your main display stuff, of course, all your menus and everything else. It's going to be handling all that. Whether or not it's

**Dave Jones:** actually the real live data real live waveform data uh directly screen. I mean, they could be mapping it through this ASIC up here. You know, that that'd be a better guess than trying to funnel everything into this poor little

**Dave Jones:** applications processor, even though it is pretty beefy. Um yeah, it's more likely to be handled up here, the display parts of it. That's what they do in the Agilent ones, for example. All the ASIC handles the direct mapping of the waveform to the screen,

**Dave Jones:** and then the main processor just sends the data to that processor, which is then, you know, adds the menus and cursors and everything else around, wrapping around or overlaying that waveform data. So, you get the fast waveform updating, and of course, all

**Dave Jones:** your menus and everything else they can be slow as a wet week, and you don't care. And there's nothing else terribly exciting on here. We've got a couple of push buttons down here, CPU power on off, very interesting, global reset,

**Dave Jones:** built-in switches like this PCB mount. They've gone to a bit of trouble to mount those things in for design development and servicing and stuff like that. I don't know. Yeah, we've got another big multi multi-channel switch-mode supply up here doing some stuff. Not

**Dave Jones:** sure why they just why they did that on the board. They've got this full main power supply board all out here doing stuff. But anyway, big multi-channel big multi-way connector up here connecting the main power supply board. They've got some miscellaneous stuff

**Dave Jones:** down here that's just handling the USB port, the front panel USB port down the bottom. So, nothing terribly exciting there. So, that's the main overview of this board. Not a huge amount on there, but I should expect or, you know,

**Dave Jones:** Tektronix go to town in terms of developing custom ASICs, and you know, really engineering this thing to the hilt to get the cost down. And well, we've got main three main heatsink devices over here. Obviously, two of them drive two of them are identical and

**Dave Jones:** handling two channels each. We've got a third one which handles all four in some way. We've got this mysterious FPGA over here doing something with some ROMs hooked up to it. We've got a main Tektronix process well, ASIC over here, not heatsink,

**Dave Jones:** curiously. We've got an applications processor which handles all the real-time OS, and we've got our logic analyzer stuff down here. And well, there's not a huge amount more.

**Dave Jones:** Okay, let's lift this main processor board out. Ta-da! Haha, we're in. And here's the main board, and it's pretty much what you'd expect. Not much on the bottom apart from some additional memories just to get the density. It makes sense to

**Dave Jones:** put them on the back just from a PCB routing point of view. Flip them on the other side of the other chip on the top. Um it just, you know, it works out fairly well. So, here are your three

**Dave Jones:** main heat sinker ASICs. One of these per sharing channel. We've got some extra memory over here. So, we've now got a total of two gigabits memory per channel. There you go. And of course our main ASIC in here coupling

**Dave Jones:** all two channels together. There's nothing else on the back of that FPGA over there. Of course, there's our logic analyzer input connector. That's actually the front panel connector there. We've got some more high-speed comparators on the front end there, but

**Dave Jones:** apart from that, not much else. Here's our main Tektronix ASIC down here. Yes, we've got more memory coupled around that. So, tons of it. Got two board-to-high-speed board-to-board interconnects, and they're going to be actually bringing the data over from the

**Dave Jones:** front ends. I presumably this is where the systems engineering in this gets interesting cuz you notice the ADCs, well, the the front end, sorry, are not on this board. They're on the other board, and they got to get across. The data's got to get

**Dave Jones:** across well, this high-speed connector here cuz this one over here is coupling in some other stuff over here to the main Tektronix processor ASIC over here. So, yeah, go figure. We do have an extra memory up here on our um

**Dave Jones:** um applications processor over there, but apart from that, not much else. By the way, I just checked the photos from the MDO 4000 teardown and the main Tektronix ASIC here on the 4000 was the tech 3005B. So, this is presumably a new revision of

**Dave Jones:** that part. Now, here's where the surprising part comes in. Just like the MDO 4000, yes, they have a separate input board here which contains the analog front ends. These are the 1 GHz front ends four-channel scope, of course.

**Dave Jones:** And this is our RF front end over here, but that's all there is to it. I'll show you a photo from the Tektronix MDO 4000 and it was much bigger, like this, and that contained all the big RF can all up

**Dave Jones:** there for all of the spectrum analyzer stuff. But look, there's nothing else inside this thing. All we've got is this tiny RF front end over here. No wonder they're keeping the cost down on this thing. This thing is nothing like the

**Dave Jones:** MDO 4000 and not only in the spectrum analyzer part of things, but also there's no ADCs on this board directly, at least not on this side. The once again, here's a photo from the MDO 4000 and it had above each one of these ADC

**Dave Jones:** Sorry, each one of these analog front ends here, it it had a separate ADC per channel with a big heat sink on it protruding up through the top side of the main processable. The heat sink was so big it

**Dave Jones:** had to go up through the through cutouts in the main board. This has none of that. Where are the ADCs? These are the analog front ends 1 GHz bandwidth, but hey, are they just taking the analog data through

**Dave Jones:** this connector here? Anyway, if you send your scope back to Tektronix to upgrade it from the 100-500 MHz version to the 1 GHz version I've got here. This is the board that will swap, no doubt. The processor board would still all remain

**Dave Jones:** exactly the same, but uh they just uh swap this board over. Not a huge amount of cost in this thing. I was expecting basically a a similar analog or RF uh section to the MDO 4000, but it's nothing like it. Just this tiny can over

**Dave Jones:** here. I doubt there's anything on the flip side of this. It's just going to be the front panel, the keyboard, and stuff like that. We will go further to try and find out, but they've really completely re-engineered this, by the looks of it,

**Dave Jones:** and built it down to cost. Because the MDO 4000 was, you know, a ridiculously expensive scope. Uh you know, incredibly uh you know, versatile, but very, very expensive. They've done some serious re-engineering to get the cost down for

**Dave Jones:** this MDO 3000. That's why they can even afford to include the RF spectrum analyzer onto, you know, the base model 100 MHz dual channel scope. That's it. And they software limit the RF bandwidth. So, this is going to be a 3

**Dave Jones:** GHz RF spectrum analyzer, regardless of whether or not you buy the 100 the cheapest 100 MHz model. But, granted, as I said right at the start, the 100 MHz model dual channel is uh $3300 or thereabouts. Starts from that price.

**Dave Jones:** And that only includes a software limited 100 MHz front end. But, the full 3 GHz front end is there, but obviously it's not your traditional spectrum analyzer. There's nothing in there. Now, I'll take this board out as well, of

**Dave Jones:** course, but um there is not going to be any analog to digital converter on this board. Because when you start talking, you know, 5 gig samples uh per second ADC, right? You need some serious heat sinking. That's what that board over

**Dave Jones:** there is, right? These are still going to be your ADCs sharing two channels there. But, the difference the MDA4000 had them directly coupled on this board. So, the only thing that can be happening here is they've got the differential

**Dave Jones:** analog signal from the buffer here coming out. It's probably this trace here. Look, you can see it's snaking its way up there. They've got some length matching on that, going through something there, and going into this connector. So, they've got the analog

**Dave Jones:** signal running through this high-speed connector over here. Nothing inherently wrong with that. You're just driving it a little bit more distance. These connectors are really, you know, expensive and really well engineered for that sort of thing. And of course,

**Dave Jones:** they'd have alternate grounds and pins and all sorts of stuff going on in there to to ensure that there's no cross talk and stuff like that. So, you know, it's not bad, but yeah, they're running the analog connectors over that

**Dave Jones:** board-to-board analog signals for all four channels over that thing. Yeah, look, they're obviously matching length. You can see this one over here. This pair goes all the way over there, and they go, "Oh, we have to this one is

**Dave Jones:** physically closer, so we have to match the length of that pair cuz you can't just have different length pairs. Oh, the propagation layer screwed." So, that's why they have to switch it back there. So, the length of that trace would be precisely matched to

**Dave Jones:** the length of that one. And this one here as well. You can see it. Ah, here it is, running in here for this channel three, I guess it is, and snaking up there, all around there, down there, and

**Dave Jones:** back up and into there. Woo. And the other fascinating thing is, look, we've found our display connector. There it is, the razor ribbon cable going off to the display. And all of this is going through a buffer over here coming from

**Dave Jones:** this main board-to-board interconnect, which goes up to the main processor board. Wow, they haven't even They're going via this power supply board here. Woo. Why? So, coming back to our main processor board here, here is our board-to-board interconnect. This is the only thing

**Dave Jones:** that the front panel display and keyboard has to go through. And unfortunately, I can't see the traces on either side of those. So, they're obviously running in the middle layers of this board somewhere. Now, where they're actually running to, my guess

**Dave Jones:** would be that they're running over to this tech ASIC over here, and then that, as I said, is the main applications processor is mapping uh any required user interface data over this main tech ASIC, which is then driving the display, exactly how it

**Dave Jones:** works in the uh Agilent uh X-Series scopes. But, that's only a guess. I do stand to be corrected on that. It could very well be coupled directly into the applications processor. But, as I said, that's not going to handle a couple of

**Dave Jones:** hundred thousand uh waveform all your waveform update processing is going to be done in this main tech ASIC, all your DPO stuff and things like that. It's going to definitely going to be done in here. And whether or not they're

**Dave Jones:** actually transferring that and just updating a slower rate to the screen, they could certainly well be. They could uh certainly be actually doing that because the There is a There is a big difference between the waveform update rate, i.e., the

**Dave Jones:** processing waveform update rate of this thing, I think, is like 250,000 waveforms updates per second. It's a big difference that. That doesn't necessarily mean that uh that information is being updated on the screen, of course, at 250,000 waveform

**Dave Jones:** updates per second. It's not. It's being done in memory, and then a slower version of that, a slower copy of that information, is being transferred to the display. So, it could certainly All the DPO is certainly happening in here, but

**Dave Jones:** it could be funneled, and all the processing for the display is done via the applications processor. Actually, that might make more sense cuz this does have a big display processing engine in it and driver as well. And it does look like inside this thing

**Dave Jones:** they've got one huge piece of B on the front here. You can see this matte black PCB material here with the pins for the intelligent probes which actually plug on to this thing. I think there's one big matte black board covering this

**Dave Jones:** whole front panel. And you can see that it extends up here to these plug-in application modules as well with the contacts directly on the board. And by the way, for those wondering the spectrum analyzer over here, this is

**Dave Jones:** literally going to be just the front-end amplifier and attenuators and everything else for the spectrum analyzer. After that, it's purely digital. And I believe I read somewhere that it's doing because this has a very wide capture bandwidth by the way, 1 GHz wide capture

**Dave Jones:** bandwidth. Absolutely fantastic if you need to resolve and capture and debug different signals over an entire, you know, you might have something operating at 400 MHz and you have something else operating at 800. This is a way to

**Dave Jones:** really capture the whole bandwidth at once and see time correlation between the two signals. Now, speaking of which, the time correlation for this this MDO 3000 is not the same as the MDO 4000. They've deliberately cut this the

**Dave Jones:** performance in this thing down completely so that you cannot do simultaneous time sampling and correlation between the spectrum analyzer and between the analog inputs as well. And that's an incredible shame and one of the big disadvantages of this thing is that, you

**Dave Jones:** know, one of the huge advantages of the MDO 4000 was that you could do that fantastic magical time correlation between your analog signals and your RF signals and your digital signals as well, hence the mixed domain name. So,

**Dave Jones:** this thing almost doesn't deserve the mixed domain name because if you can't do time correlation and sample at the same time between the RF channel and the analog inputs, well, what's the point? It's just a tacked-on spectrum analyzer

**Dave Jones:** in its in a box. Anyway, enough ranting about that. Yeah, this is just an RF front end. That's it. I read somewhere that it's doing it's sampling this the 3 gigahertz bandwidth is being sampled at 10 gig samples per second.

**Dave Jones:** So, I reckon they're tying Well, obviously, the analog channels are being sampled at 5 gig samples per second. They're obviously tying at least two of those, maybe even four of those together to sample the RF front end. And hence

**Dave Jones:** why you can't do time correlation between the and sample at the same time between the RF channel and the analog channels because well, to when it's sampling the RF, it's working as a spectrum analyzer sampling that RF front

**Dave Jones:** end, it needs all the power of those ADCs, which are over here on this board, to actually do that. And then it's got no resources left over for the analog channels at the same time. So, you switch you either use this as a spectrum

**Dave Jones:** analyzer or as a regular time domain oscilloscope. Aha, what I've done is I've undone four machine screws down in here or three, actually, and it looks like we might be able to lift this out independently of the rest of the chassis. So,

**Dave Jones:** let me carefully lift this sucker out. Yeah. Yeah, she's coming out. Oh, look at that. That is a beautiful design. Aha, tons more stuff on the back. So, I'm actually quite impressed by the design of this thing, the modularity,

**Dave Jones:** and the way that you can service it and or assemble the thing. Fantastic. I was afraid that I'd have take out this entire chassis. I actually started to take out the main self-tapper screws here which go into the front

**Dave Jones:** panel plastic. I thought all that I'd have to lift out, but it doesn't. I just lift it out this RF board here, the RF and analog front end board. Fantastic. Obviously, because it is designed, they put some thought into this design for

**Dave Jones:** that upgradeability, because when you as I said, if you send your scope back and you want to decide you want to pay the extra and get the 1 GHz version, well, they have to make the upgrade of this

**Dave Jones:** board really easy and they've done so. Fantastic. And you can see I think I was right about the front panel connector. Maybe you can't see it due to the exposure of the camera, but there is one big matte black board going right on the

**Dave Jones:** front panel. I may not actually get that far in the teardown cuz there's nothing interesting on there. And that's it. Check it out. Look, they haven't even bothered to shield the the front side, put a can on the front

**Dave Jones:** side of this RF front end. It is so incredibly simple compared to the MDO 4000, which was more traditional you know, spectrum analyzer sort of construction and design as well. We'll take a look, try and see what that little puppy in

**Dave Jones:** there is. Obviously, look at all the via stitching around here. They're obviously getting a super Well, in fact, all the way around here. Obviously getting super low inductance ground path there, but yeah, they're not bothering to shield the top like they did. There you go.

**Dave Jones:** They got the can on the front side there, so we'll try and open that up and get a look at the RF front end, but that is all there is to it. Unbelievable. Looks like some sort of little processor over here just

**Dave Jones:** controlling the front end. Now, I am sorry, but I will not be able to show you the 1 GHz analog front end because these solder connections here, here, and over there are the metal shielding cans over the 1 gig

**Dave Jones:** front end. So, this is the backside of it here. So, they've obviously got a chip. There we go. It's like some sort of heat sink QFN package, something like that. So, they've got a bit of heat sinking on the bottom side of there. So,

**Dave Jones:** all of your good stuff for the RF front end is on the other side of the board. Sorry about that. Some HCT04 logic here. But, old school 77400 can't beat it. You've got to have that somewhere. There's one of those per

**Dave Jones:** channel. And further on up each channel, three six-pin sock 23's. Not sure what they're doing. Probably regulation by the huge traces going in and out like that with the huge vias and the decoupling. So, they're probably local voltage regulation for

**Dave Jones:** the front end. And we have ourselves a Maxim MAX9601. And that is no surprises a high-speed PECL comparator for the triggering. Obviously, the triggering front end. So, there you go. That's the proper analog triggering section, 500 picoseconds. You know,

**Dave Jones:** really really kick-ass comparator there. And I don't know what that one there is doing. 441LAA. I don't know. You can try and figure that out. Don't even know that symbol offhand. But, anyway, one of those per channel. So, we're basically looking at

**Dave Jones:** a duplication of all that circuitry all there across all four channels. And aha, backside of that RF spectrum analyzer. No real surprises. It's another ADF4360. Exactly the same part we saw on the main logic board. That is a synthesizer and

**Dave Jones:** VCO to generate the sampling clock required. And curiosity is going to get the better of me. So, I'm going to lift up that label. Lift up the skirt. See what that thing is. Of course, it's a dead giveaway. It's some sort of

**Dave Jones:** processor cuz anyone that has a label like this, this means it's been flashed and has code in it. Yeah, there you go. Little lot Freescale HS8 8-bit processor. Freescale, of course, well, they use them Freescale main applications processor. So, hey, might

**Dave Jones:** as well use the same manufacturer for your little 8-bit micro. Now, these traces are interesting. Look at these. All these high-speed differential pairs all going over to this connector on this far side of the board. I thought they'd

**Dave Jones:** all be popping out that middle one. But, they're not. There's a ton going over to here. Now, here's where we look at the systems engineering and see where all this stuff is flowing to figure out what's going on. We We know we've got

**Dave Jones:** these high-speed differential pairs one coming from each channel, probably even from the RF channel over here. So, there's a whole bunch of them going to this connector over here. And where's that one connected? Well, if we have a

**Dave Jones:** look at our main board here, it's this connector over here. What is that connected near? Aha, that main Tektronix ASIC over here. Here's the other one. So, as I said, all of the analog channels would be going through this

**Dave Jones:** connector through to ADC1 and ADC2 here, which handle all four channels. But, all But, then they've got a whole bunch of other pairs coming over here coming out of, if you have a look, where they're coming out of that chip we

**Dave Jones:** had a look at down in there, which is your high-speed comparator for your trigger. So, these are actually the triggering outputs from each channel going through that connector. And that connector pops up here. There it is. It's mounted on the backside of

**Dave Jones:** that there coupled into this main Tektronix ASIC over here. So, this is handling all of the triggering. But, of course, if that's handling all of your triggering, then what is this third device over here? I You know, these are

**Dave Jones:** obviously your main ADCs and acquisition ASICs. as I said, one per two channels there. Well, what's that third common device doing between all four channels if it's not doing the triggering? Check out this. Someone was thinking when they laid out this board.

**Dave Jones:** Look at this. They have put notes to whoever was designing the case or the system, you know, the whole putting the whole thing together. The person who laid out the board went, "Ooh, okay, it's important we don't short out the

**Dave Jones:** positive tab of this battery to anything cuz it's a through-hole part. If we accidentally short that pin out to some metal or if it's very, very close, that could, you know, in production or something like that with tolerances short out to one of the metal

**Dave Jones:** cases or something like that, then well, it's going to ruin your day." So, they've put a radius around there where we must cover or whoever designs the next part of the system must cover that pin there. And look, even may cover.

**Dave Jones:** Hey, if you want to gild the lily, let's may cover that part. And they've followed that up with it on the bottom. Just in case you missed it. Look at that. Brilliant. And of course, we can't let this go without

**Dave Jones:** having a peek in the RF section. I've undone three screws there. Yes, we have our gasket. Look at that. Completely separated. You can see the signal path. How it hit it There's the RF connector there. It's flowing up through here,

**Dave Jones:** flowing up around there, and out well, there. Somewhere. It's popping out on the top side. So, let's take that aside and flip our board over and see what we have. Hey, not much. There we go. No solder mask on there. That's pretty

**Dave Jones:** typical, but there's hardly anything in that front end at all. And as you can see, it follows the path directly of what that was covered with our metal diecast top on there. And that's very typical of these spectrum analyzers con-

**Dave Jones:** construction or controlled impedance, of course, or, you know, very critically designed. We've got some length matching around there and you know, basically, when you're talking in the gigahertz range, everything on your PCB becomes an a component. I've talked at this before

**Dave Jones:** extensively on previous videos and how you can actually have a distributed element filters manufactured out of your PCB bandwidth, you know, low pass, high pass, bandwidth filters manufactured magically into the traces of your PCB. Doesn't seem to be a

**Dave Jones:** huge amount of that going on here or any of that going on here, really. All I see is out There's our input. There's our AC coupling and then we've got some filtering there on the input. We'll have a look at what that

**Dave Jones:** is. That's our input amp and then yeah, we've got some more in series termination here, some more AC coupling going on. We'll have a look at that, but some more filtering happening around there. Little transformer coupled little balun, sorry.

**Dave Jones:** Uh, going there and well, not a huge amount else. Now, if you're concerned about those solder joints, I know they look ugly, but that's what happens with a high when a high thermal mass component meets lead-free solder. It just It looks

**Dave Jones:** pretty horrid like that, but no, there's nothing actually inherently wrong with that. And smack on the input here, no surprises for finding that we've got an attenuated chip. In this case, it's a Hittite Hittite Microwave Corporation HMC 624

**Dave Jones:** LP4. It's a digital attenuator. I.E. by digital, it means it's got a digital serial interface, serial or parallel interface controlling the attenuation in there. So, yeah, we're basically just got our AC coupled input, little bit of filtering happening there and it goes

**Dave Jones:** straight to the attenuator, which gives your input all your input attenuation ranges. And as always, I will link in all the data sheets down below, so you can go and check these out for yourself and follow through. And what do you need

**Dave Jones:** after an attenuator? Well, you need your amplifier, of course. And yeah, once again, we've got a Hittite Corporation. Hey, if you're going to get the all your stuff, you might as well get it from the one company, especially the company who

**Dave Jones:** specializes in these sort of chipsets for these sort of RF front ends. And this is a DC to 6 GHz gain block. It's a HMC 311, and for all you RF fans, it is a heterojunction bipolar transistor amplifier, a HBT, with 14 and 1/2 dB of

**Dave Jones:** gain. Fantastic. And you might notice, if you look very, very carefully, it might be a bit puzzling that there's no other pins connected except the input and the output pin. How does that work? How does a chip like this work if there is no

**Dave Jones:** power pin at all? In fact, this is true. Take a look at the data sheet here. There is only an input and an output pin. There's no power pin. How does it work? Well, easy. Read further down in

**Dave Jones:** the data sheet, and you'll see that the power is actually coupled in via the output here, via this inductor here. There we go. So, it's coupled into the output, powers the chip internally. This is very common for these sorts of

**Dave Jones:** RF amplifiers. And you'll find these in all sorts of things, like you might be familiar with the your TV masthead amplifier, for example. It'll be a similar thing. You feed in your voltage down at your, you know, at your TV

**Dave Jones:** outlet. You actually feed it up the coax, and it's powered from the output. Exactly the same thing happening here. Oops, and I forgot before and after that little eight-pin packages here, labeled 360. I don't know what they are. There's no

**Dave Jones:** equivalent, you know, HMC360 from Hittite or something like that. But basically, based on the operation of this thing, there we go. There's our input attenuator, our digital attenuator from our RF front end. So, our RF comes in, goes through our digital attenuator,

**Dave Jones:** and obviously, you can see that there's a bypass trace here, of course, controlled impedance trace going over and bypassing our amplifier, our gain block there. So, obviously, these are little RF switches that digital line there would switch between, well, switch to bypass

**Dave Jones:** completely our RF amplifier there. And then we've got our signal coming out of our filter here, going up to what looks like a little transformer, and that will be a balun, of course, cuz at this stage, we're still operating

**Dave Jones:** single-ended. It is not a differential pair. It is a single-ended reference to the ground. And you can see all the vias stitching around here. Ah, beautiful low impedance. And you'll see that out of the other side of the balun here, bingo,

**Dave Jones:** it comes out differential. So, we're no longer referenced to ground at this point. But curiously, then it just pops out, does some extra It looks like we've got some load matching there, and looks like No, there was supposed to be like

**Dave Jones:** some filtering happening there, but I don't know. And then we've got some extra delay introduced by this trace around here, and then they're basically just joining up again single-ended over at this side. So, not sure why they've actually done that.

**Dave Jones:** And this is where it ends. And well, curiously, well, you've got to think Well, with a spectrum analyzer, it's got to have that VCO. Got to have that local oscillator. And here it is. It's a Once again, Hittite HMC429,

**Dave Jones:** and it's a 4.45 to 5 GHz VCO. And that's all it does. It just basically voltage input it can generate a frequency out within that range. So, at this point I started to get rather confused actually because well, we've got ourselves that

**Dave Jones:** VCO there. And anyone who knows the basic operation of a traditional spectrum analyzer which you've seen in many of my previous videos, once you see well, they have a VCO like that and the VCO feeds into a mixer along with the RF

**Dave Jones:** signal goes into the other side of the mixer and bingo, out the other side pops your immediate frequency IF signal which then goes on to further pass down in the spectrum analyzer. And well, we've got a VCO here. So, I thought well, okay,

**Dave Jones:** there's going to be a traditional mixer in this thing but well, it just didn't make sense. I mean, where is the mixer in those two little white four-pin white things there and and a couple of traces with some termination. It just didn't

**Dave Jones:** make sense. So, I contacted fellow blogger Alan Wolke. If you haven't subscribed to his YouTube channel, you certainly should. Who actually is an applications engineer at Tektronix and he wasn't quite sure either exactly how this new product actually worked. But he

**Dave Jones:** had a couple of ideas and well, it started to make some more sense. Now, there's one thing which we both knew was that the Tektronix MDO technology actually samples the RF, the entire RF spectrum in in this case at 10 GHz. So, obviously

**Dave Jones:** it combines the traditional ADCs in the oscilloscope and uses those to do the sampling directly on the RF spectrum. But hey, we had this this VCO in here, right? Acting as a local oscillator. And when you've got a local oscillator in a

**Dave Jones:** spectrum analyzer, it implies that it feeds into a mixer and your RF comes in and you get that intermediate frequency out. So, you know, we didn't quite know what going on, but Alan knew that there was a technique

**Dave Jones:** where you dither the where you inject a dithered RF signal into the RF signal you're trying to measure and then sample that and that would increase your performance of your RF front end. And bingo, he pulled up a

**Dave Jones:** rather obscure, I think, application note or white paper from Tektronix that explains exactly how the MDO RF spectrum technology works. And this was the other thing that was puzzling me. I didn't quite understand how they were getting the performance out of this spectrum

**Dave Jones:** analyzer when they were using just the regular ADC in the oscilloscope. Sure, they're all sampling at a high sample rate. In this case, they're combining all the ADCs together, presumably to give that 10 gig sample per second sample rate for our 3 GHz RF bandwidth.

**Dave Jones:** So, they're sampling the RF directly doing that. But hey, what's the difference between just a regular oscilloscope with an FFT function and this Tektronix MDO technology. You know, like yeah, you can do some boxcar averaging like you're familiar with with

**Dave Jones:** the high-res mode and stuff like that, but we didn't have the extra bandwidth. Yeah, you can do some other averaging and things like that, but it just didn't make sense. I mean, an 8-bit converter at best is only going to get, you know,

**Dave Jones:** around about that 50 dB dynamic range. And well, this spectrum analyzer has, you know, it's got like 100 dB in the order of 100 dB dynamic range. So, how do they get that increased performance using an 8-bit converter?

**Dave Jones:** And here's the white paper I was referring to. Now, I will link this in down below. So, if you want to read all the gory details yourself, you certainly can. And well, here it is. Learn how the MDO series scopes, including the 3000,

**Dave Jones:** this is for the 4000, but it will apply to the 3000 with you know, the subtraction of something we'll show in a minute. They're able to leverage existing oscilloscope acquisition technology to achieve spectral fidelity on par with entry-level spectrum analyzers. So, the

**Dave Jones:** design techniques used in the MDO series allow them to achieve that fidelity far in excess of that provided by the typical FFT feature found in other oscilloscopes. And that is the key point, the key point of difference, even

**Dave Jones:** though they're using exactly the same 8-bit ADC. Now, let's take a look at the basic block diagram here. And it's um this is for the 4000, so the 3000 in fact they're actually missing something out of here which we'll show in a minute

**Dave Jones:** as well, even on the 4000 which what we're what we're doing. Basically, the RF input can is just here which is what we've seen, well, at this point that's all it is. Input attenuator, some gain, some you know,

**Dave Jones:** some low-pass filter in and stuff like that, but it's basically just an RF front-end amplifier. And it's going into what's called a block down converter because in the MDO 4000 series, well, they're trying to get up to 6 GHz bandwidth, but

**Dave Jones:** we don't need that in the MDO 3000 bandwidth because we're only going to 3 GHz here. So, we're just operating within that one block. So, we don't need a block frequency down converter. So, that is gone out of the MDO 3000. And

**Dave Jones:** then, well, yeah, a trigger signal comes out of that and it just goes into an analog digital converter. In this case, it'll be all of the ADCs that are regularly used on the analog channels. They tie them all

**Dave Jones:** together so they can get 10 gig samples per second. So, massively high sample rate and as it says further on, here we go, a bandwidth in excess of 5 GHz. So, the actual ADC itself has an input bandwidth up to 5 gig. The ADC hybrid or

**Dave Jones:** whatever ASIC developed by Tektronix that massive 5 gig bandwidth so they can they can easily get a 3 gig input spectrum analyzer. They can sample the RF signal directly. So, you know, none of your traditional um uh spectrum analyzer type stuff. It's

**Dave Jones:** basically just operating like a regular scope. That's pretty much all all it is, except you you know, you've got some nicer RF sort of front end with your 50 ohm load and your attenuator and your gain and you know, some filtering and

**Dave Jones:** that sort of stuff, but apart from that, it's just like another analog channel, really. And as such, you can forget about all the rest because well, yeah, it does some digital down conversion and stuff like that and some discrete

**Dave Jones:** Fourier transform, which they don't show in here, but that's all just your digital processing inside the thing. It's basically RF straight into your analog-to-digital converter, except for something that But how does it do that, exactly? How does it get like 100 dB of

**Dave Jones:** dynamic range instead of 50 dB you'd expect with your regular 8-bit analog-to-digital converter? Well, it's not using averaging. It's basically using two different Well, three different things effectively, but processing gain is one of the main ones, which is all done in the digital domain.

**Dave Jones:** I won't bore you with the formulas and stuff like that, but it's basically saying what I've been saying is that a regular 8-bit converter only gives you 50 dB noise floor. That's, you know, pretty much it. But we're after in a spectrum

**Dave Jones:** analyzer like a, you know, 100 dB for a, you know, a half-decent entry-level spectrum analyzer. So, that's what we're getting still with that 8-bit ADC. But what they can do is they can do some digital down conversion and some

**Dave Jones:** discrete Fourier transforms in the software after the ADC. This is all software processing and that gives you what's called process gain, which effectively lowers your noise floor because it's over a smaller bandwidth and it can calculate and it do

**Dave Jones:** all that in digital. So, even with an 8-bit ADC, you can get a noise floor down at, you know, uh -100 dB. Fantastic. Oh, magic. And there you go, they give you an example of a 10 MHz span, for example,

**Dave Jones:** and a resolution bandwidth of 10 MHz with the 10 gig sample per second MDO 4000 and MDO 3000 samples at the same rate. In this respect, they are the same instrument working the same way. So, that improves the signal-to-noise ratio

**Dave Jones:** by roughly 57 dB, massive. So, they get a 107 dB noise floor out of an 8-bit converter. Ha, unbelievable. And they go on to say that a traditional spectrum analyzer, like modern ones, they're also doing digital ADC sampling.

**Dave Jones:** You know, very few of them are, you know, really true analog anymore, but they're very low sample rate. So, if they're sampling at like 20 meg samples per second, it requires a 12.5 bit ADC to get the same signal-to-noise ratio as

**Dave Jones:** they can use an 8-bit ADC in the MDO series scopes. And of course, hey, you're already paying for that 8-bit ADC inside your oscilloscopes, so why not use it? It's very clever. But, there's one more trick up their sleeve, which

**Dave Jones:** confused us in the teardown because there was that local oscillator in there, that VCO chip. What the hell was that doing in there? Well, it was adding dither into the RS signal before the ADC to increase the spurious-free dynamic

**Dave Jones:** range. And they explain exactly how that works here. I won't bore you with all the details, but basically, it does this in the MDO 4000 as well, but they don't show it on the block diagram. But, in the MDO 3000, it's much simpler cuz

**Dave Jones:** there's no block down conversion. There's no IF frequency or mixer or anything like that. The RF just goes straight into the ADC. Well, but they add in or they mix in a dither signal like that. And basically, a dither

**Dave Jones:** signal is just a random noise, and of course, the VCO, the output frequency changes based on the input voltage here. So, you put a a random, you know, signal on there, you're going to adjust your frequency or dither your frequency that

**Dave Jones:** is added onto there, and that reduces your spurious free dynamic range by spreading it over your entire range of your array wider range of your ADC. But, yeah, you can read the white paper if you want to know

**Dave Jones:** how it works. So, there's no block down converter in the MDO 3000. It's just the RF straight in, and then they add the dither signal on here straight into the ADC. Now, the dither signal has to be just below, somewhere just below the

**Dave Jones:** Nyquist sampling frequency Nyquist frequency. Of course, we've got 10 gig samples per second here. So, 5 it has to be somewhere under 5 gig. And of course, as we saw in the data sheet, this HMC 429 VCO is designed for

**Dave Jones:** just under 5 gig. Perfect chip to add some dithering into there. So, that's all they got. So, that's the only cost that they're adding to this thing is this VCO. It's just some RF attenuating and some switching and some

**Dave Jones:** amplification. That's it. Bang, straight into the existing analog-to-digital converter in that that that you're using for the analog channels, and Bob's your uncle. So, the result of all this, you know, RF and digital processing magic is that they're able to leverage the

**Dave Jones:** existing analog-to-digital converter already in the scope, and to add some just some low-cost RF input parts that, as I said, only cost like, you know, 25, 30 bucks tops, and bingo, you got yourself a full 3 gig bandwidth spectrum

**Dave Jones:** analyzer that has a massive capture bandwidth over the whole effectively the whole range or 1 gig capture bandwidth, I think, in the case of the MDO 3000. It's absolutely incredible that you can get this performance. Of course, it is

**Dave Jones:** not as good a performance as a proper, you know, well-designed spectrum analyzer with a a better ADC in here, of course, but hey, you know, it it matches the performance is going to be similar to entry-level spectrum analyzers on the

**Dave Jones:** market. And hey, that's good enough when you include in just some basic spectrum analyzer functionality into a scope. It's brilliant. Unless they've got this thing patented, I expect all the other manufacturers are going to start up doing this with you know, in the

**Dave Jones:** not-too-distant future. But I suspect as with a lot of things, it's probably not as simplistic as it look. You can't just whack it in there and do a couple of routines and Bob's your uncle, you got yourself a spectrum analyzer. There's

**Dave Jones:** probably a bit of secret sauce and some, you know, tongue angle, you know, graybeard tweaking that goes on inside this thing to actually get it to work really well, but still, hey, you can get that spectrum analyzer for a low cost.

**Dave Jones:** Ah, it's brilliant. All right, I haven't put it fully back together yet, but I'm curious to know what happens when you power it up A without that communications with the case open like this and without the comms board plugged into it. And also I

**Dave Jones:** want to see what that mysterious, I think, finger touch switch does. So, I don't know, let's give it a go. Only one way to find out. And here we go. Whoop. We have some lights. No. Yes. It's booting up. I didn't have to touch

**Dave Jones:** the power switch, which is a soft power switch, by the way. Ta-da. Come on. Twiddle thumbs. See how long it takes to boot up. Quite a lot, I think. It takes like 30 seconds or something. I think it's on par with

**Dave Jones:** the Agilent. Haven't actually timed it yet. Ta-da. And ta-da. It's getting there. It's getting there. It's getting there.

**Dave Jones:** It's getting there. Not yet. Oh dear. There we go. We're on. Power on self-test failed. If the error persists after power cycle, refer to the oscilloscope to qualified repair personnel. There you go. You can proceed. If it's possible to save menu off error, this

**Dave Jones:** oscilloscope may not perform. There we go. Menu off. Warning, the oscilloscope is not compensated. Ta-da, but it has booted up. And if we push our RF button over here, there we go. Our RF is sampling. So, let's um I found a bug in this, by the

**Dave Jones:** way. Check it out. If you press the RF button again to turn it off, you would think it would go back to your digital channels, but watch this. It doesn't. It just freezes. Dumb. Oh, well, well, it hasn't actually locked

**Dave Jones:** up, but uh anyway, just press that and you're back. So, RF takes you into that, and then going back, you know, you can just press that and you're back in. But, uh just a silly little thing. Now, I'm curious to know

**Dave Jones:** what happens when you touch that magic finger sensor. Only one way to find out. Nothing. Bummer. Whoa, look at that. Warning, internal temperature is approaching a point where the oscilloscope could be damaged if you continue. Check that the

**Dave Jones:** fans are operating and there's sufficient clearance, blah blah blah. Yeah, TechScopes, they run hot. All right. Well, let's do a quick uncalibrated temperature of this thing with my Fluke E8. Look at that. I mean, I don't want to leave this thing here

**Dave Jones:** for too long, but uh yeah, I mean, well, they're silver heat sinks, so I may not have the emissivity set correct and all that sort of stuff, but we're we're talking, you know, 50° at least. Those heat sinks are a hot spot up in there.

**Dave Jones:** 50 on the other side of the board there. So, I'm not sure what's uh what's going on there. But, anyway, this thing it I think it did actually automatically switch off. So, uh yeah, it's definitely got some sort of internal uh

**Dave Jones:** temperature measurement and it does not like being operated with the case off. That's for sure. I mean, it was barely up for like a minute before two minutes before that warning came on. And yep, there we go. I just pressed stop and it

**Dave Jones:** switched itself off. So, yeah. Well, at least it won't damage itself, hopefully. And of course, system airflow-wise, that's why they've got the fan in this position and that's why they've got it blowing inwards. The air is sucked in

**Dave Jones:** from the outside here, from this uh vent on the outside, sucked in directly over, wham, right on top of the three main heat sinks here across the board, and then out the other side up there. And no, the fan is not very loud in this

**Dave Jones:** thing for those who uh are concerned about that thing. It looks like it does have variable speed on the fan cuz you can hear it sort of whir up as soon as you turn it on, it goes and then

**Dave Jones:** and then then it's a quite a low-level hum. It really is, you know, not that distracting. And there you go. It even logs that fire warning. During the previous power-on session, the oscilloscope automatically shut itself off due to excessive

**Dave Jones:** internal temp- temperature. Check that the fans are operating that there is sufficient clearance for airflow. Now, I'm not sure whether or not I'm supposed to be impressed by that or not. Impressed by the fact that, well, engineering the design

**Dave Jones:** engineers have thought of that. Like, you know, to actually put that menu in there. They're sensing the temperature, it'll automatically shut down. That's all really great, but you can't help but wonder, well, why is it shutting down in the first place? Is

**Dave Jones:** it that critical that you know, like less than two minutes after probably, you know, any a matter of a minute or two after you power it on, it shuts down due to over temp. I mean, jeez, what it can't last 10 minutes

**Dave Jones:** before the die gets up to temperature that it's obviously sensing? I don't know. I get the sense that maybe there's, you know, marginal thermal performance on this thing, perhaps. I don't know, but hey, this is Tektronix. I'm sure they know

**Dave Jones:** what they're doing, but they do have a bit of a history of with their stuff running hot, that's for sure. But with heat, of course, comes performance, usually, unless they're really piss-poor. But anyway, here it is. We'll only find out if its performance is

**Dave Jones:** great when we do the review, which will be coming up, of course. And in case you're wondering, does it work? Well, yes, it does. Here's my RF signal generator, 100 MHz -10 dBm, and there's the signal. There we go, almost bang on

**Dave Jones:** 100 MHz -10.3 dBm. Not a problem. And I just finished putting this thing back together, and damn it, I forgot that it has six instruments in one, and one of them is the arbitrary function generator, and that's on the output

**Dave Jones:** here. And clearly, that's on this board, which connects into the PCI slot. This is a board which handles a ton of stuff on the output. No wonder they have to put this little heat sink on this little beasty. Obviously, there's some

**Dave Jones:** sort of probably some sort of FPGA. I don't know if it would be a custom device or anything like that, but uh clearly, they're doing something to generate the AFG on this, because I didn't see any arbitrary waveform stuff

**Dave Jones:** on the other board, and it makes sense, of course, to put it on here. We've got some you know, output relay switching here, and well, the switching the 50-ohm load termination and stuff like that. So, this looks like function generator

**Dave Jones:** circuitry, and obviously, some sort of FPGA or some other controller to handle it. And we always forget about the line frequency trigger. There it is. They've just got two wires heat shrunk over the mains cable there. No, that is not

**Dave Jones:** making any direct connection. It's just a you know, a proximity, a capacitive coupling thing. And that's coupled into that little chip down there. Not sure what it is. Couldn't be bothered reading the number. Anyway, that does your line

**Dave Jones:** triggering 50 or 60 hertz depending on where you are. 50 hertz here in Australia. Once again, a high speed comparator ADCMP 562. So, it looks like we don't have a at least I can't see any DDS generator. So, it's obviously doing it

**Dave Jones:** internally. Well, it is a full arb generator, of course. So, yeah, most likely it's just doing it completely internally inside that FPGA or whatever that beast is. So, yes, the entire arb generator seems to be that single chip there. And pretty much just

**Dave Jones:** miscellaneous support stuff. There really doesn't seem to be anything else happening there. There's our output buffer there obviously with our 50 ohm output terminator switchable with the relay. And that just goes to the output. And that's it. I mean, yeah.

**Dave Jones:** They haven't added much cost there at all. So, there you have it. I hope you enjoyed the teardown of this new brand spanking new Tektronix MDO 3000 scope. And yes, it is a bit of a game changer. The MDO 4000, its big brother, was a

**Dave Jones:** game changer in that you could get that mixed domain debugging capability, which was so fantastic. But woah, did you pay a price premium for it. But now with this sucker, they've brought it down into the you know, affordable mid mid

**Dave Jones:** level domain to compete with well, their major competitor obviously, the Agilent 3000 X series. And they're about equivalent on price. The base model, absolute bare bones 100 megahertz dual channel version of this is about 3300 US dollars and the Agilent one is

**Dave Jones:** about 3200 or something. It's a little bit cheaper for the equivalent bandwidth and number of channels, but this sucker you get the RF spectrum analyzer built in 3 GHz capable of course, but hey, you know, everything's optional extra with these

**Dave Jones:** companies. So that's an extra 2500 bucks if you want to enable the 3 gig spectrum analyzer front end, but at least you do get it built in in the base model up to the bandwidth the the scope. So you buy

**Dave Jones:** the 100 MHz model, you get at least a 100 MHz spectrum analyzer, which is better than just the FFT built into a regular scope. It's got better performance than that. Um so really that is quite interesting and it will be very

**Dave Jones:** interesting to see what the competitors do if they eventually bring out a mixed domain scope as well. Um well, they might be already working on them since uh Tektronix the big brother MDO 4000, but I found this rather interesting

**Dave Jones:** teardown. I expected a lot more in here, but they haven't. They've really gotten the price down the the system integration. They seem to have done a lot of work in that respect to actually get the price of this sucker down and uh

**Dave Jones:** you there's a performance hit in that respect in that it's not a true mixed domain oscilloscope anymore like the MDO 4000 series and that was the huge advantage of that. You could actually capture the uh RF and your analog and your digital

**Dave Jones:** all at the same time. So it was truly a mixed domain. This really isn't. You have to choose either the spectrum analyzer or the analog front end. So a bit disappointing that, but hey, you effectively get the free spectrum

**Dave Jones:** analyzer thrown in for free. So really you can't complain. Now I did look at the uh bill of materials cost. I thought they were being a bit silly with this thing by bundling in the spectrum analyzer built in, but as we've seen, there's hardly

**Dave Jones:** any circuitry in there at all. And I actually costed it out all the main chips, and even at Digikey prices, we're only talking 25 to $30 in 10,000 quantity at Digikey prices for the spectrum analyzer functionality. That doesn't include the connector or the RF

**Dave Jones:** diecast can or something like that, but you know, even then it's worth should be well under 50 bucks bottom cost added just for a full 3 GHz spectrum analyzer. So, that's a bit of a killer. Unfortunately, you do have to pay for it

**Dave Jones:** with the software options, but anyway, this is a really nice compared this scope. I don't haven't used it all that much yet, and a review will follow, of course, but I hope you found the teardown interesting because they have

**Dave Jones:** done a few interesting things in here to make it competitive. Awesome. Teck are back. Excellent. So, if you want to see those high-res photos, as I said, check out the eevblog.com. Link is down below, and as always, there's a forum link down

**Dave Jones:** below where you can discuss this thing to your heart's content. There you go. And as always, if you like the video, give it a big thumbs up. Beauty. Catch you next time.
