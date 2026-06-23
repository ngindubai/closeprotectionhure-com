#!/usr/bin/env python3
"""Block 5: 10 new P4 city pages (batch24)."""
import os

OUTPUT_DIR = "/home/user/closeprotectionhure-com/site/content/cities"
os.makedirs(OUTPUT_DIR, exist_ok=True)

pages = {}

# PORT MORESBY
pages["port-moresby.md"] = """---
title: "Port Moresby"
description: "Close protection and executive security in Port Moresby, Papua New Guinea. Bodyguard hire, security drivers, and risk assessment for PNG's capital."
slug: "port-moresby"
h1: "Close Protection in Port Moresby, Papua New Guinea"
country: "Papua New Guinea"
risk_level: "high"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Port Moresby | Bodyguard Hire PNG"
date: "2026-06-20"
threats:
  - type: "Raskol Gang Activity and Street Crime"
    detail: "Port Moresby has one of the highest violent crime rates in the Pacific. Raskol gangs operate across many suburban areas and are responsible for armed robberies, carjacking, and home invasions. ADB and UN agency reports have consistently rated Port Moresby among the most difficult operating environments in the region. The main business districts (Town, Gordons, Waigani) have better security presence but crime occurs across all areas."
  - type: "Carjacking and Vehicle Crime"
    detail: "Carjacking is a specific and common risk in Port Moresby, including on the Jacksons Airport approach road and the main Waigani Drive corridor. Vehicles stopped at intersections and in traffic are targeted. Compound-based movement with vetted security drivers and pre-planned routes is the standard operating model for business visitors."
  - type: "Kidnapping"
    detail: "Kidnap risk in Port Moresby is elevated relative to most Pacific capitals. Both random opportunistic abductions and targeted kidnaps for ransom have been recorded. Executives in the extractive, resources, and construction sectors are the primary targeting profile. FCDO and US State Department Level 3 advisories reference the kidnapping risk."
  - type: "Civil Unrest"
    detail: "Tribal and political tensions occasionally produce protest and civil unrest in Port Moresby. Election-period violence is a documented pattern in PNG's political history. Monitor local media and PNG Police Force advisories during periods of political activity."
available_services:
  - name: "Security Drivers"
    description: "Vetted drivers for Jacksons Airport transfers and in-city business movement. Essential for navigating Port Moresby's compound-to-compound operating model."
  - name: "Bodyguard Hire"
    description: "Close protection officers for executives in PNG's resources, construction, and government sectors."
  - name: "Executive Protection"
    description: "Full protective arrangements for senior executives. Includes residential security assessment and compound-based security planning."
  - name: "Risk Assessment"
    description: "Pre-travel risk assessment covering Port Moresby's gang crime environment, carjacking patterns, and kidnap risk. Site-specific assessment available for operations outside the capital."
regulations:
  firearms: "The PNG Police Force administers security firm licensing under the Security (Protection) Act 2004. Armed private security is available through licensed PNG operators. Firearms are common in Port Moresby's security environment given the threat level."
  licensing: "Security companies in PNG must hold a current licence under the Security (Protection) Act 2004, administered by the PNG Police Force. Licence verification is important given the variability in operator quality in the Port Moresby market."
  foreign_operators: "Foreign security personnel may operate in PNG in advisory and supervisory roles. Formal armed security roles require engagement of licensed local operators."
zones:
  safe:
    - "Town (CBD): Central business district with Port Moresby's highest concentration of security infrastructure. Government offices, banks, and major hotels. Requires compound-to-compound discipline even here."
    - "Waigani: Administrative and NGO hub north of Town. Parliament, government departments, and UN agencies. Better managed than suburban areas but not crime-free."
    - "Gordons: Industrial and commercial area. Key business address for resources and construction sector companies."
    - "Harbour City and Ela Beach Hotel zone: The Ela Beach area in Town includes some of the city's better-managed hotel and business infrastructure."
  elevated:
    - "Gerehu, Erima, 9 Mile: Major suburban settlements with very high gang crime rates. Not on standard corporate itineraries."
    - "Hohola and surrounding suburbs: High crime residential areas. Avoid after dark and without vetted transport."
    - "Port Moresby General (Public) Hospital Zone: The public hospital area in Boroko carries elevated crime risk."
    - "Rural PNG outside the capital: Mining and resource sites require their own security planning; this profile covers Port Moresby only."
emergency_contacts:
  - service: "PNG Police Force Emergency"
    number: "000"
  - service: "Port Moresby General Hospital"
    number: "+675 324 8200"
  - service: "Pacific International Hospital (private)"
    number: "+675 323 4400"
  - service: "Australian High Commission Port Moresby"
    number: "+675 300 9100"
  - service: "British High Commission Port Moresby"
    number: "+675 325 6677"
warnings:
  - "Port Moresby operates on a compound-to-compound model: movement between secured compounds by vetted vehicle is the standard approach for all business visitors. Solo movement, walking between destinations, and unvetted taxis are not appropriate for visitors in any part of the city."
  - "The Jacksons Airport approach road and the main Waigani Drive corridor are specific carjacking risk areas. Pre-arranged airport collection with a vetted driver is essential; do not accept transport from unvetted operators at the arrivals area."
  - "FCDO advises against all travel to some parts of PNG outside Port Moresby and issues a general high-risk advisory for the capital. US State Department rates PNG at Level 3: Reconsider Travel. Review both advisories before any PNG trip."
  - "Medical facilities in Port Moresby are limited. Pacific International Hospital provides the best available private care. For serious trauma or medical emergencies, medical evacuation to Australia (Brisbane or Cairns) is the appropriate response."
related_cities:
  - name: "Brisbane"
    slug: "brisbane"
  - name: "Sydney"
    slug: "sydney"
  - name: "Manila"
    slug: "manila"
faqs:
  - question: "Is Port Moresby safe for business travel?"
    answer: "Port Moresby is a viable business destination with functioning corporate infrastructure, but it requires a substantially higher level of security planning than most comparable regional capitals. The compound-to-compound operating model -- moving between secured locations by vetted vehicle only -- is the standard approach for all business visitors, not an exceptional measure. FCDO and US State Department both issue high-risk advisories. Crime targeting business visitors is the primary concern, followed by kidnap risk for principals in the resources and construction sectors."
  - question: "What sectors drive business travel to Port Moresby?"
    answer: "Papua New Guinea's economy is dominated by extractive industries: liquefied natural gas (the PNG LNG project operated by TotalEnergies and Santos), gold and copper mining, and forestry. Port Moresby hosts the corporate offices for PNG LNG operators, the Porgera gold mine (Barrick Gold), and the major mining sector service companies. Development finance (Asian Development Bank, World Bank) and the NGO sector are also significant employers of international business visitors."
  - question: "How do I get from Jacksons Airport to central Port Moresby safely?"
    answer: "Jacksons International Airport (POM) is 11 kilometres from the Town CBD. Pre-arranged collection with a vetted driver is the only appropriate method for arriving business visitors. Do not take unvetted taxis from the arrivals area. The driver should meet you inside the terminal building, not at the kerb. The airport approach road carries documented carjacking risk. Pre-arranged collection should be confirmed before departure from origin."
  - question: "What medical facilities are available in Port Moresby?"
    answer: "Pacific International Hospital in Boroko provides the best available private medical care in Port Moresby. Port Moresby General Hospital is the main public facility but is significantly under-resourced by international standards. For serious trauma, surgical emergencies, or conditions requiring intensive care, medical evacuation to Brisbane or Cairns (approximately 2 to 3 hours by air) is the standard response. Travel insurance with medical evacuation cover is a baseline requirement for any PNG trip."
  - question: "Do I need local security operators or can I bring my own team?"
    answer: "Formally armed security roles must be provided by licensed PNG operators under the Security (Protection) Act 2004. Foreign security advisers and close protection personnel may operate in advisory and supervisory roles. The practical approach for most visiting executives is to engage a PNG-licensed local security company for vehicle and residential security, with a foreign close protection adviser integrated where the principal's profile warrants it."
---

Port Moresby is the capital of Papua New Guinea, the most populous country in Melanesia and one of the world's most resource-rich developing economies. The city is the commercial hub for PNG's liquefied natural gas, gold and copper mining, and forestry sectors, and hosts the Pacific region's largest volume of extractive-industry international business travel outside Australia. It is also consistently rated among the most challenging urban security environments in the Pacific.

## The Port Moresby risk environment

Raskol gang activity, carjacking, and kidnap risk make Port Moresby a high-priority security planning destination. The compound-to-compound operating model -- movement between secured locations by vetted vehicle -- is not an exceptional measure but the standard operating procedure for all business visitors. FCDO rates PNG as requiring high precautions throughout the country. US State Department issues a Level 3 advisory.

## Security framework in PNG

The Security (Protection) Act 2004, administered by the PNG Police Force, governs private security company licensing. Operator quality varies significantly; licence verification and reference checking are important steps before engaging any Port Moresby security operator.

For close protection services in Port Moresby, see our [executive protection services](/services/executive-protection/) and [security drivers](/services/security-drivers/).
"""

# LILONGWE
pages["lilongwe.md"] = """---
title: "Lilongwe"
description: "Close protection and executive security in Lilongwe, Malawi. Security drivers, bodyguard hire, and risk assessment for southern Africa's agricultural capital."
slug: "lilongwe"
h1: "Close Protection in Lilongwe, Malawi"
country: "Malawi"
risk_level: "moderate"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Lilongwe | Bodyguard Hire Malawi"
date: "2026-06-20"
threats:
  - type: "Opportunistic Crime"
    detail: "Lilongwe's crime environment is characterised by opportunistic theft, bag snatching, and petty crime rather than organised violent crime at the level seen in South African or East African capitals. The Old Town market area and Lilongwe Bus Depot carry higher petty crime risk. FCDO advises normal security precautions for Malawi and notes that crime does occur."
  - type: "Carjacking and Vehicle Crime"
    detail: "Carjacking incidents are reported in Lilongwe, though at lower frequency than in Nairobi or Johannesburg. Incidents concentrate on approaches to ATM machines, isolated road sections at night, and the areas immediately outside Old Town. Vetted transport is the appropriate baseline for all business movement."
  - type: "Road Safety"
    detail: "Road traffic accidents are a significant cause of injury to foreign visitors in Malawi. Road quality outside Lilongwe is poor, night driving on rural roads is high-risk due to pedestrians and livestock, and vehicle maintenance standards are variable. A security driver who knows local road conditions is as much a road-safety resource as a security one."
  - type: "Political and Civil Environment"
    detail: "Malawi has a multi-party democracy that has operated with reasonable stability since 1994. The 2020 election annulment and subsequent re-run demonstrated functioning democratic institutions. Protests and demonstrations occur periodically but have not resulted in the level of violence seen in some regional neighbours. Monitor conditions around election periods."
available_services:
  - name: "Security Drivers"
    description: "Vetted drivers for Kamuzu International Airport transfers and in-city and regional business movement. Particularly important for out-of-town mining, agriculture, and development sector visits."
  - name: "Bodyguard Hire"
    description: "Close protection officers for development finance, government, and extractive sector principals in Malawi."
  - name: "Executive Protection"
    description: "Security arrangements for executives working in Malawi's tobacco, mining, and agricultural sectors."
  - name: "Risk Assessment"
    description: "Pre-travel risk assessment covering Lilongwe's crime environment, road safety considerations, and regional security context."
regulations:
  firearms: "The Malawi Police Service administers private security regulation. Armed private security in Malawi requires licensing from the Police Service. The regulatory framework is less developed than in South Africa or Kenya but armed security is available through licensed operators."
  licensing: "Private security companies in Malawi must hold a licence from the Malawi Police Service. The market is smaller than in southern African capitals; operator vetting is important."
  foreign_operators: "Foreign security personnel may operate in advisory and supervisory roles. Armed functions require engagement of licensed Malawian operators."
zones:
  safe:
    - "Area 43 (Capital Hill): Government ministries, embassies, and major NGO offices. Lilongwe's administrative core with the best security presence."
    - "Area 3 (City Centre): Major hotels including the Sunbird Capital and Crossroads Hotels. Commercial banks and the primary corporate hotel zone."
    - "Area 12 (Diplomatic Quarter): Embassy and high commission area. Some of Lilongwe's best-maintained residential infrastructure."
    - "Lilongwe Wildlife Centre and Lodge Zone: The wildlife centre area in Lilongwe's central zone is a controlled and safe environment."
  elevated:
    - "Old Town: Lilongwe's original commercial centre with dense market activity and higher petty crime risk."
    - "Lilongwe Bus Depot Area: High pedestrian density and documented petty theft."
    - "Peripheral residential areas at night: Lower-income residential zones carry higher crime risk after dark."
emergency_contacts:
  - service: "Malawi Police Emergency"
    number: "997"
  - service: "Lilongwe Central Hospital"
    number: "+265 1 753 555"
  - service: "Mwaiwathu Private Hospital"
    number: "+265 1 756 888"
  - service: "British High Commission Lilongwe"
    number: "+265 1 772 400"
  - service: "US Embassy Lilongwe"
    number: "+265 1 773 166"
warnings:
  - "Malawi's rainy season (November to April) significantly affects road conditions outside Lilongwe. Unpaved roads in rural areas become impassable. Any travel outside Lilongwe during the rainy season requires local knowledge and appropriate vehicles."
  - "Medical facilities in Lilongwe are limited. Mwaiwathu Private Hospital provides the best available private care. For serious conditions, medical evacuation to Nairobi, Johannesburg, or South Africa is the appropriate response."
  - "Malawi has experienced recurring fuel shortages that can affect vehicle availability and add unpredictability to transfer timing. Confirm fuel availability with the security driver before any transfer."
  - "Lake Malawi is a significant business and leisure destination but carries bilharzia (schistosomiasis) risk. Swimming in the lake without specific local advice on safe zones is not recommended."
related_cities:
  - name: "Lusaka"
    slug: "lusaka"
  - name: "Nairobi"
    slug: "nairobi"
  - name: "Harare"
    slug: "harare"
faqs:
  - question: "What sectors bring business visitors to Lilongwe?"
    answer: "Malawi's primary economic sectors are tobacco (historically the main export earner), tea, sugar, and increasingly mining (uranium at Kayelekera, rare earths at Kanyika). Development finance, NGO, and international aid organisations maintain a significant presence given Malawi's status as one of sub-Saharan Africa's lower-income economies. Business visitors are predominantly from these sectors: commodities trading, development finance, agricultural investment, and humanitarian organisations."
  - question: "Is Lilongwe safe for business travel?"
    answer: "Lilongwe is a moderate-risk business destination by southern African standards. It does not carry the violent crime profile of Harare, Lusaka, or Johannesburg. The risks for business visitors are primarily opportunistic crime (petty theft, bag snatching), vehicle crime, and road safety outside the capital. Standard precautions -- vetted transport, avoiding isolated areas at night, keeping valuables out of sight -- are appropriate. FCDO advises normal precautions for Malawi."
  - question: "How far is Kamuzu International Airport from Lilongwe city centre?"
    answer: "Lilongwe Kamuzu International Airport (LLW) is approximately 23 kilometres north of the city centre (Area 3 hotel zone) and Area 43 Capital Hill. Transfer time is typically 25 to 40 minutes via the main Kamuzu Procession Road. The road is well-maintained by regional standards. Pre-arranged collection from the airport is the appropriate approach for all business visitors."
  - question: "Do I need close protection in Lilongwe?"
    answer: "A vetted security driver is the appropriate baseline for most business visitors to Lilongwe. A dedicated close protection officer is warranted for principals with specific targeting risk -- executives in mining, senior government advisers, or those with a specific threat profile identified in a pre-travel assessment. The general crime environment does not automatically require an armed close protection officer for all visitors, unlike higher-risk regional capitals."
---

Lilongwe is the capital of Malawi, one of sub-Saharan Africa's smaller and less wealthy economies, positioned between Tanzania, Zambia, and Mozambique. It serves as the administrative and commercial centre for Malawi's tobacco, tea, and agricultural sectors, and is the base for a substantial development finance and NGO community given Malawi's dependence on international aid and investment. The security environment is moderate by southern African standards, making Lilongwe a manageable destination for business visitors who apply appropriate precautions.

## The Lilongwe security environment

Malawi does not carry the gang crime profile of Johannesburg or Nairobi, but opportunistic crime, vehicle crime, and road safety risks are real and require a vetted transport model. The Malawi Police Service administers private security licensing; the regulatory framework is functional but less developed than in the Southern African Development Community's larger economies.

## Security considerations for Lilongwe

Vetted transport for all in-city and inter-city movement is the baseline requirement. Airport transfers, out-of-town business visits, and movement during and after dark should all use pre-arranged, vetted security drivers.

For security services in Lilongwe, see our [executive protection services](/services/executive-protection/) and [secure airport transfers](/services/secure-airport-transfers/).
"""

# MANDALAY
pages["mandalay.md"] = """---
title: "Mandalay"
description: "Security assessment and close protection in Mandalay, Myanmar. Executive security for the Myanmar conflict environment and FCDO against-all-but-essential-travel advisory."
slug: "mandalay"
h1: "Security Services in Mandalay, Myanmar"
country: "Myanmar"
risk_level: "critical"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Mandalay | Security Myanmar"
date: "2026-06-20"
threats:
  - type: "Armed Conflict: Civil War"
    detail: "Myanmar has been in a state of civil conflict since the February 2021 military coup. The Myanmar military (Tatmadaw) and resistance forces including the People's Defence Force (PDF) and ethnic armed organisations are engaged in active fighting across much of the country. Mandalay city experienced protests and violent crackdowns in 2021 and periodic security incidents since. The conflict risk in Mandalay city is lower than in many rural areas but is not negligible. Source: FCDO Myanmar travel advice; ACLED Myanmar conflict data."
  - type: "Arbitrary Detention and Legal Risk"
    detail: "Since the 2021 coup, foreigners have been detained in Myanmar on charges including associating with opposition figures, photographing military installations, and engaging with civil society organisations. The legal environment is unpredictable. Diplomatic protection for detained foreign nationals is limited. FCDO advises against all but essential travel to Myanmar specifically because of this risk."
  - type: "Infrastructure and Service Disruption"
    detail: "Power outages, internet shutdowns, and banking system disruptions are recurring features of Myanmar's post-coup environment. Foreign bank cards may not function. Internet access is subject to scheduled and unannounced outages. Fuel availability is variable. Any operation in Myanmar requires pre-positioned cash and communications contingency planning."
  - type: "Terrorist and Bomb Incidents"
    detail: "Bomb and IED incidents in Mandalay and other Myanmar cities have been reported since 2021, primarily targeting military and government infrastructure. The risk to foreign visitors is lower than the primary targeting profile but cannot be excluded. Avoid congregating near military checkpoints or government buildings."
available_services:
  - name: "Security Assessment"
    description: "Pre-travel and in-country security assessment for organisations that must operate in Myanmar despite the FCDO advisory. Assessment covers legal risk, movement protocols, and contingency planning."
  - name: "Security Drivers"
    description: "Vetted drivers for in-city movement in Mandalay and road transfers within Mandalay Region. Assessment of route security on a case-by-case basis given the conflict environment."
  - name: "Risk Assessment"
    description: "Ongoing security monitoring and threat assessment for organisations maintaining operations in Mandalay despite the advisory. Includes conflict mapping and legal risk tracking."
  - name: "Executive Protection"
    description: "Close protection for senior executives or aid workers in Mandalay for organisations that have assessed travel as essential. Full advance work and contingency planning."
regulations:
  firearms: "Myanmar's private security regulatory framework has been disrupted by the 2021 coup. The Myanmar Police Force under military control now administers security company licensing. Armed private security arrangements in Myanmar post-2021 require careful legal assessment."
  licensing: "Private security companies in Myanmar require licensing from the Myanmar Police Force. The regulatory environment is unpredictable in the post-coup period."
  foreign_operators: "Foreign security personnel face significant legal and personal risk operating in Myanmar in the current conflict environment. Any foreign security engagement in Myanmar requires extensive pre-deployment legal assessment."
zones:
  safe:
    - "Central Mandalay: The city centre including the Mandalay Palace moat area and the main commercial districts carries lower immediate conflict risk than rural Mandalay Region, but is not a safe zone by standard definitions."
    - "International Hotels: Mandalay's major international-brand hotels provide relatively controlled environments for short-stay visits."
  elevated:
    - "Military Checkpoints and Installations: Avoid congregating near any military presence. Risk of arbitrary detention and conflict-related incidents."
    - "Rural Mandalay Region: Active conflict operations in parts of Mandalay Region. Do not travel outside the city without current security assessment."
    - "Chin State, Sagaing Region (borders with Mandalay): Active fighting areas. FCDO advises against all travel."
emergency_contacts:
  - service: "Myanmar Emergency (limited reliability)"
    number: "999"
  - service: "Mandalay General Hospital"
    number: "+95 2 36110"
  - service: "British Embassy Yangon (nearest to Mandalay)"
    number: "+95 1 370 863"
  - service: "US Embassy Yangon"
    number: "+95 1 536 509"
warnings:
  - "FCDO advises against all but essential travel to the whole of Myanmar. This advisory is the result of the February 2021 coup, civil war, and the legal risk of arbitrary detention. Do not travel to Mandalay or any part of Myanmar without a specific essential-travel assessment."
  - "Internet and phone connectivity in Myanmar is subject to scheduled and unannounced shutdowns. Any operation in Myanmar requires offline contingency planning and pre-positioned communications."
  - "Foreign bank cards may not function at Myanmar ATMs due to banking sanctions and infrastructure disruption. Pre-position adequate cash (USD or EUR preferred) before entering Myanmar."
  - "Medical evacuation from Mandalay is significantly more complex than from most Asian cities. Bangkok is the nearest reliable medical evacuation destination (approximately 2 hours by air). Medical insurance with evacuation cover including conflict environments is a baseline requirement."
related_cities:
  - name: "Bangkok"
    slug: "bangkok"
  - name: "Yangon"
    slug: "yangon"
  - name: "Chiang Mai"
    slug: "chiang-mai"
faqs:
  - question: "Should I travel to Mandalay at all?"
    answer: "FCDO advises against all but essential travel to the whole of Myanmar, including Mandalay. This advisory reflects the civil conflict, legal risk of arbitrary detention, and infrastructure disruption. The correct first question for any Mandalay trip is whether the travel is genuinely essential and cannot be achieved by remote means. If the answer is yes, a full security assessment covering the specific legal, conflict, and logistics risks is required before departure."
  - question: "What is the security situation in Mandalay city specifically?"
    answer: "Mandalay city carries lower immediate conflict risk than rural Mandalay Region and neighbouring Sagaing Region, where active fighting is ongoing. The city experienced mass protests, crackdowns, and street-level violence in 2021. Since then, the situation has been unstable with periodic bomb incidents, military checkpoints, and arbitrary detention incidents. The city functions commercially but under significant constraint and with unpredictable security conditions."
  - question: "What happened to Myanmar's private security industry after the 2021 coup?"
    answer: "Myanmar's private security sector has been significantly disrupted by the 2021 coup and subsequent conflict. The Myanmar Police Force under military control administers security company licensing. Several international security companies withdrew from Myanmar after the coup. Engaging any security operator in Myanmar post-2021 requires careful vetting and legal assessment, as some operators are directly affiliated with the military government."
  - question: "What communications contingency planning is required for Mandalay?"
    answer: "Internet access in Myanmar is subject to scheduled and unannounced shutdowns. Social media platforms including Facebook have been blocked since the 2021 coup. Satellite communication devices are advisable for any essential travel to Myanmar where communication continuity is required. Pre-agreed check-in schedules with a base outside Myanmar, offline mapping, and pre-positioned emergency contact details are the minimum contingency communications requirements."
---

Mandalay is Myanmar's second city and the commercial hub of upper Myanmar, positioned at the junction of road, rail, and river routes linking Yangon with China's Yunnan Province. It has historically been a significant trading city and a base for jade, gems, and teak industries. Since the February 2021 military coup, Myanmar has been in a state of civil conflict that has profoundly changed the operating environment for all foreign business visitors.

## The Myanmar conflict context

FCDO advises against all but essential travel to the whole of Myanmar. The advisory reflects the ongoing civil war between the Myanmar military and resistance forces, the risk of arbitrary detention of foreign nationals, and severe infrastructure disruption. Travel to Mandalay or any part of Myanmar in this environment requires an essential-travel justification and a full pre-deployment security assessment.

## Operating in Mandalay under current conditions

Any engagement in Mandalay under current conditions must be treated as a conflict-environment operation, not standard business travel. Legal risk assessment, communications contingency planning, medical evacuation planning, and continuous security monitoring are all baseline requirements.

For security assessment services for Myanmar operations, see our [executive protection services](/services/executive-protection/) and [risk assessments](/services/risk-assessments/).
"""

# WUHAN
pages["wuhan.md"] = """---
title: "Wuhan"
description: "Close protection and executive security in Wuhan, China. PSB-compliant security drivers and executive protection for Hubei Province's industrial and automotive hub."
slug: "wuhan"
h1: "Close Protection in Wuhan, China"
country: "China"
risk_level: "low-moderate"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Wuhan | Security Drivers Hubei China"
date: "2026-06-20"
threats:
  - type: "Business Intelligence and Counter-Intelligence"
    detail: "Wuhan is a significant industrial and automotive manufacturing centre with major foreign direct investment in the automotive sector (Dongfeng-Honda, Dongfeng-Nissan, SAIC-GM). Principals from automotive, advanced manufacturing, and technology sectors should treat Wuhan as a business intelligence-sensitive environment. Counter-intelligence awareness and digital device discipline are appropriate precautions."
  - type: "Legal and Regulatory Risk"
    detail: "China's National Security Law, Data Security Law, and Personal Information Protection Law create legal exposure for foreign executives conducting due diligence, competitive intelligence gathering, or meetings with individuals who may have opposition associations. China's exit ban mechanism allows the Ministry of Public Security to prevent departure during investigations. Source: UK FCDO China travel advice."
  - type: "Digital Surveillance Environment"
    detail: "Wuhan, like all major Chinese cities, operates an extensive digital surveillance infrastructure. CCTV coverage in public areas is near-universal. Digital communications on Chinese networks are subject to monitoring. Principals should brief on digital hygiene practices before any Wuhan visit."
available_services:
  - name: "Security Drivers"
    description: "PSB-compliant vetted drivers for Tianhe Airport transfers and in-city business movement in Wuhan."
  - name: "Executive Protection"
    description: "Close protection arrangements for senior executives visiting Wuhan's automotive and industrial sector partners. Operates within the MPS Order No. 564 legal framework."
  - name: "Risk Assessment"
    description: "Pre-travel risk assessment covering Wuhan's business intelligence environment, legal risk under Chinese data and security laws, and digital hygiene briefing."
regulations:
  firearms: "China's Ministry of Public Security Order No. 564 (2010) governs commercial security services. Private security companies must hold PSB registration. Firearms are not available to foreign security personnel under Chinese law."
  licensing: "All commercial security operators in China must hold PSB registration. Security services are provided by licensed Chinese operators. Foreign security personnel cannot hold commercial security licences in China."
  foreign_operators: "Foreign security personnel cannot drive or carry arms in China. Foreign advisers may accompany principals in a supervisory capacity. All formal security functions must be performed by PSB-registered local personnel."
zones:
  safe:
    - "Wuhan Economic and Technological Development Zone (WEDZ): Automotive manufacturing district hosting Dongfeng Motor Group and joint ventures. Primary corporate operating zone for automotive sector visitors."
    - "Jiefang Avenue and Jianghan District CBD: Central business district with major hotels and commercial banks."
    - "Optical Valley (East Lake High-Tech Development Zone): Technology and optoelectronics cluster. Secondary corporate operating zone."
    - "Wuhan International Expo Centre Area: Convention and event zone north of East Lake."
  elevated:
    - "Wuchang old city peripheral areas at night: General crime risk is low but standard urban precautions apply."
    - "Hankou Old Concession Area: Historic district with pedestrian density and some petty crime risk."
emergency_contacts:
  - service: "Emergency (Police/Fire/Ambulance)"
    number: "110 / 119 / 120"
  - service: "Wuhan Union Hospital"
    number: "+86 27 8572 6114"
  - service: "Wuhan Tongji Hospital (International)"
    number: "+86 27 8366 3163"
  - service: "British Consulate-General Chongqing (nearest to Wuhan)"
    number: "+86 23 6369 1000"
  - service: "US Consulate General Wuhan (closed 2020 -- US Embassy Beijing)"
    number: "+86 10 8531 3000"
warnings:
  - "The US Consulate General in Wuhan was closed by the Chinese government in 2020. US citizens in Wuhan should register with the US Embassy in Beijing and are covered by the Chengdu Consulate General for consular emergencies. British nationals should contact the Chongqing Consulate-General."
  - "China's exit ban mechanism allows the Ministry of Public Security to prevent departure during investigations without notice. Foreign executives involved in commercial disputes, regulatory investigations, or any litigation with Chinese state-connected entities should assess this risk before travel."
  - "Digital devices taken into China should be treated as potentially exposed to access. VPN use is subject to Chinese law and available VPN services change. Brief on digital hygiene before travel."
  - "Wuhan's summers are extremely hot and humid; outdoor events and walking significant distances in summer months require heat management planning."
related_cities:
  - name: "Beijing"
    slug: "beijing"
  - name: "Shanghai"
    slug: "shanghai"
  - name: "Chengdu"
    slug: "chengdu"
faqs:
  - question: "What sectors bring business visitors to Wuhan?"
    answer: "Wuhan is China's primary automotive manufacturing hub: Dongfeng Motor Group's headquarters is here, and major joint ventures including Dongfeng-Honda, Dongfeng-Nissan, and SAIC-GM operate in the Wuhan Economic and Technological Development Zone. The city is also a significant centre for optoelectronics and optical communications through the Optical Valley development zone. Steel production (Wuhan Iron and Steel), chemicals, and heavy engineering are also significant sectors."
  - question: "Is Wuhan a high-risk destination for business travel?"
    answer: "Wuhan is a low to moderate risk destination by urban security standards. Street crime risk for business visitors is low, and the city has extensive infrastructure and international hotel capacity. The risks that require planning are business intelligence exposure, legal risk under Chinese data and national security laws, and the digital surveillance environment -- none of which are unique to Wuhan but are heightened in China's industrial centres. FCDO rates China as requiring normal precautions with specific awareness of the legal and counter-intelligence environment."
  - question: "How far is Wuhan Tianhe Airport from the city centre?"
    answer: "Wuhan Tianhe International Airport (WUH) is approximately 30 kilometres north of Wuhan's central business district via the airport expressway. Transfer time is typically 30 to 50 minutes under normal conditions. Peak-hour congestion on the expressway and the inner ring road can extend this to 60 to 75 minutes."
  - question: "What digital security precautions apply in Wuhan?"
    answer: "Wuhan operates within China's national digital surveillance infrastructure. All communications on Chinese mobile networks are subject to monitoring. Devices connected to Chinese Wi-Fi networks may be exposed. Principals carrying commercially sensitive materials should use dedicated travel devices with minimal data, use VPN services compliant with Chinese law, and brief staff on digital hygiene protocols before departure. These precautions apply throughout China and are not specific to Wuhan."
---

Wuhan is the capital of Hubei Province and one of China's largest industrial cities by output, serving as the national centre for automotive manufacturing, optoelectronics, and heavy engineering. With a population exceeding 12 million, it is among China's ten largest cities and hosts significant foreign direct investment from major automotive groups. The security environment is assessed as low to moderate for business visitors, with the primary risks being business intelligence exposure and the legal framework specific to operating in China rather than street crime.

## The Wuhan operating environment

Wuhan's risks for international business visitors are China-specific rather than city-specific: PSB oversight, the digital surveillance environment, exit ban risk for executives in commercial disputes, and the counter-intelligence considerations applicable across China's industrial centres. Ministry of Public Security Order No. 564 (2010) governs commercial security operations.

## Security in Wuhan

PSB-compliant vetted drivers and operations controller oversight are the appropriate baseline for executive movement in Wuhan. Business intelligence briefing before any visit to the automotive or advanced manufacturing zones is a standard precaution.

For executive security in Wuhan, see our [close protection officers](/services/executive-protection/) and [secure airport transfers](/services/secure-airport-transfers/).
"""

# RECIFE
pages["recife.md"] = """---
title: "Recife"
description: "Close protection and executive security in Recife, Brazil. SESP-PE licensed drivers, armed bodyguard hire, and kidnap-counter protocols for Pernambuco's capital."
slug: "recife"
h1: "Close Protection in Recife, Brazil"
country: "Brazil"
risk_level: "high"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Recife | Bodyguard Hire Pernambuco Brazil"
date: "2026-06-20"
threats:
  - type: "Armed Robbery and Express Kidnapping"
    detail: "Recife and the metropolitan area of greater Recife (Regiao Metropolitana do Recife) record consistently high violent crime rates in the SDS-PE (Secretaria de Defesa Social de Pernambuco) annual crime statistics. Armed robbery targeting business visitors occurs in commercial areas, hotel approaches, and on the Guararapes Airport approach road. Express kidnapping -- short-duration abductions for immediate ATM withdrawals -- is a specific risk for foreign business visitors."
  - type: "Vehicle Crime and Carjacking"
    detail: "Carjacking is documented in Recife, particularly at traffic lights and in the peripheral zones of the metropolitan area. The EN-route from REC Guararapes International Airport through the Santo Amaro and Imbiribeira areas carries elevated vehicle crime risk. Vetted transport from REC is essential."
  - type: "Gang Territory and No-Go Zones"
    detail: "Recife's metropolitan periphery includes areas controlled by criminal factions where police authority is contested. Mangueira, Alto de Santa Terezinha, and several peripheral bairros are not accessible for foreign business visitors. Crime risk in these areas is extreme and they are entirely off standard corporate itineraries."
  - type: "Port Activity and Industrial Crime"
    detail: "Recife and its industrial satellite Suape Port are significant in Brazil's sugar, agribusiness, and petrochemical sectors. Industrial and port operations have specific security profiles including cargo theft and organised criminal infiltration of supply chains."
available_services:
  - name: "Security Drivers"
    description: "SESP-PE licensed vetted drivers for REC Guararapes airport transfers and in-city movement in Recife and the metropolitan area."
  - name: "Bodyguard Hire"
    description: "Armed close protection officers for senior executives in Recife's agribusiness, port, and financial sectors."
  - name: "Executive Protection"
    description: "Full protective arrangements for executives and HNWI in Recife. Includes advance work, residential security assessment, and secure transport."
  - name: "Risk Assessment"
    description: "Pre-travel risk assessment covering Recife's violent crime profile, express kidnapping risk, and safe operating zones."
regulations:
  firearms: "Private security in Pernambuco is regulated by the Secretaria de Defesa Social (SDS-PE) at state level and Policia Federal Portaria 387/2006 at federal level. Armed security requires a SINARM firearms registration and Policia Federal authorisation. Armed private security guards must hold DPF-issued firearms licences."
  licensing: "Security companies in Brazil must register with the Policia Federal and comply with state-level SDS-PE registration in Pernambuco. Both federal and state credentials should be verified for any Recife security engagement."
  foreign_operators: "Foreign security personnel cannot legally carry firearms in Brazil. All armed security must be provided by licensed Brazilian operators. Foreign advisers may accompany transfers in a supervisory capacity."
zones:
  safe:
    - "Boa Viagem: Recife's primary beachfront hotel and business district. The main zone for international hotel infrastructure and corporate offices. Still requires vetted transport; crime occurs in Boa Viagem including at night."
    - "Recife Antigo: Historic centre redevelopment area with some corporate office space. Significantly better managed than the broader metropolitan area."
    - "Pina and Piedade: Adjacent to Boa Viagem, secondary hotel and business zone."
    - "Suape Industrial Port Zone: The major industrial port 40km south of Recife. Controlled access infrastructure but requires security planning for transfers from the city."
  elevated:
    - "Casa Amarela, Afogados, and peripheral bairros: High crime residential zones. Not on corporate itineraries."
    - "Greater Metropolitan Periphery (Camaragibe, Jaboatao dos Guararapes peripheral areas): Elevated gang crime and carjacking risk."
    - "Central Recife (Derby, Madalena, Gracias): Higher crime density than Boa Viagem; use vetted transport for any movement."
emergency_contacts:
  - service: "Emergency Police (SAMU/Fire)"
    number: "190 / 192 / 193"
  - service: "Hospital Esperanca (private)"
    number: "+55 81 3216 1300"
  - service: "Real Hospital Portugues (private)"
    number: "+55 81 3416 1000"
  - service: "British Consulate Recife"
    number: "+55 81 3326 5050"
  - service: "US Consulate Recife"
    number: "+55 81 3416 3050"
warnings:
  - "Recife's metropolitan area has one of Brazil's highest per-capita homicide rates. Business visitors in Boa Viagem are not in the primary violence zones but the surrounding metropolitan area is genuinely dangerous. Vetted transport and zone discipline are essential, not optional."
  - "The carnival period (February/March) brings very large crowds to Recife's Frevo and Olinda Carnival, significantly increasing the visitor population and creating security planning challenges in terms of crowd density and transport disruption."
  - "Both the British Consulate and US Consulate operate in Recife, which reflects the city's importance as a regional business centre. Consulate contact details should be registered before arrival."
  - "Suape Industrial Port is approximately 40 kilometres south of Recife. The transfer corridor to Suape passes through areas with elevated crime risk. Transfers to Suape require vetted transport and should not be undertaken in unvetted taxis."
related_cities:
  - name: "Fortaleza"
    slug: "fortaleza"
  - name: "Sao Paulo"
    slug: "sao-paulo"
  - name: "Salvador"
    slug: "salvador"
faqs:
  - question: "Is Recife safe for business travel?"
    answer: "Recife requires a higher level of security planning than most Brazilian business destinations outside Rio de Janeiro. The city's violent crime rate is among the highest in Brazil, though the risk for business visitors operating in Boa Viagem and using vetted transport is significantly lower than the metropolitan average. FCDO issues a high crime advisory for Recife and advises avoiding certain areas entirely. A vetted driver, zone discipline, and a pre-travel security assessment are baseline requirements."
  - question: "What industries bring business visitors to Recife?"
    answer: "Recife is the commercial capital of Brazil's north-east region and hosts businesses in agribusiness (sugar, fruit and fibre export), petrochemicals, textiles, and tourism. Suape Port, 40 kilometres south, is one of Brazil's most modern deep-water ports and handles significant container and petroleum volumes. The Porto Digital innovation district has developed a technology sector. Development finance institutions and government-sector investors are significant presences."
  - question: "What is the express kidnapping risk in Recife?"
    answer: "Express kidnapping -- short-duration abductions for immediate ATM withdrawals, typically lasting 2 to 8 hours -- is a documented risk in Recife for business visitors arriving at uncontrolled contact points such as the airport kerb, unvetted taxi queues, and isolated ATM locations. Pre-arranged inside-terminal collection at REC Guararapes with a SESP-PE-licensed driver is the primary mitigation for the airport arrival window."
  - question: "How far is REC Guararapes from Boa Viagem?"
    answer: "Recife Guararapes International Airport (REC) is approximately 12 kilometres from the main Boa Viagem hotel zone. Transfer time via the Santos Dumont Avenue and the Avenida Domingos Ferreira is typically 20 to 35 minutes under normal conditions. Peak-hour congestion can extend this to 45 to 60 minutes. The airport approach road through Santo Amaro carries elevated crime risk, making vetted transport essential from the moment of arrival."
---

Recife is the capital of Pernambuco, the commercial hub of Brazil's north-east, and the operational base for businesses working in the region's agribusiness, port, and manufacturing sectors. Suape Port, 40 kilometres south, is one of Brazil's most significant deep-water industrial ports. The city's security environment is characterised by high violent crime rates in the metropolitan periphery and specific risks -- express kidnapping, carjacking, and armed robbery -- that directly affect foreign business visitors.

## The Recife security environment

SDS-PE crime statistics consistently place the greater Recife metropolitan area among Brazil's highest-crime urban regions. Boa Viagem is the principal operating zone for business visitors, but crime also occurs there. The vetted transport model and zone discipline are the foundations of safe business operations in Recife.

## Security framework

Policia Federal Portaria 387/2006 and SDS-PE registration govern private security in Pernambuco. Both federal and state credentials should be verified for any security engagement in Recife.

For security services in Recife, see our [bodyguard hire services](/services/bodyguard-hire/) and [secure airport transfers](/services/secure-airport-transfers/).
"""

# FORTALEZA
pages["fortaleza.md"] = """---
title: "Fortaleza"
description: "Close protection and executive security in Fortaleza, Brazil. SSPDS-CE licensed operators and armed bodyguard hire for Ceara's coastal capital."
slug: "fortaleza"
h1: "Close Protection in Fortaleza, Brazil"
country: "Brazil"
risk_level: "high"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Fortaleza | Bodyguard Hire Ceara Brazil"
date: "2026-06-20"
threats:
  - type: "High Homicide Rate"
    detail: "Fortaleza has recorded some of Brazil's highest homicide rates in recent years. The Ceara Public Security Secretariat (SSPDS-CE) statistics show elevated homicide rates across the metropolitan area, driven primarily by territorial disputes between organised criminal factions. The violence is concentrated in peripheral neighbourhoods but affects the overall security environment including transfer routes."
  - type: "Armed Robbery and Street Crime"
    detail: "Armed robbery targeting business visitors and tourists occurs in Fortaleza, including in the Aldeota and Meireles hotel zones. Beach robberies along the Praia de Iracema and Praia do Futuro are a specific documented risk. ATM crime -- robbery during cash withdrawals -- is among the most consistently reported patterns affecting foreign visitors."
  - type: "Gang-Related Criminal Activity"
    detail: "Organised criminal factions control substantial areas of Fortaleza's metropolitan periphery. The GDE (Guardioes do Estado) and CV (Comando Vermelho) presence in Ceara has generated periodic waves of extreme violence including attacks on infrastructure that produced a public security crisis in 2019. The situation has stabilised since but the underlying criminal structures remain."
  - type: "Express Kidnapping"
    detail: "Express kidnapping is documented in Fortaleza, particularly targeting business visitors at uncontrolled contact points including airport arrivals, unvetted taxis, and isolated ATM locations. Pre-arranged inside-terminal collection and avoidance of unvetted transport are the primary mitigations."
available_services:
  - name: "Security Drivers"
    description: "SSPDS-CE licensed vetted drivers for Pinto Martins Airport transfers and in-city movement in Fortaleza."
  - name: "Bodyguard Hire"
    description: "Armed close protection officers for executives in Fortaleza's agribusiness, port, and industrial sectors."
  - name: "Executive Protection"
    description: "Full protective arrangements for senior executives and HNWI visiting or resident in Fortaleza."
  - name: "Risk Assessment"
    description: "Pre-travel assessment covering Fortaleza's gang-crime environment, express kidnapping risk, and safe operating zones."
regulations:
  firearms: "Private security in Ceara is regulated by the SSPDS-CE at state level and Policia Federal Portaria 387/2006 at federal level. Armed security operators must hold SINARM registration and Policia Federal authorisation."
  licensing: "Security companies must hold Policia Federal registration and SSPDS-CE state-level credentials. Verify both sets of credentials before any Fortaleza security engagement."
  foreign_operators: "Foreign security personnel cannot legally carry firearms in Brazil. All armed security must be provided by licensed Brazilian operators."
zones:
  safe:
    - "Meireles: Primary beachfront hotel and business zone. International hotel brands, corporate offices, and restaurants. Still requires vetted transport; crime occurs in Meireles."
    - "Aldeota: Inland business and residential district adjacent to Meireles. Secondary corporate zone with office buildings and commercial banks."
    - "Cocó and Fatima: Further inland residential and commercial zones with somewhat lower crime density than the beachfront."
    - "Fortaleza Port Zone: Pecem Industrial Port (70km west) handles significant iron ore and general cargo volumes. Requires specific security planning for transfers from the city."
  elevated:
    - "Praia de Iracema at night: Concentrated bar and nightlife zone with documented robbery risk after dark."
    - "Barra do Ceara, Siqueira, Mondubim: Western and south-western peripheral zones with very high crime rates. Not on corporate itineraries."
    - "Centro (Central Fortaleza) at night: The commercial centre after dark carries elevated crime risk. Daytime commercial movement with vetted transport is manageable."
emergency_contacts:
  - service: "Emergency (Police/SAMU/Fire)"
    number: "190 / 192 / 193"
  - service: "Hospital Sao Carlos (private)"
    number: "+55 85 4005 3700"
  - service: "Hospital do Coraao (private)"
    number: "+55 85 3265 8000"
  - service: "British Consulate Fortaleza (Honorary)"
    number: "+55 85 3219 7020"
warnings:
  - "Fortaleza's homicide rate is among the highest for any city in the Americas. The violence is concentrated in specific zones, but its scale creates an elevated ambient risk that requires security planning well above the standard Latin American business travel baseline."
  - "Beach robberies are common along Praia de Iracema and Praia do Futuro, including during daytime hours. Do not walk on the beach with valuables, smartphones, or bags. Praia do Futuro in particular is a documented robbery location."
  - "ATM crime -- robbery during cash withdrawals -- is specifically documented in Fortaleza. Use ATMs inside hotels or shopping centres during business hours only."
  - "The 2019 public security crisis in Ceara, which involved attacks on buses, banks, and infrastructure triggered by criminal factions, demonstrated that the organised crime environment in Fortaleza can produce city-wide disruption. Monitor local security news during any visit."
related_cities:
  - name: "Recife"
    slug: "recife"
  - name: "Sao Paulo"
    slug: "sao-paulo"
  - name: "Natal"
    slug: "natal"
faqs:
  - question: "Is Fortaleza safe for business travel?"
    answer: "Fortaleza requires a higher level of security planning than most Brazilian business destinations. Its homicide rate has been among the highest of any Brazilian state capital in recent years. Business visitors operating in the Meireles and Aldeota zones with vetted transport have a materially lower risk profile than the metropolitan average, but the overall threat environment means that basic precautions are insufficient. A vetted driver, zone discipline, avoidance of isolated locations, and a pre-travel security assessment are all appropriate baselines."
  - question: "What industries bring business visitors to Fortaleza?"
    answer: "Fortaleza is the commercial capital of Ceara and the north-east Brazilian coast. Key sectors include cashew and other agricultural commodity processing, textiles and apparel manufacturing, aquaculture (shrimp production and export), tourism, and port logistics through Pecem Industrial Port, which handles iron ore and general cargo for the north-east region. Development finance and infrastructure investment are also significant."
  - question: "How far is Pinto Martins Airport from Meireles?"
    answer: "Fortaleza Pinto Martins International Airport (FOR) is approximately 6 kilometres from the Meireles hotel and business district. Transfer time is typically 15 to 25 minutes via the Avenida Senador Carlos Jereissati. The short distance does not reduce the risk at the airport arrival zone; pre-arranged inside-terminal collection with a licensed driver is the appropriate approach regardless of distance."
  - question: "What was the 2019 Ceara security crisis?"
    answer: "In February 2019, organised criminal factions in Ceara -- responding to changes in the state prison system -- coordinated attacks on public infrastructure including buses, banks, and police posts across Fortaleza and Ceara State. Over 200 attacks occurred in a week. The crisis demonstrated the capacity of Fortaleza's organised crime structures to produce city-wide disruption and was a significant event in Brazil's criminal gang history. It has not been repeated at the same scale but the underlying criminal infrastructure remains."
---

Fortaleza is the capital of Ceara State and the north-east's primary coastal commercial hub, handling significant volumes of agricultural commodity exports, textiles, and aquaculture through Pecem Industrial Port. The city's security environment is characterised by some of the highest crime rates in Brazil, driven by territorial competition between organised criminal factions and a peripheral residential zone with extreme crime density. Business visitors can operate effectively in Fortaleza but require more active security planning than in most Brazilian cities.

## The Fortaleza security environment

SSPDS-CE statistics and national Brazilian crime data consistently identify Fortaleza among the highest-homicide Brazilian state capitals. The Meireles and Aldeota hotel and business zones are comparatively better managed, but crime occurs across the entire city and vetted transport is a baseline requirement for all business movement.

## Security framework

Policia Federal Portaria 387/2006 and SSPDS-CE registration govern private security in Ceara. Both sets of credentials should be verified for any security engagement.

For security services in Fortaleza, see our [bodyguard hire services](/services/bodyguard-hire/) and [secure airport transfers](/services/secure-airport-transfers/).
"""

# CALI
pages["cali.md"] = """---
title: "Cali"
description: "Close protection and executive security in Cali, Colombia. SVSP-registered operators, armed bodyguard hire, and kidnap-counter protocols for Valle del Cauca."
slug: "cali"
h1: "Close Protection in Cali, Colombia"
country: "Colombia"
risk_level: "high"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Cali | Bodyguard Hire Valle del Cauca Colombia"
date: "2026-06-20"
threats:
  - type: "Kidnap and Extortion"
    detail: "Cali and Valle del Cauca Department have historically had elevated kidnap and extortion rates compared with Bogota and Medellin. Dissident FARC factions and organised crime groups operating in the Valle del Cauca corridor maintain kidnap capability targeting business sector principals. FCDO and US State Department both issue Level 3 advisories for Colombia that specifically reference kidnap risk."
  - type: "Armed Robbery and Carjacking"
    detail: "Armed robbery and carjacking are documented in Cali, including on the Alfonso Bonilla Aragon Airport approach road and in the peripheral residential zones. The El Aguacatal, Agua Blanca, and Siloé areas carry extreme crime profiles and are entirely off standard corporate itineraries. Vetted transport is essential for all business movement."
  - type: "Gang and Organised Crime Activity"
    detail: "Cali has a significant organised crime presence including groups historically connected to the Cali Cartel infrastructure and active dissident FARC networks in the surrounding Cauca Valley. The organised crime environment directly affects the transfer and event security picture for foreign business visitors with visibility in the sector."
  - type: "Civil Unrest"
    detail: "Cali experienced sustained and at times violent civil unrest during the 2021 paro nacional (national strike), including blockades, clashes between protesters and security forces, and significant disruption to the city. Monitor conditions around social and political mobilisations."
available_services:
  - name: "Security Drivers"
    description: "SVSP-registered vetted drivers for Alfonso Bonilla Aragon Airport transfers and in-city movement in Cali."
  - name: "Bodyguard Hire"
    description: "Armed close protection officers for executives in Cali's agribusiness, port, manufacturing, and financial sectors."
  - name: "Executive Protection"
    description: "Full protective arrangements for senior executives and HNWI. Includes kidnap counter-protocol briefing and residential security assessment."
  - name: "Risk Assessment"
    description: "Pre-travel risk assessment covering Cali's kidnap and extortion profile, organised crime environment, and safe operating zones."
regulations:
  firearms: "Private security in Colombia is regulated by the Superintendencia de Vigilancia y Seguridad Privada (SVSP) under Decreto 356/1994. Armed private security must be provided through SVSP-registered operators with valid firearms licences."
  licensing: "Security companies must hold current SVSP registration. Verification of SVSP licence status is a baseline check before any Colombian security engagement."
  foreign_operators: "Foreign security personnel may operate in advisory and supervisory roles. Armed security must be provided by SVSP-registered Colombian operators."
zones:
  safe:
    - "El Penal and Granada: Cali's primary upmarket hotel and restaurant zone. International hotel brands and corporate offices in the northern sector of the city."
    - "Ciudad Jardin and Ciudad Jardin Norte: Upmarket residential and commercial area. Lower crime density than the eastern zones."
    - "Chipichape and Unicentro Mall Areas: Major shopping and commercial centres with controlled access security."
    - "Alfonso Bonilla Aragon Airport Zone: Industrial and logistics corridor north of Cali."
  elevated:
    - "Agua Blanca: Eastern residential district with very high crime rates. Not on corporate itineraries."
    - "Aguacatal and Siloé: Peripheral hillside zones with extreme crime risk."
    - "Central Cali (Centro) at night: High pedestrian density and documented crime risk after dark."
    - "Cauca Valley Rural Areas: Areas outside Cali city carry specific armed group presence risk."
emergency_contacts:
  - service: "Emergency Police (SIJIN)"
    number: "112"
  - service: "SAMU (medical emergency)"
    number: "123"
  - service: "Clinica Valle del Lili (private)"
    number: "+57 2 331 7474"
  - service: "Imbanaco Clinica (private)"
    number: "+57 2 682 1000"
  - service: "British Embassy Bogota (serves Cali)"
    number: "+57 1 326 8300"
  - service: "US Consulate Cali (closed -- US Embassy Bogota)"
    number: "+57 1 275 2000"
warnings:
  - "FCDO advises against all travel to specific areas of Colombia including parts of Valle del Cauca Department outside Cali city. Review the FCDO Colombia travel advice before any out-of-city movement in Valle del Cauca."
  - "US State Department rates Colombia at Level 3: Reconsider Travel, with specific kidnap risk warnings. Colombia is one of the countries where kidnap risk insurance and counter-kidnap briefing are recommended for senior executives."
  - "Cali experienced serious and prolonged civil unrest during the 2021 paro nacional. Monitor conditions around any major social or political mobilisation. Demonstrations can block roads including airport access routes."
  - "Medical facilities in Cali include Clinica Valle del Lili, which is one of Colombia's better private hospitals. For serious conditions, medical evacuation to Bogota or Miami may be appropriate."
related_cities:
  - name: "Bogota"
    slug: "bogota"
  - name: "Medellin"
    slug: "medellin"
  - name: "Barranquilla"
    slug: "barranquilla"
faqs:
  - question: "Is Cali more dangerous than Bogota or Medellin?"
    answer: "Cali's homicide rate has generally been higher than Bogota's and comparable with or exceeding Medellin's in recent years, according to Colombian National Police statistics. The organised crime environment in the Cauca Valley, including dissident FARC and other armed groups operating in rural areas, adds a kidnap dimension that is less prominent in Bogota. Business visitors require a higher level of security planning in Cali than in Bogota, though both cities are manageable with appropriate arrangements."
  - question: "What industries bring business visitors to Cali?"
    answer: "Cali is the commercial capital of Valle del Cauca and Colombia's south-west. Key sectors include sugar and ethanol production (Colombia's primary sugar growing region), pharmaceuticals, food processing, and logistics. The Cali metropolitan area has a significant industrial base, and the city hosts the CENCAR logistics hub. Pacific Alliance trade and investment also generates business traffic through Cali's commercial networks."
  - question: "What is the kidnap risk for business visitors in Cali?"
    answer: "Kidnap risk in Cali is elevated compared with most Colombian cities. Dissident FARC and ELN networks in Valle del Cauca and the surrounding Cauca region retain kidnap capability. Express kidnapping -- short-duration, opportunistic abductions for immediate financial extraction -- is more common in the city itself. Pre-arranged inside-terminal collection at CLO Alfonso Bonilla Aragon and vetted SVSP-registered transport throughout are the primary city-level mitigations. For principals at elevated targeting risk, counter-kidnap briefing and a threat-specific security plan are appropriate."
  - question: "How far is CLO Alfonso Bonilla Aragon from El Penal?"
    answer: "Cali Alfonso Bonilla Aragon International Airport (CLO) is approximately 20 kilometres from the El Penal and Granada hotel zone. Transfer time via the dual-carriageway access road is typically 25 to 40 minutes under normal conditions. The approach road from CLO through the northern industrial zone carries moderate crime risk; pre-arranged inside-terminal collection with a SVSP-registered driver is the appropriate protocol."
---

Cali is Colombia's third-largest city and the commercial capital of Valle del Cauca Department, positioned in the Cauca Valley with significant agricultural, industrial, and logistics sectors. It serves as the business hub for Colombia's primary sugar-producing region and hosts significant pharmaceutical and food processing operations. The security environment is characterised by elevated kidnap risk from armed groups in the region, high urban crime rates, and an organised crime legacy from the historical Cali Cartel that continues to shape the current criminal landscape.

## The Cali security environment

SVSP Decreto 356/1994 governs private security in Colombia. Cali requires SVSP-registered operators, kidnap counter-protocol briefing for senior executives, and vetted transport throughout. FCDO and US State Department both issue high-risk advisories for Colombia that apply in Cali.

## Security planning for Cali

All Cali business travel requires a pre-travel security assessment, vetted transport for all movement, and an emergency contact and extraction plan before arrival.

For security services in Cali, see our [bodyguard hire services](/services/bodyguard-hire/) and [close protection officers](/services/executive-protection/).
"""

# MACAO
pages["macao.md"] = """---
title: "Macao"
description: "Close protection and executive security in Macao SAR, China. PSP-licensed operators, gaming sector security, and executive protection under Law 2/2002."
slug: "macao"
h1: "Close Protection in Macao SAR, China"
country: "Macao SAR"
risk_level: "low"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Macao | Security Services Macao SAR"
date: "2026-06-20"
threats:
  - type: "Gaming Sector Crime"
    detail: "Macao is the world's highest-revenue casino jurisdiction. High-stakes gaming environments attract a specific set of risks: fraud, junket-related crime, and, historically, triad organisation involvement in the gaming sector. These risks affect individuals operating in or adjacent to the VIP gaming segment rather than standard corporate visitors. Source: Macao Gaming Inspection and Coordination Bureau (DICJ) annual reports."
  - type: "Financial Crime and Money Laundering"
    detail: "Macao's gaming sector has historically been associated with money laundering risks, which have attracted international regulatory scrutiny and enforcement action, including from the US Treasury OFAC. Executives in the gaming, junket, and financial services sectors should be briefed on compliance risk before operating in Macao."
  - type: "General Crime: Low Risk"
    detail: "General street crime risk in Macao for business visitors is low. Petty theft occurs in dense tourist areas near the Cotai Strip and Lisbon Square, but at significantly lower rates than comparable Asian gaming and tourism destinations. FCDO advises normal precautions for Macao."
  - type: "Political and Legal Environment"
    detail: "Macao is a Special Administrative Region (SAR) of China under the one country, two systems framework. The National Security Law applied to Hong Kong in 2020 does not apply directly to Macao, but Macao has had its own national security law since 2009. Political activity is constrained. Business operations in Macao are subject to Chinese legal oversight alongside the SAR framework."
available_services:
  - name: "Security Drivers"
    description: "PSP-licensed vetted drivers for Macao International Airport and ferry terminal transfers, and in-city movement in Macao and Cotai."
  - name: "Bodyguard Hire"
    description: "Close protection for gaming sector executives, HNWI, and high-profile principals in Macao."
  - name: "Executive Protection"
    description: "Discreet close protection for senior executives and VIP principals in Macao's casino resort environment."
  - name: "Risk Assessment"
    description: "Pre-visit risk assessment for gaming sector and financial services executives, covering compliance, triad background, and VIP sector risks."
regulations:
  firearms: "Macao's private security industry is governed by Law 2/2002 (Private Security Activity Law). The Macao Public Security Police (PSP) licenses security companies and individual security personnel. Armed private security is tightly controlled; firearms authority is limited to specific categories of PSP-licensed operators."
  licensing: "Security companies in Macao must hold a licence under Law 2/2002 from the PSP. Individual security officers must hold PSP certification. The regulatory framework is well-developed."
  foreign_operators: "Foreign security personnel face similar constraints in Macao as in mainland China. Formal security functions must be performed by PSP-licensed local operators. Foreign close protection advisers may accompany principals in a supervisory capacity."
zones:
  safe:
    - "Cotai Strip: The major integrated resort corridor connecting Taipa and Coloane. Sands, Wynn, MGM, and Galaxy resorts. Highly controlled security environments within the resort campuses."
    - "Macao Peninsula (Central): The hotel and casino zone around Avenida de Almeida Ribeiro and Lisbon Square. Functioning business and tourism infrastructure."
    - "Taipa: Residential and university island. Lower tourist density than the peninsula. Macao International Airport is on Taipa."
    - "Hengqin (adjacent Zhuhai Mainland): The Hengqin co-operation zone between Macao and mainland China is increasingly significant for Macao business expansion."
  elevated:
    - "Dense tourist areas near Ruins of St Paul and Senado Square: Highest petty theft risk in Macao due to tourist concentration."
emergency_contacts:
  - service: "Macao Emergency (Police/Fire/Ambulance)"
    number: "999"
  - service: "Macao Public Security Police (PSP)"
    number: "+853 2857 3333"
  - service: "Kiang Wu Hospital"
    number: "+853 2837 1333"
  - service: "S. Januario General Hospital"
    number: "+853 2831 3731"
  - service: "British Consulate-General Hong Kong (serves Macao)"
    number: "+852 2901 3000"
warnings:
  - "Macao is one of the world's most compact jurisdictions (approximately 33 square kilometres). Journey times between any two points in Macao are short, but ferry and bridge links to Hong Kong and the Guangdong mainland are subject to weather disruption and, periodically, policy-related closure."
  - "The Hong Kong-Zhuhai-Macao Bridge provides a fixed link to the mainland for the first time. Border crossing at the bridge involves standard mainland China immigration procedures. Factor this into any cross-border transfer timing."
  - "Gaming debt enforcement, historically a specific risk associated with the junket sector, has significantly reduced since the 2021-2022 regulatory reforms to the Macao gaming industry. The risk has not disappeared entirely and is most relevant for principals with exposure to VIP gaming junket operations."
  - "Macao's summer typhoon season (May to October) can produce Category 8 or above Typhoon Signals, which shut down most outdoor activities, transport links, and business operations. Check Hong Kong Observatory typhoon forecasts before any Macao visit during the season."
related_cities:
  - name: "Hong Kong"
    slug: "hong-kong"
  - name: "Guangzhou"
    slug: "guangzhou"
  - name: "Shenzhen"
    slug: "shenzhen"
faqs:
  - question: "Is Macao safe for business travel?"
    answer: "Macao is one of Asia's lower-crime business destinations. General street crime is rare; FCDO advises normal precautions. The specific risks are gaming sector-related (fraud, compliance exposure, VIP junket-associated crime) and legal or political in nature (national security law framework, compliance with Chinese oversight). Standard corporate business travel to Macao is low-risk in physical security terms; the risks that require planning are sector-specific."
  - question: "What is the gaming sector security risk in Macao?"
    answer: "Macao is the world's highest-grossing casino jurisdiction by gaming revenue. The specific risks in the gaming sector include fraud targeting VIP players, triad-associated junket operations (though these have reduced significantly since 2021-2022 gaming reforms), and money laundering compliance risk for financial sector principals. These risks are most relevant for individuals operating in or close to the VIP gaming segment. Standard corporate visitors to Macao for non-gaming business purposes face a much lower risk profile."
  - question: "How do I get from Macao International Airport to the Cotai Strip?"
    answer: "Macao International Airport (MFM) is on Taipa Island. The Cotai Strip is on the reclaimed land between Taipa and Coloane, directly adjacent to the airport. Transfer time from MFM to the major Cotai resorts is typically 10 to 20 minutes. Casino resort shuttles are available from MFM; pre-arranged vetted transport is appropriate for principals requiring security."
  - question: "What law governs private security in Macao?"
    answer: "Macao's private security sector is governed by Law 2/2002 (Private Security Activity Law). Security companies and individual personnel must hold licences from the Macao Public Security Police (PSP). The regulatory framework is more developed than in mainland China but similarly restricts armed security and foreign operator roles. Any security engagement in Macao should verify PSP licence status for the operator."
---

Macao is a Special Administrative Region of China with a population of approximately 680,000 and the world's highest casino gaming revenue. Positioned across the Pearl River estuary from Hong Kong and adjacent to the Guangdong city of Zhuhai, Macao's economy is dominated by the integrated resort gaming sector, with supplementary business in finance, trade, and the emerging Hengqin co-operation zone. The physical security environment is among the lowest-risk in Asia; the specific risks that require planning are gaming-sector compliance and the legal framework specific to Chinese special administrative regions.

## The Macao security environment

General crime risk in Macao is low. The risks for business visitors are sector-specific: gaming executives face compliance and junket-related risks; financial sector visitors face the same legal and counter-intelligence considerations that apply across China. PSP Law 2/2002 governs private security licensing.

## Security services in Macao

Discreet close protection, PSP-licensed vetted transport, and compliance-aware risk assessment are the appropriate service profile for Macao business visitors with specific security requirements.

For security services in Macao, see our [bodyguard hire services](/services/bodyguard-hire/) and [executive protection services](/services/executive-protection/).
"""

# NANJING
pages["nanjing.md"] = """---
title: "Nanjing"
description: "Close protection and executive security in Nanjing, China. PSB-compliant security drivers and executive protection for Jiangsu Province's capital."
slug: "nanjing"
h1: "Close Protection in Nanjing, China"
country: "China"
risk_level: "low"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Nanjing | Security Drivers Jiangsu China"
date: "2026-06-20"
threats:
  - type: "Business Intelligence and Legal Risk"
    detail: "Nanjing is a significant industrial, automotive, and defence electronics centre in Jiangsu Province. Executives in automotive, petrochemical, and technology sectors should operate with appropriate counter-intelligence awareness. China's National Security Law, Data Security Law, and exit ban mechanism apply in Nanjing as across China."
  - type: "Digital Surveillance"
    detail: "Like all major Chinese cities, Nanjing operates extensive CCTV and digital surveillance infrastructure. All communications on Chinese networks are subject to monitoring. Standard digital hygiene protocols apply for any Nanjing business visit."
  - type: "General Crime: Low Risk"
    detail: "General violent crime risk for business visitors in Nanjing is low. Nanjing is a well-managed city with a functioning public security infrastructure. Petty theft occurs in tourist and commercial areas but at low rates by Chinese urban standards."
available_services:
  - name: "Security Drivers"
    description: "PSB-compliant vetted drivers for Lukou Airport transfers and in-city movement in Nanjing."
  - name: "Executive Protection"
    description: "Close protection arrangements for senior executives visiting Nanjing's automotive, petrochemical, and technology sector operations. Operates within the MPS Order No. 564 framework."
  - name: "Risk Assessment"
    description: "Pre-travel assessment covering Nanjing's business intelligence environment, legal risk under Chinese law, and digital hygiene briefing."
regulations:
  firearms: "Ministry of Public Security Order No. 564 (2010) governs all commercial security services in China, including Nanjing. PSB registration is required. Foreign security personnel cannot carry arms under Chinese law."
  licensing: "All commercial security operators must hold PSB registration. Security services are provided by licensed Chinese operators. Foreign personnel cannot hold commercial security licences in China."
  foreign_operators: "Foreign security personnel cannot drive or carry arms. Formal security functions must be performed by PSB-registered local personnel. Foreign advisers may accompany in a supervisory capacity."
zones:
  safe:
    - "Xinjiekou CBD: Central business district with major hotels, corporate offices, and commercial banking. Primary operating zone for business visitors."
    - "Jianye District (Olympic Sports Centre Area): Convention and commercial zone with international hotel brands."
    - "Jiangning Economic and Technological Development Zone: Automotive and electronics manufacturing district. Primary zone for industrial sector visits."
    - "Qinhuai River Historic District: Tourism and leisure zone near the Confucius Temple area."
  elevated:
    - "Nanjing South Railway Station peripheral areas: High density transit zone; standard urban precautions apply."
emergency_contacts:
  - service: "Emergency (Police/Fire/Ambulance)"
    number: "110 / 119 / 120"
  - service: "Nanjing Drum Tower Hospital International"
    number: "+86 25 8310 4204"
  - service: "Nanjing First Hospital"
    number: "+86 25 5222 7806"
  - service: "British Consulate-General Shanghai (nearest to Nanjing)"
    number: "+86 21 3279 2000"
  - service: "US Consulate-General Shanghai (nearest to Nanjing)"
    number: "+86 21 8011 2000"
warnings:
  - "Nanjing Lukou International Airport (NKG) is approximately 39 kilometres from the Xinjiekou CBD, making it one of the longer airport-to-city distances among China's Tier 2 cities. Factor 45 to 70 minutes transfer time into arrival and departure scheduling."
  - "China's exit ban mechanism can prevent foreign nationals from leaving during commercial disputes or investigations. Executives in complex transactions or regulatory engagement should assess this risk before travel."
  - "Digital devices taken into China should be treated as potentially exposed. Brief on digital hygiene before any Nanjing visit, particularly for automotive or technology sector visits where commercial sensitivity is highest."
  - "British consular cover for Nanjing is provided by the Shanghai Consulate-General. US consular cover is similarly based in Shanghai. Factor the approximately 300-kilometre distance when assessing emergency consular response."
related_cities:
  - name: "Shanghai"
    slug: "shanghai"
  - name: "Beijing"
    slug: "beijing"
  - name: "Wuhan"
    slug: "wuhan"
faqs:
  - question: "What sectors bring business visitors to Nanjing?"
    answer: "Nanjing is the capital of Jiangsu Province and one of China's most significant industrial cities. Key sectors include automotive manufacturing (SAIC-Volkswagen, Nanjing Automobile Group now part of SAIC), petrochemicals and chemical engineering (Nanjing Chemical Industry Park), electronics and telecommunications, and higher education and research. Jiangsu Province as a whole is one of China's wealthiest provinces by GDP, generating significant financial and manufacturing sector business travel."
  - question: "Is Nanjing a high-risk destination for business travel?"
    answer: "Nanjing is a low-risk business destination for physical security purposes. The risks that require planning are the same China-wide considerations: business intelligence exposure, legal risk under Chinese data and national security laws, and digital surveillance environment. These are addressed through pre-travel briefing and PSB-compliant vetted transport rather than protective security measures typical of high-crime environments."
  - question: "How far is NKG Lukou from Nanjing city centre?"
    answer: "Nanjing Lukou International Airport (NKG) is approximately 39 kilometres from the Xinjiekou central business district. Transfer time via the Lukou Airport Expressway is typically 45 to 65 minutes under normal conditions. Peak-hour congestion on the expressway and the Nanjing outer ring road can extend this to 75 to 90 minutes. The Nanjing Metro Line S1 also connects NKG to the city but is not appropriate for principals requiring security."
  - question: "What PSB compliance checks apply for Nanjing transfer drivers?"
    answer: "All commercial security transport operators in Nanjing must hold PSB (Public Security Bureau) registration under MPS Order No. 564 (2010). A compliant Nanjing operator will be able to produce their current PSB business licence and evidence of driver background verification. These are the same checks that apply to any commercial security engagement across China."
---

Nanjing is the capital of Jiangsu Province and one of China's largest and most historically significant cities, serving as the industrial, educational, and governmental hub for one of the country's wealthiest provinces. Key sectors include automotive manufacturing, petrochemicals, electronics, and higher education. The security environment for business visitors is assessed as low by Chinese urban standards, with the primary risks being business intelligence exposure and the legal framework common to all China operations.

## The Nanjing operating environment

Nanjing's physical security risk for business visitors is low. The risks that require pre-travel attention are China-wide: PSB oversight, digital surveillance, exit ban risk for executives in complex transactions, and business intelligence considerations for automotive and technology sector visits. Ministry of Public Security Order No. 564 (2010) governs commercial security operations.

## Security in Nanjing

PSB-compliant vetted transport and a pre-travel business intelligence briefing are the appropriate baseline for executive movement in Nanjing.

For executive security in Nanjing, see our [close protection services](/services/executive-protection/) and [secure airport transfers](/services/secure-airport-transfers/).
"""

# SHARM EL-SHEIKH
pages["sharm-el-sheikh.md"] = """---
title: "Sharm el-Sheikh"
description: "Close protection and executive security in Sharm el-Sheikh, Egypt. Security assessment for the Sinai Peninsula environment and FCDO against-all-but-essential-travel advisory."
slug: "sharm-el-sheikh"
h1: "Security Services in Sharm el-Sheikh, Egypt"
country: "Egypt"
risk_level: "critical"
hero_image: "Close-Protection-2560.webp"
seo_title: "Close Protection Sharm el-Sheikh | Security Egypt Sinai"
date: "2026-06-20"
threats:
  - type: "Terrorism: Sinai Peninsula"
    detail: "The Sinai Peninsula, on which Sharm el-Sheikh is located, carries one of the highest terrorism risk designations in the Middle East and North Africa region. The Islamic State affiliate Wilayat Sinai (formerly Ansar Beit al-Maqdis) has conducted attacks on Egyptian security forces, infrastructure, and, historically, tourist targets. The 2015 bombing of the Metrojet flight departing Sharm el-Sheikh killed 224 people and triggered extensive international flight bans to SSH. FCDO advises against all travel to most of the Sinai Peninsula and against all but essential travel to Sharm el-Sheikh. US State Department rates the Sinai at Level 4: Do Not Travel."
  - type: "Aviation Security"
    detail: "SSH Sharm el-Sheikh International Airport has been the subject of specific aviation security concerns since the 2015 Metrojet bombing. UK flights to SSH were suspended from 2015 to 2019 following a UK government security assessment of SSH airport infrastructure. Some restrictions on carry-on electronics have applied at various points since 2017. Check current aviation security advisories before any flight to or from SSH."
  - type: "Kidnapping and Hostage Risk"
    detail: "Kidnapping risk in the Sinai Peninsula is high and is specifically referenced in FCDO and US State Department advisories. While the resort zone in Sharm el-Sheikh is more controlled than the north and central Sinai, movement outside the resort corridor carries very high kidnap risk. Do not travel outside the Sharm el-Sheikh resort zone under any circumstances without a current security assessment."
  - type: "General Crime in Resort Zone"
    detail: "Within the Sharm el-Sheikh resort zone (Naama Bay, Sharm el-Sheikh Bay, and the main resort areas), the general crime risk is moderate. Petty theft and opportunistic crime target tourists. Vehicle crime and scams targeting arriving visitors at SSH airport are documented."
available_services:
  - name: "Security Assessment"
    description: "Pre-travel and in-country security assessment for organisations that must operate in the Sharm el-Sheikh area despite the FCDO advisory. Assessment covers the terrorism picture, movement restrictions, and contingency planning."
  - name: "Security Drivers"
    description: "Licensed vetted drivers for SSH airport transfers and movement within the Sharm el-Sheikh resort zone. Assessment of movement outside the resort zone on a case-by-case basis."
  - name: "Risk Assessment"
    description: "Ongoing threat assessment for organisations with operational requirements in Sharm el-Sheikh or the wider Sinai. Includes terrorism monitoring and movement protocol design."
  - name: "Event Security"
    description: "Security arrangements for conferences and corporate events at Sharm el-Sheikh resort venues, including COP27-era infrastructure. Includes venue security assessment and close protection for high-profile delegates."
regulations:
  firearms: "Egyptian private security is governed by the Ministry of Interior under Law 394 of 1954 as amended. All private security companies must hold Ministry of Interior licences. Armed security is available through licensed Egyptian operators."
  licensing: "Security companies in Egypt must hold a licence from the Egyptian Ministry of Interior. Verify current licence status and sector-specific authorisations before any engagement in Sharm el-Sheikh."
  foreign_operators: "Foreign security personnel may operate in advisory and supervisory roles. Armed security must be provided by licensed Egyptian operators under Ministry of Interior supervision."
zones:
  safe:
    - "Naama Bay: Primary resort hotel zone. Egyptian security forces maintain a significant presence in the resort corridor. The major international-brand hotels are in Naama Bay."
    - "Sharm el-Sheikh Bay (Old Market Area): Secondary resort zone south of Naama Bay. More local commercial character but still within the security-managed resort corridor."
    - "Ras Nasrani (northern resort fringe): Upper-end resort hotels north of Naama Bay. Within the managed security corridor."
  elevated:
    - "North Sinai (Arish, Sheikh Zuweid, Rafah): FCDO advises against all travel. Active conflict zone."
    - "Central Sinai (outside resort corridor): FCDO advises against all travel. Terrorism and kidnap risk."
    - "Movement between Sharm el-Sheikh and Cairo by road: Very high risk. Road transit through Sinai is subject to attack and ambush. Do not travel by road from SSH to Cairo."
emergency_contacts:
  - service: "Egyptian Police Emergency"
    number: "122"
  - service: "Egyptian Ambulance"
    number: "123"
  - service: "Sharm International Hospital"
    number: "+20 69 366 0893"
  - service: "Hyperbaric Medical Center (diving emergencies)"
    number: "+20 69 366 0922"
  - service: "British Embassy Cairo (serves Sharm el-Sheikh)"
    number: "+20 2 2791 6000"
  - service: "US Embassy Cairo"
    number: "+20 2 2797 3300"
warnings:
  - "FCDO advises against all travel to most of the Sinai Peninsula and against all but essential travel to Sharm el-Sheikh itself. US State Department rates the Sinai Peninsula at Level 4: Do Not Travel. These advisories are driven by terrorism risk from Wilayat Sinai and kidnapping risk in the wider Sinai."
  - "Do not travel between Sharm el-Sheikh and Cairo by road. The Sinai road network between SSH and Cairo passes through areas with terrorism and ambush risk. Travel between SSH and Cairo must be by air only."
  - "Do not move outside the Sharm el-Sheikh resort corridor (Naama Bay, Sharm el-Sheikh Bay, Ras Nasrani) without a current specific security assessment. Movement outside the resort zone enters the risk environment that FCDO and US State Department advisories address."
  - "The 2015 Metrojet crash directly affects the SSH aviation security environment. UK and some other national carriers have restrictions or enhanced security requirements for SSH routes. Confirm current aviation security status with your airline and the relevant national government advisory before any SSH flight."
related_cities:
  - name: "Cairo"
    slug: "cairo"
  - name: "Dubai"
    slug: "dubai"
  - name: "Tel Aviv"
    slug: "tel-aviv"
faqs:
  - question: "Is Sharm el-Sheikh safe to visit for business?"
    answer: "Sharm el-Sheikh is not recommended for general business travel. FCDO advises against all but essential travel to the city due to the Sinai Peninsula terrorism environment. The resort zone within Sharm el-Sheikh has a managed security presence, and major conference events (including COP27 in 2022) have been held here with extensive Egyptian government security deployments. Travel to SSH for an essential business reason -- a major conference, critical client meeting -- requires a full security assessment and should be conducted using the resort-zone model only, with air travel to and from SSH."
  - question: "What happened at Sharm el-Sheikh in 2015?"
    answer: "On 31 October 2015, a Metrojet Airbus A321 carrying 224 passengers and crew departed Sharm el-Sheikh International Airport and crashed in the Sinai Desert 23 minutes after take-off. All on board were killed. The investigation concluded the aircraft was destroyed by an explosive device. Wilayat Sinai claimed responsibility. The UK government suspended all flights to SSH in November 2015 following a security assessment of the airport, citing an unacceptable level of aviation security risk. Flights resumed in October 2019 after Egyptian authorities implemented UK-specified security improvements."
  - question: "Can I drive from Sharm el-Sheikh to Cairo?"
    answer: "No. Road travel between Sharm el-Sheikh and Cairo via the Sinai road network carries very high terrorism and ambush risk and is specifically advised against by FCDO and US State Department. Travel between SSH and Cairo must be by air: the flight takes approximately 1 hour 20 minutes. Do not use any ground transport route that leaves the Sharm el-Sheikh resort corridor into the Sinai interior."
  - question: "How far is SSH airport from Naama Bay?"
    answer: "Sharm el-Sheikh International Airport (SSH) is approximately 18 kilometres from Naama Bay, the primary resort hotel zone. Transfer time is typically 20 to 30 minutes via the main Sharm el-Sheikh resort highway. Pre-arranged collection by a vetted driver is the appropriate approach; unvetted taxi operators at SSH arrivals have documented histories of price-setting scams and in some cases have diverted passengers to venues other than those requested."
---

Sharm el-Sheikh is an Egyptian resort city on the southern tip of the Sinai Peninsula, best known as a Red Sea dive and beach destination and, since hosting COP27 in November 2022, as a venue for major international conferences. The city occupies a complex security position: the resort zone is actively managed by Egyptian security forces, but it sits within the Sinai Peninsula, which carries one of the highest terrorism designations in the Middle East and North Africa region. Travel to Sharm el-Sheikh requires a careful assessment of the specific visit requirements against the FCDO and US State Department advisories.

## The Sinai security context

FCDO advises against all travel to most of the Sinai Peninsula and against all but essential travel to Sharm el-Sheikh. US State Department rates the Sinai at Level 4: Do Not Travel. These advisories reflect the presence of Wilayat Sinai, an Islamic State affiliate that has conducted attacks on Egyptian security forces, infrastructure, and international aviation. The 2015 Metrojet bombing is the most prominent single incident in the Sharm el-Sheikh security record.

## Operating in Sharm el-Sheikh

Any business engagement in Sharm el-Sheikh must be treated as essential-travel-only, with resort-zone movement discipline, air travel to and from the city, and a full pre-travel security assessment.

For security assessment and services in Sharm el-Sheikh, see our [risk assessment services](/services/risk-assessments/) and [executive protection services](/services/executive-protection/).
"""

for filename, content in pages.items():
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w") as f:
        f.write(content.lstrip("\n"))
    print(f"Written: {filepath}")

print(f"\nBlock 5 complete: {len(pages)} city pages written.")
