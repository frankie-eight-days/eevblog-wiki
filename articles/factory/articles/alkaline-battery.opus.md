# alkaline battery

The alkaline battery is the dominant disposable primary cell in consumer electronics, built on alkaline manganese dioxide chemistry with a nominal 1.5 V per cell.[515] Its defining feature for a designer is not its capacity but the shape of its discharge curve: the terminal voltage slides continuously from around 1.6 V down to 0.8 V, so a product that stops working too early throws away a large fraction of the energy it paid for.[772][140] Its defining feature for anyone maintaining equipment is that it eventually leaks a caustic electrolyte that destroys whatever it is sitting in.[1497][1274]

## Chemistry and construction

The electrolyte is potassium hydroxide, and it is the potassium hydroxide that gives the chemistry its name.[518] The anode material is zinc oxide, soaked in that electrolyte; between anode and cathode sits a separator, usually a fabric, whose job is to conduct ions across the gap.[518] The manganese dioxide cathode material is a distinctly powdery substance, more so than the zinc oxide paste.[518]

In a cylindrical cell the outer metal can is the positive terminal, not merely a housing. The only thing separating positive from negative is a small rubber O-ring seal around the base, which means a metal object bridging the can to the negative end will short the cell directly.[751] There is no seal at the positive end at all, which is why leakage is essentially never seen emerging from the positive terminal.[1296][H-yOP-KSMC4]

A 9 V alkaline is not a single cell but six 4A-size alkaline cells stacked in series, each stack's bottom plate forming the positive terminal of the next.[515][518][2Y1tVvllklc] More than one internal construction is used for 9 V alkalines, distinguishable by how the pack responds to being physically squeezed.[865]

## Terminal voltage and discharge behaviour

A brand-new alkaline cell does not sit at exactly 1.5 V. Open-circuit voltage ranges from the nominal 1.5 V up to about 1.65 V per cell, which for a 9 V battery means up to about 9.9 V at the terminals; the spread comes from the internal electrochemistry and the purity of the materials used.[515] A fresh single cell measured unloaded might read around 1.6 V.[779]

Open-circuit voltage on its own carries little information about state of charge, because the cell's internal resistance is inseparable from its electrochemistry — it is not a component that can be factored out of the measurement.[779] Manufacturer discharge curves are therefore given as loaded terminal voltage under a stated constant-current, constant-power or constant-resistance drain.[779]

Alkaline cells share the general shape common to nickel metal hydride and lithium-ion curves — an initial drop, a long sloping middle, then an abrupt collapse at the end — but the alkaline slope is markedly worse.[176][772] Lithium-ion is far flatter, which makes cutoff design easy; the alkaline's non-flat characteristic is what makes wasted capacity a real design problem.[772]

Practical end of life is 0.8 V per cell.[320][140] At 0.8 V roughly 95% of the cell's capacity is already gone, and the residual area under the curve below that point is on the order of 5% even at high discharge currents such as 1 A.[1296] Some designers take 0.9 V as the endpoint instead, though 0.8 V is the more common figure.[284] Below about 1 V lies only the lowest 30% or so of capacity, with the bulk of the energy delivered above 1.2 V.[139]

## Capacity

Capacity figures depend on discharge current, and published numbers are not always met. A quality AA alkaline — a Duracell Procell with four years left on its stamped shelf life, straight out of the box — delivered just over 2 Wh at 250 mA continuous discharge, falling short of a specified 9 hours to 0.8 V by more than an hour.[141] At the low currents typical of instrumentation, a AAA alkaline runs to roughly 1.8 Wh, sustaining 1 mA for around 1,400 hours.[1333] A high-end AA is worth about 4 Wh per cell.[1092] Nominal AA capacity quoted for battery-life estimation is around 2,800 mAh, though no product uses all of it.[1095]

Temperature matters more than the room-temperature curves suggest. Taken from 21 °C down to 0 °C, alkaline capacity more than halves, the cause being the sharp rise in the cell's internal series resistance as temperature falls.[140] Lithium primary cells such as the Energizer L91 outperform alkalines at room temperature across all discharge currents, and the gap widens dramatically in the cold.[140]

## Designing to the curve

A well-designed product has as low a cutout voltage as possible; a superbly designed one runs all the way to 0.8 V per cell.[140] Setting the cutout at 1.2 V instead wastes half the battery's capacity.[140] The penalty applies across essentially the whole practical current range, from 5 mA to 1 A.[772] By contrast, any product designed around rechargeable cells must already tolerate 1.1 V or less, at which point the wasted capacity is negligible.[772]

Single-cell operation is the demanding case. A boost converter fed from one AA or AAA must accept an input from 0.8 V to 1.5 V, which is what forces the choice of part.[139] Manufacturer parametric search tools make this explicit — Texas Instruments offers a single-cell alkaline/NiMH input checkbox that narrows ninety step-up regulators to a workable shortlist.[139] Substituting a lithium AA for the alkaline improves converter performance further, because the input voltage stays higher for longer.[139]

The same threshold drives component selection elsewhere. Ultra-low-power microcontrollers operating from 0.9 V to 5.5 V are well matched to single-cell alkaline use, because the usable energy in the cell is essentially exhausted by the time it reaches 0.9 V.[284] JFETs in electret microphone circuits that hold their gain down to 0.8 V, rather than rolling off at 1.1 to 1.2 V, can practically run from a single alkaline cell until it is dead.[611] Well-regulated LED torches are judged on the same basis: constant brightness maintained down to about 1 V per cell, with the alkaline cutout at roughly 0.8 V, is the desired behaviour.[78][67]

Bench equipment is specified against the same number. A lab power supply that regulates down to 0.8 or 0.9 V is useful precisely because a single D or AA alkaline is effectively dead over that range.[222] An electronic load intended for battery discharge curves must operate down to 0.8 V for alkaline work, and lower still for low-power testing.[862]

Battery-life estimation for a product follows directly from average current and the datasheet curve. A meter drawing 1.3 mA normally and 20 mA with the backlight on comfortably meets a 400-hour claim on a roughly 800 mAh alkaline.[60] A meter drawing 1.5 mA reaches about 800 hours on a 1,200 mAh lithium 9 V and a few hundred hours less on an alkaline 9 V.[1371] A meter with an always-on display drawing nearly 17 mA yields only about 165 hours best case and realistically closer to 100.[1095]

Not every product is suited to alkalines. Some cameras explicitly recommend nickel metal hydride and warn that alkalines may degrade performance.[495] Alkalines nonetheless have a decisive logistical advantage for a shipped product: they can be shipped without the restrictions that apply to lithium cells.[121]

## The last few percent

Recovering the residual energy below the normal cutout is a well-understood engineering trade-off, not a novel capability — extracting an extra 5% to 10% is something a designer can already build into a product, and there is no intellectual property in it to commercialise.[ixbLmBWUqcQ] Marketing claims built on the idea have not withstood examination. The premise that new batteries contain "1.5 volts of energy" confuses voltage with energy, and the accompanying claim that many devices stop functioning around the 1.3 volt mark did not hold up against the devices available to test it.[751] The capacity that such a sleeve is attempting to reach is the same 5% that lies below 0.8 V.[1296]

## Squeezing and dropping

Mechanically deforming a cell measurably changes its behaviour. A squeezed AAA alkaline yielded 261 mAh against 140 mAh for an unsqueezed control from the same pair; both began at the same 1.35 V recovery voltage, but the unsqueezed cell's voltage plummeted immediately while the squeezed one held a flatter response.[865] Squeezing a 9 V pack likewise raises its terminal voltage.[865]

The related drop test — determining state of charge by bouncing a cell on end, with a fully charged cell bouncing less than an empty one — is a real phenomenon rooted in the cell's electrochemistry, and works more reliably with AA cells than AAA.[508][865]

## Leakage

Leakage is specific to alkaline chemistry; lithium primaries do not do it, and it happens across brands, engineered leak-proof claims notwithstanding.[1350] It is a consequence of the vent design rather than a straightforward defect: alkaline cells are deliberately built to vent, because hydrogen pressure builds up inside from the internal electrochemistry and must be released.[1350] Because there is no seal at the positive end, the electrolyte escapes at the negative seal.[1296][H-yOP-KSMC4] Once out, the potassium hydroxide reacts with atmospheric carbon dioxide and forms the familiar white dendrite-like crystalline growths — potassium carbonate.[1296][1687]

The damage is severe and progressive. Leaked electrolyte creeps along and under a PCB, gets onto the top side, wicks under lead-mounted parts and heatsinks, and eats through solder mask down to bare copper.[1497][p8T4Dtc6OKk] Resistor markings dissolve until the bodies are transparent.[p8T4Dtc6OKk] It corrodes battery terminals to the point where a device with visually acceptable contacts fails in a subtle way — for example a voltage detector that gives a single beep at power-on instead of the double beep and LED flashes it should produce.[VZuebPVrzI8] Cleanup involves neutralising the residue, for which white vinegar is used.[-KSPOPz4VXk]

The resulting bench rule is unambiguous: never leave discharged alkaline cells in equipment long term, and be especially careful about alkalines stored in gear that is used only occasionally, such as a multimeter kept in a drawer.[1296][1636] Carbon zinc cells and rechargeables are preferred for exactly this reason — "None of that alkaline rubbish" is the operative habit when restocking a device that will sit unused.[1163][18OhbyQslF0][1571][1670]

## Controlled leakage testing

Establishing which conditions actually provoke leakage has proven difficult, and no manufacturer documentation or research identifying a discharge regime that makes leakage more likely could be found.[1296] The experimental approach taken was to obtain many different brands of standard alkaline cell, drain them under controlled conditions, and observe over months which ones leaked.[1274][j_eaXfmRB8Q] An initial run used a resistive load; some cells were left half-drained and others fully drained, in two stacks, then stored.[j_eaXfmRB8Q] After a period that included the 2019 flood and long storage on a window sill, none of them had leaked — a negative result, but a result.[1274]

A second attempt changed the method. Resistive discharge was abandoned because the dissipation required 1 W resistors in quantities not available, so thirteen sets of two cells each were wired in series and discharged at a constant 100 mA for 24 hours, or 86,400 seconds, chosen from the Duracell datasheet to land at roughly a 1 V end voltage without needing datasheets for the obscure brands.[RFb3TwWzza0] Series-string discharge of many dissimilar cells has its own failure mode: after 2,283 mAh had been extracted the entire string collapsed to near zero volts while 50 mA was still flowing, with individual cells reading around 0.46 V.[XDjyY48u0PU][hSkaZEgrZkY]

Leakage was eventually obtained.[1508] The brand pattern did not match the folklore. Not one of the Duracells in the test failed, and Fujitsu, Eclipse, Panasonic, Coles supermarket-brand, generic eBay cells, Philips and Maxell all came through intact — despite Coles cells being known to leak in ordinary use.[1508] The conclusion is that the discharge and storage conditions, not brand, dominate the outcome.[1508] Individual failures observed in the field span every major name, including both Duracell and Energizer, and 9 V alkalines as well as cylindrical cells.[1350][1497][2Y1tVvllklc]
