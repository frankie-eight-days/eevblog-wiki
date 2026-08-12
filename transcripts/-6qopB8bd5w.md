---
video_id: -6qopB8bd5w
title: EEVblog #589 - Voltech PM300 Power Analyser Teardown
url: https://www.youtube.com/watch?v=-6qopB8bd5w
source: youtube-asr
timestamps: {"0": 0, "1": 13, "2": 29, "3": 44, "4": 59, "5": 76, "6": 84, "7": 103, "8": 117, "9": 129, "10": 149, "11": 159, "12": 173, "13": 189, "14": 203, "15": 218, "16": 227, "17": 247, "18": 265, "19": 278, "20": 291, "21": 312, "22": 324, "23": 336, "24": 351, "25": 361, "26": 379, "27": 396, "28": 410, "29": 428, "30": 438, "31": 455, "32": 469, "33": 488, "34": 505, "35": 515, "36": 529, "37": 545, "38": 560, "39": 582, "40": 592, "41": 601, "42": 617, "43": 626, "44": 640, "45": 649, "46": 664, "47": 672, "48": 689, "49": 699, "50": 709, "51": 725, "52": 739, "53": 757, "54": 775, "55": 787, "56": 796, "57": 805, "58": 814, "59": 828, "60": 842, "61": 854, "62": 865, "63": 874, "64": 890, "65": 909, "66": 919, "67": 935, "68": 944, "69": 958, "70": 973, "71": 991, "72": 1009, "73": 1020, "74": 1033, "75": 1052, "76": 1063, "77": 1083, "78": 1108, "79": 1123, "80": 1132, "81": 1143, "82": 1160, "83": 1169, "84": 1184, "85": 1199, "86": 1218, "87": 1229, "88": 1241, "89": 1251, "90": 1264, "91": 1275, "92": 1284, "93": 1300, "94": 1318, "95": 1334, "96": 1343, "97": 1359, "98": 1382, "99": 1389, "100": 1409, "101": 1419, "102": 1431, "103": 1445, "104": 1456, "105": 1474, "106": 1488, "107": 1497, "108": 1507, "109": 1526, "110": 1547, "111": 1556, "112": 1568, "113": 1580, "114": 1595, "115": 1605, "116": 1619}
---

**Dave Jones:** Hi, welcome to Teardown Tuesday. We've got ourselves a power analyzer today. Haven't had a look inside a power analyzer before, so should be a little bit interesting. This is a Voltech PM300.

**Dave Jones:** And if you're like me, you haven't heard of Voltech before. They were sold off to Tektronix sometime ago, and Tektronix still do sell some of the Voltech power analyzers, the PA1000 and the PA4000.

**Dave Jones:** You can still buy them, but anyway, this is a nice little bit of kit which I picked up at an auction, and it is a three-phase power analyzer. There's the voltage and current inputs, and it's got a nice big graphical display on it as well, which shows all sorts of stuff, including all three channels at once.

**Dave Jones:** It even has a waveform mode that can actually show the waveform. And of course, it measures a whole range of you know, power stuff, not only for mains, although you know, it goes up to like 500 or 1000 volts or something like that.

**Dave Jones:** But it can also they do smaller voltages and currents as well, multiple ranges, and it's a really nice bit of kit. And of course, it can measure everything, you know, it can measure voltage, current, phase angle, real power, apparent power, can even do inrush current, which is really handy.

**Dave Jones:** It can has a ballast mode where it can do you know, high frequency ballast outputs and all sorts of stuff, peak and averages and all sorts of things like that.

**Dave Jones:** So, really very handy power analyzer for really you know, measuring the power consumption of products, because it's not that easy, you know, you get one of these cheap ones you buy on eBay for 10-15 bucks, gives you a rough indication, but you know, these things really go to town.

**Dave Jones:** Uh pretty accurate, too, 0.1% on pretty much all the ranges. So, and all the functions. So, pretty awesome. Should be interesting inside. Let's take a look. Not hugely complex, but hey, you never know.

**Dave Jones:** So, you know what we say here on the EV blog, don't turn it on, take it apart. Now, I'm not exactly sure how old this unit is, but it has a calibration date on the back of 2004.

**Dave Jones:** So, it's at least a 10-year-old design, but still pretty kick-ass by modern standards. You get a 0.1% three-phase power analyzer with all the bells and whistles. And good thing about learning about new brands like this Voltech one that I haven't heard of before, you add them to your eBay watch list.

**Dave Jones:** I've got a list of, you know, the more obscure name products out there, and you just keep that eBay watch list, and an alert pops up if, you know, something on the market comes up.

**Dave Jones:** Now, this is actually an ex-military unit, same as the oscilloscopes I scored recently, but it came in a nice padded custom Pelican case, genuine Pelican case. And it looks like it's hardly ever been used.

**Dave Jones:** Got some writing on the front here, but yeah, I think it just sat in a warehouse for like 10 years. There it is, calibration due 2004. So, I expect this to have been manufactured maybe in the early 2000s or something like that.

**Dave Jones:** We've probably only got like calibrated once or something like that when they originally got it. And so, it could be like 2003 would be my best guess. It's got what looks like an optional module here with the printer and RS232 interface, so you can actually get the data out of this thing.

**Dave Jones:** Standard IEC mains input, switchable, of course, which is really handy. It's got a voltage selection switch there, and three separate channels for your three-phase measurement. I've got no need for three-phase measurement here, of course.

**Dave Jones:** I don't even have three-phase power coming to the lab. Oh, no, no, actually, technically, I do. I think I have it into the switchboard, but I certainly don't have any three-phase outlets.

**Dave Jones:** That's for sure. So, I'll just use it as a single channel. And you can actually hook up an external current and use an external current shunt and you can actually program the in but it recommends of course that you use the internal current shunts for these things and they can be linked in the manual the user manual for this thing down below and it shows how it can be configured in

**Dave Jones:** Delta Y configurations for the various phases and all sorts of stuff. So very flexible input. So it looks like you know what we're likely going to see inside construction probably three separate cards for this a huge base board in there something like that and maybe a separate display board on the front and front panel board.

**Dave Jones:** So I would expect these to be separate isolated. They are galvanically isolated. So the obvious well there are a couple of ways to do that either you try and do it analog or digital.

**Dave Jones:** For me if I was designing this thing I would do it digital. So I'd have the because these are very you know very precise. They're going to have a you know like a 16-bit converter in there or something like that.

**Dave Jones:** You know it needs to be really precise AD conversion in these things and front end amplifiers and range switching and stuff like that. So I expect all that including the ADCs to be on each separate card there and then like a serial data interface to that because this thing I think sound like has a 50 kilohertz bandwidth or 100 kilohertz or something like that.

**Dave Jones:** It's not you know huge so you can just get the data over digital serial interface and it's much easier to galvanically isolated digital interface just using some optocouplers than it is to do it analog wise.

**Dave Jones:** So anyway it could be interesting. Let's crack it open. You bet your ass we're going to void the warranty. Let's do it. One of the most satisfying things you could do.

**Dave Jones:** Look at that. Brilliant. There's a tiny little fan on the base of the unit here. It doesn't really need much uh at all because well, there's no huge power dissipation in inside this thing.

**Dave Jones:** It might be drawing, I don't know, you know, 10 watts or something just to power the electronics, not even. And uh the current shunts aren't going to be dissipating much power anyway, so there you go.

**Dave Jones:** Um I expect uh some through-hole technology in here, of course, probably a mix of uh uh through-hole and surface mount, probably predominantly surface mount. The processor, you know, processor inside this thing, they're not going to have a huge um processor or anything like that, just some sort of 8-bit or 16-bit micro uh possibly, something like that.

**Dave Jones:** So, looks like we need to get the back off here. And uh anything else? No. Don't know. Okay, let's try and slide this forward. Hmm. Well, there you go.

**Dave Jones:** I just took out the serial uh parallel module and yeah, it's all through-hole. So, this thing could be maybe entirely through-hole or mostly uh through-hole anyway. Obviously, got some sort of uh micro over there.

**Dave Jones:** Huge big um through-hole package, very traditional-style card edge connector routed into the board out in here. So, that that is quite a nice design if somewhat ancient. Uh yeah, date code as I suspected, 2003.

**Dave Jones:** There you go. Got ourselves an Hitachi H8. So, if we've got one on here, uh very likely to find a an Hitachi micro also inside. Aha, I was wondering where the other screws were.

**Dave Jones:** There we go. That's a bit sneaky. No, I can't get the get this rear bezel off cuz it's got I can see under here, it's got another probably three screws up under there, but it's under the case, so I can't slide this case off forward or backwards.

**Dave Jones:** So, I probably can just going to have to lever off one side like that. Uh tricky. Almost in. And uh yeah, it did have those screws on top, so I had Buckley's chance of sliding the thing back out.

**Dave Jones:** So, it's got to come off over like so. Oh, man. That's one tricky little mongrel. But, tada! We're in. Well, it looks like I was wrong on the uh three-board uh construction there for the three different channels.

**Dave Jones:** No, we can see right through there. Hello. Looks like um what they've done is they split it into a uh single phase. So, maybe they sold a single phase unit of this, and you only got the bottom board, cuz we can see some shunts down there, and the ranges for uh phase number one.

**Dave Jones:** You know, the inputs for phase number one down here, and the top board is just two additional uh phase boards. And yes, the uh single phase model is the PM100.

**Dave Jones:** The manual uh shares between those. I forgot about that, and uh it's really interesting kind of uh construction like this. Check out the board up in there like that.

**Dave Jones:** There we go. Actually, a a connector sandwiched between the top and bottom boards here. It's got card edges on both sides. That's really quite fascinating. I've done the screws off there.

**Dave Jones:** Oh, it looks like it's just going to pop off. Oops. Here we go. Tada! And apart from the uh the wiring we're in. There we go. So, if you just got the uh PM100 model, you just get that base board down the bottom.

**Dave Jones:** And what's kind of annoying is that they haven't really put uh servicing thought into this. I mean, they haven't left enough lead length here for me to swing this board out completely, but I guess even then, of course, to actually plug this board in and get it working, you have to plug it in to this top board up in here, like this.

**Dave Jones:** It's got to plug into there. So, it's got a sandwich construction. You can't get access to the damn board to even probe it while it's operational, or it's very difficult anyway.

**Dave Jones:** Yeah, real pain in the ass to service something like this. One of the first things I noticed was this little wire budge over here going down Well, it's powering the fan.

**Dave Jones:** They've basically got the fan directly as a red wire connected there, and black one going all the way over to the other side of the cap there. And they're just budgie soldered onto the leads of these axial main output filter caps from the transformer here.

**Dave Jones:** Almost as if the fan is an afterthought. Because if you were designing a fan in from the start, you would have put a two-pin connector on there to plug your fan into, right?

**Dave Jones:** So, uh beats me. Mm. And they've put a cutout in the board here, and they've mounted what looks like I can't get the number on that yet. It's probably a you know, a linear reg or something.

**Dave Jones:** 78 Yeah, I think it is a 7805, and they're using that big block down there as a heat sink. And of course, yeah, there's nothing special with the transformer there.

**Dave Jones:** They've used a just a a PCB mount mains transformer there. And well, there's a full wave bridge rectifier on the output there. There's four 1N 4001s there, plus some beefy output filter caps.

**Dave Jones:** But that's it, you know, it doesn't need much power to power all this circuitry as I said. And there you go. As we guessed, exactly the same processor used on the inside here.

**Dave Jones:** Hey, you know, you've already got the development tools for it. It's already in your bill of materials. Why not reuse it on the serial one as well? Even though it's overkill for the serial interface card, it's probably you know, it's good enough for something like this anyway to drive the graphical LCD display.

**Dave Jones:** And clearly, it speaks French. Hm. I don't, that's for sure. And the only surface mount stuff we've got in this whole design is on, as you'd expect, on the front panel LCD.

**Dave Jones:** And yeah, this is not a Voltech design. They've just used an off-the-shelf module or they've got an OEM, you know, to supply them a module. And that's uh pretty much it.

**Dave Jones:** The interesting part about it is that the ribbon cable goes to this vertical, I think they call it an interface board. Like, you know, it's just crazy. Why? You'll notice all the uh pins on one side there are uh shorted out, especially on that uh top one there.

**Dave Jones:** But like, why? And look, behind it, they've got a an unused IDC header connector there. This is uh it's bizarre. And in case you're wondering, no, that one can't just be plugged into there.

**Dave Jones:** It's actually two pins short. So, that raises the bizarre question that well, what do they do in the PM 100, the one channel one phase module? They would have to have this vertical riser board still, even though it says it's the PM uh 300 interface board there.

**Dave Jones:** Like, huh? What the? And on this interface board, well, just a whole bunch of eight-bit shift registers. Uh 74HC 4094s. And what are they? 74HC597s. Go figure. And then just a miscellaneous uh HC04 inverter over this side.

**Dave Jones:** So, they're obviously uh shifting the data in from the other two channels on the board on top. But it's just it's bizarre. Anyway, well, we do have an eight-bit micro here.

**Dave Jones:** So, we've got to interface everything to that eight-bit micro bus. But jeez. And I'm never a big fan of crystals just freestanding like that, just flapping in the breeze.

**Dave Jones:** You get the right vibrational mode and off it's going to come. And we've got our serial interface board uh being plugged into this cartridge connector on the front panel.

**Dave Jones:** So, there's obviously a front panel connector board in there. I'm not going to bother taking this whole thing apart just to get at that to look at uh you know, the front panel user interface and stuff like that.

**Dave Jones:** Eh, boring as bat poo. It does look like though they've just got the all the buttons in a matrix, of course. Uh the front panel coming back, there's actually two of these uh multi-way ribbon connectors going down to the front panel board behind that shield in the front.

**Dave Jones:** Now, let's take a look at the interesting stuff and we're just going to have a look at one channel of this uh top two channel board. Yes, I have locked the other identical uh the other channel on the other board uh down at the base there for the PM 100.

**Dave Jones:** It's just another duplicate of all this channel. So, we're only concent- And these look like two identical channels. So, we'll just concentrate on one. And no surprises for guessing exactly what I thought it would be.

**Dave Jones:** Uh they're all galvanically isolated. Check this out. You can see the split in the ground plane, totally separate ground planes between all the channels. Looks like we've got some input attenuation here.

**Dave Jones:** We'll take over that. Very interesting looking uh current shunt on the input there. We've got some protection. We've got some interesting looking uh transformers here. We'll have a look at those in a second.

**Dave Jones:** And there's our uh galvanic isolation using three optocouplers there. So, we're just getting serial data out of this thing and that's exactly what you'd expect. Now, if you were paying attention, you would have realized that there's no power There's no other wires coming to this board.

**Dave Jones:** Ordinarily in an isolated design like this for simplicity's sake, the main transformer mains transformer on the input would have separate winding isolated winding taps for each of these. And you know, you know, you'd have a connector over here or something or you know, plugs in to each module coming from each isolated tap on the transformer.

**Dave Jones:** But, they haven't bothered to do that. All of the power is coming in via this card edge connector here. And so, aha! Well, how are they getting the power across?

**Dave Jones:** It's It's coming across the optocouplers. Bingo, it's coming across these two transformers up here. Little hand hand wound jobs, interesting. And this is very very interesting. You can tell it's uh power transfer by the big beefy tracks on one side.

**Dave Jones:** Looks like they might have a uh switching transistor here. So, they're obviously uh driving this at uh you know, switching the thing and then they've just got you know, this one's actually got uh two turns on it.

**Dave Jones:** This one's only got a single little turn. And look, they're actually using two in series like that. Look, this winding here is just directly connected to that winding. You can see the traces going like that.

**Dave Jones:** So, look at that. It's a two uh well, a effectively a two-stage transformer there going to the other side. And of course, it's a dead giveaway. They're just doing some filtering and then yeah, some rectification and then some uh filtering there.

**Dave Jones:** Probably got some uh voltage local voltage regulation in there, sort of TO-92, you know, 7805s or something like that happening. But that's rather interesting. Look at that. They've gone to quite a bit of trouble there to custom spec and wind these transformers.

**Dave Jones:** And they've used two of them. So, why they've gone with two like that in series, you know, your guess is as good as mine really. I What did they not uh get the voltage specification they were looking for, the isolation specification with just the one?

**Dave Jones:** Huh. And there's our switching transistor on the primary side. It's a 2SK940. So, they're just doing crude switching of the uh primary side there and well, they just rectify the output of the secondary and Bob's your uncle.

**Dave Jones:** So, it's very crude and very inefficient, but you know, hey, it gets the job done. Whatever floats your boat. And no surprises for guessing for finding some pretty beefy uh optocouplers here from Avago.

**Dave Jones:** Love that name. Ah, Avago, you mug. Love it. Um in these cases these are uh 10 megabit So, pretty darn quick. Uh I think uh 3,500 V RMS optocouplers with five uh kilovolts per millisecond transient voltage on them.

**Dave Jones:** So, you know, really pretty beefy optocouplers. Well, I was way off the mark on the ADC. Look at this. Pretty old school. Two of them as you'd expect, one for the voltage, one for the uh current on each channel.

**Dave Jones:** But, very old school AD 7575 ADCs. Geez, I used this these donkeys years ago. Eight-bit successive approximation converters. Really nothing fancy at all. Although, I guess all I need is eight-bit uh resolution on this thing cuz it does have uh various ranges.

**Dave Jones:** It's got like eight voltage and current ranges or something like that. Speaking of which, the range switching, nothing fancy going on here at all. Just some 74HC4053 analog muxes.

**Dave Jones:** Uh TL071, is it? Yes, that's a TL071 op amp. And another 74 you know, 4000 series mux. I mean, geez. Nothing happening here at all. So, this is pretty interesting.

**Dave Jones:** I mean, it obviously two paths here. One on this side here is for the voltage. The voltage comes in, we'll take a look at that in a second. The other side here is for the current.

**Dave Jones:** We can see the big current shunt down the bottom. Basically identical uh paths like this, and they've just got that uh you know, 4000 um and tight series analog switching and various op amp gain ranges.

**Dave Jones:** So, clearly what they're This isn't auto-ranging units. So, clearly what they're doing is just at the higher uh gain levels, they're just um letting the other op amps, uh you know, overload and saturate and then switching between those as it goes down in ranges.

**Dave Jones:** So, they're obviously getting away with that. Nothing fancy here at all. It's not like they got, you know, a relay switching or anything like that. Really, you know, basic configuration stuff.

**Dave Jones:** And the input here, very basic attenuation. They're just got four dropper resistors on each leg here, basically attenuating the input signal here down to bugger all to go into this max here.

**Dave Jones:** So, you know, really, no matter how high the transient voltage, it's not going to damage the input there. That's why we basically don't see any input protection. If we have a look around here, you just don't need it because you're just attenuating the input so much.

**Dave Jones:** I mean, there's nothing on the input protecting that at all. And as far as our current shunt goes here, well, look at this. This is a fancy pantsy. It's an SMD current shunt, I guess you could call it because it is actually, you know, soldered, although surface mount onto large pads over here.

**Dave Jones:** And that's super duper wide. What is that? Like, you know, 30 mm wide. That's going to be a low tempco metal, of course. And they've looks like they've made no attempt at all to actually trim that.

**Dave Jones:** Trimming would be done in software afterwards. So, yeah, they're not going to dick around and laser cut that or, you know, solder little bits on there to sort of, you know, change the resistance of mine mine you to mount something like that.

**Dave Jones:** Yes, that is a cutout down in the boards there, so that can extend down below the board. And of course, there's no fusing on this puppy at all. It's just, yeah, it's straight into there.

**Dave Jones:** Look, big beefy blade terminals there soldered directly into our current shunt. And if you're wondering what this circuitry here, this is the external current shunt input. So, they've just got added some protection there.

**Dave Jones:** There's a thermistor on the input there. Dead giveaway, TH1. Looks like they got a botched ceramic cap on there just for some extra noise suppression there. Hey, if you're going to botch it, do it nice.

**Dave Jones:** They've put heat shrink tubing over the leads there and a couple of back-to-back diodes in a series resistor there. So, that's just a feed in an external shunt voltage if you want to.

**Dave Jones:** So, anytime you're feeding in external voltages like that, you have to add some input protection and some noise suppression. And on every back panel connection there for the voltage and current input, they've got that noise suppression to ground, high voltage ceramic cap there, 6 kilovolts, 22 nanofarads by the looks of it.

**Dave Jones:** Look at those, ceramic noise suppression caps down to earth as far as the eye can see, all the way through there, every back panel connector except for the external current shunt input as we saw, which is taken care of on the main board as we just saw before.

**Dave Jones:** Right next to our ADC there, we have ourselves our voltage reference. There you go, a little two-pin shunt. And the voltage regulators on the output of the voltage isolation that we saw before for the power coming in, yeah, no surprises as I guess, 78L05s.

**Dave Jones:** And of course, make that a split supply with the 79L05 negative. So, you might still be wondering the input configuration here, voltage and current, they're obviously not galvanically isolated.

**Dave Jones:** So, how does that work? Well, of course, the entire channel here is galvanically isolated by the by the transformer over here, this switching transformer that provides the positive and negative 5-volt rails for all the logic.

**Dave Jones:** But, basically, what they're doing here is they're referencing everything to the current shunt here. So, the current shunt would effectively be the reference voltage and because we've got such a large input attenuation here on the voltage side, you can pretty much do whatever you want on the voltage inputs here and pretty much not blow anything on the input stage.

**Dave Jones:** That's why you don't find any protection in there as I said before. And of course, you wouldn't be able to do that if you only had single side attenuation here.

**Dave Jones:** If you were say referencing one of the voltage terminals, it would have to be common referenced to the current shunt down here. But because they've got two separate high voltage attenuators on the input effectively, this voltage you can hook it up wherever you want over the entire operational range of this thing and you're not going to blow anything.

**Dave Jones:** And then the data output side of our ADC, as I said, it's an 8-bit parallel output. So they're just whacking that into some shift registers. And of course, we don't have enough bits there.

**Dave Jones:** So they're just feeding that over the optocoupler. And well, that's it. Nothing fancy whatsoever. Oh, I forgot to mention there is a trim pot down here. I'm not sure exactly what they're trimming.

**Dave Jones:** If that's only in the voltage path, they don't have a similar trimmer pot in the current path. So I'm not exactly sure what they're doing there. You can calibrate this thing in software anyway to you know, there's a whole procedure in the manual to do that.

**Dave Jones:** So there you go. I hope you found that relatively interesting. That was the Voltech PM 300 power analyzer. Well, and it was a little bit different than I expected.

**Dave Jones:** This is clearly with all through hole technology and the ancient Hitachi processor stuff like that, you know, it's based on a much older design and they've just carried that over into future designs cuz you know, this thing well, here it was manufactured around that 2003 date or something early 2000s.

**Dave Jones:** They've only manufactured this is serial number 2000 or something. So it hasn't manufactured too many before that. So you know, it's like late '90s design at best. So I'm surprised we didn't see any surface mounting there.

**Dave Jones:** But that's what you get in these products. The designers of these products, if they're familiar with all the stuff before, then they're not going to change everything when just for a new model.

**Dave Jones:** No, oh, let's all go surface mount. Well, why? You know, it's worked before. All our footprints are like packed here in our CAD package. We'll just run the damn thing again.

**Dave Jones:** Heck, even our layout can probably reuse a layout from an existing product or something like that. But, yeah. Anyway, um there's very crude sort of ADC front end, just 8-bit ADCs that fixed fixed gain ranges with the 4000 series marks on there to switch.

**Dave Jones:** They're obviously overloading the other ranges when you switch low, but it doesn't matter. It's just internally clamped, and it's all just fine. And you can manually auto switch between those ranges seamlessly cuz this thing just continuously samples all the time, of course, at uh you know, like at 100 kHz or some fixed sample rate or something like that.

**Dave Jones:** It does that to be able to do the transient capture and all that sort of stuff. So, actually collect the data, and then uh dump it or uh display the waveform at a later date.

**Dave Jones:** So, it's got to be able to do that auto range switching. And that's just a crude easy way to do it. And with the voltage input, they don't even need any uh you know, any protection or clamping on the input.

**Dave Jones:** Just attenuate the buggery out of the voltage input. That's it. I don't know. I expected a little bit more complexity from all that, but it is what it is.

**Dave Jones:** There you go. It obviously quite works. It's really quite accurate and professionally This is a professional level product. It's not something that you'd buy on eBay. It's from a company that specializes in these sorts of power analyzers, and they're probably been designing them since before I was born.

**Dave Jones:** I don't know. Anyway, now it's owned by Tektronix and the Danaher group. Groan. Anyway, I hope you enjoyed that. If you did, please give it a big thumbs up.

**Dave Jones:** And if you want to discuss it, the forum links are down below. That's the best place to do it. And as always, I will have high-res photos of this teardown available on evblog.com.

**Dave Jones:** And the link for that will be down below, as well. So, go there and check out the photos. Hope you enjoyed it. Catch you next time.
