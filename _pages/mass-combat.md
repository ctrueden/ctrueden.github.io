---
layout: page
title: "Mass Combat: Gridless"
permalink: /rules/mass-combat
category: rules
snippet: A combat system for D&D3E which expedites large encounters
---

In the d20 system, combat involving more than one or two dozen participants often becomes very lengthy, with each combat round taking an hour or more to complete due to the large number of actions being performed, and the complexity involved. This document defines a mass combat system—that is, combat between a number of opposing factions—designed to expedite such encounters while still giving heroic characters the chance to personally involve themselves in a meaningful way.

These rules were adapted from Savage Worlds (starting on page 104) and the Lord of the Rings (starting on page 238).

Naturally, to model large-scale battles capable of lasting many in-game minutes or even hours, the granularity of actions is much coarser. Players do not dictate every individual action their characters perform as they would in a normal combat scenario—rather, they decide how their character is trying to influence the outcome of the battle. Which army do you support? Do you fight in the thick of the melee? Command and inspire the troops you lead? Sling spells from the sidelines? Target the enemy generals? Or do you cower until the worst is over?

Mass combat basics:

*   Each **battle round** lasts 10 minutes (as opposed to a **combat round**, which lasts 6 seconds).
*   Combat occurs between a number of opposing **factions**.
*   Each faction is divided into one or more **units**, which are troops of a particular type that deploy together. Depending on the scale of the battle and effectiveness of the unit's constituents, the unit might consist of a handful, dozens, hundreds, or even thousands of individual combatants.
*   The strength of each unit is represented by a number of **tokens**.
*   Each important character—such as PCs, villains and notable NPCs—is a **hero** treated separately from units.
*   Each unit has a **general** responsible for leading that unit. Every general counts as a hero.

Initial battle setup:

*   Identify the factions.
*   Identify the heroes involved.
*   Identify the units of each faction, including the general of each unit.
*   Assign tokens to represent the **strength** of each unit. The general rule of thumb is one token per 30 total ECL of the unit, but may be modified by situational factors.
*   Each hero chooses an initial **affiliation** (i.e., the unit with which he fights in the first battle round), and identifies the other heroes with which he is **teaming**, if any.
*   Each general makes a Knowledge (tactics) roll to **assess** the strength of the enemy factions. The base DC is 20, modified by the situation as determined by the GM. For example, a +5 modifier if the enemy type is unfamiliar to the general (e.g., giants rather than humanoids), or a -5 modifier if the general has extensive reconnaissance data regarding the enemy.

**Affiliation:** Each hero is affiliated with a specific unit during a particular battle round, though he may change affiliations during the course of the battle as a heroic attack action (see "Decide Heroic Actions" below).

**Teaming:** Multiple heroes affiliated with the same unit can choose to join forces. However, just because two heroes have the same affiliation does not necessarily mean they are teamed—they must agree to work together, and commit to staying side by side for the duration of the battle round.

Teamed heroes have a number of advantages over solo heroes, but also some drawbacks:

*   They fight together in deadly combat (see "Decide Heroic Actions" and "Resolve Deadly Combats" below).
*   They can heal or otherwise buff each other using their utility actions (see "Perform Heroic Utility Actions" below).
*   They contribute to the battle roll only once for the team, although they assist one another in doing so (see "Teaming" in "Determine Modifiers" below).

Heroes can alter their team configuration using a complex utility action (see "Heroic Utility Actions" below).

## Phases of Combat

Combat is divided into 10 minute battle rounds. The following phases happen each round:

### 1) Events  

Occasionally, during the course of a fight, external events will occur that affect the tide of battle. Here are some examples:

*   A unit or faction enters the fight late after some rounds have already transpired. Incorporate the new unit into the battle from then on.
*   A unit or faction changes sides in response to something. Adjust the unit's token allocations accordingly.
*   A hero joins the battle late, or leaves midway through.
*   Artillery, air support or other phenomenon begins or ends.

The GM will announce any events at the start of each battle round.

### 2) Allocate Forces

Each general simultaneously and secretly allocates his unit's tokens with respect to the enemy units. This allocation identifies the enemies being **targeted** and represents how the unit will fight during the coming battle round. For example, a human unit with 8 tokens facing three enemy units—lions, tigers and bears—might allocate 2 tokens to the lions, 6 tokens to the tigers, and no tokens to the bears, indicating that 25% of the human unit's strength will target the lions, 75% will target the tigers, with no offensive against the bears.

These allocations are kept secret until the final modifiers are computed (see "Determine Modifiers" below).

### 3) Perform Heroic Utility Actions

A hero can perform utility (non-attack) actions, as deemed appropriate by the GM. Each battle round, a hero has 5 <span style="font-weight: bold;">simple</span> **utility actions** with obvious consequences, and 1 **complex utility action** requiring some GM interaction. Some examples:

*   Simple: Heal himself using his paladin _lay on hands_ ability.
*   Simple: Buff a teamed ally using a wand of _cat's grace_.
*   Complex: Create a _wall of stone_ at a critical choke point as an impromptu fortification (assuming such a location is nearby).
*   Complex: (Generals only) Issue specific orders to members of his unit; e.g.: find and retrieve a specific fallen hero.

Although it is assumed that the hero is taking these actions over the course of the coming battle round, treat the results as going into effect early enough to make a difference during this battle round (see "Make Battle Rolls" below).

A utility action that takes between 1 and 5 minutes always uses the complex utility action. For example, a cleric could cast <span style="font-style: italic;">bless water</span> (1 minute casting time) as a complex utility action.

A utility action that takes more than 5 minutes counts as a **lengthy action** (see "Decide Heroic Attack Actions" below) and uses the hero's heroic attack action for the round. A lengthy action that takes 10 minutes (e.g., _true resurrection_) uses both the heroic attack action and all utility actions for the round.

### 4) Decide Heroic Attack Actions

Heroes decide how they fight for the round. Possible actions include:

*   _Command army_ – Make a Tactics roll to command your unit (general only; see "Tactical maneuvering" in "Determining Modifiers" below).
*   _Change affiliation_ – Change your affiliated unit.
*   _Fight_ – Attack enemies; roll on Flow of Battle table below.
*   _Defend_ or _hide_ – Avoid fighting this round; incur -2 morale penalty for affiliated unit. As part of this action, you may retrieve a fallen ally from the same unit and carry them away from the battle, in preparation to heal them.
*   _Stealth_ – Sneak around looking for future battle opportunities (see "Stealth" in "Determining Modifiers" below).
*   _Desert_ or _retreat_ – Escape the battle completely; incur -4 or larger morale penalty for all units of affiliated faction.
*   _Lengthy action_ – Perform a lengthy action requiring more than 5 minutes; e.g.:
    *   Cast a _true resurrection_ spell (10 minute casting time) on a fallen ally.
*   _Defect_ – Change your affiliated faction (i.e., "switch sides"). You do not contribute to the battle roll this round. However, the unit from which you defected suffers a morale penalty depending on your relative strength (typically at least -4) for that battle round, and the unit to which you defect gains a commensurate morale bonus. For the remainder of the battle, the morale penalty/bonus is -2/+2.
*   _Betrayal_ – If a general defects, and he has arranged it with his unit in advance, the entire unit may defect with him, changing factions. The general still spends his heroic attack action for the round, but he immediately reallocates his unit's strength (see "Allocate Forces" above) versus his formerly affiliated faction. In this case, if the general is teaming with other heroes who are not part of the defection, he immediately enters deadly combat with them.
*   _Other_ – as deemed appropriate by the GM; e.g.:  

    *   Sing a continuous bard song to inspire allied heroes and nearby members of the affiliated unit.

**Flow of Battle table:** When fighting, roll 2d6, and use the result as follows:

*   Ferocious Battle (2-4): Same as normal battle, but hero takes double damage.
*   Normal Battle (5-8): Character contributes to the battle roll. See "Determine Modifiers" section below.
*   Deadly Combat (9-10): As normal battle, but the character's team also encounters a powerful foe, and has individual combat. See "Resolve Deadly Combats" section below.
*   Valorous Deed (11-12): Character gets an opportunity to accomplish a great task. As normal battle, but character's bonus to the battle roll this round is 3 higher than normal. (The GM should add flavor text as appropriate, or may choose to require the player to describe his character's particularly impressive feat in order to receive the bonus.)
*   Choice (13+): If a result above 12 is somehow achieved, the character has a choice of any other result above.

### 5) Determine Modifiers

Before each unit makes its battle roll (see "Make Battle Rolls" below), the GM determines and totals the appropriate modifiers. These include:

_Token advantage_: If fewer enemy tokens are allocated against a unit than there are tokens in that unit, there is a **token advantage**. To compute, first determine the unit's **threat value**: the total number of enemy tokens allocated against it. Subtract the thread value from the unit's strength. If this number is greater than zero, there is an advantage, representing the discrepancy between a unit's power and that of the enemies engaging it. For example, say a dwarven unit with 17 tokens has two enemy units—orcs and goblins—targeting it, with the orcs having allocated 9 tokens, and the goblins 3\. In this case, the dwarven unit's threat value is 12 (9 + 3), for a token advantage of 5 (17 - 12)—the dwarves are in good shape this round.

_Hero contribution_: Each attacking hero makes a roll with a DC of 15 + threat value. The type of roll depends on how the hero is attacking—it is often a melee attack roll with their favored weapon, but could be a ranged attack roll, ranged touch attack (e.g., using _eldritch blasts_), tactics skill check (generals only), stealth skill check (in the case of using the Stealth action above), or other roll as deemed appropriate by the GM. Due to the continuous dangers of battle, he also takes damage up to a number of d6s equal to the threat value, depending on his roll:

*   Less than the DC: No bonus, full damage.
*   DC to DC+4: +1 bonus, 80% damage.
*   DC+5 to DC+9: +2 bonus, 60% damage.
*   DC+10 to DC+14: +3 bonus, 40% damage.
*   DC+15 or DC+19: +4 bonus, 20% damage.
*   DC+20 or more: +5 or higher bonus, no damage.

The hero's modifier is based on the form of attack they are using. For example, a barbarian fighting with a greataxe would use his normal to-hit bonus with the axe when making his roll. Normal modifiers apply, but only if they would affect the majority of the attacks during the battle round. For instance, a bard using his action to sing for the round would grant morale bonuses to hit for allies on his team, and a barbarian affected by _bull's strength_ would use his improved strength score as long as at least 5 minutes were remaining on the spell's duration, but activating his rage ability would not be beneficial since it only lasts for a few combat rounds. Instead, heroes can make use of their limited-term abilities such as rage, _true strike_, smite evil and action points during deadly combats (see "Resolve Deadly Combats" below).

**Using magic:** A hero may opt to use magic as his attack form for a round. To do so, he expends any number of spells (or spell-like abilities) with total levels up to his character level. It is assumed that the hero is casting spells or otherwise channeling magic in the most advantageous way over the course of the round. No hero contribution roll need be made, and the hero takes a fixed 50% damage.

*   **In a normal spellcasting system:** Battle roll bonus is +1, with an additional +1 for every 4 levels of spells expended.
*   **In a vitality-based casting system:** Battle roll bonus is +1 for every 10 points of vitality spent to cast the spells. Full spellcasters (clerics, druids, geomancers and runemages), as well as bards, receive an additional +1 bonus for their focus on spellcasting aptitude (i.e., champions and rangers do not receive this extra bonus). See the [handy table](http://spreadsheets.google.com/pub?key=tJL7V5uiNSOaTM-e0zkYf9g&output=html) for assistance.

**Teaming:** For teaming heroes, they check against the Flow of Battle table only once for the team. Each hero on the team makes a hero contribution roll, taking damage individually as indicated on the table above. For the purposes of the battle roll bonus, however, the team takes the highest result, adding a +2 bonus per team member beyond the first, to represent the assistance from allies. The total result is then compared on the chart above. Hence, it is easier for a team to achieve a higher DC, but the heroes might still have reached a greater total battle roll bonus fighting separately, depending on the situation.

**Tactical maneuvering:** If the general chooses to spend his attack action this round on tactics rather than fighting, he uses his Knowledge (tactics) skill for his heroic contribution roll. However, a general leading in this way draws attention to himself, and thus always takes 100% damage for that battle round.

**Stealth:** Stealth must be undertaken as a team—i.e., if anyone on the team wishes to be stealthy, everyone must attempt to be stealthy. Each person rolls a Stealth check and compares the result on the heroic contribution table. Everyone on the team must beat the DC... \*\*TODO\*\*

_Terrain_: Different kinds of terrain contribute to the battle roll in different ways, as determined by the GM. For example:

*   One-sided terrain (e.g., higher ground; elves vs. dwarves in a forest; dwarves vs. humans in underground tunnels): +1 bonus to advantaged units, -1 penalty to disadvantaged units
*   Fortifications or trenches: -2 penalty to enemy
*   Major defensive advantage (e.g., a castle): -6 penalty to enemy

_Artillery, air support or other offensive advantage:_

*   Light (e.g., archers, musketeers): +2
*   Medium (e.g., catapults, ballistas): +4
*   Heavy (e.g., cannons): +6
*   Devastating (e.g., orbital laser fire, continuous _meteor swarm_): +10

_Other modifiers_ (GM discretion):

*   E.g.: one faction set traps on the battlefield beforehand that grant them a +2 bonus on the first round of battle.

### 6) Resolve Deadly Combats

A deadly combat is a break in the normal flow of battle where heroes briefly engage one another. Each deadly combat that has been incurred (see "Decide Heroic Actions" above) lasts up to ten rounds, and involves a conflict between the heroic team that rolled it, and the appropriate foes as determined by the GM. It is resolved as a normal d20 combat would be.

As a rule of thumb, to decide which foes a team of heroes encounters, first note the enemy units being targeted. From those units only, make a list of affiliated enemy hero teams. These teams are encountered from lowest CR to highest CR, but with enemy generals encountered last. The GM has the final say in which foes a team of heroes will encounter, and may adjust the order based on circumstance.

Note that it is possible for a team to be involved in more than one deadly combat in the same battle round. In this case, resolve the fights sequentially in an order determined by the GM.

**Unconsciousness, Dying and Death:** If a hero drops to 0 HP or below, he suffers from unconsciousness, dying and death as normal. A fallen hero retains his affiliation, and can be healed or resurrected as normal by allies with the same affiliation during subsequent utility phases (see "Perform Heroic Utility Actions" above). If a hero falls unconscious, his unit takes a -2 morale penalty that round (see "Make Morale Check" below. For every full round a character is unconscious, he takes an additional 1 point of damage per token targeting his affiliated unit as the battle rages around him.

### 7) Make Battle Rolls

Each unit rolls a d20, adding their appropriate modifiers, against DC 10 - token advantage. Success causes a targeted enemy unit to lose a token. For every 5 over the DC, a targeted enemy unit loses an additional token. In the case of multiple targeted enemy units, the fraction of tokens each enemy unit loses must match the attacking unit's token allocation as closely as possible.

For example, suppose a robot unit with 17 tokens has allocated 5 tokens versus a unit of pirates, 3 tokens versus a unit of ninjas, and 9 tokens versus a unit of knights. Further suppose that the robot unit exceeds its battle roll DC by 17, thus reducing the targeted enemy units by 4 tokens total. The enemies lose tokens as follows:

*   pirates: 4 × 5/17 ≈ 1.18 <span style="font-family: LucidaGrande;">→</span> 1 token
*   ninjas: 4 × 3/17 ≈ 0.71 <span style="font-family: LucidaGrande;">→</span> 1 token
*   knights: 4 × 9/17 ≈ 2.12 <span style="font-family: LucidaGrande;">→</span> 2 tokens

In the case of any rounding ties, the attacking unit's general chooses how the ties are broken.

### 8) Make Morale Check

Each general makes a Will save (using his own Will save modifier), DC 20, each round that his unit loses a token, with the following modifiers:

*   -2 per token lost that round
*   -1 per token lost in previous rounds
*   -2 (or more) per defected or deserted hero (see "Defect" and "Desert" above)
*   +4 if your unit is fearless (e.g., undead)
*   +4 if your unit is behind fortification
*   +4 if your unit cannot retreat
*   other situational factors as decided by the GM; e.g., morale modifiers during the battle round (e.g., bard song) may affect the roll

If the general fails the save, the army loses one token to desertion for every two points below the target DC (e.g.: a general who nets an 11 loses 2 tokens).

A final battle roll determines how many troops are defeated during the retreat. Apply the amount the general failed to the final battle roll to represent a "morale penalty" for the retreat. (E.g., if the leader fails badly, then this penalty could result in devastating losses during the retreat—i.e., a rout).

If a general is removed from the battle for any reason, the base Will save bonus for the morale check becomes +0\. In this situation, another affiliated hero can take over as general at the beginning of the next battle round.

## Aftermath

After the battle is over, some fraction of the casualties are merely wounded rather than dead. Some enemy soldiers may be captured, killed or exiled by the winning side afterward. The exact circumstances depend on the situation; it is the GM's role to describe what happens.

* * *

Notes on wounds/vitality and vitality-based casting:

*   Net vitality recovery during a battle round is 0.
*   If you hide or otherwise rest for the round, you recover 50 vitality.
*   Each battle round you may expend points from your spellpool during utility actions to gain the increased caster level benefit. Whatever portion of your spellpool you expend, you do not have for any deadly combats that round.
*   In general, you do not take wound damage during a battle round, except during deadly combats, or if your vitality is fully depleted. Some exceptions may apply depending on the circumstances.
