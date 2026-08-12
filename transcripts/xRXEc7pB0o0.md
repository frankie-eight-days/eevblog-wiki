---
video_id: xRXEc7pB0o0
title: EEVblog #253 - KiCAD Install & Schematic - First Impressions
url: https://www.youtube.com/watch?v=xRXEc7pB0o0
source: youtube-asr
---

**Dave Jones:** Hi, I thought I'd uh do a quick screen capture of me playing around with uh Keycad or Kyad if you want to call it that for the first time. It's the open- source free PCB schematic CAD tool. And

**Dave Jones:** um this isn't really a tutorial. I just thought uh this is seeen as this is the first time I've actually used it, first time I've downloaded, installed it, and had a go at it. I thought I'd just uh

**Dave Jones:** get a screen capture of my experiences of this and to see how intuitive it is to actually use it uh for the first time. So, I've typed in Keycad download into here. I'm going to use the uh Windows the latest Windows official uh

**Dave Jones:** distribution in here. And I'm currently downloading, as you can see down in the corner here, it's 146 megabytes. I'm downloading uh looks like version I don't know BZR 3256 stable the windful with components doc install. So, uh, once this is done

**Dave Jones:** downloading it, we'll, uh, have a play around with it, install it for the first time, see if it's intuitive to use. And my CAD background, of course, I used to work for, uh, Alium, and I've used Alium for 20 plus years. So, it's my main CAD

**Dave Jones:** tool. The CAD tool I'm pretty um, much the only CAD tool I'm familiar with. I've dabbled with a couple of others, but never done anything serious. So this so my perspective will be coming from somebody who's used the professional uh

**Dave Jones:** Alium designer environment um as a full-time PCB designer or former full-time PCB designer. So uh that's my background and I'll see if it's just works the way that I intended and just have a general play around with it and

**Dave Jones:** I'll let you know what my uh uh first impressions are and my gut feel of the product uh when it first installs. So here we go. We're almost there. 145 of 146 megabytes. 1 second left. We're getting close. Here

**Dave Jones:** we go. All right, it's done. Let's uh run this thing and install it. Got to bring this on screen here. I thought my screen capture program was supposed to uh force it in the middle there. Welcome to Keycad 2012 1112

**Dave Jones:** setup. Let's go. Yeah, I agree. I don't care what the license is. It's open source. It's all good. Main applications. I want to install everything. You bet. It'll take 315 megabytes to install it all. That'll do. Won't muck around with a specific path.

**Dave Jones:** I'll install it in the default directory. And it's all looking good so far. There's a lot of PDFs. Look, there's a whole bunch of PDFs. Why? I assume that they're to go with components. Why would you bother including

**Dave Jones:** PDFs in the install build? I don't understand that at all. I mean, it didn't take long there, but it's just makes for a bigger download. There's PDFs again. That's okay for the manual and everything else like that, but data

**Dave Jones:** sheets. I assume they're just example uh data sheets to go with example components on the building library. Anyway, bingo. We're done. So to edit or create, you need to install Wings 3D. Oh, okay. Right. So if you want to do

**Dave Jones:** any 3D uh models and um presumably do the 3D preview, then we have to install something called Wings. We won't do that uh yet. Check this box to open the Wings 3D web page. No, we'll do that later.

**Dave Jones:** Not going to muck around. Finish. We're done. So I will open up Kyad here for the first time. And this is what it looks like here. And I'm capturing this as a,024 by uh 768 window. So it's not going to be um

**Dave Jones:** as big as uh possible, but this is so that you're actually able to see it. And what have we got here? We've got uh the EES. What is it? The EES schema. The sorry EE schema. E schematic program. I

**Dave Jones:** hate that term schema. I don't like it at all, but it seems uh popular in um European countries to actually call it that. Um CV PCB is the PCB module. It's all modular. They've got different presumably different executables that do

**Dave Jones:** the schematic. The PCB. We've got PCB new. Oh, no. That's the PCB editor. Sorry. Components to modules. That's a It converts. Is that the library? No, I think the library is somewhere else. Gerber view bit map 2 component.

**Dave Jones:** Excellent. So, we can actually um install uh we can uh do bit maps like you saw on my previous blog. I put the image of a platypus or on my board. And you can you could put your logo,

**Dave Jones:** whatever you want um on your board. That should be really nice. That's neat. And a PCB calculator. The Swiss the Swiss Army knife. Let's open that. I'm curious to have a look at that actually. Sorry, I'm going to drag things on

**Dave Jones:** screen. Okay, it's just got some multi track width. That's handy. It's got a trace width uh calculator to determine the uh current um to determine the trace width required for a specific current. So, if you're designing a power supply

**Dave Jones:** board or something like that and say it's got 1 amp current capability, 10° rise um here, this is what I'm talking about, temperature rise here. that 10° is a nominal uh temperature rise which you want to um generally take as an as a

**Dave Jones:** rule of thumb. You don't want your traces to increase more than 10 degrees. You can if you're designing systems and you want higher margins and things like that, but 10 degrees is a good um figure. So they give you that by

**Dave Jones:** default. That's good. Copper thickness in millimeters, 35.035 millimeters. And you can do it in microns or mills. Anyway, that's a default uh thickness and your conductor length is 20 mm. We want let's say we want a 100 mm power trace to go across

**Dave Jones:** our board and we press this button over here. These are the formulas it uses to actually calculate it. It got it from the IPC uh triple 21 standard. But I think that's been updated recently because um all these figures are very um

**Dave Jones:** they're uh based on uh an actual like a a curve in the a a characteristic measured characteristic curve in the IPC21 standard. Um, and for like I think like 20 30 years it was the same old graph that which they used to refer to,

**Dave Jones:** but I think it might they may have actually updated that now to be more consistent with uh current practices. And anyway, uh, required trace width. There we go. 3 millimeters. I don't like working in trace width trace widths in millimeters.

**Dave Jones:** I prefer imperial mills. Oh, look. It doesn't automatically doesn't automatically change. That's a bit annoying. You have to hit it again. There we go. So your required trace width is 11.8. So you need round that up. You need a 12 thou

**Dave Jones:** twi trace or a 12 mil uh trace. Mill is the same as thou. Um but uh if you use the term mill, you can confuse it with millimeters and things like that. So but I I use those terms interchangeably.

**Dave Jones:** Mill and thou. So if you hear me using uh mil, it means thou. It doesn't mean millimeters. um usually. Anyway, there you go. That's the answer. You want a 12th hour trace for a will will current will carry one amp at for a 10° C

**Dave Jones:** temperature rise at 100 mm length. Neat. Uh and that's for sorry that's for an external layer. If you got a multi-layer board, then the trace because the uh heat can't escape as much. Oh, sorry, Mill. because the heat on the outer

**Dave Jones:** layers can more easily uh transfer to free air and you have maybe you've got some uh a fan forced uh thing through your uh case and you've got just convection and general convection inside um free air, little bit of wind or

**Dave Jones:** something happening, your external layers are going to cool down quicker. So your internal layers have to be bigger. In this case almost three times the width. There you go. 32 uh uh almost 31 thou wide for an internal layer on a

**Dave Jones:** multi-layer board. You got a four layer board and you're carrying 1 amp on an internal trace 10° rise. You want 30. But if you've got components on the top and you don't want them to heat up by 10°, then well, drop that down to one

**Dave Jones:** degree. Let's say a one° C rise over here. Bingo. You need a almost a 50 thou trace on the outer and 125 thou trace on the inner. Anyway, enough talking about that. I just think these cool as a tool

**Dave Jones:** that these are cool tools to have built in to a CAD program like this electrical spacing for various voltages. Um once again from the IPC21 uh standard and I was under the impression that these uh values actually oh yeah up to C sea level to 3,000

**Dave Jones:** mters. Yes they do um these values are spacings for dialectric breakdown at certain voltages. So if you got 240 volts running across your board um you want a certain spacing. So oh we got some transmission line stuff. Excellent.

**Dave Jones:** We've got micro strip standard micro. We've got a co-planer wave guide wave guide. Sorry. We've got a grounded co-planer wave guide. Rectangular wave guide. Excellent. Coaxial. Uh not that you need that on your uh PCB really, but it's built in uh coupled

**Dave Jones:** micro strip. And you've got strip line, which is inner designed to go on the inner layers of your board if you got ground planes either side of it. um and you can work out the characteristic impedance for a certain frequency. This

**Dave Jones:** is not like a field solver. It's not a professional uh field solver, I don't think. It's just more it uses your generic um formulas for your dialectric constants. And there it is, 4.6 there and things like that. So, it's fairly

**Dave Jones:** simplistic, but it gets the job done. And that's nice having that uh calculator built in. RF attenuators, resist color code, neat board classes. There you go. So, that's a neat little PCB calculator. There's more powerful ones on the market, but uh having that

**Dave Jones:** built in is rather neat. I like that. So, anyway, got sidetracked there. Back to Keycad. Um, this looks like yes, components to modules. I guess that's the library editor, I guess you could call it, because I don't I see a PCB editor, but

**Dave Jones:** I don't see there's Gerber viewer. There's that. And they're the only tools that we've got by the looks of it. So, this is the main. We've got a text editor, PDF viewer. Uh, what else have we got up here? Open,

**Dave Jones:** save, archive. Okay, it's uh it's pretty simplistic. And we've got an empty project called noame.pro. And well, I guess let's try the schematic editor. Let's open it up. And yeah, bubba. Hang on. I can't. It's given me this error message.

**Dave Jones:** Not found. And it's actually loaded up into a separate window. So there you go. It's not It's like It is actually I presume like it's a separate XI and it loads up. So it doesn't use the same uh windowed environment. So

**Dave Jones:** it's not like a unified program, but that's just fine. So let's see. If I'm using my mouse here, I'm using the center wheel, the scroll wheel, and that does exactly what I expect. It scrolls to the center location of the cursor.

**Dave Jones:** So, that's exactly what I was expecting. That's nice. It just zooms in and zooms out. Neat. I like it. Uh, we've got um not sure what size page template that is by default. Whether or not it probably wouldn't be

**Dave Jones:** A4. It might be. Oh, it might be. Uh, I'm not sure how we can find that, but uh, let's have a look at some of our We got our tools up the top here. Maybe we can Let's load in an existing schematic.

**Dave Jones:** That's an easier way to do it. Open. We don't have any open recents. Let's see if we have uh any dev group homepage. No, there's no examples. It should come with examples. I'm a bit disappointed. Unless they're buried.

**Dave Jones:** Share maybe into demo demos. There we go. Uh, pick programmer. All right. Well, let's try the P programmer. Pick programmer.sketch. There we go. Excellent. Would have been nicer if they labeled them uh as like a demo subdirectory or something, but I

**Dave Jones:** found that no problem. So, that's excellent. Nice little modular schematic. It shows that you can put borders around uh parts of the schematic as you've seen in some of my previous videos. I like to do that to make it

**Dave Jones:** visually quite nice and I'm enjoying that. Now I expect the left the zoom works exactly what I want using the center mouse wheel. Now I expect if I hold down the left button that will be pan. Will it be? No. Bit disappointed by

**Dave Jones:** that. I like being able to now I'm using the right uh sorry the left mouse button and that just highlights. Oh, highlights and moves. Okay, so left mouse button highlights and moves. I didn't expect that. I expected it to just highlight

**Dave Jones:** the objects and not move them, but I guess I'll press escape. And so there's no easy way to pan that. I hate having to go down here and use these um slider controls, slider bars on the side. I just find that really annoying.

**Dave Jones:** I like being able to um say do the uh right mouse click and then just pan around and pan around because I do lots of panning. So maybe there's an option for that perhaps or there's another way. Maybe there's a maybe the home key might

**Dave Jones:** be a way to Oh, home. Okay. So, the pressing the home key takes you to the full page. Excellent. End key. Page up, page down. Don't seem to do anything. Um, but anyway, I would have liked something that I could pan around much easier than

**Dave Jones:** that. But anyway, um, it shows the, uh, junctions. The junctions in here are shown as, uh, as these round circles there. So you know it's actually made uh contact. It looks a bit messy on the screen. I wonder what it looks like when

**Dave Jones:** it's actually printed out. Whether or not they get rid of those circles. They very well may when you actually save that. Speaking of which, let's see if we can save it as uh save current sheet as. What options do we get? We get Keycad

**Dave Jones:** schematic file. And that's it. There's no direct export to uh PDF by the looks of it, which would be nice. I guess you have to print it or plot it. Um gez, they support old postcript and HPGL and

**Dave Jones:** those older formats, but you can plot to a DXF. uh you can plot to clipboard which is a bit silly but if we print it then we can presumably we can choose like a PDF printer driver and you can print to a

**Dave Jones:** PDF that way but it would have been failed to upgrade the user configuration file. Okay, what does that mean? I won't say it's a crash but it looks like I aborted that and it didn't like it for some reason.

**Dave Jones:** So would have preferred to see a direct PDF export, but anyway, uh we've got some back annotate functionality there. We've got place, we can place a component, a power port, um and they have hotkeys, shift A, shift P, uh a wire, a bus. It

**Dave Jones:** can do bus oriented stuff, which is quite nice. Wire to bus entry. Excellent. That's all good. No connect flag. um that will be used for your uh design real check in your uh DRC. So if you don't want it to analyze a

**Dave Jones:** particular uh node in your circuit like you've left a pin open or something and you don't want it to give you an error message, you'll left that pin floating for a reason, then you would put a no connect flag on there. So let's see if

**Dave Jones:** we can actually put that no connect. Ah, it's just a it's just an X. So if we put no connect on that pin like that when we do a design rule check it won't actually analyze that pin. Um speaking of which

**Dave Jones:** uh now it automatic no it doesn't stay in that mode. Okay I pressed escape inches millimeters good we can just uh switch that'll be important in the PCB editor and just jump between inches and millimeters there. um change cursor

**Dave Jones:** shape draws and buses in any direction. Okay, so that's instead of 90° angles, it looks like you can uh do them in any direction, which is quite nice. Not often you want to do that, but when you do, it's good to have the capability

**Dave Jones:** to be able to draw any angles you want. Now, I was talking about the uh design rule checking. There it is. ERC error rule checking and let's the library browse the library editor annotate you see generate net list bill

**Dave Jones:** of materials okay the net list can go out to like a spice uh simulator or something like that a bomb of course uh we'll have to check that out but uh let's just run the ERC here and uh test

**Dave Jones:** has it already run I guess we have to test ERC see that that doesn't make sense why is it called test ERC See error rule. It's just there should just be go or start or something like that. Um no connect symbol is connected to

**Dave Jones:** more than one pin. Pin connected to some of pins but no pin to drive it. So that was that. Ah look and it's flagged it. Nice. It's put error markers there. So it's flagged that that I've done something dumb there. So if I highlight

**Dave Jones:** that how do I delete edit delete something. Okay, so I'm in delete mode now. Wonder if I press escape, I go back. Wonder if I press the delete key, does it put me into delete mode? Oh no, I just deleted a component. Um, oops.

**Dave Jones:** Uh, control zed. Thank you very much. It's back. All right, so obviously the delete key does not put you into delete mode, and that would have made sense. Um, so I assume in the delete mode I can just go, okay, it's got several

**Dave Jones:** components because it doesn't know which one to choose. So I'm going to go the um ERC, sorry, the no connect. It even puts up the ERC marker as an object. That's a bit unusual. So usually that shouldn't be an object on your schematic. It's

**Dave Jones:** just a it's just a marker, but we can erase that and go back into the ERC here. And I'll run that again. Test ERC. There you go. It got rid of that error message. So that schematic as it came

**Dave Jones:** has one error in it. And it's a type error three. Pin connected to some other pins but no pin to drive it. And there's the delete markers. So if you want to delete the markers from your page, you

**Dave Jones:** can do that. Um pin connected to some other pins but no pin to drive it. Okay. Pin 14. Power in of component U5 is not driven. So there you go. It's a floating input. So the input to U5

**Dave Jones:** is where? Down here probably. No, U4. Uh, which is U? Where's U5? Maybe I could probably jump to the component. That' be handier. Where is U5? Okay, maybe we try the find capability. Find U5. Let's try this. Match whole word. Just

**Dave Jones:** go. Okay, there we go. Bingo. U5 is Huh. Oh. Oh, it's a multi-heet. Oh, okay. Must be a multi-heet schematic. It's jumped over here. And uh there's our error marker. Sure enough, pin 14. It didn't like that. That uh

**Dave Jones:** that net name there. Um it obviously doesn't think that that's a power uh port. So it uh got confused because this is I assume that when you edit your components this component here you can when you set your pins you can place

**Dave Jones:** them up as power pins or data pins or not connected pins or whatever you choose the pin type usually that's how it works in Altium Designer anyway and uh a lot of other packages. So uh I assume that it knows that's a power pin

**Dave Jones:** and it should be connected to power but it doesn't like having just that net name. Hence it gave us an error message there when we compiled our schematic. And uh this is handy to get your error um to you know if you ignore all these

**Dave Jones:** errors you have to make sure that you know what you're doing. Um because the whole idea is you want to get zero errors before you push this schematic through to the PCB. But yeah, you can't always do that. Uh, a lot of the time

**Dave Jones:** you'll, you know, you can be spend a lot of time around trying to get your errors down to zero when you know you knew what you were doing and you know what the errors are and you can just ignore them. But there you go. So,

**Dave Jones:** I've got a multi-page schematic and I don't see any way to uh jump around. It tells us about the part down here. Reference U2 name 74 HC125 component library and description keywords. All right. So, I jumped to this schematic and I don't know. No,

**Dave Jones:** we're still in the same window. So, I'm not sure what's happened here. And how I jump to my multiple schematic pages. I've got to figure this out and I'm trying to do it in real time. So, it really is quite embarrassing. Everyone's

**Dave Jones:** probably navigate schematic hierarchy. There we go. So, anyone familiar who's used this um Oh, no. Pinockets dot sketch and that's the ah there you go root schematic. Okay, so it looks like I'm not sure if that's the default term and

**Dave Jones:** it always uses that but your main schematic page I guess is called the root schematic and there it is. Okay, I got no problems with that. That's quite fine. And then your subs schematic page is under there and it's hierarchal and

**Dave Jones:** you could have some pages under that I'm sure. Um okay, I rather like that. It didn't take me too long to figure that out. Wasn't that embarrassing? I'm rather liking it. Uh, place power ports. So, over here, here's our toolbar. Let's

**Dave Jones:** look at the right hand side here. I've been going for 24 minutes already, and uh I'm This is one continuous uh recording, by the way, and I'm doing good. I haven't really uh found any major issues yet. I

**Dave Jones:** quite uh I'm not minding this at all at the moment. Anyway, let's look at the left hand right hand side over here. Sorry, I get my lefts and rights confused often. I'm hopeless. Um, you can place a component. There we go. The

**Dave Jones:** uh, sorry, the little tool tips off the screen there. But as you can see, place a component, place a power port, place a wire, place buses, blah blah blah. Uh, net name. Excellent. Global label. Okay, so it looks like net

**Dave Jones:** names by default are not global across sheets. I'm assuming that that's what I would uh assume based on these two uh and I'll drag this over here so you can see the entire tool tip for that. Place a global label warning global labels

**Dave Jones:** with the same with same name are connected in whole hierarchy. Yep. So that's what I'm that's what I gathered from that. And that's fairly logical that net names are tied to the one sheet. A bit annoying if you want to um

**Dave Jones:** if you're used to just, you know, hacking a schematic together, not doing a hierarchal, but you need to separate the pages and the nets aren't uh global across sheets. They they don't connect. I assume you got to use ports.

**Dave Jones:** Um did we see a power port place a P? No, that's a power like let's power ground, but there's not place a junction. I wonder if it does auto junctions. We haven't actually tried that yet, but uh we will. No problems

**Dave Jones:** actually. Let's try that now. Let's draw a wire here. We want to go from here. And by def by the way, it's um set up the grid already. And the grid uh by default is if you look down here,

**Dave Jones:** it's got the XY coordinates because we're in millimeters mode. So obviously this was an imperial grid there. Yeah, there we go. Yep. Although that doesn't that's not rounded. Okay, we got 0.1 inch. Oh, okay. Yes. No. So it's a 50

**Dave Jones:** thou. It's a Yes, the grid is 50 thou. Okay, so this is an imperial schematic grid and it's done in 50 thou. So let's join this wire up here like this. And it does actually um do the 90° uh bend like

**Dave Jones:** that. So that's quite nice. That works as I expected. And let's just go up here just for kicks. And bingo. We're we're connected. And it removed those dots. It auto removed those junctions. Very nice. That's what I'd expect it to do. Now if

**Dave Jones:** we I expect it to auto place a junction as well. Obviously, if we connect, we're still in the drawing mode, which is good. And I like that how if you go out this way, it draws a line in that

**Dave Jones:** direction. If you go up here first, it draws it in that direction. That works as expected. So, I'm quite happy with that. If I go up there, bingo. It's autoplaced the junction. But if you want to, you can go in and place more

**Dave Jones:** junctions manually, but uh usually you shouldn't have to because it's uh Oh, maybe. That's right. Let's try this. Will it auto junction a line if you go over another? So if you go over like that, I do not want this to

**Dave Jones:** auto connect to that. If I just go over it like this. So if I go over, bang. And it didn't. Okay. So it didn't actually and that's exactly the behavior that I would have expected. So um in that case, here's a

**Dave Jones:** case where you want to place a manual junction. So you get your manual junction. Bang. I really expected that. Eh, a lot of people say that's bad practice to do um uh T junctions. Um sorry, uh cross junctions like that. So

**Dave Jones:** anyway, let's not get into that argument. What else have we got down here? So everything's working as expected so far. Quite happy. Uh place a hierarchial label. This label will be seen as hierarchal pin in this sheet schematic. Okay.

**Dave Jones:** Create a hierarchal sheet. So, you create a new sheet. Oh, let's create a new sheet. I can't can't pass up that. Oh, okay. There you go. It's a sheet symbol. All right. Excellent. Yeah, let's just label it. Yeah, whatever.

**Dave Jones:** Happy with that. And bingo. That is your hierarchial schematic sheet. Now, interestingly, it doesn't show me I'm already at my top hierarchy. I'm already Oh, sorry. No, I'm not on my route. That's why. There you go. I'm in uh pick sockets and it's

**Dave Jones:** created that hierarchial sheet under P sockets there. So, if we go back to root, we should find that. Yeah, there's that sheet. There it is. There's the sheet, the P sockets there. And there the data ports. There you go. It's uh

**Dave Jones:** works very similar to Altium's uh port structure with uh you you you draw a um a second schematic sheet and you can do ports going over like that. So that's why you place a hierarchal label. What else we got? Hierarchal pin

**Dave Jones:** imported from corresponding hierarchy layer. Let's go there. Test. And bingo. That is a How do How do we spin it? Okay. How do we rotate something? I've got my Let's press spacebar. No. See, spacebar to rotate would have been nice.

**Dave Jones:** I would have expected maybe R for rotate. Yes, there you go. I guessed it. That wasn't hard. R for rotate. There you go. And it's automatically uh flipped the text over. I quite like that. And there we go. We've created our

**Dave Jones:** another uh port there that's actually done that as an output. So, it's an output from that sheet. And this is clearly like an input going. You can tell by by the direction of the arrow there. This one's an output. that's

**Dave Jones:** pointing out from the that hierarchial sheet. This one's pointing inwards to the hierarchial sheet. And I'm assuming I could end tool. I'm assuming that I can edit that pin. Now, what mode am I in? I think I'm in like select. I'm in

**Dave Jones:** select mode because I'm I can just drag like that. Can I just double click on that? And yes, I can. I can just double click hierarchal because it doesn't know whether I want to select the sheet or the pin. So, hierarchal label test. I

**Dave Jones:** want to do that. No, it doesn't let me alter the properties. Clarify selection. Yeah. Have I selected the item? How do I edit the properties of that particular pin? I don't know. Anyway, I'm not too happy with that.

**Dave Jones:** That doesn't rotate move. Edit hierarchy oral label. There you go. Okay. So, E for edit. All right. There we go. And I can change the pin. There we go. The style is output. So, we can change it to an

**Dave Jones:** output. Let's make it a birectional. There we go. Bang. It's a birectional pin. Okay, that works quite good. So, it looks like to select something and edit something, you've got to doubleclick that and then press E for edit. There

**Dave Jones:** you go. Maybe if you're just here and you move your cursor over it and you press E for edit. Yep, there you go. Okay, so you've got to press E first. That's not too bad. Don't mind that. That's uh there's no issue with that. I

**Dave Jones:** would have preferred if it just doubleclicked that it knows you want to edit that particular item. I assume that's the same with this transistor over here. If I double click the transistor. Oh no, there you go. It works. So, it looks like the double

**Dave Jones:** click doesn't work if you have multiple items in there and you've got to select it first. It might be a bug perhaps. Anyway, so that's that works quite well. I'm happy with that. The BC 307. There it is. And you can go edit the Q value,

**Dave Jones:** you know, you can edit the uh designator. Here it is down here. Q3 if we wanted to change that to Q2 for whatever. Um, looks like you can change the size of the font. I'm assuming you can do all this globally and you can

**Dave Jones:** global select things as well and do all sorts of stuff like that. So, uh you can mirror it, rotate it, do whatever. You can add fields. Okay, beautiful. So, we've now changed that to Q2. And if I want to move it, there you go.

**Dave Jones:** Move it around. So, that that's what you got to do if you want to move something. You got to go press M and I want the field value moved. Okay, that's not too bad. That's pretty neat. I like that. Okay,

**Dave Jones:** no issues with that at all. And wow, I've been going for 30 minutes and I have already got the gist of uh the basics of uh editing hierarchial schematics. I think I think I could master hierarch hierarchial schematics already. What else have we

**Dave Jones:** got? We got graphics, lines, and polygons and free text maybe. Is there anything else? Just let me drag this off the screen. Yeah, there's a couple more. There's a place a bit map image and a delete items. So it looks like you need

**Dave Jones:** at least you need bigger than a,024x 768 screen I think to reliably use this but um no it's usable you just can't get access to a couple of tools down the bottom there with uh that size screen. And so if

**Dave Jones:** you're using this on, you know, a little netbook or something like that with 1,024 x 768, you might be limited. Sorry, I'm I'm capturing 1280 by 720 at the moment. Um, a 16:9 aspect ratio screen here, but yeah, I am fairly happy

**Dave Jones:** with that schematic editor so far. Annotate schematic, perform electric. Okay, the DRC's up there. Generate net list. It's all there. Let's have a look at the bill of materials components by reference. Yeah, whatever. Let's choose. Okay. And it's a list

**Dave Jones:** format. Okay. Bill of materials. It only gives you a dot list. I assume it's a text format like a commaepparated uh value file. We can probably save that. We'll have a look at that those sorts of things later. But there you go. I'm

**Dave Jones:** pretty happy with that schematic schematic editor so far. Haven't tried to create schematic components yet. But let's have a look at the uh let's go place. Hang on. Where's our place place component? Let's have a look at our

**Dave Jones:** libraries. Let's choose one. Select by browser. Oh, okay. List all. Search by keyword. Let's see if it has a uh BC 547 in it. Can we search by keyword? No. Okay. Uh, well, we'll go select by browser. Here we go. Now we're talking.

**Dave Jones:** Here's our library browser. This is the one the library components it comes with. Presumably, you can add your own. Oh, that's is that our current program? That's our current design. Look at that. It looks like it has loaded in our

**Dave Jones:** That's our current uh That's our current design. The P programmer. And it looks like they're all the devices used in our current project. I like that. That's rather neat. I wonder if you can then take that and drag it over to here. Oh,

**Dave Jones:** that that would have been neat if you could take someone's existing schematic and just import their schematic and then just drag Oh, that's a bit Maybe there is a way to do it, but I was hoping that I could drag that. But that's really

**Dave Jones:** quite neat. What does it come with? ADCs and DAXs. There we go. Uh, it's analog heavily dependent analog devices ones there. 74XX series. That looks pretty complete. Pretty happy with that. Can't complain. That's an individual gate. I wonder if

**Dave Jones:** it auto increments. Let's try that, huh? Oh, yeah. There we go. Part A, B, C, and D. It's got four separate parts because there's four gates in that and gate. So that works as expected. Show to Morgan converted part. Ooh, really? It is.

**Dave Jones:** There you go. Hey, that's neat. I like that. Oh boy. I wonder if that if it automatically does that or whether or not you have to program it in or not. That's interesting. ADC DAC. And then the de Morgan part of

**Dave Jones:** course vanishes. Um, analog switches, some DGs, Atmail. This looks Wow, somebody's a big Atmail fan. Whoever's done uh Keycad, they're a big That's a pretty comprehensive list of 80 megaparts. Wow, that's pretty good. I like that. Wonder if it's got the same

**Dave Jones:** thing for pick microchip. Here we go. Yeah, they're obviously not nearly as big a uh a PI fan as they are uh or whoever's contributed that thing, but I wonder if there's any central location where central repository where you can

**Dave Jones:** send your library parts and they actually get incorporated into the official build. I wonder if that's uh if that's possible at all. But anyway, audio parts. There couple of audio amps and things there. 4000 series CMOS. That's not fully comprehensive, but uh a

**Dave Jones:** good selection there. Happy with that. It's got like a 4066 quad bilateral switch. Neat connectors. Okay. It's got generic connectors, of course. 10-way things like that. I wonder how you do the uh footprint. If I just double click

**Dave Jones:** on that, it doesn't doesn't do anything. If I right click on it, I get nothing. So, I wonder how you link in your footprint. Actually getting sidetracked. Zoom. Auto home. Select part to browse. Okay. No. Oh, okay. Because this is not

**Dave Jones:** the library editor. Duh. Silly me. I thought we were in the library editor and we could actually edit parts here. We can't. This is just the library browser. So, um, Cypress parts few there. Device. It's got generic devices,

**Dave Jones:** diodes, seven segs, dual diodes, okay, switches, transformers, you know, all your generic parts. There's always a generic part which you won't find there, which is really annoying, but anyway, quite a few seven segment displays. That's pretty good. DSPs, Intel parts, interface

**Dave Jones:** parts. Uh, looks like some I squared C stuff, whatever that is. Linear devices. Um, no, linear parts, not linear. Um, so lots of national stuff there. LM331. So, we got op amps and comparators, memory devices. We got our uh,

**Dave Jones:** ers and stuff like that. We've probably got our E squ in here somewhere, maybe. No. Microchip microcontrollers more pick I don't know see why are those microcontrollers why are those pick parts not in microchip somebody hasn't tidied up the

**Dave Jones:** library there couple of motor roller parts old school stuff 68 HC11 nice optoouplers Phillips parts power all right now we got uh all sorts of power ports VDD plus 3 volts all that sort of stuff it looks a bit messy on the pin But I'm assuming

**Dave Jones:** that those grayed out uh parts won't actually be displayed. It'll just be the red circle with the plus 36 volts. Slonics special. Oh, there's a special library. Hey, that's nice. That's a pot. I saw a digital pot there somewhere.

**Dave Jones:** And so, you know, by all means, it's not a comprehensive library, but you wouldn't expect it. Um, but it would be nice if there's some sort of repository where you can go to. Maybe there is. I haven't looked. This is my first time

**Dave Jones:** using Keycad, so I got no idea. One chip in the Texas, couple of transistors. That's why we couldn't find our BC 547 because there isn't one. If I search for BC237 would have found something. So, valves. Somebody's a fan.

**Dave Jones:** And Xylink parts. Oh, that's not comprehensive, but it's not bad. And there you go. That's our library browser. So we can choose to uh uh place one of those parts. Let's um place a atmemell device. Where are we?

**Dave Jones:** An at mega 161. How do we place? Do we just press okay? Enter. I guess there's no okay button. I don't see one. No, I'm pressing enter and nothing happens. Okay, so we got a parts browser. That's bizarre. We got a parts browser, but we

**Dave Jones:** can't do anything with it. We can't select the device. So, I'd have to go back and actually choose an AT mega 162-P. Huh. It's got a insert component. There it is. Okay. Ah, view component documents. There we go. There's a PDF

**Dave Jones:** button and it links. There you go. That's nice. It's linked directly to the ATMmail website there. That's actually uh that's actually themail.com/im images/document. So, they've linked in the direct link to that data sheet. Neat. I like that. Pretty darn happy there. So, and then of

**Dave Jones:** course we can just place it. Silly me. And Mario got to get that screen back. And there's our part. So, we can zoom out while we're placing it. That all works as expected. Probably can't jump to another hierarchal schematic. Of

**Dave Jones:** course. There you go. By default, it looks uh like the parts are seeth through. They're actually transparent. Is that a good thing? It's probably not that bad, I guess. Um, so stuff isn't hidden underneath, especially when you're just hacking schematics together

**Dave Jones:** like this and you're placing components willy-nilly, updating schematics, you know, it doesn't hide the stuff behind it. And uh, assume if we just press M for move, we can place that part. No. What's the move command? Delete. Fine. Back annotate.

**Dave Jones:** All right. I feel like a dummy that I can't actually move a part because I can't I don't think I can just click on it. See, I can't just click on it and move it because then it selects. That's a bit

**Dave Jones:** weird. There we go. Move. Yeah, it is. M. There you go. I was right. M. Ah, you've got to have your cursor over the current device. There's a bit of ghost in there. You see that when it first moved? I

**Dave Jones:** don't know if it's that's my video card or not. seems very sluggish to sort of update that sort of stuff on the screen. I haven't seen like I can actually almost see it painting in the colors and things like that. It's very slow. So, I

**Dave Jones:** haven't seen that since the old Protel uh DOSs days really where you could actually depends on the speed of machine. You could actually see it redraw the component and in what order it actually drew things and stuff like

**Dave Jones:** that when you're panning around and moving parts. It was uh fascinating. But oh, there you go. I'm fairly pleased with that. And this is literally my first time using this. So, I've been going 45 minutes now. And uh in 45

**Dave Jones:** minutes, I've installed it, played around, around with the uh calculators, talking about those, and I've been able to edit hierarchy or schematics and do uh design rule checks and use my component library. Haven't created parts yet, but gee, it's not

**Dave Jones:** bad. I like it. So, I'll call that uh quits for uh this one anyway, just for this uh schematic part. I need a drink.
