---
video_id: MCDsge-3z0U
title: EEVblog #706 - Joystick Porn
url: https://www.youtube.com/watch?v=MCDsge-3z0U
source: whisper-large-v3-q5_0
timestamps: {"0": 1, "1": 16, "2": 36, "3": 56, "4": 71, "5": 96, "6": 106, "7": 121, "8": 136, "9": 156, "10": 171, "11": 196, "12": 216, "13": 236, "14": 251, "15": 276, "16": 291, "17": 306, "18": 326, "19": 341, "20": 366, "21": 381, "22": 401, "23": 416, "24": 431, "25": 451, "26": 471, "27": 491, "28": 511, "29": 531, "30": 551, "31": 566, "32": 581, "33": 596, "34": 616, "35": 631, "36": 656, "37": 676, "38": 686, "39": 706, "40": 721, "41": 741, "42": 756, "43": 771, "44": 796, "45": 811, "46": 831, "47": 846, "48": 861, "49": 881, "50": 896, "51": 911, "52": 931, "53": 946, "54": 966, "55": 986, "56": 1001, "57": 1021}
---

**Dave Jones:** Hi, let's take a look inside one of these professional, industrial-quality joysticks, as seen in a previous Mailbag episode and sent in by Mark Sadowski from Control Devices here in Sydney. So thank you very much, Mark. Let's take a look at what makes one of these puppies tick.

**Dave Jones:** So Mark's included two joysticks here. One is the fully complete one, complete with interface and presumably has all the circuitry fully functional inside the thing, and the other one is essentially the same thing but all stripped down so that we can take a look at the mechanicals.

**Dave Jones:** And he says that this one here is most likely used in the garbage trucks which come around and you know, lift up your bins and haul them into the back. That'd be one of the industrial applications for one of these puppies. Of course, you know, the buttons would do various things and they'd label them

**Dave Jones:** for a specific purpose and they would operate the, operate, you know, up, down, dump, rubbish, all that sort of stuff. Or they could be used in flight simulators or anything that requires a real top-quality joystick. Because these things, I mean, there's a lot of engineering which goes into that.

**Dave Jones:** And it's hard to really give you an insight as to how good this thing feels, but a real top-quality like you know, a military-style grade joystick for example, won't only just go like that in any direction. It'll have more movement in the four axis, like easier movement in the four axes

**Dave Jones:** like that than it does, you can actually push these like at any angle, but there's more force required to do that. So you know, if you're flying a plane or something you, you know, if you want it to go forward, you just push forward.

**Dave Jones:** You don't want it to go slightly off to an angle, you know, like that. So you want the joy, I'm not sure of the correct term for that, I'm sure people will scream at me, the joystick aficionados will scream at me, I know the term for that.

**Dave Jones:** Anyway, it is, yeah, there's less resistance, so if you push it forward, it's naturally going to go forward. You need actually a fair bit of force to sort of move it over to one side and get that different angle. So yeah, superbly engineered they really are.

**Dave Jones:** Cost a fortune. And these buttons, Mark was telling me that they used to be designed in the US, they used one from a US company, but they failed. You know, just too much use, too many button presses, they weren't reliable enough. So they designed these ones themselves

**Dave Jones:** here in Sydney at their factory, and they manufacture them here. They're a Hall Effect switch, so all it is is basically putting, there's no actual contact in there, so basically all they're doing is putting a magnet beside a Hall Effect sensor. And these have up to 20 million operations.

**Dave Jones:** And yes, they have actually designed some test jigs to actually prove that, and actually test them out, push them 20 million times, and actually test the reliability of these things. Now this mechanism here, however, does use standard, well, they're going to be super high quality, but you can see the wipe contacts in there, and as

**Dave Jones:** I move it, you can see that arm swing across. So just like, say, your range switch in your multimeter, they've got the pads, you can probably see, through the PCB there onto the other side, those dual wipe contacts of course, dual wipe either side, so they can determine how, when these

**Dave Jones:** things have been moved. So there's a lot of mechanical porn which goes into ensuring, I mean we can, you know, we can tear this whole thing down and see inside, because it's, there's a lot of engineering porn which goes into that. As I said, to give the extra force required to go

**Dave Jones:** at the various angles. Ah, very nice. And we have some unpopulated circuitry in here. By the way, all the mechanical stuff, this is all designed and made in the UK, but all the rest of it, all of the PCBs and that circuitry and everything else, they're all done here in Sydney.

**Dave Jones:** So presumably all this, like there'd be a micro on there, and it gives presumably a proportional output, or you know, some sort of decoded output, and or serial protocol custom interface for whatever device you need. So yeah, that's probably completely customizable to the customer's

**Dave Jones:** requirements, because these things basically aren't off the shelf pretty much. They're sort of, you know, more of your design to the customer spec kind of thing. And aha, the PCB gives it away, 4 to 20 milliamp times 2, that's a current loop output,

**Dave Jones:** so we'd get a proportional current output based on the movement of the joystick. And they reason they use a current output instead of a voltage output because industrial applications typically got big long wiring harnesses and things like that, you don't want any interference.

**Dave Jones:** So a nice 4 to 20 milliamp industry standard current loop output, proportional output, is exactly what you want for that sort of thing. So yeah, you can eliminate any noise interference because it's relatively high current. It's not a high impedance voltage input. So it's a

**Dave Jones:** huge difference there, so no surprise that an industrial unit has 4 to 20 milliamp current loop outputs on it. But yeah, I'm sure they could design it to, you know, they'd custom make this board to whatever requirements you wanted. And if you take that grommet off, aha,

**Dave Jones:** we can really see how they achieve this, you know, less force required in one axis like that. You can see that they've got little milled cutouts in there, so obviously in this, with the circular disk going in back and forth and left and right is much less force required than, as I

**Dave Jones:** said, going opposite like that, because it's a higher up ridge like that, and of course this being around in here obviously just slides in that slot there real easy, so it stays on target unless you really have to put a bit of force to move it over.

**Dave Jones:** That is terrific stuff. And of course the force is determined by your spring on there, so if the customer said, oh look, that's a bit, that joystick's a bit stiff, I don't like a stiff joystick, that's a bit dodgy, give me one that's a bit soft, then they can just

**Dave Jones:** change the spring in there and give the customer whatever they want. So all this physical base inside here is manufactured in the UK, as I said, by Penny and Gilley's Control Limited, made in the old dart, there you go. And yeah, they're all

**Dave Jones:** individually serial numbered, because you know, these things cost a lot of money and you really want to trace them. But as I said, the rest of the electronics and that stuff inside is done by control devices here in Sydney. Now if we take that board

**Dave Jones:** assembly out here, you can see the dual-wipe contacts under there, so there's two separate circuits, and ta-da! And check out the backside of the board here. Yes, it is a proportional output, not just like a four-position output or something like that. Dead giveaway is this carbon

**Dave Jones:** trace over here like this, so one of those dual-wipe contacts there, these two pads, this one down here, here and here, they make contact, so one makes contact of course with that main pad which goes all the way across there, and the other goes onto this

**Dave Jones:** variable resistance. Well, it's a continuous resistance right across there, it's going to have a controlled resistance right across, but depending on the position, then you can actually tap it off just like a regular pot. So there's your three terminals, here's your one terminal going across there, and there's either side of your pot

**Dave Jones:** like that, and they might even be tapping off from the center as well there. And let's measure the end-to-end resistance of that. There we go, about 3.6k or thereabouts, and that'll be fairly linear across that arc like that. It's fairly evenly distributed resistance across there, it's based on the graphite or

**Dave Jones:** whatever material it is, and then the controlled thickness as well. There'd be a lot of art in actually manufacturing those for the joystick, so I don't know who's actually manufacturing those, but it'd be really top-quality stuff. And we've got another one across here which is a different axis,

**Dave Jones:** but this doesn't look like it's used at all on this particular joystick with the contacts anyway, that one's around about 500 ohms apiece. It looks like that we've got, as I said, we've got two contacts there and two contacts there, so maybe they had something else up there for these top

**Dave Jones:** contacts, but these aren't used in this particular model. So you've got one wiper across there, and there as I said, that'll be a regular potentiometer going back and forth with your center tap in there, and then the other one goes between here, and it's just a multi-position, it

**Dave Jones:** detects whether or not it's the center and goes over there. So it'll be dependent, whether or not you use that depends on your system requirements. And of course the carbon on there is going to be some sort of, you know, graphite-based material. I'm not sure what it is precisely,

**Dave Jones:** but it's going to want to be very special for this, you know, really high-end industrial military-type application to get. You know, if you've got the wiper continuously going across that, eh, it's not like a regular, you know, 10-cent pot you can buy from your local Tricky Dick store.

**Dave Jones:** It's going to be really high-quality carbon on there, bet your bottom dollar. And of course they wouldn't just get that from any PCB manufacturer either, they would have had to carefully selected and qualified that particular PCB manufacturer to do that particular process that they wanted, and

**Dave Jones:** it probably cost a fortune. And of course, needless to say, the gold plating on there wouldn't be a standard one that you're going to get on your $5 board from your one-hung low PCB manufacturer. That's going to be really top-quality, super-hard, super-thick gold on there.

**Dave Jones:** Bet your bottom dollar again. And by the way, I know all about selecting the right type of button here. I used to work at Australian Defence Industries and working on military stuff, and we were doing simulators for the Navy. And we had to, you know, we would spend like 6 months

**Dave Jones:** sourcing, selecting, and testing and qualifying the right switch for the damn thing. I mean, that's why these military bloody projects are so expensive. Like, the switch would cost, yeah, $500 a bloody switch, but we'd spend how many, you know, $100,000 just selecting the damn thing, just in

**Dave Jones:** labour and red tape. And look at all these cast parts that they have to make. I mean, jeez. You know, these things would cost a fortune. And we're getting more down into the guts of, jeez, you could use that in some sort of sci-fi movie, couldn't you?

**Dave Jones:** That's fantastic. I love that. Anyway, we're getting down into it. And there's the money shot for you mechanical grease monkeys. Look at that. Fantastic. So yeah, I mean, that is just you know, a great work of mechanical engineering, you know, for such a simple function

**Dave Jones:** for a joystick. But, you know, to perfect it and get it right requires you know, a lot of design effort and a lot of, you know, precision machining and things like that to, you know, really separate the real top quality ones from just your junk ones for bloody gamer kiddies.

**Dave Jones:** And you would think a part like that would be symmetrical, but it's not. There's a little pin in there which is designed to mate up with the hole down in there, so it goes in one orientation only. But it looks pretty darn symmetrical, but

**Dave Jones:** it ain't. And likewise for that part too, you think it's symmetrical, looks symmetrical, but nah, it's got a little key in there which mates up with that so you can't mount it any other orientation. Bet your arse we're going to avoid that warranty.

**Dave Jones:** Yeah. And here is inside, presumably, a fully assembled one, or a fully assembled customized, I don't know, it could be a prototype or anything like that, I don't know. It wasn't certainly brand new out of their stock, they just gave me whatever they had hanging around.

**Dave Jones:** So yeah, that looks like possibly just jewellery rigged, maybe for test purposes, something like that. And fortunately it looks like the board is actually riveted on there. Check it out, it's not actually screwed in, completely riveted on. So yeah, I'm not sure there's anything of value on the bottom of the board in there.

**Dave Jones:** And by the looks of these connectors on the side, yeah, I'd say it's some sort of test unit. So yeah, nothing interesting on there. Let's take a squeeze at these buttons if we can. To get at those buttons, it looks like we can remove the silicon

**Dave Jones:** in here, or get through there somehow and get the screws off and access those. And we've popped that out, but unfortunately, wah, it's potted. So we can't get to see the hall effect sensor in there, but as I said, it's just a hall effect sensor, probably on a little board with a push button

**Dave Jones:** and a spring which then pushes a magnet in front of the hall effect sensor. And there's going to be a little board on there, it's got a PNP output. And Mark says this is rated for 20 million operations. Datasheet says 10 million, but yeah,

**Dave Jones:** they probably get a lot more than that, probably very conservatively rated. So yeah, they're manufactured by Control Devices here in Sydney. They're their own hall effect sensor because mechanical wipe contacts, you know, to get 10 or 20 million operations out of those, it's a bit dodgy.

**Dave Jones:** So yeah, so hall effect with no metal-to-metal contact, all electronic effectively, is the best way to get that reliability. Then you've only got to pretty much rely on the spring. And that's pretty much it. So as long as you can get the spring to do those 10 or 20 million operations,

**Dave Jones:** then Bob's your uncle. And they're all ESD protected as well, as you'd expect in an industrial application like this. And just a small thing, like putting heat shrink over the wiring which goes through the cavity there, just so it doesn't rub against the inside.

**Dave Jones:** I know there's no movement on here once you've physically installed it, but it just shows attention to detail, I really like it. And of course you've got rubber o-ring seals as well because, well, you can't have the operator, you know, spilling their coffee all over these buttons

**Dave Jones:** and, well, accidentally having that drone shoot somebody. No, you want to do it on purpose. If we have a brief look at the data sheet here for the Penny & Gillies JC6000 multi-axis joystick controller, designed for demanding operator control applications in off-highway vehicles and other man-machine interfaces

**Dave Jones:** where reliability, blah blah blah, is super important. So you can get hall effect or potentiomic sensing, which we've got in here, we've got the potentiometers in there as we saw. And you can get single or dual axis control, high strength lever with superb proportional control.

**Dave Jones:** That's probably the word I was looking for, proportional axis kind of control. And they're IP66. And the hall effect ones actually supplied by them, but they've got up to 15 million operations. But as I said, the hall effect switches in these ones, the joystick switches

**Dave Jones:** on the top, they're actually manufactured locally here in Sydney, not by this company. But the potentiometer ones, they've got more than 5 million operations. So fantastic reliability on that, that's just awesome. And you can get dual output ones as well for like failure detection, safety critical applications, all that sort of jazz.

**Dave Jones:** And of course, a lot of design, whatever the hell you want. So there you have it, that's a brief look inside one of these professional industrial type joysticks. And it's, you know, there's quite a lot of really nice engineering which goes into these things.

**Dave Jones:** And well, if you have to ask the price, you probably can't afford it, you gamer kiddies. So these are designed for real industrial high reliability applications. And pretty much sort of, you know, custom design for your particular needs. So thank you very much to Mark from Control Devices here in Sydney for letting us

**Dave Jones:** have a look inside these beautiful joysticks. And oh man, just love a good stiff joystick, that's just fantastic. Catch you next time.
