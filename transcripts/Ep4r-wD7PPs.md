---
video_id: Ep4r-wD7PPs
title: KiCAD PCB Design
url: https://www.youtube.com/watch?v=Ep4r-wD7PPs
source: youtube-asr
---

**Dave Jones:** Anyway, I thought that I would finish this Gigatron thing. Let's go. Shift mouse wheel goes up and down. Control mouse wheel goes left and right. You can't right click and pan. Don't like that. How do you pan? No,

**Dave Jones:** it's not alt. It's not It's It's not right click. Oh, you hold down the middle mouse. That's right. I I hate that. I'm not a fan of clicking the middle scroll wheel. Why can't I hold down the the right button and then

**Dave Jones:** pan around? That's how like half the other programs in the world work. Click and hold middle button. I I I don't like it. It's It's too much force required on the button. It's like It's like not a natural thing

**Dave Jones:** to click the middle wheel. Like requires a lot of force, you know. It's Maybe it's the mouse I've got. It's a Logitech thingamabob. Anyway, hey, check this out. I got another camera.

**Dave Jones:** Oh, look. I'm a tag bag. Which tag bag. Kai, where was I? Yeah, cuz I never actually finished this. Anyway, this is where I last left off. For those playing around on EV blog 2 before, couple of months back,

**Dave Jones:** when I did this. Did someone just say why KiCad is not Altium? Because the original source file is in KiCad. That's why. No, I'm not looking at alternatives. It just For those who don't know, this is the Gigatron TTL computer, which you you've

**Dave Jones:** seen in a couple of videos on my Bloody hell. No, I don't I don't like I don't like how they've done the scroll wheel on this. Sorry. Just don't like it. This is the Gigatron TTL computer. I want to do a four-layer version of this

**Dave Jones:** board. And the the original designers of the Gigatron were kind enough to send me a four layer kit send me the KiCad files. And obviously, I'm not going to convert them to Altium just to do that. So, I'm

**Dave Jones:** using KiCad. So, I've installed the new version five 5.0000000. Yeah, there you go. And I'm using PCB new for those playing along at home. Where I got up to last time is I had removed I removed the top and bottom

**Dave Jones:** layer, that's right. There we go. Is it So, that's that's the ground. Genius, I tell you. Cuz now you can see the menu bar on the left. I'm not sure if you can actually Can you Oh, yeah. Yeah, look. Look, you can

**Dave Jones:** change change the docking for this. Wow, okay. Uh-oh. How How do I redock? I don't Hold down control, shift, alt. It's not automatically snapping back. I've undocked it that permanently. I'm not mildly bummed. I've I woke up this morning and

**Dave Jones:** there are no field zones because these are um It's a ground plane. And uh there's no VCC, ground. VCC's not a thing. Where Where's my VCC? I've got a ground plane, but I don't have a VCC. Drag title bar

**Dave Jones:** to side you want just below the buttons. Oh, yeah. There it There it goes. Aha, thanks. Yep, I didn't notice the shadow in there. Cool bananas. Hey, I can't make that any smaller. Why can't I make that smaller? Look at

**Dave Jones:** all this wasted space down here. Look at all this wasted space. I'm going to drag Look, I can drag it bigger, but I can't drag it smaller. Got wasted space there. Look at that. Poor you Poor GUI design. So, did I

**Dave Jones:** create that ground plane last time? Did I manually When you create a ground plane, do you have to put Do you have to actually manually put in the pour it in. KiCad doesn't have planes, only filled zones. It's tedious.

**Dave Jones:** Thanks, Joshua. Ground plane must be filled manually. Okay, is that the same? I assume that's the same for VCC. Must be. It has to be. Right, if it is right. Okay, so I filled that manually. Okay. So, front. I I don't like how they use F for

**Dave Jones:** front. I I just like that's by default. It may may is that like a European thing or something? I don't know cuz they don't the you know, isn't it mostly written by Europeans or somebody? But it's like yeah, if I assume F means front. Um

**Dave Jones:** B means bottom. F means front. I I I don't like that. It's always top bottom. It's always top bottom. I I don't It's like if you That's what that That's what that layer is saying to me. Like it just FCU.

**Dave Jones:** It's funny. Sorry. It's my childish sense of humor. All right, so there's there's bottom layer. And there's our top our front layer. Screw that. Top top layer. And the ground I've already put in a groundy do dad. All right, so

**Dave Jones:** that means that let's actually just go in. Have a look. Yeah, okay, it's already done the thermal reliefs. Yep. Okay, it's already done the thermal reliefs to the ground plane. So, uh now what it's missing now of course, you can see

**Dave Jones:** all these white lines, these are the missing nets. So, um yeah, all I've got to do is uh uh pour my VCC, I think. It should be right and then we should be good to go. How do I pour a um

**Dave Jones:** pour a fill? Is it a polygon? I've got a cheat sheet here. My cheat sheet does not have B for report here. Maybe I've got an old cheat sheet or something. Place zone, is it? Joshua seems to be

**Dave Jones:** the man. Create fill, select net, draw polygon, place zone. Oh yeah, zone looks like a fill. Okay, so they call it a zone. Okay. Groovy. So, I'm going to have some pull back on there. All right. You have to have some pull

**Dave Jones:** back. Tip for young players, never take ground planes to the edge of the board or outside, even if the tool automatically has a thing to trim. Um I don't know if KiCad has the ability to pull back. Choose our layer.

**Dave Jones:** But even if it does, I would recommend not relying on it. Okay. Uh thermal reliefs? Yep. Solid. Uh through-hole thermal. I wonder what the difference maybe we can uh play with that later later. What's I assume THT thermal is

**Dave Jones:** through-hole thermal. What's the What's going to be the difference between the through-hole thermal and the thermal relief, I wonder. I think you're wrong, Gabriel. It's not polygon. It's a zone. What is a pull back? That's a good question,

**Dave Jones:** digital hands. Okay. I Yeah, I didn't finish finish my thought there, did I? Fundamentals of PCB design on my channel. Uh there's lots of Yeah, yeah, I've done walkthroughs. I've done like like an hour like I've done like

**Dave Jones:** hour-long walkthroughs of designing a PCB with lots of hints and tips along the way. Um sorry, I don't have know the name of it to hand. It was one of my power supply design series videos. It's It's labeled power supply

**Dave Jones:** design PCB layout or something. Let's go out of here for a second. Okay. You've When you've got a PCB, right? You've You've got the edge of your board here. The edge is defined on this particular layer. I don't know which layer they use

**Dave Jones:** in KiCad. Fabrication layer, is it? No. No, it's not the fab layer. Um bottom fat no and mask pad adhesive. Edge cuts. There we go. They got an edge cuts layer. Right, so your board is defined by It It doesn't have to be on the edge

**Dave Jones:** cuts layer. It can be on the copper layer. It can be anywhere as long as the PCB uh manufacturer knows like they they they know when they see lines like this on It doesn't matter what layer it is.

**Dave Jones:** They They're going to know that you're implying that that's the edge of your board. Now, the edge of your board, right? When they manufacture your PCB, right? They use um either routing or big guillotines or saws to chop your board

**Dave Jones:** up, right? And when they chop your board up, um especially if it's a multi-layer board like we're designing here. We're designing a four-layer board. So, that means we've got the top copper, the bottom copper, and ground and VCC in

**Dave Jones:** here. Okay? So, what we're doing at the moment is we're actually creating these two inner layers, ground and VCC, and they're just one big solid copper plane in this particular case. Doesn't have to be. And they will uh by default

**Dave Jones:** in a lot of packages In In In this case, KiCad does not have planes as such. They're just layers with polygon fills or zones in this particular case. So, uh But anyway, right? If If you draw them all the way to the

**Dave Jones:** edge like I can't I My My snap doesn't go in there. It doesn't snap to object. Anyway, if you take your plane copper plane all the way to the edge of the board where the board gets routed or

**Dave Jones:** sawed or cut off, then if you've got the copper in the inner layers, when they do that, when they slough or slice or route through it, it can cause little burrs in the copper. And then the copper, if it's right on

**Dave Jones:** the edge of the board, can Yeah, the copper is like right on the edge of the board. Like that. It's right on the edge and they route or they slice your board, it can actually short those two layers

**Dave Jones:** together. Right? Yeah, in case you can get little birds and they can short together. And obviously, if you short your power plane and your ground plane together, it's going to ruin your day. So, you don't want that. So, what

**Dave Jones:** pullback is called, right? Is I I do not want to define the copper going right to the edge of the board. I want to pull it back a distance from the edge. And a package like Altium will have, you know, it knows what planes are

**Dave Jones:** and it knows what pullback is and all that sort of stuff. So, you can define that. KiCad, I believe, doesn't What I'm told here, KiCad doesn't have that ability. So, you got to do it manually. So, that's why I'm going to select,

**Dave Jones:** rather than go right to the edge, I'm going to leave a gap. Pullback around the edge of the board. That's what it is. So, do do do Thermal relief. I don't think I ever asked. Yes, I'm sick. Sorry. That's

**Dave Jones:** why my voice is crap. I just woke up this morning and now it's fine. Last night, woke up this morning and probably picked up something from the germ factory yesterday, preschool for those who don't have kids. It's the germ factory.

**Dave Jones:** We're going to place a zone and we're going to pull back from the edge. We're going to select the layer we want VCC, which is our power, and then we select the net that we want. They're They're not in alphabetical order. Why aren't

**Dave Jones:** they in alphabetical order? Hidden net filter, you know, we can guess we can just use the net filter. Apply filter. All right. Alphabetical. Ah, it must must be called something else. Okay? It's It's probably called plus five or something. Ah, that's

**Dave Jones:** right. That's right. They um Yeah. Yeah, the designers of the Gigatron, where is it? Not very good at this. Gigatron schematic, create Yeah, I think cuz I'm using version five. We're not found transistor lit. Hm. Well, lots of libraries weren't found.

**Dave Jones:** That's not good. Remap symbols. Project rescue helper. I I think cuz I've got an old that was done in an old version or something, so I Whoa. This is heavy. Okay. So, it's mapped. Backing up rescue. Oh god.

**Dave Jones:** Oh. Oh. It's done It's It's remapping, re-saving, backing up files. Oh god. Okay. Um, I don't like this. Don't like the sound of that. Doesn't instill a lot of confidence in me. Anyway, the designers of the Gigatron, they, uh, hierarchical sheet

**Dave Jones:** project There we go. Haha. Well, I'm now KiCad expert. Um, they looks like they've got hidden power pins on there, do they? They must have They They don't have power pins on their, um, on the chips. They don't have power pins

**Dave Jones:** on the schematics. So, that must be over on Yeah, where's like Where's my hierarchical list of I so don't know how to use this. Must be painful to watch for those who have a clue. People are probably screaming at

**Dave Jones:** me, "You're bored." What? Leave sheet. Oh, okay, thanks. Hierarchical sheet. There we go. There we go. In like Flynn. Drag. I'm I'm getting I'm getting used to it. Yeah, they've named Took me 5 minutes to get to this point.

**Dave Jones:** They've named the nets here high and low. Somebody just beeped me. It's not going to be Mr. Christopher J. Gammell, is it? And, yeah, so they've labeled them high and low. It's Chris Gammell. He's not He's not a happy camper that I

**Dave Jones:** don't know how to use KiCad. Should I Should I embed Chris's chat window up? I don't know. Anyway, yeah, they instead of labeling the ground and VCC There he is. There's Mr. Gammon. Say hi, Chris. He's watching my live stream.

**Dave Jones:** Hi, guys. Wave to Chris. I think your audience might know just as well anything I know. Anyway, I can't leave your chat window up there because as soon as I click on this stupid thing it's going to it's going to go.

**Dave Jones:** It's going to vanish. See? Anyway, um yeah. Hi, Chris. Bye, Chris. Anyway back to this. Yes, they um labeled them high and low. Okay. It's fine. It like like as long as you know. You know, I don't know. I've never

**Dave Jones:** ever seen anyone do that before. H and L. Is that like a thing? Does that Has anyone ever seen somebody do H and L before? High and low? Maybe Maybe you know, cuz it's digital only and it's a digital only board. There's

**Dave Jones:** basically no analog on it. So, it's like high and low. Makes sense, you know? Yeah, VCC and ground, of course. I'm sure. Um Nope, never seen H and L on a digital board. Never seen it. Nope. Nope. Nope.

**Dave Jones:** H and old tube schematics. Oh, yeah, you get H plus. That's Or you get HT. HT for like high tension. On old tube stuff, that was common. You see it on home brew stuff all the time. 5VF for fused. Yeah, you know, like I

**Dave Jones:** would understand that. Like if I saw 5VF, I'd you know, it wouldn't take me long to guess that that's fused. Um H and L sounds more like a can than a power rail. Yeah. Anyway, anyway, there you go. There you

**Dave Jones:** go. We got sidetracked enough. H and L. So, that's the net I need to We've already done L um cuz the only nets we're missing based on these white um net lines, they tell us that that they're un unrouted

**Dave Jones:** nets. That's the term I was looking for. They're the unrouted nets. Um and I guess KiCad by default has unrouted nets on, which is great. So, I've explained pullback. So, let's go in and let's place our zone again.

**Dave Jones:** Once again, we've got pullback. We're putting it on the VCC layer. I'm not going to rename it rename it H. Anyway, hi. H. There you There we go. Right? So, we're going to do thermal relief. As I said before, I don't know the

**Dave Jones:** difference between thermal relief and through-hole thermal relief, but I did thermal relief before on the ground plane, I believe, and that that seemed to come out fine, but we can change that. Not sure what the default difference is there. I wonder if you can

**Dave Jones:** set those up. I wonder if you can actually um uh define Are Are they fixed in KiCad? Or are they Can you go in and like have a user-defined uh pad connection? I'd like to know that. Like I I assume that you can set the

**Dave Jones:** diameter and all like the width of the um traces with whether you want uh two connections for your thermal relief that goes horizontal or vertical or whether or not you want a cross or whether you want diagonal or whether it however you

**Dave Jones:** want to uh yeah. So, anyway, thermal relief. Enough around. We're We're going to We're going to connect on the VCC layer to H. Ta-da! Oh, no, there it is. Sorry. Arbitrary. There you go. You can define it You You do it in here.

**Dave Jones:** Horizontal and vertical and 45° only. There you go. Um so, I answered my own question. Outline style, hatched. Uh fill mode, polygon or segment? Boundary mode, low resolution, high resolution? Not sure what that is. When it gets towards a boundary

**Dave Jones:** condition near an edge, it maybe takes longer to process or something. Corner smoothing. Oh, chamfer or fillet. Clearance minimum width. Okay. We can do our Um yes, of course, it's all in here. I should have just looked before I start

**Dave Jones:** I started yapping on saying, you know, I wonder if it's got all this stuff and it's like right in front of me.

**Dave Jones:** Oh dearie. Anyway, and it it has all the stuff I was talking about. Right in front of me. Yes, someone mentioned it. Anyway, you know, all the parameters are in the window. Exclamation mark. Alf Alfredo knows. Export settings to other zones. Okay,

**Dave Jones:** cool. Anyway, let's not dick around. Um All right, for the hatched. Um yep. Good old hatched ground plane. People don't do hatched ground planes anymore. That was all the rage back in the '70s and '80s. Anyway, here we go. So,

**Dave Jones:** do do do We're creating our zone. I won't say polygon cuz polygon is a different thing, isn't it? And we've got our pullback. I'm not sure the distance of that pullback, but who cares? It's good enough. Not not even sure what grid

**Dave Jones:** spacing I'm using. Where Where is it? It's down the bottom somewhere? Grid, 1.27, 50 mil. And ta-da. And there we go. I assume we have to go back up the top or can I just right click and get out of it?

**Dave Jones:** And it will complete. Ta-da. There it is. I like that feature there that it shows you that it's you know, it hasn't bothered to fill in that. Guess it's kind of neat. It's a little bit visually messy. Do appreciate

**Dave Jones:** that. What's going on here? Some silly buggers happening in there. Do they have like invisible pads or something in that footprint? Anyway, it has joined. There you go. It has joined all those in there and why do we have an unrouted

**Dave Jones:** net? Why Why do we have still have a few unrouted net connections? Maybe they're on the top side. Look, a few a few of these black lines. The heart feature turned on. It's called the love heart of death.

**Dave Jones:** Okay, you you can't set clearance between tracks of different classes, really? Try and hit B. I did hit B and it just rebuilt. What is it doing? Sorry, I missed that. Loading zones. It re- it rebuilds the zone. Okay, great.

**Dave Jones:** Something weird going on here. Well, it's not weird. It's obviously there's a reason for it. Okay, so there's our low Oh, okay. Oh, okay, there's a couple of low ones which weren't connected. No? Yes, they are. Okay. So, they're they're nothing to with VCC.

**Dave Jones:** Oh, hi. This one here is, look. Hi. Look, H, right? So, Oh, look at that. Look at that. We have a DAG. We've got a DAG. We found it. There we go. Look at that. We've got a genuine DAG.

**Dave Jones:** Little little bit of track in there. So, it's going So, if we did a DRC on this a design rule check, it would say that you've got some floating copper. I don't know what it would call it in KiCad, but

**Dave Jones:** you know, that's basically it's it's floating copper. It's unconnected copper. So, we want to kill that and our trace goes away. So, we're now we're in our basically our our tidy-up phase of our PCB. Let's assume that we

**Dave Jones:** had to routed this and um then we're uh in the point where we're um just making sure all of the nets and where we've we've connected all the nets. We've got no unconnected nets. You might at this stage do a DRC and you might get a

**Dave Jones:** report and you might put that on a second screen so that you have your report there and then you just go through and you might have 20 things that aren't connected because of that floating copper you had there or you

**Dave Jones:** know, some other issue or something like that and you just go through and tidy them all up until you get a DRC zero DRC errors and then there's lots of other things before before actually releasing your board but anyway, why don't what

**Dave Jones:** why doesn't L come in here? Is there a No, cuz we're using a ground plane. So it should work. So ground and VCC Yeah, look. Why is it going over Is there another bit of daggy copper out here? Yeah,

**Dave Jones:** there we go. Another dag. It's another dag. That's that's left over. That's That is totally unsurprising because this No, no, it's not actually because they use zones and I just deleted the zones cuz this was originally a two-layer

**Dave Jones:** board. Okay, and they they would have filled in the copper the positive and negative rails on the two layers on the top and bottom layers as zones as fills and yeah, look. Yeah, we've now we've now got a bunch of Oh.

**Dave Jones:** Don't want to flip. Yeah, we've now got a bunch of these. See? Got a bunch of floating coppers. So it's a bunch of dags. So even though I I actually deleted those, it shouldn't have left little residual dags like that. So that's that's really

**Dave Jones:** rather surprising. There's another one down here. So I don't know where these little residual dags came from. Isn't a big deal. What is this? What is this? Is this some sort of registration? I'm like you know, test coupon. If so, I

**Dave Jones:** don't really understand it. Okay, that's that doesn't even match the trace width, you know? That doesn't even match the minimum trace width. So, I'm not not sure what's going on there. For for for those who don't know, often you'll

**Dave Jones:** usually do this outside the board. You usually won't do it on the board um cuz it's just visual pollution. Uh well, some people do. And it's fine. Um you will have a uh test coupon. It goes by various other names, but you'll

**Dave Jones:** generally put it on the outside of the panel, and you'll put uh things like the the minimum trace width that your manufacturer can do. So, you'll put a couple of lines on there to set like minimum trace and spa- minimum trace and

**Dave Jones:** space and stuff like that. And uh you might put some alignment markers for, you know, you might put uh some silk screen over the copper, for example. And what you do that for is that when you get the board back from the

**Dave Jones:** manufacturer, you can look at the test coupon, and it's got all of the information in there you need to check the manufacturing quality of that board. So, you can see you can go you say you put it under the microscope, and you have a

**Dave Jones:** look, and you can see the alignment of the layers. You can uh you you might pull back your copper there, so you can see all all through the different layers. Um and you can see the alignment of the

**Dave Jones:** masks that and everything solder mask uh um your silk screen top and bottom, your copper, uh you know, stuff like that, whether or not they've over etched or under etched. You can get in with there with your micrometer, and you can

**Dave Jones:** actually measure uh you know, if your you know, 4 thou track is actually 4 thou, you know, what in the hell how much they're out by. Have they over etched the thing? You know, all all that sort of stuff. So, it's common

**Dave Jones:** to add a test coupon. For this board, I don't care. Right, we're not pushing the envelope here. But if you were, you You if you had a board that had three thou three thou tolerance or something, you know, you're really

**Dave Jones:** getting down there to like a real dense board, then you'd maybe want that. Because especially if you've got a big large complex board and everything's really dense, you've got really thin traces, you've got really fine pitch stuff that need really good alignment,

**Dave Jones:** big 2,000 pin BGAs and stuff like that that need real critical alignment on the solder mask and all sorts of things, then a test coupon is absolutely vital. So, on a a professional board, you would uh do that. Something that you do. So,

**Dave Jones:** anyway, there's another one. We got one. Let's go around and get all the dags. I'm I'm getting used to this. I'm getting used to it. Another dag. Oh, look. Naughty naughty. Uh-oh. Greater than 90°.

**Dave Jones:** Bad design practice. Dock your day's pay. As an old colleague of mine used to say. If you did that, I'd dock your day's pay. Um it it just goes back to the old um the the reason that you don't do that it

**Dave Jones:** have sharp angles like that. Um it's not so much an issue these days cuz the process tolerances are like the the process controls are really good on manufacturing boards these days. They're just stunningly good. But um uh you know, back in the old days,

**Dave Jones:** um it it it's still the case this these days. When the board is in there, when the board's in the um etch bath getting etched, and the etchant, you know, they they use like a bubble etch, so it's all

**Dave Jones:** bubbling around in there, right? So, it's all swishing around. So, when that um when that etchant um either ammonium persulfate or ferric chloride. I don't know if they use anything else in industry. They might. Might be some special mixture. Anyway,

**Dave Jones:** it's all agitating in there, right? So, the swell of of the um etchant in there, when you got sharp angles like that, it can sort of like it like builds up in there, and it can etch more away. So, in theory,

**Dave Jones:** um you could actually get over etching in that particular space there. So, that's why you don't want sharp angles like that. You'll have 90° or nothing. And then a lot of people will say, "Oh, I don't even like 90° cuz that's also an

**Dave Jones:** and it's also called an a um an etchant trap or an acid trap. And so, if you got really sharp angles like that, all the all the etchant, you know, in theory can sort of like Now, even though it's only

**Dave Jones:** really thin, right? And it generally just washes over the top, it it does actually potentially etch away more of the trace in there. If you got really thin traces, you can get breakthroughs on your traces or, you know, so it's

**Dave Jones:** it's really bad. So, that's called an acid trap or an etchant trap. And uh So, some people would think that even 90° is an acid trap, right? So, they'll put a fillet in, they'll put a chamfer, right? And uh and PCB packages will have

**Dave Jones:** cham you know, options. They they chamfer all of you though it'll auto chamfer your traces for you, you know. Um and some people like like that look, and I don't blame them, you know? It's pretty funky. I'm Yeah, I I probably

**Dave Jones:** went through a a fillet phase, you know? And uh and and the other thing is teardrops as well. Now now that we're talking about this, see? Like See, the problem here is is this trace here, right? So, coming down on the

**Dave Jones:** this this trace here, right? This is not This is not good layout, right? You don't have your trace coming down and then at an angle. Like even though it might be angling in here properly and it might be physically connected. I don't

**Dave Jones:** like that KiCad doesn't actually No, there it is. It's hidden. See, I didn't like that that was hidden, right? So, it's it's going to the center, which is all great. Okay, but then you've created the acid trap in there, right? It's It's

**Dave Jones:** just not good design technique to actually do that. So, I don't know if we can I don't know how to move. Um yeah, so that's that's not good layout practice to go like that. Never enter Basically, never enter the the rule is

**Dave Jones:** never enter a pad at anything but 45° or 90°, right? In this particular case, we're entering sort of like well we are entering at 45, but it's coming right down and touching it. So, it shouldn't It should have come down like

**Dave Jones:** that. Maybe going in like that and then down. So, you know, like it's it's just minor thing. And then there's minor tidy up things like this. Like, you know, if I was a PCB Well, I am a PCB designer.

**Dave Jones:** Right, but if I was laying out What I meant to say is if I was laying out this board, right? I could not live with this. Right? As I As a professional piece I like I could not live with that. I would have to tidy

**Dave Jones:** that up, right? So, I I I drag those flat. Like, there's no reason to have them going like that. There's no electrical reason why that's a problem. Okay, it's not. It's It's visually. Um so, you know, stuff like that. But

**Dave Jones:** by the way, don't be harsh on the on the guys who did this because it was their first rodeo. This was like that They learned to use I think I believe they said that they learned to use KiCad. This was like

**Dave Jones:** their first layout like ever, you know? And like other things in there that's just going straight through. That's really, you know, that's a bit how you doing. You know? So, they did really well for their first board ever. Here we

**Dave Jones:** go. I got more dags. Looking for dags. Another one. I guess we should just do a DRC, right? Yeah, it's it's not necessarily an an Maybe it is an OCD thing. But you know, it's it's just taking pride in your PCB layout. You know, any

**Dave Jones:** professional PCB designer will have pride in their layout and you know, just I know I thought I saw another day. You know, have it having something as simple as that right would like just show that you show that you don't care. You know,

**Dave Jones:** and and like it it wouldn't matter to anyone. Like it's just you know, it's it's purely a self-satisfaction thing. But anyway, they've they've they've done a pretty good job on this layout. Like it's it's their first time doing

**Dave Jones:** anything and I'm I'm really impressed that they actually got the you know, the the the routing the placement and everything is really quite decent. So it's it really is a good job. There's those other pads. Here you go.

**Dave Jones:** Yeah, that explains that. Um right. So how do I run a DRC? Design rules checker. Rules. Design rule or rules? Hmm. Um I have a measure and list nets. Gravy. See, hang on. Hang on. I just want to

**Dave Jones:** try Well, look there's another another non-right angle in there. Sorry, I know I'm just I'm just around now. I want to um How do I tidy that up? No, I No, I don't want to. No, I don't want to because

**Dave Jones:** No, the whole idea of this doing this is so that it's exactly the same layout as before. It's exactly the same. I changed nothing. So I don't want people going, "Oh, but you moved the traces." Inspect design rule checker. How do we switch modes?

**Dave Jones:** How do we switch from imperial to metric? Inches and So I can't do it within here. See, if I was inside Altium I'd be able to hotkey it. Be able to hot key Imperial metric straight within side the um

**Dave Jones:** dialog box. Left toolbar, inches and millimeters. Doesn't do it inside the dialog box, you see? I'm I'm actually sorry you can't see it cuz it's under the chat window, but I'm actually clicking on the millimeters and inches thing.

**Dave Jones:** And uh which is fine. But uh it doesn't reflect in the open dialog boxes. So, it maybe that that's a you know, it's a programming thing. There we go, inches. Minimum trace width seven Give it to me in thou's. Like seriously,

**Dave Jones:** when you're doing DRCs, KiCad developers, um when you're when you're doing a DRC, you're not working in inches, okay? You're working in thou's, 1/1000 of an inch. By having it display point double 078 is ridiculous. This should not be in

**Dave Jones:** inches, it should be in thou's, 1/1000 of an inch, okay? Um that's just that's just silly. That is absolutely silly. Please Please Please change that. That's just insane. Right? I don't want to have to be through multiple decimal places.

**Dave Jones:** That's That's visually That's terrible. Muriel, please fix it. Anyway, so we're talking uh you know, 7.8 for those uh Imperial fanboys. We're talking about uh 7.8 thou uh minimum track width and uh minimum via size of uh 15.7

**Dave Jones:** um track width. Where Where's our spacing? Clearance by net Ah, clearance is by net class. Wow. Okay. Right. And we can't click on that. Oh, look, you can just go list unconnected pads or tracks. Unconnected items. There you go. Pad 16 on

**Dave Jones:** FCU internal non-copper. Can we just click on that? Yes, there we go. Found our dag. There you go. Found our dag. So, that was the unconnected thing. How do we get back to our dialogue? See, our dialogue box is gone.

**Dave Jones:** That's that's no good. I want my dialogue box to stay open, please. Like cuz if I've got this dialogue box on another screen, like, you know, if I'm professional designer, right? I got my multi screens, and I'm I'm, you know,

**Dave Jones:** doing the business, right? And I So, I've got this thing like it's half of the screen. So, like it's on the other screen here. List unconnected items. There we go. It didn't even Did that not refresh? See, it popped up, right?

**Dave Jones:** Maybe understandable. Um but I I go click on this, right? I I want to jump to this, and my dialogue box vanishes. Why? I want the dialogue box open, please. I want it left open. We've got another dag. So, it's finding all our dags,

**Dave Jones:** which is good. And uh yeah, so it calls them unconnected items. So, items, like like item. It doesn't know what it is. Of course it knows what it is. It's a track, right? It's got an unconnected copper. It knows it's copper, right? So, anyway,

**Dave Jones:** unconnected items. But, I guess when you're doing DRC, but you can do DRC on silk screen and solder mask layers. So, you know, it should go unconnected copper cuz it knows. It's not an item. It's copper.

**Dave Jones:** Unconnected count. Okay, list unconnected. We can redo it. Anyway, there you go. Oop. And takes us in. I The thing is, it doesn't zoom. See? It doesn't zoom. Here's another thing. If I'm out like this, all right, and I'm

**Dave Jones:** off off over here with the fairies, let's let's try this. Design rule checker. I'm sure there's a shortcut for that. List unconnected. Why did that change? Oh, no. Uh what? Okay. So, it it's centered. Oh, the good thing

**Dave Jones:** is it centers. Look. Okay, so that's nice. That's that's nice. Unfortunately, we don't have multiple ones anymore. I could go in and create multiple ones just to show you, but it Every time you click on it, so I assume if we had the

**Dave Jones:** list back here and we clicked on it, it would move around. But you notice it doesn't zoom in. So, I can't see diddly-squat detail on that. I shouldn't have to set the correct zoom level first and then uh you know, do that. Like it should at

**Dave Jones:** least go to some manageable zoom some workable zoom level so that I can see the thing that's failing. Okay? So, now I've got to go in and now I've got to go like that, right, to see it. And when when you've got a big list of

**Dave Jones:** stuff like this, you want to have your dialogue box off in the other screen. You want to click on each thing and then you want it to like jump just jump around the board to see what all the

**Dave Jones:** errors are and stuff like that. So, yes, KiCad developers, please uh add that ability. Okay, so we're good. List unconnected. So, we've got diddly-squat unconnected. Beautiful. So, everything's uh everything's hunky-dory. So, if we start our design rule checker,

**Dave Jones:** boop boop boop, pad clearances checked, clearances checking zone fills, zone-to-zone clearances. We don't have any of those um because we don't have multiple zones on multiple layers. Unconnected pads, keep out areas, test text, items on disabled layers. Finished and we're we're good.

**Dave Jones:** Yay! In theory, we can just go get it manufactured. Keep clicking the wrong thing, though, to scroll around. So, anyway, now we've got our like So, that's our top copper. There's our bottom copper. And we've got our VCC

**Dave Jones:** plane and uh the the thermal reliefs look good. No wackers. I can just see them. Sorry if you can't see them. Yeah. No No problem whatsoever. That's not going to cause a problem soldering wise. You know, we could I don't What's the wi-

**Dave Jones:** thi- thickness of those? They're They're like 15 thou traces. 15 thou for your reliefs. Can we How do I edit my zone? I can't double click on my zone. Why Why can't I double click on my zone? Help.

**Dave Jones:** Now I have to click the edge of the zone. What? Really? Okay. Even if there's nothing else. Even if Even if I've got all the other layers turned off, right? Whoa. Just slow down there for a second. So, even if I've got all the other

**Dave Jones:** layers turned off, there's nothing else under here, you're telling me that I can't double click on that. That sucks. That's just terrible, Muriel. That is terrible, right? I like I can I like even if you have multiple items there,

**Dave Jones:** when you double click on it, it should pop up with a box and say which item would you like, sir. And it like Yeah. I You know, it's small things like this. Just, you know, spit and polish. Um

**Dave Jones:** You know, I like I'm I'm not saying it's bad, right? But it's it it could be a lot better, right? To to have to go to the edge and select it like that. Oh. See, I can't even Then how do I

**Dave Jones:** zones? Then how How I How do I edit my zone? I've got my zone selected. Damn it. Is there E for edit? I'm exactly pointing all these things out. Free and open source is terrible on Um on spit polish, yeah. Well, you know,

**Dave Jones:** like it takes a long time to get spit and polish. E E for edit, that makes sense. Let me my cheat sheet. My cheat sheet doesn't have E on it. You're using some cheat sheet, obviously. All right. There you go. So, did we actually

**Dave Jones:** find out what this is? What the difference is? THT thermal. Doesn't look any different, does it? Doesn't look any different. Um clearance, minimum width, anti-pad, spoke width. Yes, 20 thou. Yeah, that's that's that that's a lot, isn't it?

**Dave Jones:** Geez, you know, you can take that down to 10. Must be greater than the minimum width. Oh, yeah? Fair enough. Was just testing. Little bit thinner, 15 thou. 20 thou thermal relief, that's pretty chunky. Just for completeness, you know, for OCD

**Dave Jones:** reasons, uh we'll uh we'll do that on our uh ground on our copper on our ground plane as well, or our L bus. There you go. No wuckers. 15 thou, plenty. Plenty. All right. So, we're good. Oh, I should

**Dave Jones:** bloody save this, shouldn't I? Haven't haven't crashed yet. I don't want to really want to save as, I just want to save four-layer PCB. Yep, yep, yep, happy with that. Just save it over the same file. Yes. Yeah, lots of clearance

**Dave Jones:** around there, no wuckers. All right. So, I Yeah, probably good to go. You know, I could do a lot more checking and stuff, but really I think uh that is that is fine. We should be good to go.

**Dave Jones:** Cuz the whole idea is that I didn't want to touch anything. Didn't want to touch a thing. Um except convert it to a four layer PCB and I don't want copper on the top or bottom. I don't want any copper fill.

**Dave Jones:** Cuz the whole idea, for those who don't know, the whole concept of this is that um, I want to show the difference um, in EMC in radiated emissions of a two layer board with ground fill top and bottom,

**Dave Jones:** you know, just like like like filling copper everywhere and higgledy-piggledy against a solid ground plane and I think this could be a quite a good example of that. So, yeah, you can get a better example, but I'd have to manufacture, I'd have to design

**Dave Jones:** a better example. I I just have this one to hand and uh, I think it's good. So, it passes all the DRCs. I think we're uh, I think we're good to go. Geez, we don't have much uh, look at how poor via is there.

**Dave Jones:** But, I'm not going to I'm not going to change anything. I'm going to leave it. Right? I would have had uh, cuz you risk breakout there, okay? And and you'll have a ring around the via there, right? That I I don't know. I

**Dave Jones:** could go in there and measure it, right? I can There it is, right? There's inches. I wish you could like toggle between inches and millimeters in in the dialogue box. That'd be really nice. Right? And so, we've we've Okay, so

**Dave Jones:** we've got a 23 thou pad with a uh, 15 um, thou drill, 15.7 thou drill. It's good enough, right? But anyway, I I wouldn't that's not, you know, I did that just looks a bit thinny to me. So, I'd uh, anyway, I'm I'm not not

**Dave Jones:** going to touch it. The board's going to be the same. I I don't think I have to do anything else. Like, this is not a production board, right? I I just like this is a one-off. I just want one.

**Dave Jones:** Right? So, I'm going to uh So, I'm not going to fuss over other things. I've done my DRC. It's all connected. It should work. But, it's a four-layer board. Like and we and we don't have to worry about like other stuff like 15

**Dave Jones:** thou Oh, look, it's added chamfers. Oh, look. Isn't that pretty? Isn't that? It's added the chamfers. Uh was it was it was that an option? Was that a secret option? And it's uh And it's rounded them, too. Isn't that groovy? All right, maybe that

**Dave Jones:** was an option in that uh polygon fill box. Anyway, like stuff like you know, like we're not talking high currents here. So, you know, having four four traces at 15 thou actually connecting through to the ground plane and

**Dave Jones:** everything else, that's you know, it's fine. Don't worry about it. We're good to go. Oh, 3D. Everyone wants a 3D viewer. Yes, we should. Yeah, before you get anything manufactured, thanks for kind of reminding me. Uh we should

**Dave Jones:** actually have a look at the 3D view. There you go. Because the the best thing about the 3D view is it's what you see is what you get. You can see the solder mask expansion on the pads. Like you can see,

**Dave Jones:** you know, you can see that sort of like I know you can test these in DRC, but there's nothing like actually looking at what your board is going to look like, right? Absolutely nothing. Um Actually, let's just hang on.

**Dave Jones:** So, how do I uh How do I do daddy it? There we go. That's how I do daddy it. That's a technical term for do technical term, do daddy in. I just hold down the left thing. So, that that that's all groovy.

**Dave Jones:** You can see exactly what you're getting. There's there's no silk screen on the bottom. See exactly what you're getting. How far can we go in? Can can we go into the layers like you can in Altium? Nah. Yeah, a few little

**Dave Jones:** artifacts. A few little render artifacts around there. Uh I was about to say, we need to add get rid of that pesky pesky copper. So, how do I place text? Dave Full layer, that'll do. So, I just know at a glance which board

**Dave Jones:** is what. There we go. Just whack it under there. That'll do. Dave CAD full layer. Yep, good to go. All right. Yeah, I won't I'm not going to This This is not going to be a tutorial on how to

**Dave Jones:** how to do a PCB, the steps going through for getting your PCB made. And uh It's passed DRC and uh there's no there's no unconnected jobs. I I like the fact that it has list unconnected as separate to the DRC. It's

**Dave Jones:** kind of good. You know, cuz they they are kind of different steps. Um you know, in in the checking process after you've finished a board. So, I kind of like that. You know, like a a DRC will find unconnected stuff, right?

**Dave Jones:** That's I would I don't have any errors now, but but I presume if we ran start DRC before with those um floating coppery bits and stuff like that, that you know, it would have uh it would have picked those up. Let's try

**Dave Jones:** it. Sorry, I don't know like the key the shortcut keys for this, you know. What? It's gone back to our silk layer. Select copper layer, right? We're on our copper layer. Place Oh, okay. Right, cuz it knows it's a line instead

**Dave Jones:** of a trace. That's why I was a bit confused. Because so it So, it knows that if I'm placing a line, boom, it jumps back to the nearest layer that has lines, which would be the silk, right? Cuz it's non-copper.

**Dave Jones:** So, that's interesting. So, how do I place my track? Track display mode. What's track display mode? What's K? Oh, yeah. Right. That's the thing I was thinking of before. I thought there was another layer on top of that. Add new track X.

**Dave Jones:** Why is there no place track under there? Am I blind? So, X. There we go. Beautiful. All right. So, I've got our floating copper, all right? Net. Let's just put it to H, right? Okay, so we've got We've

**Dave Jones:** We've now got our error, okay? Look at that. Automatically comes up. Sweet ass. So, if go to our DRC and we start our DRC. Ah. They're different. They're two different processes. That's interesting. Okay, I guess it makes sense. If your

**Dave Jones:** design rule check it it is your design rules. It's not connection-based thing. But anyway, yeah, so they've they've decided to separate those. I Okay, I've I've got no complaint about that. It was nice to check that. Okay, so if we list the unconnected, boom,

**Dave Jones:** there it is, right? Okay, I I've got no issue with that at all. Curious to know, curious to learn. Ah, look at that. Look at that. Okay. Like for all the smarts in apparently, you know, it's all got you

**Dave Jones:** know, whiz-bang super auto interactive auto routing and stuff like that. It can't do a simple thing like straighten that trace, right? It should know that I'm being a fanny fuss pot and I've moved my cursor over to here.

**Dave Jones:** It should know I intend to make that flat. Okay? But it's just rigidly sticking to the rules in that to the snap grid. It's just rigidly sticking to the snap grid. And is there a way around that? Break

**Dave Jones:** the trace first. No, I don't want to break the trace first. That's Okay? No. No. No, this is No. Uh No. This is just wrong. No. I should not have to break that trace and then rejoin it or whatever. I should just be able to

**Dave Jones:** take that trace, drag it, and it should overrule. Can I do No, shift alt No. No, it it it should know. It should know that I want to straighten that up. It knows where my cursor is, right? It knows where my

**Dave Jones:** cursor is. It should know that I'm over that. Oh, thanks for telling me that. I'll join it straight across. All right? No, I don't want to use X and draw a new trace. No, I don't want to change my

**Dave Jones:** grid size. See, No, I'm sorry. But as somebody who worked at Altium and advised on this sort of stuff, okay? That was my job at Altium is to advise on this sort of stuff. Is that This is not how

**Dave Jones:** a professional PCB designer wants to work. Okay? A professional PCB designer to fix that does not want to have to break the trace. They don't want to have to delete the traces. They don't want to have to dick around with their grid

**Dave Jones:** size. They don't want to do anything. They want the software to know their intention and overrule the snap grid. That's what they want to do. Okay? Yeah, I I know KiCad's not Altium and this is constructive feedback to the

**Dave Jones:** KiCad team. Okay? Is that Something simple like that can make the in- can make the routing experience much better, right? I've come into this package cold. I know nothing about this package, but as a professional PCB designer, that's what I want to do. A simple thing

**Dave Jones:** like that, and you're forcing me to either break the trace or change my snap grid. No, wrong. Please fix it. I mean this in the It's not criticism of I mean this in It's constructive feedback to the KiCad team.

**Dave Jones:** What Richard asked a good question. Why did a professional PCB designer put traces off grid? Well, I I didn't design this board, but there are many reasons why you would do that, because you're very often changing your as when you're designing a board,

**Dave Jones:** especially a complex one, you are changing your snap grids and visual grids all the time. You are changing them all the time for various reasons that I won't go into like you're mixing imperial and metric components, surface mount and through hole. You're doing all

**Dave Jones:** sorts of other stuff. You're working on high density stuff versus you know, larger stuff like that. And there's many reasons why you might have a grid uh traces off grid and stuff like that, especially when you're doing interactive auto routing and stuff like

**Dave Jones:** that, which won't you can overrule the grids and stuff like that. So, there's many reasons why you want to do that. And so, I should not be forced to have to change the grid to match that. It It It's just dumb. It

**Dave Jones:** should do it. I'm sorry. Unless I'm completely wrong and then there's a way to do it, but I'm sure everyone would be screaming at me if there was a way. Yeah, no, okay, Glenn, fair enough, you know, submit my suggestions to KiCad.

**Dave Jones:** Thanks, James. Jane, sorry. Jane says I'm right. Course I'm right. I know what I'm talking about. Just lower it enough. Oh, okay. You lower the grid enough, but I shouldn't have to. I shouldn't have to touch the grid. That's the entire point.

**Dave Jones:** And trust me, anyone any professional PCB designer, I guarantee you will agree with me. Guarantee you. Anyone who's done any serious large-scale PCB design would absolutely agree with me. That you shouldn't to change that grid is just like it's going to cause

**Dave Jones:** frustration in using the tool. Just draw a new one. I don't want to have to draw a new one. Why should I have to draw a new trace? That is ludicrous. Okay? I should just be I would have to drag and

**Dave Jones:** tidy up. This is a step in the PCB layout process is going through and tidying up stuff like this, okay? Cuz you might have all these residual things left You might have these residual things left over cuz you've moved, you know,

**Dave Jones:** you've pushed and shoved around it, and you're moving all over the place. And as a final pass, you're going through and you're just tidying up stuff like this. And you know, I It It It should be trivial to do that.

**Dave Jones:** And it's not. Okay? And I know you might think it's trivial. Just change the grid size. Just delete the track and place a new one. Or just place a new track. It It It is totally beside the point.

**Dave Jones:** Okay? Trust me, if you had this, you and you saw the difference in productivity on a huge board that has thousands of components, tens of thousands of traces, and things that you have to tidy up as a professional PCB designer.

**Dave Jones:** Right? It It It Okay, I can do this, right? I'm trying to place a new track. Right? I'm doing the X thing. Ah, there we Go. Okay, it took it got rid of it. It's kind of groovy. Undo. But I shouldn't

**Dave Jones:** have to place a trace. I should just be able to drag it around. See, when I place the trace, it was the wrong width. Meh, it didn't even do the pickup. Okay? It does I'll I'll ask this. Does KiCad

**Dave Jones:** have the ability to automatically pick the existing trace size from the trace I connected to? To have the ability to automatically pick the trace size and overall the current trace size to the track that I'm editing, right? Cuz you know, generally

**Dave Jones:** you do not want to make it to neck that down, which is what that's called. That's the industry term for when you go to a thin trace to neck it down. There is a button for that. Drop down trace sizes. It can button at

**Dave Jones:** the top. Ah, auto track with when starting into is use its width. Otherwise, thank you. It's got it. It's got it. Okay. Okay, so you got to enable that. Okay, that's groovy. All right. Well done, KiCad. Nice. Look at that.

**Dave Jones:** Did it. Fantastic. Okay, happy. But, I'm not happy that Sorry, I want to undo that. But, I'm not happy that it doesn't allow me to drag. Yeah, it does have features. Yeah, I I will stand corrected every time. I have

**Dave Jones:** not used this, okay? This is literally the first time I've used KiCad 5. I do I'm just, you know, um adding my uh commentary as I go. Now, try drawing a new trace from out four to under under red, right? All right. Now, I get

**Dave Jones:** like we could go into this forever. I don't know if I'm in OpenGL view mode. Push the lowest connection up should fix them all. Yeah, but I I want to drag just one. And if it did push them, then

**Dave Jones:** if they happen to be the same spaces, it might work. But, then again, it might not if they're a bit higgledy-piggledy. KiCad needs a do-what-I-mean mode. Look, I'm not badmouthing KiCad. a very impressive and usable package, okay? Uh

**Dave Jones:** I I just want to make that clear. From my just using it from for you know, for the last hour and the previous time that I used it. I I know as a professional piece of engineering it's a

**Dave Jones:** very powerful and capable package. Um there's just you know, I just offer some constructive feedback in things. Um drag but one is limited to the grid. If dragging multiple will go beyond the grid. Okay. Drag item or drag Yeah.

**Dave Jones:** There you go. So yeah, you know, I I just want I just want the ability to be able to tidy up my work. It's not my work but you know. Anyway, enough around. Right, so okay. How do we generate Gerbers? Surely

**Dave Jones:** there's probably a print board. Is that it? Print? Is print Gerbers? Or is print print? Generic options. It looks like print print. Looks like paper print. Can you PDF? So I can import Spectra and DXF. Can export Spectra,

**Dave Jones:** GenCad, VRML, step. Fabrication outputs. Footprint position. Drill file footprint. Netlist file, a bomb. Plot. Now put Gerbers. There you go. All right, so Okay, whoa whoa whoa. Sorry. Wrong screen. All right, so this is our Gerber postscript, SVG, DXF. Wow, uh

**Dave Jones:** PDF, there you go. Yep. So generating our Gerbers. It went our FCU. Love it. VCC, ground, our copper. And uh our uh we don't have an adhesive layer. Don't have a paste layer. We only have a top silk. We don't have a

**Dave Jones:** bottom silk. Um and uh solder mask front and back solder mask, drawings and edge cuts, which is our board outline. I think that's that's all we need. Am I missing anything? Drills is the button bottom button. Oh, you can run run DRC

**Dave Jones:** from here. That's handy. We should have already done that. Uh save reports, generate drill files. Okay. Plot. Okay, do we need to generate drill files first? Okay, bottom right. Generate drill files. Okay, so we've got our layers. We've got top copper

**Dave Jones:** inner planes bottom copper uh top silk. There is no bottom silk. We've got our top and bottom solder mask. That's all we need and our edge cuts. Um edge cuts. Just weird names. Should be like board outline, something

**Dave Jones:** like that. Edge cuts. I don't get that. Uh so generate drill drill drill files. Okay, we've got our excellent format, inches. Doesn't matter. Drill map file format. And mirror Y. No, we don't want to absolute. Uh auxiliary. We don't want an auxiliary

**Dave Jones:** axes. No, we want absolute. Uh decimal format, suppress leading zeros. We're not fussed in that. Uh precision two four. That'll do it. Generate drill files. I think all the defaults are uh good to go. Uh plated through and non-plated through

**Dave Jones:** in single file. Um I don't think we have any Oh, yeah, there's five non There it is. There's five non-plated pads. This is not a production board. Generating. Oh, no. Yeah, no. It It created separate files. There you go.

**Dave Jones:** Created a plated through hole and non-plated through hole. Check the option to combine them. There was an option for that, was there? Oh, okay. In in single file. Not not recommended. Only use for board houses which ask for merged No, I I always do

**Dave Jones:** them separate. You You want to do them separate. Um The PCB manufacturers know. Like, you don't have to muck around with that. So, anyway, yep, done. All right. So, I've generated drill files and then we whoa. It just plotted.

**Dave Jones:** I expected I don't know expected it to ask something. It just did it. So, with our FCU Gerber is created, our VCC, our ground. I I like how it uh how it names them. That's good. F silk, F mask Gerber edge cuts

**Dave Jones:** It's all good. I I think we're probably done. Does it have a Gerber viewer? Really, PCBWay asked for a combined. Why Why can't they just do it? Why can't they just take both files and import them? Yes, in viewer. Yes, in the launcher.

**Dave Jones:** Blah blah blah blah blah. Okay, so some Someone said it's in the viewer. All right, let's go to the Gerber viewer. Yeah, there it is. Yeah. Okay, open Gerber files on the current layer. So, I've got to open them, do I?

**Dave Jones:** Okay, there we go. Created them today. Uh these are the original ones. Okay, so we don't want those. Okay, can we uh open multiples? Yep. Yep, we're good.

**Dave Jones:** Hey, we're we're in. Okay. Can I delete you know all that? Whatever. I don't think Here we go. This Gerber viewer's all right, isn't it? It's overlayed them by default. How about that? There you go. Does it have any like um any checking?

**Dave Jones:** Any design errors? Just just a viewer? Yeah, it's it's not a professional production tool. All right, showing the um showing the outline here. Where does that come from? Showing the um I didn't think that we printed didn't think that we printed the

**Dave Jones:** Why Why is it got the sheet on there? We didn't print a sheet. Or is it Or is that generated in the in the just the Gerber viewer does that? Oh, it showed the sheet before I imported. Thank you, Clayton.

**Dave Jones:** All right. Yeah. All right. Yeah, it did cuz I'm I was just confused. I didn't think that it was possible for it to uh Is that edge cuts? Edge cuts. Um I find that just that name fascinating. No. So, yeah, the Gerbers look good.

**Dave Jones:** They're all lined up. We didn't goof anything. And uh Uh cuz you can goof it up with uh absolute origin versus uh you know a uh other reference. So, there you go. And we want to check for our pullback. Like

**Dave Jones:** I said, here's the important stuff. Okay, you do not want this copper to go right to the edge cuz if you do, especially on a multi-layer board and especially given that the inner planes are usually on a prepreg, a very small

**Dave Jones:** prepreg it's called, uh very thin prepreg. They're They're They're not usually quite thin actually together. So, when you saw the edge of the board off or route it off or do whatever. Yeah, you can get the burrs and you can easily

**Dave Jones:** short out your copper planes. So, huge trap. Um many people have come a cropper on that one. Uh Yeah, so you want that You do not want that copper to go to the edge of the board. Not sure what's going on

**Dave Jones:** there. Actually, that Why Why is that not a The pad didn't look like that in the PCB designer. Is that a Is that a Gerber render in issue? Gerber command IDs, yeah. Need to add more chamfer sections or

**Dave Jones:** something. High high quality {slash} low quality. Oh, okay. Is there a Basically, we just want to know that the um you know, the Gerbers are all lined up. Nothing looks out of place. There's no There's no dags. There's our VCC layer.

**Dave Jones:** So, I think we're I think I think we're good to go. I think I think we're done. Oh, that needs to be done in the PCB layout. Did I Oh, okay. Right. That was actually at the PCB level, was it? Okay.

**Dave Jones:** PCB plotter use low Okay. So, it occurred back in the PCB stage. Low low quality polygons for speed. Okay. There's 16 32 selection of how many segments on a circle. Okay. Thank you, Lucas. KiCad does not seem to

**Dave Jones:** export circles on planes. Okay. Right. Cool. All right. Thanks, guys. I I think I'm done. I'm I'll get this board um get this board manufactured. How big is the board? Sorry. That's just Might as well finish this off. Let's go all the way

**Dave Jones:** with LBJ. Uh how how big is the board? Can we uh Can it give us dimensions, anyone? Can it give us like uh inspect May I I know we can measure, but I want to see if it can do it from the

**Dave Jones:** uh cuts. You know, edge cuts. Is there like a board information thing? Display options. Is there a board information? Tool in the bottom right. No, yeah, there's a measure tool. Yeah, no, I don't want to measure the distance. I want it to automatically

**Dave Jones:** give me stats about my board. Cuz it knows how big my board is. It's got that edge cuts outline. I want it to be able to tell me. Does it have that ability? That'd would nice. I would like it to just tell me your

**Dave Jones:** board is X by X. It's got 2,000 components. And Yeah, no, yeah, this place measure tool. I okay, you know, that looks like the only thing you can do. All right. See, it should be able to snap. It It

**Dave Jones:** knows I'm on the Oh, thank you. Fatato potato? For your $10 super chat. That's generous. I love your videos. I've learned so much. I've been working with Eagle for about 5 years and just recently switched to Altium and want to take my boards to

**Dave Jones:** the next level. Any tips? Um I don't know. I've done as I said before early in the stream, I've done a But if you if you already have 5 years experience using Eagle, um but I've already done a

**Dave Jones:** video. It was part of my power supply design series laying out a board. Um and I walk It's It's like walk-through commentary. Laying out the board. And I've got manufacturing design rule videos. They're massively popular. It's one of

**Dave Jones:** my most popular videos. It's got like 800,000 views or something. It's huge. Um I've done a couple of those. Like there's at least part one and part two for the manufacturing design rules and stuff like that. Panelization is a big

**Dave Jones:** thing part of part of uh the production side of stuff. You know, panelizing things if you want to take your boards to the next level is integrate a test solution into them. And I've done a video on that.

**Dave Jones:** Uh how to integrate test in into your boards like edge connectors so that you can plug in test jigs and and test, you know, 10, 50 boards all at once on the panel. Um which, you know, um So, yeah, um Um, maybe, you know, if you

**Dave Jones:** if you're serious about it, um, go get do the IPC certification course, get a the CID certification. Um, I'm I'm a CID certified PCB designer. They often running depends where you live and stuff like that, but they're not cheap. But if your company can pay

**Dave Jones:** for it, maybe. They've they've got a training budget. Try and uh They have to spend their yearly training budget. If you're doing PCB design at work, I would highly recommend um the CID course, for example. How do you know the size of my board?

**Dave Jones:** 9.25 by 6.25. Um, yeah, so those things I recommend to take your uh PCB design into the next level is knowing about production, knowing about, you know, things like that. Anyone can lay out a board, right? But, you know,

**Dave Jones:** to do to know about getting boards manufactured and tested and things like that with the utmost efficiency, that's where the value add comes in for a professional PCB designer. Oh, potato potato, you're a 16-year-old. Really? Is there an age No, I don't think

**Dave Jones:** there's an age limit. They'll happily take your money. It's It's It's not cheap. It's not cheap. It's like like It's a multi-day course. It's a professional multi-day course. It's not going to be cheap. Yeah, at at 16, okay.

**Dave Jones:** Yeah. All right, well, that's a different That's a different thing. You You You wouldn't do it at 16, probably. Unless you find someone to pay for it for you. Oh, you did. Thank you, B Upstick. You're the one who sent me the files.

**Dave Jones:** Thank you. Of course you know. Right. I don't inches, what's that in millimeters? Let's go over here. This will be the final thing for the day. Dimensions. Oh, no. Input What What was it? 9.25? 6.25. No 9.25 by 6.25.

**Dave Jones:** Four layers. Quantity. Just need one. Um least expensive color. Yeah. Let's just go least expensive color. What can we get this for? Silk screen just on the top. I don't need bottom. Cheapest finish. Yeah, give me a cheapest ass finish possible. Not that

**Dave Jones:** gold flash rubbish. Um board thickness. Yep, standard board thickness. 2 mil Oh, really? You can't even go above Like you can't go to 2.4 or anything. You can't do any thickity doodad boards. It's a shame. 1 oz copper. 6 mil trace

**Dave Jones:** and space. I think we're 10 mil. Like we're we're 10 thou or something. But I'll just leave it by default. Whatever. Like eight. I don't know. I don't know what the design rule thing in this one was. Minimum drill

**Dave Jones:** size. No one does drill sizing. Inches. Rubbish. Anyway, I'll just leave it by default. Uh gold fingers. No, we don't have any gold fingers.

**Dave Jones:** Number of designs separated only by silk screen. Quality certifications. No, we don't want any of that rubbish. I don't want quality certified. China versus Taiwan PCBs. Ding ding ding. Fight it out. Yeah. Yep. No, we don't need a stencil.

**Dave Jones:** Don't need a stencil for my through-hole design. Ship to Australia. Board arrives in default time. Get prices. Here we go. Yep. Yeah, this one the cheapest ass finish. I don't care if it's lead or not. They They They're not going to give you

**Dave Jones:** lead by default. They're going to give you lead free. PCBWay. Some of these are spammers. In fact, probably most of them at some stage. I should know. I didn't know. It's but some of them PCBWay have spammed. JLCPCB,

**Dave Jones:** I think they've spammed as well. AllPCB, yeah, no doubt. I think I think they've all tried to spam the forum. Make sock sock puppet accounts. I don't know what it is with PCB. Chinese PCB suppliers, they're like I don't know. They they're just obsessed

**Dave Jones:** with making sock puppet accounts. Thank you, Darkhorse Matter. Okay, Aussie bucks. Here we go. China Post 45 days, 234 bucks. Woah. That's JLCPCB, this is what I found last time, the cheapest price. Oh, it's an advertisement for PCBWay. Okay, sorry.

**Dave Jones:** Yeah, PCBWay have paid to uh um get right up the top of the list.

**Dave Jones:** Yep. So, the but otherwise that, they're sorted in price, yeah. Look at Look at this, yep. Yep. So, it's anywhere up to Look at this, 700 bucks. Advanced PCBs in the US, but they they're going to do a good job and

**Dave Jones:** they're going to turn it around quick. Breadboard Killer in Australia, 600 bucks cuz they they're they're good for like little boards, little tiny, that's their thing. But this is a big board. See, people think PCBs are cheap and

**Dave Jones:** well, they are compared to when I was a boy. But um you know, cuz people make you know, everyone does little bloody Arduino things these days. This is a decent size board, all right? This is a real PCB.

**Dave Jones:** All right? So, like even even Dirty PCBs, people think they're the cheapest on the planet. All right? They say like a lot of Dirty PCB fanboys, for example, not you know, bashing them. I'm you know, you know, you hear a lot, "Oh, you Dirty

**Dave Jones:** PCBs, get a PCB for a dollar." You know, it's practically free. Or whatever, yeah. 388 bucks, right? Because their their whole process is set up to manufacture to their entire business model relies on the fact that they can

**Dave Jones:** fit 50 different designs on their one panel this big. You know, once caught a panel this big. And they Yeah, and when you come along, smart ass come along with your big ass piece of real like this that takes up

**Dave Jones:** most of the panel and they're going to go screw you. You know, it's going to cost money. So, but check this out. I mean, this is insanely cheap. JLCPCB EasyEDA They have They're the ones who have that online EasyEDA thing, but they

**Dave Jones:** also have a PCB service. I don't know if they do it themselves or like I don't or they farm it out, I'm not sure. But anyway, it's insane. $87.50 and I get five of them. Five. I get five boards of 9 in by 6 in four

**Dave Jones:** layer for $87. That is insane. When I was doing like, you know, it's like for me to get 10 years ago to get a four layer board manufactured, just one, probably would have cost me a thousand bucks. This is insane.

**Dave Jones:** Insanely cheap. So, yeah. It's I'm going to use I think I'll use JLCPCB. Um you know, and 24 days I can get DHL Express. 100 Of course, I'm going to get go DHL Express, right? For the extra 10 bucks or whatever, 13 bucks. You're

**Dave Jones:** damn straight. Cuz I got a DHL dude that comes here every day and I'm I'm going to get my boards in 9 days. In 9 days, five of them for $87. Four layer, large. That is just wow. Wow.

**Dave Jones:** You young whippersnappers these days, you have no idea how good you have it with your online bloody shopping and your and your super duper cheaper cheap ass PCBs and your mouses and your Digikeys and and everything else. It's just

**Dave Jones:** It's ludicrous. That is nuts. Anyway, so there you go. So, that's it. So, I'll probably use them. I won't go through the process of getting it made now. Um well, I will after this after the live stream. So,

**Dave Jones:** that's it. Thanks everyone for joining me. I'll call it quits there. Now, get off Dave's lawn, yeah. And hopefully and then see the video I do, hopefully I'll get uh no, I'll probably get about 50 bucks in ad

**Dave Jones:** revenue from the video unless it goes gets very popular, you know, so it almost pays for the boards, you know. Yeah, I kind of peer it. Yeah, I kind of I'll pro- I'll probably get around to I I want to

**Dave Jones:** do like a a demo board. Um I actually design a demo board and then actually go through and get them made and have like a PCB manufacturer shootout, but unfortunately, it's one of those videos that doesn't that that dates, right? As

**Dave Jones:** soon as I release it, 6 months later, it it's just not may may not be can complete, you know, may as well delete it from YouTube cuz it's useless, you know. Um Please do more of these streams. All

**Dave Jones:** right, no worries. Potato, potato. Yeah, I haven't watched all the JLCPCB Factory 2 on Stranger Parts yet. I saw that it was there and I watched a minute or two here or there. Uh JLCPCB claim to be the biggest PCB

**Dave Jones:** prototype house in China and that's a big ass claim. Enjoy the rest of your day, Dave. Thank you very much. Thanks, guys. Thanks for joining me. Yeah, you're a bit late to the party. You just came in and said bye.

**Dave Jones:** Catch you next time.
