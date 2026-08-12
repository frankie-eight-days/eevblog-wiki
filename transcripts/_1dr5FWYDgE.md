---
video_id: _1dr5FWYDgE
title: EEVblog #1029 - BGA PCB Fanout
url: https://www.youtube.com/watch?v=_1dr5FWYDgE
source: youtube-asr
---

**Dave Jones:** All right, let's take a look at the Actel Igloo part here on a real FPGA. This is a fairly small board. It's only 50 mm by 33 mm. Couple of 0.1 in headers here. There's the JTAG interface down

**Dave Jones:** here. 0.1 in dual row pin header down there. Pretty standard, but look at the size of this chip here and a couple of 0603 surface mount bypass caps. Let's take a look at the chip. It is absolutely tiny. And if we have a look at the 3D

**Dave Jones:** view here, you can see that the FPGA itself is only 3 mm by 3 mm. And it really is not much bigger than than the footprints of the two 0603 bypass capacitors here. Absolutely crazy. It's That's how small this device

**Dave Jones:** actually is. It's one of the the smallest FPGA on the market, but I mean, we can go for smaller bypass caps there, of course, but really, you know, it depends on the design you want to do. This is a

**Dave Jones:** prototype, so I'm going to use 0603. Now, the device, as we've mentioned, is a 0.4 mm pin pitch. So, it's 0.4 mm between each one of those pins. Now, this is a standard footprint for this for this particular BGA device. It's 36 pins. You

**Dave Jones:** can see the tiny little pads in there. Now, the first thing you're going to want to do when you put this down is to figure out how you're actually going to route out, or what's called fan out, the pins

**Dave Jones:** on this device. And And is dependent upon whether you're using a uh double-sided board or you're using a multi-layer board. Now, I'm going to put this on a double-sided board, and I've decided to actually uh completely fan out the device on the one layer, and I

**Dave Jones:** can do this because it's only effectively uh two layers deep on the outer um pads to get down to the core down here. Now, these uh traces uh because um well, FPGA, when you're fanning out these sort of things,

**Dave Jones:** there's a whole trade-off between uh how many layers PCB you're going to do when you're fanning out these BGA type devices as opposed to a quad flat pack or something like that which has all the pins around the outside, and you can

**Dave Jones:** just uh route them out really easily. But because this is a BGA device, a ball grid array, real pain in the ass. And uh this is why it's a massive trade-off between your ability to route out the traces and the minimum trace width.

**Dave Jones:** These traces I've got here, they're only 0.1 mm or uh just on 4 thou uh width. And a lot of the cheap PCB manufacturers will not be able to do 4 thou traces. If you want to go to um you know, or you'll

**Dave Jones:** have to pay more for that technology. So, we're using a 4 thou track and space as it's called in between here. Then uh really we have to uh pay a manufacturer who's capable of manufacturing a what's called a 4 4

**Dave Jones:** um spec board, 4 thou trace, 4 thou clearance. And that doesn't include any vias at all on this design. Now, I've got some vias up here. Now, they might look uh like typical vias, but take into account that my grid space in here is

**Dave Jones:** 0.1 mm. Okay? Each one of these grids, and this via here is a hole size, a drill hole size of 0.1 mm. It's ridiculously small, and it's got a pad diameter of 0.2 mm. You know, that's quite leading-edge stuff. You would be

**Dave Jones:** very hard-pressed to get anyone to do anything under this one here, which is a 0.3 mm hole size or and a 0.4 mm pad. Now, generally you wouldn't do that because you would want to include a bigger ratio

**Dave Jones:** between the via hole size and the pad size. So, you might want to increase that to say 0.5 mm like that. So, you don't get what's called a via breakout. So, the drill is not always aligned perfectly, and it you don't want it to

**Dave Jones:** break out the pad. So, you've got to take into account what your PCB manufacturer specifies in their tolerance there. But, that's a 0.3 mm, which for general boards, you would not want to go below 0.3 mm drill size.

**Dave Jones:** Trust me. Uh get you're in for a lot of expense and and special costing. Now, this is a 0.4 mm via size here, but I would typically use on a dense surface-mount board. I'll typically My standard via will be 0.3 mm like this

**Dave Jones:** one. Now, if I try and drag that via under this chip, and you can see because it's only a 0.4 mm pin pitch, I can't use a 0.3 mm via under there. It's impossible. Maybe I could get away with a 0.2 mm via if I

**Dave Jones:** reduced the solder mask expansion, which we've got here, but we'll talk about that in a second. If I want to uh actually fan out this FPGA on different layers with vias, I'm going to have to use a 0.1 mm drill size. Maybe I can get

**Dave Jones:** away with 0.2, but it's just crazy. Now, um solder mask, as I've shown in my soldering tutorials, is very, very important here. Look, you can see that tiny sliver down there. The manufacturer is not going to be able to manufacture

**Dave Jones:** that, okay? There'll be no solder mask left. We've actually got a what's called a solder mask expansion here of 0.05 mm or 2 mil or 2 thou, okay? That is a very small solder mask expansion. On a general board, you might use, say, 4

**Dave Jones:** thou, but because this is a very dense chip, which, by the way, this chip drives this entire design, okay? You might have through-hole parts on the rest of your board, big through-hole parts, massive pin pitches, you can use

**Dave Jones:** 20 thou tracks, 20 thou space, but because you've decided to use this little tiny piss ant FPGA in this pain-in-the-ass 0.4 mm pin pitch BGA package, bingo, instantly your to get your PCB manufactured, you've got to go down to

**Dave Jones:** at least 4 4 thou rules, or if you wanted to route out individual vias on different layers, say this was a four-layer board and you wanted to use the a drop through to the bottom layer to route out some of those pins,

**Dave Jones:** well, you've got to use a tiny little drill size like that. Now, I could actually change my solder mask expansion if the manufacturer actually could actually do this. I could change it down to say 1 thou like that, and you'll see

**Dave Jones:** it change. And in this case, I might be able to get away with a 0.2 mm, maybe, but look at the solder mask expansion there, it's bugger all. So, you don't want your paste when you solder this in your solder paste to

**Dave Jones:** short out to your via, and you would want what is called a tented via. So, you'd want to go in there, and you'd want to force tenting onto those vias like that, so that there is no solder mask expansion. So,

**Dave Jones:** when you flip to the 3D view, you'll actually see the difference there. So, if I drag say two vias in here like this, I've got my 0.1 mm one here, my 0.2 mm. This one has tenting on the top of the via, top and

**Dave Jones:** the bottom. So, if we go into 3D view here, you'll see you'll notice that this is what one of the things 3D mode is really great for because it can actually show you the the real solder mask expansion on the board and what

**Dave Jones:** it's actually going to look like. In this case, it's a blue solder mask and you can see the individual pads there and the solder mask expansion. Once again, remember we've only got a very tiny, very tight tolerance 1 thou solder

**Dave Jones:** mask expansion on those pads. The manufacturer is going to choke when they hear that. They're going to charge you a crap load of money if they're actually able to do that at all, but as you can see, this one here this 0.2 mm hole

**Dave Jones:** here, doesn't matter if it's 0.1 or 0.2 mm what the size is, but because it's forced tenting on top of those, then um there is no chance of paste when you manufacture your board, you'll lay down some solder paste, no chance of it

**Dave Jones:** shorting to the via next to it. But, look at this one here. It's tiny and that distance in there is only going to be less than 0.1 mm. It's tiny. So, if you accidentally get solder bridging across there, you're in deep trouble if

**Dave Jones:** you've applied too much solder paste. So, really when you're doing high density BGA boards like this, make sure that you tent your vias and you might actually have to plug them, too. You might have to get the manufacturer to what's called

**Dave Jones:** plug it and they actually put a little resin or something in inside to plug the hole first so that the solder mask truly does cover it. But, when you're talking about like a 0.1 mm hole like this one, which is insanely

**Dave Jones:** small, it's almost a micro via size really. So I've just start tinted that one. There you go. It's tinted. Just make sure you tint or plug them. Otherwise, you could end up with massive shorts under there and you won't be able to inspect it of

**Dave Jones:** course and you won't know until you go and actually power up your prototype and it could actually even go bang if you accidentally short out ground and power. Poof. Release the magic smoke. Oops. Now, I got a little bit sidetracked there

**Dave Jones:** talking about all that sort of stuff, but we're talking about fanning out this FPGA either using vias or traces. Now, because this is only two layers two pin layers deep, I'm actually able to get one trace out there. I can't

**Dave Jones:** get two really cuz we're already down to 4 thou or 0.1 mm track width. But sometimes on some FPGAs, especially on the larger pin pitch ones, you can actually get two tracks out between one individual pin. Now, if this FPGA was

**Dave Jones:** any bigger, we would not be able to route out the extra tracks here. We'd be forced to use some vias here to drop through to our other layers. Bingo, we've instantly meant that we have to get 0.1 or 0.2 mm

**Dave Jones:** drill hole boards, much more expensive, pain in the ass. But anyway, I figured out a way to route or fan out this device just based on a single layer here. So if you'll notice each quadrant of the FPGA like this is basically a

**Dave Jones:** rotational mirror image of the one up here. Well, it's not quite, but it's close. Sort of this one matches that. This quadrant matches the diagonal quadrant over there and so on. And it really it is quite a nice symmetrical rotational design. I

**Dave Jones:** like it. Brings a bit of a tear to the eye, really. So, we've routed out these using 4 thou traces. Okay, let's switch to Imperial mode cuz I like to use Imperial, not metric mode for my traces. But, for whole sizes and board sizes and

**Dave Jones:** things like that, I use metric. Go figure. But, yeah, it's just the way the a lot of the industry works. The PCB industry does mix up their uh their millimeters and their thou's quite a lot. Um but, you have to generally

**Dave Jones:** juggle both when you're doing a PCB design like this. Anyway, um this means that we can um sort of start fanning out um these using larger traces. We might uh say go to a 6 thou trace or something

**Dave Jones:** like that when we um take that because you don't want to use a 4 thou trace all over your board. So, you might just fan it out with those small uh 4 thou traces or you could even uh say fan it out with

**Dave Jones:** say an 8 thou trace perhaps. You might be able to get away with that. But, just watch your clearances in there. Um if you don't have enough space, there we go. We might Yeah, that's probably going to be enough space in there. So,

**Dave Jones:** we could fan this out with an 8 with 8 mm traces. No problems at all. So, there you go. That is um basically uh fanning out a a FPGA, a 0.4 mm pitch BGA device. Really, if you can

**Dave Jones:** avoid using these type of packages and these devices, do it cuz it can be uh really expensive and a real pain in the butt. And likewise, uh we're trying to get our bypass caps here close to our uh

**Dave Jones:** close to our power pins in here. So, you drag it all the way over here and then you might have say a a via in here like this. Okay? Dropping it down to a um you know, a power trace on on a different layer.

**Dave Jones:** But, look, this is a 0.3 mm via, which is the which is the minimum size I would be comfortable with on on a basic board like this without paying a lot more. Some people would even say 0.4 mm is too

**Dave Jones:** small. Okay, but once I get in there, you can see that routing out these becomes a bit of a pain. And then I've got to move my cap in here and it just it gets really quite ugly really

**Dave Jones:** quickly, especially if you've got a lot of bypass caps on a design a lot of FPGA designs, especially some more advanced ones, will actually the bypass caps will be directly under the chip on the bottom layer the bottom side

**Dave Jones:** of the board and what's called a called a two-sided load components on both sides of the board. So, you can get a very low inductance path between your pad, like if your via's here like this, okay? I might swap component down to the

**Dave Jones:** bottom layer down there, okay? It's now flipped over to the bottom and I might sit that on the bottom like that, okay? So, I can actually get if this was a huge device, like a massive big, you know, 4-500 or 1,000 pin BGA device, I'd

**Dave Jones:** put that bypass cap on the bottom there and bingo, it's disappeared. You'll find that it's actually vanished onto the bottom side of the board right next to the via that allows me to get a low inductance path through to that bottom

**Dave Jones:** layer, but really this was a very basic implementation, a very like the lowest end FPGA you can get. And there's actually a lot of factors I didn't cover. You go check the data sheets. Don't be scared of these sorts of

**Dave Jones:** devices. Just be aware that there's lots of traps for young players, a lot of things which drive your design decisions for FPGA not only on the schematic and the component level, but on the PCB level as well. So, that was like one

**Dave Jones:** extreme example there of a ultra tiny 3 mm by 3 mm FPGA with not many IO, but it had a killer 0.4 mm pin pitch, and that really made the process technology for the PCB quite difficult. But, hey, we could

**Dave Jones:** actually fan all of that out on just the one layer. So, we could actually technically do a two-layer board there if you didn't want to do ground planes or whatnot. You could get away with it. Now, let's go to an a

**Dave Jones:** completely opposite example here, opposite in two ways. One, this is an pretty much extreme pin count FPGA. We've got 1,131 pin BGA, but the pin pitch, the ball pitch, is instead of 0.4 mm, it's 1 mm. So, you can practically drive a truck

**Dave Jones:** through a 1 mm pin pitch. So, let's have a look at this. This is a board I designed quite a long time ago. This is based on a Virtex 5. I'll give you a squeeze. Isn't that jazzy? Anyway,

**Dave Jones:** it's a whoa, Vir- Virtex 5 FPGA for those playing along at home, and that's the part number. The FFG the 1136 in there means it's 1,136 pins, and this is like an $800 BGA. It's not cheap at all. It's got SRAM. It's

**Dave Jones:** got flash. It's got controlled impedance differential traces to rocket IO. It's got 10 gigabit SATA connection on it and things like that. So, let's actually have a look. Now, this is actually a 10-layer PCB. Why? Because not only do

**Dave Jones:** you need that for the controlled the high-speed differential traces, you need ground planes in there to create your controlled Oh, well, you don't necessarily need those, but they helped a lot for the controlled impedance traces, but mainly because

**Dave Jones:** the number of layers is dictated by how many pins you've got on your FPGA here. And with 1,136 pins, we basically needed 10 layers to fan this thing out and do all the ground planes and all the different power planes and stuff that we

**Dave Jones:** wanted. So, let's actually take a look on the bottom here. Here we go. And you can see that we've got a smattering of bypass caps around here. This isn't a very good example of a nice symmetrical design uh bypass arrangement. I can show

**Dave Jones:** better examples of that, but you know, I I didn't really want need or want to uh show that here. But you can see that all the vias are uh tented, but as you'll see, they didn't really uh need to be in

**Dave Jones:** this particular case. So, uh what have we got? Yeah, and you can whoop. Whoa. Not sure what's going on there. Okay. Uh they weren't I think something they were supposed to be uh surface mount on the top. I'm not

**Dave Jones:** No, it's something's gone horribly wrong with the model. Don't look at that. Um don't look at the uh man behind the curtain. So, let's actually go into uh 2D mode and take a squeeze at this board. Zoom all. Here we go. So, now we'll be

**Dave Jones:** able to see the different layers. So, I'll go into single layer mode, basically, and we can uh go through the different layers here. So, you can see this is the top layer. So, you can see how um I've actually fanned

**Dave Jones:** out the uh You can see how here I've actually chosen the outer row of pins here. Um you are limited, it depends on the the internal structure of the uh chip. But I for the high-speed rocket IO uh stuff,

**Dave Jones:** these are all the uh high-speed differential pairs coming out. You can see that they're uh length matched and things like that. Um not only matched length from for each pair because I've uh snaked it like that, that matches the

**Dave Jones:** uh length in there, but also these little wiggles in there. Wiggle wiggle wiggle, yeah. That matches the length of this one of this trace to its opposite pair there. And that's important not only to match between the different pairs, but also

**Dave Jones:** in between the two pairs as well. So, anyway, that's just a little aside. So, that's on the top layer. And as you can see here, I've basically fanned out every single Here are the BGA pads, okay? And I've basically fanned

**Dave Jones:** those out to a very large via. Look at this. This is Let's go into metric mode. 0.3 mm, 0.6 mm 0.3 mm hole with a 0.6 mm pad. And I was able to do that because uh because I can. Um because this is a

**Dave Jones:** very wide 1 mm between these pins these BGA balls here, they're 1 mm each. For those playing along at home, that pad size is 0.5 mm. And you might take that from the IPC standard or in this case

**Dave Jones:** the Xilinx recommended footprints or whatever it is you want to you choose to use for this thing. Now, you can see that I've basically fanned out every single pad here to the differential except for some kind of tiny unused ones

**Dave Jones:** here. I guess I just like I went through and did a tidy up pass at the end and just went, "Well, that pin's unused. I won't bother even fanning that one out." But you could just in case um

**Dave Jones:** you needed to do that. But you can see that I didn't don't necessarily need to tent the vias in this particular case because I'm it's a 1 mm ball-to-ball distance and I can fit a reasonable size via in there. 0.3

**Dave Jones:** mm with 0.6 mm pad. Awesome. We could And this is on a huge 1,100 pin BGA. We couldn't do that before on that little tiny piece ant 3 mm by 3 mm FPGA because the ball pitch was far too small. So,

**Dave Jones:** that determined our manufacturing geometry. In this case, you know, my my traces this is just like really basic like 5 thou, right? 5 mil trace and space. I think there's clearance on this is like 5 mil. So, it's actually this board, even though it

**Dave Jones:** uses a much bigger, much more expensive, much vastly higher pin count FPGA, its manufacturing tolerances are much wider because dictated by the pin pitch. So, if we go back here to the 3D view and we disable all the 3D packages, you can see

**Dave Jones:** that all my my top vias in there, they're all tinned. So, all we've got is the BGA ball pad with a tiny bit of solder mask expansion there on the pad. But, like I said, like there's large tolerances there and then

**Dave Jones:** maybe I didn't have to actually tin that via in there. But, as a matter of course, you would actually tin even though their tolerances are quite large here, you would tin all the vias on the top there. But, on the

**Dave Jones:** bottom, I did, but you don't have to. In fact, it's handy not to. I'm not sure why it's done in this particular case. I can't remember, but it's handy to leave them untinned on the bottom because then you can solder a

**Dave Jones:** little mod wires onto them, use them as test points and access things like that. So, that's just like because you don't have to worry about solder paste on the bottom here except with you know, nearby pads and stuff like that, but it's not as big

**Dave Jones:** a deal as it is under the FPGA chip itself. Okay, for those who want to see all the different layers. So, that's the top layer. You can see that I'm mostly fanning out these ones on the side. Now,

**Dave Jones:** I could with the uh pitch here, ball pitch, I could have actually got went down to fourth hour fourth hour and I could have routed out two traces between pads. And I've got other boards where I've done that, no problems. Might have

**Dave Jones:** even been three in one case in an extreme example um somewhere. But basically uh two is, you know, pushing it. But you can with a large 1 mm pin pitch or a uh say a 1.27 uh mm pitch,

**Dave Jones:** for example, on modern some modern large parts do that to allow you to fan out on cheaper double and sided and four layer boards. But really with this particular board, cost really wasn't, you know, a huge uh issue whether or not it was six

**Dave Jones:** layers or 10 layers. Didn't really matter a huge amount. If it was really for high volume production, yeah, I'd probably be optimizing it trying to get trying to fan out uh two traces between uh pads. So then, you know, I might be

**Dave Jones:** able to get with a lower count um uh layer layer count board. So anyway, let let's have a look. Let's go down the layers. And what I've done here is I've just uh removed all the ground planes so

**Dave Jones:** we can go through and we see the uh fan out a bit nicer there. So there's the different uh signal layers. So I've got uh 1 2 3 4 5 6 seven different uh signal layers there. And the other three are devoted to uh

**Dave Jones:** power and ground planes. And you'll notice that one here, this is not actually ground. This is actually how I get in uh this is a 2.5 V uh net. This is the uh FPGA core. So I actually uh

**Dave Jones:** bring that in from over here. Snake that in. But you can see how like, you know, not complicated. You know, this is 1,000 I'm not sure if I've used all um but I've probably used like 8 or 900 pins or something like

**Dave Jones:** that. And there's not that, you know, it's not that complicated. It gets more complicated when you're forced to do it on a cheaper number a cheaper board with a smaller number of layers. But that is like quite neat and tidy and of course the pin

**Dave Jones:** swapping really made this essential. You can see all the you know, all the pin swaps around here. So it was just you know, very neat and tidy. When you got the luxury as a PCB designer luxury of a

**Dave Jones:** 10 layers for a board like this you just go ah no sweat. You know, but when they got you got to do it on six layers. We need to shave it you know, another couple of bucks off each board then

**Dave Jones:** you're you know, it it gets much more harder much messier. It's much nicer like this cuz you can get grounds between all your different layers. You get like your signal integrity is much better. Your your ground impedances are much lower and

**Dave Jones:** everything's just much ground inductances and everything are much lower and it's just much nicer like that. And you can um have you know, separate differential uh pairs within separate ground planes and stuff like that. So this is not a particularly complicated board uh

**Dave Jones:** at all. But I just wanted to show you a large pin count BGA with a luxurious 1 mm pin pitch. Beautiful. The good thing about having the ground plane is that they're super low impedance. And for high speed FPGAs like this that need

**Dave Jones:** lots of bypassing it's all about the loop inductance loop area. I've done separate videos on that I'm sure. Um and ground planes are pretty much essential on something like this. So even if you could fan it out on a double-sided board

**Dave Jones:** you might go pretty much be forced to go to a four-layer board so that you could at least have a ground plane on there and then have the bypass gaps caps going to that. So let's go through. This is layer

**Dave Jones:** three. This one actually has a combination of some signal traces coming out. You can see the SATA ones the SATA connections once again with the differential pair length and also pair matching as well. But just thought I'd show you more ground

**Dave Jones:** plane and then we've got signal and then you just flood fill with ground plane. That was basically what I was doing there. So I haven't aggressively tried to fan out this out on the minimum number of layers. It was you know pretty

**Dave Jones:** generous being able to use a 10 layer board here, you know. I would you'd at least target an eight layer board in this particular example. And as for the bypass caps on the bottom, as I said this is not very

**Dave Jones:** symmetrical but there's like large ones on like the 1 volt core here. There's a 2.5 volt core voltage as well and there's probably some IO. Yep, some IO over here at 3.3 volts. So just a smattering usually in most FPGA pin outs, if you go

**Dave Jones:** and look at the pin outs for them, generally all of the pound ground and power are clumped around the middle and that's why if you look at the bottom of any any production board with an FPGA, you'll typically find if they're double-sided

**Dave Jones:** load which you know your big pin count high speed ones are, then you'll find all the bypass caps clumped around the middle of the chip instead of the outside. They leave the outside for the IO so that you can fan them out

**Dave Jones:** easier cuz if you got all your IO in the middle and all your ground on the outside then fanning them out on your layers can be a real pain in the butt. So they thought about that when they

**Dave Jones:** actually design a layout for the silicon and have most of the ground and power pins in the middle. And if we go to the top, we might be able to see that. Look, most of them are ground pins. See, 1

**Dave Jones:** volt ground ground. There's a couple of ones in here that that are nets but like a good lot of them look a whole you know whole big inner quadrant of them are ground and power cores. So that's great and or they just

**Dave Jones:** leave all the IO to the outside. You know, there's a few other like 3.3 V. Oh, no, no, that's a net. Is it? Anyway, and most of the outside ones are going to be um your IO. So, there you go.

**Dave Jones:** That's a look at a 1,136 pin BGA. You'll notice these things over here, these traces over here. Look at Look at these these little joiners. This is how you do pin swapping in Altium Designer. Uh maybe I should do a video

**Dave Jones:** on that cuz it's kind of cool. Because if you have a look at the schematic, let's have a look. Right, here's all the IO banks. Right? This is all the IO banks for the FPGA. And there's just an

**Dave Jones:** absolute like there's a ton of these things. And what you do is you go in there uh Yeah, I I won't do it now, but you go in there and you basically fan out the FPGA. Altium has an automated fan out

**Dave Jones:** tool, so it allows you to fan it out. I don't Sometimes I use that, sometimes I didn't and I did it manually. Can't remember if I did it use the automatic one here or not. But then you route out

**Dave Jones:** the traces right around to the edge like this, and then you basically route in Right? So, you don't Well, you you put all your signal names on here, right? But then you fan them out to here and you leave a gap

**Dave Jones:** and then you bring in you you route in all your other memory chips and everything else. You can note how, you know, nothing like the like this flash chip, for example, doesn't go to the other side of the FPGA. It just I just

**Dave Jones:** routed them into here like this, right? And you know, it just nice routing on there. And then what you do is you run the FPGA pin swapping tool and it will go in there and reorganize and you can

**Dave Jones:** set banks to keep them within banks. That's important. Um and I won't explain why. And two and it go it goes through and swaps all those nets to match up. It's really like magic. Um so, hands up if you want to see a separate video on

**Dave Jones:** that, but it's very Altium Designer specific. It's not, you know, a generic thing for our PCB layout tools. Actually, I'll just show you that automated fan out tool in Altium Designer. This is specific. So, I've actually dragged the chip out of there

**Dave Jones:** and I've done a test one down here. It does actually work. So, what you do is you go in and set up all your rules first. You set up your via uh size, your hole size, your pad size, you set up

**Dave Jones:** your spacing, your clearances, and all that sort of stuff designed on your manufacturing rules based on the manufacturer that you're going to target. And we can just go in here to route, fan out, and individual component. And once again, it gives us

**Dave Jones:** some options. Fan out pads without any nets. Um and means if you have no nets assigned to that particular pad, it'll fan it out anyway, as I said before about the unused pad. If it's unused, you might want to fan them out cuz you

**Dave Jones:** might want to be able to attach to stuff later. Highly recommended. If you've got the space, I'd just leave that ticked. And then you can do stuff like blind vias and stuff like that that are buried down in the layers. And we won't

**Dave Jones:** worry about any of that. Let's just go okay and watch the magic. Come on, magic computer. Magic out. Ta-da! There you go. We've fanned out an 1,136 pin BGA instantly, just like that. It's done it in quadrants, as you can see like that.

**Dave Jones:** And it it just knows that's the smartest way to do that particular component. Altium Designer specifically knows about, you know, fan out BGAs, and it's fanned out unused pins that don't have any nets and stuff like that. So, there's lots of

**Dave Jones:** unused There's quite a few unused ones around here, and it's fanned them out anyway. There you go. Has it has it tinted those?

**Dave Jones:** No, look at that. Horrid. I guess we don't have to have any solder mask. Look at that. That's hilarious. Look, you can see all the different layers. You can see all the different layers. That is great. That's one one of the cool things. You

**Dave Jones:** can actually go inside the You can go inside the board, by the way, with Altium Designer 3D view. Look at that. You can go inside. That's just great. Love it. Love it. It's actually it's not just like a gimmick. It's actually very

**Dave Jones:** valuable. So, you can see the larger space in here between you see the core that we've actually set. It's got a larger prepreg prepreg between the boards and the between the layers. Sorry, but that's yeah, that's very cool. Sorry, I don't have my space

**Dave Jones:** navigator. I'm That's just neat. I always get a kick around playing with that. It's great. It never gets old. But, anyway, there you go. That's a look at fanning out FPGAs. I just wanted to show you that extracted from an older video that I had

**Dave Jones:** because I thought it was kind of interesting. So, anyway, if you liked that, please give it a big thumbs up cuz that always helps a lot. And if you want more PCB type stuff like this, yes, definitely give it a thumbs up. Leave it

**Dave Jones:** in the comments and I'll know to do more PCB type stuff. Hope you liked it. Catch you next time.
