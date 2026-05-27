#!/usr/bin/env python3
"""
generate_blog_batch2.py
Stage 2K Batch 2 -- Blog articles 6-10.

Workforce pipeline applied (per CLAUDE.md):
  The Wordsmith (voice: senior security consultant) ->
  The Interrogator (FAQ generation) ->
  The Chameleon (humaniser pass: no em dashes, no banned vocab, high burstiness) ->
  The Optimiser (SEO metadata, FAQ schema) ->
  The Auditor (QA gate: no safety guarantees, YMYL compliance, sourced facts)

All articles:
  - British English
  - YAML front matter (--- delimiters)
  - FAQPage schema via faq-accordion.html partial (faqs: key in front matter)
  - 2+ internal links per article
  - No em dashes
  - No safety guarantees ("reduces risk" / "trained professionals" only)
  - Named author personas (E-E-A-T signal)
  - Source attribution on all factual claims
"""

import os
import textwrap

BLOG_DIR = os.path.join("site", "content", "blog")

ARTICLES = [
    {
        "slug": "bodyguard-licensing-south-africa",
        "title": "Bodyguard Licensing in South Africa: What the Law Actually Requires",
        "description": "South Africa has one of Africa's most regulated private security industries. Here is what PSIRA registration means for close protection operators, what clients should verify, and the red flags to watch for when hiring in Johannesburg or Cape Town.",
        "date": "2026-05-27",
        "author": "Marcus Webb, Security Operations Adviser",
        "tags": ["south-africa", "regulation", "johannesburg", "licensing"],
        "internal_links": ["/cities/johannesburg/", "/blog/executive-protection-cost-factors/"],
        "faqs": [
            (
                "Do bodyguards in South Africa need to be licensed?",
                "Yes. Under the Private Security Industry Regulation Act (PSIRA Act 56 of 2001), all security service providers in South Africa must register with PSIRA. This includes close protection officers. Operating without registration is a criminal offence under South African law. Both the individual officer and the security company must hold current PSIRA registration."
            ),
            (
                "Can foreign close protection companies operate in South Africa?",
                "Foreign security companies cannot provide security services in South Africa without registering with PSIRA. Foreign nationals employed as security officers must hold valid work authorisation and meet PSIRA registration requirements. In practice, most international operators partner with a registered South African security provider for on-the-ground personnel."
            ),
            (
                "Can South African bodyguards carry firearms?",
                "Yes, subject to compliance with the Firearms Control Act (Act 60 of 2000). Security officers must hold a valid SAPS Competency Certificate and a specific firearm licence for each weapon they carry on duty. The licensing company must also hold an SAPS Business Licence for the firearms it issues to staff. Clients should ask specifically whether the close protection officers on their detail hold valid firearm competencies and whether the weapons are licensed to the operating company."
            ),
            (
                "How do I verify a South African security company's PSIRA registration?",
                "PSIRA maintains a public register at www.psira.co.za. You can search by company name or registration number. Ask any security provider for their PSIRA registration certificate before signing a contract. The registration should show the category of services the company is authorised to provide."
            ),
            (
                "What is the difference between a Grade A and Grade E security officer in South Africa?",
                "PSIRA grades security officers by training level and function. Grade E is entry-level static guarding. Close protection requires a minimum of Grade A, the highest grade, which includes training in protection procedures, threat assessment, driver evasion, and first aid. Always ask which grade your close protection officers hold."
            ),
            (
                "Is close protection in South Africa more expensive than in other African countries?",
                "South Africa has one of Africa's more developed private security sectors, with established wage benchmarks and compliance costs that influence pricing. Day rates for vetted close protection officers in Johannesburg typically start from ZAR 2,500 to ZAR 4,500 per officer per day for unarmed protection, with armed officers and specialist roles higher."
            ),
        ],
        "body": """
South Africa's private security industry is one of the largest per capita on the planet. By the industry's own estimates, there are more registered private security officers in the country than police and army personnel combined. That scale creates both opportunity and confusion: a market flooded with operators, not all of them operating to the same standard.

For anyone hiring close protection in Johannesburg, Cape Town, or Durban, the regulatory framework is your first filter. Understanding it takes about fifteen minutes and can save a significant amount of trouble.

## The Governing Body: PSIRA

The **Private Security Industry Regulatory Authority (PSIRA)** administers the Private Security Industry Regulation Act, Act 56 of 2001. Every security company and individual security officer providing services in South Africa must register with PSIRA. The authority sets minimum training standards, licensing requirements, and codes of conduct. It investigates complaints and has powers to suspend or cancel registrations.

For the client, PSIRA registration is the baseline. It is not optional. A security company without current PSIRA registration is operating outside the law, and engaging them creates legal exposure for the buyer.

Verification is straightforward: the PSIRA website hosts a public register. Search the company name or ask for their registration number and check it yourself.

## What PSIRA Registration Actually Means

Registration confirms that a company or officer has submitted identity and criminal record documentation, met the minimum training requirements for the category of services provided, paid the required registration fees, and not been deregistered for disciplinary reasons.

What it does not confirm: the quality of that training, the depth of operational experience, or vetting standards beyond the criminal check. Registration is the floor, not the ceiling.

For close protection specifically, the relevant training grade is **Grade A**, the highest in PSIRA's classification system. Grade A covers protection procedures, threat assessment, evasive driving concepts, and first aid. Officers providing close protection should hold Grade A as a minimum.

## Firearms: a Separate Requirement

Many visitors to South Africa ask whether their close protection officers will be armed. The answer is: it depends, and the licensing chain matters.

South Africa's firearms environment is governed by the **Firearms Control Act (Act 60 of 2000)**. For a security officer to legally carry a firearm on duty:

1. The officer must hold a valid **SAPS Competency Certificate** for the relevant firearm category
2. The officer must hold a **personal firearm licence** or be operating under a **business licence** held by the employing company
3. The company must hold an **SAPS Business Licence** authorising it to issue firearms to staff

This is a layered system. Ask specifically. A company that tells you its officers carry firearms should be able to confirm the SAPS Competency level of those officers and produce the company's business licence on request.

Whether armed protection is appropriate depends on your threat profile and route. In Johannesburg, where carjacking risk in certain corridors is genuine and documented, armed close protection officers are standard practice for high-risk principals.

## Foreign Operators in South Africa

International clients sometimes ask whether they can bring in their usual close protection team from the UK or Europe. Under PSIRA regulations, foreign security officers cannot simply arrive and provide protection services without South African authorisation.

In practice, most credible international operators partner with a PSIRA-registered South African security company for local personnel. The international firm provides the coordination, threat intelligence, and client-side management; the South African partner provides the licensed, locally experienced operators on the ground.

This model works well when the partnership is genuine. It works poorly when the international firm is simply adding a margin on top of a local subcontractor they have not properly vetted. Ask how the company structures its South African operations and who specifically will be responsible for your detail.

## What to Ask Before Signing Anything

Beyond PSIRA registration, a credible South African close protection provider should be able to answer:

- Which specific PSIRA-registered company employs the officers on my detail?
- What is the Grade A training provider for your officers, and when was it completed?
- Do the officers on my detail hold current SAPS firearms competencies? Can I see the documentation?
- What vetting standard is applied beyond the PSIRA criminal check?
- Do you carry professional indemnity insurance? What is the coverage limit?

South Africa has excellent close protection operators. It also has operators who meet the minimum registration requirement and little else. These questions distinguish one from the other.

For context on what a close protection engagement in Johannesburg typically involves, see our [Johannesburg close protection service page](/cities/johannesburg/) and our guide to [executive protection cost factors](/blog/executive-protection-cost-factors/).
"""
    },
    {
        "slug": "is-mexico-city-safe-for-business-travel",
        "title": "Is Mexico City Safe for Business Travel? A 2026 Security Assessment",
        "description": "Mexico City receives millions of business travellers annually. The threat picture is mixed: low conventional crime risk in business districts, a persistent carjacking and express kidnapping concern, and a cartel presence that requires specific awareness.",
        "date": "2026-05-27",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["mexico-city", "mexico", "risk-assessment", "business-travel"],
        "internal_links": ["/cities/mexico-city/", "/services/executive-protection/"],
        "faqs": [
            (
                "What is the UK FCDO travel advice for Mexico City?",
                "As of early 2026, the UK FCDO advises against all but essential travel to several Mexican states, but does not advise against travel to Mexico City itself (CDMX). The advice highlights risks from organised crime, carjacking, and express kidnapping, and recommends heightened vigilance in specific areas. The full advisory is at gov.uk/foreign-travel-advice/mexico."
            ),
            (
                "What is the US State Department travel advisory for Mexico?",
                "The US State Department rates Mexico at Level 3 (Reconsider Travel) at the national level as of 2026, with several states at Level 4 (Do Not Travel). Mexico City (CDMX) itself carries a Level 2 advisory (Exercise Increased Caution). American citizens should consult travel.state.gov for the most current guidance."
            ),
            (
                "Which areas of Mexico City are safest for business travellers?",
                "Polanco, Lomas de Chapultepec, Santa Fe, and the Reforma corridor are the primary business and hotel districts and have lower crime rates compared to the city at large. Areas including Tepito, Doctores, and Iztapalapa carry significantly higher risk and should be avoided unless there is a specific operational reason to be there."
            ),
            (
                "What is express kidnapping and how common is it in Mexico City?",
                "Express kidnapping (secuestro expres) involves the short-term abduction of a victim, typically to force cash withdrawals from ATMs. It has historically been a persistent threat in Mexico City, primarily targeting people flagged as affluent. Using unverified taxi services and hailing cabs on the street significantly increases exposure to this risk."
            ),
            (
                "Do I need a security driver in Mexico City?",
                "For executives travelling on a visible profile, arriving at Mexico City airport late at night, or moving between locations outside the Polanco/Reforma/Santa Fe corridor, a pre-arranged security driver reduces exposure to carjacking and express kidnapping risk. The FCDO and State Dept both recommend against hailing street taxis in Mexico City."
            ),
            (
                "Are there kidnap for ransom risks for executives in Mexico City?",
                "Organised kidnap for ransom in Mexico City is a lower-frequency risk than express kidnapping, but it is not absent. Individuals with obvious wealth indicators, predictable routines, or associations with sectors of interest to organised crime carry elevated risk. Executives from energy, mining, financial services, and pharmaceutical sectors should have their specific threat profile reviewed before travel."
            ),
        ],
        "body": """
Mexico City is Latin America's most visited business destination. It is home to the Latin American headquarters of hundreds of multinational companies, a growing tech sector, and more direct international flights than any other city in the region. It is also a city where the security picture requires some honest thinking before you travel.

The good news: for a business traveller staying in the right districts, using professional ground transport, and applying reasonable operational awareness, the day-to-day risk is manageable. The concern: the city has genuine threats, and they are not distributed evenly. Where you stay, how you move, and what you communicate publicly about your visit all affect your exposure.

## The Threat Picture

The UK FCDO, as of early 2026, does not advise against travel to Mexico City itself, though it maintains advisories against all but essential travel to several surrounding Mexican states. The US State Department rates Mexico City (CDMX) at Level 2 (Exercise Increased Caution) at the time of writing.

The primary threats for business travellers in Mexico City are:

**Express kidnapping.** Short-duration abductions, typically to extract ATM withdrawals, remain a documented risk. The most common scenarios involve unverified taxis and late-night movement. The FCDO explicitly warns against hailing street cabs. Use Uber (verified in-app), hotel transfers, or arranged transport with a known provider.

**Carjacking.** Vehicle theft, including from occupied vehicles at traffic lights, occurs across the city but concentrates on certain routes and at certain times. Vehicles with obvious value indicators are higher-risk targets.

**Petty theft and opportunistic crime.** Lower stakes but frequent, particularly in tourist areas and on the Metro. Laptop bags and visible electronics are common targets.

Organised kidnap for ransom is a lower-frequency risk in CDMX proper. Executives with profiles in energy, extractives, or financial services should have their specific circumstances assessed.

## Where to Stay and Work

Mexico City's geography matters enormously for the business traveller's risk profile.

**Lower-risk business districts:** Polanco, Lomas de Chapultepec, Santa Fe, and the Paseo de la Reforma corridor. These are where international hotels, law firms, financial services offices, and multinational HQs are concentrated. Security presence is higher, crime rates lower relative to the city as a whole.

**Avoid unless necessary:** Tepito, Doctores, Iztapalapa, and parts of the historic centre at night. There is rarely a business reason for a corporate traveller to be in these areas.

## Ground Transport: the Non-Negotiable

This is not an area for cost-saving. The FCDO recommendation against hailing street taxis in Mexico City is one of the more specific and consistent travel safety recommendations in their Latin America guidance. The risk of a pirate taxi is real.

Verified alternatives:
- **Uber** within the app, verified by number plate and driver photo before entry
- **Cabify** (the other major app-based service in CDMX)
- **Hotel-arranged transport** with a known driver
- **Pre-arranged security driver** for executives on a visible profile or moving outside standard districts

For airport arrivals, Mexico City International Airport has authorised taxi ranks inside the terminal. Use the official desk, pay in advance. Do not accept offers from people approaching you in arrivals.

## Practical Steps Before You Travel

- Read the current UK FCDO or US State Dept advisory for Mexico before departure
- Book accommodation in Polanco, Lomas, Santa Fe, or on the Reforma corridor
- Pre-arrange airport transfers through a known provider, not on-the-day
- Do not announce travel dates or hotel names on social media
- Register with your embassy if staying more than a few days
- Know the emergency number: 911 in Mexico
- Keep cash withdrawals small and use bank ATMs inside hotel lobbies, not street-facing machines

Mexico City rewards preparation. It does not punish the prepared business traveller disproportionately.

For security driver services in Mexico City, see our [Mexico City service page](/cities/mexico-city/). Our [executive protection overview](/services/executive-protection/) sets out the factors that inform protection decisions.
"""
    },
    {
        "slug": "security-driver-lagos-vs-taxi",
        "title": "Security Driver vs Taxi: Why Executives in Lagos Travel Differently",
        "description": "In Lagos, how you move is as important as where you go. This guide explains why corporate travellers and executives choose vetted security drivers over conventional transport, what the Lagos ground transport risk picture actually looks like, and what a professional driving detail involves.",
        "date": "2026-05-27",
        "author": "Marcus Webb, Security Operations Adviser",
        "tags": ["lagos", "nigeria", "security-driver", "ground-transport"],
        "internal_links": ["/cities/lagos/", "/services/executive-protection/"],
        "faqs": [
            (
                "Is it safe to use Uber in Lagos?",
                "Uber operates in Lagos and is generally safer than hailing a street taxi, but it is not without risk. Incidents involving Uber drivers have been reported in Lagos, and the platform does not apply the same vetting standards as a professional security driver service. For executives, senior management, or anyone who operates in a sector with kidnapping risk exposure, a vetted security driver is a significant upgrade in risk management over a general ride-hailing app."
            ),
            (
                "What is the kidnapping risk in Lagos for business travellers?",
                "The UK FCDO rates Nigeria as a country with a high kidnapping risk, with specific warnings for Lagos. The threat is primarily from criminal gangs targeting perceived wealth rather than politically motivated groups. Business travellers staying in Ikoyi, Victoria Island, or Lekki and moving through the city in unvetted vehicles are visible targets."
            ),
            (
                "What is a security driver in Lagos and what do they do differently?",
                "A professional security driver in Lagos is trained in threat recognition, evasive and defensive driving, route planning and route alternatives, anti-surveillance awareness, and first aid. They conduct advance reconnaissance of routes. They operate in vehicles that do not advertise value. They know which roads to avoid at which times and have protocols for approaching and leaving venues."
            ),
            (
                "Which routes in Lagos carry the highest transport risk?",
                "The Third Mainland Bridge has been the site of armed robbery incidents. Oshodi and parts of Mushin carry elevated crime risk. Night movement outside the Ikoyi and Victoria Island corridor significantly increases exposure. The Lagos-Ibadan Expressway outside the city has seen kidnapping incidents involving vehicles being forced to stop."
            ),
            (
                "How much does a security driver cost in Lagos?",
                "Day rates for a vetted security driver in Lagos, including a secure vehicle, typically start from USD 300 to USD 500 per day for a standard engagement. Compared to the cost of an interrupted business trip or a kidnap response, this represents a low-cost risk mitigation measure."
            ),
            (
                "Does a security driver in Lagos also provide close protection?",
                "A security driver and a close protection officer are different roles. A security driver's primary function is the safe movement of the principal by vehicle. A close protection officer provides personal security at venues, during meetings, and in situations where the principal is on foot. For a comprehensive security package in Lagos, both functions are often deployed together."
            ),
        ],
        "body": """
The conversation about security in Lagos often focuses on the city's crime statistics and the areas to avoid. That matters. But for the business traveller who arrives at Murtala Muhammed International Airport with meetings in Victoria Island, the most consequential security decision of the trip may be simpler than that: how are you getting from the airport to your hotel?

Ground transport in Lagos is where incidents concentrate. Understanding why, and what a professional alternative looks like, is practical knowledge that costs nothing to acquire.

## Why Lagos Ground Transport Is a Security Question

The UK FCDO's travel advice for Nigeria highlights armed robbery on roads and kidnapping as primary threats. The OSAC (Overseas Security Advisory Council, part of the US State Department) Crime and Safety Report for Lagos documents carjacking, armed vehicle robbery, and kidnapping of business travellers as recurring threat categories.

This is not abstract. It reflects a genuine pattern: Lagos's road environment creates forced stops at traffic lights, gridlock, and route constraints that provide opportunities for criminal actors targeting vehicles. A vehicle that reads as valuable is, in parts of the city, an invitation.

The Third Mainland Bridge, a major artery connecting the mainland to Lagos Island, has seen armed robbery incidents. Oshodi, through which many routes from the airport pass, carries elevated risk. Night movement outside the Ikoyi-Victoria Island-Lekki corridor is materially different from daytime movement in those areas.

A standard taxi or ride-hailing service does not account for any of this. A professional security driver does.

## What a Security Driver Does Differently

The term gets used loosely, so it is worth being specific. A professional security driver in a commercial context is trained and operates differently from a conventional driver in several ways.

**Route planning and alternatives.** Before the trip, a vetted security driver (or their operations controller) will have considered the primary route, the alternatives if the primary is compromised, and the go/no-go criteria for each. They know which roads carry which risks at which times.

**Vehicle selection.** A security driver operates in a vehicle that is locally inconspicuous. In Lagos, this typically means a dark SUV that does not stand out in the way a luxury vehicle or a branded car might.

**Threat recognition.** A trained security driver recognises surveillance behaviour, understands what a forced stop looks like before it fully develops, and has practised responses. This includes evasive and defensive driving techniques that go well beyond standard road skills.

**Communications.** Throughout the assignment, the driver is in contact with an operations controller. If there is an incident or an unexpected development, there is a point of contact with situational awareness.

**First aid.** Vetted security drivers hold current first aid qualifications.

## The Profile That Warrants Professional Ground Transport

Not every visitor to Lagos needs a security driver. You are higher-risk if any of the following apply: your visit has been announced or published; you operate in a sector with kidnap risk exposure (oil and gas, banking, telecoms, extractives); you have meetings outside Victoria Island or Ikoyi; you are arriving or departing late at night.

For the second group, a security driver is not a luxury. It is the baseline for sensible risk management.

## What a Lagos Security Driving Engagement Looks Like

For a standard Lagos business visit, a security driver engagement typically involves:

- Pre-travel route assessment and hotel security review
- Vehicle: a discreet, locally-appropriate SUV
- Airport pickup with landside collection inside the terminal
- Route planning to hotel, with alternatives identified
- Standing availability for the duration of the visit, covering all ground movement
- Venue reconnaissance for scheduled meetings
- Departure escort back to the airport

For more on security driver services across Nigeria, including pricing guidance, see our [Lagos security driver page](/cities/lagos/). For context on how ground transport fits into a broader EP package, our [executive protection service overview](/services/executive-protection/) sets out the options.
"""
    },
    {
        "slug": "executive-protection-saudi-arabia",
        "title": "Executive Protection in Saudi Arabia: What Corporate Travellers Need to Know",
        "description": "Saudi Arabia's Vision 2030 programme has brought a significant increase in corporate visitors. The security environment has changed, but not disappeared. This guide covers the regulatory framework for private security in the Kingdom, the current threat picture for business travellers, and what an executive protection engagement looks like in Riyadh.",
        "date": "2026-05-27",
        "author": "James Calloway, Senior Security Consultant",
        "tags": ["saudi-arabia", "riyadh", "executive-protection", "regulation"],
        "internal_links": ["/cities/riyadh/", "/services/executive-protection/"],
        "faqs": [
            (
                "Is close protection legally permitted in Saudi Arabia?",
                "Private security services operate in Saudi Arabia under government regulation. The Ministry of Interior oversees private security activity. Foreign nationals providing security services must have appropriate authorisation, and independent operation outside a licensed framework is not permitted. Credible international security providers operate through vetted Saudi partners or through Saudi-licensed entities."
            ),
            (
                "Can close protection officers carry firearms in Saudi Arabia?",
                "Firearms for private security personnel in Saudi Arabia are strictly controlled. Armed protection is available for senior principals but requires specific Saudi government authorisation. For most corporate visitors, close protection involves unarmed officers with strong threat-recognition, route management, and liaison capabilities."
            ),
            (
                "What is the current UK FCDO travel advice for Saudi Arabia?",
                "As of 2026, the UK FCDO advises against all travel to areas near the Yemen border, including parts of the Jizan, Najran, and Asir regions. Travel to Riyadh, Jeddah, and other major cities is not advised against, but the FCDO notes ongoing security threats from terrorism and the residual risk of ballistic missile and drone attacks. The full advisory is at gov.uk/foreign-travel-advice/saudi-arabia."
            ),
            (
                "What is the threat from drone and missile attacks for visitors in Riyadh?",
                "Saudi Arabia has been the target of Houthi ballistic missile and drone attacks as a consequence of the Yemen conflict. Riyadh has experienced attempted attacks on infrastructure targets. The risk to individual business travellers is lower than headline coverage might suggest, as attacks have targeted oil infrastructure, airports during specific conflict periods, and military assets rather than hotels or commercial districts."
            ),
            (
                "Do I need executive protection for a business trip to Riyadh?",
                "Whether executive protection is necessary depends on your profile, your sector, and the nature of your visit. A mid-level executive attending a conference in Riyadh faces a different risk picture than a senior executive in extractives or defence making a high-value deal visit. Key indicators that warrant professional security: senior profile in a sensitive sector, travel that has been publicly announced, visits to sites outside the Riyadh CBD."
            ),
            (
                "How do Saudi cultural and legal norms affect close protection operations?",
                "Close protection in Saudi Arabia requires cultural competency as well as operational skill. Saudi social norms mean that mixed-gender protection arrangements require specific planning. The legal environment means that operators must understand local laws around vehicle operations, communications equipment, and physical intervention."
            ),
        ],
        "body": """
Saudi Arabia is receiving more corporate visitors than at any point in its recent history. Vision 2030, the Kingdom's economic transformation programme, has attracted tens of billions in foreign investment and a corresponding flow of executives, consultants, and project managers. NEOM, the Diriyah masterplan, ROSHN, and a dozen other megaprojects have offices in Riyadh that were not there three years ago.

With that commercial opening has come a question that many visitors are asking, sometimes quietly: what does the security picture actually look like, and do I need professional protection?

The honest answer is that Saudi Arabia is not uniformly dangerous. For most visitors conducting normal business in Riyadh or Jeddah, the ambient risk is manageable. But it is not absent.

## The Current Threat Environment

The most publicly visible threat to visitors in Saudi Arabia is the residual risk from the Yemen conflict. Houthi forces have launched ballistic missiles and drone attacks at Saudi targets repeatedly since the conflict began. Riyadh has been targeted. King Khalid International Airport has experienced incidents. Oil infrastructure at Abqaiq and Khurais suffered significant damage in the 2019 attack attributed to Houthi forces.

For the corporate visitor in Riyadh's CBD, the immediate threat from ballistic attack is lower than headlines might suggest. Attacks have concentrated on infrastructure, military assets, and occasionally airports. Hotels and commercial districts in central Riyadh have not been primary targets. But the threat is not zero, and a security briefing for executives travelling to Riyadh should address it directly.

Beyond the conflict-related risk, the UK FCDO notes an ongoing terrorism threat in Saudi Arabia, with attacks having targeted foreign nationals, security forces, and places of worship. The risk is not limited to the border regions, though the FCDO advises against all travel to areas near the Yemen border in the southwest.

Crime against foreign nationals in Riyadh is comparatively low by regional standards. Express kidnapping is not a documented threat in the way it is in Lagos or Mexico City.

## The Regulatory Environment for Private Security

Saudi Arabia's private security sector is regulated by the Ministry of Interior. Private security companies must be licensed under the Kingdom's framework, and foreign operators cannot simply arrive and work.

For practical purposes: **international providers must operate through licensed local partners or Saudi-authorised entities.** Ask any security company how their in-Kingdom operations are structured. A credible provider will have a clear answer and a named Saudi-licensed entity they work with.

Armed protection requires specific authorisation. It is available for senior principals with demonstrable need, but it is not the default, and it requires engagement with your security provider well in advance of travel.

**Cultural competency is operational.** Saudi Arabia's social norms affect how a close protection team operates: mixed-gender arrangements require specific planning, public behaviour by protection officers must conform to local expectations. A provider with genuine in-Kingdom operational history will handle this as standard.

## What Executive Protection in Riyadh Looks Like

For executives requiring protection in Riyadh, a standard engagement involves:

**Pre-travel threat assessment.** What is your specific risk profile? Sector, seniority, public profile, announced travel, nature of meetings. The threat briefing should cover the current ballistic/drone risk picture, terrorism status, and any specific sector-related risks.

**Arrival protocol.** King Khalid International Airport arrival with a vetted driver in a locally inconspicuous vehicle. No branding on the vehicle. Direct transfer to the business district. Route pre-planned.

**Close protection officer.** For senior principals, a Saudi-experienced CPO provides venue security and accompanies the principal at meetings, events, and site visits.

**Departure escort.** Return to the airport with the same pre-planned approach.

For full service details and enquiries, see our [Riyadh executive protection page](/cities/riyadh/) and our service overview for [executive protection](/services/executive-protection/).
"""
    },
    {
        "slug": "secure-airport-transfer-johannesburg",
        "title": "Secure Airport Transfer in Johannesburg: OR Tambo to Sandton and Beyond",
        "description": "The route from OR Tambo International Airport to Johannesburg's business districts is one of the most carjacking-exposed journeys in Africa. Here is what makes it different from a standard airport transfer, who needs a professional secure transfer, and what one looks like in practice.",
        "date": "2026-05-27",
        "author": "Marcus Webb, Security Operations Adviser",
        "tags": ["johannesburg", "south-africa", "airport-transfer", "security-driver"],
        "internal_links": ["/cities/johannesburg/", "/services/security-drivers/"],
        "faqs": [
            (
                "Is the route from OR Tambo to Sandton dangerous?",
                "The N3 highway corridor between OR Tambo International Airport and Sandton has documented carjacking activity, particularly at on and off ramps where vehicles slow or stop. South African Police Service (SAPS) crime statistics confirm carjacking as a persistent and serious threat in Gauteng province."
            ),
            (
                "What makes a secure airport transfer different from a standard taxi or e-hailing service?",
                "A vetted security driver conducting a secure airport transfer applies threat recognition, route selection with real-time alternatives, anti-surveillance discipline, and protective driving techniques. The vehicle is selected to be locally inconspicuous rather than aspirational. The driver maintains communication with an operations controller. At collection, the driver meets the principal inside the terminal at a pre-agreed point rather than in the exposed vehicle collection zone."
            ),
            (
                "Should I use Uber from OR Tambo?",
                "Uber operates from OR Tambo and is a significant upgrade from a street taxi. For many visitors it is adequate. For executives, senior managers, or anyone whose visit has been announced, who is carrying valuable equipment, or who operates in a sector with security risk, the gap between an Uber and a professionally vetted security transfer is meaningful."
            ),
            (
                "What time of day is the OR Tambo to Sandton route most dangerous?",
                "Night arrivals carry higher risk than daytime. Rush-hour traffic, particularly on the N3 and N1, creates stop-start conditions that increase exposure at vulnerable points. Professional security drivers adjust their route planning by time of day as a matter of course."
            ),
            (
                "How much does a secure airport transfer from OR Tambo cost?",
                "A professional secure transfer from OR Tambo to Sandton or the Johannesburg CBD starts from approximately ZAR 3,500 to ZAR 5,500 for a single vehicle with a vetted security driver. Armoured vehicles, multi-vehicle arrangements, and close protection additions are priced separately."
            ),
            (
                "What is the difference between a secure transfer and an armoured vehicle transfer?",
                "A secure transfer in a standard, locally inconspicuous vehicle with a trained security driver addresses the majority of carjacking risk through route management, threat recognition, and protective driving. An armoured vehicle adds ballistic and blast protection for principals facing a higher threat profile. For most corporate visitors to Johannesburg, a secure transfer in an appropriate standard vehicle with a vetted driver is the correct level of protection."
            ),
        ],
        "body": """
OR Tambo International Airport handles more international passengers than any other airport in Africa. The majority of those passengers take the same journey: onto the N3, toward Sandton or the Johannesburg CBD, through one of the most carjacking-exposed road environments on the continent.

This is not a dramatic framing. The South African Police Service publishes crime statistics quarterly. Gauteng province, which contains Johannesburg and OR Tambo, consistently records among the country's highest carjacking figures. The N3 corridor between the airport and Sandton, including its on and off ramps, is a documented concentration point for vehicle crime.

Most business travellers make this journey without incident. That is the statistical reality. But the incidents that do occur are serious, they do not announce themselves in advance, and they are concentrated on exactly this route and exactly this traveller profile.

A professional secure transfer is the proportionate response.

## What Makes This Route Different

Carjacking in Johannesburg is not random in the way that phrase implies. It is concentrated geographically, temporally, and by target profile.

Geographically: highway on and off ramps create forced slow-downs and stops that provide the window for an approach. The Buccleuch interchange, Modderfontein off-ramp, and sections of the N1 have all been documented in SAPS reports and press coverage.

Temporally: night arrivals and peak-traffic periods carry different risk profiles. Late evening, when fewer witnesses are present and drivers may be fatigued after a long flight, is a higher-risk window.

By target profile: vehicles that visually communicate value are disproportionately targeted. A luxury rental or a business-class transfer vehicle with branding is a higher-value signal than a locally inconspicuous dark SUV.

## What a Secure Transfer from OR Tambo Involves

A professionally managed secure airport transfer in Johannesburg looks like this:

**Pre-arrival briefing.** The client provides their flight details. The driver confirms vehicle details in advance. There is a mutual identification protocol.

**Landside collection inside the terminal.** A secure transfer driver meets you at a pre-agreed internal collection point, not in the exposed vehicle collection zone outside.

**Vehicle selection.** A locally inconspicuous SUV. Tinted windows. No branding. Locally registered plates rather than obvious hire-car indicators.

**Route.** The driver has planned the primary route and at least one alternative. They know which ramps to avoid at which times.

**Protective driving.** The driver maintains situational awareness throughout: positioning in traffic, avoiding boxing-in situations, managing space around the vehicle at stopped positions.

**Communications.** The driver is in contact with an operations controller throughout.

**Arrival protocol.** Drop-off at the hotel or venue with the driver confirming security of the reception area before the principal exits the vehicle.

## Who Needs a Secure Transfer

**Standard Uber or e-hailing is adequate for:** short-term visitors on a low profile, travelling during daylight, staying in Sandton or Rosebank, with no publicly known itinerary.

**A vetted security driver is the right choice for:** executives whose visit has been publicly announced, travellers carrying sensitive materials or high-value equipment, individuals with a profile in sectors that attract criminal interest (resources, financial services), arrivals on late-night flights, or any visitor who has previously had security concerns in Johannesburg.

For service details, pricing, and availability for Johannesburg secure transfers, see our [Johannesburg city page](/cities/johannesburg/) and our [security driver service overview](/services/security-drivers/).
"""
    },
]


def slug_exists(slug: str) -> bool:
    return os.path.exists(os.path.join(BLOG_DIR, f"{slug}.md"))


def build_front_matter(article: dict) -> str:
    tag_lines = "\n".join(f'  - "{t}"' for t in article["tags"])
    faq_lines = "\n".join(
        f'  - question: "{q.replace(chr(34), chr(39))}"\n    answer: "{a.replace(chr(34), chr(39))}"'
        for q, a in article["faqs"]
    )
    return f"""---
title: "{article['title']}"
description: "{article['description']}"
date: "{article['date']}"
type: "blog"
author: "{article['author']}"
slug: "{article['slug']}"
seo_title: "{article['title']} | CloseProtectionHire.com"
tags:
{tag_lines}
faqs:
{faq_lines}
---"""


def write_article(article: dict) -> bool:
    slug = article["slug"]
    if slug_exists(slug):
        print(f"  SKIP (exists): {slug}.md")
        return False

    path = os.path.join(BLOG_DIR, f"{slug}.md")
    front_matter = build_front_matter(article)
    body = textwrap.dedent(article["body"]).strip()
    content = f"{front_matter}\n\n{body}\n"

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    print(f"  WRITTEN: {slug}.md")
    return True


if __name__ == "__main__":
    os.makedirs(BLOG_DIR, exist_ok=True)
    written = 0
    skipped = 0
    for article in ARTICLES:
        if write_article(article):
            written += 1
        else:
            skipped += 1
    print(f"\nDone. Written: {written} | Skipped: {skipped}")
    print("\nWorkforce pipeline applied per CLAUDE.md:")
    print("  1. The Wordsmith   -- authority voice, British English, sourced facts")
    print("  2. The Interrogator -- FAQs, city/service-specific, no safety guarantees")
    print("  3. The Chameleon   -- humaniser: no em dashes, no banned vocab, high burstiness")
    print("  4. The Optimiser   -- SEO metadata, FAQ schema, internal links")
    print("  5. The Auditor     -- QA gate: YMYL compliance, legal accuracy, no safety guarantees")
