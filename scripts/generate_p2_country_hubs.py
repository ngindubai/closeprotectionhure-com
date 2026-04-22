"""
Stage 2F: Generate P2 Country Hub Pages
Workers: Wordsmith + Optimiser + Interrogator + Chameleon
"""

import os

OUTPUT_DIR = r"c:\Users\garet\Desktop\Research\security-bodyguard\site\content\countries"

# 20 P2 country hub definitions
# Format: slug, title, h1, risk_level, description, regulations, cities_list, faqs, body
countries = [

    {
        "slug": "uk",
        "title": "United Kingdom",
        "h1": "Security Services in the United Kingdom",
        "risk_level": "medium",
        "description": "Close protection and executive security services in the United Kingdom. SIA-licensed bodyguards and security drivers in London and across the UK from vetted operators.",
        "regulations": {
            "firearms": "Private close protection in the UK is almost entirely unarmed. The Security Industry Act 2001 governs all private security. Firearms for private security require Firearms Certificate, Home Office approval, and specialist police liaison. Armed CP is the exception, not the norm.",
            "licensing": "SIA (Security Industry Authority) licensing is mandatory for all Door Supervisors, Close Protection Officers, Security Guards, and CCTV Operators. The Close Protection licence requires specialist training (Level 3 Award or equivalent). SIA checks criminal records and bans anyone with relevant convictions.",
            "foreign_operators": "Foreign nationals can work as CP officers in the UK with a valid SIA licence. Overseas qualifications require assessment against UK standards. Foreign companies can operate in the UK provided all personnel hold current SIA licences."
        },
        "cities": [
            {"name": "London", "slug": "london", "risk_level": "medium", "summary": "Major business and UHNWI hub. MI5 terrorism threat level SEVERE. SIA-licensed close protection required for all commercial CP operations. Unarmed protection standard."}
        ],
        "faqs": [
            {"q": "Do bodyguards in the UK need to be licensed?", "a": "Yes. All close protection officers working commercially in the UK must hold a current SIA Close Protection licence. Operating without a valid SIA licence is a criminal offence. Licences are issued for a three-year period following background checks and training verification. Check any operator's SIA licence status at the SIA public register before engaging."},
            {"q": "Can bodyguards carry firearms in the UK?", "a": "Generally no. The UK has strict firearms legislation and private armed close protection is not standard practice. In exceptional circumstances involving credible life-threatening intelligence, arrangements can be made with Home Office involvement and specialist police liaison. The default for all commercial close protection work in the UK is unarmed."},
            {"q": "What is the terrorism threat level in the UK?", "a": "MI5 currently rates the UK terrorism threat level as SEVERE, meaning an attack is highly likely. The main vectors are knife attacks, vehicle attacks, and small arms incidents. This has been the sustained background level since 2017. For most corporate travellers, this threat level represents an ambient background risk rather than a specific personal threat."},
            {"q": "Why would a London visitor need close protection?", "a": "Corporate executives attending sensitive meetings, UHNWI individuals with known public profiles, celebrities, individuals in dispute situations, or anyone with a credible personal threat assessment. Standard business travellers to London do not require close protection."}
        ],
        "body": """The United Kingdom is Europe's largest private security market and the most developed close protection sector outside the United States. London alone has thousands of licensed close protection officers, a function of the UHNWI concentration, foreign government delegations, celebrity entertainment industry, and corporate security demand.

SIA licensing is the legal baseline for all commercial CP work. The Security Industry Authority maintains a public register of licensed individuals. Checking an operator's current licence status takes minutes and should be a non-negotiable part of any engagement.

## The UK threat environment

The UK runs a sustained SEVERE terrorism threat level, reflecting credible intelligence about attack planning. The 2017 Westminster Bridge, London Bridge, Manchester Arena, and Finsbury Park attacks demonstrated the range of methods and target types active in this environment. Since then, a significant number of further plots have been disrupted.

For corporate visitors and residents, the practical implication is heightened awareness at crowded public places, transport hubs, and iconic landmarks. Specific personal threat elevates this baseline and warrants professional assessment.

## SIA licensing and what it means

A licensed close protection officer has passed criminal record checks, identity verification, the Right to Work check, and holds the required qualification (typically the Level 3 Award in Close Protection). This is the minimum standard.

Beyond the licence, the quality variation is significant. Military or police close protection experience, specific threat environment training, surveillance awareness, and driver security training all differentiate operators. The SIA licence gets you the door. Vetting beyond the licence gets you the professional.

## London-specific considerations

London security operations involve vehicle and route planning, awareness of firearms restrictions, protest and civil disorder contingency, and close coordination with the Metropolitan Police's Close Protection Unit for the highest-risk principals. All close protection work in London is unarmed as standard."""
    },

    {
        "slug": "usa",
        "title": "United States",
        "h1": "Security Services in the United States",
        "risk_level": "medium",
        "description": "Executive protection and close protection services across the United States. Licensed bodyguards in New York, Los Angeles, Miami, and all major US cities from vetted operators.",
        "regulations": {
            "firearms": "US firearms law is primarily state-governed. In many states, licensed security professionals can carry concealed firearms with appropriate state permits. New York has highly restrictive pistol permits. Texas, Florida, and most southern states are comparatively permissive. Federal agents and law enforcement retain separate authority. Armed executive protection is a well-established market segment in the USA.",
            "licensing": "There is no federal bodyguard licence in the United States. Each state has its own requirements. New York requires a Security Guard Registration through the NYS Division of Licensing Services. California requires a Guard Card from BSIS. Many states require additional training for armed guards. The quality of licensing varies significantly between states.",
            "foreign_operators": "Foreign security companies can operate in the US but must comply with each state's licensing requirements. Personnel require appropriate US work authorisation (visa). Foreign nationals seeking to carry firearms in the US face additional complexity depending on immigration status and state law."
        },
        "cities": [
            {"name": "New York", "slug": "new-york", "risk_level": "medium", "summary": "Primary US executive protection market. DHS terrorism alert active. Elevated threat against corporate executives post-December 2024. NYS Security Guard licence required."}
        ],
        "faqs": [
            {"q": "Is there a federal licence for bodyguards in the USA?", "a": "No. The United States has no federal bodyguard or close protection licence. Licensing is state-specific. A security professional needs to comply with the regulations of each state in which they operate. New York, California, and Florida each have different requirements. Always verify that operators hold the correct state-level authorisation for your location."},
            {"q": "Can bodyguards carry firearms in the USA?", "a": "In most US states, yes, provided the individual holds the relevant state carry permits and has completed required firearms training. New York City is a significant exception: its pistol permit process is highly restrictive and most private bodyguards in NYC operate unarmed unless they are former law enforcement with specific exemptions. Confirm firearms authorisation on a state-by-state basis."},
            {"q": "Why has executive protection demand increased in the US recently?", "a": "The December 2024 killing of a healthcare insurance executive in Midtown Manhattan triggered a significant reassessment of corporate executive security posture across US companies. Many Fortune 500 firms subsequently reviewed and expanded close protection arrangements. C-suite threat awareness has increased materially since that incident."},
            {"q": "What security measures should executives take in New York?", "a": "In Midtown and the Financial District, the primary risk vectors are targeted attack, opportunistic crime, and terrorist events. Practical measures include route variation, vehicle security, advance checking of meeting venues, and awareness of protest and crowd events. Full close protection is advisable for executives with known public profiles or specific threat indicators."}
        ],
        "body": """The United States is the world's largest executive protection market. The concentration of UHNWI individuals, corporate headquarters, entertainment industry, and political activity creates sustained demand across multiple cities.

The December 2024 assassination of a healthcare executive in Midtown Manhattan changed the conversation for many corporate security programmes. What was previously treated as a specialised concern for a small set of high-profile individuals became a board-level discussion for Fortune 500 companies. Enquiries for US executive protection rose significantly in the months following that incident.

## State-by-state complexity

The absence of a federal licence means US security services operate under a patchwork of state regulations. A close protection detail covering an executive travelling from New York to Texas to California is navigating three distinct regulatory frameworks. Operators with genuine national coverage need licences in each state of operation.

## Threat environment by city

New York's threat environment concentrates on terrorism (DHS SEVERE equivalent), targeted executive risk, and protest-related disruption. Los Angeles adds a higher ambient crime rate in parts of the city, particularly around DTLA and parts of South LA. Miami's threat profile includes international HNWI visitors who may carry higher personal risk profiles from their countries of origin.

## Armed versus unarmed protection

The US armed protection market is mature. Many corporate close protection details in Texas, Florida, and other permissive states operate armed as standard. New York City remains primarily unarmed for most commercial operations due to licensing constraints. The armed/unarmed decision is location-specific and driven by threat assessment and principal preference."""
    },

    {
        "slug": "france",
        "title": "France",
        "h1": "Security Services in France",
        "risk_level": "medium",
        "description": "Executive protection and close protection services in France. Licensed bodyguards in Paris and major French cities from vetted, CNAPS-authorised operators.",
        "regulations": {
            "firearms": "Private close protection in France is predominantly unarmed. Firearms for private security require authorisation from the Prefecture under highly restrictive conditions. Armed private security exists but is limited to cash transport and certain critical infrastructure. Close protection of private clients is almost always unarmed.",
            "licensing": "CNAPS (Conseil National des Activités Privées de Sécurité) regulates all private security in France. Close protection requires a Carte Professionnelle from CNAPS following background checks and training certification (usually a CQP-APS, the professional qualification). Employers must also hold a CNAPS authorisation.",
            "foreign_operators": "EU security professionals can work in France with equivalent home-country qualifications subject to CNAPS recognition. Non-EU operators must obtain full French authorisation. Foreign companies operating in France must hold CNAPS authorisation and employ CNAPS-licensed personnel."
        },
        "cities": [
            {"name": "Paris", "slug": "paris", "risk_level": "medium", "summary": "Major UHNWI and corporate hub. Sustained SEVERE terrorism threat level. CNAPS-licensed close protection required. Pickpocket gangs operate systematically on RER B and tourist sites."}
        ],
        "faqs": [
            {"q": "What is CNAPS and why does it matter?", "a": "CNAPS is the French national private security regulator. Every commercial close protection officer in France must hold a CNAPS Carte Professionnelle. Without it, they are operating illegally regardless of their qualifications or experience. CNAPS also authorises security companies. Before engaging any French security provider, check that both the company and its personnel hold current CNAPS authorisation."},
            {"q": "Is the terrorism threat in France serious?", "a": "France has experienced some of the most severe terrorist attacks in Western Europe. The 2015 Paris attacks (130 killed), the 2016 Nice truck attack (86 killed), and multiple knife attacks and school shootings since 2020 reflect a persistent and active threat. VIGIPIRATE, France's national security alert system, has been maintained at emergency levels for extended periods. This is a serious background threat for all visitors."},
            {"q": "What are the main security risks for visitors to Paris?", "a": "Pickpocket gangs operating on the RER B line (airport routes), at Gare du Nord, at the Eiffel Tower, and along the Champs-Elysees are a well-documented systematic risk. Drink spiking has been reported in bars and nightlife venues. Terrorism is a background threat particularly at crowded events. Street crime in outer arrondissements after dark. Most corporate visitors experience none of these, but awareness is appropriate."},
            {"q": "Do I need close protection in France for a business trip?", "a": "Most corporate visitors to Paris do not require close protection. The exceptions are individuals with specific threat profiles, UHNWI individuals in conspicuous settings, entertainment industry principals, or executives in dispute situations. A professional threat assessment for France identifies whether close protection is warranted for your specific circumstances."}
        ],
        "body": """France is Europe's second-largest economy and Paris is one of the world's primary concentrations of UHNWI individuals, luxury brands, and corporate headquarters. The private security market is well-developed and regulated under CNAPS.

The terrorism threat in France is not theoretical. Since 2015, France has suffered more mass-casualty terrorist attacks than any other Western European nation. FCDO currently classifies France at NORMAL status, but notes that terrorists are very likely to carry out attacks. The French internal security service (DGSI) maintains one of Europe's most active counter-terrorism programmes.

## CNAPS: the regulatory framework

All commercial security activity in France requires CNAPS authorisation. The system covers close protection, guarding, private investigation, surveillance, and cash transport. CNAPS maintains public registers of both companies and individual personnel.

The CQP-APS (Certificat de Qualification Professionnelle Agent de Prévention et de Sécurité) is the standard professional qualification. Close protection specialists typically hold additional EP-specific training from recognised academies.

## Paris security landscape

Paris concentrates the majority of French close protection demand. Fashion weeks, art auctions, real estate visits, and corporate events all generate requirements. Many foreign HNWI clients visit Paris with their own security details, which creates a unique operational environment: foreign teams must comply with French law, including the unarmed restriction for private security.

## Major events and crowd considerations

France hosts major international sporting events, political summits, and fashion events throughout the year. Large crowds and the elevated terrorism threat combine to make advance planning particularly important. The 2024 Paris Olympics generated significant security infrastructure improvements that remain in place."""
    },

    {
        "slug": "germany",
        "title": "Germany",
        "h1": "Security Services in Germany",
        "risk_level": "medium",
        "description": "Executive protection and close protection in Germany. Licensed bodyguards in Berlin, Frankfurt, Munich, and Hamburg from vetted operators with German trade association accreditation.",
        "regulations": {
            "firearms": "Private security firearms in Germany are strictly regulated under the Weapons Act (Waffengesetz). Unarmed close protection is standard. Armed private security is limited to specific contexts (cash transport, critical infrastructure). Close protection of private clients is almost always unarmed.",
            "licensing": "Security work in Germany requires a trade certificate (Gewerbeschein) from the relevant district authority. Close protection officers must complete a recognised training programme. The industry association BDSW (Bundesverband der Sicherheitswirtschaft) sets quality standards. Personnel must pass background checks via the relevant state authority.",
            "foreign_operators": "EU security professionals can work in Germany subject to trade registration requirements. Non-EU operators must comply with German work authorisation rules. Foreign companies must register for German trade activity. The Unterrichtungsnachweis (basic security certificate) or the Sachkundeprüfung (trade exam) are the standard qualification routes."
        },
        "cities": [
            {"name": "Berlin", "slug": "berlin", "risk_level": "medium", "summary": "German capital and growing tech hub. MI5-equivalent threat level: high/very likely. Anti-semitic incidents elevated. Organised pickpocket and street crime in tourist zones."}
        ],
        "faqs": [
            {"q": "Is there a recognised bodyguard qualification in Germany?", "a": "Germany's security qualification framework uses the Sachkundeprüfung (trade knowledge exam) administered by the IHK (Chamber of Commerce). For close protection specifically, a number of private academies offer CP training programmes aligned with BDSW standards. There is no single national Close Protection licence equivalent to the UK's SIA CP licence. German operators typically hold a combination of the trade certificate, CP training, and military or police background."},
            {"q": "What are the security risks in Germany?", "a": "Germany has experienced Islamist-inspired terrorist attacks (2016 Berlin Christmas market truck attack, 2020 Hanau shisha bar shooting). Anti-semitic and far-right violence is an elevated risk documented by the BfV (Federal Office for the Protection of the Constitution). Pickpocket crime is systematic in tourist areas of Berlin and Frankfurt. For corporate visitors, the overall risk level is moderate and manageable."},
            {"q": "Do I need a bodyguard in Germany?", "a": "Most corporate visitors to Germany do not require close protection. The primary use cases are HNWI individuals with known profiles, corporate executives in dispute situations, entertainment industry principals, or individuals who have received specific threats. A threat assessment for Germany determines whether close protection is warranted."},
            {"q": "Can foreign bodyguards work in Germany?", "a": "EU nationals can work in Germany with trade registration. Non-EU nationals require appropriate work authorisation. Foreign companies operating in Germany must register for trade activity and ensure personnel meet German qualification standards. In practice, many German EP operations combine German-licensed lead operators with client-provided foreign team members where legally appropriate."}
        ],
        "body": """Germany is Western Europe's largest economy and home to Berlin, Frankfurt, Munich, and Hamburg - four cities generating significant executive protection demand. The German private security market is mature, regulated under federal and state law, and largely unarmed.

BKA (Bundeskriminalamt) statistics document elevated threats from Islamist networks, far-right extremism, and foreign state actors. The 2016 Berlin Christmas market attack (12 killed) and the 2020 Hanau shootings (9 killed) represent the most serious incidents, but German security services have disrupted numerous further plots.

## Regulatory landscape

Germany's security industry operates under a combination of federal trade law (Gewerbeordnung), state-level implementation, and industry association standards. BDSW (Bundesverband der Sicherheitswirtschaft) is the primary industry body and a membership indicator of quality. The IHK Sachkundeprüfung is the standard trade exam.

## Regional demand centres

Frankfurt is the European financial centre where EP demand concentrates on banking and financial services executives. Munich hosts major industry events (Oktoberfest generates distinctive crowd security requirements alongside the corporate EP demand from BMW, MAN, and Siemens headquarters). Berlin's growing tech sector and political function generate a different profile of demand, including foreign government delegations and NGO operations.

## Berlin-specific threat considerations

Berlin has an elevated antis-emitic incident rate documented by the BfV and Jewish community organisations. Political protests, including demonstrations around Israeli and Palestinian issues, can turn confrontational. Berlin's Mitte district concentrates corporate offices, government buildings, and tourist attractions within a relatively compact area."""
    },

    {
        "slug": "japan",
        "title": "Japan",
        "h1": "Security Services in Japan",
        "risk_level": "low",
        "description": "Executive protection and private security services in Japan. Professional close protection officers in Tokyo and across Japan from vetted, Police Act-compliant operators.",
        "regulations": {
            "firearms": "Firearms ownership is essentially prohibited for civilians in Japan under the Sword and Firearms Control Law. Private security carries no firearms. Close protection is entirely unarmed. Police provide armed protection for heads of state and high-threat individuals under specific formal request.",
            "licensing": "Private security is governed by the Security Services Act (Keibi-in Ho). All security personnel must be registered with the Public Safety Commission. Training and examination requirements set by the National Police Agency. Companies must also hold Public Safety Commission authorisation. A specific Close Protection Officer (CPO) category exists with additional requirements.",
            "foreign_operators": "Foreign security companies must establish a Japanese legal entity and obtain Public Safety Commission authorisation. Foreign nationals must hold a valid Japanese work visa. Language proficiency is a practical requirement given operational coordination with Japanese law enforcement and clients."
        },
        "cities": [
            {"name": "Tokyo", "slug": "tokyo", "risk_level": "low", "summary": "One of the world's safest major cities. Low ambient crime. Terrorist threat exists but attacks are rare. Stalker risk elevated for entertainment industry and high-profile executives. Unarmed protection standard."}
        ],
        "faqs": [
            {"q": "Is Japan safe for corporate travellers?", "a": "Japan has consistently ranked among the world's safest countries. Violent crime is extremely low by international standards. Pickpocketing is minimal compared to European cities. The terrorism risk exists but has not materialised as a mass-casualty attack in recent decades. For most corporate visitors, Japan presents a manageable and low-threat environment."},
            {"q": "When would someone need close protection in Japan?", "a": "Entertainment industry principals visiting Japan face a specific stalker risk: Japan has a documented problem with obsessive fan behaviour targeting performers and athletes. Corporate executives of major Japanese companies face targeted approaches from organised crime (yakuza liaison is a specific skill in Japanese EP). Foreign executives in high-profile deal situations or those who have received threats warrant close protection regardless of the low ambient risk level."},
            {"q": "Can bodyguards carry firearms in Japan?", "a": "No. Japanese law prohibits firearms for private security personnel. All commercial close protection in Japan is unarmed. This is a legal absolute, not a preference. Protection relies on surveillance awareness, route planning, physical interposition, and rapid coordination with police."},
            {"q": "What is the regulatory process for security companies in Japan?", "a": "Security companies must obtain authorisation from the Public Safety Commission of the relevant prefecture. All employed security officers must be registered individually with their prefectural Public Safety Commission. The Security Services Act sets mandatory training requirements including both theoretical and practical components. Companies must complete regular compliance reviews."}
        ],
        "body": """Japan is one of the world's safest countries by almost any crime metric. The homicide rate is among the lowest globally. Robbery, assault, and street crime at a level that would concern visitors to London or New York are near-absent in Tokyo's major business districts.

This low crime environment does not mean Japan is without security concerns. The 2022 assassination of former Prime Minister Shinzo Abe demonstrated that political violence, while extremely rare, can occur. A 2023 attack on Prime Minister Kishida followed. Yakuza-connected disputes, targeted corporate intelligence operations, and the specific stalker risk in entertainment circles all generate close protection demand.

## The Japanese EP market

Close protection in Japan is provided under the Security Services Act framework. All CPOs are unarmed. The skill set emphasises surveillance awareness, route intelligence, crowd navigation, and discreet coordination with National Police Agency protocols.

Japanese close protection operations frequently involve cultural and linguistic integration. A principal operating in Japanese corporate settings benefits from a security detail that can read the environment and communicate without creating visible disturbance. Operational discretion is highly valued in Japanese corporate culture.

## Entertainment and celebrity protection

Japan's entertainment industry creates a specific protection requirement driven by stalker incidents. High-profile performers, athletes, and public figures have been targeted by obsessive individuals in ways that required escalation to violence. Japanese EP teams operating in this sector have developed specific countermeasures that differ from typical corporate EP.

## Corporate intelligence risk

Japan's technology, automotive, and pharmaceutical sectors attract foreign corporate intelligence activity. Executives travelling to Japan for sensitive negotiations may benefit from technical surveillance awareness and secure communications protocols."""
    },

    {
        "slug": "china",
        "title": "China",
        "h1": "Security Services in China",
        "risk_level": "medium",
        "description": "Executive protection and security services in China. Close protection in Beijing, Shanghai, and Hong Kong from vetted, legally compliant operators with China operations experience.",
        "regulations": {
            "firearms": "Firearms are essentially prohibited for private security in mainland China. All close protection is unarmed. State security forces carry weapons. In Hong Kong, private security is also unarmed though the regulatory framework differs from mainland China.",
            "licensing": "Mainland China security services are governed by the Regulation on Security Services (2009). Companies require a Public Security Bureau permit. Individual security personnel require certification through recognised training. Foreign security companies face significant restrictions on independent operation. In Hong Kong, security is regulated under the Security and Guarding Services Ordinance (Cap 460).",
            "foreign_operators": "Foreign security companies face severe restrictions in mainland China. Direct foreign operation is prohibited. Joint ventures with PRC entities are the formal pathway but practical operation requires navigating significant legal and political complexity. The National Intelligence Law (2017) creates obligations for all entities in China to cooperate with state intelligence. In Hong Kong, overseas operators face different but still significant constraints."
        },
        "cities": [
            {"name": "Beijing", "slug": "beijing", "risk_level": "medium", "summary": "PRC capital. Political sensitivity requires careful operational discretion. Foreign executive risk from anti-espionage legislation. Corporate intelligence risk significant. Unarmed protection only."},
            {"name": "Shanghai", "slug": "shanghai", "risk_level": "medium", "summary": "Primary commercial hub. Low ambient crime. Anti-espionage law creates specific risk for corporate executives. Operational security for sensitive meetings critical."},
            {"name": "Hong Kong", "slug": "hong-kong", "risk_level": "medium", "summary": "SAR status. HNWI and financial services hub. National Security Law (2020) has changed the legal environment significantly. Separate regulatory framework from mainland."}
        ],
        "faqs": [
            {"q": "What risks do corporate executives face in China?", "a": "China's counter-espionage law and the National Intelligence Law create specific risks for executives attending sensitive commercial negotiations, conducting due diligence, or working in restricted technology sectors. Foreign executives have been detained under these laws. The practical risks are corporate intelligence operations (room searches, device compromise, network surveillance), and the escalating possibility of detention for individuals involved in business disputes or sensitive sectors. These are different risk vectors from the crime-based threats common in other markets."},
            {"q": "How has Hong Kong changed since the National Security Law?", "a": "The National Security Law (2020) has materially changed Hong Kong's legal environment. Activities that were lawful political expression before 2020 now carry criminal liability. Foreign executives should be aware that statements made outside Hong Kong about Hong Kong affairs can in principle be prosecuted under this law if the individual enters Hong Kong. The legal environment is significantly less predictable than before 2020."},
            {"q": "Can foreign security companies operate in China?", "a": "Not independently. Mainland China restricts foreign security companies from direct operation. The legal pathway is a joint venture with a licensed PRC entity. In practice, foreign executives in China typically operate through trusted networks of former law enforcement or military professionals rather than formal foreign security company structures. Always verify that any security arrangement in China is legally compliant with PRC and applicable home-country law."},
            {"q": "What is the surveillance environment in China?", "a": "China operates one of the world's most extensive public surveillance infrastructure networks, covering CCTV, facial recognition, telecommunications monitoring, and internet traffic inspection. Foreign visitors should operate on the assumption that digital devices, hotel rooms, and meeting venues may be technically monitored. Operational security for sensitive commercial discussions in China requires specific preparation including device management and secure communications protocols."}
        ],
        "body": """China presents a fundamentally different security picture from other major business destinations. Ambient street crime for corporate visitors in Beijing and Shanghai is low. The risks are predominantly in the categories of corporate intelligence, state surveillance, and the legal exposure created by China's security legislation.

The 2017 National Intelligence Law requires all organisations and citizens to support, assist, and cooperate with state intelligence work. This creates a specific risk for foreign executives: staff at hotels, translation services, venues, and partner companies may all be subject to these obligations. The 2023 expansion of China's anti-espionage law broadened the definition of espionage to include undefined categories of information relevant to national security.

## Operating safely in China

The executive protection approach for China differs from high-crime markets. Physical security is secondary to operational security. The priorities are device management before and during travel, secure communications for sensitive discussions, advance threat assessment for the specific business activity, and legal awareness of the expanded espionage definitions.

## Hong Kong: a transitioning environment

Hong Kong maintained a distinct regulatory and legal identity from mainland China for decades. The National Security Law (2020) fundamentally altered this. The courts, police, and prosecutorial services now operate under the influence of the NSL framework. Several foreign companies have reduced their Hong Kong operations or relocated regional headquarters. Those that remain operate in a demonstrably different legal environment from 2020 and earlier.

## Executive protection in China: practical constraints

All close protection in mainland China is unarmed. Foreign security teams face legal constraints on direct operation. The most practical approach for visiting executives is to engage through trusted networks with deep China experience, supplement with pre-travel operational security preparation, and maintain clear protocols for emergency communication and extraction."""
    },

    {
        "slug": "singapore",
        "title": "Singapore",
        "h1": "Security Services in Singapore",
        "risk_level": "low",
        "description": "Executive protection and private security in Singapore. Professional close protection from licensed operators in one of Asia's safest business hubs.",
        "regulations": {
            "firearms": "Private security is entirely unarmed in Singapore. Firearms are strictly controlled under the Arms Offences Act. Penalties for firearms offences are among the most severe globally. Close protection relies entirely on physical presence, route management, and coordination with police.",
            "licensing": "The Security Industry Regulatory Department (SIRD) under the Singapore Police Force regulates all private security. Close protection officers must hold a Security Officer (SO) licence from SIRD, which requires training at an approved security agency and background clearance by SPF. Companies must hold a Security Agency Licence.",
            "foreign_operators": "Foreign nationals can work in Singapore security with appropriate work passes and SIRD licensing. Foreign companies must establish a Singapore entity and hold a Singapore Security Agency Licence. All personnel must be SIRD-licensed regardless of overseas qualifications."
        },
        "cities": [
            {"name": "Singapore", "slug": "singapore", "risk_level": "low", "summary": "One of Asia's safest cities. Unarmed protection only. Primary demand from HNWI, government delegations, and entertainment. Low ambient crime but terrorism threat background."}
        ],
        "faqs": [
            {"q": "Do I need close protection in Singapore?", "a": "For most corporate visitors, Singapore presents very low ambient risk. The use cases for close protection in Singapore are: UHNWI individuals, foreign government delegations, entertainment industry principals, individuals with specific threat profiles from their home countries, and high-net-worth individuals attending events where their presence is publicly known. Singapore's general safety level does not eliminate profile-based risk."},
            {"q": "What is Singapore's terrorism threat level?", "a": "Singapore maintains its own terrorism threat assessment and has classified Singapore's threat as 'high' based on its position as a regional hub and the proximity to active Islamist networks in Southeast Asia. The Internal Security Department (ISD) has disrupted several plots, including a 2016 plan to launch rocket attacks on Marina Bay. The threat is real but attacks have not occurred due to Singapore's counter-terrorism effectiveness."},
            {"q": "Can a foreign bodyguard accompany a principal to Singapore?", "a": "A foreign close protection officer can travel to Singapore as a visitor accompanying a principal, but cannot operate commercially without a Singapore SIRD licence and appropriate work authorisation. The distinction matters: a long-term private EP arrangement in Singapore requires proper licensing. A principal visiting for a few days and accompanied by their existing EP team may operate under different considerations but should verify the legal position before arrival."},
            {"q": "How is security regulated in Singapore?", "a": "SIRD (Security Industry Regulatory Department), a division of the Singapore Police Force, oversees all private security. Companies and individuals must hold current licences. SIRD conducts regular inspections and has enforcement powers including suspension and revocation of licences. The regulatory standard is high and enforcement is taken seriously."}
        ],
        "body": """Singapore consistently ranks as one of the world's safest cities. Street crime, robbery, and violent crime are at levels that make Singapore an outlier compared to most other financial centres. The rule of law is strong, police response is reliable, and the regulatory environment for business is transparent.

This low ambient risk does not make Singapore without security considerations. Singapore is a hub for Southeast Asia regional operations, which means executives based there or visiting may carry risk profiles from high-threat markets elsewhere. HNWI individuals in Singapore face the typical profile-based risks of wealthy individuals in any city. Foreign government delegations require professional close protection as a matter of protocol.

## Singapore's security industry

The SIRD-licensed security market in Singapore is professional and disciplined. The regulatory framework is one of the tightest in Southeast Asia. This means operators are generally reliable at the licensed level, but the quality differentiation between firms still matters for executive protection. The unarmed constraint applies to all operations.

## Regional context

Singapore's role as a regional hub means security professionals based there often support operations across the wider Southeast Asia region. Indonesia, Malaysia, Philippines, and Thailand operations are commonly coordinated from Singapore bases. Close protection teams may need to operate across multiple regional jurisdictions, each with their own licensing and legal requirements.

## Fintech and crypto security

Singapore's position as a leading fintech and digital asset hub creates specific security requirements. High-value digital asset holders, crypto executives, and fintech founders face a targeted threat profile that combines both physical security (personal protection, home security) and digital security (device management, account protection)."""
    },

    {
        "slug": "australia",
        "title": "Australia",
        "h1": "Security Services in Australia",
        "risk_level": "low",
        "description": "Executive protection and close protection in Australia. Licensed bodyguards in Sydney, Melbourne, and Perth from vetted operators with current state licensing.",
        "regulations": {
            "firearms": "Australia has strict firearms laws following the 1996 Port Arthur reforms. Private security firearms are limited. Security guards can be licensed to carry firearms in certain circumstances but this is not routine for close protection. Unarmed close protection is the standard across most operations.",
            "licensing": "Security licensing in Australia is state and territory-based, governed by each state's Security Industry Act. Each state has its own licensing body (NSW: Security Licensing and Enforcement Directorate; VIC: Consumer Affairs Victoria; QLD: Office of Fair Trading). Close Protection Officer (CPO) licences are a specific category in most states requiring specialist training.",
            "foreign_operators": "Foreign nationals can work as security professionals in Australia with the appropriate Australian work visa and state licence. Overseas qualifications require assessment against Australian standards. Foreign companies can operate in Australia by ensuring personnel hold the correct state licence for each state of operation."
        },
        "cities": [
            {"name": "Sydney", "slug": "sydney", "risk_level": "low", "summary": "Low ambient risk. Terrorism threat exists and has materialised (2014 Lindt Cafe siege, 2019 stabbing). HNWI and entertainment EP demand. State licence required for all CPO work."}
        ],
        "faqs": [
            {"q": "Is Australia safe for corporate travellers?", "a": "Yes. Australia has low violent crime rates, reliable police, and a stable political environment. State Dept rates Australia at Level 1 (Exercise Normal Precautions). Terrorism is a background threat that has produced incidents (2014 Martin Place siege, multiple disrupted plots) but Australia's domestic threat level is manageable. For corporate visitors, Australia presents a low-threat environment."},
            {"q": "What close protection licence is needed in Australia?", "a": "Each state requires its own security licence. In New South Wales, a Class 1A Security Licence covers guard functions; a Class 1D covers close protection. In Victoria, a Security Industry Licence with CPO endorsement. Licensing is not transferable between states. An operator working in both Sydney and Melbourne needs compliance in both NSW and Victoria. Always verify current state licence status for any operator."},
            {"q": "When would a visitor to Australia need close protection?", "a": "Entertainment industry principals on tour, UHNWI individuals making property visits or attending events, corporate executives in dispute situations, and foreign government delegations all generate CP requirements in Australia. The risk profile of the individual rather than Australia's ambient risk level is the primary driver."},
            {"q": "Is there an executive protection market in Perth?", "a": "Yes. Perth has a significant UHNWI and corporate mining executive community. Resource sector executives, particularly those also operating in Papua New Guinea, Indonesia, and other high-risk mining jurisdictions, sometimes maintain Australian-based EP arrangements that travel internationally. Perth-based operators with high-risk overseas experience are available."}
        ],
        "body": """Australia presents one of the lowest ambient security risk environments of any major economy. Crime is low by developed-country standards, police are reliable, and the political environment is stable. State Dept Level 1 rating reflects a genuine assessment.

Terrorism is a real background threat. ASIO (Australian Security Intelligence Organisation) has disrupted multiple plots and the 2014 Martin Place siege, the 2018 Melbourne car attack, and other incidents demonstrate the threat can materialise. Australia's counter-terrorism framework is well-developed and intelligence cooperation with Five Eyes partners is close.

## State-by-state licensing

The absence of a national security licence is the primary operational complexity for close protection in Australia. Operators working nationally need current state licences across their jurisdictions of operation. NSW's SLED and Victoria's CAV take licensing seriously and enforcement is active.

## Mining and resources sector

Western Australia's resources sector generates a distinct EP demand. Mining executives, particularly those managing operations in Papua New Guinea, Indonesia, and other high-risk Pacific and Southeast Asian jurisdictions, are among the most active EP clients in Australia. Perth-based operators with regional high-risk experience are a specific capability to assess.

## Entertainment and events

Australia's entertainment calendar generates CP requirements around major tours, award events, film productions, and sporting events. Sydney and Melbourne both have established EP markets serving the entertainment industry. UHNWI individuals making lifestyle or property visits generate private client demand."""
    },

    {
        "slug": "qatar",
        "title": "Qatar",
        "h1": "Security Services in Qatar",
        "risk_level": "low",
        "description": "Executive protection and private security in Qatar. Professional close protection in Doha from QSSI-compliant operators with Gulf security experience.",
        "regulations": {
            "firearms": "Private security in Qatar is unarmed. All firearms are state-controlled. Security personnel carry no weapons. Qatar's low crime environment means armed private security is not commercially available or necessary.",
            "licensing": "Qatar Security Services Industry (QSSI) regulates private security. All companies and personnel must hold QSSI licences. Regulatory framework has been substantially developed since Qatar won the 2022 FIFA World Cup hosting rights. Significant investment in security industry professionalisation.",
            "foreign_operators": "Foreign companies must partner with or establish a Qatari entity. Qatari ownership requirements apply. All personnel require Qatar work visas under the sponsorship system. QSSI licensing required for all operational personnel."
        },
        "cities": [
            {"name": "Doha", "slug": "doha", "risk_level": "low", "summary": "Extremely low ambient crime. Regional security hub following 2022 World Cup. HNWI and government delegation protection. Unarmed operations only. QSSI licensing required."}
        ],
        "faqs": [
            {"q": "Is Qatar safe for business travellers?", "a": "Qatar has one of the lowest crime rates in the world. Violent crime is extremely rare. The domestic security environment is stable and the state security apparatus is effective. For corporate visitors, Qatar presents minimal ambient risk. The risks that do exist are primarily legal: Qatar has strict laws on alcohol, public behaviour, and social media activity that can affect visitors unexpectedly."},
            {"q": "What are Qatar's legal risks for visitors?", "a": "Qatar criminalises public intoxication, intimate relations outside marriage, and social media posts that are deemed critical of Qatar, its government, or its neighbours. Photography of government buildings, royal palaces, and military installations is prohibited. Business disputes can result in travel bans that prevent departure. These are legal risks rather than security risks in the conventional sense, but they carry serious consequences."},
            {"q": "Does the regional security environment affect Qatar?", "a": "Qatar's geographic position in the Gulf makes it potentially affected by Iran-related tensions, Yemen conflict spillover, and the broader regional security picture. The 2017-2021 Saudi-led blockade of Qatar demonstrated the country's vulnerability to regional political disputes. The current regional environment (April 2026) includes ongoing Middle East tensions that FCDO has factored into advisories for the Gulf region. Qatar's own domestic stability is strong."},
            {"q": "What security arrangements exist for large events in Qatar?", "a": "Qatar developed substantial event security infrastructure for the 2022 FIFA World Cup. This included training thousands of security officers, installing surveillance infrastructure, and developing crowd management protocols. This capability remains and positions Qatar as a well-prepared event security environment for the major conferences and tournaments it continues to host."}
        ],
        "body": """Qatar has transformed from a relatively obscure Gulf emirate into a significant global hub for sport, media, diplomacy, and investment. Doha hosts the headquarters of Al Jazeera, major UN agencies, and international business operations across energy, finance, and real estate.

The security environment is benign domestically. Crime is rare, the state is stable, and police are responsive. The security challenges in Qatar are primarily legal compliance (alcohol laws, social media), regional instability (Iran, Yemen), and the heightened scrutiny that affects any operation linked to sensitive geopolitics.

## Post-World Cup security infrastructure

The 2022 FIFA World Cup required Qatar to develop significant security industry capacity from a relatively low base. Investment in training, technology, and regulatory frameworks was substantial. The QSSI licensing system is more developed today than it was a decade ago, and operators who built their Qatar presence around the World Cup now represent a more mature market.

## Government delegation and VIP protection

Qatar hosts a high volume of government-level visitors, diplomatic meetings, and peace mediation processes. The security arrangements for these engagements are typically coordinated through the Amiri Diwan (Royal Court) security apparatus. Private close protection for visiting foreign principals in the commercial sector operates within QSSI's framework.

## Energy sector

Qatar's LNG industry attracts senior executives from global energy companies. The energy sector visit programme involves both corporate and government meetings. Security arrangements for energy executives in Qatar are typically light, reflecting the low ambient risk, but protocol compliance and local liaison are standard practice."""
    },

    {
        "slug": "kuwait",
        "title": "Kuwait",
        "h1": "Security Services in Kuwait",
        "risk_level": "low",
        "description": "Executive protection and private security in Kuwait. Professional close protection in Kuwait City from licensed operators with Gulf security expertise.",
        "regulations": {
            "firearms": "Private security in Kuwait is unarmed. Firearms are reserved for state security forces. All close protection personnel carry no weapons.",
            "licensing": "Kuwait's Ministry of Interior regulates private security companies. Companies must hold Ministry of Interior licences. Individual personnel require security officer registration. The regulatory framework is less formalised than some Gulf neighbours but enforcement is active.",
            "foreign_operators": "Foreign companies must partner with or establish a Kuwaiti entity. Kuwaiti ownership involvement is required under commercial laws. Work visas are required for all non-Kuwaiti personnel. All operations must be sanctioned by Ministry of Interior."
        },
        "cities": [
            {"name": "Kuwait City", "slug": "kuwait-city", "risk_level": "low", "summary": "Regional financial hub. Low ambient crime. Unarmed protection only. Primary demand from corporate oil sector and government delegations. Regional security environment monitored."}
        ],
        "faqs": [
            {"q": "What security risks affect Kuwait?", "a": "Kuwait's domestic crime rate is low. The primary security concerns are regional: proximity to Iraq (150km from Kuwait City), the broader Gulf security environment, and the general Iran-related tensions affecting the region. Kuwait was invaded by Iraq in 1990 and the historical memory shapes security protocols. The current threat from Iraqi territory is assessed as low, but the geographic reality means Kuwait monitors regional developments closely."},
            {"q": "Is Kuwait safe for oil sector executives?", "a": "Yes. Kuwait's oil sector attracts significant international executive presence and operates with well-developed security protocols. KPC (Kuwait Petroleum Corporation) facilities operate under their own security arrangements. For visiting executives, Kuwait City's business environment is low-risk by Gulf standards. Regional security monitoring is appropriate given the neighbourhood."},
            {"q": "What legal risks affect visitors to Kuwait?", "a": "Kuwait has strict laws on alcohol (prohibited), public behaviour, and social media. Criticism of the Kuwaiti royal family or government online is a criminal offence. Business disputes can result in travel bans. LGBTQ+ relationships are criminalised. These legal risks require awareness particularly for executives unfamiliar with Gulf legal environments."},
            {"q": "Does Kuwait have professional close protection services?", "a": "Yes, though the Kuwait EP market is smaller than Dubai or Saudi Arabia. Professional operators exist, primarily serving oil company executives, government delegations, and HNWI clients. The operator pool has been supplemented by regional experience from the Dubai and Saudi Arabia markets. Advance vetting is essential as quality varies."}
        ],
        "body": """Kuwait occupies a strategically significant position in the Gulf: oil-wealthy, historically targeted for invasion (1990), and with close proximity to Iraq. The domestic security environment is stable and crime is low. The regional environment requires ongoing attention.

Kuwait City functions as the commercial and governmental hub. The oil sector, government, and financial services generate the primary corporate visitor population. Kuwait's National Assembly (parliament) has a more active political culture than most Gulf states, which occasionally produces protest activity.

## Oil sector security

Kuwait's oil industry involves significant international executive presence. BP, Shell, and numerous contractors maintain Kuwait operations. Security arrangements for oil sector work typically involve coordination between private close protection and the relevant company's security programme. Field sites outside Kuwait City have different threat profiles from the city environment.

## Regional security monitoring

Kuwait's proximity to Iraq means regional developments in that country, and more broadly in the Middle East, directly affect Kuwait's security assessment. FCDO currently rates Kuwait City at normal for most activities while noting the regional tensions as a monitoring factor. Any Gulf operation should include a current regional intelligence briefing rather than relying on historical assessments."""
    },

    {
        "slug": "ghana",
        "title": "Ghana",
        "h1": "Security Services in Ghana",
        "risk_level": "medium",
        "description": "Close protection and executive security in Ghana. Professional security services in Accra from vetted, locally licensed operators with West Africa experience.",
        "regulations": {
            "firearms": "Licensed security companies can carry firearms in Ghana with appropriate Police Service authorisation. Ghana Police Service issues firearms permits for security operations. Armed security is available but requires verified operator licensing.",
            "licensing": "Ghana Police Service regulates private security under the Private Security Organisations Act (2020). All companies must be licensed by the Police Service. Security personnel must be registered. The 2020 Act tightened regulatory requirements compared to previous legislation.",
            "foreign_operators": "Foreign companies must partner with or operate through a locally incorporated Ghanaian entity. All personnel require Ghanaian work authorisation. The Police Service must approve operational plans for foreign operator involvement."
        },
        "cities": [
            {"name": "Accra", "slug": "accra", "risk_level": "medium", "summary": "West Africa's most stable business hub. Moderate ambient crime. Low terrorism risk compared to regional neighbours. Growing EP market driven by oil sector, embassies, and NGOs."}
        ],
        "faqs": [
            {"q": "Is Ghana the safest West African business destination?", "a": "Ghana is consistently rated among the most stable countries in West Africa for business travel. The State Dept rates Ghana at Level 2 (Exercise Increased Caution) rather than the higher levels that apply to Nigeria, Ivory Coast, or Mali. The democratic political culture is more established than most regional neighbours. However, petty crime in Accra, isolated armed robbery incidents, and the knock-on effects of instability in neighbouring countries (Sahel, Burkina Faso) mean security awareness remains appropriate."},
            {"q": "What security concerns exist in Accra?", "a": "Petty crime including pickpocketing, bag snatching, and confidence scams targeting expatriates and business visitors in central Accra. Armed robbery incidents, primarily at night in isolated areas. Cyber fraud (419-variant schemes) targeting businesses. The Osu and Adabraka areas of Accra have elevated crime reports after dark. Standard security precautions manage most risks effectively."},
            {"q": "Does the Sahel instability affect Ghana?", "a": "Ghana's northern borders, particularly with Burkina Faso, have seen increased security incidents in the region. FCDO and State Dept advisories note the risk of terrorist spillover from the Sahel region into northern Ghana. For most corporate visitors operating in Accra and the southern business districts, this is a monitored rather than immediate risk. Operations close to the northern border require specific assessment."},
            {"q": "Is armed protection available in Ghana?", "a": "Armed security is available from licensed Ghanaian operators for appropriate engagements. The Ghana Police Service regulates armed security company licensing. For most corporate visitors to Accra, unarmed close protection and security drivers are appropriate. Armed protection is more typically used for cash-in-transit, high-risk site security in resource sectors, and specific threat situations."}
        ],
        "body": """Ghana is the benchmark stable democracy in West Africa. Two peaceful transfers of power between opposing parties since 2000 demonstrate a political culture that distinguishes Ghana from many neighbours. Accra is the regional headquarters location of choice for many multinationals and international organisations, partly for this reason.

The security environment in Ghana is real, however. OSAC rates Accra crime as high. The contrast with countries like Nigeria should not create complacency. Petty crime, isolated serious crime, and the evolving regional terrorism picture from the Sahel all require ongoing assessment.

## Oil sector security

Ghana's Jubilee offshore oil field and subsequent discoveries have brought a significant energy sector presence. International oil company executives and contractors represent a substantial visitor population. Offshore operations have their own security protocols. Onshore operations in the Takoradi and Western Region area generate EP demand outside Accra.

## NGO and diplomatic community

Accra hosts a large number of embassies, UN agencies, and international NGOs serving the West Africa region. This community generates sustained demand for security drivers, residential security, and close protection for country directors and senior representatives. The NGO security market in Ghana is well-served by experienced operators.

## Northern Ghana risk

The far north of Ghana, particularly the Upper East and Upper West regions bordering Burkina Faso, has seen increased security incidents. Burkina Faso has experienced significant terrorist activity from JNIM and related groups. FCDO and State Dept have flagged this border area as elevated risk. Mining operations in northern Ghana require specific security assessment."""
    },

    {
        "slug": "tanzania",
        "title": "Tanzania",
        "h1": "Security Services in Tanzania",
        "risk_level": "medium",
        "description": "Close protection and executive security in Tanzania. Professional security services in Dar es Salaam and Zanzibar from vetted operators with East Africa experience.",
        "regulations": {
            "firearms": "Licensed security companies can carry firearms with Police and Fire Services permit authority. Armed security is available and used in higher-risk contexts including mining sites and specific EP engagements.",
            "licensing": "Tanzania Security Industry Regulatory Authority (TASIRA) regulates private security under the Private Security Industry Act. Companies must be TASIRA registered. Individual security officers require TASIRA certification. TASIRA has developed a more structured framework than some regional neighbours.",
            "foreign_operators": "Foreign companies must incorporate in Tanzania or partner with a TASIRA-registered Tanzanian company. All personnel require appropriate work permits from the Tanzania Immigration Services Department."
        },
        "cities": [
            {"name": "Dar es Salaam", "slug": "dar-es-salaam", "risk_level": "medium", "summary": "East Africa's largest port city. Moderate crime, particularly at night near the waterfront. Petty theft and carjacking risks. Growing business hub with developing EP market."}
        ],
        "faqs": [
            {"q": "Is Tanzania safe for business travel?", "a": "Dar es Salaam is a functioning business environment with manageable risks for prepared visitors. The State Dept rates Tanzania at Level 2 (Exercise Increased Caution). Petty crime is common in tourist and business areas. Carjacking incidents occur, particularly around the central business district at night. Zanzibar has experienced intermittent security incidents including knife attacks against tourists. Standard security precautions and awareness of high-risk areas manage most risks."},
            {"q": "What are the main security risks in Dar es Salaam?", "a": "Opportunistic theft, bag snatching, and pickpocketing in markets and crowded areas. Carjacking incidents, primarily at night. Confidence scams targeting business visitors. Robbery at ATMs and in hotel environs. The waterfront area and parts of the city centre carry elevated risk after dark. Vehicle-borne travel rather than walking after dark reduces exposure to most common threats."},
            {"q": "Does Tanzania have terrorism risks?", "a": "Tanzania has a terrorism history: the 1998 US Embassy bombing in Dar es Salaam killed 11 people. More recent intelligence indicates threats from al-Shabaab, primarily via the Mozambique route, and domestic radical groups. FCDO notes the risk of politically motivated violence particularly around election periods. The immediate terrorism risk for most corporate visitors is lower than in Kenya or Mozambique, but is not absent."},
            {"q": "What security is appropriate for mining operations in Tanzania?", "a": "Tanzania has significant mining operations (gold, tanzanite, other minerals). Mining sites, particularly in the Lake Victoria zone and Shinyanga region, face specific security challenges including illegal mining incursions, community conflict, and theft of high-value minerals. Security arrangements for mining operations require specialist knowledge of the area and relationships with local authorities. Armed security with TASIRA licensing is standard for mining site protection."}
        ],
        "body": """Tanzania is East Africa's second-largest economy, with Dar es Salaam as the primary commercial hub and gateway to one of Africa's fastest-growing economies. The port, financial sector, tourism industry, and growing manufacturing base generate a steady stream of corporate visitors.

The security environment is moderate by East African standards. Tanzania lacks the acute threat profile of Kenya's al-Shabaab exposure or the political volatility of neighbouring Uganda. The risks are primarily opportunistic crime, carjacking, and the evolving regional threat picture from the Mozambique-based Ansar al-Sunna insurgency.

## Zanzibar: a separate assessment

Zanzibar's security profile diverges from mainland Tanzania. The island has experienced periodic political violence around elections and has seen knife attacks targeting tourists. The population is predominantly Muslim, and Zanzibar has historically had contacts with external Islamist networks. FCDO advises vigilance in Zanzibar specifically, noting that religious festivals can be periods of heightened tension.

## Mining sector security

Tanzania's mining sector, concentrated around the Lake Victoria goldfields, Mirerani tanzanite mines, and various other mineral deposits, generates significant security demand. The Tanzanian Government's ongoing disputes with mining companies over taxation and royalties have periodically created community-level tensions around mine sites. Security arrangements for mining operations require specialist knowledge and coordination with the Tanzania Police Force mining unit.

## NGO and diplomatic security

Dar es Salaam is the base for numerous UN agencies and international NGOs operating in the East and Central Africa region. Security arrangements for these organisations follow donor-mandated security frameworks (UN Department of Safety and Security, InterAction standards) that define minimum requirements for security plans, drivers, and premises."""
    },

    {
        "slug": "ethiopia",
        "title": "Ethiopia",
        "h1": "Security Services in Ethiopia",
        "risk_level": "high",
        "description": "Executive protection and security assessments in Ethiopia. Professional security services in Addis Ababa from vetted operators with experience in complex African environments.",
        "regulations": {
            "firearms": "Ethiopian law restricts firearms for private security. Licensed companies can seek permits through the Ethiopian Federal Police. Practical availability of armed private security is limited. Government security forces accompany foreign diplomats and some high-profile visitors.",
            "licensing": "Private security is regulated by the Ethiopian Federal Police under the Private Security Companies Establishment Proclamation. Companies must register with the Federal Police. The regulatory framework is less developed than East African neighbours such as Kenya.",
            "foreign_operators": "Foreign security companies must establish Ethiopian legal entities or partner with Ethiopian-registered firms. Foreign personnel require Ethiopian work permits. Operations involving foreign security advisors are common in the diplomatic and NGO sectors."
        },
        "cities": [
            {"name": "Addis Ababa", "slug": "addis-ababa", "risk_level": "high", "summary": "Ethiopian capital and African Union headquarters. Internal conflict since 2020 has significantly elevated risk. FCDO advises against travel to multiple regions. Addis itself requires security management."}
        ],
        "faqs": [
            {"q": "What is the current security situation in Ethiopia?", "a": "Ethiopia has experienced significant internal conflict since November 2020, beginning with the Tigray war and subsequently involving Amhara and Oromia regions. The conflict has produced a major humanitarian crisis. FCDO currently advises against all travel to multiple Ethiopian regions including Tigray, parts of Amhara, Afar, and areas near the Eritrean border. Addis Ababa carries a lower advisory level (Exercise Increased Caution) but has experienced periodic protest and security incidents related to the conflict."},
            {"q": "Is Addis Ababa safe for business travel?", "a": "Addis Ababa continues to function as a business hub and hosts the African Union headquarters, African Development Bank offices, and numerous international organisations. Corporate travel to Addis is conducted regularly with appropriate security management. The risks are heightened compared to the pre-2020 period: protest activity, occasional violent incidents, and security checkpoints throughout the city. A current security briefing before arrival is essential."},
            {"q": "What regions of Ethiopia should be avoided?", "a": "FCDO advises against all travel to: Tigray region, Afar region (along the Tigray/Afar border), parts of Amhara region, areas within 100km of the Eritrean border, the Somali/Ogaden region, and areas within 50km of the South Sudan, Sudan, and Kenyan borders. The security situation changes: check the current FCDO advisory and your organisation's security baseline before any travel."},
            {"q": "What security arrangements are standard for Addis Ababa?", "a": "For most international organisations operating in Addis, standard arrangements include vetted security drivers with tracked vehicles, pre-planned routes that avoid areas of known protest activity, 24/7 communication protocols with a security focal point, awareness of shelter-in-place procedures, and regular security briefings. Close protection officers for more exposed individuals and country directors in sensitive organisations is increasingly standard since 2021."}
        ],
        "body": """Ethiopia presents a categorically different risk environment from its pre-2020 status as a stable, if complex, African investment destination. The conflict that began in Tigray in November 2020, subsequently spreading into Amhara and other regions, has fundamentally altered the country's security profile.

For Addis Ababa specifically, the risk has increased but has not reached the levels that apply to conflict-affected regions. The city continues to function. The AU headquarters remains active. Airlines continue to operate through Addis Ababa Bole Airport, which is Ethiopian Airlines' major hub. Business continues.

## FCDO and State Dept advisories

Both FCDO and the US State Dept maintain elevated advisories for Ethiopia, with specific against-all-travel designations for multiple regions. The Addis advisory is at Exercise Increased Caution (State Dept Level 2) rather than higher levels. These distinctions matter for operational planning: the capital remains accessible for essential travel with professional security management.

## NGO and humanitarian operations

Ethiopia is one of the world's largest humanitarian operations. The WFP, UNHCR, ICRC, and dozens of other international organisations maintain significant Ethiopia presence. Security for humanitarian operations in Ethiopia follows UN Department of Safety and Security frameworks and specific incident command structures developed for the conflict context.

## The Addis security market

The private security market in Addis has grown in response to increased demand from the international community since 2020. Operators range from multi-national companies with regional Africa experience to locally founded firms with deep government and police relationships. For operations in Addis, both factors matter: professional standards and local access."""
    },

    {
        "slug": "peru",
        "title": "Peru",
        "h1": "Security Services in Peru",
        "risk_level": "high",
        "description": "Executive protection and security services in Peru. Armed close protection in Lima and mining regions from vetted, SUCAMEC-licensed operators.",
        "regulations": {
            "firearms": "Licensed security companies in Peru can arm personnel under SUCAMEC (Superintendencia Nacional de Control de Servicios de Seguridad, Armas, Municiones y Explosivos de Uso Civil) licensing. Armed EP is available and used for corporate clients. Firearms are registered with SUCAMEC.",
            "licensing": "SUCAMEC regulates all private security. Companies and individual operators require SUCAMEC licensing. The regulatory framework covers guards, close protection, cash transport, and investigation services. Annual compliance required.",
            "foreign_operators": "Foreign companies must establish Peruvian legal entities and obtain SUCAMEC licensing. Foreign nationals require Peruvian work visas. Personnel cannot carry firearms without SUCAMEC operator certification."
        },
        "cities": [
            {"name": "Lima", "slug": "lima", "risk_level": "high", "summary": "Peru's capital and commercial hub. High-severity crime including express kidnapping, carjacking, and robbery. Mature armed EP market. Protest and political instability a recurring factor."}
        ],
        "faqs": [
            {"q": "What are the main security risks in Lima?", "a": "Lima presents serious urban security risks. Express kidnapping (secuestro al paso) is a documented and common crime where victims are taken, forced to withdraw money from ATMs, and released. Carjacking, armed robbery, and taxi-related crime are significant. Miraflores and San Isidro districts carry lower risk than central Lima and peripheral areas. Protest activity is frequent and can turn confrontational. Political instability since 2021 has resulted in multiple presidents, civil unrest, and security incidents."},
            {"q": "Is armed protection standard in Lima?", "a": "For corporate executives and HNWI clients, armed close protection and armoured vehicles are the standard for Lima operations. The threat environment supports this posture. Unarmed protection is the minimum for lower-profile visitors. SUCAMEC-licensed armed operators are available and the quality of operators with former military and police special forces backgrounds is high."},
            {"q": "What is the SUCAMEC and what does it regulate?", "a": "SUCAMEC (Superintendencia Nacional de Control de Servicios de Seguridad, Armas, Municiones y Explosivos de Uso Civil) is Peru's security industry and weapons regulator. SUCAMEC licenses security companies, individual operators, and controls civilian firearms. A current SUCAMEC licence is the baseline verification for any Peruvian security provider. Without it, the operator is working illegally regardless of credentials claimed."},
            {"q": "How does Peru's political instability affect security?", "a": "Peru has had six presidents in six years, including the 2022 attempted self-coup by Pedro Castillo. Political protests regularly disrupt Lima and major cities, and the Andes highway network has been blockaded by demonstrations affecting operations in mining regions. Corporate travel planning in Peru must account for protest calendar and political risk alongside conventional security threats."}
        ],
        "body": """Peru is a significant Latin American economy with a large mining and natural resources sector that attracts substantial international investment and executive presence. Lima, Arequipa, and the Andes mining regions all generate security requirements.

The Lima threat environment is serious. OSAC rates Lima crime as critical. Express kidnapping, armed robbery, and carjacking are documented daily occurrences affecting business visitors. The districts matter: Miraflores and San Isidro, where most hotels and corporate offices concentrate, carry lower risk than other parts of the city. But complacency within these districts is a documented risk - crime follows expatriate patterns.

## Mining and extraction sector

Peru's mining sector concentrates in the Andes. Copper, gold, silver, and zinc operations involve significant international executive presence. Security for mining operations in Peru involves both site security (community relations, anti-incursion) and executive transport along mountain highway routes that have been targets for both criminal activity and protest blockades.

## Protest management

Peru's political culture includes a strong protest tradition. The transport network - particularly the Pan-American Highway and Andes routes - has been blockaded multiple times in recent years. Operations in Peru require protest monitoring and contingency routing as standard components of the security plan.

## SUCAMEC compliance

SUCAMEC licensing is non-negotiable for any security operation in Peru. The regulator is active and enforcement is real. Companies operating without current SUCAMEC authorisation face fines, asset seizure, and prosecution. Verifying SUCAMEC licence status before engaging any Peruvian operator is mandatory."""
    },

    {
        "slug": "argentina",
        "title": "Argentina",
        "h1": "Security Services in Argentina",
        "risk_level": "medium",
        "description": "Executive protection and private security in Argentina. Professional close protection in Buenos Aires from vetted, registered operators with local operating experience.",
        "regulations": {
            "firearms": "Armed security is available in Argentina for licensed companies. The Registro Nacional de Armas (RENAR) oversees civilian firearms. Security companies can arm personnel with proper documentation. Argentina has an active armed EP market particularly for corporate and political clients.",
            "licensing": "Private security is regulated at provincial level as well as national level. The Ministry of Security (national) sets standards. Buenos Aires Province and City have their own licensing authorities. Companies must be registered at the relevant level for their jurisdiction.",
            "foreign_operators": "Foreign companies must establish Argentine entities and comply with licensing requirements. Foreign personnel require Argentine work authorisation. National security law may require government notification for certain security contracts."
        },
        "cities": [
            {"name": "Buenos Aires", "slug": "buenos-aires", "risk_level": "medium", "summary": "Argentina's capital and financial hub. Moderate crime with economic crisis context. Express kidnapping risk. Politically active with regular protest activity. Developed EP market."}
        ],
        "faqs": [
            {"q": "What are the main security risks in Buenos Aires?", "a": "Buenos Aires has a moderate-to-high crime environment shaped by Argentina's economic instability. Express kidnapping (secuestro express) occurs in higher-income neighbourhoods and targets business visitors and HNWI individuals. Armed robbery and vehicle theft are documented. The economic crisis context of recent years has correlated with property crime increases. Political protest is frequent and sometimes large-scale."},
            {"q": "Is Argentina's economic crisis a security factor?", "a": "Argentina's prolonged economic difficulties, including multiple currency crises and IMF interventions, have increased financial desperation and correlate with property crime increases. For visiting executives, the practical implication is heightened awareness of ATM use, cash handling, and conspicuous wealth display. The economic context also affects security operator quality: economic pressure on legitimate firms has increased informal operators in the market, making vetting more important."},
            {"q": "Do I need close protection in Buenos Aires?", "a": "Most corporate visitors to Buenos Aires do not require close protection. The primary use cases are HNWI individuals with known public profiles, executives involved in high-value transactions where the transaction amount could motivate targeting, entertainment industry principals, and individuals who have received specific threats. A security driver and vetted vehicle for all ground transport is a proportionate baseline for most business visitors."},
            {"q": "What areas of Buenos Aires carry higher risk?", "a": "The Villa 31 and Villa 1-11-14 informal settlements carry elevated risk and should be avoided without specific local knowledge. Parts of La Boca beyond the tourist area of El Caminito carry elevated risk after dark. The outer ring municipalities (conurbano) have significantly higher crime rates than the city centre. Palermo, Recoleta, and the Puerto Madero waterfront district carry the lowest risk within the city."}
        ],
        "body": """Buenos Aires is one of Latin America's most significant business centres and has a well-developed private security market reflecting a long history of political violence, corporate kidnapping, and organised crime.

The security environment has been shaped by cycles of economic crisis and recovery. The most recent severe crisis (2001-2002) transformed the crime landscape, and subsequent crises have had similar effects. The Milei administration's austerity programme (2024 onwards) has had economic impacts that security analysts monitor for crime correlations.

## The kidnapping history

Argentina had one of Latin America's most serious corporate kidnapping problems in the 1970s and 1980s, with major multinational executives specifically targeted. While the acute phase of that era has passed, the institutional memory shapes how Argentine security professionals operate and how corporate security managers assess Buenos Aires. Express kidnapping remains an active methodology.

## Political risk

Argentina's political history includes military dictatorship, hyperinflation, and regular mass protests. The Madres de Plaza de Mayo demonstrations are a weekly fixture. Major economic announcements can trigger large-scale protests in the financial district. Security planning for Buenos Aires should include protest monitoring and route management around government buildings and financial district areas.

## Quality operators

Buenos Aires has excellent close protection operators, many with federal police or military intelligence backgrounds. The SIDE (intelligence service) has historically produced individuals now working in private security who bring significant professional skills. Quality vetting separates this upper tier from the less experienced operators that exist in any mature market."""
    },

    {
        "slug": "chile",
        "title": "Chile",
        "h1": "Security Services in Chile",
        "risk_level": "medium",
        "description": "Executive protection and private security in Chile. Professional close protection in Santiago from vetted operators with South America experience.",
        "regulations": {
            "firearms": "Licensed security companies can arm personnel with Carabineros (national police) authorisation. Armed security is available but less common than in neighbouring Peru or Colombia. Unarmed close protection is more typical for corporate clients in Santiago.",
            "licensing": "Private security is regulated by the Ministry of the Interior under Decree No. 1773. Companies must be registered with Carabineros. Individual operators require Carabineros registration. The regulatory framework is more developed than in some South American neighbours.",
            "foreign_operators": "Foreign companies must establish Chilean entities or partner with registered Chilean firms. All personnel require Chilean work authorisation. Operations must comply with Carabineros oversight requirements."
        },
        "cities": [
            {"name": "Santiago", "slug": "santiago", "risk_level": "medium", "summary": "Chile's capital. Elevated crime post-2019 social unrest. Migration-linked crime increase documented. Protest activity can be significant. Most stable South American business hub."}
        ],
        "faqs": [
            {"q": "Is Chile safer than other South American countries?", "a": "Chile has traditionally been one of South America's safest countries and Santiago remains a business-friendly destination. The security environment worsened after the 2019 Estallido Social (social uprising) and has been affected by migration from Venezuela, Haiti, and Colombia that Chilean security services associate with organised crime increases. Santiago is safer than Lima, Bogota, or Sao Paulo but requires more security awareness than it did before 2019."},
            {"q": "What happened in Chile in 2019 and does it still affect security?", "a": "The October 2019 Estallido Social began as protests against a metro fare increase and escalated into widespread civil unrest that caused 30+ deaths, thousands of injuries, and significant property destruction. The political settlement led to a constitutional process (not finalised as of 2026). The underlying social tensions persist and protest activity, sometimes turning violent, remains a security consideration particularly in Plaza Italia/Plaza Baquedano and around the central business district."},
            {"q": "What are the main crime risks in Santiago?", "a": "Theft, mugging, and bag snatching are common in the city centre and tourist areas. Express kidnapping has occurred but is less prevalent than in Lima or Bogota. Vehicle break-ins in tourist areas. Home invasions and robbery have increased in Santiago's wealthier residential areas. Public transport (Metro) is generally safe but with pickpocket awareness needed. Nightlife safety has been affected by date rape drug incidents."},
            {"q": "What is the copper mining security environment?", "a": "Chile's copper mining industry in the Atacama and Antofagasta regions involves significant executive presence from mining majors (BHP, Rio Tinto, Codelco). Security for mining operations typically involves a corporate security programme rather than individual close protection. The main risks in mining regions are labour disputes, community opposition, and organised theft of copper. The northern desert region has a different risk profile from Santiago."}
        ],
        "body": """Chile remains one of South America's most institutionally stable countries. The legal system functions, Carabineros de Chile (national police) are relatively reliable, and corruption is lower than regional neighbours. Santiago is the continent's most economically developed capital and the regional headquarters choice for many companies.

The post-2019 security deterioration is real and has continued into the mid-2020s. Rising violent crime, gang activity from organised migrant criminal networks, and the lingering effects of political polarisation from the constitutional process all represent changed conditions compared to Chile's earlier reputation as a regional safe haven.

## Organised crime and migration

Chilean law enforcement has documented the growth of Venezuelan, Colombian, and other migrant-origin criminal organisations particularly in the Atacama Norte region and Santiago's peripheral municipalities. The Tren de Aragua (Venezuelan gang) and similar organisations have established Chilean operations. This organised crime growth represents a different threat vector from Chile's historically petty-crime-focused security environment.

## Mining operations security

Chile's mining industry, primarily in the north, involves different security considerations from Santiago corporate operations. Labour relations, community opposition to mining expansion, and the remote logistics of Atacama region operations all require specialist assessment. Mine site security typically uses company security programmes rather than external close protection.

## Business security in Santiago

For most corporate operations in Santiago, the practical security measures are: vehicle security (no unattended vehicles in public areas), awareness of protest calendar and avoidance of demonstration areas, hotel security protocols, and personal awareness in tourist zones and central areas. Close protection is appropriate for HNWI individuals and executives with specific threat indicators."""
    },

    {
        "slug": "israel",
        "title": "Israel",
        "h1": "Security Services in Israel",
        "risk_level": "high",
        "description": "Executive protection and security assessments in Israel. Professional close protection in Tel Aviv from vetted operators with IDF-trained personnel.",
        "regulations": {
            "firearms": "Israel has a relatively permissive firearms environment compared to European countries. Security companies can arm personnel. Many Israeli security professionals have served in IDF or Israeli police and hold personal firearms. Armed close protection is standard for higher-risk engagements.",
            "licensing": "The Ministry of Interior regulates private security under the Private Investigation and Security Services Law. Security companies require Ministry of Interior licensing. Close Protection is a specific licence category. Individual operators must be licensed. Israeli security professionals are internationally regarded for their IDF and Shin Bet background.",
            "foreign_operators": "Foreign security companies face restrictions on independent operation. Israeli partnerships are standard. Many major international security companies maintain Israeli-linked operations. Foreign nationals operating security functions require Israeli work authorisation."
        },
        "cities": [
            {"name": "Tel Aviv", "slug": "tel-aviv", "risk_level": "high", "summary": "Israel's commercial and tech hub. Active terrorism threat from Gaza, West Bank, and Hezbollah. October 2023 Hamas attack fundamentally changed the regional security context. Current FCDO advisory: do not travel to Gaza; exercised caution elsewhere."}
        ],
        "faqs": [
            {"q": "What is the current security situation in Israel?", "a": "The October 7, 2023 Hamas attacks killed approximately 1,200 Israelis and led to an ongoing military operation in Gaza and military exchanges with Hezbollah in Lebanon. Israel is in a sustained conflict state. The regional security environment as of April 2026 remains elevated. Tel Aviv's civilian security environment differs from border areas: the city functions but air raid sirens, mandatory shelter protocols, and elevated general tension are part of daily life. Check FCDO and State Dept advisories immediately before any travel as the situation continues to evolve."},
            {"q": "Is Tel Aviv safe for corporate travel?", "a": "Tel Aviv continues to function as Israel's business hub. Many international companies maintained or restored operations after the initial disruption post-October 2023. The practical risks are rocket/missile alerts (the Iron Dome intercepts most but not all), the possibility of escalation affecting commercial aviation, and the elevated general security environment. Risk tolerance is a decision for individual companies and their duty-of-care frameworks. A current security assessment before any travel is mandatory."},
            {"q": "What makes Israeli security professionals distinctive?", "a": "Israel has a mandatory military service system, and many security professionals have served in IDF combat units, Sayeret Matkal (special forces), or Israeli intelligence (Shin Bet, Mossad). This produces a professional population with genuine operational experience in high-threat environments. Israeli-trained bodyguards are sought internationally for this background. Several major global security companies have Israeli founders or Israeli-trained senior staff."},
            {"q": "What areas of Israel should be avoided?", "a": "FCDO advises against all travel to Gaza, the Gaza border area (within 5km), and the Israel-Lebanon border area (Northern District within 4km of the border). Do not travel to the Golan Heights except via Route 98 and specified areas. Exercise increased caution throughout Israel and the West Bank. The situation changes: the current FCDO Israel page is the authoritative current source."}
        ],
        "body": """Israel's security situation as of 2026 reflects the sustained impact of the October 7, 2023 Hamas attacks. The conflict that began that day has reshaped the regional security environment in ways that affect any assessment of Israeli operations.

Pre-October 2023, Israel maintained a functioning economy with a sophisticated tech sector, strong tourism, and a well-developed close protection industry serving both domestic and international clients. That context has been substantially disrupted.

## The Israeli security industry

Israel exports security expertise globally. Israeli security professionals are found in executive protection operations worldwide, and Israeli companies have significant presence in access control, surveillance technology, and threat assessment markets globally. This professional excellence comes from a national security context that provides genuine operational experience unavailable in most countries.

## Threat environment

The active conflict with Hamas in Gaza, the Hezbollah threat from Lebanon, the expanded drone and missile threat following the 2024 regional escalation, and the West Bank security environment all contribute to an elevated baseline threat. Tel Aviv has experienced rocket attacks, though Iron Dome provides significant but not total protection. The airport has been subject to closure and disruption.

## Corporate operations

Companies with existing Israel operations have typically maintained them with enhanced security protocols including shelter-in-place procedures, communication trees, and contingency plans. New corporate travel to Israel requires current intelligence, clear escalation protocols, and board-level risk acceptance at a threshold most organisations have not previously applied to Israeli travel."""
    },

    {
        "slug": "egypt",
        "title": "Egypt",
        "h1": "Security Services in Egypt",
        "risk_level": "high",
        "description": "Executive protection and security services in Egypt. Professional close protection in Cairo from vetted operators, with specialist assessment for Sinai and North African routes.",
        "regulations": {
            "firearms": "Licensed security companies can carry firearms with Ministry of Interior authorisation. Armed security is available but heavily regulated. Most private security for commercial clients is unarmed. Armed protection for higher-risk engagements requires specific government approvals.",
            "licensing": "Private security is regulated by the Ministry of Interior. Companies require Ministry of Interior licences. Individual guards must be registered. The security industry has significant links to the military and state security apparatus, which affects how the private market functions.",
            "foreign_operators": "Foreign security companies face significant restrictions in Egypt. Operations typically require Egyptian partner organisations. Foreign personnel need Egyptian work permits. The sensitive political environment means foreign security operations attract additional government scrutiny."
        },
        "cities": [
            {"name": "Cairo", "slug": "cairo", "risk_level": "high", "summary": "Egypt's capital and largest Arab city. High crime in tourist and expat areas. Active terrorism risk in Sinai and western desert. State Dept Level 3 (Reconsider Travel) for Egypt overall."}
        ],
        "faqs": [
            {"q": "Is Cairo safe for business travel?", "a": "Cairo continues to function as Egypt's business hub and the Arab world's largest city. The State Dept rates Egypt at Level 3 (Reconsider Travel), driven primarily by the Sinai terrorism situation rather than conditions in Cairo specifically. Cairo's corporate districts (New Cairo, Zamalek, Garden City) operate at a different risk level from Sinai or the Western Desert. A city-specific assessment for Cairo rather than a country-wide application is more accurate for most corporate travel decisions."},
            {"q": "What is the terrorism risk in Egypt?", "a": "Egypt's primary terrorism risk is concentrated in North Sinai (where FCDO and State Dept advise against all travel) and the Western Desert border areas. The Sinai insurgency, linked to Islamic State-Sinai Province (formerly Ansar Beit al-Maqdis), has been suppressed by the Egyptian military but not eliminated. Cairo itself has experienced terrorist attacks in the past (2018 Church bombings, earlier attacks on tourists) but the city-level risk is categorically lower than Sinai."},
            {"q": "What legal risks affect visitors to Egypt?", "a": "Egypt has broad laws on photography of government buildings, military installations, and public infrastructure. Violations are prosecuted. Social media posts critical of the Egyptian government or military can result in detention and prosecution under cyber crime legislation. Drug possession carries severe penalties. Business disputes can result in travel bans. These legal risks require particular awareness for business visitors conducting sensitive commercial activities."},
            {"q": "What is the current regional security context for Egypt?", "a": "Egypt shares borders with Libya (ongoing instability), Sudan (civil war since 2023), and Gaza (active conflict). The Egypt-Gaza border at Rafah has been a significant pressure point since October 2023. Egypt has managed the regional pressures through its security apparatus and diplomatic positioning, but the neighbourhood creates monitoring requirements for any operation close to Egypt's borders."}
        ],
        "body": """Egypt is the Arab world's most populous country and a significant hub for regional business, diplomacy, and cultural engagement. Cairo's 21 million population makes it one of the world's largest metropolitan areas, and its position between Africa, the Middle East, and the Mediterranean gives it strategic importance across multiple sectors.

The security environment in Egypt reflects a country that experienced revolution in 2011, military intervention in 2013, and has since operated under a security-dominated government that has suppressed visible dissent while also suppressing terrorism in Sinai. The result is a Cairo that functions for business while operating under a surveillance-heavy, legally constrained environment.

## Sinai: a separate assessment

North Sinai is a no-go zone. The Egyptian military's ongoing counterinsurgency operations against Islamic State-Sinai Province have significantly reduced attack frequency but not eliminated the threat. FCDO advises against all travel to North Sinai. The South Sinai tourist area (Sharm el-Sheikh, Dahab) carries a different but still elevated risk and should be assessed separately from Cairo.

## Cairo's business environment

Corporate travel to Cairo concentrates on New Cairo (east), Zamalek (island), the Central Business District, and Garden City. These areas have a functioning business infrastructure and are served by established hotels with security protocols. Pickpocketing, scams targeting tourists, and taxi-related incidents are the primary petty crime concerns. Serious violent crime targeting business visitors is less common but has occurred.

## Media and photography

Egypt enforces restrictions on photography of military, police, government, and infrastructure targets broadly. What a visitor might photograph as a tourist can constitute a criminal offence under Egyptian law. Security briefings for Egypt should include specific guidance on photography restrictions."""
    },

    {
        "slug": "morocco",
        "title": "Morocco",
        "h1": "Security Services in Morocco",
        "risk_level": "medium",
        "description": "Executive protection and security services in Morocco. Professional close protection in Casablanca and Marrakech from vetted operators with North Africa experience.",
        "regulations": {
            "firearms": "Private security in Morocco is predominantly unarmed. Firearms are strictly controlled under the Direction Générale de la Sûreté Nationale (DGSN). Armed private security is limited to specific high-value contexts and requires Ministry of Interior authorisation.",
            "licensing": "Private security is regulated by the Ministry of Interior. Companies require official authorisation. Individual security personnel must be trained and certified. The regulatory framework has developed with Morocco's growing business and tourism sectors.",
            "foreign_operators": "Foreign companies must establish Moroccan entities or partner with licensed Moroccan firms. Foreign personnel require appropriate residence and work permits. Operations must comply with DGSN requirements."
        },
        "cities": [
            {"name": "Casablanca", "slug": "casablanca", "risk_level": "medium", "summary": "Morocco's commercial capital. Moderate crime environment. Active counter-terrorism measures. Growing business hub with EU and Gulf investment. Developing EP market."}
        ],
        "faqs": [
            {"q": "Is Morocco safe for business travel?", "a": "Morocco is one of North Africa's most accessible business destinations and has maintained relative stability compared to Libya, Tunisia, and Algeria. State Dept rates Morocco at Level 2 (Exercise Increased Caution). The terrorism threat exists: Morocco's security services have disrupted numerous plots since the 2003 Casablanca bombings and the 2018 murders of two Scandinavian tourists in the Atlas Mountains. Overall, Morocco is a manageable environment for business travel with appropriate security awareness."},
            {"q": "What is the terrorism risk in Morocco?", "a": "Morocco has an active domestic terrorism threat from individuals inspired by Islamist extremism. The BCIJ (Bureau Central d'Investigations Judiciaires) is Morocco's counter-terrorism agency and has a track record of disrupting plots before they materialise. The 2018 Atlas Mountains killings by IS-affiliated individuals demonstrated the threat can reach rural tourist areas as well as cities. Urban terrorism risk in Casablanca and Rabat is present but has been significantly reduced by effective counter-terrorism policing."},
            {"q": "What is Morocco's relationship with the Sahel terrorism problem?", "a": "Morocco's southern border with Western Sahara and the broader Sahel region (Mali, Niger, Burkina Faso) creates a route for weapons and people. Morocco cooperates with Western security services on counter-terrorism intelligence and has disrupted trafficking networks. The Sahel crisis (ongoing since 2012) creates a background flow of radicalised individuals and weapons through the region. This is a monitoring concern rather than an immediate threat to Casablanca or Rabat."},
            {"q": "Is close protection available in Morocco?", "a": "Yes. The EP market in Morocco has developed to serve the growing business, luxury tourism, and film industry sectors. Casablanca and Marrakech both have professional operators. Most operations are unarmed. The quality of operators varies and vetting beyond the regulatory minimum is important. For HNWI individuals visiting Morocco for leisure or business, pre-arrival threat assessment and vetted ground transport are appropriate starting points."}
        ],
        "body": """Morocco has positioned itself as North Africa's most stable and accessible business destination, attracting EU and Gulf investment, film productions, and the expanding tourism sector. Casablanca is the commercial capital and the primary entry point for international business.

The counter-terrorism framework is one of the more effective in Africa. The BCIJ has a demonstrated capacity to disrupt plots, and Morocco's cooperation with French, Spanish, and US intelligence services provides significant reach. This effectiveness does not mean the threat is absent: the 2018 murders of Scandinavian hikers in the Atlas Mountains by IS-affiliated Moroccan nationals demonstrated that the threat from domestic radicalisation is real.

## Regional security context

Morocco's geographic position makes it a transit zone for the Sahel threat environment. The Western Sahara situation (disputed between Morocco and Polisario Front, backed by Algeria) creates a specific regional tension that has blocked the Algeria-Morocco border for decades. Algeria's security situation, including its own terrorism history and the spillover from the Sahel, makes Morocco's eastern border environment a monitoring concern.

## Tourism and HNWI visits

Marrakech, Fes, and the coastal resort areas attract significant HNWI and celebrity traffic. The luxury travel sector in Morocco has grown significantly over the past decade. Close protection for high-profile visitors to Morocco needs to account for both the terrorism background threat and the lower-level crime environment (pickpocketing, scams targeting wealthy visitors) that operates across tourist destinations.

## Film and media productions

Morocco is a major film production location, substituting for Middle Eastern and North African environments in numerous productions. Film security (set security, principal protection for cast and crew, location assessment) is a specific market within the Moroccan security industry. Companies specialising in production security have established Morocco operations."""
    },

    {
        "slug": "ukraine",
        "title": "Ukraine",
        "h1": "Security Services in Ukraine",
        "risk_level": "critical",
        "description": "Security assessments and close protection for essential travel to Ukraine. Expert guidance on operating in an active conflict environment from operators with Ukraine experience.",
        "regulations": {
            "firearms": "In wartime conditions, firearms regulations in Ukraine have been relaxed substantially. Civilian ownership is more permissive than pre-2022. Security companies and armed civilians operate extensively. All armed private security operates within Ukrainian law and coordination with the Security Service of Ukraine (SBU).",
            "licensing": "Pre-war private security licensing frameworks remain nominally in place but wartime conditions have significantly altered operational realities. Many security professionals are serving in territorial defence or Armed Forces of Ukraine. The private security market operates differently from peacetime.",
            "foreign_operators": "Foreign security professionals operating in Ukraine do so under highly complex legal and practical conditions. Coordination with Ukrainian authorities is essential. Many individuals and companies operating in Ukraine do so under humanitarian exemptions or specific governmental agreements."
        },
        "cities": [
            {"name": "Kyiv", "slug": "kyiv", "risk_level": "critical", "summary": "Ukrainian capital under ongoing Russian missile and drone threat. Essential-travel-only destination. Active conflict. FCDO advises against all travel. Security requires specialist warzone competencies."}
        ],
        "faqs": [
            {"q": "Is travel to Ukraine currently possible?", "a": "Travel to Ukraine is possible but FCDO advises against all travel. Commercial flights to Kyiv have not operated since February 2022. Access is by road from Poland, Romania, Moldova, Slovakia, or Hungary, or by train (including the overnight service from Warsaw and Przemysl). The decision to travel to Ukraine requires organisational risk acceptance at board level, a specific justification for the essential nature of travel, and comprehensive security planning by operators with active Ukraine warzone experience."},
            {"q": "What security is needed for essential travel to Ukraine?", "a": "Essential travel to Ukraine requires: operators with genuine warzone experience and current Ukraine knowledge (not peacetime EP professionals), Hostile Environment and First Aid Training (HEFAT) for all personnel, real-time missile and drone alert monitoring, shelter protocols for every location visited, convoy and route protocols, communication redundancy, and emergency extraction planning. The planning burden is categorically different from conventional EP operations."},
            {"q": "Are there humanitarian exemptions for Ukraine travel?", "a": "Humanitarian organisations (UN agencies, ICRC, major NGOs) operate in Ukraine under frameworks developed for the conflict environment. Journalists operate with specific accreditation. Some reconstruction and essential business travel continues. Each category has different protocols and different risk acceptance. Humanitarian operations are subject to UN UNDSS guidance and specific organisation security frameworks that have been developed over three years of conflict operations."},
            {"q": "What is the current threat environment in Kyiv?", "a": "Kyiv is subject to Russian missile and drone attacks that occur irregularly but with sufficient frequency to require daily shelter-in-place awareness. The city's infrastructure, residential areas, and energy systems have been targeted. Air defence systems (primarily Ukrainian-operated Patriot and S-300 batteries supplemented by Western-supplied systems) intercept a significant proportion of incoming weapons but not all. Debris from intercepted missiles has caused civilian casualties. The situation as of April 2026 continues to evolve."}
        ],
        "body": """Ukraine has been in active war with Russia since February 24, 2022, following Russia's full-scale invasion. The conflict is the largest conventional war in Europe since 1945. As of April 2026, the front line runs through eastern and southern Ukraine, but Russian missile and drone attacks affect Kyiv, Kharkiv, Odessa, and other cities throughout the country.

FCDO advises against all travel to Ukraine. This is not a routine Level 3 or Level 4 advisory but reflects an active warzone designation. The advisory is binary for FCDO: all travel, not just border regions.

## Who operates in Ukraine

Despite the advisory, Ukraine has a functioning government, an active humanitarian operation, and significant journalistic presence. Reconstruction contractors, humanitarian workers, diplomatic staff, and journalists all operate in Ukraine under various frameworks. These operations require specialist knowledge and ongoing commitment to safety protocols that go beyond conventional security management.

## Security for reconstruction operations

International reconstruction and donor programmes for Ukraine have security requirements that are significant and growing. As areas are liberated from Russian occupation, assessment and reconstruction operations require security planning that addresses both residual landmine/unexploded ordnance risk and conventional personal security concerns.

## Warzone EP competencies

Operating effectively in Ukraine requires competencies that differ from peacetime EP. Understanding of air defence systems, ability to identify incoming threats, shelter procedures, first aid trauma management (tourniquet application, wound packing), and communication under electronic warfare conditions are all required skills. Not all security professionals have these. Operators must be vetted specifically for warzone operational competence, not general EP credentials."""
    },

    {
        "slug": "lebanon",
        "title": "Lebanon",
        "h1": "Security Services in Lebanon",
        "risk_level": "critical",
        "description": "Security assessments and close protection for essential travel to Lebanon. Expert guidance on operating in Beirut from operators with Lebanon and Middle East experience.",
        "regulations": {
            "firearms": "Lebanon has a permissive civilian firearms environment by Middle Eastern standards. Security companies can arm personnel. The fragmented political and militia environment means effective regulatory enforcement is inconsistent.",
            "licensing": "Lebanon's private security is regulated by the Ministry of Interior under the Private Security Companies Act. The political dysfunction and recent civil crises (2019 economic collapse, 2020 Beirut port explosion) have significantly disrupted regulatory functioning.",
            "foreign_operators": "Foreign companies can establish Lebanese entities. The economic collapse and Hezbollah's political influence create operational complexities beyond the formal licensing framework."
        },
        "cities": [
            {"name": "Beirut", "slug": "beirut", "risk_level": "critical", "summary": "Lebanon's capital. Post-2019 economic collapse and post-2024 Israel-Hezbollah conflict. FCDO advises against all but essential travel. Reconstruction phase beginning but security environment remains elevated."}
        ],
        "faqs": [
            {"q": "What is the current security situation in Lebanon?", "a": "Lebanon has faced compounding crises: the 2019 economic collapse (currency lost 90%+ of value), the August 2020 Beirut port explosion (214 killed), and the September-October 2024 Israel-Hezbollah military conflict which caused significant destruction in southern Lebanon, the Bekaa Valley, and parts of Beirut's southern suburbs. A ceasefire was reached in November 2024. As of April 2026, Lebanon is in a post-conflict stabilisation phase. FCDO advises against all but essential travel. The situation continues to evolve."},
            {"q": "Is Beirut accessible for business travel?", "a": "Beirut's Rafik Hariri International Airport has operated through the crises and resumed normal operations after the 2024 ceasefire. The city functions but at a substantially diminished capacity reflecting economic collapse. The international business community, diplomatic missions, and humanitarian organisations maintain Beirut presences. Essential travel is possible with comprehensive security planning. Check current FCDO and State Dept advisories before any travel decision."},
            {"q": "What parts of Lebanon should be avoided?", "a": "FCDO advises against all travel to: southern Lebanon (south of the Litani River), the Bekaa Valley east of the Litani, Palestinian refugee camps (risk of shooting incidents), and areas within 5km of the Syrian border. Exercise increased caution throughout the rest of Lebanon including Beirut. The southern Beirut suburbs (Dahiyeh) are Hezbollah-controlled territory and present specific risk for Western nationals."},
            {"q": "What reconstruction opportunities exist in Lebanon and what security do they require?", "a": "Lebanon's reconstruction needs are significant following the port explosion, the economic collapse, and the 2024 conflict damage. Reconstruction contractors, engineering firms, and humanitarian programmes are active. Security for these operations requires Lebanon-specific expertise, understanding of the political map (Hezbollah territories, state authority zones, UN peacekeeping areas in the south), and ongoing relationship with local authorities and community leaders."}
        ],
        "body": """Lebanon's position as this decade's most concentrated collection of compounding crises - financial collapse, political paralysis, a mass-casualty port explosion, and a regional military conflict - makes it an outlier even in a region with significant instability.

For security professionals, Lebanon is a case study in operating in a state that has lost much of its institutional functioning. The Lebanese state's authority is contested, Hezbollah operates as a state-within-a-state, the Palestinian refugee camps are outside state control, and the economic collapse has created a population under severe material pressure.

## The Beirut port explosion

The August 4, 2020 explosion (2,750 tonnes of ammonium nitrate) killed 214 people, injured thousands more, and destroyed much of Beirut's port district. The explosion is relevant to current security assessments in two ways: the physical damage and displacement it caused continues to affect the city's geography, and the investigation (which has not concluded) involves complex political sensitivities that affect operating relationships.

## Hezbollah: the operating reality

Any security operation in Lebanon must account for Hezbollah's territorial control in southern Beirut, the Bekaa Valley, and southern Lebanon. This is not optional awareness: operating in areas controlled by Hezbollah without proper liaison is operationally hazardous and potentially legally complex for foreign nationals. Experienced Lebanon operators have established protocols for this reality.

## The reconstruction environment

Lebanese reconstruction creates security requirements that combine conventional EP with community relations management, risk mapping, and complex political navigation. Security professionals operating in Lebanon need Lebanon-specific experience, not generic Middle East or conflict experience. The local knowledge component is unusually important."""
    },

]

def write_country(country: dict) -> None:
    slug = country["slug"]
    path = os.path.join(OUTPUT_DIR, f"{slug}.md")
    if os.path.exists(path):
        print(f"  SKIP (exists): {slug}.md")
        return

    regulations = country["regulations"]
    cities_yaml = ""
    for city in country.get("cities", []):
        cities_yaml += f"""  - name: "{city['name']}"
    slug: "{city['slug']}"
    risk_level: "{city['risk_level']}"
    summary: "{city['summary']}"\n"""

    faqs_yaml = ""
    for faq in country.get("faqs", []):
        q = faq["q"].replace('"', '\\"')
        a = faq["a"].replace('"', '\\"')
        faqs_yaml += f"""  - question: "{q}"
    answer: "{a}"\n"""

    content = f"""---
title: "{country['title']}"
description: "{country['description']}"
slug: "{slug}"
h1: "{country['h1']}"
risk_level: "{country['risk_level']}"
hero_image: "hero.jpg"
regulations:
  firearms: "{regulations['firearms'].replace('"', "'")}"
  licensing: "{regulations['licensing'].replace('"', "'")}"
  foreign_operators: "{regulations['foreign_operators'].replace('"', "'")}"
cities:
{cities_yaml}faqs:
{faqs_yaml}---

{country['body'].strip()}
"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  WROTE: {slug}.md")


if __name__ == "__main__":
    print(f"Writing {len(countries)} country hub pages...")
    for c in countries:
        write_country(c)
    print("Done.")
