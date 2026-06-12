#!/usr/bin/env python3
"""
Batch 10: 10 new P4 city pages + bodyguard-hire, security-drivers,
executive-protection, residential-security for each = 50 pages total.
Cities: Manama, Jeddah, Erbil, Lahore, Phnom Penh, Quito,
        Port Harcourt, Kano, Douala, Santo Domingo
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(REPO, "site", "content")

cities = {
    "manama": {
        "name": "Manama",
        "country": "Bahrain",
        "risk_level": "moderate",
        "region": "Middle East",
        "related": [("Dubai", "dubai"), ("Riyadh", "riyadh"), ("Doha", "doha")],
        "city_body": """Manama is the capital and financial centre of Bahrain, a constitutional monarchy and member of the Gulf Cooperation Council. The city hosts the Bahrain International Circuit (home of the Formula 1 Bahrain Grand Prix), a significant Islamic finance sector, and the regional headquarters of numerous international banks and energy companies. Bahrain's relative openness compared with neighbouring Gulf states has made it a hub for expatriates, international events, and corporate regional operations.

## The security environment

The FCDO advises normal travel precautions for Bahrain overall, while noting that the threat from terrorism remains high across the Middle East region. Manama itself is stable day-to-day, but the political environment carries residual sensitivity from the 2011 unrest associated with the Arab Spring. The Shia community, which represents the majority of the population, has historically expressed political grievances, and demonstrations have occurred in areas outside the central business district. The Adliya, Seef, and Diplomatic Area are the primary zones for international business and hotel stays and carry a considerably lower incident profile than outer townships. Source: FCDO Bahrain travel advice (2026). US State Department Bahrain advisory Level 2 (2026).

## Organised crime and fraud

Petty theft and confidence fraud targeting visitors are the most common criminal risks in Manama. Vehicle crime is documented in outdoor car parks. The financial services sector makes Bahrain a target for sophisticated fraud schemes; principals engaged in deal-making or fund transfer activity should apply rigorous counterparty verification and should not conduct sensitive financial transactions in hospitality settings.

*Sources: FCDO Bahrain travel advice (2026). US State Department Level 2 advisory Bahrain (2026). Bahrain Ministry of Interior security licensing framework.*
For comparable Gulf operating environments, see our [Dubai city briefing](/cities/dubai/) and [Doha city briefing](/cities/doha/).""",
        "threats": [
            ("Terrorism Threat in the Gulf Region",
             "The threat from terrorism remains high across the wider Middle East, including Bahrain. ISIL and affiliated groups retain capability to conduct attacks in the Gulf region. International hotels, venues hosting large gatherings, and government facilities carry an elevated profile as potential targets. Source: FCDO Bahrain travel advice (2026)."),
            ("Political Demonstrations and Civil Unrest",
             "Bahrain experienced significant unrest during the 2011 Arab Spring period. Political demonstrations continue to occur in areas outside central Manama, particularly in Shia-majority townships including Sitra, Bilad Al Qadeem, and Sanabis. The authorities have in the past used security forces to disperse gatherings. Demonstrations in outer areas can affect routes into the city. Source: FCDO Bahrain travel advice (2026)."),
            ("Petty Crime and Fraud",
             "Petty theft and fraud targeting visitors are the most common criminal risks. Pickpocketing occurs in crowded commercial areas. Sophisticated fraud schemes operate in the financial services sector. Source: Bahrain Ministry of Interior crime statistics (2025)."),
        ],
        "regulations": {
            "firearms": "Private security personnel in Bahrain are not routinely armed. The Bahrain Police Force and National Security Agency maintain jurisdiction over armed response. Licensed private security companies may seek authorisation for armed operators in specific high-risk contract contexts, but unarmed close protection is the standard commercial model.",
            "licensing": "Private security companies in Bahrain must hold a licence from the Ministry of Interior's General Directorate of Criminal Investigation and Forensic Science. Individual security personnel require individual registration. The licensing framework is well-administered relative to regional norms.",
            "foreign_operators": "Foreign security personnel may accompany principals as personal protection staff. Commercial security contracting in Bahrain requires local company registration and Ministry of Interior licensing."
        },
        "zones": {
            "safe": [
                "Diplomatic Area: Central business district, international banks, and government ministries. The primary hub for corporate visitors.",
                "Seef District: Commercial and retail hub. International hotels and the Bahrain World Trade Centre. Good security infrastructure.",
                "Adliya: Upscale residential and dining district. Popular with expatriates and business visitors."
            ],
            "elevated": [
                "Outer townships (Sitra, Bilad Al Qadeem, Sanabis): Historically associated with political demonstrations. Not on standard corporate visitor routes but may affect road access.",
                "Riffa and outer southern areas: Reduced security infrastructure compared to central Manama."
            ]
        },
        "emergency": [
            ("Police", "+973 17 716 060"),
            ("Bahrain Defence Force Military Hospital", "+973 17 652 000"),
            ("American Mission Hospital Manama", "+973 17 253 447"),
            ("British Embassy Manama", "+973 17 574 100"),
        ],
        "warnings": [
            "Bahrain's political environment retains sensitivity. Avoid all political gatherings and demonstrations, including those in outer townships. FCDO advises against attending protests.",
            "Photography of government buildings, military installations, and the royal palace is prohibited. Detention for photography violations has occurred. Confirm photography rules before using cameras in public areas near official facilities.",
            "Ramadan and public holiday periods affect operating hours for businesses, restaurants, and some security services. Plan logistics around these periods, particularly for international events."
        ],
        "faqs": [
            ("Why do international businesses maintain a presence in Manama?",
             "Bahrain's financial sector, Islamic finance expertise, and relatively liberal regulatory environment attract international banks, asset managers, and energy companies. The country has been a gateway into the Gulf Cooperation Council market for decades. The Bahrain Financial Harbour and Bahrain Bay developments provide modern Grade A office space for regional operations."),
            ("What is the threat from terrorism in Manama?",
             "The FCDO assesses the threat from terrorism in Bahrain as high, consistent with the broader Gulf region assessment. No major attack has occurred in Manama's central business districts in recent years, but the threat assessment reflects the regional context rather than a specific local intelligence picture. Large public events and international gatherings warrant a security overlay appropriate to the regional threat level. Source: FCDO Bahrain travel advice (2026)."),
            ("Are there restrictions on alcohol and social conduct in Bahrain?",
             "Bahrain permits the consumption of alcohol in licensed premises, including international hotels, restaurants, and some private clubs. This is more permissive than most Gulf neighbours. However, public intoxication is illegal and will result in arrest. Personal conduct norms are more conservative outside tourist and expatriate areas."),
            ("Does Manama require a dedicated bodyguard for standard corporate visits?",
             "For most corporate visitors to Manama, a risk-appropriate approach involves vetted transport and a pre-travel briefing rather than a dedicated close protection officer. For higher-profile principals, visiting delegations for major deals, or events that attract a large international audience, a CPO overlay is appropriate given the regional terrorism threat level.")
        ]
    },
    "jeddah": {
        "name": "Jeddah",
        "country": "Saudi Arabia",
        "risk_level": "high",
        "region": "Middle East",
        "related": [("Riyadh", "riyadh"), ("Dubai", "dubai"), ("Doha", "doha")],
        "city_body": """Jeddah is Saudi Arabia's second-largest city and the primary gateway for Hajj and Umrah pilgrims at King Abdulaziz International Airport. It is the commercial capital of the Kingdom, with a major Red Sea port, a large retail and hospitality sector, and the headquarters of significant oil and petrochemical companies. Saudi Vision 2030 has driven significant infrastructure investment, including the Jeddah Season entertainment district, the Jeddah Tower (under construction), and the NEOM-adjacent Red Sea development corridor. The expatriate community in Jeddah is substantial, drawn primarily by the energy and construction sectors.

## FCDO advisory context

The FCDO advises against all travel to within 10km of the Saudi-Yemen border and against all but essential travel to the Najran, Jizan, and Asir regions due to the Houthi missile and drone threat. Jeddah itself, on the Red Sea coast, is within the zone that has experienced cross-border missile and drone attacks originating from Yemen. The FCDO travel advice for Saudi Arabia records that missiles and drones have struck targets in Saudi Arabia including in the Jeddah region, and recommends awareness of shelter procedures. Source: FCDO Saudi Arabia travel advice (2026).

## Security and social environment

Saudi Arabia applies strict social codes. Dress codes and public conduct norms are strictly enforced. Photography of government buildings, military sites, and individuals without consent carries legal risk. The Vision 2030 liberalisation programme has relaxed some restrictions (entertainment venues, mixed-gender working environments), but the underlying legal framework retains significant penalties for conduct that would be unremarkable elsewhere.

*Sources: FCDO Saudi Arabia travel advice (2026). US State Department Level 2 advisory Saudi Arabia (2026). Saudi General Authority for Security Companies (GASC) framework.*
For comparable operating environments, see our [Riyadh city briefing](/cities/riyadh/) and [Dubai city briefing](/cities/dubai/).""",
        "threats": [
            ("Houthi Missile and Drone Attacks",
             "Since the outbreak of the Yemen conflict, Houthi forces have launched cross-border missile and drone attacks targeting Saudi cities including Jeddah. The FCDO Saudi Arabia travel advice (2026) records that Jeddah has been in the target envelope of these attacks. King Abdulaziz International Airport and major infrastructure are potential targets. Shelter-in-place procedures and an understanding of the local warning system are part of operational planning for extended Jeddah stays."),
            ("Terrorism",
             "Saudi Arabia has been the target of terrorist attacks by al-Qaeda in the Arabian Peninsula and other groups. Although the frequency of domestic attacks has decreased significantly since the 2000s, the threat remains. International hotels, government facilities, and public gatherings carry an elevated profile. Source: FCDO Saudi Arabia travel advice (2026)."),
            ("Photography and Legal Restrictions",
             "Photography of government buildings, military facilities, palaces, and individuals without consent is prohibited under Saudi law. Violations have resulted in detention and deportation. Legal restrictions extend to social conduct, alcohol, and a range of activities that are legal in other jurisdictions. Briefing all members of a travelling party on local legal requirements is essential before arrival.")
        ],
        "regulations": {
            "firearms": "Private security personnel in Saudi Arabia operate under the General Authority for Security Companies (GASC) framework. Armed private security is available for high-risk contexts including industrial site protection and principal security. GASC licences are required for armed operators. The regulatory framework is comparatively sophisticated by regional standards.",
            "licensing": "All security companies in Saudi Arabia must hold a GASC licence from the Ministry of Interior. GASC regulates company registration, personnel vetting, training standards, and equipment authorisation. Saudi nationals must make up a minimum percentage of licensed security company workforces under Saudisation (Nitaqat) requirements.",
            "foreign_operators": "Foreign security personnel require individual GASC authorisation to operate commercially in Saudi Arabia. International companies typically partner with GASC-licensed Saudi entities to deliver operations on the ground."
        },
        "zones": {
            "safe": [
                "Al Hamra and Al Naeem districts: Primary expatriate and international hotel zone. Relatively secure with good infrastructure.",
                "Al Balad (Historic Jeddah): UNESCO World Heritage Site. Active tourist and commercial area in the old city. Standard precautions apply.",
                "Al Rawdah and Al Zahra: Residential and business districts used by corporate visitors."
            ],
            "elevated": [
                "Industrial port areas: Access-controlled, but the surrounding districts carry a higher crime profile.",
                "Southern districts closer to the Jeddah-Makkah corridor: Higher traffic volumes, less expatriate-oriented infrastructure."
            ]
        },
        "emergency": [
            ("Police", "999"),
            ("Red Crescent (Ambulance)", "911"),
            ("Dr. Erfan and Bagedo General Hospital", "+966 12 682 9000"),
            ("British Consulate General Jeddah", "+966 12 622 5550"),
        ],
        "warnings": [
            "Houthi cross-border missile and drone attacks have targeted Saudi Arabia including the Jeddah region. All visitors should familiarise themselves with the local air-raid warning system and shelter-in-place procedures before commencing work in the city. Source: FCDO Saudi Arabia travel advice (2026).",
            "Alcohol is prohibited in Saudi Arabia. Possession or consumption is a criminal offence punishable by flogging, imprisonment, and deportation. Do not attempt to import or purchase alcohol.",
            "Saudi Arabia operates a strict dress code. Female visitors must cover their hair and wear modest clothing in public. Male visitors should avoid shorts and vest tops outside hotel premises. Non-compliance can attract unwanted attention and, in some areas, intervention by authorities."
        ],
        "faqs": [
            ("Why do international companies have offices in Jeddah rather than only Riyadh?",
             "Jeddah is the commercial capital with the largest seaport in the Kingdom and significant concentration of private sector and family-group conglomerates. The Hajj and Umrah economy generates year-round logistics, hospitality, and construction business that does not centre on Riyadh. Vision 2030 projects including NEOM, the Red Sea Project, and the Jeddah Tower are headquartered or operationally managed from Jeddah, creating a significant project management and investment presence."),
            ("What is the Houthi missile threat for Jeddah visitors?",
             "The FCDO records that Houthi forces have launched missile and drone attacks against targets in Saudi Arabia including in the Jeddah region. Visitors should be familiar with the Saudi civil defence warning system and emergency shelter procedures. The risk is real but the frequency of successful strikes affecting central Jeddah's business districts has been limited. Source: FCDO Saudi Arabia travel advice (2026)."),
            ("Is close protection routine for senior executives visiting Jeddah?",
             "For senior executives engaged in high-value deal activity, site visits to industrial or construction zones, or with a profile that makes them a kidnapping or fraud target, a close protection arrangement is appropriate. For standard office-based visits in Al Hamra or Al Naeem districts with a vetted driver, a CPO overlay may not be required but should be assessed against the principal's specific profile and activities."),
            ("What GASC documentation should a Jeddah security provider hold?",
             "Any security company delivering close protection or security driver services in Jeddah must hold a GASC (General Authority for Security Companies) licence from the Saudi Ministry of Interior. The GASC number should be provided on request. Individual operators must hold personal GASC authorisation. Operators without GASC licences are operating illegally and should not be engaged.")
        ]
    },
    "erbil": {
        "name": "Erbil",
        "country": "Iraq",
        "risk_level": "high",
        "region": "Middle East",
        "related": [("Baghdad", "baghdad"), ("Amman", "amman"), ("Beirut", "beirut")],
        "city_body": """Erbil (also written Irbil or Arbil) is the capital of the Kurdistan Region of Iraq (KRI) and one of the world's oldest continuously inhabited cities. It serves as the administrative and commercial hub for the KRI's substantial oil and gas sector, hosting the Kurdistan Regional Government (KRG), international oil companies including BP, TotalEnergies, and DNO, and a significant NGO and diplomatic presence. Erbil is substantially more stable than the rest of Iraq, but the surrounding region and the Iraq-Syria border area retain a very high threat profile.

## FCDO advisory and KRI context

The FCDO advises against all travel to Iraq with the exception of the Kurdistan Region, for which it advises against all but essential travel. This distinction is operationally important: Erbil has experienced periodic rocket and drone attacks directed at the US Consulate and international coalition military presence, and the threat from Iran-aligned militia groups is assessed as ongoing. Erbil International Airport has been targeted. Source: FCDO Iraq travel advice (2026). US State Department Level 4 Do Not Travel advisory for Iraq (Level 3 for Kurdistan Region) (2026).

## Oil sector and business context

The KRG's oil sector is the primary driver of international business travel to Erbil. The Bazian, Taq Taq, and Shaikan fields have attracted long-term international operator presence. Project finance, legal, and technical visitors move regularly between Erbil, Dubai, and London. KRG political dynamics, including disputes with Baghdad over oil revenue sharing and customs revenues, affect the business environment and should be monitored by any principal engaged in contract or licensing discussions with the KRG.

*Sources: FCDO Iraq travel advice (2026). US State Department Iraq advisory (2026). Kurdistan Regional Government Ministry of Interior security licensing framework.*
For comparable operating environments, see our [Baghdad city briefing](/cities/baghdad/) and [Amman city briefing](/cities/amman/).""",
        "threats": [
            ("Rocket and Drone Attacks",
             "Iran-aligned militia groups have conducted rocket and drone attacks against targets in Erbil, including Erbil International Airport, the US Consulate, and coalition military facilities. Attacks have occurred without warning and have caused casualties. The threat is assessed as ongoing. Source: FCDO Iraq travel advice (2026); US State Department Iraq advisory (2026)."),
            ("Kidnapping",
             "The Kurdistan Region has a lower kidnapping incidence than the rest of Iraq, but the risk is not zero. Criminal and politically motivated kidnap affecting international nationals has occurred in the KRI. Kidnap-for-ransom operations by criminal groups and politically motivated targeting by militia actors are both documented threats in the broader region."),
            ("Terrorism and Cross-Border Spill",
             "Despite the military defeat of ISIL's territorial caliphate, ISIL retains insurgent capability in areas near the KRI borders, including the Sinjar region and areas south of the KRI administrative boundary. Attacks on Kurdish military positions have continued. The Erbil city centre itself has a more controlled security environment than border areas, but the regional threat cannot be discounted.")
        ],
        "regulations": {
            "firearms": "Armed security is widely used in Erbil and is the standard configuration for senior principals in the KRI. The Kurdistan Regional Government Ministry of Interior licenses security companies operating in the region. Armed CPO with armoured vehicles is the norm for higher-risk principals, particularly those operating outside the city centre.",
            "licensing": "Security companies in the Kurdistan Region of Iraq are licensed by the Kurdistan Regional Government Ministry of Interior. This is separate from the Baghdad-based federal licensing framework. KRG-licensed operators are required for all commercial security activity in Erbil and the KRI.",
            "foreign_operators": "International security personnel may accompany principals into the KRI but require KRG Ministry of Interior permits for commercial security operations. International companies typically partner with KRG-licensed local entities."
        },
        "zones": {
            "safe": [
                "Ankawa district: Predominantly Christian suburb of Erbil. Primary expat residential area, with international hotels and restaurants. Generally the most secure residential zone.",
                "Ainkawa Road corridor: Main spine connecting the Citadel area to Ankawa. International hotels, embassies, and commercial offices. Highest security infrastructure density.",
                "Erbil Citadel area: City centre commercial and government zone. Active security presence."
            ],
            "elevated": [
                "Southern Erbil and approaches to Mosul road: Adjacent to contested territory. Not recommended for non-essential movement.",
                "Makhmour and areas south and west of Erbil: Historically affected by ISIL activity and remain elevated-risk."
            ]
        },
        "emergency": [
            ("Kurdistan Region Emergency Line", "104"),
            ("Erbil Emergency Hospital", "+964 66 226 2222"),
            ("German Hospital Erbil (best private facility)", "+964 66 258 8888"),
            ("British Embassy Baghdad (covers KRI)", "+964 7901 926 280"),
        ],
        "warnings": [
            "Erbil International Airport (EBL) has been targeted by rocket and drone attacks. Maintain awareness of the local emergency procedures and your accommodation's security protocols. Register with your embassy before arrival. Source: FCDO Iraq travel advice (2026).",
            "The KRI border with Syria and the area south of Erbil's administrative boundary retain a very high threat from ISIL insurgency and militia activity. Do not travel outside the KRI without a specific security assessment and armed support.",
            "The KRG-Baghdad relationship periodically deteriorates, affecting financial flows, oil export revenue, and occasionally civil servant salaries. Monitor political developments before extended deployments that depend on KRG contract stability."
        ],
        "faqs": [
            ("Is Erbil safe compared with the rest of Iraq?",
             "Erbil and the Kurdistan Region are substantially more stable than central and southern Iraq. The KRG maintains its own security forces (Peshmerga) and has kept ISIL from the city. However, the FCDO still advises against all but essential travel to the KRI, and Iran-aligned militia rocket and drone attacks on international targets in Erbil have continued. The risk picture is better than Baghdad but still significantly elevated compared with other major business cities. Source: FCDO Iraq travel advice (2026)."),
            ("What security configuration is standard for Erbil?",
             "Armed close protection with an armoured or reinforced vehicle is the standard configuration for senior principals visiting Erbil, particularly for movement outside the Ankawa-Ainkawa Road corridor. For routine office-based visits in the centre, a security driver with operations controller support is a minimum baseline. The KRG Ministry of Interior licensing framework should be verified for any provider."),
            ("Which industries drive business travel to Erbil?",
             "The Kurdistan Region's oil and gas sector is the primary driver, with BP, TotalEnergies, DNO, Genel Energy, and Gulf Keystone Petroleum among the international operators with active field programmes. Construction, telecommunications, and development finance have also grown alongside the KRG's relatively stable governance. NGO and UN agency activity remains significant given the displacement crisis context."),
            ("How do I verify a security company's credentials in Erbil?",
             "Security companies in Erbil must hold a licence from the Kurdistan Regional Government Ministry of Interior. Ask for the KRG Ministry of Interior licence number and verify it directly with the ministry before engagement. Companies operating without KRG licensing have no legal standing during incidents and create significant liability for the principal.")
        ]
    },
    "lahore": {
        "name": "Lahore",
        "country": "Pakistan",
        "risk_level": "high",
        "region": "South Asia",
        "related": [("Islamabad", "islamabad"), ("Karachi", "karachi"), ("Delhi", "delhi")],
        "city_body": """Lahore is Pakistan's second-largest city and the capital of Punjab province. It is the country's cultural, educational, and industrial heartland, home to the Lahore Stock Exchange, a significant textile and light manufacturing sector, and a large population of approximately 14 million. The city hosts important historical and cultural sites including the Lahore Fort, Badshahi Mosque, and Walled City. International business visitors travel primarily for trade, investment in manufacturing, and the growing technology sector.

## FCDO advisory

The FCDO advises against all travel to Pakistan's tribal areas, Balochistan, and areas within 10km of the border with Afghanistan and India (specific areas). For Lahore and Punjab more broadly, the FCDO advises against all but essential travel to certain areas and notes the high and unpredictable threat from terrorism across Pakistan. The FCDO specifically records that terrorist attacks including suicide bombings occur across Pakistan with little or no warning. Source: FCDO Pakistan travel advice (2026). US State Department Level 3 Do Not Travel advisory for Pakistan (2026).

## Terrorism and political violence

Pakistan experiences recurring terrorist attacks, with groups including Tehrik-e-Taliban Pakistan (TTP), Jaish-e-Mohammed, and Lashkar-e-Taiba active in the country. Lahore has experienced mass-casualty attacks in recent years, including attacks on markets, religious sites, and security forces. The Lahore environment requires constant situational awareness and active threat monitoring as part of any operational security programme.

*Sources: FCDO Pakistan travel advice (2026). US State Department Pakistan advisory (2026). Pakistan Security Management Alliance (PSMA) framework.*
For comparable operating environments, see our [Islamabad city briefing](/cities/islamabad/) and [Karachi city briefing](/cities/karachi/).""",
        "threats": [
            ("Terrorism",
             "Pakistan's terrorism threat is assessed as very high. Lahore has experienced multiple mass-casualty terrorist attacks targeting markets, religious gatherings, and security installations. The threat from TTP, sectarian groups, and other militant organisations is sustained. Attacks occur with little or no warning. Source: FCDO Pakistan travel advice (2026); US State Department Pakistan advisory (2026)."),
            ("Kidnapping",
             "The FCDO records a widespread kidnapping threat in Pakistan affecting foreigners. Criminal kidnap-for-ransom and politically motivated abduction have both occurred. International nationals are considered high-value targets. Movement in public without security measures is not appropriate for foreign principals. Source: FCDO Pakistan travel advice (2026)."),
            ("Political Instability",
             "Pakistan's political environment has been highly volatile, with mass protests, PTI-government tensions, and military-civilian friction creating periodic flashpoints. Demonstrations in Lahore have turned violent and have been met with security force responses. Monitor the political calendar closely. Source: FCDO Pakistan travel advice (2026).")
        ],
        "regulations": {
            "firearms": "Armed security is widely used in Lahore. Pakistan's private security sector operates under provincial regulatory frameworks. Punjab's Security Companies (Regulation) Act governs the licensing of security companies in Lahore. Armed CPO is available and is the standard configuration for international principals.",
            "licensing": "Security companies in Lahore require a licence from Punjab's Home Department under the Security Companies (Regulation) Act. Verify licence status with the Punjab Home Department before engagement. Individual armed personnel require weapons licences under Pakistan's Arms Ordinance.",
            "foreign_operators": "Foreign security personnel accompanying a principal require Pakistani government clearance for armed commercial operations. International companies partner with Punjab-licensed local entities to deliver ground operations."
        },
        "zones": {
            "safe": [
                "Gulberg: Primary expatriate and business district. International hotels, restaurants, and corporate offices. Best security infrastructure in the city.",
                "DHA (Defence Housing Authority) Phase 1-6: High-security residential and commercial area. Lower crime profile than other districts.",
                "Cantt (Cantonment): Military cantonment area with a controlled-access environment. Relatively secure."
            ],
            "elevated": [
                "Old City (Walled City): High visitor density, difficult vehicle access, historical attack targeting. Avoid without security overlay.",
                "Peripheral industrial districts: Higher crime profile and reduced security infrastructure.",
                "Areas near religious sites on significant religious dates: Elevated sectarian attack risk."
            ]
        },
        "emergency": [
            ("Police Emergency", "15"),
            ("Rescue Emergency", "1122"),
            ("Shaukat Khanum Memorial Cancer Hospital (best facility)", "+92 42 3576 1000"),
            ("Doctors Hospital Lahore", "+92 42 3591 0845"),
        ],
        "warnings": [
            "The terrorism threat in Lahore is high. Avoid all demonstrations and political gatherings. Do not travel to areas without a current security assessment. Carry emergency contact details at all times. Source: FCDO Pakistan travel advice (2026).",
            "Do not display wealth publicly. Expensive watches, jewellery, laptops, and camera equipment attract criminal attention. All movement between sites should use vetted, pre-booked transport. Do not hail street taxis or use unvetted ride-share apps.",
            "Medical facilities in Lahore vary significantly in quality. Shaukat Khanum Memorial Hospital provides internationally comparable care for serious cases. Medical evacuation insurance covering Dubai (approximately 3 hours by air) or Bangkok is advisable for extended deployments."
        ],
        "faqs": [
            ("What industries draw international visitors to Lahore?",
             "Lahore's textile and garment sector is the largest draw for international buyers and supply chain managers. Pakistan is one of the world's major cotton producers and garment exporters. Technology and software development, light manufacturing, and trade finance also generate corporate visits. The city's educational institutions attract academic and development sector visitors."),
            ("Is the FCDO advice against travel to Lahore specifically?",
             "The FCDO advises against all but essential travel to certain areas of Punjab and notes the high and unpredictable terrorism threat across Pakistan. Lahore itself falls within the category where essential travel is cautioned rather than prohibited, but the FCDO recommendation is to exercise extreme caution throughout Pakistan including Lahore. Source: FCDO Pakistan travel advice (2026)."),
            ("What is the minimum security baseline for a Lahore visit?",
             "A vetted security driver with an operations controller, accommodation in Gulberg or DHA, and a pre-travel security briefing is the minimum baseline for most international principals visiting Lahore. For higher-profile principals, deal-related visits, or movements outside the primary zones, a close protection officer alongside the driver is the appropriate standard. Source: FCDO Pakistan travel advice (2026)."),
            ("How does the political instability affect corporate operations in Lahore?",
             "Pakistan's recurring political crises, including the PTI-government confrontations of 2023-2024, have produced mass protests, communications disruptions, and intermittent internet shutdowns. Corporate operations dependent on continuity of communications or public movement need contingency planning for these periods. Monitor the political calendar and maintain a low-profile routine during heightened political events.")
        ]
    },
    "phnom-penh": {
        "name": "Phnom Penh",
        "country": "Cambodia",
        "risk_level": "moderate",
        "region": "Southeast Asia",
        "related": [("Bangkok", "bangkok"), ("Ho Chi Minh City", "ho-chi-minh-city"), ("Yangon", "yangon")],
        "city_body": """Phnom Penh is the capital and largest city of Cambodia, situated at the confluence of the Mekong and Tonle Sap rivers. The city is the political, economic, and cultural centre of Cambodia and has grown significantly since the post-Khmer Rouge reconstruction period. International business presence is concentrated in development finance, NGO operations, garment sector supply chain management, real estate, and an emerging technology and hospitality sector. The city has a substantial expatriate community and is well-served by international hotels and amenities by regional standards.

## FCDO advisory

The FCDO advises normal precautions for Cambodia overall, noting specific risks from crime, unexploded ordnance (UXO) in rural areas, and political context. Phnom Penh has seen periodic political unrest associated with elections and protests, with the authorities using force to disperse demonstrations on previous occasions. The political environment under Prime Minister Hun Manet (who succeeded his father Hun Sen in 2023) remains an authoritarian model with restrictions on civil society. Source: FCDO Cambodia travel advice (2026). US State Department Level 1 (Exercise Normal Precautions) advisory Cambodia (2026).

## Crime profile

Petty crime including bag snatching, pickpocketing, and phone theft is common in Phnom Penh. Motorbike-mounted theft (drive-by snatching) is the most frequently reported incident type affecting visitors. Armed robbery occurs, particularly after dark. Kidnapping is not a significant risk for standard business visitors, but express kidnapping affecting people who have withdrawn cash from ATMs has been documented.

*Sources: FCDO Cambodia travel advice (2026). US State Department Cambodia advisory (2026). Cambodia National Police crime reporting data.*
For comparable operating environments, see our [Bangkok city briefing](/cities/bangkok/) and [Ho Chi Minh City city briefing](/cities/ho-chi-minh-city/).""",
        "threats": [
            ("Petty Crime and Drive-By Theft",
             "Bag snatching from motorbikes is the most common crime affecting visitors to Phnom Penh. Phones, handbags, and camera straps are targeted. The risk is highest in tourist and market areas, around ATMs, and after dark in entertainment districts. Victims have been injured when dragged. Source: FCDO Cambodia travel advice (2026)."),
            ("Political Demonstrations",
             "Cambodia has a history of suppressing political opposition and civil society. Protests against the government have been dispersed by security forces using force on previous occasions. Election periods carry an elevated risk of political demonstrations. Source: FCDO Cambodia travel advice (2026)."),
            ("Scams and Fraud",
             "Tourist and business visitor scams are common in Phnom Penh, including taxi scams, gem scams, and confidence fraud. Online scam operations (a growing regional concern) have been linked to operations in Cambodia near the Thai border, though these affect remote workers rather than visiting executives.")
        ],
        "regulations": {
            "firearms": "Private security companies in Cambodia may hold licences for limited armed operations. In practice, most commercial security in Phnom Penh is unarmed. Armed security is used for high-value property protection and some diplomatic missions.",
            "licensing": "Security companies must register with Cambodia's Ministry of Interior under the Law on the Management of Private Bodyguards and Security Guards. Individual guards require registration and identification cards issued by the ministry.",
            "foreign_operators": "Foreign close protection personnel may accompany principals. Commercial security contracting requires local company registration with the Ministry of Interior."
        },
        "zones": {
            "safe": [
                "BKK1 (Boeung Keng Kang 1): Primary expatriate residential and commercial district. International hotels, restaurants, and NGO offices. Best urban security infrastructure.",
                "Daun Penh (around the National Museum and riverside): Commercial and government zone. Active during daytime with a reasonable security presence.",
                "Tonle Bassac and Chamkarmon: Growing commercial districts with good infrastructure."
            ],
            "elevated": [
                "Riverside and tourist areas after dark: Elevated bag snatching and robbery risk.",
                "Markets (Russian Market, Central Market): High footfall zones with documented pickpocketing.",
                "Outskirts and peripheral districts: Reduced security infrastructure and longer emergency response times."
            ]
        },
        "emergency": [
            ("Police", "117"),
            ("Ambulance", "119"),
            ("Royal Phnom Penh Hospital (best private facility)", "+855 23 991 000"),
            ("British Embassy Phnom Penh", "+855 23 427 124"),
        ],
        "warnings": [
            "Drive-by bag snatching from motorbikes is a regular occurrence in Phnom Penh. Do not carry bags over the shoulder on the street side. Keep phones in pockets rather than in hand. Be especially vigilant around ATMs and markets. Source: FCDO Cambodia travel advice (2026).",
            "The political environment in Cambodia restricts civil society and opposition activity. Avoid all political gatherings, demonstrations, and protests, which may be dispersed by security forces.",
            "Unexploded ordnance (UXO) from the Khmer Rouge period remains a risk in rural and peri-urban areas outside Phnom Penh. Do not venture off established roads in rural areas without local guidance."
        ],
        "faqs": [
            ("What industries bring international business visitors to Phnom Penh?",
             "The garment sector supply chain (Cambodia is a major garment exporter to the EU and USA), development finance and NGO operations, real estate investment, and a growing technology sector are the primary business travel drivers. UN agencies including UNHCR and UNDP maintain significant offices in Phnom Penh. Tourism infrastructure investment has also grown."),
            ("Is Phnom Penh high risk for international executives?",
             "Phnom Penh has a moderate risk profile relative to other cities in this security briefing network. The FCDO and US State Department advise normal precautions rather than elevated warnings for the city. The primary risks are petty crime and drive-by theft rather than terrorism or kidnap. A vetted transport arrangement and standard personal security awareness are typically sufficient for most corporate visits."),
            ("What medical facilities are available in Phnom Penh?",
             "Royal Phnom Penh Hospital is the best private facility in the city and provides a reasonable standard of care for most conditions. For serious trauma, evacuation to Bangkok (approximately 1 hour by air) is the standard response. Medical evacuation insurance with Bangkok coverage is advisable for any extended deployment."),
            ("Do I need close protection in Phnom Penh?",
             "For most standard corporate visits, a vetted driver and standard personal security awareness are sufficient. A close protection officer is appropriate for higher-profile principals, during election periods, or for movements to peripheral areas. The security environment does not routinely require CPO cover for typical business travel.")
        ]
    },
    "quito": {
        "name": "Quito",
        "country": "Ecuador",
        "risk_level": "high",
        "region": "Latin America",
        "related": [("Bogota", "bogota"), ("Lima", "lima"), ("Medellin", "medellin")],
        "city_body": """Quito is the capital of Ecuador, situated at approximately 2,850 metres altitude in the Andes. It is the political and administrative centre of Ecuador and a significant base for NGO and development finance operations, oil sector activity, and regional corporate headquarters. Ecuador's security environment has deteriorated significantly since 2022, driven by a surge in organised crime linked to narcotics trafficking, gang violence, and spillover from Colombian criminal organisations. The FCDO has elevated its Ecuador advisory substantially in response to this change.

## FCDO and State Department advisory

The FCDO advises against all but essential travel to several provinces of Ecuador including Esmeraldas, Manabi, Santa Elena, El Oro, Guayas (excluding Guayaquil city), and areas near the Colombian border. For Quito itself, the FCDO notes increased security incidents including kidnappings, shootings, and carjackings. The US State Department rates Ecuador at Level 3: Reconsider Travel, elevated from the prior Level 2 in response to the surge in gang violence. Source: FCDO Ecuador travel advice (2026). US State Department Ecuador advisory Level 3 (2026).

## The Ecuador security deterioration

Ecuador's security environment changed rapidly from 2022 onwards, driven by narcotics-linked criminal organisations expanding from coastal port areas into urban centres including Quito. The January 2024 prison escapes and live-television studio attack marked a public escalation. The government declared an internal armed conflict and deployed the military. Quito's city centre remains operational but the surrounding metropolitan area has seen an increase in violent crime, kidnapping, and armed robbery.

*Sources: FCDO Ecuador travel advice (2026). US State Department Level 3 Ecuador advisory (2026). Ecuador National Police crime statistics (2025).*
For comparable operating environments, see our [Bogota city briefing](/cities/bogota/) and [Lima city briefing](/cities/lima/).""",
        "threats": [
            ("Kidnapping and Express Kidnapping",
             "Kidnapping in Ecuador has increased significantly since 2022, including express kidnapping (short-term abduction for immediate financial gain, typically forcing withdrawals from ATMs or bank accounts). The risk affects both Ecuadorian residents and foreign nationals. Criminal organisations with Colombian cartel links have expanded their operations into urban areas including Quito. Source: FCDO Ecuador travel advice (2026)."),
            ("Armed Robbery and Carjacking",
             "Armed robbery, carjacking, and vehicle hijacking have increased across Quito, particularly in peripheral and commercial districts. The combination of narcotics-linked organised crime and economic pressure has elevated the crime profile significantly since 2022. Source: FCDO Ecuador travel advice (2026); US State Department Ecuador advisory (2026)."),
            ("Civil Unrest and Political Demonstrations",
             "Ecuador has a history of significant civil unrest. Indigenous-led protests have blocked major highways including routes to Quito. The January 2024 security crisis and subsequent military operations produced significant disruption. Political demonstrations can occur with limited notice. Source: FCDO Ecuador travel advice (2026).")
        ],
        "regulations": {
            "firearms": "Ecuador's private security sector is regulated by the Ministry of Government (Ministerio de Gobierno) through the Directorate of Specialised Security Services. Armed security is available and widely used. Licensed operators must hold authorisations for armed personnel from the Ministerio de Gobierno.",
            "licensing": "Private security companies in Ecuador must be registered with the Ministerio de Gobierno's Directorate of Specialised Security Services. Individual security personnel require individual registration and annual renewal.",
            "foreign_operators": "Foreign security personnel may accompany principals. Commercial security operations require local company registration with the Ministerio de Gobierno."
        },
        "zones": {
            "safe": [
                "La Mariscal and Gonzalez Suarez: Primary expatriate and diplomat residential zone in north Quito. International hotels, restaurants, and corporate offices. Best security infrastructure.",
                "Quito historic centre (La Ronda area during daylight): UNESCO World Heritage colonial centre. Active during daytime with security presence.",
                "Cumbaya: Eastern suburban valley with a large expatriate community. Lower crime profile than the city centre."
            ],
            "elevated": [
                "La Marin and south Quito: Higher crime rates and gang activity. Not on standard corporate visitor itineraries.",
                "Night-time movement throughout the city: Crime increases significantly after dark across all districts.",
                "Areas around Quito bus terminals: High theft risk."
            ]
        },
        "emergency": [
            ("Police Emergency", "101"),
            ("ECU 911 (combined emergency)", "911"),
            ("Hospital Metropolitano (best private facility)", "+593 2 399 8000"),
            ("British Embassy Quito", "+593 2 397 2200"),
        ],
        "warnings": [
            "Ecuador's security environment has deteriorated significantly since 2022. Kidnapping, armed robbery, and carjacking have all increased. All principals should implement a comprehensive security plan before and during any Quito visit. Source: FCDO Ecuador travel advice (2026); US State Department Level 3 advisory (2026).",
            "Do not use informal taxis or unverified ride-share drivers in Quito. Virtual kidnapping and express kidnapping have been facilitated through informal transport. Pre-booked vetted transport from trusted operators is the only acceptable standard.",
            "The altitude of Quito (approximately 2,850 metres) affects visitors arriving from sea level, causing altitude sickness symptoms including headache, nausea, and shortness of breath. Allow 24-48 hours of acclimatisation before conducting strenuous meetings or site visits."
        ],
        "faqs": [
            ("Why has Ecuador's security situation deteriorated?",
             "Ecuador's position between Colombia and Peru made it a transit country for narcotics trafficking. Between 2022 and 2025, major cartels including Los Lobos and R7 gang networks expanded from port cities into the interior, including Quito. The collapse of prison security culminating in the January 2024 escapes triggered a declared internal armed conflict. The government's military response has had partial effect, but the underlying criminal economy continues to drive violence. Source: US State Department Ecuador advisory Level 3 (2026)."),
            ("Is Quito appropriate for standard corporate travel?",
             "Corporate travel to Quito is conducted by oil sector, NGO, development finance, and government-affairs professionals on a routine basis. The appropriate security baseline has increased significantly since 2022. Pre-booked vetted transport, accommodation in La Mariscal or Cumbaya, an operations controller, and a current threat briefing are the minimum standard. Senior executives with a higher profile should consider a CPO overlay."),
            ("What medical facilities are available in Quito?",
             "Hospital Metropolitano is Quito's best private facility and provides a good standard of care for most conditions. For complex trauma or serious medical events, evacuation to Miami (approximately 4 hours by air) or Bogota (approximately 1 hour) is the planning assumption. Medical evacuation insurance is advisable for all Ecuador deployments."),
            ("How does altitude affect security operations in Quito?",
             "Altitude affects both the principal and the security team. Physical exertion (including emergency extractions) is significantly more demanding at 2,850 metres. Vehicle performance is also affected. Security planning for Quito should account for the reduced physical capacity of team members in the first 48-72 hours and should include acclimatisation time before any high-intensity activities.")
        ]
    },
    "port-harcourt": {
        "name": "Port Harcourt",
        "country": "Nigeria",
        "risk_level": "high",
        "region": "West Africa",
        "related": [("Lagos", "lagos"), ("Abuja", "abuja"), ("Luanda", "luanda")],
        "city_body": """Port Harcourt is the capital of Rivers State and the commercial centre of Nigeria's Niger Delta oil region. The city is the operational base for most major international oil companies active in Nigeria, including Shell, TotalEnergies, Chevron, and Eni, and for a substantial supporting service and logistics industry. International business visitors travel to Port Harcourt primarily for oil field services, pipeline operations, LNG (via the Bonny Island facility), and associated legal and financial services.

## FCDO advisory

The FCDO advises against all travel to the riverine areas of Delta, Bayelsa, Rivers, Akwa Ibom, and Cross River states. Port Harcourt city itself falls within Rivers State, which the FCDO advises against all but essential travel to (non-riverine areas). The combination of armed militancy, oil bunkering criminal networks, kidnapping, and general crime makes Port Harcourt one of the most operationally demanding environments in West Africa. Source: FCDO Nigeria travel advice (2026). US State Department Level 3 Reconsider Travel Nigeria advisory (2026).

## The Niger Delta security context

The Niger Delta has experienced decades of armed militancy related to oil revenue distribution grievances. While the amnesty programme of 2009 reduced large-scale attacks on oil infrastructure, criminal oil bunkering, armed robbery on waterways, and kidnapping for ransom remain significant operational threats. Foreign oil sector personnel are considered high-value kidnap targets. Security protocols for the Niger Delta involve a level of operational complexity not required in most other African business cities.

*Sources: FCDO Nigeria travel advice (2026). US State Department Nigeria advisory Level 3 (2026). Nigerian Oil Producers Trade Section (OPTS) security protocols.*
For comparable operating environments, see our [Lagos city briefing](/cities/lagos/) and [Luanda city briefing](/cities/luanda/).""",
        "threats": [
            ("Kidnapping",
             "Port Harcourt and the broader Niger Delta region have one of the highest kidnapping rates in West Africa. Criminal kidnapping for ransom targeting foreign nationals and wealthy Nigerians is well documented. Oil sector personnel are considered high-value targets and are specifically sought by criminal networks. The FCDO Nigeria travel advice (2026) records kidnapping as a major threat in Rivers State."),
            ("Armed Robbery and Militancy",
             "Armed robbery, carjacking, and attacks by armed criminal groups are documented across Port Harcourt. The city's peripheral areas and waterway approaches carry the highest risk. Oil infrastructure sabotage and attacks on vessels in the Niger Delta creeks continue, primarily linked to oil bunkering criminal networks. Source: FCDO Nigeria travel advice (2026)."),
            ("Piracy on Waterways",
             "Waterway access to and from Port Harcourt, including the Bonny Island LNG facility approach, carries a piracy and armed robbery risk. Armed attacks on vessels and kidnappings of crew and passengers on Delta waterways are recorded. Any movement by boat in the Delta requires specific security assessment and armed escort. Source: Nigerian Navy and MEND monitoring data.")
        ],
        "regulations": {
            "firearms": "Armed security is standard in Port Harcourt for oil sector operations and for protection of senior principals. Nigeria's private security sector is regulated by the Nigeria Security and Civil Defence Corps (NSCDC) under the Private Guard Companies Act (Cap P29). Armed operators require specific NSCDC authorisation.",
            "licensing": "Private security companies in Nigeria must hold a NSCDC licence. The NSCDC maintains a publicly accessible register of licensed companies. Individual armed guards require individual NSCDC registration and weapons permits from the Nigerian Police Force.",
            "foreign_operators": "Foreign security personnel may accompany principals. Commercial security operations require a NSCDC-licensed Nigerian partner company. Oil sector operations often use international security management companies in partnership with NSCDC-licensed local providers."
        },
        "zones": {
            "safe": [
                "GRA (Government Residential Area) Phase 1 and Phase 2: Primary expatriate residential zone. International oil company guesthouses and hotels. Higher security infrastructure density.",
                "Trans-Amadi Industrial Area: Primary oil services and logistics hub. Controlled access environment during business hours.",
                "Airport Hotel area and Port Harcourt International Airport vicinity: International standard facilities with security."
            ],
            "elevated": [
                "Waterfront areas and creek access points: High kidnapping and armed robbery risk. No movement without security escort.",
                "Peripheral city areas (Mile 1 Market, Rumuola): Elevated crime profile.",
                "Night-time movement throughout the city: All after-dark movement requires security overlay."
            ]
        },
        "emergency": [
            ("Emergency (Police)", "199"),
            ("Rivers State Emergency Management Agency", "+234 84 462 020"),
            ("Braithwaite Memorial Specialist Hospital", "+234 84 231 544"),
            ("British Deputy High Commission Port Harcourt", "+234 84 611 700"),
        ],
        "warnings": [
            "Kidnapping is a serious and documented threat in Port Harcourt. Foreign oil sector personnel are specifically targeted. No movement outside secured compounds without vetted armed security. Source: FCDO Nigeria travel advice (2026).",
            "Waterway travel in the Niger Delta carries a piracy and armed robbery risk. Movement by boat, including to Bonny Island, requires a specific security assessment and armed escort arrangement. Do not use informal water taxis.",
            "Night-time movement in Port Harcourt significantly increases risk exposure. All after-dark movements must use a vetted security driver with an operations controller. Avoid all exposure in public areas after dark."
        ],
        "faqs": [
            ("Is Port Harcourt the most dangerous city for oil sector operations in Nigeria?",
             "Port Harcourt and the broader Niger Delta carry a higher operational risk profile than Abuja and Lagos for oil sector personnel, primarily due to the kidnapping risk, waterway piracy, and the proximity of criminal oil bunkering networks. The FCDO advises against all travel to the riverine areas of Rivers State and against all but essential travel to non-riverine Rivers State. Source: FCDO Nigeria travel advice (2026)."),
            ("What security infrastructure do international oil companies use in Port Harcourt?",
             "International oil companies operating in Port Harcourt typically use a combination of NSCDC-licensed Nigerian security providers, international security management companies for programme oversight, and military maritime escorts for waterway movement. GRA-based compounds with access control, armed guard posts, and vehicle tracking are standard."),
            ("What is the medical situation in Port Harcourt?",
             "Medical facilities in Port Harcourt are limited compared with international standards. Braithwaite Memorial Specialist Hospital provides basic public sector care. For serious medical events, evacuation to Lagos (approximately 45 minutes by air) or London is the planning assumption. Medical evacuation insurance is mandatory for all Port Harcourt deployments."),
            ("Can I transit through Port Harcourt International Airport safely?",
             "Port Harcourt International Airport (PHC) has a reasonable security environment within the terminal. The risk is primarily in the approach roads and at the baggage carousel. Pre-booked inside-terminal collection with a vetted driver is the required standard. Do not accept transfers from unknown individuals.")
        ]
    },
    "kano": {
        "name": "Kano",
        "country": "Nigeria",
        "risk_level": "high",
        "region": "West Africa",
        "related": [("Abuja", "abuja"), ("Lagos", "lagos"), ("Bamako", "bamako")],
        "city_body": """Kano is northern Nigeria's largest city and the commercial capital of the north, with a population of approximately 4 million. It is a major hub for textile production, leather goods, and trans-Saharan trade, with a large wholesale market economy. Kano's Aliko Dangote (a Kano native) and other major northern Nigerian business families maintain significant industrial operations in the city. International business visitors travel primarily for manufacturing sector operations, trade, and increasingly for the agricultural commodities and telecoms sectors.

## FCDO advisory

The FCDO advises against all but essential travel to Kano State, noting the threat from terrorism including Boko Haram-linked groups, politically motivated intercommunal violence, and significant crime. Kano sits within the zone of Boko Haram and Islamic State West Africa Province (ISWAP) influence spillover from the north-east. The city has experienced bomb attacks in the past and the security environment remains elevated. Source: FCDO Nigeria travel advice (2026). US State Department Level 3 Nigeria advisory (2026).

## Political and religious dynamics

Kano is a predominantly Muslim city governed under a partly sharia-based legal framework in personal law matters. Religious sensitivities around dress, conduct, and interactions between men and women require specific awareness from international visitors. Political tensions between Kano's established political networks and state-level power have periodically produced civil unrest. Governor's-office transitions have historically been accompanied by demonstrations and violence.

*Sources: FCDO Nigeria travel advice (2026). US State Department Nigeria advisory Level 3 (2026). Nigerian Security and Civil Defence Corps (NSCDC) framework.*
For comparable operating environments, see our [Abuja city briefing](/cities/abuja/) and [Lagos city briefing](/cities/lagos/).""",
        "threats": [
            ("Terrorism and Boko Haram Spillover",
             "The FCDO advises against all but essential travel to Kano State, citing the threat from terrorism. Boko Haram and ISWAP have conducted attacks in northern Nigeria including in Kano and surrounding areas. Bomb attacks and targeted killings have occurred. The threat level is higher than in Lagos or Abuja. Source: FCDO Nigeria travel advice (2026)."),
            ("Intercommunal Violence",
             "Kano has experienced recurring intercommunal violence between different ethnic and religious communities, often triggered by political events, religious provocations, or resource disputes. These episodes can produce rapid escalation and movement restrictions across the city. Source: FCDO Nigeria travel advice (2026)."),
            ("Crime",
             "Violent crime including robbery and carjacking is documented in Kano. The economic pressures in northern Nigeria contribute to opportunistic crime targeting visitors, particularly in markets and at night. Source: FCDO Nigeria travel advice (2026).")
        ],
        "regulations": {
            "firearms": "Armed security is available in Kano through NSCDC-licensed providers. Given the elevated terrorism and intercommunal violence risk, armed CPO is the appropriate standard for foreign principals visiting the city.",
            "licensing": "Private security companies require NSCDC licences. The NSCDC Kano State Command licensing framework applies. Verify NSCDC licence numbers before engagement.",
            "foreign_operators": "Foreign security personnel may accompany principals. Commercial security contracting requires NSCDC-licensed Nigerian partner companies."
        },
        "zones": {
            "safe": [
                "Nassarawa GRA: Primary residential zone for senior government officials and business executives. Better security infrastructure.",
                "Kano State Government House area: Active security presence in and around government premises.",
                "Major international hotels (Tahir Guest Palace, Kampala International): International-standard security within the property."
            ],
            "elevated": [
                "Sabon Gari: Area with a predominantly southern Nigerian and Christian population. Has historically been a flashpoint for intercommunal tensions.",
                "Kano Central Market area: High footfall, elevated theft risk.",
                "Peripheral outskirts towards Daura and Kaduna roads: Elevated terrorism and robbery risk on highways."
            ]
        },
        "emergency": [
            ("Police Emergency", "199"),
            ("NEMA Kano Office", "+234 64 315 100"),
            ("Aminu Kano Teaching Hospital", "+234 64 660 100"),
            ("British Deputy High Commission Lagos (covers Kano)", "+234 1 277 0780"),
        ],
        "warnings": [
            "The terrorism threat in Kano is elevated compared with Lagos and Abuja. Bomb attacks and targeted violence have occurred in the city. Avoid all public gatherings and demonstrations, particularly around religious occasions and political events. Source: FCDO Nigeria travel advice (2026).",
            "Intercommunal violence in Kano can occur with very little warning and can rapidly restrict movement across the city. Have a pre-planned shelter-in-place protocol and confirmed emergency contact chain before arriving.",
            "Be respectful of local religious and cultural practices. During Ramadan, eating, drinking, and smoking in public during daylight hours can attract serious negative attention. Dress modestly and follow the conduct expectations of the local environment."
        ],
        "faqs": [
            ("Why do international businesses visit Kano?",
             "Kano is a major centre for Nigeria's textile, leather, and groundnut oil industries. The Dangote Group, BUA Group, and other northern Nigerian conglomerates have significant manufacturing and trading operations based in Kano. The city is also a major transit hub for trans-Saharan trade, including goods moving to and from Niger, Chad, and Libya."),
            ("Is Kano more dangerous than Lagos for business travel?",
             "Kano's terrorism risk from Boko Haram and ISWAP spillover is higher than Lagos, and the intercommunal violence risk is also elevated. The FCDO advises against all but essential travel to Kano State, which is a stronger caution than applies to Lagos. The appropriate security baseline for Kano is armed CPO, whereas a vetted driver with operations controller may be sufficient for some Lagos visits. Source: FCDO Nigeria travel advice (2026)."),
            ("What cultural considerations apply in Kano?",
             "Kano applies Islamic social norms more extensively than southern Nigerian cities. Female visitors should dress modestly, covering hair and wearing loose-fitting clothing. Avoid overt physical contact between men and women in public. During Ramadan, eating and drinking in public during daylight hours is inappropriate and may attract official attention. Alcohol is effectively unavailable in most of Kano outside private international hotel facilities."),
            ("What NSCDC licensing should a Kano security provider hold?",
             "All security companies in Kano must hold NSCDC (Nigeria Security and Civil Defence Corps) licences from the Kano State Command. The NSCDC maintains a register of licensed companies. Verify NSCDC licence documentation before engaging any provider. Unlicensed operators have no legal standing during security incidents.")
        ]
    },
    "douala": {
        "name": "Douala",
        "country": "Cameroon",
        "risk_level": "high",
        "region": "Central Africa",
        "related": [("Lagos", "lagos"), ("Kinshasa", "kinshasa"), ("Abidjan", "abidjan")],
        "city_body": """Douala is Cameroon's largest city and economic capital, home to the country's main seaport and the hub of its oil, forestry, agribusiness, and light manufacturing sectors. With a population of approximately 4 million, it is the commercial centre for much of Central Africa, with a large banking, logistics, and telecoms sector. International visitors travel primarily for oil sector operations, port and trade logistics, and the forestry and agribusiness industries.

## FCDO advisory and Anglophone crisis context

The FCDO advises against all but essential travel to the North-West and South-West regions of Cameroon due to the Anglophone crisis: armed separatist activity and military operations have produced significant violence and population displacement in these English-speaking regions. Douala itself is in Littoral Region and is not a direct conflict zone, but the crisis creates tensions and intermittent security incidents. The FCDO advises normal travel precautions for Douala and the wider Littoral Region, though noting ongoing crime risks. Source: FCDO Cameroon travel advice (2026). US State Department Level 2 Cameroon advisory (2026).

## Crime profile

Crime in Douala includes armed robbery, vehicle theft, and pickpocketing. The Akwa, Bonanjo, and Bonaberi districts carry distinct risk profiles. Douala's port area and night-time movement outside secured areas carry elevated risk. Security incidents at ATMs and in commercial markets are regularly reported.

*Sources: FCDO Cameroon travel advice (2026). US State Department Cameroon advisory Level 2 (2026). Cameroon Ministry of Interior security licensing framework.*
For comparable operating environments, see our [Lagos city briefing](/cities/lagos/) and [Kinshasa city briefing](/cities/kinshasa/).""",
        "threats": [
            ("Crime and Armed Robbery",
             "Petty crime, pickpocketing, and armed robbery are documented across Douala. The risk is highest in market areas, around ATMs, at night, and in the Akwa nightlife district. Vehicle theft is common. Source: FCDO Cameroon travel advice (2026)."),
            ("Anglophone Crisis Spillover",
             "The armed conflict in Cameroon's North-West and South-West regions between Anglophone separatists and government forces creates political tension in Douala, which has a significant Anglophone population. Demonstrations and occasional incidents related to the crisis occur in the city. Travel to the North-West or South-West regions from Douala requires a specific security assessment. Source: FCDO Cameroon travel advice (2026)."),
            ("Road Accidents and Transport Risk",
             "Road traffic accidents are a significant cause of harm in Cameroon. Poor road conditions, overloaded vehicles, and erratic driving are the primary risk factors. Night-time road travel outside secured areas is not recommended. Use vetted transport rather than public buses or informal taxis.")
        ],
        "regulations": {
            "firearms": "Private security companies in Cameroon must obtain authorisation from the Ministry of Territorial Administration (MINAT) for armed operations. Armed security is available for high-risk principals and site protection. The regulatory framework is less standardised than West African counterparts.",
            "licensing": "Security companies in Cameroon must hold authorisation from MINAT. Individual security personnel require registration and identification documentation. The licensing framework has been updated in recent years but enforcement capacity is limited.",
            "foreign_operators": "Foreign security personnel may accompany principals. Commercial security contracting requires MINAT authorisation, typically through a locally registered partner company."
        },
        "zones": {
            "safe": [
                "Bonanjo: Administrative and business district. Government ministries, banks, and some international company offices. Active security presence.",
                "Bastos equivalent zone (Bonapriso): Expatriate residential area. International hotels and restaurants. Better security infrastructure.",
                "Akwa (daytime): Main commercial district during business hours. Elevated pickpocketing risk but active police presence during the day."
            ],
            "elevated": [
                "Akwa at night: Nightlife district with elevated armed robbery and assault risk after dark.",
                "Port approaches and Bonaberi industrial area: Access-controlled during business hours but peripheral areas carry elevated crime.",
                "Bassa and peripheral industrial suburbs: Higher crime profile."
            ]
        },
        "emergency": [
            ("Police Emergency", "17"),
            ("Fire and Emergency", "18"),
            ("Clinique Bastos (best private facility)", "+237 22 221 4343"),
            ("British High Commission Yaounde (covers Douala)", "+237 22 222 0545"),
        ],
        "warnings": [
            "Armed robbery occurs in Douala, including in commercial and hotel areas. Do not display expensive equipment, watches, or cash in public. Use pre-booked vetted transport for all movements. Source: FCDO Cameroon travel advice (2026).",
            "Do not travel to Cameroon's North-West or South-West regions without a specific security assessment. The FCDO advises against all but essential travel to these regions due to the Anglophone armed conflict. Travel beyond Douala requires a current security briefing.",
            "Medical facilities in Douala are limited compared with international standards. For serious cases, evacuation to Paris or Johannesburg is the standard planning assumption. Medical evacuation insurance is advisable for all deployments."
        ],
        "faqs": [
            ("Why is Douala a regional commercial hub?",
             "Douala's deep-water port is the largest in Central Africa and handles the majority of Cameroon's imports and exports, as well as significant transit goods for landlocked neighbours including Chad and the Central African Republic. The oil sector, operated primarily by TotalEnergies through the Chad-Cameroon pipeline terminal at Kribi and onshore fields, adds significant international business activity. Forestry, agribusiness, and telecoms complete the commercial picture."),
            ("How does the Anglophone crisis affect business operations in Douala?",
             "Douala itself is in Littoral Region and is not directly affected by the armed conflict in the North-West and South-West. However, the presence of a large Anglophone diaspora in Douala means that tensions from the conflict create occasional demonstrations and incidents in the city. Access to the English-speaking regions for site visits requires a specific security assessment and armed support."),
            ("What is the standard security baseline for Douala?",
             "A vetted security driver with an operations controller and accommodation in Bonanjo or Bonapriso is the standard baseline for most corporate visits. For senior principals or visits involving high-value commercial activity, a close protection officer alongside the driver is the appropriate standard. Night-time movement outside secured premises requires a security overlay."),
            ("Which regulatory body licenses security companies in Douala?",
             "Security companies in Cameroon must hold authorisation from the Ministry of Territorial Administration (MINAT). Verify MINAT authorisation before engaging any security provider. The licensing framework requires annual renewal and individual staff registration.")
        ]
    },
    "santo-domingo": {
        "name": "Santo Domingo",
        "country": "Dominican Republic",
        "risk_level": "moderate",
        "region": "Caribbean",
        "related": [("Bogota", "bogota"), ("Panama City", "panama-city"), ("Miami", "miami")],
        "city_body": """Santo Domingo is the capital of the Dominican Republic and the oldest European-founded city in the Americas. With a population of approximately 3.5 million in the metropolitan area, it is the largest city in the Caribbean and a significant regional financial, legal, and business centre. The city hosts the headquarters of major Caribbean conglomerates, a growing free trade zone sector, and significant international hotel and tourism infrastructure. The Dominican Republic has maintained relatively stable economic growth and political continuity by Caribbean standards.

## FCDO advisory

The FCDO advises normal travel precautions for the Dominican Republic, noting crime as the principal risk. Violent crime including armed robbery and homicide is concentrated in specific districts and neighbourhoods, particularly Boca Chica, certain areas of the capital, and areas near the Haitian border. The tourist and business districts of Santo Domingo (Piantini, Naco, and the Colonial Zone) have a better security profile than peripheral areas. Source: FCDO Dominican Republic travel advice (2026). US State Department Level 2 Dominican Republic advisory (2026).

## The business environment

Santo Domingo serves as a commercial hub for the Caribbean and for broader trade with the Dominican Republic's largest partners: the United States, Haiti, and the European Union. The city is a base for Caribbean-wide free trade zone operations (Las Americas, San Pedro de Macoris), tourism investment, and a growing technology and call-centre sector. The legal and financial services sector serves significant Dominican diaspora interests in the United States.

*Sources: FCDO Dominican Republic travel advice (2026). US State Department Level 2 Dominican Republic advisory (2026). Dominican Republic Interior and Police Ministry security framework.*
For comparable operating environments, see our [Bogota city briefing](/cities/bogota/) and [Panama City city briefing](/cities/panama-city/).""",
        "threats": [
            ("Crime and Armed Robbery",
             "Crime is the primary risk in Santo Domingo. Armed robbery and mugging occur in tourist and commercial areas as well as peripheral neighbourhoods. The FCDO specifically notes violent crime in Boca Chica. Carjacking is documented. Source: FCDO Dominican Republic travel advice (2026)."),
            ("Express Kidnapping",
             "Express kidnapping, where victims are held briefly for forced ATM withdrawals, has been reported in Santo Domingo. Incidents are primarily associated with informal transport use and isolated movement after dark. Source: US State Department Dominican Republic advisory Level 2 (2026)."),
            ("Road Safety",
             "Traffic accidents are a significant cause of harm in the Dominican Republic. Driving standards are poor, motorbike use is widespread, and road conditions outside major arteries can be poor. Use vetted transport rather than driving independently in Santo Domingo.")
        ],
        "regulations": {
            "firearms": "Private security companies in the Dominican Republic may be licensed for armed operations under the Ministry of Interior and Police framework. Armed security is available and widely used for high-value commercial and residential applications.",
            "licensing": "Security companies in the Dominican Republic must hold licences from the Ministry of Interior and Police (Ministerio de Interior y Policia). Individual armed security personnel require separate registration and weapons authorisation.",
            "foreign_operators": "Foreign close protection personnel may accompany principals. Commercial security operations require a locally registered and licensed Dominican company."
        },
        "zones": {
            "safe": [
                "Piantini: Primary expatriate and business residential district. International hotels, corporate offices, and restaurants. Good security infrastructure.",
                "Naco: Commercial and residential district adjacent to Piantini. International companies and financial offices.",
                "Colonial Zone (daytime): UNESCO Heritage colonial centre. Good security during business hours with tourist police presence."
            ],
            "elevated": [
                "Boca Chica beach area: The FCDO specifically notes violent crime risk in this area.",
                "Peripheral barrios (Capotillo, Villa Juana, Villa Consuelo): Higher crime profile. Not on standard corporate visitor routes.",
                "Night-time movement in areas outside Piantini/Naco: Elevated robbery risk after dark throughout the city."
            ]
        },
        "emergency": [
            ("Police Emergency", "911"),
            ("Fire and Medical Emergency", "911"),
            ("Centro Medico Nacional Siglo XXI", "+1 809 540 1000"),
            ("Hospital General Plaza de la Salud (best private)", "+1 809 565 7477"),
        ],
        "warnings": [
            "Crime including armed robbery is a significant risk in Santo Domingo, particularly in peripheral areas and after dark. Use pre-booked vetted transport for all movements. Do not walk between locations after dark in unfamiliar areas. Source: FCDO Dominican Republic travel advice (2026).",
            "Informal taxis and unlicensed transport are associated with express kidnapping incidents. Use only pre-booked reputable transport services or hotel-arranged taxis. Never accept a lift from an unmarked or unidentified vehicle.",
            "The Haitian border area and specific provincial towns carry a significantly higher risk profile than Santo Domingo. Do not travel to border areas without a current security assessment. The political instability in Haiti creates periodic spillover effects into Dominican border regions."
        ],
        "faqs": [
            ("Why is Santo Domingo a Caribbean commercial hub?",
             "The Dominican Republic is the largest economy in the Caribbean and Central American region. Santo Domingo hosts the headquarters of major Dominican conglomerates active in construction, food and beverage, banking, and telecoms. The city's free trade zones, including Las Americas and San Pedro de Macoris nearby, are significant exporters to the United States under the CAFTA-DR trade agreement. Tourism investment, call-centre operations, and a growing technology sector also draw international business."),
            ("Is the Dominican Republic safe relative to other Caribbean destinations?",
             "The FCDO and US State Department both rate the Dominican Republic at their lower advisory levels (normal precautions and Level 2 respectively), reflecting a moderate rather than high security environment. The primary risk is crime rather than terrorism or kidnapping on the scale seen in some Latin American capitals. For a Caribbean destination, the risk profile is comparable to Jamaica and higher than the smaller island states. Source: FCDO Dominican Republic travel advice (2026)."),
            ("What security is needed for a standard Santo Domingo business visit?",
             "For most corporate visits to Santo Domingo, a vetted driver with accommodation in Piantini or Naco is a reasonable baseline. Standard personal security awareness, including not displaying valuables and using pre-booked transport, is the primary risk mitigation. A close protection officer is appropriate for higher-profile principals or those conducting high-value financial activity."),
            ("What is the political environment in the Dominican Republic?",
             "The Dominican Republic has maintained democratic governance since the 1990s, with peaceful power transfers between parties. President Luis Abinader's administration has pursued anti-corruption measures and continued relatively stable economic management. The political risk for business visitors is low by regional standards. The primary concern is the country's relationship with Haiti and the management of border security and migration.")
        ]
    }
}

SERVICE_DATA = {
    "bodyguard-hire": {
        "title_prefix": "Bodyguard Hire in",
        "h1_prefix": "Bodyguard Hire in",
        "seo_prefix": "Bodyguard Hire",
        "seo_suffix": "Close Protection",
        "slug_service": "bodyguard-hire",
        "cta_suffix": "Request a licensed bodyguard briefing for your visit.",
    },
    "security-drivers": {
        "title_prefix": "Security Drivers in",
        "h1_prefix": "Security Drivers in",
        "seo_prefix": "Security Drivers",
        "seo_suffix": "Secure Transport",
        "slug_service": "security-drivers",
        "cta_suffix": "Request a vetted security driver for your visit.",
    },
    "executive-protection": {
        "title_prefix": "Executive Protection in",
        "h1_prefix": "Executive Protection in",
        "seo_prefix": "Executive Protection",
        "seo_suffix": "EP",
        "slug_service": "executive-protection",
        "cta_suffix": "Request an executive protection programme for your visit.",
    },
    "residential-security": {
        "title_prefix": "Residential Security in",
        "h1_prefix": "Residential Security in",
        "seo_prefix": "Residential Security",
        "seo_suffix": "Expat Security",
        "slug_service": "residential-security",
        "cta_suffix": "Request a residential security assessment.",
    },
}


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  WROTE {path}")


def make_city_page(slug, data):
    threats_yaml = ""
    for t_type, t_detail in data["threats"]:
        threats_yaml += f'  - type: "{t_type}"\n    detail: "{t_detail}"\n'

    available_yaml = """  - name: "Security Drivers"
    description: "Vetted, licensed security drivers for airport transfers and in-city movement."
  - name: "Bodyguard Hire"
    description: "Close protection officers for senior principals and visiting executives."
  - name: "Executive Protection"
    description: "Structured EP programmes for principals with elevated risk profiles."
  - name: "Risk Assessment"
    description: "Pre-travel security assessment covering the current threat environment."
"""

    regulations = data["regulations"]
    zones = data["zones"]
    emergency = data["emergency"]
    warnings = data["warnings"]
    related = data["related"]
    faqs = data["faqs"]

    zones_yaml = "  safe:\n"
    for z in zones["safe"]:
        zones_yaml += f'    - "{z}"\n'
    zones_yaml += "  elevated:\n"
    for z in zones["elevated"]:
        zones_yaml += f'    - "{z}"\n'

    emergency_yaml = ""
    for svc, num in emergency:
        emergency_yaml += f'  - service: "{svc}"\n    number: "{num}"\n'

    warnings_yaml = ""
    for w in warnings:
        warnings_yaml += f'  - "{w}"\n'

    related_yaml = ""
    for rname, rslug in related:
        related_yaml += f'  - name: "{rname}"\n    slug: "{rslug}"\n'

    faqs_yaml = ""
    for q, a in faqs:
        faqs_yaml += f'  - question: "{q}"\n    answer: "{a}"\n'

    city_name = data["name"]
    country = data["country"]
    desc = f"Close protection and executive security in {city_name}, {country}. Security drivers, bodyguard hire, and risk assessment for international business visitors."
    if len(desc) > 175:
        desc = desc[:175]
    seo_title = f"Close Protection {city_name} | Bodyguard Hire {country}"
    if len(seo_title) > 70:
        seo_title = f"Close Protection {city_name} | {country} Security"
    if len(seo_title) > 70:
        seo_title = seo_title[:70]

    content = f"""---
title: "{city_name}"
description: "{desc}"
slug: "{slug}"
h1: "Close Protection in {city_name}, {country}"
country: "{country}"
risk_level: "{data['risk_level']}"
hero_image: "Close-Protection-2560.webp"
seo_title: "{seo_title}"
date: "2026-06-08"
threats:
{threats_yaml}available_services:
{available_yaml}regulations:
  firearms: "{regulations['firearms']}"
  licensing: "{regulations['licensing']}"
  foreign_operators: "{regulations['foreign_operators']}"
zones:
{zones_yaml}emergency_contacts:
{emergency_yaml}warnings:
{warnings_yaml}related_cities:
{related_yaml}faqs:
{faqs_yaml}---

{data['city_body']}
"""
    return content


def make_service_page(city_slug, city_data, service_slug, service_data):
    city_name = city_data["name"]
    country = city_data["country"]
    risk = city_data["risk_level"]
    region = city_data["region"]

    svc_title = service_data["title_prefix"]
    seo_pre = service_data["seo_prefix"]
    seo_suf = service_data["seo_suffix"]

    title = f"{svc_title} {city_name}"
    h1 = f"{service_data['h1_prefix']} {city_name}, {country}"
    seo_title = f"{seo_pre} {city_name} | {seo_suf} {country}"
    if len(seo_title) > 70:
        seo_title = f"{seo_pre} {city_name} | {country}"
    if len(seo_title) > 70:
        seo_title = seo_title[:70]

    desc_map = {
        "bodyguard-hire": f"Licensed bodyguard hire in {city_name}, {country}. CPO teams covering the local threat environment, airport management, and vetted transport for visiting executives.",
        "security-drivers": f"Vetted security drivers in {city_name}, {country}. Licensed operators covering airport transfers, in-city movement, and operations controller tracking for business visitors.",
        "executive-protection": f"Executive protection in {city_name}, {country}. Licensed EP programmes covering the current threat environment for senior principals and corporate visitors.",
        "residential-security": f"Residential security in {city_name}, {country}. Licensed operators for compound security, staff vetting, and emergency planning for expatriates and NGO personnel.",
    }
    description = desc_map[service_slug]
    if len(description) > 175:
        description = description[:175]

    cta = f"Visiting {city_name}? {service_data['cta_suffix']}"

    risk_map = {"moderate": "moderate", "high": "high", "critical": "critical"}

    # Generate components and FAQs based on service type and city
    if service_slug == "bodyguard-hire":
        components, faqs = make_bodyguard_components(city_slug, city_data)
    elif service_slug == "security-drivers":
        components, faqs = make_drivers_components(city_slug, city_data)
    elif service_slug == "executive-protection":
        components, faqs = make_ep_components(city_slug, city_data)
    elif service_slug == "residential-security":
        components, faqs = make_residential_components(city_slug, city_data)

    components_yaml = ""
    for comp_title, comp_desc in components:
        components_yaml += f'  - title: "{comp_title}"\n    description: "{comp_desc}"\n'

    faqs_yaml = ""
    for q, a in faqs:
        faqs_yaml += f'  - question: "{q}"\n    answer: "{a}"\n'

    # Body text
    other_service = get_other_service(service_slug)
    body = make_service_body(city_slug, city_data, service_slug, other_service)

    content = f"""---
title: "{title}"
description: "{description}"
slug: "{city_slug}"
h1: "{h1}"
seo_title: "{seo_title}"
service: "{service_slug}"
city: "{city_name}"
country: "{country}"
risk_level: "{risk}"
hero_image: "Close-Protection-2560.webp"
date: "2026-06-08"
cta_text: "{cta}"
components:
{components_yaml}faqs:
{faqs_yaml}---

{body}
"""
    return content


def get_other_service(service_slug):
    others = {
        "bodyguard-hire": ("security drivers", "security-drivers"),
        "security-drivers": ("bodyguard hire", "bodyguard-hire"),
        "executive-protection": ("security drivers", "security-drivers"),
        "residential-security": ("close protection officers", "close-protection-officers"),
    }
    return others[service_slug]


def make_bodyguard_components(slug, city):
    name = city["name"]
    country = city["country"]
    risk = city["risk_level"]
    region = city["region"]

    c1 = (f"Licensing Framework in {country}",
          f"All close protection operators in {name} must hold valid licensing from the relevant {country} regulatory authority. Our {name} bodyguard network operates through licensed, vetted partners with documented compliance records. Licence documentation is provided before deployment. Source: relevant {country} security regulatory framework.")
    c2 = (f"Airport Transfer Protocol at {name} International Airport",
          f"Inside-terminal collection before the principal exits the arrivals hall is the required standard for {name} airport transfers. The bodyguard enters the arrivals area before the principal clears immigration, waits at a pre-agreed collection point, and escorts the principal directly to the vehicle. No unescorted kerb-side wait. An operations controller maintains flight tracking and driver communication throughout the transfer.")
    c3 = ("Threat-Specific Counter-Protocols",
          f"The {name} bodyguard programme is built around the specific threat vectors documented in the city's current risk profile. {'Armed robbery and kidnapping counter-protocols apply.' if risk in ('high', 'critical') else 'Crime awareness and avoidance protocols apply.'} Route planning, vehicle discipline, and daily security briefings are calibrated to the {name} environment. Source: FCDO {country} travel advice (2026).")
    c4 = ("Vehicle and Movement Discipline",
          f"Security driver vehicle discipline in {name}: windows up and doors locked throughout all movements, pre-planned routing incorporating current incident intelligence, no extended stationary exposure at unmanaged locations, and operations controller check-in cadence maintained throughout every journey.")
    c5 = ("Medical and Emergency Planning",
          f"The bodyguard programme for {name} includes a documented medical emergency plan covering the best available local facility and, where local facilities are limited, the evacuation routing and medevac provider on retainer. Medical evacuation insurance is the baseline requirement for any {name} deployment.")

    components = [c1, c2, c3, c4, c5]

    faqs = [
        (f"What licensing must a {name} bodyguard company hold?",
         f"All commercial security companies in {country} must hold licensing from the relevant national or provincial regulatory authority. Verify licensing documentation before engaging any provider. Unlicensed operators have no legal standing during security incidents."),
        (f"Is armed bodyguard protection available in {name}?",
         f"{'Armed close protection is available in ' + name + ' through licensed operators. Armed CPO is the appropriate configuration for higher-risk principals given the documented threat environment.' if risk == 'high' else 'Armed and unarmed close protection are both available in ' + name + '. The appropriate configuration depends on the principal profile and specific activities.'}"),
        (f"What is the airport transfer protocol for {name}?",
         f"Inside-terminal collection with a pre-positioned vehicle is the standard protocol. The bodyguard meets the principal inside the arrivals hall before they exit to the kerb. An operations controller tracks the flight and maintains communication with the driver throughout the transfer from the airport to the principal's destination."),
        (f"What medical planning applies for a {name} bodyguard assignment?",
         f"The medical plan for every {name} assignment includes the best available local medical facility for initial stabilisation and, where local capability is limited, evacuation routing to the nearest internationally accredited hospital. Medevac provider contacts are confirmed active before the principal's arrival. Medical evacuation insurance is the baseline requirement.")
    ]
    return components, faqs


def make_drivers_components(slug, city):
    name = city["name"]
    country = city["country"]
    risk = city["risk_level"]

    c1 = (f"Licensed Driver Network in {name}",
          f"All security drivers in {name} are vetted through {country}'s relevant licensing framework, with police clearance documentation, valid commercial driving licences, and reference verification. Driver assignments are confirmed in writing before travel. Licence documentation is available on request.")
    c2 = (f"Airport Transfer at {name} International Airport",
          f"Pre-positioned vehicle, inside-terminal collection, and operations controller tracking from wheels-down through to confirmed safe arrival at destination is the standard protocol for {name} airport transfers. Night arrivals use a modified protocol appropriate to the local risk environment.")
    c3 = ("Vehicle Security Discipline",
          f"Security driver vehicle protocol in {name}: windows up and doors locked throughout all movements, pre-planned primary and secondary routes, no extended stationary exposure, and a live check-in cadence with the operations controller throughout every journey.")
    c4 = ("Zone Management and Route Intelligence",
          f"The {name} driver network maintains current intelligence on high-risk areas, road conditions, and incident locations. Route planning for each journey incorporates this intelligence. Movements to non-standard areas or outside the primary business zones require advance route assessment.")
    c5 = ("Operations Controller Coverage",
          f"Every {name} security driver engagement is backed by an operations controller who monitors the journey timeline, holds the emergency contact chain, and coordinates emergency response if required. Any missed check-in triggers an immediate welfare call.")

    faqs = [
        (f"Is a security driver necessary for {name}?",
         f"{'A vetted security driver is the minimum appropriate baseline for international business visits to ' + name + ' given the documented crime and threat environment. Informal taxis and unverified ride-share services are not appropriate.' if risk in ('high', 'critical') else 'A vetted security driver provides a significantly higher level of personal security than informal transport for visitors to ' + name + '.'}"),
        (f"What licensing must a {name} security driver hold?",
         f"Security drivers in {name} must hold a valid commercial driving licence and police clearance documentation. Security driver companies must hold the relevant national or provincial regulatory authority licence. Verify all documentation before engagement."),
        (f"How does the operations controller work for {name} transfers?",
         f"The operations controller monitors every transfer from departure to confirmed arrival. They track the vehicle's progress, maintain a check-in cadence with the driver, and activate the emergency protocol if any check-in is missed. They hold the principal's organisation's emergency contact chain and can coordinate with local emergency services if required."),
        (f"What is the airport transfer procedure for {name}?",
         f"The driver enters the arrivals terminal before the principal clears immigration and waits at a pre-agreed collection point. Inside-terminal collection eliminates unescorted kerb-side waiting. The vehicle is pre-positioned for immediate departure. The operations controller confirms flight arrival and adjusts timing accordingly.")
    ]

    components = [c1, c2, c3, c4, c5]
    return components, faqs


def make_ep_components(slug, city):
    name = city["name"]
    country = city["country"]
    risk = city["risk_level"]

    c1 = (f"Regulatory Framework for EP in {country}",
          f"Executive protection operations in {name} are delivered through operators licensed by the relevant {country} security regulatory authority. All EP providers must hold current licensing and provide documentation before deployment. Source: {country} security regulatory framework.")
    c2 = ("Principal Movement Programme",
          f"The EP programme for {name} covers the full principal movement cycle: airport arrivals, hotel accommodation, meetings at government offices or corporate premises, site visits where applicable, and airport departure. Advance work at each venue is completed before the principal's arrival. All movement routes are pre-assessed.")
    c3 = ("Threat and Risk Assessment",
          f"A pre-deployment risk assessment is completed for every {name} EP engagement, covering the current threat environment, the principal's specific profile and activities, and any heightened risk factors such as deal-related targeting, political calendar, or geographic exposures. Source: FCDO {country} travel advice (2026).")
    c4 = ("Team Configuration and Vehicle",
          f"EP team configuration in {name} is based on the principal's threat assessment. {'Armed CPO with an armoured or reinforced vehicle is the recommended configuration given the documented threat environment.' if risk in ('high', 'critical') else 'Unarmed or armed CPO with a reinforced vehicle is available depending on the principal profile.'} Driver selection is a core part of the programme, with local knowledge providing route flexibility.")
    c5 = ("Medical and Emergency Action Plan",
          f"Every {name} EP programme includes a documented emergency action plan covering medical emergency, vehicle compromise, political demonstration response, and shelter-in-place procedures. The plan names the receiving medical facility, evacuation routing, and the operations controller's emergency activation protocol.")

    faqs = [
        (f"Is armed executive protection available in {name}?",
         f"{'Armed EP is available in ' + name + ' through licensed operators. Given the threat environment, armed configuration is the recommended standard for senior principals and those with a higher-risk profile.' if risk in ('high', 'critical') else 'Both armed and unarmed EP configurations are available in ' + name + '. The appropriate configuration depends on the principal profile and threat assessment.'}"),
        (f"What does an EP programme cover in {name}?",
         f"A {name} EP programme covers the full principal movement cycle from airport arrival through to departure: advance work at all venues, close escort during movements, accommodation security liaison, and a documented emergency action plan. Daily security briefings are provided to the principal."),
        (f"How is the EP team configuration determined for {name}?",
         f"The team configuration is based on a pre-deployment threat assessment covering the principal's profile, activities, and the current {name} security environment. The assessment considers the specific threat vectors, any heightened risk periods, and the principal's movement programme. Configuration options range from a single security driver to a full CPO team with advance capabilities."),
        (f"What emergency planning is built into a {name} EP programme?",
         f"The emergency action plan for every {name} EP programme covers: medical emergency (naming the receiving facility and evacuation routing), vehicle compromise (contingency routing and shelter options), political demonstration response (avoidance protocols and contingency routing), and communications procedures. The plan is shared with the principal and their organisation before deployment.")
    ]

    components = [c1, c2, c3, c4, c5]
    return components, faqs


def make_residential_components(slug, city):
    name = city["name"]
    country = city["country"]
    risk = city["risk_level"]

    c1 = (f"Private Security Licensing in {country}",
          f"Residential security companies in {name} must hold licensing from the relevant {country} regulatory authority. Individual guards require registration and identity documentation. Verify licensing before engagement. Source: {country} security regulatory framework.")
    c2 = (f"Expatriate Residential Zones in {name}",
          f"The primary residential zones for expatriates and NGO personnel in {name} are concentrated in areas with the best available security infrastructure. Property selection should prioritise walled compounds with controlled vehicle and pedestrian access, generator backup, and proximity to vetted emergency response.")
    c3 = ("Property Security Survey and Hardening",
          f"A residential security survey for {name} covers: perimeter integrity (wall height, anti-climb), access control at vehicle and pedestrian gates, CCTV coverage with battery or generator backup, lighting with motion activation, and a safe room specification where the threat assessment warrants it. Surveys are refreshed after significant local incidents.")
    c4 = ("Domestic Staff Vetting",
          f"Domestic staff vetting in {name} uses identity document verification through the relevant {country} civil authority, police clearance records where available, and employment reference checks. A probationary period with restricted access to security-sensitive areas is applied before full access is granted.")
    c5 = ("Emergency Response and Medevac Planning",
          f"The residential security programme for {name} includes a documented emergency response plan covering the residential security team's role in the first response, contact protocols with local police and ambulance services, and medical evacuation routing where local facilities are insufficient for serious cases.")

    faqs = [
        (f"Which body licenses residential security companies in {name}?",
         f"Residential security companies in {name} must hold licensing from the relevant {country} regulatory authority. Verify licensing documentation before engaging any provider. Companies operating without valid licensing have no legal standing during security incidents."),
        (f"What infrastructure considerations affect residential security in {name}?",
         ("Power supply reliability, water availability, and internet connectivity are all variables that affect security system performance in " + name + ". Generator backup for security-critical systems is essential. Survey all infrastructure dependencies before finalising a residential security design." if risk in ("high", "critical") else "Standard infrastructure is generally available in " + name + "'s primary expatriate zones, but generator backup for security-critical systems is advisable as standard practice.")),
        (f"Is domestic staff insider risk a concern in {name}?",
         f"Insider risk from domestic staff is a documented pattern in many locations where residential security programmes operate. A structured vetting process using identity document verification, police clearance, and reference checks, combined with a probationary period with restricted access to security-sensitive areas, is the standard mitigation."),
        (f"What is the recommended medevac routing from {name}?",
         f"The appropriate medevac routing from {name} depends on the nature of the medical event and the available regional facilities. The programme includes pre-identified local facilities for initial stabilisation and documented evacuation routing to the nearest internationally accredited hospital. A medevac provider should be on retainer before the principal or staff move into the property.")
    ]

    components = [c1, c2, c3, c4, c5]
    return components, faqs


def make_service_body(city_slug, city, service_slug, other_service):
    name = city["name"]
    country = city["country"]
    risk = city["risk_level"]
    other_name, other_slug = other_service

    if service_slug == "bodyguard-hire":
        intro = f"Bodyguard hire in {name} operates within {country}'s licensing framework, with close protection officers drawn from a vetted partner network holding valid national security authorisation."
        body2 = f"\n\n## The {name} security environment\n\nThe current security environment in {name} requires a bodyguard programme calibrated to the specific documented threat vectors. {'Armed robbery, kidnapping, and political instability are among the principal risk factors.' if risk in ('high', 'critical') else 'Crime and regional threat factors are the principal drivers for security planning.'} Source: FCDO {country} travel advice (2026).\n\n## What bodyguard hire covers in {name}\n\nA {name} bodyguard programme covers airport transfers with inside-terminal collection, accommodation in vetted properties in the primary security zone, in-city movement with pre-planned routes and operations controller tracking, and a documented emergency action plan with medevac provisions."
    elif service_slug == "security-drivers":
        intro = f"Security drivers in {name} are licensed under {country}'s relevant regulatory framework, providing vetted transport for airport transfers and in-city movement with full operations controller support."
        body2 = f"\n\n## The {name} transport security environment\n\n{'Vetted, licensed transport is the minimum appropriate baseline for international business visitors to ' + name + ' given the documented threat profile.' if risk in ('high', 'critical') else 'A vetted security driver provides significantly better risk management than informal transport for visitors to ' + name + '.'} Source: FCDO {country} travel advice (2026).\n\n## What security drivers cover in {name}\n\nSecurity driver operations in {name} cover airport transfers with inside-terminal collection, in-city movement with pre-planned primary and secondary routes, vehicle discipline protocol throughout all journeys, and operations controller tracking from departure to confirmed arrival."
    elif service_slug == "executive-protection":
        intro = f"Executive protection in {name} is built around licensed {country} operators with current ground knowledge, providing a structured programme covering the principal's full movement cycle in the city."
        body2 = f"\n\n## The {name} EP environment\n\n{'The threat environment in ' + name + ' warrants a structured EP programme for senior principals, with armed capability and armoured vehicles as the recommended configuration.' if risk in ('high', 'critical') else 'EP in ' + name + ' provides a structured security overlay for the principal movement cycle, calibrated to the current threat assessment.'} Source: FCDO {country} travel advice (2026).\n\n## What executive protection covers in {name}\n\nAn EP programme in {name} covers the full principal movement cycle: advance work at all venues, close escort during movements, accommodation security liaison, daily route variation, a documented emergency action plan, and medevac provider confirmation before arrival."
    elif service_slug == "residential-security":
        intro = f"Residential security in {name} addresses the compound protection, staff vetting, and emergency planning requirements of expatriates, NGO personnel, and diplomats based in the city."
        body2 = f"\n\n## The residential environment in {name}\n\n{'Compound-based residential arrangements are standard for expatriates in ' + name + ', reflecting the ' + risk + ' threat environment. Structured compound security, infrastructure resilience, and staff vetting are the foundations of a functional residential protection programme.' if risk in ('high', 'critical') else 'Expatriate residential security in ' + name + ' addresses crime risk and the need for reliable emergency response arrangements.'} Source: FCDO {country} travel advice (2026).\n\n## What residential security covers in {name}\n\nA residential security programme in {name} covers static compound guarding, vehicle access control, perimeter and CCTV maintenance, domestic staff vetting, and emergency response coordination including medevac planning."

    footer = f"\n\nFor the full {name} security picture, see our [{name} city briefing](/cities/{city_slug}/). For principals requiring {other_name}, [{other_name} in {name}](/{other_slug}/{city_slug}/) covers the {country} programme."

    return intro + body2 + footer


def main():
    created = 0
    errors = []

    for slug, city_data in cities.items():
        # City page
        city_path = os.path.join(CONTENT, "cities", f"{slug}.md")
        if not os.path.exists(city_path):
            try:
                content = make_city_page(slug, city_data)
                write_file(city_path, content)
                created += 1
            except Exception as e:
                errors.append(f"CITY {slug}: {e}")
        else:
            print(f"  SKIP (exists) {city_path}")

        # Service pages
        for service_slug, service_data in SERVICE_DATA.items():
            svc_path = os.path.join(CONTENT, service_slug, f"{slug}.md")
            if not os.path.exists(svc_path):
                try:
                    content = make_service_page(slug, city_data, service_slug, service_data)
                    write_file(svc_path, content)
                    created += 1
                except Exception as e:
                    errors.append(f"SERVICE {service_slug}/{slug}: {e}")
            else:
                print(f"  SKIP (exists) {svc_path}")

    print(f"\nDone. Created {created} files.")
    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  {e}")
    return 0 if not errors else 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
