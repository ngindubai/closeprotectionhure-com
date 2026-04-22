#!/usr/bin/env python3
"""Stage 2G: Generate event-security city pages."""

import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "site", "content", "event-security")
os.makedirs(OUT_DIR, exist_ok=True)

cities = [
    {
        "slug": "dubai",
        "city": "Dubai",
        "country": "United Arab Emirates",
        "risk_level": "low",
        "h1": "Event Security in Dubai",
        "description": "Corporate event security in Dubai. Venue assessment, access control, VIP close protection, and secure transport for conferences, exhibitions, and private functions across Dubai.",
        "cta_text": "Planning a corporate event or conference in Dubai?",
        "components": [
            {"title": "Venue Security Assessment", "description": "Pre-event walkthrough by a locally based security professional. We identify access control vulnerabilities, service entrance risks, emergency exit capacity, and perimeter weaknesses specific to Dubai's venue stock: hotel ballrooms, MICE facilities, outdoor event spaces, and marina venues."},
            {"title": "VIP Close Protection", "description": "Dedicated close protection for keynote speakers, C-suite executives, and high-profile guests. SIRA-licensed operators with experience of Dubai's corporate events circuit, including Dubai Airshow, GITEX, and private investment forums."},
            {"title": "Access Control", "description": "Credentialed entry management with guest verification, ID checking, and vehicle screening. Dubai events attract international visitors and third-party vendors; robust access control is the first line of threat management."},
            {"title": "Secure Transport Coordination", "description": "Coordinated arrivals and departures for VIP attendees with SIRA-licensed security drivers. Applies to hotel-to-venue transfers, airport runs, and multi-venue itineraries."},
            {"title": "Emergency Response Plan", "description": "Written emergency protocols covering medical incidents, security threats, fire evacuation, and crowd incidents. Includes pre-event liaison with Dubai Civil Defence and the event venue's own security team."},
            {"title": "Communications Security", "description": "Dubai's surveillance infrastructure means sensitive business discussions at events require disciplined communications hygiene. Our team provides advisory on communications security for high-sensitivity corporate events."},
        ],
        "faqs": [
            {"question": "Is Dubai a high risk location for corporate events?", "answer": "Physical security risk in Dubai is low by global standards. The risks at Dubai events are more nuanced: communications monitoring, reputational exposure for high-profile attendees, legal compliance for international guests, and the operational complexity of managing large-scale MICE events in a city with strict regulatory requirements. Our event security in Dubai focuses on these specific risk categories."},
            {"question": "Do event security officers in Dubai need specific licensing?", "answer": "Yes. All security personnel in Dubai require Security Industry Regulatory Agency (SIRA) certification. Working with unlicensed operators creates legal exposure for the event organiser. All operators we work with hold current SIRA registration."},
            {"question": "Can you provide security for GITEX or Dubai Airshow scale events?", "answer": "We handle events across the full size range, from private investment dinners to multi-day conferences. For large-scale events, we coordinate with venue security and local authorities as a standard part of the security plan."},
        ],
        "body": """Dubai hosts some of the world's largest corporate events: GITEX, Arabian Travel Market, Dubai Airshow, Cityscape Global. The events infrastructure is excellent. The physical security risk is low. But event security in Dubai is not a checkbox exercise.

## The specific risks at Dubai events

The primary security considerations at Dubai events are not criminal threats. They are reputational and legal. High-profile executives attending investment forums face business intelligence gathering by competing interests. Communications at sensitive boardroom events may be monitored. International guests unfamiliar with UAE law can inadvertently create legal liability for the event organiser.

For events hosting political figures, senior government officials, or high-net-worth individuals from conflict-adjacent regions, the threat profile changes. Targeting of Israeli or Jewish interests has been noted in the FCDO threat assessment for the UAE. These risks require event-specific assessment rather than generic security provision.

## Our approach in Dubai

We begin with a venue assessment conducted by an operator with current Dubai knowledge. Dubai's event venues range from world-class hotel convention centres with their own security teams to outdoor waterfront spaces with minimal built-in security infrastructure. The gap between them matters.

For the security plan, we focus on access control, VIP protection, and communications security. Transport coordination is standard for any event with senior executive attendees. All operators are SIRA-licensed.

We do not provide generic crowd management. What we provide is security planning informed by the specific threat environment and the specific guest profile of your event.
""",
    },
    {
        "slug": "nairobi",
        "city": "Nairobi",
        "country": "Kenya",
        "risk_level": "high",
        "h1": "Event Security in Nairobi",
        "description": "Event security for corporate conferences, summits, and private functions in Nairobi. Venue assessment, armed close protection, access control, and emergency planning for Nairobi's high-risk environment.",
        "cta_text": "Running a corporate event in Nairobi? Security planning is not optional here.",
        "components": [
            {"title": "Pre-Event Threat Assessment", "description": "Current threat intelligence for your event dates in Nairobi. Al-Shabaab maintains the capability to conduct attacks in Nairobi, and the FCDO advisory reflects this. Our assessment covers the current threat level, specific venue risk, and any event-specific factors (political sensitivity, high-profile attendees, event publicity)."},
            {"title": "Venue Security Assessment", "description": "Physical assessment of the venue covering perimeter security, service access, vehicle screening capacity, emergency exits, and blast standoff where relevant. Kenya's history of mass-casualty attacks (Westgate, DusitD2) means the venue selection decision itself carries security implications."},
            {"title": "Armed Close Protection", "description": "Licensed armed close protection for executives and high-risk principals. Kenya allows armed private security for appropriate threat levels. Our vetted operators hold valid Kenya Security Industry Authority (KSIA) licensing and firearms permits."},
            {"title": "Access Control and Screening", "description": "Credentialed entry management with ID verification and bag search. For high-profile events, this includes vehicle undercarriage checks and electronic screening at the perimeter."},
            {"title": "Emergency Response and Evacuation", "description": "Written emergency protocols and rehearsed evacuation routes. Nairobi's emergency services response times are variable. A self-sufficient emergency response capability is part of every security plan we produce for Nairobi events."},
            {"title": "Liaison with Kenyan Authorities", "description": "Pre-event engagement with Nairobi police and Kenya's Anti-Terrorism Police Unit (ATPU) where warranted by the event profile. High-profile international events may qualify for additional police support through formal channels."},
        ],
        "faqs": [
            {"question": "What is the realistic security risk at corporate events in Nairobi?", "answer": "Nairobi has experienced major terrorist attacks targeting locations frequented by expatriates and international business visitors: Westgate shopping centre (2013), DusitD2 hotel complex (2019). The threat from Al-Shabaab is active and current. Alongside terrorism, venue crime, vehicle crime, and carjacking during event transport are significant risks. Security planning for Nairobi events must address all three threat categories."},
            {"question": "Which Nairobi venues are appropriate for high-security events?", "answer": "We assess each venue individually based on your specific event requirements. Generally, venues with controlled perimeters, vehicle standoff capability, and multiple emergency exits score better in security assessments. We do not publish venue recommendations publicly as threat profiles change; we provide venue assessment as part of the security planning process."},
            {"question": "How much advance notice is needed for Nairobi event security?", "answer": "Minimum four weeks for effective security planning in Nairobi. Complex events with multiple principals, large guest counts, or high political sensitivity require six to eight weeks. Last-minute requests are handled but the security plan will be less comprehensive."},
        ],
        "body": """Nairobi is the economic hub of East Africa and a major conference city for development finance, technology, and regional policy. It is also one of the more complex security environments on this platform.

## The security context

Al-Shabaab has demonstrated both the intent and capability to conduct attacks in Nairobi targeting locations associated with international visitors and Western interests. The DusitD2 attack in 2019 killed 21 people at a complex that included offices, a hotel, and a conference facility. Event security planning in Nairobi begins with this baseline.

Street crime, vehicle crime, and carjacking are elevated in Nairobi relative to most conference cities. Event transport, particularly for early-morning or late-evening transfers, requires a security driver, not just a local taxi.

## What effective event security in Nairobi requires

The difference between adequate and inadequate event security in Nairobi is often the quality of the pre-event planning rather than the number of security personnel on the day. A venue that looks suitable from a hospitality perspective may have a service entrance that provides uncontrolled access to the main hall. A guest list that includes government officials from neighbouring countries changes the threat profile.

We produce a written security plan for every Nairobi event engagement. The plan covers venue assessment, access control procedures, principal protection, transport protocols, communications, and emergency response. It is reviewed with the event team before deployment and adjusted as the guest profile and programme evolve.

## Our operators in Nairobi

Operators are KSIA-licensed, locally based, and have operating experience in Nairobi's event and commercial security environment. Where the event profile warrants armed protection, our operators hold valid firearms permits under Kenyan law. We do not contract unlicensed or informally organised security teams regardless of cost pressure.
""",
    },
    {
        "slug": "lagos",
        "city": "Lagos",
        "country": "Nigeria",
        "risk_level": "high",
        "h1": "Event Security in Lagos",
        "description": "Corporate event security in Lagos, Nigeria. Armed protection, venue assessment, and access control for conferences and private functions in Nigeria's commercial capital.",
        "cta_text": "Corporate event in Lagos? Talk to us before you finalise your security plan.",
        "components": [
            {"title": "Pre-Event Risk Briefing", "description": "Current threat assessment for your event dates and location in Lagos. This covers the general security environment, kidnapping risk for high-profile attendees, and any specific threats active at the time of your event."},
            {"title": "Venue Security Assessment", "description": "Physical security assessment of the event venue: perimeter, access points, vehicle screening, emergency exits, and proximity to known risk areas. Lagos venues vary significantly in their baseline security provision."},
            {"title": "Armed Close Protection", "description": "Licensed armed close protection for executives and high-risk principals. Nigeria's security environment justifies armed cover for most high-profile events. Our operators hold valid Nigeria Security and Civil Defence Corps (NSCDC) licensing."},
            {"title": "Access Control", "description": "Managed entry with ID verification and bag search. For events with international guests, this includes a screening process that goes beyond the typical Lagos venue security provision."},
            {"title": "Secure Event Transport", "description": "Security-trained drivers for event transfers including airport pickups, hotel-to-venue runs, and post-event departures. Lagos traffic creates vulnerability windows during transfers that require active management."},
            {"title": "Kidnap Risk Management", "description": "For high-profile events with international executives, kidnapping risk is part of the security calculus in Lagos. We include kidnap risk management protocols in our event security plans for appropriate client profiles."},
        ],
        "faqs": [
            {"question": "How serious is the security risk for events in Lagos?", "answer": "Lagos has one of the higher corporate security risk profiles in Africa. Kidnapping of business executives and high-net-worth individuals is an active threat. Armed robbery and vehicle crime are common. Infrastructure challenges (power, communications) complicate emergency response. These risks do not prevent corporate events from operating successfully in Lagos, but they require a security plan that reflects the actual environment rather than a generic template."},
            {"question": "Do you provide security for oil and gas sector events in Lagos?", "answer": "Yes. Lagos is the operational headquarters for much of Nigeria's oil sector and we have experience of the specific security requirements of energy sector events, including the elevated threat profile for executives from extractive industries in the Niger Delta context."},
            {"question": "Is armed security legally permitted for private events in Nigeria?", "answer": "Yes, with proper licensing. Private security companies and their armed personnel must be registered with the Nigeria Security and Civil Defence Corps. All operators we work with are NSCDC-registered. Unlicensed armed security creates significant legal exposure for event organisers."},
        ],
        "body": """Lagos is Nigeria's commercial capital: home to the Nigerian Stock Exchange, the headquarters of most multinational Nigeria operations, and the country's major port and logistics hub. It is also a city where corporate event security requires substantive planning rather than a nominal security presence.

## The security environment

Kidnapping of business executives and high-net-worth individuals is a documented and active threat in Lagos. The frequency has varied over time, but the risk class is real and insurance underwriters treat it as such. For international executives attending Lagos events, this is the primary threat requiring specific mitigation.

Armed robbery, vehicle crime, and opportunistic crime in areas around major event venues are everyday operational factors. Power outages are common and affect venue security systems as well as communications. These are known, manageable risks, not exceptional ones, but they require a security plan written for Lagos rather than imported from another operating environment.

## Planning an event in Lagos

The security plan for a Lagos event starts with the venue. Not all Lagos venues have equivalent security infrastructure. Access control capability, generator backup, perimeter security, and proximity to police posts all vary. We assess the venue independently of the venue's own security team.

For events with international executive attendees, the security plan includes transport protocols for every transfer from arrival at Murtala Muhammed International to departure. This is not belt-and-braces caution. It reflects the specific risk windows that Lagos creates during vehicle transit.

Our operators in Lagos are NSCDC-licensed, locally based, and have experience of Lagos's corporate events sector. For events requiring armed cover, operators hold valid firearms permits under Nigerian law.
""",
    },
    {
        "slug": "johannesburg",
        "city": "Johannesburg",
        "country": "South Africa",
        "risk_level": "high",
        "h1": "Event Security in Johannesburg",
        "description": "Event security in Johannesburg for conferences, corporate functions, and private events. Venue assessment, armed close protection, and access control in South Africa's business capital.",
        "cta_text": "Event in Johannesburg? Security planning starts with the venue.",
        "components": [
            {"title": "Venue Security Assessment", "description": "Assessment of the event venue covering access control, perimeter security, emergency exits, vehicle access points, and proximity to risk areas. Johannesburg venues in Sandton and the CBD have significantly different security profiles."},
            {"title": "Armed Close Protection", "description": "PSIRA-registered armed close protection for executives and high-profile guests. South Africa has one of the most developed private security industries in the world. We work with operators holding current PSIRA Grade A/B registration and valid firearms competencies."},
            {"title": "Access Control", "description": "Managed entry with ID verification and bag search. For corporate events in Johannesburg, the access control process is a functional requirement rather than a ceremonial one."},
            {"title": "Secure Event Transport", "description": "Security drivers for all event transfers. Carjacking is a specific and common risk in Johannesburg. Transfers during evening hours or to non-central venues require active security management, not ordinary taxi provision."},
            {"title": "Residential and Villa Security", "description": "For events hosted at private properties or executive residences, we provide venue hardening, perimeter security, and gate control. Private event venues in Johannesburg create different security challenges from hotel ballrooms."},
            {"title": "Emergency Response Planning", "description": "Written emergency protocols for medical incidents, security threats, and evacuation. Includes coordination with Netcare 911 or Mediclinic emergency services where appropriate."},
        ],
        "faqs": [
            {"question": "Is Johannesburg too dangerous for international corporate events?", "answer": "No. Johannesburg hosts major international conferences and corporate events routinely. The Sandton convention district has good security infrastructure. The risks are real but manageable with proper planning. The mistake is treating Johannesburg like a lower-risk conference city and applying minimal security provision. With appropriate planning, corporate events run safely."},
            {"question": "What areas of Johannesburg are suitable for corporate events?", "answer": "Sandton remains the primary corporate and conference district with the most developed security infrastructure. Rosebank is a secondary option. Events outside these zones require more detailed security assessment. We do not publish area rankings publicly as threat profiles change; venue-specific assessment is the right approach."},
            {"question": "Is South Africa's private security industry reliable?", "answer": "South Africa has one of the largest and most developed private security industries in the world by ratio of operators to population. The PSIRA regulatory framework is established. The quality varies significantly between operators. Our vetting process focuses on PSIRA registration grade, training records, and references from comparable event assignments."},
        ],
        "body": """Johannesburg is sub-Saharan Africa's largest economy by GDP and one of the continent's primary conference destinations. The Sandton convention district competes with Dubai and Singapore for large-format corporate events. The security environment requires direct engagement rather than reassurance.

## The security profile

South Africa's violent crime statistics are among the most cited in the world. For corporate event planning, the specific risks that matter are carjacking, robbery during transfers, and residential/venue crime for events hosted outside hotel infrastructure. Johannesburg's CBD and Sandton have different risk profiles: events in Sandton benefit from higher private security density and better infrastructure; events in the CBD require more detailed planning.

The organised crime environment in Johannesburg is sophisticated. For events involving significant financial activity, luxury goods, or HNWI clients, this is part of the threat picture.

## Planning for Johannesburg events

Venue selection has security implications that go beyond hospitality quality. A venue with a controlled vehicle access point, operating CCTV, a basement loading dock that can be secured, and proximity to private emergency medical services starts from a better security position than a venue without these characteristics.

Event transport is a specific risk management requirement in Johannesburg, not an optional upgrade. We build transport security into every Johannesburg event plan from the first conversation.

Our operators hold PSIRA Grade A registration as a minimum. For principals requiring armed cover, operators hold valid SAPS-issued firearms competency certificates and licences. We do not work with operators below PSIRA Grade B regardless of cost considerations.
""",
    },
    {
        "slug": "mexico-city",
        "city": "Mexico City",
        "country": "Mexico",
        "risk_level": "high",
        "h1": "Event Security in Mexico City",
        "description": "Corporate event security in Mexico City. Armed close protection, venue assessment, and kidnap risk management for conferences and business events in CDMX.",
        "cta_text": "Planning an event in Mexico City? Kidnap risk management is part of our standard scope here.",
        "components": [
            {"title": "Pre-Event Risk Briefing", "description": "Current threat assessment for your event dates in Mexico City. This covers the general security environment, cartel activity in event-adjacent areas, and kidnapping risk for senior executive attendees. Mexico City's risk profile is not static; conditions vary by colonia and by period."},
            {"title": "Venue Security Assessment", "description": "Physical assessment of the event venue: access control, vehicle screening capability, emergency exits, perimeter, and neighbourhood risk profile. Some Mexico City venues carry local security challenges that venue marketing materials do not mention."},
            {"title": "Armed Close Protection", "description": "Licensed armed close protection from operators certified under Mexico's federal private security regulatory framework (DGSP). Kidnapping risk in Mexico makes armed protection a standard inclusion for executive-level attendees rather than an optional upgrade."},
            {"title": "Access Control", "description": "Credentialed entry management with ID verification. For events with high-profile attendees, this includes vehicle screening and bag search at the venue perimeter."},
            {"title": "Secure Event Transport", "description": "Armoured vehicle options for appropriate threat levels. Mexico City event transport requires anti-surveillance awareness and counter-surveillance protocols rather than standard chauffeur service."},
            {"title": "Kidnap Risk Protocols", "description": "Written protocols covering principal tracking, communication security, emergency contact procedures, and response protocols if a principal is missing. This is standard in Mexico, not an exceptional request."},
        ],
        "faqs": [
            {"question": "What is the kidnapping risk at Mexico City corporate events?", "answer": "Mexico City's kidnapping rate is one of the highest in Latin America for business executives. Express kidnappings (short-duration, ransom-focused abductions) are more common than classic kidnappings but both occur. For international executives attending high-profile events, the combination of a known schedule, arrival at an announced venue, and departure at a predictable time creates an exposure window that requires active management."},
            {"question": "Which colonias in Mexico City are appropriate for corporate events?", "answer": "Polanco, Santa Fe, and Lomas de Chapultepec have the most developed corporate event infrastructure and security profile. Events outside these zones require more detailed assessment. We evaluate each venue individually; general area guidance has limits in a city where conditions change."},
            {"question": "Is armoured vehicle protection necessary for Mexico City events?", "answer": "For most senior executives, yes. Standard vehicles are appropriate for limited, low-profile movements within secure corporate districts. For airport transfers, hotel-to-venue runs that pass through mixed areas, or events with publicly announced attendance by named executives, armoured vehicles are the appropriate risk management choice."},
        ],
        "body": """Mexico City is Latin America's largest metropolitan economy and a major conference destination for business, technology, and policy events. It operates at a different point on the risk spectrum from conference cities in Europe or East Asia.

## The security environment

Mexico City's risk profile is driven by organised crime rather than terrorism or civil conflict. Kidnapping, extortion, and vehicle crime are the primary security considerations for corporate event planners. The city's police capability is uneven. Response times in an emergency are not comparable to London or Singapore.

For international executives, the combination of a published event appearance, a fixed venue, and a predictable travel schedule creates the conditions that organised criminal groups can exploit. The mitigation is not to cancel the event but to plan the security specifics: venue choice, transport routes, arrival timing, and principal communication security.

## Planning events in Mexico City

Polanco is the standard corporate event district: developed private security infrastructure, proximity to major international hotels, and a lower ambient crime rate than much of the city. Events in this zone start from a better security position. Events in other parts of the city require specific assessment.

For any event with named senior executives in public attendance, our security plan includes counter-surveillance protocols for transport, limiting public exposure of the event schedule, and kidnap risk management procedures. This is not crisis planning. It is standard operating practice in Mexico City.

Our operators hold valid DGSP federal registration. Where armoured vehicles are required, these are arranged through vetted providers with current mechanical certification. We do not use informal armoured vehicle providers regardless of availability and cost.
""",
    },
    {
        "slug": "bogota",
        "city": "Bogota",
        "country": "Colombia",
        "risk_level": "high",
        "h1": "Event Security in Bogota",
        "description": "Corporate event security in Bogota, Colombia. Kidnap risk management, armed close protection, and venue assessment for conferences and business events in the Colombian capital.",
        "cta_text": "Event in Bogota? Kidnap risk management is built into our scope here.",
        "components": [
            {"title": "Pre-Event Threat Assessment", "description": "Current intelligence on the security environment for your event dates in Bogota. Colombia's security situation has improved significantly since the FARC peace process but active criminal groups and dissident FARC factions maintain kidnapping and extortion capability in and around Bogota."},
            {"title": "Venue Assessment", "description": "Physical and neighbourhood assessment of the event venue. Bogota's security profile varies significantly by zona: Zona Rosa, Chapinero Alto, and the CBD have different risk characteristics. We assess the specific venue rather than offering generic zone guidance."},
            {"title": "Armed Close Protection", "description": "Licensed armed close protection. Colombia's extensive private security industry is regulated by the National Surveillance and Private Security Superintendency (Supervigilancia). Our operators hold valid Supervigilancia certification with firearms accreditation."},
            {"title": "Secure Event Transport", "description": "Security drivers with counter-surveillance training. Bogota's traffic creates significant vulnerability windows during transfers. Airport pickups and hotel-to-venue transfers require active security management."},
            {"title": "Access Control", "description": "Controlled entry with ID verification and bag search. For events with international executives from sectors associated with extortion targeting (mining, energy, finance), access control is a substantive risk management measure."},
            {"title": "Kidnap Risk Protocols", "description": "Standard inclusion for Bogota events with senior executive attendance. Covers principal tracking, communication procedures, emergency response, and liaison with specialist K&R (kidnap and ransom) providers where relevant."},
        ],
        "faqs": [
            {"question": "Has Colombia's security situation improved enough to hold events safely?", "answer": "Yes, significantly. The 2016 FARC peace agreement substantially reduced the terrorism and mass-casualty risk that characterised Colombia through the 1990s and 2000s. Bogota now hosts major international business events. The risk profile has changed: the current environment involves criminal groups, extortion, and opportunistic crime rather than politically motivated mass-casualty attacks. This is a different and more manageable risk category, but it still requires active security planning."},
            {"question": "What sectors face the highest risk at Bogota events?", "answer": "Mining, oil and gas, and financial services executives face higher specific risk in Colombia due to the association of these sectors with extortion targeting by criminal groups. High-net-worth individuals who are publicly identifiable are also at elevated risk. The security plan should reflect the specific profile of the attending executives rather than applying a generic Bogota-wide risk level."},
            {"question": "Which areas of Bogota are suitable for corporate events?", "answer": "Zona Rosa, El Nogal, and Usaquén are the primary corporate event zones in Bogota. These areas have developed private security infrastructure and a relatively lower crime rate compared to other parts of the city. Events south of the city centre require more detailed security assessment."},
        ],
        "body": """Bogota has undergone a genuine security transformation since the FARC peace process. The city that was effectively off the international conference circuit 20 years ago now hosts investment forums, technology conferences, and regional summits. The security environment is manageable. It is not low risk.

## The current environment

Criminal groups including dissident FARC factions and urban criminal organisations maintain active kidnapping and extortion capability in Colombia. Bogota's crime rate, while improved, remains elevated by international standards. The risk to corporate events is primarily from opportunistic targeting of identifiable high-value individuals rather than mass-casualty attacks.

For international executives, the specific risk factors are: public announcement of attendance at a named event, predictable transport routes, and the visibility that comes with being a foreign executive in a Latin American business environment. These risks are manageable with appropriate planning.

## Planning for Bogota

The corporate event zones in Bogota (Zona Rosa, El Nogal, Chapinero Alto) have relatively good security infrastructure. Outside these zones, assessment becomes more important.

Transport security is the single most important element of a Bogota event security plan. The transfer from El Dorado airport to the hotel, and the daily hotel-to-venue run, are the primary vulnerability windows. Our security drivers hold Supervigilancia certification and operate with counter-surveillance awareness as a standard practice.

For events with named senior executive attendance, we include kidnap risk protocols in the standard security plan. This reflects the operational environment, not exceptional circumstances.
""",
    },
    {
        "slug": "istanbul",
        "city": "Istanbul",
        "country": "Turkey",
        "risk_level": "high",
        "h1": "Event Security in Istanbul",
        "description": "Event security in Istanbul for corporate conferences, private functions, and multi-day summits. Terrorism risk management, armed close protection, and venue assessment.",
        "cta_text": "Corporate event in Istanbul? Terrorism risk assessment is part of our standard scope.",
        "components": [
            {"title": "Terrorism Risk Assessment", "description": "Istanbul has a documented history of mass-casualty terrorist attacks. Our pre-event threat assessment covers current FCDO and State Dept advisories, active threat group capability, and specific risk factors for your event dates and venue."},
            {"title": "Venue Security Assessment", "description": "Physical assessment covering blast standoff, access control hardening, emergency exits, vehicle exclusion zones, and proximity to previous attack sites or current risk areas. Istanbul's European and Asian sides have different risk profiles."},
            {"title": "Armed Close Protection", "description": "Licensed armed close protection from operators holding valid ÖZEL GÜVENLIK certification under Turkey's Private Security Law (Law 5188). Armed protection is appropriate for the Istanbul threat environment for high-profile principal attendance."},
            {"title": "Access Control and Screening", "description": "Bag search and ID verification at the event perimeter. For events where the guest profile or event subject matter creates elevated risk, vehicle screening and electronic detection are included."},
            {"title": "Secure Event Transport", "description": "Security drivers with Istanbul operational knowledge. The city's geography (Bosphorus crossing points, traffic concentration) creates specific transport planning considerations. Counter-surveillance protocols are standard for principal transport."},
            {"title": "Emergency Response Plan", "description": "Written emergency protocols including evacuation plans, medical response, and communication procedures. Istanbul's emergency services are generally capable; the plan supplements rather than replaces them."},
        ],
        "faqs": [
            {"question": "What is the terrorism risk at Istanbul events?", "answer": "Istanbul has experienced multiple significant terrorist attacks including the 2016 Ataturk Airport attack (45 dead), the 2016 Reina nightclub attack (39 dead), and multiple bomb attacks in tourist and commercial districts. Both PKK/TAK and ISIS have conducted attacks in Istanbul. The FCDO terrorism advisory for Turkey is SEVERE. This does not mean events cannot be held safely, but it does mean the threat must be addressed in the security plan rather than assumed to be background noise."},
            {"question": "Which Istanbul venues have the best security infrastructure?", "answer": "Istanbul's five-star hotel convention centres in Nisantasi, Levent, and Besiktas have reasonably developed security infrastructure. Events in these venues benefit from existing CCTV, controlled vehicle access, and professional venue security teams. We assess each venue independently; general hotel ratings are not a proxy for security provision."},
            {"question": "Do I need armed security for a business conference in Istanbul?", "answer": "For most corporate conferences with no specific threat indicators, the standard provision is professionally trained unarmed security with access control, venue assessment, and emergency planning. Armed close protection is recommended for individually identified high-risk principals (senior government officials, executives with specific threat history, HNWI clients with publicly known wealth). We make this assessment on a case-by-case basis."},
        ],
        "body": """Istanbul is a major European-Asian conference city: the gateway between Europe and the Middle East for investment, energy, and policy events. It is also on the FCDO SEVERE terrorism advisory.

## The security environment

Turkey faces active terrorist threats from PKK/TAK (Kurdistan Workers' Party affiliate) and residual ISIS capability. Istanbul has been hit by both. The Reina nightclub attack in 2017 killed 39 people at a location that was hosting a New Year's event. The Ataturk Airport attack in 2016 killed 45. These are not historical footnotes; they inform current security planning.

The threat environment in Istanbul is not so high that corporate events cannot operate. Turkish security forces have disrupted multiple planned attacks. The city's security infrastructure has been upgraded significantly since 2016. But the terrorism risk is real and must be addressed directly in the security plan.

## What event security in Istanbul covers

Venue selection matters more in Istanbul than in most European cities. A venue with controlled vehicle access, blast standoff from the street, and managed perimeter is not just better hospitality. It is better security.

Access control at Istanbul events should include bag search as a minimum. For events where the subject matter, attending officials, or guest profile creates elevated risk, additional screening is appropriate. We make this assessment in the context of the specific event.

Transport security in Istanbul involves counter-surveillance as a standard practice for principal protection. The city's geography creates predictable choke points (Bosphorus bridges, motorway access) that are part of any professional route planning process.

Our operators hold valid ÖZEL GÜVENLIK certification under Turkish law. All security plans are reviewed against current FCDO and State Dept advisory guidance.
""",
    },
    {
        "slug": "mumbai",
        "city": "Mumbai",
        "country": "India",
        "risk_level": "medium",
        "h1": "Event Security in Mumbai",
        "description": "Corporate event security in Mumbai for business conferences, investor summits, and private functions. Terrorism risk management, VIP protection, and access control in India's financial capital.",
        "cta_text": "Planning a corporate event or investor summit in Mumbai?",
        "components": [
            {"title": "Terrorism Risk Assessment", "description": "The 2008 Mumbai attacks (26/11) remain the reference point for event security planning in the city. Current threat indicators, FCDO advisory status, and event-specific risk factors form the basis of our pre-event assessment."},
            {"title": "Venue Security Assessment", "description": "Physical assessment of the event venue covering access control, perimeter security, emergency exits, and proximity to risk areas. Mumbai's five-star hotel stock was directly targeted in 2008; security upgrades since then vary significantly between properties."},
            {"title": "VIP and Executive Protection", "description": "Close protection for senior executives, government officials, and HNWI clients. Mumbai hosts significant investor and financial sector events; the attendee profile often includes individuals with specific security requirements."},
            {"title": "Access Control", "description": "Credentialed entry with ID verification and bag search. Mumbai's major conference venues have their own security teams; our service supplements and coordinates with venue provision rather than replacing it."},
            {"title": "Secure Event Transport", "description": "Security drivers for principal transport. Mumbai traffic is among the densest in Asia; transfers require route planning and time management that goes beyond standard chauffeur service."},
            {"title": "Emergency Response Planning", "description": "Written emergency protocols covering medical incidents, security threats, and evacuation. Mumbai has capable private emergency medical providers. We include specific coordination with Breach Candy Hospital or Lilavati Hospital as standard depending on venue proximity."},
        ],
        "faqs": [
            {"question": "How has Mumbai's security changed since the 2008 attacks?", "answer": "The 2008 attacks prompted significant investment in Mumbai's security infrastructure. Major hotels have upgraded vehicle screening, access control, and emergency response capability. The NSG counter-terrorism unit's response protocols have been revised. The current terrorism threat is present but the immediate response capability has improved. That said, the threat environment across the broader South Asia region remains elevated."},
            {"question": "What is the civil unrest risk for events in Mumbai?", "answer": "Communal tensions periodically affect Mumbai, particularly around religious festivals or specific political events. Our pre-event assessment includes current civil unrest indicators. This rarely affects corporate conference security materially but can affect transport routes and event timing decisions."},
            {"question": "Is armed protection available in Mumbai?", "answer": "Armed close protection requires specific licensing under Indian law. Foreign nationals face particular complexity obtaining arms licences. We work with licensed Indian private security companies that have the necessary permissions. For most corporate conferences, professionally trained unarmed close protection with access control is the standard and appropriate provision."},
        ],
        "body": """Mumbai is India's financial capital and the primary destination for international investor conferences, financial services events, and corporate summits. It is a sophisticated, complex city with a security environment that rewards specific planning rather than generic reassurance.

## The security context

The 2008 attacks on the Taj Mahal Palace hotel, Oberoi Trident, and Chhatrapati Shivaji Terminus killed 166 people. Mumbai's corporate conference circuit includes multiple hotels that were directly affected. Since 2008, the city's major event venues have made substantive security investments. The quality of those investments varies.

The current terrorism threat in Mumbai is assessed as lower than the pre-2008 period in terms of immediate mass-casualty risk. India's counter-terrorism capability has been significantly enhanced. However, the regional environment (India-Pakistan tensions, cross-border terrorism) means the threat class remains present.

## Event security in practice

Mumbai's major corporate event venues are predominantly five-star hotel convention centres: the Taj Mahal Palace, the Oberoi Trident, the Grand Hyatt, and others. These venues have their own security teams. Our role is to assess, supplement, and coordinate rather than to replace venue security provision.

For events with specifically identified high-risk principals (government officials, executives with personal threat histories, HNWI clients from conflict-proximate regions), we provide dedicated close protection that operates alongside venue security.

Transport in Mumbai is a specific planning challenge. Traffic density is extreme. Route planning, departure time management, and communication between security drivers and venue security are essential elements of the transport plan.
""",
    },
    {
        "slug": "bangkok",
        "city": "Bangkok",
        "country": "Thailand",
        "risk_level": "medium",
        "h1": "Event Security in Bangkok",
        "description": "Corporate event security in Bangkok for regional conferences, private functions, and investor summits. Venue assessment, VIP protection, and anti-scam intelligence for events in Thailand's capital.",
        "cta_text": "Running a regional conference or corporate event in Bangkok?",
        "components": [
            {"title": "Venue Security Assessment", "description": "Physical assessment of the Bangkok event venue. Thailand's major hotels and conference centres have variable security infrastructure. Venues in Sukhumvit, Silom, and Ploenchit have different risk profiles from venues elsewhere in the city."},
            {"title": "VIP Close Protection", "description": "Discreet close protection for senior executives and HNWI clients. Bangkok's corporate event circuit includes significant financial services, real estate, and cryptocurrency sector events. The attendee profile often includes individuals with specific privacy or security requirements."},
            {"title": "Fraud and Scam Intelligence", "description": "Bangkok is an active centre for sophisticated fraud targeting corporate executives: pig butchering scams, investment fraud, and business meeting fraud. Our pre-event briefing includes intelligence on current active scam operations and how to protect event delegates."},
            {"title": "Access Control", "description": "Credentialed entry management. Useful particularly for events in the financial sector where competitor intelligence gathering is an active concern."},
            {"title": "Anti-Surveillance", "description": "Counter-surveillance for high-profile principals. Bangkok's surveillance environment has become more sophisticated. Principals carrying sensitive business information should assume the possibility of monitoring."},
            {"title": "Emergency Response", "description": "Emergency planning covering medical incidents (Bangkok's private hospital infrastructure is excellent), security incidents, and evacuation. Bumrungrad International and Bangkok Hospital are reference providers."},
        ],
        "faqs": [
            {"question": "What is the primary security risk at corporate events in Bangkok?", "answer": "Terrorism risk is lower in Bangkok than in most cities in this region. The primary risks at corporate events are fraud and intelligence gathering targeting executives, opportunistic crime around event venues, and road safety during event transport. Bangkok has specific fraud exposure: the city is a major hub for sophisticated scam operations targeting financial sector executives and investors."},
            {"question": "How does civil unrest affect events in Bangkok?", "answer": "Thailand experiences periodic political unrest and has had multiple government changes since 2006, some involving street-level protests and military intervention. Our pre-event assessment includes current political risk indicators. Most corporate events are not affected by Bangkok's political cycle, but the risk of unexpected disruption to event transport or access routes is real and addressed in our planning."},
            {"question": "Is Bangkok appropriate for high-security or sensitive corporate meetings?", "answer": "Bangkok is used extensively for discreet corporate meetings, particularly for Southeast Asian regional business. The city offers good operational security for low-profile events if the right precautions are taken. For highly sensitive meetings, communications security and counter-surveillance are part of the security plan."},
        ],
        "body": """Bangkok is one of Asia's primary corporate event destinations: the regional hub for Southeast Asian business, a conference city for financial services, technology, and real estate sectors. The security environment is less extreme than other cities on this platform but has specific characteristics that require active planning.

## The security context

Bangkok's terrorism risk is lower than Istanbul, Nairobi, or Mexico City. The city's last significant terrorist attack was the 2015 Erawan shrine bombing, which killed 20 people at a tourist location. Subsequent attacks have been smaller. This is not a low-risk terrorism environment but the frequency of mass-casualty incidents is lower than in several other cities where major conferences are held.

The more specific risks at Bangkok corporate events are fraud-related. Bangkok is one of the world's leading centres for sophisticated investment fraud targeting corporate executives. Pig butchering scams, fake investment platforms, and business meeting fraud have targeted foreign executives attending events in Thailand. These are not street crimes. They are carefully constructed operations that can begin at a corporate event.

## Planning Bangkok events

Bangkok's five-star hotel convention circuit (the Anantara, the Mandarin Oriental, the St. Regis, the Conrad) has reasonable base security infrastructure. Our pre-event assessment evaluates each venue individually.

For events in the financial services, cryptocurrency, or real estate sectors, our security plan includes a fraud intelligence briefing for event staff and senior attendees. The financial cost of fraud at a Bangkok business event can exceed the physical security cost of a crime incident.

Transport security in Bangkok involves managing the city's exceptional traffic density. Sukhumvit, the primary corporate district, can be effectively gridlocked during peak hours. Route planning and timing are genuine risk management elements.
""",
    },
    {
        "slug": "london",
        "city": "London",
        "country": "United Kingdom",
        "risk_level": "medium",
        "h1": "Event Security in London",
        "description": "Corporate event security in London for conferences, product launches, and private functions. Terrorism-aware venue assessment, SIA-licensed close protection, and access control from vetted operators.",
        "cta_text": "Planning a high-profile event or product launch in London?",
        "components": [
            {"title": "Terrorism-Aware Venue Assessment", "description": "The FCDO terrorism threat level for the UK is SEVERE. Our venue assessment reviews vehicle exclusion, blast standoff from the street, access control hardening, and emergency evacuation. These are not hypothetical considerations in London."},
            {"title": "SIA-Licensed Close Protection", "description": "All close protection officers hold current Security Industry Authority (SIA) close protection licences. This is a legal requirement in the UK. We do not work with unlicensed operators."},
            {"title": "Access Control", "description": "Credentialed entry management with ID verification. For high-profile events, this includes vehicle screening and electronic detection. London's corporate event security standards are well-developed; we work within established frameworks."},
            {"title": "Counter-Terrorism Awareness", "description": "Event staff briefings on recognising suspicious activity, vehicle exclusion management, and emergency response procedures. Martyn's Law (Protect Duty) may apply to your event; we advise on compliance requirements."},
            {"title": "Secure Event Transport", "description": "SIA-licensed security drivers for VIP and executive transfers. London event transport includes awareness of current police operations, protest routing, and access restrictions."},
            {"title": "Protest and Disruption Management", "description": "London is an active city for organised protest. For events on politically sensitive subjects, we assess protest risk and provide crowd management capability that complies with UK public order law."},
        ],
        "faqs": [
            {"question": "What is Martyn's Law and does it apply to my event?", "answer": "Martyn's Law (the Terrorism (Protection of Premises) Bill) is UK legislation requiring specified venues and events to implement protective security measures. At the time of writing it is working through parliament. Larger events and venues will have specific compliance obligations. We advise clients on current requirements and upcoming legislative changes as part of our London event security scope."},
            {"question": "Is armed security available for London events?", "answer": "Firearms are prohibited for private security in the UK. All close protection in London is unarmed. This is the legal requirement and the appropriate provision for London's threat environment. Armed police can be requested through police liaison for specific threat profiles."},
            {"question": "How does the UK terrorism threat level affect event planning?", "answer": "The UK maintains a SEVERE terrorism threat level. For event planning, this means vehicle exclusion, controlled access, and staff counter-terrorism training are appropriate for any public-facing event with significant attendance. For events at lower risk levels, the practical impact on security planning is proportionate. We calibrate the security plan to the specific event profile rather than applying the national threat level uniformly."},
        ],
        "body": """London is one of the world's leading corporate event cities: home to a professional-grade events infrastructure, an established private security industry, and a regulatory framework that is among the most developed globally.

## The security environment

The UK terrorism threat level is SEVERE, meaning an attack is judged highly likely. London has experienced multiple significant attacks: Westminster Bridge (2017), London Bridge and Borough Market (2017), Manchester Arena (2017). The current threat comes primarily from Islamist extremism and lone actor attacks. This is the backdrop against which London events are planned.

The specific risk to corporate events is lower than the national threat level implies for most events. The vast majority of London corporate conferences proceed without incident. However, the threat is real, and the Counter Terrorism Policing guidance on Protect Duty makes clear that event organisers have responsibilities that go beyond hiring a door supervisor.

## Planning for London events

The UK has a developed private security regulatory framework. All close protection officers must hold a current SIA licence. Working with unlicensed operators is illegal and creates unlimited liability for the event organiser. Our operator network holds current SIA close protection and door supervisor licences as a minimum.

Vehicle exclusion is a standard consideration for London events in central locations. The 2017 vehicle ramming attacks demonstrated that vehicle access management is an operational requirement rather than an aesthetic choice.

For events on politically sensitive topics, protest risk assessment is part of the planning process. London's protest culture is active and Protected protests can affect venue access and event logistics.
""",
    },
    {
        "slug": "new-york",
        "city": "New York",
        "country": "United States",
        "risk_level": "medium",
        "h1": "Event Security in New York",
        "description": "Corporate event security in New York City for conferences, investor summits, and private functions. SLA-licensed close protection, venue assessment, and counter-terrorism planning.",
        "cta_text": "High-profile event in New York? Executive protection and venue security from vetted operators.",
        "components": [
            {"title": "Venue Security Assessment", "description": "Assessment of the event venue covering access control, vehicle exclusion, emergency exits, and perimeter management. New York's major conference venues (Javits Center, hotel ballrooms, financial district event spaces) have variable security infrastructure."},
            {"title": "State-Licensed Close Protection", "description": "New York State requires private security guards to hold a Security Guard licence (Article 7A of the General Business Law). Close protection officers must additionally hold firearms licences if armed. All operators we work with hold current New York State licensing."},
            {"title": "Executive Protection", "description": "Protective detail for C-suite executives, HNWI clients, and named public figures. New York's financial sector event calendar (investor summits, private equity forums, IPO roadshows) creates regular demand for discreet executive protection."},
            {"title": "Access Control", "description": "Credentialed entry management with ID verification. For events with high-profile financial sector attendees, access control limits competitive intelligence gathering."},
            {"title": "Active Shooter Response Planning", "description": "Written emergency protocols for active threat scenarios including shelter-in-place procedures, evacuation routes, and communication with NYPD. New York has a developed NYPD counter-terrorism capability that coordinates with private security at major events."},
            {"title": "Protest and Disruption Management", "description": "New York has an active protest environment. For events on politically sensitive topics, demonstration management and crowd control planning are relevant security considerations."},
        ],
        "faqs": [
            {"question": "What are the primary security risks at New York corporate events?", "answer": "New York's primary security risks for corporate events are active shooter/terrorism (the city remains a high-priority target), protest disruption for events on politically sensitive topics, and routine crime (theft, fraud) targeting high-net-worth attendees. The city has an exceptional NYPD counter-terrorism capability that provides a baseline of protection, but private security planning supplements rather than depends on police response."},
            {"question": "Do New York event security personnel need specific licences?", "answer": "Yes. New York State requires all security guards to be licensed under Article 7A of the General Business Law. This includes basic guards and close protection officers. Armed personnel require New York State firearms licences. Working with unlicensed security personnel creates legal exposure for the event organiser. We work exclusively with licensed operators."},
            {"question": "Is NYPD coordination standard for major New York events?", "answer": "For events above a certain size or profile, NYPD coordination is standard practice. The NYPD Counter Terrorism Bureau has liaison protocols for large events and high-profile venue security. We coordinate with NYPD as appropriate for the event scale and profile."},
        ],
        "body": """New York City is one of the world's primary corporate event destinations: the location of choice for investor summits, financial sector conferences, and high-profile product launches. The city has an exceptional private security industry and one of the most capable police counter-terrorism operations in the world.

## The security context

New York has been a persistent target for terrorism: the 1993 World Trade Center bombing, the September 11 attacks, the 2017 truck attack on the Hudson River bike path, multiple disrupted plots. The NYPD Counter Terrorism Bureau has a sophisticated operational capability. The threat is real; the response infrastructure is also real.

For corporate events, the specific risks beyond terrorism are: active shooter scenarios at public venues, protest disruption for events on politically sensitive topics, and crime targeting wealthy attendees (pickpocketing, fraud, hotel room theft). These are manageable risks with appropriate planning.

## Planning for New York events

New York's major conference venues have developed security infrastructure. The Javits Center has its own security team and NYPD liaison. Hotel ballrooms in Midtown Manhattan are adjacent to some of the most heavily policed areas in the country. This provides a baseline that is better than most cities in this region.

The key additions our security team provides for New York events are: close protection for identified high-risk principals, access control beyond standard hotel provision, emergency response planning that goes beyond fire evacuation, and protest risk assessment for relevant events.

All operators are licensed under New York State Article 7A. Armed operators carry valid New York State firearms licences. We do not work with out-of-state security companies who have not verified their New York licensing status.
""",
    },
    {
        "slug": "paris",
        "city": "Paris",
        "country": "France",
        "risk_level": "high",
        "h1": "Event Security in Paris",
        "description": "Corporate event security in Paris for conferences, private functions, and major summits. Terrorism risk management, CNAPS-licensed protection, and venue assessment in France's capital.",
        "cta_text": "Planning a corporate event or summit in Paris? Terrorism risk is part of our scope here.",
        "components": [
            {"title": "Terrorism Risk Assessment", "description": "France operates under its highest terrorism alert level, Urgence Attentat. Our pre-event assessment covers current threat indicators, VIGIPIRATE plan requirements, and specific risk factors for your event dates and venue."},
            {"title": "Venue Security Assessment", "description": "Physical assessment covering access control hardening, vehicle exclusion, blast standoff, emergency exits, and compliance with VIGIPIRATE security recommendations for public spaces."},
            {"title": "CNAPS-Licensed Close Protection", "description": "All close protection officers hold CNAPS (Conseil National des Activités Privées de Sécurité) authorisation. This is a legal requirement in France. Unarmed protection only (firearms prohibited for private security in France)."},
            {"title": "Access Control", "description": "Credentialed entry management with bag search. French law and current terrorism threat guidance make bag searches at events a legal expectation rather than an optional addition."},
            {"title": "Counter-Terrorism Awareness Training", "description": "Pre-event staff briefing on suspicious activity recognition, evacuation procedures, and the Stop-Alert-Protect protocol used by French security authorities."},
            {"title": "Secure Event Transport", "description": "CNAPS-licensed security drivers for principal transport. Paris event transport includes route planning around known protest areas and areas of elevated surveillance activity."},
        ],
        "faqs": [
            {"question": "What is the current terrorism threat level for Paris events?", "answer": "France maintains Urgence Attentat, its highest terrorism alert level, as a sustained posture following the attacks of 2015-2016 and subsequent incidents. The threat is primarily from Islamist extremism. France has disrupted numerous plots but attacks continue to occur. For event planning, this means terrorism risk mitigation is a mandatory component of the security plan rather than a contingency consideration."},
            {"question": "What is VIGIPIRATE and how does it affect event security planning?", "answer": "VIGIPIRATE is France's national counter-terrorism plan. At the Urgence Attentat level, it imposes specific security obligations on public events and venues including controlled access, bag searches, and liaison with police. Event organisers have legal obligations under this framework. We ensure our event security plans comply with current VIGIPIRATE requirements."},
            {"question": "Are armed security officers available for Paris events?", "answer": "No. Firearms are prohibited for private security in France. All close protection is unarmed. CNAPS-authorised operators are trained in conflict avoidance, de-escalation, and extraction. For events requiring armed security, a formal request to the Prefecture de Police for police presence is the route."},
        ],
        "body": """Paris is one of Europe's most significant conference cities: home to major international summits, technology events (VivaTech), luxury and fashion events, and political conferences at EU and NATO level. It is also one of the highest terrorism risk cities in Europe.

## The security context

France has experienced some of Europe's most severe terrorist attacks in the past decade: the Charlie Hebdo/Hyper Cacher attacks (January 2015, 17 dead), the Bataclan concert hall attack as part of the coordinated November 2015 attacks (130 dead), the Nice Bastille Day truck attack (86 dead, 2016). France's counter-terrorism capability has been substantially enhanced since 2015. The Urgence Attentat alert level reflects the sustained nature of the threat.

For corporate event planning in Paris, terrorism risk is not hypothetical. It is the central security planning assumption.

## Event security in Paris

The French private security regulatory framework is among the most developed in Europe. CNAPS authorisation is required for all security activity. All close protection in France is unarmed. The standard approach is venue access control, bag search, counter-terrorism-aware security planning, and VIGIPIRATE compliance.

For events with named high-risk principals (government officials, executives from sectors with specific threat histories, HNWI clients), we recommend dedicated close protection from CNAPS-authorised operators with specific counter-terrorism training.

Vehicle exclusion management is a practical requirement for Paris events in central locations. Vehicle ramming has been used in France. Physical exclusion barriers at venue approaches are increasingly standard for large-format events.
""",
    },
    {
        "slug": "singapore",
        "city": "Singapore",
        "country": "Singapore",
        "risk_level": "low",
        "h1": "Event Security in Singapore",
        "description": "Corporate event security in Singapore for conferences, investor summits, and private functions. SIRD-licensed protection, access control, and communications security for events in the regional hub.",
        "cta_text": "Planning a regional conference or investor summit in Singapore?",
        "components": [
            {"title": "Venue Security Assessment", "description": "Assessment of the event venue covering access control, emergency exits, and communications security considerations. Singapore's major conference venues (Sands Expo, Suntec Singapore, Marina Bay Sands) have well-developed security infrastructure. Our assessment supplements rather than replicates venue provision."},
            {"title": "SIRD-Licensed Close Protection", "description": "Close protection officers licensed under the Private Security Industry Act (PSIA) by the Security Industry Regulatory Department (SIRD). Singapore's private security industry is tightly regulated and professionally developed."},
            {"title": "Executive Protection for HNWI Clients", "description": "Discreet executive protection for family office clients, HNWI attendees, and senior executives. Singapore's status as a wealth management hub creates specific demand for low-profile, high-quality executive protection."},
            {"title": "Communications Security", "description": "Singapore's intelligence infrastructure is sophisticated. For events involving commercially or politically sensitive discussions, communications security is a relevant consideration. We provide advisory on operational security for high-sensitivity meetings."},
            {"title": "Access Control", "description": "Credentialed entry management and bag search for events requiring controlled attendance. Singapore's corporate event circuit includes significant private equity and family office events where access control is commercially essential."},
            {"title": "Emergency Response", "description": "Emergency planning covering medical incidents, security threats, and evacuation. Singapore's emergency services infrastructure is excellent. Our plan supplements and coordinates with Singapore Civil Defence Force procedures."},
        ],
        "faqs": [
            {"question": "Is Singapore a low-risk environment for corporate events?", "answer": "By most conventional security metrics, yes. Singapore has very low crime rates, no active terrorism attacks since the 1990s (though the Internal Security Department has disrupted plots), and exceptional infrastructure. The risks at Singapore corporate events are primarily commercial: competitive intelligence gathering, communications monitoring, and fraud targeting financial sector attendees. Physical security risk is low; information security risk is higher than it appears."},
            {"question": "What specific licences do Singapore security personnel need?", "answer": "Security personnel in Singapore must be licensed under the Private Security Industry Act. The SIRD issues licences for security officers, security supervisors, and private investigators. All operators we work with hold current SIRD licences. Note that foreign security personnel cannot legally work in Singapore without specific authorisation; this affects international teams accompanying visiting executives."},
            {"question": "Can foreign security personnel accompany executives into Singapore?", "answer": "Foreign close protection officers cannot operate legally in Singapore without SIRD licensing. Visiting executives who require close protection in Singapore should use locally licensed operators rather than travelling with unlicensed foreign teams. We arrange SIRD-licensed operators who can be briefed on the principal's specific requirements."},
        ],
        "body": """Singapore is Southeast Asia's primary corporate event hub: home to major financial services conferences, technology summits, and the regional headquarters of hundreds of multinationals. By most conventional security metrics it is one of the safest cities in the world.

## The security environment

Singapore's violent crime rate is extremely low. Terrorism plots have been disrupted but no mass-casualty attacks have occurred since the 1990s. The Internal Security Department (ISD) maintains a robust counter-terrorism capability. For most corporate event planners, Singapore's security environment is not the primary concern.

The less obvious risk categories at Singapore events are information security related. Singapore operates a sophisticated state intelligence apparatus. Commercially sensitive discussions at major corporate events should assume the possibility of surveillance. This is relevant for events involving significant M&A activity, competitive intelligence, or politically sensitive business discussions.

## Event security in practice

Singapore's major conference venues (Marina Bay Sands, Suntec, Changi Business Park) have their own well-developed security teams. Our scope for Singapore events is typically: executive protection for HNWI or high-profile principals, access control for high-sensitivity private meetings, and communications security advisory for commercially sensitive events.

The licensing requirement is important to note: foreign close protection officers cannot legally operate in Singapore without SIRD authorisation. Visiting executives who travel with their own security team need to transition to SIRD-licensed operators on arrival or arrange formal licensing clearance in advance.

Singapore's emergency services are excellent. Our emergency planning for Singapore events is genuinely supplementary rather than compensatory.
""",
    },
    {
        "slug": "sydney",
        "city": "Sydney",
        "country": "Australia",
        "risk_level": "medium",
        "h1": "Event Security in Sydney",
        "description": "Corporate event security in Sydney for conferences, major summits, and private functions. Terrorism-aware venue assessment, licensed close protection, and access control in Australia's business capital.",
        "cta_text": "Planning a major conference or corporate event in Sydney?",
        "components": [
            {"title": "Terrorism-Aware Venue Assessment", "description": "Australia's ASIO terrorism threat level for Sydney is PROBABLE. Our venue assessment addresses vehicle exclusion, controlled access, and emergency evacuation with specific reference to the current threat level and any event-specific indicators."},
            {"title": "Licensed Close Protection", "description": "All security personnel hold current NSW Security Industry Act licences (Class 1C for close protection). NSW Fair Trading regulates the security industry; unlicensed operation creates legal exposure for event organisers."},
            {"title": "Access Control", "description": "Credentialed entry management with bag search. For events in central Sydney, access control is informed by the current terrorism advisory rather than treated as a routine door management function."},
            {"title": "VIP and Executive Protection", "description": "Close protection for senior executives, government officials, and HNWI clients. Sydney hosts major investment conferences, Asian finance forums, and government summits with attendees requiring professional protection."},
            {"title": "Secure Event Transport", "description": "Licensed security drivers for principal transport. Sydney event transport includes current awareness of police operations, large event access restrictions (particularly around Darling Harbour and the CBD), and road closure management."},
            {"title": "Emergency Response Planning", "description": "Emergency protocols covering medical incidents, security threats, and evacuation. Sydney has excellent private emergency medical capability; our planning coordinates with St John Ambulance or equivalent for large events."},
        ],
        "faqs": [
            {"question": "What is the terrorism risk for events in Sydney?", "answer": "ASIO rates the terrorism threat for Australia as PROBABLE, meaning an attack is likely at some point. Sydney has experienced attacks: the 2014 Lindt Cafe siege, the 2016 Minto stabbing, and multiple disrupted plots. The primary threat is from individuals inspired by Islamist extremism rather than organised group attacks. For event planning, this means access control, vehicle exclusion at major events, and staff counter-terrorism awareness are appropriate rather than exceptional security measures."},
            {"question": "What licences do Sydney event security personnel need?", "answer": "All security personnel in New South Wales must be licensed under the Security Industry Act 1997. Class 1A covers crowd control; Class 1C covers close protection (bodyguarding). NSW Fair Trading issues and regulates licences. We work exclusively with currently licensed operators."},
            {"question": "Is Sydney appropriate for high-sensitivity corporate meetings?", "answer": "Sydney has a well-developed private security industry and is appropriate for high-sensitivity corporate meetings with proper planning. The main considerations are communications security (Australia's Five Eyes membership means national intelligence capabilities are sophisticated) and access control for meetings requiring strict confidentiality."},
        ],
        "body": """Sydney is Australia's primary corporate event destination and a regional hub for Asia-Pacific business conferences, investment forums, and financial services events. The security environment is lower risk than most cities on this platform but not without specific threats.

## The security context

ASIO maintains an Australia-wide terrorism threat level of PROBABLE. Sydney has experienced terrorist incidents: the 2014 Lindt Cafe siege (3 dead) was a watershed event for Australian security planning. The current primary threat is from lone actors inspired by Islamist extremism rather than organised group attacks. Australia's counter-terrorism capability (ASIO, Australian Federal Police, NSW Police Counter Terrorism and Special Tactics Command) is advanced.

For corporate event planning, the practical impact of PROBABLE threat level is: vehicle exclusion at major central venue events, access control with bag search for large-format conferences, and staff counter-terrorism awareness training.

## Event security in Sydney

Sydney's major conference venues (ICC Sydney at Darling Harbour, central hotel convention centres) have their own security teams. Our scope typically covers executive close protection for high-profile principals, supplementary access control for high-sensitivity events, and emergency planning coordination.

The licensing framework in NSW is well-established. All security personnel require current NSW Security Industry Act licences. This is rigorously enforced; event organisers who use unlicensed contractors face significant penalties.

Transport security in Sydney is straightforward by comparison with Asian megacities. Sydney traffic is variable; route planning around large events at Darling Harbour or the CBD is standard. Counter-surveillance is relevant for HNWI clients or executives with specific threat histories.
""",
    },
    {
        "slug": "tokyo",
        "city": "Tokyo",
        "country": "Japan",
        "risk_level": "low",
        "h1": "Event Security in Tokyo",
        "description": "Corporate event security in Tokyo for conferences, investor roadshows, and private functions. Licensed close protection, access control, and stalking threat management in Japan's capital.",
        "cta_text": "Running a corporate event or investor conference in Tokyo?",
        "components": [
            {"title": "Venue Security Assessment", "description": "Assessment of the Tokyo event venue covering access control, emergency exits, and the specific operational requirements of Japan's major conference hotels. Tokyo's corporate venue infrastructure is excellent and well-maintained; our assessment focuses on gaps and supplementation."},
            {"title": "Police Act-Licensed Close Protection", "description": "Security personnel licensed under Japan's Police Act and the Workers Dispatching Act where applicable. Japan's private security industry is strictly regulated; operators must hold valid Public Safety Commission authorisation."},
            {"title": "Stalking and Harassment Risk Management", "description": "Japan has a specific and documented stalking risk against public figures and corporate executives. For events with named public attendees, stalking risk is part of the security assessment alongside conventional crime and terrorism factors."},
            {"title": "Access Control", "description": "Credentialed entry management with ID verification. For Tokyo corporate events with international executives, access control also addresses the risk of competitor intelligence gathering."},
            {"title": "VIP Executive Protection", "description": "Discreet close protection for executives, HNWI clients, and public figures. Tokyo's low ambient crime rate does not eliminate the need for protection for specifically targeted individuals."},
            {"title": "Emergency Response Planning", "description": "Emergency protocols covering medical incidents, security threats, natural disaster response, and evacuation. Japan's seismic environment means earthquake response planning is a mandatory component of Tokyo event security, not a theoretical one."},
        ],
        "faqs": [
            {"question": "Is Tokyo a low-risk environment for corporate events?", "answer": "By conventional violent crime and terrorism metrics, yes. Tokyo has one of the lowest violent crime rates of any major city in the world. Terrorism attacks are extremely rare (the 1995 sarin attack in the Tokyo metro remains the defining reference event, now 30 years ago). However, Tokyo is not zero risk: stalking against public figures is a documented and growing threat, anti-espionage targeting of corporate executives is relevant in the current geopolitical environment, and Japan's earthquake vulnerability is a genuine emergency planning factor."},
            {"question": "What security licences are required in Japan?", "answer": "Security companies in Japan must be registered with the Public Safety Commission under the Security Services Act (Keibi-in Ho). Individual security officers require certificated training. Foreign security companies cannot legally operate in Japan without a Japanese legal entity and Commission registration. Foreign close protection officers cannot legally work in Japan; locally licensed operators must be used."},
            {"question": "How does Japan's earthquake risk affect event security planning?", "answer": "Tokyo sits on one of the world's most active seismic zones. The probability of a major earthquake during a given week in Tokyo is non-trivial over multi-day conference periods. Emergency response planning for Tokyo events includes earthquake evacuation procedures, communication protocols if mobile networks are disrupted, and designated safe assembly points. This is standard practice, not crisis planning."},
        ],
        "body": """Tokyo is one of Asia's most significant corporate event destinations. It hosts major technology conferences, automotive sector events, government-to-government forums, and investor roadshows for the world's third-largest economy. By most security metrics it is one of the safest cities in the world.

## The security environment

Tokyo's violent crime rate is extremely low. Terrorism incidents are rare; the last mass-casualty attack (the 1995 sarin attack by Aum Shinrikyo) killed 13 people and is now three decades past. The National Police Agency has a capable counter-terrorism capability. Day-to-day criminal risk is minimal.

The specific security risks at Tokyo corporate events are less conventional: stalking and harassment of public figures and named executives is a documented and growing problem in Japan; competitive intelligence gathering by corporate actors is relevant given Japan's strategic industries; and Japan's seismic environment creates genuine emergency planning requirements that do not exist in most European or North American conference cities.

## Event security in Tokyo

Tokyo's major conference and hotel venues have well-developed security infrastructure and highly professional venue teams. Our scope for Tokyo events typically covers: executive protection for specifically targeted or high-profile principals, access control for events where competitive intelligence gathering is a concern, and earthquake emergency planning.

Earthquake response planning is not optional for Tokyo events. A major seismic event during a multi-day conference creates communication disruption, transportation failure, and evacuation challenges that require pre-prepared protocols. We include this in every Tokyo event security plan.

Foreign security personnel cannot legally operate in Japan. Any visiting executive who travels with a foreign close protection team must transition to Japan-licensed operators on arrival.
""",
    },
    {
        "slug": "moscow",
        "city": "Moscow",
        "country": "Russia",
        "risk_level": "critical",
        "h1": "Event Security in Moscow",
        "description": "Security assessment for corporate events in Moscow. Current advisory: most Western governments advise against all travel to Russia. If operating in Moscow, specialist advice is mandatory.",
        "cta_text": "Still operating in Moscow? Specialist advice before any event activity.",
        "components": [
            {"title": "Travel Advisory Review", "description": "FCDO, State Dept, and EU member state advisories uniformly advise against all travel to Russia. Any corporate event activity in Moscow must be assessed against these advisories and the specific risk profile of the attending executives."},
            {"title": "Detention and Legal Risk", "description": "Wrongful detention of foreign nationals is an active and documented risk in Russia. Executives from Western companies face specific legal risk from sanctions enforcement, espionage allegations, and commercial disputes. This is the primary security risk for most Western executives in Moscow."},
            {"title": "Communications Security", "description": "Russia's FSB maintains extensive surveillance capability. All communications should be treated as potentially monitored. Devices brought into Russia carry data exfiltration risk. TSCM (Technical Surveillance Countermeasures) sweep for sensitive meeting locations."},
            {"title": "Physical Security", "description": "Conventional close protection for principals. Moscow's physical crime risk is moderate; the primary security concern for Western executives is not street crime but state-actor risk, detention risk, and commercial dispute escalation."},
            {"title": "Exit Planning", "description": "Reliable and vetted exit routes from Moscow for all principal attendees. Flight disruption (Western carriers have suspended Russia routes), land border options, and emergency extraction planning."},
            {"title": "Sanctions Compliance Review", "description": "Corporate event activity in Moscow may create sanctions exposure for Western companies. This is a legal and security risk category that must be assessed before any event engagement."},
        ],
        "faqs": [
            {"question": "Should we hold a corporate event in Moscow currently?", "answer": "The honest answer is that most Western-connected corporate events in Moscow are not operating due to the combination of travel advisories, sanctions, flight suspensions, and legal risk to attending executives. If your organisation has specific reasons to operate in Moscow, specialist security and legal advice is mandatory before any planning begins. We can provide that advisory but we do not facilitate event activity that creates undue risk to attendees."},
            {"question": "What is the detention risk for Western executives in Moscow?", "answer": "Multiple Western executives and nationals have been detained in Russia since 2022 on charges including espionage, sanctions violations, and commercial disputes. The risk is real, documented, and cannot be mitigated away with standard security planning. Any Western executive entering Russia currently must accept a non-trivial detention risk. This should be reflected in corporate risk committee decisions, not treated as an operational security matter."},
            {"question": "Are any security operators still active in Moscow?", "answer": "Locally licensed operators continue to operate in Moscow. The challenge is vetting and trust assurance in the current environment. We do not operate standard vetted operator referrals for Moscow; we provide specialist advisory only."},
        ],
        "body": """Moscow is included in this platform because corporate event enquiries continue to arrive from organisations with Russia operations, despite the current advisory environment. The honest and accurate assessment is that corporate event planning in Moscow for Western-connected organisations is a high-risk activity at present.

## The current advisory position

FCDO advises against all travel to Russia. The State Department advises against all travel to Russia. Most European governments advise against all travel. These advisories exist for specific documented reasons: the war in Ukraine, the risk of detention of Western nationals, sanctions enforcement risk, and the general deterioration in the rule of law environment for foreign businesses.

## If you are operating in Moscow

Some organisations continue to operate in Russia: companies with Russia-domiciled entities, organisations with specific compliance obligations, and individuals with family or contractual necessity. If you are in this category, specialist security advice is not optional.

The primary security risk in Moscow for Western executives is not conventional crime or terrorism. It is detention by Russian authorities, data exfiltration by FSB surveillance operations, and commercial dispute escalation into criminal proceedings. These are state-actor risk categories that require specialist advisory rather than standard event security provision.

## What we provide for Moscow

We do not operate a standard vetted operator referral service for Moscow given the current environment. We provide specialist pre-deployment advisory covering legal risk, communications security, device hygiene, and exit planning. Any organisation planning corporate event activity in Moscow should begin with a legal opinion from Russia-specialist counsel alongside a security assessment.
""",
    },
]


def write_city_event_page(city: dict, out_dir: str):
    slug = city["slug"]
    out_path = os.path.join(out_dir, f"{slug}.md")
    if os.path.exists(out_path):
        print(f"  SKIP (exists): {slug}.md")
        return

    components_yaml = ""
    for comp in city.get("components", []):
        title = comp["title"].replace('"', '\\"')
        desc = comp["description"].replace('"', '\\"')
        components_yaml += f'  - title: "{title}"\n    description: "{desc}"\n'

    faqs_yaml = ""
    for faq in city.get("faqs", []):
        q = faq["question"].replace('"', '\\"')
        a = faq["answer"].replace('"', '\\"')
        faqs_yaml += f'  - question: "{q}"\n    answer: "{a}"\n'

    content = f"""---
title: "{city["h1"]}"
description: "{city["description"]}"
slug: "{city["slug"]}"
h1: "{city["h1"]}"
city: "{city["city"]}"
country: "{city["country"]}"
risk_level: "{city["risk_level"]}"
hero_image: "hero.jpg"
cta_text: "{city.get("cta_text", "")}"
components:
{components_yaml}faqs:
{faqs_yaml}---

{city["body"].strip()}
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  WROTE: {slug}.md")


if __name__ == "__main__":
    print(f"Writing {len(cities)} event-security city pages...")
    for c in cities:
        write_city_event_page(c, OUT_DIR)
    print("Done.")
